"""Roof recolour: keep each roof pixel's brightness (the artist's shading) and
give it a new hue/saturation. Grey slate has no hue to rotate, so it is
colourised; saturated roofs are re-hued. GBA 15-bit snapping."""
import colorsys
import numpy as np

def snap(c):
    return tuple(min(248, int(round(v / 8)) * 8) for v in c)

def ramp(colours, hue, sat, vmul=1.0):
    out = {}
    for c in colours:
        _, _, v = colorsys.rgb_to_hsv(*[x / 255 for x in c])
        # darker shades a touch more saturated, highlights a touch less: reads as paint, not tint
        s = min(1.0, sat * (1.15 - 0.3 * v))
        r, g, b = colorsys.hsv_to_rgb(hue, s, min(1.0, v * vmul))
        out[tuple(c)] = snap((r * 255, g * 255, b * 255))
    return out

def apply(img, mask, mapping):
    out = img.copy()
    for src, dst in mapping.items():
        sel = mask & (img == np.array(src)).all(-1)
        out[sel] = dst
    return out


def patch_roof_holes(img, roof, holes):
    """Fill pixels the user wants as roof (dark patches enclosed by roof) from the
    nearest roof pixel in the SAME COLUMN at an even offset: the church's side roofs
    are vertical plank columns, so a column copy keeps the planks continuous."""
    out = img.copy(); H = img.shape[0]
    for y, x in zip(*np.nonzero(holes)):
        v = None
        for d in range(2, H, 2):
            for yy in (y - d, y + d):
                if 0 <= yy < H and roof[yy, x] and not holes[yy, x]:
                    v = img[yy, x]; break
            if v is not None: break
        if v is not None:
            out[y, x] = v
    return out
