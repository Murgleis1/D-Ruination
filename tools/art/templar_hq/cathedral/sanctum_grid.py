"""The Sanctum's collision (17x15, sanctum/sanctum_mock.png), by hand 2026-11-23: the summoning circle is floor (the
shadow-self fights stand on it); the stair down (x 7-9) leads to the nave's gold grille ('E', its bottom step)."""
GRID = """
#################
#################
#################
####.........####
####..#...#..####
###...........###
###...........###
###.#.......#..##
###............##
###...........###
####..#...#..####
####.........####
#######...#######
#######...#######
#######EEE#######
""".strip().split('\n')
assert len(GRID) == 15 and all(len(r) == 17 for r in GRID), [len(r) for r in GRID]
