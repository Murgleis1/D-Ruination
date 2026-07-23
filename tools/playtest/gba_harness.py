#!/usr/bin/env python3
"""
Dreamstone Ruination - headless GBA play-test harness.

VERIFIED WORKING in this container (Python 3.12, x86-64 Ubuntu 24):
  pip install --break-system-packages stable-retro
`stable-retro` is the maintained fork of the archived openai/retro (gym-retro).
It ships the **mGBA** core - the same emulator the repo owner tests with.
The archived gym-retro 0.8.0 source is NOT worth building: it needs cmake +
capnproto + lua5.1 and targets old Python. stable-retro installs in seconds.

WHAT THIS GIVES YOU
  - load pokeemerald.gba, step frames, press buttons
  - 160x240x3 uint8 framebuffer per frame (exact GBA resolution)
  - get_state()/set_state() save states (~397 KB) -> jump straight back to a
    scene instead of replaying the intro every time. THIS is what makes
    iterating on a cutscene practical.
  - screenshots + contact sheets to hand to the user via present_files

WHAT IT DOES NOT GIVE YOU
  The assistant's image/view tool has been BLIND for this whole project: it
  can CAPTURE frames but cannot LOOK at them. So use it for:
    - programmatic checks (see assertions below): did the scene advance? did a
      battle start? is the screen static (softlock)? is there sprite garbage?
    - producing filmstrips for the USER to eyeball in one go
  Do NOT claim a screen "looks right" - you cannot see it. Ask the user.

USAGE
    from gba_harness import GBA
    g = GBA('/path/to/pokeemerald.gba')
    g.run(600)                 # boot + intro
    g.tap('START'); g.run(120)
    g.save('/tmp/shot.png')    # then present_files it
    st = g.state()             # checkpoint
    ...
    g.restore(st)              # replay from checkpoint after a rebuild
"""
import numpy as np
from PIL import Image, ImageDraw

BTN = ["B", None, "SELECT", "START", "UP", "DOWN", "LEFT", "RIGHT", "A", None, "L", "R"]

class GBA:
    """GOTCHA: stable-retro allows ONE emulator instance PER PROCESS. Creating a
    second raises "Cannot create multiple emulator instances per process". If you
    need a fresh emulator, do it in a subprocess (see checkpoint()/replay below)."""
    def __init__(self, rom):
        import warnings; warnings.filterwarnings('ignore')
        from stable_retro import RetroEmulator
        self.em = RetroEmulator(rom); self.f = 0

    def _mask(self, buttons):
        a = [0]*12
        for b in buttons: a[BTN.index(b)] = 1
        return a

    def run(self, frames, *buttons):
        m = self._mask(buttons)
        for _ in range(frames):
            self.em.set_button_mask(m, 0); self.em.step(); self.f += 1
        return self

    def tap(self, button, hold=8, gap=12):
        return self.run(hold, button).run(gap)

    def walk(self, direction, tiles=1, frames_per_tile=17):
        """Overworld movement: ~17 frames per tile at normal walking speed."""
        return self.run(tiles*frames_per_tile, direction)

    def frame(self):  return np.asarray(self.em.get_screen())
    def state(self):  return self.em.get_state()
    def restore(self, st): self.em.set_state(st); self.em.step(); return self

    def save(self, path, scale=3):
        Image.fromarray(self.frame()).resize((240*scale,160*scale), Image.NEAREST).save(path)
        return path

    # ---------------- programmatic checks (usable while blind) --------------
    def stats(self):
        a = self.frame().reshape(-1,3)
        return dict(frame=self.f, colours=int(len(np.unique(a,axis=0))),
                    mean=[round(v,1) for v in a.mean(0)], std=round(float(a.std()),1))

    def is_black(self, thresh=8):
        return self.frame().mean() < thresh

    def changed_over(self, frames=60, thresh=1.5):
        """True if the screen is animating. False => static screen / softlock."""
        a = self.frame().copy(); self.run(frames)
        return float(np.abs(self.frame().astype(int)-a.astype(int)).mean()) > thresh

    def garbage_score(self):
        """Heuristic for corrupted sprites/tiles: legit GBA scenes use a limited
        palette in coherent blocks. High per-8x8-block colour variety across many
        blocks suggests garbage (this is what the Osrid 'confetti' looked like).
        Compare against a known-good baseline rather than an absolute number."""
        a = self.frame()
        blocks = []
        for y in range(0,160,8):
            for x in range(0,240,8):
                b = a[y:y+8, x:x+8].reshape(-1,3)
                blocks.append(len(np.unique(b,axis=0)))
        blocks = np.array(blocks)
        return dict(mean_colours_per_block=round(float(blocks.mean()),2),
                    pct_blocks_over_12=round(float((blocks>12).mean()*100),1))

def contact_sheet(frames_with_labels, out, scale=2, cols=3):
    """frames_with_labels: [(label, HxWx3 array, frame_no), ...]"""
    W,H = 240*scale, 160*scale
    rows = (len(frames_with_labels)+cols-1)//cols
    sheet = Image.new('RGB',(cols*(W+8)+8, rows*(H+30)+8),(22,22,28))
    d = ImageDraw.Draw(sheet)
    for i,(lab,fr,fn) in enumerate(frames_with_labels):
        x = 8+(i%cols)*(W+8); y = 8+(i//cols)*(H+30)
        sheet.paste(Image.fromarray(fr).resize((W,H),Image.NEAREST),(x,y))
        d.text((x+2,y+H+6), '%s  (frame %d)'%(lab,fn), fill=(255,220,120))
    sheet.save(out); return out


# ---------------------------------------------------------------------------
# CHECKPOINTS - the thing that makes iterating practical
# ---------------------------------------------------------------------------
# Save states are ~397 KB raw / ~42 KB gzipped and round-trip EXACTLY across
# separate processes (verified: frame diff 0.00). Drive to a scene once, save a
# checkpoint, then re-test that scene after every rebuild without replaying the
# intro. Store them next to the repo, NOT in /tmp (sandboxes reset).
import gzip, os

def save_checkpoint(g, path):
    with gzip.open(path, 'wb') as f:
        f.write(g.state())
    return path

def load_checkpoint(g, path):
    with gzip.open(path, 'rb') as f:
        g.restore(f.read())
    return g

# ---------------------------------------------------------------------------
# REGRESSION CHECK - run a fixed input script, compare against a stored baseline
# ---------------------------------------------------------------------------
# This is the single most useful blind workflow: it catches "I fixed the lab and
# silently broke the intro" without anyone playing the game.
def frame_signature(a):
    """Cheap, stable fingerprint of a frame - compare across builds."""
    a = np.asarray(a)
    return dict(mean=[round(float(v),2) for v in a.reshape(-1,3).mean(0)],
                colours=int(len(np.unique(a.reshape(-1,3),axis=0))),
                std=round(float(a.std()),2))

def compare_runs(sig_a, sig_b, tol_mean=1.0, tol_colours=8):
    """Returns list of human-readable differences between two signature lists."""
    out = []
    for i,(x,y) in enumerate(zip(sig_a, sig_b)):
        dm = max(abs(p-q) for p,q in zip(x['mean'], y['mean']))
        dc = abs(x['colours'] - y['colours'])
        if dm > tol_mean or dc > tol_colours:
            out.append('step %d: mean delta %.2f, colour delta %d' % (i, dm, dc))
    return out
