"""Hand cleanup of the 2/3 portraits (option C, user 2026-11-16).

The 2/3 resize keeps the user's proportions but, being a 4/3 enlargement of the 48px art, doubles
pixels on a fixed grid: eyes break up or stretch, 1-px lines go uneven. Each fix here is a hand-placed
pixel, written as a small text grid over the 2/3 output so every edit is visible and reviewable.

PATCHES[name] = list of (x0, y0, rows, why): rows are strings; each char is a key of KEY (a colour of
that portrait's own palette), 'x' = transparent, or '.' = leave the pixel alone.  Colours are matched to the nearest entry
of the portrait's palette, so no colour is ever added.
"""
import numpy as np

KEY = {
    # Cadmus (2/3 palette)
    'k': (30, 20, 24),      # hair / outline dark
    's': (183, 139, 108),   # skin in the hat's shadow
    'S': (218, 167, 134),   # skin
    'G': (130, 130, 135),   # eye: grey-blue top lid
    'L': (199, 199, 225),   # eye: lavender white
    'W': (240, 240, 248),   # eye: white highlight
    'R': (114, 27, 45),     # eye: red pupil
    'M': (124, 101, 84),    # eye: mauve iris shadow
    'h': (32, 19, 49),      # hat: dark body
    'F': (96, 83, 70),      # stubble: dark brown
    # Kimaris (2/3 palette)
    'O': (148, 151, 159),   # hair outline
    'C': (184, 187, 195),   # hair shade ring
    'H': (202, 205, 213),   # hair
    # 'x' = transparent (index 0)
}

PATCHES = {
    'cadmus_neutral': [
        # Left eye: the 4/3 grid repeated its bottom row (lavender + white) into y54 -> a dripping
        # streak. The eye keeps your 3 rows; y54 is cheek again.
        (27, 54, ["s..ss"], 'left eye: remove the doubled bottom row'),
        # Right eye: top row was doubled up into the hair (y49), the red pupil doubled (x45-46), and
        # the lower row lost its mauve + lavender. Rebuilt from your master: r0 M L, r1 L R M . W,
        # r2 W M L.
        (47, 49, ["kk"], 'right eye: top row back to hair (was doubled upward)'),
        (46, 51, ["M"], 'right eye: single red pupil, iris shadow beside it'),
        (44, 52, ["WML"], 'right eye: lower row W M L as in the master'),
        (50, 49, ["s", "s", "s"], 'right eye: brown edge is 1 px in the master, the grid made a 2x3 block'),
        # Right brim tip: the side completion ended in a 6-row vertical edge (x75, y31-36) -- a box.
        # Redrawn to taper like the left tip: the top edge eases down to a point at x76 (y32-33), the
        # underside sweeps back to the existing edge at y39.
        (70, 30, ["hhhkk",
                  "hhhhhk",
                  "hhhhhhk",
                  "hhhhhhk",
                  "hhhhhk",
                  "hhhhkx",
                  "hhkkxx",
                  "kkxxx"], 'right brim: tapered tip'),
        (69, 38, ["kkxxx"], 'right brim: underside meets the existing edge'),
        # Chin stubble: your native art is a broken mix -- mostly brown (M) and dark brown (F) with
        # grey flecks (G) about one in four, skin gaps along the top. The grid merged it into flat
        # runs (6 dark-brown in a row). Redrawn by hand in that mix; the jaw-shadow pixels around it
        # are left alone.
        # Hat top (user 2026-11-16: "still looks partly cut off ... round it slightly"): the crown
        # ended in one flat 25-px line (y14) with hard corners. Rounded: the centre rises 2 rows to a
        # 13-px top, stepping 4, 3, 2 px out to the existing corners; filled with the hat's own dark.
        (27, 12, [".........kkkkkkkkkkkkk.........",
                  ".....kkkkhhhhhhhhhhhhhkkkk.....",
                  "..kkkhhhhhhhhhhhhhhhhhhhhhkkk..",
                  "kkhhhhhhhhhhhhhhhhhhhhhhhhhhhkk"], 'hat top: rounded'),
        (32, 71, ["....MGMF...GFMGFF",
                  ".MGFMGMFGFFGFMF..",
                  "...FGMFFGFMF.....",
                  "...MFFGFFMFG....."], 'chin stubble texture'),
    ],
}

# Kimaris: the reconstructed crown widened in 4-px jumps (left x32->28 at y20, right x50->54 at
# y19), so the top 3-4 rows sat on the head like a cap -- the lump the user saw. Rows 15-20 rebuilt so
# the outline widens 3,1,2,1-2,2 px per row from a 10-px top; outline / shade ring / hair as in the rest of his hair,
# the existing strand shading inside the old outline kept. Identical in all four expressions (their
# differences start at y25).
PATCHES['kimaris_neutral'] = [
    (28, 15, [".........OOOOOOOOOO..........",
              "......OO.CCCCCCCCCCOOO.......",
              ".....OCC...........CCCO......",
              "...OOC................COO....",
              "..OCC..................CC....",
              "..CC........................."], 'crown: smooth outline, no cap'),
]
for _e in ('positive', 'negative', 'smile'): PATCHES['kimaris_' + _e] = PATCHES['kimaris_neutral']

# Cadmus's smile differs from neutral only at the mouth (rows 64-68): same fixes, same pixels.
PATCHES['cadmus_smile'] = PATCHES['cadmus_neutral']


def apply(name, idx, pal):
    """idx: 80x80 canvas (0 = transparent, k = pal[k]); pal: (16,3). Returns patched copy + mask."""
    out = idx.copy(); touched = np.zeros(idx.shape, bool)
    for x0, y0, rows, _ in PATCHES.get(name, []):
        for dy, row in enumerate(rows):
            for dx, ch in enumerate(row):
                if ch == '.': continue
                if ch == 'x': k = 0
                else:
                    c = np.array(KEY[ch]); k = 1 + int(np.argmin(((pal[1:].astype(int) - c) ** 2).sum(1)))
                out[y0 + dy, x0 + dx] = k; touched[y0 + dy, x0 + dx] = True
    return out, touched
