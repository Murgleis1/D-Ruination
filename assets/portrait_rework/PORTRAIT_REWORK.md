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
