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
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'monomyth', 'dormitory'))
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
