"""A dropped silver coin glinting in the sand (the Burglar Egg's trail of clues, 2026-11-27): a 16x16 object.
The coins in the old man's purse are silver ("stamped with the Regent-Queen's face"), so: a small silver disc lying
flat, a darker rim, a glint. Usage: python3 tools/art/pelluca/burglar/coin.py [--write]"""
import os, sys
from PIL import Image
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'codebase/graphics/object_events/pics/misc/dr_coin.png')
PAL = [(115, 197, 165), (40, 40, 56), (96, 104, 128), (160, 168, 184), (208, 216, 228), (248, 248, 255), (120, 96, 72)]
ROWS = [
    "................",
    "................",
    "................",
    "............5...",
    "...........545..",
    "............5...",
    "................",
    "......1111......",
    ".....132241.....",
    "....13244451....",
    "....12344441....",
    "....12233341....",
    ".....122231.....",
    "......1111......",
    "................",
    "................",
]
def main(write):
    im = Image.new('P', (16, 16)); flat = []
    for c in PAL + [(0, 0, 0)] * (16 - len(PAL)): flat += c
    im.putpalette(flat)
    for y, r in enumerate(ROWS):
        for x, ch in enumerate(r): im.putpixel((x, y), 0 if ch == '.' else int(ch))
    path = os.path.abspath(OUT) if write else '/tmp/dr_coin.png'
    im.save(path); print('saved', path)
    im.convert('RGB').resize((128, 128), 0).save('/tmp/dr_coin_x8.png')
if __name__ == '__main__':
    main('--write' in sys.argv)
