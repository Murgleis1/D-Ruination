# Portrait rework (user 2026-11-16: "I want MonoMyth's portrait system ... our portraits are blurry and ugly")

## What MonoMyth does (measured from the ROM, tools/monomyth/mm_portraits.py)
- One portrait = one **80x80** image, 4bpp, LZ77, one raw 16-colour palette, **index 0 transparent**.
- **No frame, no window box**: a head-and-shoulders bust, right-aligned in the canvas, cut flat at
  the bottom. On screen it sits at the **bottom right**, standing on the text box's top edge, over
  the map. The speaker's name is **inline** in the text ("Mom: We love you, River!").
- Every expression, hand gesture and emote mark ("?", heart, sweat, anger) is its own full image:
  495 portraits, ~70 characters, typically 3-10 images each.
- The art is authored AT 80x80: clean 1px dark outlines on the silhouette and every feature, flat
  cel shading with 2-3 tones per material, a deliberate 15-colour budget per portrait.

## Why ours look bad (evidence: ours_engine_vs_source.png)
1. **Not authored at size.** Our 96x96 sources are crops of larger illustrations, downscaled: soft
   edges, staircase jaggies, no consistent outline, muddy mid-tones. No palette fix can repair that.
2. **Conversion bugs in the engine copies** (engine PNG vs _src):
   - Baradus: sunglasses lenses (black) landed on index 0 -> transparent holes.
   - Osrid: outline/edge pixels dropped to transparent -> magenta holes around the silhouette.
   - Glaive: part of an eye became transparent.
   - Cadmus: 14-colour reduction dropped his red eyes and purple collar.
3. **Display.** 96x96 square box at the top-left with a separate nameplate: larger than MonoMyth's
   80x80, framed as a crop instead of a bust, and away from the text it belongs to.

## Plan (pending user choices)
- Engine: 80x80 transparent bust, bottom-right on the text box edge, no box; inline speaker name.
- Art: each principal rebuilt from the closest MonoMyth portrait (permission granted), recoloured
  to the character; identity details (Osrid's mask, Baradus's glasses, Cadmus's hat) as edits on
  top. Expression sets come from the base's own set (neutral/smile/negative/anger/gestures).
- Catalogue: catalogue_000..448.png (every MonoMyth portrait, numbered); candidates_round1.png.

## Decisions (user 2026-11-16)
- APPROVED: MonoMyth's portrait system (80x80 transparent bust, bottom-right on the text box,
  inline speaker name) and rebuilding each principal from MonoMyth bases.
- Bases (assistant's picks, approved): Glaive #97, Ambrose #274, Baradus #314, Kimaris #115,
  Eden #113 (recoloured blonde), Cadmus #7 (hat recoloured purple).
- OSRID: base = the masked man fought at Sunbeached Cliffs: the DARK GREEN BUG MASK (user
  correction) -- overworld sprite #136 (assets/monomyth_ow/mm_ow136_bug_masked_man.png), portraits
  #383-390 (same colours: the OW palette shares 7 exact colours with them). Draft 1 used the
  spiked-helmet man #156 by mistake (kept for reference only). Reworked into Osrid
  (user: "make a better main character sprite for Osrid than the current overworld sprite").
- BARADUS (lore): his tribe has darker, bronzed skin -- portrait AND overworld sprite carry it;
  facial hair, at least a five o'clock shadow.

## Tooling
- tools/monomyth/mm_portraits.py: every MonoMyth portrait from the ROM (catalogue_*.png).
- tools/monomyth/mm_overworld.py: every MonoMyth 16x32 overworld sprite, decoded by the game
  itself under emulation (assets/monomyth_ow/catalogue_ow16x32.png), full 9-frame extraction.

## Status 2026-11-16 (v1 in the game)
- Engine: 80x80 bust at tile rows 4-13 / cols 19-28 on BG0 (palette 13), transparent index 0,
  standing on the text box frame; SPEAKER_NAME_INLINE prints "Name: " at the start of a message
  (src/field_message_box.c). Verified on the cold open (ingame_cadmus_v1.png).
- Art: all 17 registered portraits rebuilt by tools/art/portraits_mm.py from MonoMyth bases
  (portraits_v1_before_after.png). The old 96x96 masters + build_portraits.py (median-cut
  quantiser: the source of the transparent-lens / outline-hole / lost-colour bugs) are retired to
  legacy_96px/.
- Osrid's base is KAKUGO (user-named): MonoMyth's dark green bug-masked hero, ruby visor eyes,
  scarf; OW #136, portraits #383-390. Portrait v1: hood -> dark green, visor plate -> cream mask,
  antennae -> red-orange hair.
- Next: Osrid OW draft 2 review; extra expressions (Eden wave, Kakugo set for Osrid); Baradus's
  round sunglasses if wanted; overworld sprites for the other principals from MonoMyth bases.

## Correction (user 2026-11-16, 12:38): "the portraits and sprites in the game [must] BE what we had
originally ... adapt my art into the MonoMyth system and rebuild them cleanly if necessary, not just
recolor or tweak existing MonoMyth portraits and overworld sprites."
- The MonoMyth-recolour portraits (v1) are withdrawn from the game (kept for reference only in
  mm_recolour_v1/; tools/art/portraits_mm.py is NOT part of the pipeline). Osrid OW drafts 1-2
  (MonoMyth #156/#136) are likewise reference only and were never wired in.
- v2 in the game: the project's own portraits, adapted by tools/art/portrait_adapt.py -- 80x80
  native-scale crop (no resampling), solid edges, index 0 reserved for transparency, accent-
  preserving 15-colour palette. Fixes the lens/outline/eye/collar defects. Engine unchanged
  (MonoMyth placement + inline names).
- Open: our art is a face close-up filling its square, so in game it reads as a square panel, not
  a MonoMyth bust (head + shoulders, transparent around). A true MonoMyth fit needs each portrait
  rebuilt as a bust at MonoMyth's scale -- pending the user's direction.

## v3 (user 2026-11-16: "Rebuild the portraits please") -- in the game
- tools/art/portrait_rebuild.py: each OWN portrait rebuilt as a MonoMyth-scale bust: the master's
  own 15 colours only; 3:2 reduction by dominant-colour vote (no blended colours, ties to the
  darker so lines survive); 1px outline in the darkest NEUTRAL colour; lone-pixel cleanup;
  bottom-aligned, centred, transparent around (rebuilt_v3_before_after.png, ingame_rebuilt_v3.png).
- Osrid (user 2026-11-16, 13:05): his overworld sprite is to be designed on KAKUGO's overworld
  sprite, and his portrait redesigned in MonoMyth's style. Kakugo's portrait = MonoMyth #69/#70
  (brown spiked helmet, ruby goggle eyes, white scarf, dark coat). His overworld sprite has NOT
  been located yet: not among the 211 16x32 / 137 32x32 entries of the main graphics table
  (0x93C0F8), not on the Sunbleached Cliffs map's object list (scripted VAR sprite); his dialogue
  text is compressed, so the script can't be traced from it.

## v4 (user 2026-11-16: "you chopped off part of the top of heads")
- Cause (measured): every master except Osrid's has hair running off its top edge (16-56 opaque px
  on row 0); the rebuild kept the cut, which reads as a chopped head on a free-standing bust.
- Fix: crown() closes each cut with an elliptical cap filled from the hair's own rows mirrored
  upward, restricted to the cut's dominant hair colours (a skin parting on Baradus is excluded),
  then outlined with the rest (rebuilt_v4_busts.png).
- KAKUGO found: Sunbleached Cliffs script `addobject 8` -> applymovement -> trainerbattle (no
  intro) 0x12F; object 8 = graphics id 0xCD. The graphics table really starts at 0x93BF90 (my
  first table base was 90 entries late). Sheet: assets/monomyth_ow/mm_ow_kakugo.png (10 frames).

## v5 (user 2026-11-16, 14:12-14:16)
- Portrait crowns: v4 capped each cut segment separately -> "a lump on its head". Now one dome on
  the cut row (half-width -> 0 over half the half-width), mirrored hair fill, existing art never
  overwritten; Kimaris (cut through an already tapering crown) gets a low dome on the head's width.
  Per-portrait table CROWN in portrait_rebuild.py; checked one by one (rebuilt_v5_busts.png).
- Osrid OW (user: "take Osrid's entire headsprite ... put it on Kakugo's body"):
  tools/art/osrid_ow_transplant.py -- Osrid's head pixels exactly as drawn, seated on Kakugo's
  neck per direction (standing frames), walk frames move the head by each sheet's own bob; Kakugo's
  coat/scarf -> Osrid's tunic greens; exact 15-colour palette (osrid_ow_draft5_*.png). Draft.
- Osrid portrait: Kakugo is a REFERENCE (positioning, shading, colours) only; his portrait stays his
  design, restyled -- in progress (tools/art/osrid_portrait.py, cel posterisation).

## v6 (user 2026-11-16, 14:28) -- in the game
- Crowns: both dome versions read as lumps -- an ellipse leaves its base with vertical sides, so the
  outline pinches where it meets the head's slope. crown() now continues each side at the head's
  measured edge slope plus a gentle quadratic rounding: smooth outline, no pinch, no per-portrait
  table (rebuilt_v6_busts.png).
- Baradus (Yo'aki tribe, bible/09): bronze skin ramp on his portraits (master recolour, same ranks),
  battle sprite (palette entry 1) and overworld sprite (entries 1-2) (baradus_bronze_sprites.png).
- Osrid OW v6 installed: his head on Kakugo's body, his OLD outfit by zone (green collar/scarf, dark
  torso, grey armoured arms, tan hands, dark legs; green cloak from behind), the old sheet's own
  colours; original kept at legacy_96px/osrid_ow_original.png (ingame_osrid_ow_v6.png).

## v7 (user 2026-11-16, 14:34)
- "A weird slight pointiness on many heads": the slope-continued crown met the steep, already
  CURVING outline at the cut (measured: Eden narrows ~1.3 px/row/side) and closed as a peak.
  crown() now FITS the head's own curvature -- half-width^2 as a quadratic in y (an ellipse) over the
  9 rows under the cut -- and extends it until it closes: round, the head's own curve
  (crowns_v7_vs_originals.png: originals above, rebuilds below; rebuilt_v7_busts.png).
- Baradus battle sprite: pixels were untouched, but his features (mouth, goatee, jaw shading) are
  palette entry 2 (71,60,57), which vanished against the bronze skin. Skin (166,110,72) and feature
  colour (42,24,18) now keep the original's contrast (baradus_front_face_fix.png).

## Baradus beard v8 (2026-11-16)
Rejected: strands drawn up from the jaw (read as a black slash; on the battle sprite a dangling tie).
Rebuilt from a pixel study of MonoMyth #351: the beard is the jaw outline grown thick -- 2 solid rows
at the chin bottom, 2 rows of strands (dark with skin gaps), a row of flecks, filling the whole chin V;
the moustache covers the upper lip (mouth row + 1 above, drooping wider), lower lip still visible.
Beard and moustache use his hair black: no new palette entries. Jaw is identical in all three
expressions, so one pattern fits; expression creases and the anger teeth are untouched.
Images: baradus_beard_v8_cmp.png, baradus_beard_v8_chin.png. Sprites wait for portrait approval.

## Baradus v10 -- APPROVED by user (2026-11-16)
- Chin beard kept (v8 construction). Moustache REMOVED: user wants his mouth and nose exactly as
  originally drawn. Verified pixel-exact: nothing above native row 36 differs from the unedited build
  except two sideburn px at the ear (32,34),(31,35).
- Collar flap beside the chin trimmed down (MASTER_TRIM), outline step borders the new top edge;
  the uncovered area under the jaw is his neck in shadow (TRIM_FILL), outside the silhouette is bg.
- Pipeline guarantee added: protect() restores every pixel outside a drawn edit's footprint from the
  unedited build (palette re-pick + despeckle had nudged his lower lip). Footprint = drawn edits only
  (not the lore recolour); trim judges collar-vs-skin on the pre-beard art.
Images: baradus_beard_v10_cmp.png, baradus_beard_v10_collar.png.
