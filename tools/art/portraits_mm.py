"""Dreamstone Ruination portraits rebuilt on MonoMyth bases (user 2026-11-16: "I want MonoMyth's
portrait system ... our portraits are blurry and ugly"; bases approved the same day).

Each character = a MonoMyth expression set (80x80, 16 colours, index 0 transparent) recoloured to
the character: palette entries are swapped by colour (spec keys are colours of the base's palette,
matched within TOL in every expression's palette, so expression sets with slightly different
palettes recolour alike). Shapes, outlines and shading stay exactly as the MonoMyth artist drew
them -- no resampling, no quantisation.

Optional per-character `edit(px, pal)` hooks do region work a palette swap cannot (Osrid's mask).

Run: python3 -I portraits_mm.py MONOMYTH_ROM OUT_DIR [--preview sheet.png]
Writes OUT_DIR/<name>_<expr>.png (indexed, transparency=0), ready for graphics/portraits/.
"""
import os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '../monomyth'))
import mm_portraits as mp

TOL = 14


def C(*v): return tuple(v)


# ---------------------------------------------------------------------------------------------
# Character specs: expressions -> MonoMyth index, recolour {base colour: new colour}
SPECS = {
    'glaive': dict(exprs={'neutral': 97, 'positive': 107, 'negative': 104}, recolour={
        # pink-crimson hair -> deep auburn red (his portrait/front pic red)
        C(200, 72, 104): C(160, 52, 40), C(120, 48, 64): C(96, 30, 24), C(248, 96, 88): C(208, 88, 56),
        C(184, 64, 96): C(136, 44, 34), C(128, 48, 88): C(104, 36, 32),
    }),
    'eden': dict(exprs={'neutral': 113, 'positive': 114}, recolour={
        # light brown hair -> pale blonde
        C(176, 136, 96): C(240, 212, 144), C(112, 80, 56): C(200, 160, 88), C(120, 56, 32): C(150, 104, 56),
    }),
    'kimaris': dict(exprs={'neutral': 115, 'positive': 116, 'smile': 116, 'negative': 117}, recolour={
        # ice-blue hair -> silver
        C(200, 224, 248): C(232, 232, 236), C(136, 168, 216): C(188, 188, 200), C(64, 128, 200): C(140, 140, 156),
        C(64, 88, 144): C(104, 104, 120), C(24, 64, 112): C(60, 60, 76),
    }, edit='kimaris'),
    'ambrose': dict(exprs={'neutral': 274, 'positive': 276, 'negative': 277}, recolour={
        # salmon hair/beard -> vivid orange
        C(192, 88, 72): C(176, 72, 24), C(216, 120, 88): C(216, 104, 32), C(232, 152, 112): C(240, 144, 64),
    }),
    'baradus': dict(exprs={'positive': 316, 'negative': 315, 'anger': 314}, recolour={
        # LORE (user 2026-11-16): his tribe has darker, bronzed skin
        C(232, 176, 144): C(190, 128, 80), C(192, 120, 104): C(152, 94, 58), C(144, 80, 80): C(108, 62, 42),
        C(96, 72, 72): C(76, 50, 38),
    }),
    'cadmus': dict(exprs={'neutral': 9, 'smile': 10}, recolour={
        # tan hat with red band -> his dark purple hat
        C(192, 176, 128): C(92, 64, 124), C(144, 128, 112): C(62, 42, 88), C(200, 80, 64): C(40, 26, 58),
        C(144, 72, 64): C(150, 40, 48),
    }),
}


def recolour(pal, spec):
    pal = pal.copy().astype(int)
    for src, dst in spec.items():
        d = np.abs(pal - np.array(src)).sum(1)
        for i in np.nonzero(d <= TOL)[0]:
            if i: pal[i] = dst
    return pal.astype(np.uint8)


def edit_kimaris(px, pal):
    """MonoMyth's character wears a lightning-bolt hair clip above the head: Kimaris doesn't.
    Bolt = the orange/yellow pixels (and their outline) above the hair's top edge -> transparent."""
    px = px.copy()
    warm = [i for i in range(1, 16) if pal[i][0] > 180 and pal[i][2] < 90]
    hair_top = min(y for y in range(80) for x in range(80) if px[y, x] and px[y, x] not in warm and px[y, x] != 1
                   and y > 0 and all(px[yy, x] not in warm for yy in range(max(0, y - 1), y + 1)))
    bolt = np.isin(px, warm)
    ys, xs = np.nonzero(bolt)
    if len(ys):
        y0, y1, x0, x1 = ys.min() - 1, ys.max() + 1, xs.min() - 1, xs.max() + 1
        region = px[max(y0, 0):y1 + 1, max(x0, 0):x1 + 1]
        region[np.isin(region, warm + [1])] = 0
    return px


EDITS = {'kimaris': edit_kimaris}


def build(rom):
    P = mp.load(rom); out = {}
    for name, spec in SPECS.items():
        for expr, idx in spec['exprs'].items():
            _, px, pal = P[idx]
            pal2 = recolour(pal, spec['recolour'])
            if spec.get('edit'): px = EDITS[spec['edit']](px, pal)
            out[(name, expr)] = (px, pal2, idx)
    return out


if __name__ == '__main__':
    rom, od = sys.argv[1], sys.argv[2]; os.makedirs(od, exist_ok=True)
    res = build(rom)
    for (name, expr), (px, pal, idx) in res.items():
        mp.save_indexed(px, pal, os.path.join(od, f'{name}_{expr}.png'))
    if '--preview' in sys.argv:
        from PIL import Image, ImageDraw
        P = mp.load(rom); S = 2; keys = list(res); cols = 6
        im = Image.new('RGB', (cols * (80 * S + 4), ((len(keys) + cols - 1) // cols) * (80 * S * 2 + 30)), (30, 30, 30))
        dr = ImageDraw.Draw(im)
        for k, key in enumerate(keys):
            px, pal, idx = res[key]; x = (k % cols) * (80 * S + 4); y = (k // cols) * (80 * S * 2 + 30)
            _, bpx, bpal = P[idx]
            for j, (a, b) in enumerate(((bpx, bpal), (px, pal))):
                rgb = b[a]; rgb[a == 0] = (110, 110, 130)
                im.paste(Image.fromarray(rgb).resize((80 * S, 80 * S), Image.NEAREST), (x, y + 14 + j * (80 * S + 4)))
            dr.text((x, y), f'{key[0]} {key[1]} (#{idx})', fill=(255, 255, 0))
        im.save(sys.argv[sys.argv.index('--preview') + 1])
