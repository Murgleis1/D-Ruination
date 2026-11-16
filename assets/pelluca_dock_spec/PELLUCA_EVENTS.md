# Pelluca map — event inventory and proposed fates (for approval before map edits)

Source: `codebase/data/maps/PellucaCity/map.json` + `scripts.pory`, 2026-11-15.
62 objects, 9 warps, 6 signs, 48 trigger tiles, 1 layout swap. Ruination's only
story script here is `DR_PellucaCity_Arrival` (the dock scene).

## Hard constraints (whatever is cut)
- **Local ids are list positions.** `LOCALID_DR_TIDAL 61` / `LOCALID_DR_CADMUS 62` must be
  updated in the same change that removes earlier objects, or the arrival scene moves
  the wrong sprites.
- **Warp slots are referenced from other maps** (interiors' return warps by index).
  Keep slot numbers or update the other side in the same change.
- Dock geometry x38-52 y42-58 and the lab warp (47,44) stay exactly as locked.
- Connections today: Ivy River (N), Routes 7/8, Hoya River — to be reconciled with the
  locked exits: N Ivy River, W Route 11, E Hoya Delta, S Surf-gated water (Route 10).

## KEEP (Ruination story)
| item | where | note |
|---|---|---|
| S.S. Tidal ship object | (44,55) | arrival scene, local id 61 today |
| Cadmus object | (44,46) | arrival scene, local id 62 today |
| `DR_PellucaCity_Arrival` | on-frame script | walks Cadmus to the lab door |
| Lab warp | (47,44) -> PELLUCA_UMBRA_LAB | locked |

## REPURPOSE (warps -> Pelluca Valley buildings)
| today | proposed |
|---|---|
| Pokemon Center (14,27) + Poke Mart (9,27) | ONE door: the Seaside Tavern (heal + shop), badge 9 |
| Fishery (3,44) | boathouse, badge 11 (Fisherman's Dilemma) |
| Houses x3 (46,38), (66,34), (33,-1) | Osrid's cover house (3), Cadmus's house/estate (4), one residence; (33,-1) is an off-map edge warp -> drop |
| Game Corner (35,38) | Arceus church door -> existing PELLUCA_TEMPLAR_MONASTERY interior |
| Gym (37,8) | Academy door (interior: reuse/rebuild the gym map as the Academy hall) |

## CUT (Dreamstone Mysteries, 3,000 years later)
| group | objects | triggers / other |
|---|---|---|
| Flooded-city rescue event | 13 flooded citizens, 4 drowning, 4 saved, Jania | 36 triggers, flooded layout swap + thunderstorm |
| Mayor fight | mayor + 3 sailors | 4 triggers |
| Cable car / Qwilsquad | blocker sailor, entrance sailor | 4 triggers, cable car sign |
| Gym | Red gym block (Spenser) | post-gym trigger |
| Greta | Greta | 3 triggers |
| Team Magma | Gabrielle + Hisuian Zoroark | |
| Mayor's Pokemon | Galarian Corsola x5 | |
| Wingull quest | girl, mother, critic, 2 Wingull | |
| DM travel mechanics | Drifblim travel, Paldean Tauros | |
| Signs | cable car, game corner, mayor house, restaurant | |

## RE-PLACE on the new layout (dialogue rewritten later for the era)
- Townsfolk: NPC1-7, NPC10-12 (+ Lycanroc, Sealeo, Stantler companions) — keep ~8 as
  Pelluca residents; their DM dialogue references the modern era and gets a pass later.
- Items x3 (two Poke Balls, one TM ball) — re-hidden on the new layout.
- Mr. Briney's boats x4 — moored fishing boats at the jetty, or cut (open).
- Signs: "Main" and "Fishery" — rewritten for Pelluca Valley.
