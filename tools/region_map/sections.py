"""Map sections for the empire-era region map.

    python3 tools/region_map/sections.py      # rewrites region_map_sections.json positions + region_map_layout.h

SECTIONS maps every place in layout.py to its MAPSEC constant and its display name. Constants are either
DM sections whose place is the same one (renamed to the empire name, e.g. MAPSEC_GASTREE_CITY ->
MAPSEC_AGUSTREI_HEIGHTS, per the atlas's DM-fate notes), or MAPSEC_DR_* sections that reuse unused
Kanto/Sevii slots (no code or map referred to them). Map-section ids are one byte (map headers and
Pokemon met-location), so they cannot simply be added.

Display names: at most 19 characters (RegionMap.mapSecName is u8[20]); the Fly/Town map name window is
96 px wide, so names above ~94 px in the normal font are cut off visually.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from layout import LAYOUT
CODEBASE = os.path.abspath(os.path.join(HERE, '..', '..', 'codebase'))

# DM sections renamed to the empire place they become (old -> new constant)
RENAMES = {
    'MAPSEC_PELLUCA_CITY':        'MAPSEC_PELLUCA_VALLEY',
    'MAPSEC_MIRROH_BASE_CAMP':    'MAPSEC_MIRROH',
    'MAPSEC_MT_MIRROH_EXTERIOR':  'MAPSEC_MT_MIRROH',
    'MAPSEC_MIRROH_PEAK':         'MAPSEC_MT_MIRROH_PEAK',
    'MAPSEC_FENNILAHL_TOWN':      'MAPSEC_FENNILAHL',
    'MAPSEC_CARABRUE_TOWN':       'MAPSEC_CARABRUE_KEEP',
    'MAPSEC_GASTREE_CITY':        'MAPSEC_AGUSTREI_HEIGHTS',
    'MAPSEC_HOYA_RIVER_SOUTH':    'MAPSEC_HOYA_RIVER_DELTA',
}
# layout name -> (constant, display name); constants marked NEW get a reclaimed slot
SECTIONS = {
 'Mt. Mirroh Peak':      ('MAPSEC_MT_MIRROH_PEAK',        'Mt. Mirroh Peak'),
 'Mt. Mirroh':           ('MAPSEC_MT_MIRROH',             'Mt. Mirroh'),
 'Templar Headquarters': ('MAPSEC_DR_TEMPLAR_HQ',         'Templar Citadel'),     # user 2026-11-18 ('Templar Headquarters' is 20 chars)
 'Route 13':             ('MAPSEC_DR_ROUTE_13',           'Route 13'),
 'Mirroh':               ('MAPSEC_MIRROH',                'Mirroh'),
 'Hollow Hill':          ('MAPSEC_DR_HOLLOW_HILL',        'Hollow Hill'),
 'Mirroh Necropolis':    ('MAPSEC_DR_MIRROH_NECROPOLIS',  'Mirroh Necropolis'),
 'Route 11':             ('MAPSEC_DR_ROUTE_11',           'Route 11'),
 'Route 14':             ('MAPSEC_DR_ROUTE_14',           'Route 14'),
 'Moray Estate':         ('MAPSEC_DR_MORAY_ESTATE',       'Moray Estate'),
 "Pierra's Manor":       ('MAPSEC_DR_PIERRAS_MANOR',      "Pierra's Manor"),
 'Route 15':             ('MAPSEC_DR_ROUTE_15',           'Route 15'),
 'Ivy River':            ('MAPSEC_IVY_RIVER',             'Ivy River'),
 'Gleamdusk Prison':     ('MAPSEC_DR_GLEAMDUSK_PRISON',   'Gleamdusk Prison'),
 'Pelluca Valley':       ('MAPSEC_PELLUCA_VALLEY',        'Pelluca Valley'),
 'Hoya River Delta':     ('MAPSEC_HOYA_RIVER_DELTA',      'Hoya River Delta'),
 'Route 10':             ('MAPSEC_DR_ROUTE_10',           'Route 10'),
 'Rivetshore City':      ('MAPSEC_RIVETSHORE_CITY',       'Rivetshore City'),
 'Riptide Bridge':       ('MAPSEC_DR_RIPTIDE_BRIDGE',     'Riptide Bridge'),
 'Windrunner Island':    ('MAPSEC_DR_WINDRUNNER_ISLAND',  'Windrunner Island'),
 'Keerin Shrine':        ('MAPSEC_DR_KEERIN_SHRINE',      'Keerin Shrine'),
 'Silversun Palace':     ('MAPSEC_DR_SILVERSUN_PALACE',   'Silversun Palace'),
 'Silversun City':       ('MAPSEC_SILVERSUN_CITY',        'Silversun City'),
 'Route 6':              ('MAPSEC_ROUTE6',                'Route 6'),
 'Alban Estate':         ('MAPSEC_DR_ALBAN_ESTATE',       'Alban Estate'),
 'Route 5':              ('MAPSEC_ROUTE5',                'Route 5'),
 'Galecrest City':       ('MAPSEC_GALECREST_CITY',        'Galecrest City'),
 'Vilethorn Woods':      ('MAPSEC_VILETHORN_WOODS',       'Vilethorn Woods'),
 'Route 7':              ('MAPSEC_ROUTE7',                'Route 7'),
 'Graymoon Keep':        ('MAPSEC_DR_GRAYMOON_KEEP',      'Graymoon Keep'),
 'Route 9':              ('MAPSEC_DR_ROUTE_9',            'Route 9'),
 'Shadowmarshes':        ('MAPSEC_DR_SHADOWMARSHES',      'Shadowmarshes'),
 'Veddev':               ('MAPSEC_DR_VEDDEV',             'Veddev'),
 'Sunset Tower':         ('MAPSEC_DR_SUNSET_TOWER',       'Sunset Tower'),
 'Route 1':              ('MAPSEC_ROUTE1',                'Route 1'),
 'Carabrue Keep':        ('MAPSEC_CARABRUE_KEEP',         'Carabrue Keep'),
 'Route 2':              ('MAPSEC_ROUTE2',                'Route 2'),
 'Fennilahl':            ('MAPSEC_FENNILAHL',             'Fennilahl'),
 'Route 4':              ('MAPSEC_ROUTE4',                'Route 4'),
 'Blue Moon Monastery':  ('MAPSEC_DR_BLUE_MOON_MONASTERY','Blue Moon Abbey'),      # user 2026-11-18 (full name is 105 px)
 'Route 3 (proposed)':   ('MAPSEC_ROUTE3',                'Route 3'),
 'Northpoint Academy':   ('MAPSEC_DR_NORTHPOINT_ACADEMY', 'Northpoint'),           # user 2026-11-18 (full name is 102 px)
 'Route 0':              ('MAPSEC_DR_ROUTE_0',            'Route 0'),
 'Agustrei Heights':     ('MAPSEC_AGUSTREI_HEIGHTS',      'Agustrei Heights'),
 'Fennilahl Suburbs':    ('MAPSEC_DR_FENNILAHL_SUBURBS',  'Fennilahl Suburbs'),
 'Paragon Gate':         ('MAPSEC_DR_PARAGON_GATE',       'Paragon Gate'),
 'Paragon Road':         ('MAPSEC_DR_PARAGON_ROAD',       'Paragon Road'),
 'Victory Cape':         ('MAPSEC_VICTORY_CAPE',          'Victory Cape'),
 'Tinkaton Lair':        ('MAPSEC_DR_TINKATON_LAIR',      'Tinkaton Lair'),
 'Seregmorn Desert':     ('MAPSEC_DR_SEREGMORN_DESERT',   'Seregmorn Desert'),
 'Dune Path':            ('MAPSEC_DR_DUNE_PATH',          'Dune Path'),
 'Mt. Ceram':            ('MAPSEC_MT_CERAM',              'Mt. Ceram'),
 'The Ashlands':         ('MAPSEC_DR_ASHLANDS',           'The Ashlands'),
}
# unused Kanto/Sevii slots (no code reference, no map) handed to the MAPSEC_DR_* sections, in order
RECLAIMED_SLOTS = list(range(0x63, 0x8F))

def write_json_and_layout():
    path = os.path.join(CODEBASE, 'src', 'data', 'region_map', 'region_map_sections.json')
    data = json.load(open(path)); secs = data['map_sections']
    by = {s['map_section']: s for s in secs}
    used = set()
    for name, kind, x, y, w, h in LAYOUT:
        const, disp = SECTIONS[name]
        if len(disp) > 19: raise SystemExit(f'{disp}: over 19 characters')
        e = by.get(const)
        if e is None:
            e = {'map_section': const}; secs.append(e); by[const] = e
        e.update({'name': disp, 'x': x, 'y': y, 'width': w, 'height': h}); used.add(const)
    for s in secs:                                   # everything else is off the empire map
        if s['map_section'] not in used:
            s.update({'x': 0, 'y': 0, 'width': 0, 'height': 0})
    json.dump(data, open(path, 'w'), indent=2); open(path, 'a').write('\n')
    grid = [['MAPSEC_NONE'] * 28 for _ in range(15)]
    for name, kind, x, y, w, h in LAYOUT:
        for j in range(y, y + h):
            for i in range(x, x + w): grid[j][i] = SECTIONS[name][0]
    out = ['// Generated by tools/region_map/sections.py from tools/region_map/layout.py -- do not edit by hand.',
           'static const u8 sRegionMap_MapSectionLayout[MAP_HEIGHT][MAP_WIDTH] = {']
    for row in grid: out.append('    {' + ', '.join(row) + '},')
    out.append('};'); out.append('')
    open(os.path.join(CODEBASE, 'src', 'data', 'region_map', 'region_map_layout.h'), 'w').write('\n'.join(out))

if __name__ == '__main__':
    write_json_and_layout(); print('sections written')
