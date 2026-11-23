"""The nave's collision (21x36, the game's nave picture: nave_mock_v2 without Ambrose, the stained-glass Arceus
over it). Read from the room picture by hand (2026-11-23): '#' solid, '.' floor, 'D' a door (its warp), 'E' the exit
(the carpet's last row; south-arrow warps back out to the courtyard). The brick at row 8 and at the foot of the
west and east doors is the floor in the walls' shadow (Empire's brick floor), so the chancel doors are reached from
it. The Sanctum's gold grille (2,7) stays solid: sealed (a sign there says so)."""
GRID = """
#####################
#####################
#####################
#####################
#####################
#####################
#####################
##################D##
##.#.....###.....#.##
##..#....###..####.##
##..###...#...####.##
##..###.......####.##
###.......#....#..###
######..#####..######
######..#####..######
######..#####..######
######..#####..######
######..#####..######
#####...........#####
####.............####
##D#.............#D##
#D....###...###....D#
#...................#
#....####...####....#
#...................#
##..#####...#####..##
##.................##
#...#####...#####...#
##.................##
##..#####...#####..##
##.................##
##....###...###....##
####.............####
####.............####
######.#.....#.######
########.EEE.########
""".strip().split('\n')
assert len(GRID) == 36 and all(len(r) == 21 for r in GRID), [len(r) for r in GRID]
DOORS = {'study': (18, 7), 'bishops': (2, 20), 'registry': (18, 20), 'kitchen': (1, 21), 'storehouse': (19, 21)}
SANCTUM_GRILLE = (2, 7)
