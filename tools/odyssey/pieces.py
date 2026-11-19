"""Pokemon Odyssey pieces at tile level, for our builders (2026-11-19).

Every piece is an object layer: a list of 4 (8x8 tile of palette indices, flips baked in) plus the palette it
uses. Builders copy the tiles into their tileset, point them at a free palette slot holding that palette, and
lay the quad in a free layer above an existing metatile of ours (`overlay`), so our wall/floor shows around it.

  hearth  Odyssey's brick hearth (fireplace hall 0x8319414), 3x3: its top layer (chimney, mantel, brick
          surround) + the firebox from the bottom layer with Odyssey's stone-floor colours cleared.
          Palette recoloured to ours (compose_mock.HEARTH_PAL: muted brick, parchment stone, brown outlines).
  plate   a plate of food (same map, metatile 712, top layer).
  rustic  barn pieces (0x871F950): hay bale 642, straw 649, stool 650, barrel 648 (top) / 656 (bottom),
          plank table 643 644 / 651 652.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'monomyth', 'dormitory')); sys.path.insert(0, os.path.join(HERE, '..', 'monomyth'))
import numpy as np
import frlib, frrender as FR
import compose_mock as CM

FIRE, RUST = CM.FIRE, FR.TS(frlib.layout(0x0871F950))
HEARTH_PAL = CM.HEARTH_PAL
PLATE_PAL, RUSTIC_PAL = list(FIRE.pal[8]), list(RUST.pal[8])

def _tile(ts, v):
    t = ts.tile(v & 0x3FF).copy()
    if v & 0x400: t = t[:, ::-1]
    if v & 0x800: t = t[::-1, :]
    return t

def top_layer(ts, mid, slot):
    e = ts.ents(mid)
    assert all(v >> 12 == slot or not (v & 0x3FF) for v in e[4:8]), (mid, [v >> 12 for v in e[4:8]])
    return [_tile(ts, v) for v in e[4:8]]

def hearth(dx, dy):
    m = CM.HEARTH[dy][dx]; e = FIRE.ents(m)
    if (dx, dy) == CM.FIREBOX:
        out = []
        for v in e[0:4]:
            assert v >> 12 == 7
            t = _tile(FIRE, v); t[np.isin(t, CM.FLOOR_IDX)] = 0; out.append(t)
        assert not any(v & 0x3FF for v in e[4:8]) or all(not _tile(FIRE, v).any() for v in e[4:8])
        return out
    return top_layer(FIRE, m, 7)

def plate(): return top_layer(FIRE, CM.PLATE, 8)
def rustic(mid): return top_layer(RUST, mid, 8)

def overlay(entries, quad_entries, is_empty):
    """Put an object quad in the lowest free layer above everything already drawn in a 12-entry metatile.
    is_empty(v) says whether an entry draws nothing (tile 0, or a blank filler tile)."""
    e = list(entries)
    used = [k for k in range(3) if not all(is_empty(v) for v in e[k * 4:k * 4 + 4])]
    k = (max(used) + 1) if used else 0
    assert k < 3, 'no free layer above the existing art'
    e[k * 4:k * 4 + 4] = quad_entries
    return e

# ---- a lit fire for the hearth (user 2026-11-19: "have the fireplace lit in the tavern") ----
# MonoMyth's fire animation (4 frames, 16x24: flames over logs, transparent background), the one burning in
# its small fire rooms (map 0x8869380; frames 0x8966278, tiles 258-263 of primary 0x87314AC, palette 2).
# Shown inside the hearth's firebox: logs at the bottom of the opening, clipped to the dark interior
# (index 13 of the firebox piece) so the brick, mantel and grate bars stay in front.
import struct as _struct
from romlib import ROM as _MM, off as _moff
from render import TS as _MMTS
from headers import load as _load
_H, _ = _load()
FIRE_ANIM_PAL = list(_MMTS([h for h in _H if h['addr'] + 0x08000000 == 0x8869380][0]['layout']).pal[2])
FIRE_ANIM_FRAMES = 0x8966278
FIRE_DY = 12 - 20                                       # bottom of the logs (fire row 20) rests on the grate (firebox row 12)

def fire_frames():
    out = []
    for i in range(4):
        f = _struct.unpack_from('<I', _MM, _moff(FIRE_ANIM_FRAMES) + 4 * i)[0]
        a = np.frombuffer(_MM[_moff(f):_moff(f) + 32 * 6], np.uint8).reshape(6, 32)
        t = np.zeros((6, 8, 8), np.uint8); t[:, :, 0::2] = (a & 15).reshape(6, 8, 4); t[:, :, 1::2] = (a >> 4).reshape(6, 8, 4)
        img = np.zeros((24, 16), np.uint8)
        for k in range(6): img[(k // 2) * 8:(k // 2) * 8 + 8, (k % 2) * 8:(k % 2) * 8 + 8] = t[k]
        out.append(img)
    return out

def lit_firebox():
    """4 frames of a 16x16 fire layer (fire palette, 0 = transparent) for the firebox cell."""
    q = hearth(*CM.FIREBOX); box = np.zeros((16, 16), np.uint8)
    for i, t in enumerate(q): box[(i // 2) * 8:(i // 2) * 8 + 8, (i % 2) * 8:(i % 2) * 8 + 8] = t
    inside = box == 13
    frames = []
    for f in fire_frames():
        layer = np.zeros((16, 16), np.uint8)
        for y in range(16):
            fy = y - FIRE_DY
            if 0 <= fy < 24: layer[y] = f[fy]
        layer[~inside] = 0; frames.append(layer)
    return frames

def as_quad(img16):
    return [img16[(i // 2) * 8:(i // 2) * 8 + 8, (i % 2) * 8:(i % 2) * 8 + 8].copy() for i in range(4)]
