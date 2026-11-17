# MonoMyth trainer-pic style: measured spec (2026-11-17)

The user asked: "study every trainer backsprite and frontsprite in MonoMyth to get the aesthetics
down better". Every front pic (136) and back pic (11) was extracted and measured.

- Fronts: `tools/monomyth/mm_fronts.py`. References are in `assets/monomyth_reference/trainer_fronts/`.
- Backs: `tools/monomyth/mm_backpics.py`. The data is in MonoMyth's packed container, and the
  game decodes it in the emulator. References are in `assets/monomyth_reference/trainer_backs/`.

The numbers below are medians, with p10 to p90 ranges in brackets. Use them as the acceptance
spec for any Ruination trainer pic.

## Fronts (64x64, all 136)

| metric | MonoMyth | Osrid (current) |
|---|---|---|
| colours used (of 15) | 15 [13 to 15] | 15 |
| figure height | 61 px [54 to 64]; feet on row 62 to 63 | 63 |
| figure width | 44 px [29 to 60] | 55 |
| canvas fill | 32% [22 to 45] | 39% |
| silhouette-edge pixels that are pure black | 50% [33 to 64] | **0%** |
| edge pixels in the 2 darkest colours | 66% [47 to 84] | **7%** |
| outline colour | pure black (0,0,0) in nearly every pic | navy (0,8,27) |
| checker dither (per figure pixel) | 2% [1 to 3] | 1% |
| isolated pixels | 15% [10 to 23] | 11% |

What the zooms show (#37, #90, #131, #30):

- **Outline.** The silhouette has a 1px pure-black outline. On lit top edges (hair crowns,
  shoulders, the lit side of capes) the outline drops to the material's own dark tone
  (selective outline). That is why only about half the edge pixels are black.
- **Interior lines.** These use each material's darkest tone, not black. Black is kept for the
  few separations that must read at 1x: belt over coat, arm over torso, and the cape's inner
  edge.
- **Shading.** Flat cel blocks with 3 tones per material (light, mid, shadow). Shadows are large,
  simple shapes on the side away from the light, and highlights are 1 to 2 px strips on top
  edges. No soft gradients.
- **Dither.** Used sparingly. Small checker patches on large cloth areas (capes, scarves) blend
  two tones of one material. It is never noise.
- **Palette.** About 15 colours, shared across materials (one material's dark tone is often
  another's mid tone). Saturation is moderate and leans warm. The background colour sits at
  index 0.
- **Pose.** Full body in 3/4 view, with feet at the bottom edge. Poses are dynamic but have a
  readable silhouette: one arm gesturing (pointing, open hand, holding a ball) and a wide
  stance. The head is about 1/5.5 of figure height, a slightly heroic and realistic proportion,
  not chibi.
- **Faces.** Small and minimal: 2 to 3 skin tones, eyes 1 to 2 px of dark, mouth 1 to 2 px.
  Masked characters (#10, #74, #82, #90, #139) use the mask as the main shape and keep it flat
  and high-contrast against the hair and clothes.

## Backs (64x64 per frame; 4 frames stacked into 64x256)

| metric | MonoMyth | Osrid (current) |
|---|---|---|
| framing | **3/4 rear bust facing right**, cropped by the bottom and left edges | full body, legs and boots |
| figure top | row 9 [6 to 17]; the bottom row is always filled | row 1 |
| width | 52 px [36 to 63] | 51 |
| black edge pixels | 47% [33 to 68] | 7% |
| lit side | the right side (toward the opponent): L-R luminance -8 | -6.5 |
| frames | 4 (player characters); #9 and #10 have 1 | 4 identical frames |

- **Head.** Large, about 26 to 30 px wide, in the upper centre-right. The face is a 3/4 profile
  on the right edge of the head (cheek, one eye, nose tip, mouth), so the character reads from
  behind.
- **Shoulders and torso.** They fill the bottom 40% and run off the bottom and left edges. Coat
  collars, scarves and straps read as big flat shapes.
- **Throw sequence.**
  - F0: idle.
  - F1: wind-up. The throwing hand comes up behind or beside the head, toward the top left.
  - F2: arm swinging forward and up.
  - F3: follow-through, with the arm extended to the right (pointing at the opponent).
  - The head bobs 2 to 4 px between frames, and the body leans into the throw.
- Outline, shading and palette follow the same rules as the fronts.

## Consequences for Osrid

1. **Front.** The current pic fails the outline rule (0% black edge), which is why it reads as
   mud. The redraw needs a black selective outline, 3-tone cel shading per material, and a mask
   that is flat cream with a black glyph, the brightest value in the figure.
2. **Back.** The current pic is the wrong framing entirely (a full-body figure from behind). The
   redraw is a right-facing 3/4 rear bust: red-orange hair mass, the mask edge visible at the
   right of the head, a dark green scarf and cloak collar, and an armoured shoulder, with a real
   4-frame throw.
3. **Portrait.** The same rules apply at 80x80 (see `assets/portrait_rework/PORTRAIT_REWORK.md`).
   Flatten the soft "AI" gradients into 3 tones per material and restore a consistent dark
   outline.
