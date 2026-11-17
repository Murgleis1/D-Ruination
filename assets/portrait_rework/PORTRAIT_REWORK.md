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

## Baradus sprites: chin beard to match portrait v10 (2026-11-16)
- Battle front pic: chin outline row 17 + row 16 (incl. jaw corners) solid hair-black (idx 13),
  ragged top on row 15 (29,32,33). Mouth (31,14) and everything above untouched; no pixel directly
  under the mouth (the rejected version read as a dangling tie).
- Overworld: every frame showing his face (front 0,3,4; side 2,7,8), found by pattern: chin row
  black + jaw-shadow px at each side of the lower face black (a U framing the lower face; side
  frames along the profile jaw). Back frames unchanged.
- Verified: compiled .4bpp decodes pixel-identical to the PNGs.
Images: baradus_battle_beard.png, baradus_ow_beard.png.

- 2026-11-16 user: overworld beard "doesn't look good" -> REVERTED to the pre-beard sprite (fd50fadc9).
  Battle sprite keeps its beard (user: it needs the beard).

## Baradus battle sprite beard -- REDONE, candidate 2 APPROVED (2026-11-16)
The previous battle beard (a962c0070) was on his NECK. Aligning his sprite to its source sprite
(trainer094, the user's base) on the feature lines showed: source mouth row 12, chin underside row 14,
rows 15-17 = neck between the collar flaps. Baradus's chin is rows 13-14; rows 15-16 (x30-32) are neck.
Approved construction (MonoMyth #105 study): row 14 (bottom of the face) beard-dark (idx 11) with one
bronze-shadow gap, row 13 bronze-shadow at the jaw corners + one dark px rising at the chin centre;
neck untouched. New colour: free palette slot 14 = bronze skin shadow (118,74,46).
Image: baradus_battle_chin_beard_candidates.png (candidate 2).

## Option C (user 2026-11-16): 2/3 size, hand-cleaned per portrait
- Measured: MonoMyth busts (495) top row ~10, height ~70, head ~46 px wide. Native 48: 49 tall,
  head 39 (too small). 2/3: 66 tall, head 52 (right size) but a 4/3 enlargement doubles px on a
  fixed grid (uneven eyes, 1-px lines). User picked C: 2/3 + hand cleanup.
- Tried and rejected (my review): seam-insertion enlargement -- keeps details exact but distorts
  proportions (hat balloons, eyes too small). Removed.
- tools/art/portrait_patches.py: per-portrait text-grid pixel patches applied after the 2/3 resize
  (portrait_rebuild main, PORTRAIT_SCALE=x). Colours matched to the portrait's own palette.
- Cadmus v1 (48 px per expression): eyes (left: removed doubled bottom row; right: single red
  pupil, lower row W M L, 1-px brown edge), right brim tip tapered like the left, chin stubble
  texture redrawn (brown/dark brown with ~1-in-4 grey flecks). Verified in-game: 0 px diff.
  Open: ear top row doubled (y45-46); small stair-steps on the cheek light diagonal.
  Image: cadmus_cleanup_v1.png. Awaiting user review before install.
- Cadmus v2: hat top rounded (user: "still looks partly cut off"): centre rises 2 rows to a 13-px
  top, stepping 4/3/2 px out to the corners. Image: cadmus_hat_round_v2.png.
- 2026-11-16 INSTALLED (user: hat "looks perfect"): Cadmus neutral/smile (option C v2) and Baradus
  positive/anger/negative (v10 beard + collar trim) at 2/3. In-game Cadmus == PNG (0 px diff).
  Other characters keep their current portraits until each is cleaned and approved.
- Kimaris v1: faces/eyes/mouths survived the 2/3 resize (no patches needed). Crown lump fixed: the
  reconstructed top widened in 4-px jumps (cap on the head); rows 15-20 rebuilt from a 10-px top,
  widening 3,1,2,1-2,2 px per row, outline/shade/hair structure kept (45 px, all 4 expressions).
  Image: kimaris_cleanup_v1.png. Awaiting review.
- Glaive v1 (all 3 expressions, 25 px): left eye -- the 4/3 grid doubled the highlight and dropped
  the black pupil; pupil restored 2 px tall under the highlight (as his right eye), doubled lower
  lid row back to skin; hair spike from the side completion (x71-74, y39-43) trimmed to a 1-px curve.
  Crown measured fine (15-px top, widens 4,3,3).
- Eden v1 (10 px): 6-px nub on top (5-px jump each side) -> top row widened to 10 px; right-side
  completion bulge had square corners -> rounded (64,65,66..66,65,64).
  Images: cleanup_kimaris_glaive_eden_v1.png, glaive_eyes_v1.png. Awaiting review.
- 2026-11-16 INSTALLED (user: "I like the work"): Kimaris x4, Glaive x3, Eden (cleanup v1, 2/3).
  Compiled .4bpp == PNG for all 8. Note: Eden has ONE portrait (neutral); the PellucaUmbraLab script
  asks for POSITIVE/NEGATIVE, which fall back to neutral.
- Eden POSITIVE/SMILE added (user: "a copy of the current Eden portrait but upturn her mouth"):
  _src/eden_positive.png = copy of eden.png; PATCHES['eden_positive'] = Eden's cleanup + a 7-px smile
  (centre of the mouth line stays, ends lift a row, shadow-side corner ticks up, the down-turned mark
  -> skin), drawn the way the user's own smiles are. Registered as both PORTRAIT_EXPR_POSITIVE and
  PORTRAIT_EXPR_SMILE. Verified in-game in the lab theft scene ("Sorry for the intrusion, boys!").
  Images: eden_positive_v1.png, ingame_eden_positive.png. Playtest driver: tools/playtest/lab_eden_scene.py.
- Found while testing (not portraits): Eden's first lab line overflows the text box ("But o|n" cut
  off); Cadmus is asked for PORTRAIT_EXPR_ANGER, which he does not have (falls back to neutral).

## Osrid trainer pics + portrait, round 1 (user 2026-11-17) -- candidates, NOT installed
User: "make sure Osrid's portrait, front trainer sprite and back sprite are a lot better ... in the
style of MonoMyth" / "study every trainer backsprite and frontsprite in MonoMyth".
- Study: all 136 fronts + 11 backs extracted and measured (tools/art/MONOMYTH_TRAINER_STYLE.md).
  Current Osrid front: 0% black silhouette edge (MonoMyth ~50%) and art cut by the top edge;
  current back: full-body figure, 4 identical frames (MonoMyth: right-facing rear bust, real throw).
- Front candidate A (tools/art/osrid_trainer_front.py): Kakugo's front (#10, identified against his
  portraits #69/#70) MIRRORED for pose/anatomy -- the same "his head on Kakugo's body" approach the
  user approved for the overworld sprite. Osrid's head hand-authored from his portrait (silhouette =
  dominant-vote downscale), hair streaming with the scarf's wind; scarf -> his green, gloves -> tan
  leather, coat -> his armour brown-grey, lining -> hair orange.
- Back candidate B (tools/art/osrid_trainer_back.py): MonoMyth back #4 (adult rear bust, 4-frame
  throw) for anatomy/animation; hair carved into his spikes by polar modulation of the outline, face
  -> mask profile with eye mark + drip, hands -> gloves, coat/strap/scarf -> his colours.
- Portrait P4 (tools/art/osrid_portrait_refine.py): the same drawing; hair 5 stacked tones -> 3 flat
  + rim light; scarf/armour near-black interleaved greens -> mode-filtered cel shapes on a real ramp;
  glyph kept stroke-for-stroke (two weights).
- review.py: new `back` mode (64x64 or 64x256; cut allowed bottom/left/right, as all 11 MonoMyth
  backs are). All three candidates pass; sheet: osrid_round1/review_round1.png (back shown composited
  into the real Eden battle frame at the measured position 48,48).
- Open for the user: base choices (Kakugo pose / MonoMyth #4), coat colour (armour brown-grey, as the
  portrait, vs the green cloak of the current front and OW), portrait refinement depth.

## Osrid round 2 (user 2026-11-17, 12:13) -- candidates, NOT installed
User: (1) portrait: "smeared or accidentally deleted some of the black on his eye of horus";
(2) front: "hair is way too huge and the mask is too small ... get it closer to his updated portrait
in terms of element balance"; (3) back: "more accurate to the actual design of Osrid".
- (1) Cause, measured: the drip's lower part and a brow stroke are drawn in the master's dark
  brown (93,81,66), which round 1 treated as anti-aliasing and lightened; two spiral strokes were
  removed by the isolated-pixel cleanup. Fix: every glyph pixel is solid black and re-applied after
  all filters (osrid_portrait_refine.py). Verified: no glyph stroke lighter than the original.
- (2) Head redrawn to the portrait's balance: mask 8x12 (was 6x8), about half the head width; hair
  crown 4 rows plus the swept mass behind. Glyph at sprite scale: eye (lid, pupil) plus the tear
  from its corner; the brow is dropped because at 8 px it fused with the drip into a "T".
- (3) Back: #4's head removed entirely; Osrid's head from behind built from shapes (skull + swept
  spikes of varied length + fringe over the mask; mask side-on as an oval with only the eye's
  outer corner and the drip at its edge; ear; strand lines); his thick green scarf wraps the
  neck and shoulders. #4 is kept only for body, arm and the 4-frame throw.
- All three pass review.py; sheet: osrid_round2/review_round2.png.

## Osrid round 3 (user 2026-11-17, 12:27-12:41) -- candidates, NOT installed
- Portrait P5: APPROVED by the user ("Portrait looks good now").
- New canonical design reference: assets/osrid_reference/osrid_character_sheet.png (user's sheet).
  Swatches sampled: cream 193,184,171; grey-green 58,63,55; charcoal 49,48,46; dark brown 67,50,39;
  rust 90,56,41; iron 104,100,91. Outfit: thick dark green scarf; quilted charcoal jacket to the
  mid-thigh; two brown straps crossing the chest; iron pauldron on his LEFT shoulder; belt with a
  square buckle and pouch; leather bracers; dark fingerless gloves; dark brown trousers;
  criss-cross shin wraps into heavy boots; long tattered dark green cloak. Hair: tousled, wavy
  auburn (not spikes). The mask is held by a leather strap with a buckle round the back of the head.
- Front F3: the outfit rebuilt part by part on Kakugo's body (jacket / cloak / trousers by region;
  straps, belt and buckle, pouch, pauldron, bracers, gloves and wraps drawn over it). Glyph per the
  sheet: brow bar, almond eye, drip, spiral, plus the plain eye hole on the other side.
- Back E7: round 2's procedural spiky head was wrong at the root (the user: "giant blobby swollen
  monstrosity"). #4's own head drawing is identical in every frame (98%, measured), so Osrid's head
  is built once on it: hair recoloured; the mask is an explicit area with an organic profile (brow,
  nose, mouth recess, chin), the hair in front of the face removed, the glyph at the front edge;
  strap and square buckle above the ear; nape tucked into the scarf; lit strands and tufts. Body:
  quilted charcoal jacket, cape over the left third of the back, strap kept, fingerless gloves.
- Sheet: osrid_round3/review_round3.png (with the user's sheet alongside).

## Osrid round 4 (user 2026-11-17, 13:05-13:12) -- candidates, NOT installed
- User edit of the front mask (osrid_round4/user_front_tweak.png, recovered to 64x64 indices): 12 px
  in the mask. User: "the eye of horus needs to take up more space on the mask like in the
  portrait" / "you need to study the eye of horus carefully".
- Eye of Horus, as on his sheet's mask and in the portrait: an arched brow with dropping ends; an
  almond with thick lids, a large pupil, an inner line and a long outer tail; a straight vertical
  line from under the eye to the jaw; a spiral going down, then curling left and up. Mapped from
  the portrait's proportions onto the 8 px sprite mask. User APPROVED ("the mask looks correct here
  now", osrid_round4/user_mask_approved.png). The front head is that exact render (verified: 0 mask
  pixels differ). A larger-mask head was tried and dropped.
- Clothes (user: "from grey to the dark green, darker grey and the pauldrons on his shoulders"):
  dark green quilted jacket (sheet 58,63,55), green-black shadows, richer green scarf and cloak,
  iron pauldrons on BOTH shoulders, iron buckle, dark gloves. The back uses the same scheme.
- Back hair (user: "doesn't look correct at all"): the combed strands are replaced by the
  portrait's way of drawing hair: clumps with lit tips, dark separations, small swept tufts
  (2-3 px). Hand detection is now geometric (skin outside the face box), which fixes the lapel
  turning into glove/iron; domed iron pauldrons on both shoulders.

## Osrid round 5: back hair TRACED (user 2026-11-17 16:38-16:39) -- candidate, NOT installed
User: "Why can't you make the hair look more like the portrait and this?" / "once you trace
something over, ... go back to the monomyth aesthetic with those exact pixels and shading and
transplant them". Honest cause: the hair kept coming from #4's bob plus rule-made tufts; the
reference's silhouette (big irregular locks flaring at the back and nape) was never in it.
Method (tools/art/trace_transplant.py + osrid_trainer_back.py HEAD_TRACED):
1. Trace: the sheet's back-view head at full resolution; material masks (hair by warm-brown hue
   and background distance, mask by warmth on the right, strap); coverage downscale to 32 px
   (partial strands kept at >= 45-50% coverage); hair tone from the reference's own light/dark
   (percentiles inside the hair: deepest 12% = crevices).
2. Re-render the MonoMyth way: 3-tone hair ramp (portrait colours), black ONLY where crevices form
   connected strand lines (lone ones -> dark), no isolated pixels, black silhouette outline.
   (A literal texture transplant of #4's hair pixels was tried first: #4 is a smooth bob, so it
   flattened the user's locks, and was dropped in favour of the traced tone structure.)
3. Strap with both buckles, ear and the mask profile placed as on the reference. The mask is 1-3 px
   wider than the true sliver so the glyph reads at 1x.
Also fixed: the floating-outline pass deleted a black pixel enclosed in a 3x3 black block (now
it only drops outline that touches transparency).

## Osrid round 6: the back as a MonoMyth profile (user 2026-11-17 16:48-16:56) -- NOT installed
User: "you aren't really imagining what the back of Osrid's head looks like on his portrait sprite as
well as the front sprite" / "studying the front versus backsprites of Trainers in MonoMyth".
- MonoMyth front/back pairs found: back 2 <-> #80, back 3 <-> #78, back 6 <-> #116, back 8 <-> #88,
  back 0 <-> #70 (osrid_round6/monomyth_front_back_pairs.png). Finding: MonoMyth back pics are NOT
  views from behind. The head is a near-profile facing right, seen slightly from behind: face about
  40% of the head width with eye, nose and mouth shown, ear just behind it, the front hairstyle seen
  from the side; only the torso turns away. Every earlier Osrid back hid the face behind hair:
  that was the root error.
- Head: the approved portrait's hair (dominant-vote downscale at natural proportions; spikes swept
  up and back) caps the crown and the back. The face becomes the mask in profile (forehead under
  the fringe, brow ridge, eye socket, nose, lips, chin, jaw) carrying the Eye of Horus side-on (brow
  bar, a foreshortened eye with its tail back toward the ear, drip, spiral). The ear sits behind
  it; strap and buckle above the ear.
- Body: #4's own three coat tones recoloured (flat cel shapes, no lattice) into his dark green
  jacket; the cape down the near side with long folds; the scarf wrap with two big folds; layered
  pauldron plates on the near shoulder (his left, per the sheet), the far one peeking.

## Osrid round 7 (user 2026-11-17 17:00) -- NOT installed
User: "you wouldn't be able to see the whole mask eye ... only the left half" / "the whole
backsprite looks artificial versus actual monomyth backsprites".
- The artificial look came from generated patterns (straight cape folds, radial scarf creases, a
  striped pauldron, a polygon scarf). The body is now MonoMyth #4's OWN coat pixels, recoloured:
  coat to his jacket greens; #4's thick collar (which wraps the neck exactly where his scarf is) to
  the scarf, keeping #4's folds and dither; #4's tie to the scarf end; coat behind #4's own fold line
  (x ~22) to the cape; #4's near shoulder pixels to iron (pauldron) with its curved shading; one
  strap. The head sits on the collar as #4's does.
- Glyph: only the LEFT half of the Eye of Horus (brow's inner end, half the eye, the spiral), 2 px in
  from the profile edge so it reads as paint, not as notches in the outline.
- Hair: the portrait-derived hair cleaned (doubled outline trimmed, black specks -> dark hair,
  single specks smoothed), then the spike tips regrown at the portrait's own measured tip
  positions and lengths (not a regular comb: a hand-drawn regular comb looked artificial).

## Osrid round 9 — back of the head (no mask); overworld hair matched

User feedback (round 8): show no mask, only the back of his hair and the connecting strap; the hair was
too thick compared with the front and portrait; the shading and colour mixes were busier than
MonoMyth's simple ones. Also: the overworld hair was browner than the auburn of the other three sprites.

- Overworld (`graphics/object_events/pics/people/osrid.png`, own palette, OBJ_EVENT_PAL_TAG_OSRID): a
  palette-only change. Hair indices 3/6/8/A now use the portrait's ramp (74,26,12)/(114,42,18)/
  (160,64,28)/(206,104,52). All four indices are hair only in all 9 frames.
- Back candidate N3 (`tools/art/osrid_trainer_back.py`, HEAD_TRACED): a hand-drawn back-of-head grid,
  pasted at (14,12).
  - Short spiky locks: chunky pointed tufts, like the front sprite, not 1-px fuzz.
  - Three hair tones plus black: flat mid base, shadow on the left and at the nape, one lit cluster at
    the upper right, two lock partings.
  - The mask strap crosses the skull from ear to ear, with the buckle off-centre.
  - Small ears at strap height. The skull tapers to the nape.
  - A sliver of nape between the lowest locks, then the scarf wrapped high (C/A/B).
  - The body is MonoMyth #4's recolour, unchanged from round 7.
  - Code changes:
    - The head's hair and skin now tuck under #4's scarf from COLLAR_Y=33.
    - Small floating leftovers of #4's old head (<20 px components) are dropped.
  - `mm_back04_frames.pkl` holds the builder input, rebuilt from the indexed back_04.png.
  - review.py --mode back: pass. The flagged nubs are the intended black spike tips.

## Osrid round 10 — head turned with the body; MonoMyth cloth colours

User feedback (round 9):
- The head and body should line up, still facing away.
- A small edge of white mask is fine, and it helps the throwing arm look right. No Eye of Horus should show.
- Keep simplifying the shading.
- Study MonoMyth's dark greens, browns, blacks and greys to get the clothes colours right.

Findings, measured on all 11 MonoMyth back pics and 136 fronts:
- Every back pic turns its head WITH the body: back and side of the head, then the ear, then a sliver of cheek or jaw on the right. Round 9 had a straight-on head on a three-quarter body, which is why it read as unnatural.
- Back #4's hair uses two tones (lit top, shadowed lower half), a few light crown strands, and part of its outline in the dark hair tone.
- Cloth uses three tones per material plus one near-black. Shadows shift cool and lights shift warm or yellow. Examples:
  - #72 greens: (16,40,24) → (40,88,40) → (152,184,80)
  - #7 red hair: (120,56,64) → (208,88,48) → (232,136,96)
  - Greys lean blue: (64,64,80), (112,120,152)
  - Closest analogue: #96 (grey-green cloak over brown leathers)

Back candidate P6 (`osrid_trainer_back.py`, HEAD_MODE='lost', `head_lost()`):
- #4's own head is converted in every frame, so it stays at the angle the body and throwing arm were drawn for.
- #4's hair is kept with its own shading, in Osrid's auburn.
- #4's face becomes hair, except a smoothed crescent (3 px) at its front edge: the white mask with a shaded rim and a black outline, no glyph. The nose and lips are trimmed off by a 7-row median.
- Holes left by #4's face lines are filled with the dark hair tone.
- Five triangular spiky locks are ray-cast from the hair centre to the silhouette.
- The strap runs from the buckle on the back of the skull to the mask's edge.

Cloth palette, shared with the front so the two match:
- Shadow (26,30,32)
- Jacket mid (50,58,56), jacket light (84,96,74)
- Scarf/cape (18,40,36) / (34,66,46) / (70,104,60)
- Iron (58,60,72)

Front candidate G4 has G3's pixels exactly; only those palette slots changed.

Both sprites have 16 distinct 15-bit colours. review.py --mode back: pass.
