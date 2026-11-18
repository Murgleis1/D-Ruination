"""Title preview: tail swish (only Chien-Pao motion) + wind-driven sky (512 strip, 1 px / SKY_SPEED frames with
sub-pixel cross-fade) + logo glint + Press Start blink.  60 fps.  usage: preview4.py FRAMES OUT [zoom]"""
from PIL import Image
import numpy as np, subprocess, os, sys, pickle
from tail_rig import TAIL
im = Image.open('dr_title.png'); a = np.array(im)
pal5 = (np.array(im.getpalette()[:768]).reshape(256, 3) // 8).astype(np.int32)
if os.path.exists('sky_newcols.npy'):
    for k, r, g, b in np.load('sky_newcols.npy'): pal5[k] = (r // 8, g // 8, b // 8)
bgf = np.load(os.environ.get('BGF', 'bg_filled.npy')); sky_mask = np.load(os.environ.get('SKYMASK', 'mask_sky.npy'))[:48]; strip = np.load(os.environ.get('SKY', 'sky_strip512.npy')); SW = strip.shape[1]
scene = a.copy(); scene[TAIL] = bgf[TAIL]                                   # BG0: body baked in, tail area = background
poses, rl = pickle.load(open(os.environ.get('TAILP', 'tail_poses.pkl'), 'rb')); tseq = np.concatenate([np.full(n, f) for f, n in rl])
on = np.array(Image.open('ps_on.png').convert('RGB')).astype(np.int32); off = np.array(Image.open('ps_off.png').convert('RGB')).astype(np.int32)
ps_mask = (np.abs(on - off).sum(-1) > 30); ps_mask[:95] = False; ps5 = on // 8
logo = np.load('mask_logo_full.npy'); fill = logo & (a == 0)
fy, fx = np.nonzero(fill); U = fx + fy; BAND = (U - U.min()) // 3; NB = BAND.max() + 1
band_c = (np.arange(NB) * 3 + 1 + U.min()).astype(float)
WHITE = np.array([31, 31, 31]); GOLD = np.array([31, 28, 21])
DUR = int(sys.argv[1]); OUT = sys.argv[2]; ZOOM = len(sys.argv) > 3
SKY_SPEED, SHINE_EVERY = 8, 480
def prof(d): return np.maximum(np.clip(1 - np.abs(d) / 7, 0, 1) ** 0.8, np.clip(1 - np.abs(d + 16) / 3.5, 0, 1) ** 0.8)
fg5 = pal5[scene]
os.makedirs('pv4', exist_ok=True)
for t in range(DUR):
    fr = fg5.copy()
    n = t // SKY_SPEED; evb = (t % SKY_SPEED) * 16 // SKY_SPEED; eva = 16 - evb
    A = pal5[np.roll(strip, -(n % SW), axis=1)[:, :240]]; B = pal5[np.roll(strip, -((n + 1) % SW), axis=1)[:, :240]]
    sky = np.minimum(31, (A * eva + B * evb) >> 4); fr[:48][sky_mask] = sky[sky_mask]
    for (x, y), v in poses[tseq[t % len(tseq)]].items(): fr[y, x] = pal5[v]
    if (t % 64) < 40 and not ZOOM: fr[ps_mask] = ps5[ps_mask]
    st = t % SHINE_EVERY; pos = U.min() - 30 + st * 2
    if pos < U.max() + 40:
        k = prof(band_c - pos)[:, None]; cols = np.round(WHITE * (1 - k) + GOLD * k).astype(np.int32); fr[fy, fx] = cols[BAND]
    img = Image.fromarray((fr * 8 + fr // 4).astype(np.uint8))
    img = img.crop((56, 96, 104, 128)).resize((720, 480), Image.NEAREST) if ZOOM else img.resize((720, 480), Image.NEAREST)
    img.save('pv4/%05d.png' % t)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '60', '-i', 'pv4/%05d.png', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '16', OUT], check=True)
print('ok', OUT, os.path.getsize(OUT))
