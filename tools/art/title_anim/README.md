# Animated title screen (sky drift + Chien-Pao tail)

Run from a folder containing `dr_title.png` (graphics/title_screen/dr_title.png), in this order:

| step | script | output |
|---|---|---|
| sky / logo masks | `masks.py`, `logo_mask.py`, `make_mask_sky2.py` | `mask_sky.npy`, `mask_logo_full.npy`, `mask_sky2.npy` |
| light sky strip (512 x 48, seamless) | `sky_light.py` | `sky_strip512_light.npy`, `sky_newcols.npy` (palette 100-102) |
| Chien-Pao cut-out | `cutout.py` | `mask_cp.npy`, `bg_filled.npy` |
| tail rig (tail = silhouette + its 1-px drawn border) | `tail_rig.py` | (module) |
| background behind the tail | `tail_bgfill.py` | `bg_filled_tail.npy` |
| tail poses (inverse-sampled bend, rigid 3-px tip, curl lift at 38 % with counter-bend) | `build_lift2.py 1.0 1.2 tail_keys_l10.pkl`, then `tail_strays.py tail_keys_l10.pkl` | 5 poses, rest = original pixels |
| idle timing | `tail_idle_seq.py` | `tail_poses_l10_idle.pkl` |
| preview | `SKY=sky_strip512_light.npy SKYMASK=mask_sky2.npy BGF=bg_filled_tail.npy TAILP=tail_poses_l10_idle.pkl preview4.py 1800 out.mp4` | 60 fps mp4 |

| ROM export | `export_rom.py <codebase>/graphics/title_screen <codebase>/src/data/title_screen_anim.h` | tile set + palette, 3 tilemaps, tail pose tiles, glint table, tail timing |

`zoomcheck.py` renders poses at 16x with outline defects marked.  Approved preview: `assets/title_previews/`.
