"""Delete Emerald's own trainers (user 2026-11-27: "lets delete all non-used Emerald trainers so far and free up the
space"; list and reachability check in docs/hoenn_trainer_cut_list.md).

* opponents.h: the Emerald ids go; Dreamstone Mysteries' and ours are renumbered 1.. in their existing order;
  TRAINERS_COUNT follows. The Emerald names are kept only as aliases of TRAINER_NONE in
  constants/opponents_emerald_legacy.h, so the unreachable Emerald maps and engine tables that still name them compile
  until those maps are deleted in the wider Emerald clean-up.
* trainers.party: their parties go (every difficulty variant).
Emerald set = every TRAINER_* in vanilla pokeemerald's opponents.h (fetched to /tmp/r11/vanilla_opponents.h).
Run once from the repo root: python3 tools/cleanup/delete_hoenn_trainers.py"""
import re, sys
C = 'codebase/'
VAN = set(re.findall(r'#define (TRAINER_\w+)\s+\d+', open('/tmp/r11/vanilla_opponents.h').read())) - {'TRAINER_NONE'}
p = C + 'include/constants/opponents.h'; s = open(p).read()
ids = re.findall(r'^\s*#define (TRAINER_\w+)\s+(\d+)', s, re.M)
gone = [n for n, v in ids if n in VAN]
kept = [n for n, v in ids if n not in VAN and n != 'TRAINER_NONE']
new_id = {n: i + 1 for i, n in enumerate(kept)}
out = []
for line in s.splitlines():
    m = re.match(r'^(\s*)#define (TRAINER_\w+)(\s+)(\d+)(.*)$', line)
    if m and m.group(2) in VAN: continue
    if m and m.group(2) in new_id:
        line = '%s#define %s%s%d%s' % (m.group(1), m.group(2), m.group(3), new_id[m.group(2)], m.group(5))
    out.append(line)
s = '\n'.join(out) + '\n'
s = re.sub(r'#define TRAINERS_COUNT\s+\d+', '#define TRAINERS_COUNT                      %d' % (len(kept) + 1), s)
s = s.replace('#include "constants/battle_partner.h"\n',
              '#include "constants/battle_partner.h"\n#include "constants/opponents_emerald_legacy.h"   // deleted Emerald trainers -> TRAINER_NONE\n', 1)
open(p, 'w').write(s)
leg = ['#ifndef GUARD_CONSTANTS_OPPONENTS_EMERALD_LEGACY_H', '#define GUARD_CONSTANTS_OPPONENTS_EMERALD_LEGACY_H', '',
       '// Dreamstone Ruination (2026-11-27): Emerald\'s own trainers were deleted (tools/cleanup/delete_hoenn_trainers.py).',
       '// Their names stay as aliases of TRAINER_NONE (0) only so the unreachable Emerald maps and the Emerald-only engine',
       '// tables that still name them build; delete this file with those maps in the wider Emerald clean-up.', '']
leg += ['#define %-40s 0' % n for n in sorted(gone)] + ['', '#endif // GUARD_CONSTANTS_OPPONENTS_EMERALD_LEGACY_H', '']
open(C + 'include/constants/opponents_emerald_legacy.h', 'w').write('\n'.join(leg))
pp = C + 'src/data/trainers.party'; t = open(pp).read()
parts = re.split(r'(?m)^(?==== TRAINER_\w+ ===)', t)
keep_parts = []; dropped = 0
for part in parts:
    m = re.match(r'=== (TRAINER_\w+) ===', part)
    if m and m.group(1) in VAN: dropped += 1; continue
    keep_parts.append(part)
open(pp, 'w').write(''.join(keep_parts))
print('deleted ids', len(gone), 'kept', len(kept), 'party sections dropped', dropped, 'TRAINERS_COUNT', len(kept) + 1)
