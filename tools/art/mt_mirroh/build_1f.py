"""Mt. Mirroh 1F, re-routed (user 2026-11-23): Dreamstone Mysteries' ice cave kept, 2F gone.
- A: a stair up (33-34, 15-16) through the double ice wall north of the upper bridge onto the upper level
  (DM's own 2x2 stair, as at its (19-20, 38-39)).
- B: a stair down (46-47, 6) off the upper level's north lip into the top band (DM's stair, single row, as at (49-50, 22)).
- The three ladders to 2F filled with floor; the Lily Pond exit (54, 1) now leads to the Peak.
- The old Peak exit (3, 12) becomes a small pile of rubble (DM's ice-rock cluster): where the Shard is found.
- Every Strength boulder removed (the five by the Peak exit: the 8a torture spot; the rest: no Strength in Chapter 1).
- DM's wild encounters (levels 26-30) removed: stage 5's job, as on the exterior.
Reads the snapshot of DM's 1F (dm_1f_map.bin), so it can be re-run."""
import os, json, struct, re
H = os.path.dirname(os.path.abspath(__file__)); C = os.path.normpath(os.path.join(H, '..', '..', '..', 'codebase'))
W = 60
cells = list(struct.unpack('<3600H', open(H + '/dm_1f_map.bin', 'rb').read()))
V = lambda mt, col, el: mt | (col << 10) | (el << 12)
def put(x, y, v): cells[y * W + x] = v
STAIR = 0x363
for p in [(33, 15), (34, 15), (33, 16), (34, 16)]: put(*p, V(STAIR, 0, 0))          # A
for p in [(46, 6), (47, 6)]: put(*p, V(STAIR, 0, 0))                                 # B
for p in [(38, 45), (53, 9), (49, 38)]: put(*p, V(0x38F, 0, 3))                      # ladders -> floor
put(3, 12, V(0x37E, 1, 0))                                                          # rubble (DM's ice rocks)
for x in (2, 3, 4): put(x, 13, V(0x379, 0, 4))                                       # the exit's light -> the lip
open(C + '/data/layouts/MirrohInterior_1F/map.bin', 'wb').write(struct.pack('<3600H', *cells))

def jload(m): return json.load(open(C + '/data/maps/%s/map.json' % m))
def jsave(m, j): open(C + '/data/maps/%s/map.json' % m, 'w').write(json.dumps(j, indent=2) + '\n')
j = jload('MirrohInterior_1F')
j['warp_events'] = [
    {'x': 55, 'y': 57, 'elevation': 0, 'dest_map': 'MAP_MT_MIRROH_EXTERIOR', 'dest_warp_id': '0'},   # 0: way out
    {'x': 54, 'y': 1, 'elevation': 0, 'dest_map': 'MAP_MIRROH_PEAK', 'dest_warp_id': '1'}]          # 1: the Peak
j['object_events'] = [o for o in j['object_events'] if o.get('graphics_id') != 'OBJ_EVENT_GFX_PUSHABLE_BOULDER']
j['bg_events'] = [b for b in j['bg_events'] if b.get('script') != 'MirrohInterior_1F_EventScript_Rubble'] + [
    {'type': 'sign', 'x': 3, 'y': 12, 'elevation': 0, 'player_facing_dir': 'BG_EVENT_PLAYER_FACING_ANY',
     'script': 'MirrohInterior_1F_EventScript_Rubble'}]
jsave('MirrohInterior_1F', j)
ids = {o['script'] + '@%d,%d' % (o['x'], o['y']): i + 1 for i, o in enumerate(j['object_events'])}
for m, wid, dest in [('MirrohPeak', 1, '1'), ('MtMirrohExterior', 0, '0'), ('LilyPond', 1, '1')]:
    k = jload(m); k['warp_events'][wid]['dest_warp_id'] = dest; jsave(m, k)              # (Lily Pond: later area)

# the script's local ids follow the boulders' removal
P = C + '/data/maps/MirrohInterior_1F/scripts.pory'; s = open(P).read()
find = lambda script, x, y: ids['%s@%d,%d' % (script, x, y)]
LOC = {'LOCALID_NURSE': find('MirrohInterior_1F_EventScript_Nurse', 41, 46),
       'LOCALID_ROBBER': find('MirrohInterior_1F_Trainer_D', 13, 34),
       'LOCALID_CH1': find('MirrohInterior_1F_EventScript_Chansey', 42, 43),
       'LOCALID_CH2': find('MirrohInterior_1F_EventScript_Chansey', 40, 44),
       'LOCALID_CH3': find('MirrohInterior_1F_EventScript_Chansey', 40, 45),
       'LOCALID_CHANSEY_LAST': find('MirrohInterior_1F_EventScript_Chansey', 42, 45),
       'LOCALID_GRUNT1': find('NULL', 6, 8), 'LOCALID_GRUNT2': find('NULL', 6, 9)}
for k, v in LOC.items(): s = re.sub(r'(\.set %s, )\d+' % k, r'\g<1>%d' % v, s)
if 'MirrohInterior_1F_EventScript_Rubble' not in s:
    s += '''
// The old Peak exit, caved in: the Shard lies under these rocks (the Sword Cult overlooked it). Giving the Shard
// is the items / story stage's job; for now the pile only describes itself.
script MirrohInterior_1F_EventScript_Rubble {
    msgbox("A small pile of rubble.\\pSomething glints faintly between\\nthe stones.")
}
'''
open(P, 'w').write(s)

E = C + '/src/data/wild_encounters.json'; w = json.load(open(E))
for g in w['wild_encounter_groups']:
    if 'encounters' in g: g['encounters'] = [e for e in g['encounters'] if e.get('map') != 'MAP_MIRROH_INTERIOR_1F']
open(E, 'w').write(json.dumps(w, indent=2) + '\n')
print('1F built; local ids', LOC)
