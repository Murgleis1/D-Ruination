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
