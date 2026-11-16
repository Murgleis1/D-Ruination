# Sprite review checklist (every sprite, every pass, BEFORE the user sees it)

Adopted 2026-11-16 at the user's request. Sources: pixel-art-studio's `validations.md` and
`sharp_edges.md` (vendored in `vendor/pixel_art_studio/`, MIT), codixel's "check before you show"
rules (MIT), adapted to GBA hardware and to the lessons of this project.
The user should never be the one who finds a flaw I could have seen.

## The loop
1. **Measure**: `python3 tools/art/review.py OUT.png --mode portrait|battle|overworld
   --prev BEFORE.png --allow <boxes the change is meant to touch> --ref <original art> <MonoMyth ref>
   --sheet SHEET.png`. Any FAIL is fixed before going further.
2. **Look**: read the sheet (zoomed and 1x side by side, next to the original and the reference at the
   same scale). For a beard, mouth or eye, also look at an 8x close-up of that area.
3. **Write the critique**: answer every line below in writing. Verdict: SHIP or FIX (list).
4. **Fix one thing at a time** by a measured step (about half when the user says too much or too
   little, never all the way to the opposite). Re-run from 1. At least two passes before showing.
5. **Show**: numbered or labelled candidates, the reference and the original on the same sheet.
   Never show a version I already know is wrong. Install only after the user approves.

## Hard rules (review.py FAILs)
- [ ] 4bpp: 15 opaque colours + transparent index 0, at most.
- [ ] Art is not cut by the frame (portraits and battle sprites may be cut by the bottom edge only;
      overworld frames by none).
- [ ] **A change touches only what it was meant to.** Every pixel changed outside `--allow` is a bug,
      even when the code ran without errors (2026-11-16: despeckle and palette re-pick nudged
      Baradus's lip; the collar trim deleted beard pixels).
- [ ] A step that changed 0 px did nothing. Find out why.

## Palette and colour
- [ ] No two colours that collapse to the same GBA 15-bit value (a wasted slot).
- [ ] Near-duplicates each earn their slot, or get merged.
- [ ] Skin and material ramps are hue-shifted (shadows cooler, highlights warmer), steps far enough
      apart to read at 1x. Lore colours are respected (Baradus: Yo'aki bronze).
- [ ] Facial hair and dark details on dark skin: check the CONTRAST. A mid-tone that reads on pale
      skin vanishes on bronze (beard v6 lesson).

## Silhouette and readability
- [ ] Reads at 1x, on the in-game background, next to the zoom.
- [ ] No 1-px nubs or holes on the silhouette. No lumps or points on head crowns: the head keeps the
      curve of the original art (crown lessons v4-v7).
- [ ] 3/4 view: far-side features read as smaller and darker, not as missing parts.
- [ ] Each part reads as what it is. A beard must not read as a slash, a tie, a mouth or a collar
      (beard lessons). A moustache over a mouth line reads as an open mouth.
- [ ] Parts that should touch touch, and parts that should be separate have a border (collar vs neck).

## Light and craft
- [ ] One light direction, consistent across parts. No pillow shading, no 1-px bands parallel to the
      outline.
- [ ] Outline: one rule for the whole sprite set; no light pixels on the silhouette edge (outline holes).
- [ ] Every isolated pixel is deliberate (glint, pupil, stud) or removed.
- [ ] Curves step monotonically (1,1,2,3), not 1,3,1. No doubled corners on 1-px lines.
- [ ] **Integer scale only.** Non-integer resampling (e.g. 2/3) breaks the pixel grid and is the
      main source of "blurry and ugly" (pixel-art-studio sharp edge #1).
- [ ] Dithering only where a band meets a band; never on faces or small sprites.

## Faithfulness (this project)
- [ ] It IS the user's character: adapted and cleaned, never replaced by a MonoMyth character or
      recoloured MonoMyth art. Unchanged areas match the original art.
- [ ] Compared with the previous version, the fix lost nothing good.
- [ ] Animation (overworld): walk frames keep the head anchored (bob only), every facing has the change.

## Sprite-specific
- **Portrait (80x80, bottom-right of the text box):** bust bottom-aligned; face size comparable to
  MonoMyth's (about 25 px wide); check all expressions together.
- **Battle front pic (64x64):** check at 1x and 2x; features stay visible against the skin.
- **Overworld (16x32 frames):** check every frame and facing; at this size a detail is 1-3 px, so
  confirm it reads at 1x, or leave it out (user rejected the overworld beard).
