"""Chapter 1 wild encounters (user-approved 2026-11-27): writes the tables from
docs/chapter1_wild_encounters_draft.md into src/data/wild_encounters.json and sets the
land slot rates to Gen 3's 20/20/10/10/10/10/5/5/4/4/1/1.

Run from anywhere; idempotent (replaces any table already on these maps)."""
import json, re, os
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
JS = os.path.join(REPO, 'codebase/src/data/wild_encounters.json')
DRAFT = os.path.join(REPO, 'docs/chapter1_wild_encounters_draft.md')
LAND_RATES = [20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1, 1]

NAMES = {'Paldean Tauros (Blaze Breed)': 'TAUROS_PALDEA_BLAZE', 'Hisuian Zorua': 'ZORUA_HISUI',
         'Hisuian Growlithe': 'GROWLITHE_HISUI', 'Hisuian Sneasel': 'SNEASEL_HISUI',
         'Alolan Sandshrew': 'SANDSHREW_ALOLA', 'Alolan Vulpix': 'VULPIX_ALOLA', 'Alolan Geodude': 'GEODUDE_ALOLA',
         'Nidoran♀': 'NIDORAN_F', 'Nidoran♂': 'NIDORAN_M', 'White-Striped Basculin': 'BASCULIN_WHITE_STRIPED'}
def species(name):
    name = name.strip('* ')
    return 'SPECIES_' + NAMES.get(name, name.upper().replace(' ', '_').replace('.', '').replace("'", ''))

# heading in the draft -> (map, land encounter rate)
SECTIONS = {'## Route 11': ('MAP_ROUTE11', 20), '## Hollow Hill': ('MAP_HOLLOW_HILL', 20),
            '## Route 13': ('MAP_ROUTE13', 20), '### Mt. Mirroh exterior': ('MAP_MT_MIRROH_EXTERIOR', 20),
            '### Mt. Mirroh cave': ('MAP_MIRROH_INTERIOR_1F', 10), '### Mirroh Peak': ('MAP_MIRROH_PEAK', 20)}
# Old Rod tables (70/30). The Good and Super Rod are not in Chapter 1: their slots repeat the
# Old Rod pair until those chapters give the maps their own deeper-water tables.
FISH = {'MAP_PELLUCA_CITY': [('MAGIKARP', 5, 10), ('ARROKUDA', 5, 10)],
        'MAP_PELLUCA_HARBOUR': [('MAGIKARP', 5, 10), ('ARROKUDA', 5, 10)],
        'MAP_ROUTE11': [('MAGIKARP', 5, 10), ('WOOPER', 5, 10)],
        'MAP_MT_MIRROH_EXTERIOR': [('MAGIKARP', 18, 20), ('BASCULIN_WHITE_STRIPED', 18, 20)]}

def land_tables():
    out, cur = {}, None
    for line in open(DRAFT, encoding='utf-8'):
        h = next((k for k in SECTIONS if line.startswith(k)), None)
        if h: cur = SECTIONS[h]; out[cur[0]] = (cur[1], []); continue
        if line.startswith('#'): cur = None; continue
        m = re.match(r'\|\s*(\d+)\s*\|\s*\**(\d+)\**\s*\|\s*([^|]+?)\s*\|\s*(\d+)(?:-(\d+))?\s*\|', line)
        if cur and m:
            slot, pct, name, lo, hi = int(m[1]), int(m[2]), m[3], int(m[4]), int(m[5] or m[4])
            rows = out[cur[0]][1]
            assert slot == len(rows) and pct == LAND_RATES[slot], (cur, line)
            rows.append({'min_level': lo, 'max_level': hi, 'species': species(name)})
    for k, (r, rows) in out.items(): assert len(rows) == 12, (k, len(rows))
    return out

def main():
    d = json.load(open(JS, encoding='utf-8'))
    g = next(x for x in d['wild_encounter_groups'] if x['label'] == 'gWildMonHeaders')
    next(f for f in g['fields'] if f['type'] == 'land_mons')['encounter_rates'] = LAND_RATES
    land = land_tables()
    maps = set(land) | set(FISH)
    g['encounters'] = [e for e in g['encounters'] if e.get('map') not in maps]
    for mp in sorted(maps):
        e = {'map': mp, 'base_label': 'gDR_' + ''.join(w.capitalize() for w in mp[4:].split('_'))}
        if mp in land:
            e['land_mons'] = {'encounter_rate': land[mp][0], 'mons': land[mp][1]}
        if mp in FISH:
            (a, alo, ahi), (b, blo, bhi) = FISH[mp]
            A = {'min_level': alo, 'max_level': ahi, 'species': 'SPECIES_' + a}
            B = {'min_level': blo, 'max_level': bhi, 'species': 'SPECIES_' + b}
            e['fishing_mons'] = {'encounter_rate': 30, 'mons': [A, B, A, B, B, A, B, A, B, B]}
        g['encounters'].append(e)
    open(JS, 'w', encoding='utf-8').write(json.dumps(d, indent=2, ensure_ascii=False) + '\n')
    for mp in sorted(maps):
        print(mp, [m['species'][8:] for m in land.get(mp, (0, []))[1]], FISH.get(mp, ''))

if __name__ == '__main__':
    main()
