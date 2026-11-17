"""Assemble the full Chapter 1 script (intro -> Eden's imprisonment) for review.
In-game text comes straight from the sources; parts still in draft come from the draft doc."""
import re, sys
R = '/home/claude/repo/'
C = R + 'codebase/'

NAMES = {'PORTRAIT_CADMUS': 'Cadmus', 'PORTRAIT_OSRID': 'Osrid', 'PORTRAIT_EDEN': 'Eden'}

def script_body(path, name):
    src = open(path, encoding='utf-8').read()
    i = src.index('script ' + name)
    j = src.index('{', i); depth = 0
    for k in range(j, len(src)):
        if src[k] == '{': depth += 1
        elif src[k] == '}':
            depth -= 1
            if depth == 0: return src[j + 1:k]

def clean(s):
    s = s.replace('\\n', ' ').replace('\\l', ' ')
    s = s.replace('{PLAYER}', 'Osrid')
    return [p.strip() for p in s.split('\\p') if p.strip()]

def render(body):
    out, speaker = [], None
    for line in body.splitlines():
        line = line.strip()
        m = re.match(r'showportrait\((\w+),', line)
        if m: speaker = NAMES.get(m.group(1), m.group(1)); continue
        m = re.match(r'speakername\("([^"]*)"\)', line)
        if m: speaker = m.group(1); continue
        if line.startswith('special(DrSetPrinceNameplate)'): speaker = 'Prince Osrid'; continue
        if line.startswith('closemessage'): speaker = None; continue
        if line.startswith('special(DrDoPlayerNaming)'):
            out.append('*[Naming screen: you sign your name.]*'); continue
        if line.startswith('playfanfare'): continue
        m = re.match(r'msgbox\(format\("(.*)"\)', line)
        if m:
            paras = clean(m.group(1))
            if speaker:
                out.append(f'**{speaker}:** ' + paras[0])
                out += paras[1:]
            else:
                out += [f'*{p}*' for p in paras]
    return '\n\n'.join(out)

def intro():
    src = open(C + 'src/dr_intro.c', encoding='utf-8').read()
    blocks = []
    for name in ['sTenebrisHeader', 'sTenebrisGreeting', 'sTenebrisP1', 'sTenebrisP2',
                 'sTenebrisP3', 'sTenebrisP4', 'sTenebrisP5']:
        m = re.search(r'static const u8 ' + name + r'\[\] = _\((.*?)\);', src, re.S)
        text = ''.join(re.findall(r'"((?:[^"\\]|\\.)*)"', m.group(1))).replace('\\n', ' ')
        blocks.append('> ' + re.sub(r'\s+', ' ', text).strip())
    return '\n\n'.join(blocks)

def draft_section(letter):
    t = open(R + 'docs/chapter1_dialogue_draft_after_briefing.md', encoding='utf-8').read()
    m = re.search(r'^## ' + letter + r'\. [^\n]*\n(.*?)(?=^---|^## )', t, re.S | re.M)
    return m.group(1).strip()

parts = [
 '# Dreamstone Ruination: Chapter 1, full script (opening to Eden\'s imprisonment)',
 'Review copy, generated 2026-11-16. **[IN GAME]** sections are exactly what the game shows now. '
 '**[DRAFT]** sections are the approved-so-far draft and are not in the game yet. '
 'Speaker names are shown on every line here for clarity; in game a name appears only when the speaker changes. '
 'Each paragraph is one text box (or a page of narration).',
 '## 1. Opening narration: Professor Tenebris  [IN GAME]', intro(),
 '## 2. The letter and Osrid\'s reply  [IN GAME]',
 render(script_body(C + 'data/maps/PellucaReflection/scripts.pory', 'PellucaReflection_Cutscene')),
 '## 3. Arrival at the Pelluca dock  [IN GAME]',
 render(script_body(C + 'data/maps/PellucaCity/scripts.pory', 'DR_PellucaCity_Arrival')),
 '## 4. Cadmus\'s lab: the briefing  [IN GAME]',
 render(script_body(C + 'data/maps/PellucaUmbraLab/scripts.pory', 'DR_Lab_Briefing')),
 '## 5. The starter notes beside each ball  [DRAFT]', draft_section('B'),
 '## 6. The theft  [DRAFT]', draft_section('C'),
 '## 7. The Templar holding cell  [DRAFT]', draft_section('D'),
 '## 8. Back at the lab: the shard briefing  [DRAFT]', draft_section('E'),
]
open(sys.argv[1], 'w', encoding='utf-8').write('\n\n'.join(parts) + '\n')
