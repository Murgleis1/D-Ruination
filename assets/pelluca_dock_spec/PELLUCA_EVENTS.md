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


## DECISIONS (user, 2026-11-15)
1. CUT everything Dreamstone Mysteries: "nothing in modern-day Pelluca exists in the empire era."
2. The Arceus church IS Pelluca's local **Templar Monastery** -> its door goes to the existing
   PELLUCA_TEMPLAR_MONASTERY interior. Lore: the back of the church holds criminals so they can
   atone, be properly sentenced, then do community service under the Templars' direction. Eden's
   jail scene (after she loses to you at the lab) is in a cell in the back of the church.
3. NO gym and NO Trial fights in Pelluca Valley: it is the starter town, home to key quests, and
   Cadmus's (and the player's) base of operations. The gym map is retired; the Academy gets its
   own interior later (not a reused gym).
4. Mr. Briney's rowboats STAY as an easter egg.

## Harbour objects (user 2026-11-16: "put another ship there to show how the docks are bustling")
Placed with the map's events (object events, not tiles):
- S.S. Tidal (OBJ_EVENT_GFX_SS_TIDAL) moves (44,55) -> (44,54): alongside the new pier head.
- A second ship (OBJ_EVENT_GFX_SS_TIDAL) at (67,45), moored on the bay jetty's east side.
- Mr. Briney's rowboats (easter egg, kept) at (60,43) and (60,45), on the jetty's west side.

## Umbra cavern entrance (author 2026-11-16: west-beach cliff, sealed)
- Cave mouth in the lower cliff at (10-11, 34-35); slab cells (10,35),(11,35) carry door
  behaviour. Events pass: warp to the deep-cavern map (when it exists) on those cells, plus a
  sign/script "sealed with the Umbra crest" that blocks entry until the Trial 4 sidequest flag.

## Overworld Pokemon (user 2026-11-16): birds enjoying the open lawn by the Academy
- 2-3 wandering bird Pokemon objects on the open lawn east of the north road (x40-47, y4-11)
  and around the Academy's grounds; species era-appropriate (chosen at the events pass).

## Signposts (draft 16): bg_event signs on the post cells, text at the events pass
- (9,27) west: Route 11 / Pelluca Valley. (71,23) east: Hoya Delta. (36,2) north road.
