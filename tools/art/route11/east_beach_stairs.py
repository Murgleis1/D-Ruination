"""Route 11's east beach: a way down (user 2026-11-25, "Stone stairs"; mock assets/route11_reference/
east_beach_stairs_mock.png). The west stairs' twin: two wide, cut into the coastal cliff at x 77-78, rows 25-27 (the lip
and its two faces), reached from the road through the tall grass on the east bank; the same metatiles as the west stairs
(x 58-59: 0x2c5 left, 0x2c6 right), walkable, elevation 3 as everything here.
Patches the committed map.bin in place (build_route11.py's write_map() is stale: do not re-run it; see the workflow
doc). The composer (route11_v2.py) carries the same stairs in EAST_STAIRS for any future rebuild.
Usage: python3 tools/art/route11/east_beach_stairs.py"""
import os, struct
C = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'codebase')
W = 90
P = os.path.join(C, 'data/layouts/Route11/map.bin')
d = bytearray(open(P, 'rb').read()); v = list(struct.unpack('<%dH' % (len(d) // 2), d))
for y in (25, 26, 27):
    for x, src in ((77, 58), (78, 59)):
        assert v[y * W + src] & 0x3FF in (0x2c5, 0x2c6), ('west stairs moved', src, y)
        v[y * W + x] = v[y * W + src]                                  # (metatile, walkable, elevation 3: the west stairs')
for x in (77, 78):
    assert (v[28 * W + x] >> 10) & 3 == 0 and (v[24 * W + x] >> 10) & 3 == 0, 'the beach or the bank is not walkable'
open(P, 'wb').write(struct.pack('<%dH' % len(v), *v))
print('east beach stairs written')
