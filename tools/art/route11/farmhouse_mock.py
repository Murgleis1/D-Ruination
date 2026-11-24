"""Route 11's farmhouse, inside (stage 1: the look; user 2026-11-24: "Route 11's farmhouse will need some kind of
interior next"). The farmhouse outside is Crown's thatched cottage (its seaside farm village, map 3.1, cells 12..18 x
9..12; route11_v2.py), door at Route 11 (55, 14). Crown's own interior for that cottage (map 5.1, warp 0: the room at
its cells 11..19 x 0..8) is the base: stone back wall, plank floor, the stone hearth, pantry crates, dresser, bed,
table and chairs, the round tub. Made a farmhouse with Pokemon Odyssey's barn (map 30.0): hay bales stacked in a
corner, loose straw on the boards, barrels; its farm's pitchfork (Route 11's piece) leant by the hay.
Two variants: A with Crown's hearth (a farm kitchen); B without one (as Pelluca's houses, user 2026-11-19), the bed
and a cot for the family where the hearth stood.
Kit and room: houses_mock.Room (Crown's cottage pair, map group 4 #1; credit Blah and the Crown team, with
permission; Odyssey's pieces credit the Pokemon Odyssey team).
Usage: ODYSSEY_ROM=/home/claude/crown/Crown.gba python3 tools/art/route11/farmhouse_mock.py [outdir]"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw
os.environ.setdefault('ODYSSEY_ROM', '/home/claude/crown/Crown.gba')
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(HERE, '..', 'houses'))
import houses_mock as HM

HEARTH = ((0x96, 0x97), (0x8E, 0x8F), (0x62, 0x63))     # Crown's stone chimney breast and fire (wall rows 0-2)
CRATES = ((0xE1,), (0x65,))                             # its slatted pantry crates (rows 1-2), one column each
DRESSER = ((0x95,), (0x1B,))
TUB = 0x24                                              # (its round wooden tub)
def png(path):
    a = np.array(Image.open(os.path.join(ROOT, path)).convert('RGBA')); return a[..., :3], a[..., 3] > 0
HAY = lambda: png('assets/odyssey_reference/pieces/barn_hay.png')
STRAW = lambda: png('assets/odyssey_reference/pieces/barn_straw.png')
OBARREL = lambda: png('assets/odyssey_reference/pieces/barn_barrel.png')
FORK = lambda: png('assets/route11_reference/pieces/odyssey_pitchfork.png')
CRATE = lambda: png('assets/crown_reference/pieces/crate.png')

def hay_corner(r, x0, y0, cells):
    for (dx, dy) in cells: r.paste(HAY(), (x0 + dx) * 16, (y0 + dy) * 16, solid={(x0 + dx, y0 + dy)})

def farmhouse(variant='A'):
    r = HM.Room(13, 10, windows={2, 9, 10} if variant == 'A' else {2, 5, 6, 10}, mat_x=5)
    # the back wall: pantry crates and the dresser on the left
    r.block(CRATES, 1, 1, solid_rows={1}); r.block(CRATES, 2, 1, solid_rows={1}); r.block(DRESSER, 3, 1, solid_rows={1})
    if variant == 'A':
        r.block(HEARTH, 5, 0, solid_rows={2})                       # (the hearth, its fire at the wall's foot)
        r.block(HM.BED, 8, 3)
        r.block(((TUB,),), 11, 3)
    else:
        r.block(HM.BED, 6, 3); r.block(HM.BED, 9, 3)                 # (the farmer's bed and the children's)
    r.block(HM.TABLE, 2, 5)                                         # table and chairs, the middle of the house
    # the farm's corner: hay stacked by the door, straw on the boards, the pitchfork leant on the hay, barrels
    hay_corner(r, 9, 6, [(1, 0), (2, 0), (1, 1), (2, 1)] if variant == 'A' else [(1, 0), (2, 0), (2, 1)])
    r.paste(FORK(), 9 * 16 + 6, 6 * 16, solid={(9, 7)})
    for (x, y) in ((8, 7), (6, 5), (10, 8) if variant == 'B' else (7, 3)): r.paste(STRAW(), x * 16, y * 16)
    r.paste(OBARREL(), 1 * 16, 7 * 16, solid={(1, 8)}); r.paste(CRATE(), 2 * 16, 8 * 16, solid={(2, 8)})
    return r

def main(outdir):
    shots = []
    for v in ('A', 'B'):
        r = farmhouse(v); img = r.render()
        Image.fromarray(img).save(os.path.join(outdir, 'farmhouse_%s.png' % v)); shots.append((v, r, img))
    W = sum(s[2].shape[1] * 3 + 20 for s in shots); H = max(s[2].shape[0] * 3 for s in shots) + 24
    sh = Image.new('RGB', (W, H), (24, 22, 28)); d = ImageDraw.Draw(sh); x = 0
    for v, r, img in shots:
        sh.paste(Image.fromarray(img).resize((img.shape[1] * 3, img.shape[0] * 3), Image.NEAREST), (x, 22))
        d.text((x + 4, 4), 'Variant %s: %s' % (v, 'with the hearth (a farm kitchen)' if v == 'A' else 'no hearth (two beds)'), fill=(255, 230, 160))
        x += img.shape[1] * 3 + 20
    sh.save(os.path.join(outdir, 'farmhouse_mock_v1.png'))

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/tmp')
