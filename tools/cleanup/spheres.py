"""PokéSpheres (user 2026-11-27): in the Cormorian Empire Poké Balls are PokéSpheres (bible 13, "Lost technology").
Renames every capture ball and every player-visible mention of a Poké Ball to a Sphere, inside string literals only
(item names and descriptions, battle and menu text, Pokédex entries, ability and move descriptions, every map's script
text), so code identifiers and graphics paths are untouched. The Master Ball keeps its name: the Empire never made
one (the concept existed only in theory; Silph's Master Ball came two thousand years later).
Run from the repo root: python3 tools/cleanup/spheres.py   (idempotent)"""
import re, os, sys
C = 'codebase/'
ITEMS = C + 'src/data/items.h'
src = open(ITEMS).read()
# the capture balls, from their pocket
balls = []
for m in re.finditer(r'\n    \[(ITEM_\w+)\] =\n    \{(.*?)\n    \},', src, re.S):
    if 'POCKET_POKE_BALLS' in m.group(2):
        nm = re.search(r'\.name = (?:ITEM_NAME|_)\("([^"]+)"\)', m.group(2)).group(1)
        balls.append((m.group(1), nm))
names = [n[:-5] for i, n in balls if n.endswith(' Ball') and i not in ('ITEM_MASTER_BALL', 'ITEM_POKE_BALL')]
RULES = [(r'Poké Balls', 'Poké Spheres'), (r'Poké Ball', 'Poké Sphere'), (r'Pokéballs', 'Poké Spheres'),
         (r'Pokéball', 'Poké Sphere'), (r'Poke Balls', 'Poké Spheres'), (r'Poke Ball', 'Poké Sphere'),
         (r'POKé BALLS', 'POKé SPHERES'), (r'POKé BALL', 'POKé SPHERE'), (r'POKéBALLS', 'POKé SPHERES'),
         (r'POKéBALL', 'POKé SPHERE')]
for n in names:
    RULES += [(n + ' Balls', n + ' Spheres'), (n + ' Ball', n + ' Sphere'),
              (n.upper() + ' BALLS', n.upper() + ' SPHERES'), (n.upper() + ' BALL', n.upper() + ' SPHERE')]
# a few lone "Ball"s that mean a capture ball
EXTRA = [('You throw a Ball now', 'You throw a Sphere now'), ('one in a BALL', 'one in a SPHERE'),
         ('BALLS thrown by', 'SPHERES thrown by'), ('"Ball{CLEAR_TO 56}', '"Sphere{CLEAR_TO 56}')]
STR = re.compile(r'"((?:[^"\\\n]|\\.)*)"')
def fix_literal(m):
    t = m.group(1)
    if '/' in t and ('.png' in t or '.4bpp' in t or 'graphics' in t or '.bin' in t): return m.group(0)
    for a, b in RULES: t = re.sub(r'(?<![A-Za-z])' + re.escape(a) + r'(?![A-Za-z])', b, t)
    return '"' + t + '"'
changed = 0
for root, dirs, files in os.walk(C):
    if root.startswith(C + 'build') or root.startswith(C + 'tools') or '/.git' in root or root.startswith(C + 'test'): continue
    for f in files:
        if not f.endswith(('.c', '.h', '.inc', '.pory', '.s', '.party', '.txt')): continue
        p = os.path.join(root, f)
        try: s = open(p, encoding='utf-8').read()
        except UnicodeDecodeError: continue
        t = STR.sub(fix_literal, s)
        for a, b in EXTRA: t = t.replace(a, b)
        if t != s: open(p, 'w', encoding='utf-8').write(t); changed += 1
# ball descriptions: the lone word Ball -> Sphere (not the Master Ball)
src = open(ITEMS).read()
def desc_fix(m):
    if m.group(1) == 'ITEM_MASTER_BALL' or 'POCKET_POKE_BALLS' not in m.group(2): return m.group(0)
    body = re.sub(r'(\.description = COMPOUND_STRING\()(.*?)(\),\n)',
                  lambda d: d.group(1) + re.sub(r'(?<![A-Za-z])Ball(?![A-Za-z])', 'Sphere', d.group(2)) + d.group(3), m.group(2), flags=re.S)
    return '\n    [%s] =\n    {%s\n    },' % (m.group(1), body)
src = re.sub(r'\n    \[(ITEM_\w+)\] =\n    \{(.*?)\n    \},', desc_fix, src, flags=re.S)
open(ITEMS, 'w').write(src)
print('files changed', changed, 'ball names', len(names) + 1)
# report ball description lines over 20 characters
for m in re.finditer(r'\n    \[(ITEM_\w+)\] =\n    \{(.*?)\n    \},', src, re.S):
    if 'POCKET_POKE_BALLS' not in m.group(2): continue
    d = re.search(r'\.description = COMPOUND_STRING\((.*?)\),\n', m.group(2), re.S)
    if not d: continue
    for line in ''.join(re.findall(r'"((?:[^"\\]|\\.)*)"', d.group(1))).split('\\n'):
        if len(line) > 20: print('  long:', m.group(1), repr(line))
