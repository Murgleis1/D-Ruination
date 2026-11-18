"""MapleStory2 MML -> note events. Dialect: t tempo, v volume 0-15, o octave, l default length, a-g (+,#,- accidentals),
n<midi>, r rest, & tie, . dots, < > octave down/up. Ticks: 96 per quarter (TPQN 96)."""
import re, xml.etree.ElementTree as ET
TPQ = 96
SEMI = {'c': 0, 'd': 2, 'e': 4, 'f': 5, 'g': 7, 'a': 9, 'b': 11}
def length_ticks(num, dots, deflen, defdots=0):
    if not num: dots = dots + defdots
    base = 4 * TPQ / (num if num else deflen)
    t = base; add = base
    for _ in range(dots): add /= 2; t += add
    return t
def parse(src):
    s = re.sub(r'\s+', '', src.lower())
    i = 0; o = 4; L = 4; LD = 0; v = 8; t = 0.0; tempos = []; notes = []; tie = False; last = None
    def num():
        nonlocal i
        m = re.match(r'\d+', s[i:])
        if m: i += len(m.group()); return int(m.group())
        return None
    def dots():
        nonlocal i
        d = 0
        while i < len(s) and s[i] == '.': d += 1; i += 1
        return d
    while i < len(s):
        c = s[i]; i += 1
        if c == 't': tempos.append((t, num()))
        elif c == 'v': v = num()
        elif c == 'o': o = num()
        elif c == 'l': L = num(); LD = dots()
        elif c == '<': o -= 1
        elif c == '>': o += 1
        elif c == '&': tie = True
        elif c in 'abcdefgnr':
            if c == 'n': pitch = num(); ln = None; d = 0
            elif c == 'r': pitch = None
            else:
                pitch = 12 * (o + 1) + SEMI[c]
                while i < len(s) and s[i] in '+#-':
                    pitch += 1 if s[i] in '+#' else -1; i += 1
            if c != 'n':
                ln = num(); d = dots()
            if c == 'n':  # n takes the default length
                dur = length_ticks(None, dots(), L, LD)
            else:
                dur = length_ticks(ln, d, L, LD)
            if pitch is None:
                tie = False; t += dur; last = None; continue
            if tie and last is not None and notes[last][1] == pitch and abs(notes[last][0] + notes[last][2] - t) < 1e-6:
                notes[last][2] += dur
            else:
                notes.append([t, pitch, dur, v]); last = len(notes) - 1
            tie = False; t += dur
        elif c in ',;': pass
        else: raise ValueError('unknown %r at %d' % (c, i))
    return notes, tempos, t
def load(path):
    root = ET.parse(path).getroot()
    parts = [root.find('melody').text or ''] + [c.text or '' for c in root.findall('chord')]
    return [parse(p) for p in parts]
if __name__ == '__main__':
    P = load('conquest.ms2mml')
    NAMES = ['melody'] + ['chord%d' % k for k in range(1, 10)]
    for name, (n, tp, end) in zip(NAMES, P):
        if not n: print(name, 'empty'); continue
        ps = [x[1] for x in n]; vs = sorted(set(x[3] for x in n))
        print('%-7s notes %4d  end %6.1f beats  pitch %d..%d  vols %s  tempos %s' % (name, len(n), end / TPQ, min(ps), max(ps), vs, tp))
