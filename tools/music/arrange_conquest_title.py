"""Title-screen arrangement of "Conquest" (MapleStory2 MML, assets/music_source/conquest.ms2mml) for solo piano.

User (2026-11-17): original tempo 115 BPM; the whole song (60 bars) loops; "a prettier, more ethereal, smooth,
rich piano". (Rejected before: a choir/strings/harp version, then a sparse version on one stretched piano sample
that sounded "downtuned and ugly".)

Instrument: voicegroup194 program 0 = the game's multi-sampled piano (sc88pro piano1 48/60/72/84 over
KeySplitTable1, as voicegroup005) with a pedal-like envelope (voicegroup195: slow decay, some sustain, long release).

  melody     part 5 (the tune), moved up an octave phrase by phrase where it sits low, kept at or below A5 (MEL_TOP)
             so the top piano sample and the engine reverb don't ring shrill (user)
  echo       the melody again a dotted eighth later, faint and short, panned to the other side (user: the first
             version had too much echo; now about half as loud)
  left hand  smooth eighth-note broken chords on each bar's chord -- root, 5th, octave, 10th, ... -- plus a soft
             low root on beat 1. Chords are read from the song: root = part 0's bass note for the bar; major or
             minor third = whichever the other parts actually play in that bar (else the C-minor key decides)
  inner      part 6, one quiet sustained harmony line in the middle register
  breakdown  part 1's own broken chords in bars 38-43, where the bass rests
Accompaniment and echo notes are short key presses; their ring is the release tail, which is what the sound
engine takes first when voices run short -- never the melody.
Output: codebase/sound/songs/midi/mus_dr_title.mid (mid2agb flags in midi.cfg)."""
import sys, os, collections
import mido
sys.path.insert(0, os.path.dirname(__file__))
import ms2mml
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(ROOT, 'assets', 'music_source', 'conquest.ms2mml')
OUT = os.path.join(ROOT, 'codebase', 'sound', 'songs', 'midi', 'mus_dr_title.mid')
TPQ = ms2mml.TPQ
BAR = 4 * TPQ
NBARS = 60
END = NBARS * BAR
E8 = TPQ // 2
BREAK = range(37, 43)                       # bars where part 1's broken chords carry it (0-based)
KEY_MINOR = {0: True, 5: True, 7: False, 8: False, 10: False, 3: False, 2: True}   # C minor: Cm Fm G Ab Bb Eb D(dim->m)

def sounding(notes, t0, t1):
    return [(t, p, d, v) for (t, p, d, v) in notes if t < t1 and t + d > t0]

def chords(parts):
    bass = parts[0][0]; out = {}; last = None
    for b in range(NBARS):
        t0, t1 = b * BAR, (b + 1) * BAR
        at1 = [n for n in sounding(bass, t0, t0 + TPQ)]
        if at1: last = min(n[1] for n in at1)
        elif not sounding(bass, t0, t1): last = None if b in BREAK else last
        if last is None: out[b] = None; continue
        r = last % 12; w = collections.Counter()
        for k in (1, 5, 6, 7, 8):
            for (t, p, d, v) in sounding(parts[k][0], t0, t1):
                w[p % 12] += min(t + d, t1) - max(t, t0)
        m3, M3 = w[(r + 3) % 12], w[(r + 4) % 12]
        minor = m3 > M3 if (m3 or M3) else KEY_MINOR.get(r, False)
        out[b] = (r, minor)
    return out

MEL_TOP = 81      # A5: above this the top piano sample + the engine's reverb ring shrill and bell-like (user)
def melody_shift(tune):
    """Per 4-bar phrase (keeps the tune's contour): +12 only if the phrase still fits under MEL_TOP,
    -12 (repeatedly) if it reaches above MEL_TOP."""
    sh = {}
    for ph in range(0, NBARS, 4):
        ns = sounding(tune, ph * BAR, (ph + 4) * BAR)
        if not ns: continue
        hi = max(p for _, p, _, _ in ns)
        k = 12 if hi + 12 <= MEL_TOP else 0
        while hi + k > MEL_TOP: k -= 12
        sh[ph] = k
    return sh

def build():
    parts = ms2mml.load(SRC)
    CH = chords(parts)
    tracks = collections.OrderedDict((k, []) for k in ('melody', 'echo', 'leftHand', 'inner', 'breakdown'))
    # melody + echo
    sh = melody_shift(parts[5][0])
    for (t, p, d, v) in parts[5][0]:
        if t >= END: continue
        q = p + sh.get(int(t // BAR) // 4 * 4, 0)
        while q > MEL_TOP: q -= 12
        tracks['melody'].append((t, q, d, 70 + 3 * v))
        if t + 3 * TPQ // 4 < END and q <= 76:          # no echo on the high notes (bell-like repeats)
            tracks['echo'].append((t + 3 * TPQ // 4, q, min(d, TPQ // 2), 30 + 2 * v))   # faint (user: too much echo)
    # left hand: broken chords from the song's own harmony
    for b, c in CH.items():
        if c is None or b in BREAK: continue
        r, minor = c
        root = 36 + (r - 36) % 12                      # C2..B2: low root octave
        third = 3 if minor else 4
        shape = [0, 7, 12, 12 + third, 19, 12 + third, 12, 7]
        t0 = b * BAR
        tracks['leftHand'].append((t0, root, BAR, 64))                       # soft low root, held the bar
        for i, iv in enumerate(shape):
            tracks['leftHand'].append((t0 + i * E8, root + 12 + iv, E8, 56 if i else 62))
    # inner harmony, folded into the middle register
    for (t, p, d, v) in parts[6][0]:
        if t >= END: continue
        while p > 72: p -= 12
        while p < 55: p += 12
        tracks['inner'].append((t, p, d, 44 + 2 * v))
    # breakdown
    for (t, p, d, v) in parts[1][0]:
        if int(t // BAR) in BREAK and t < END:
            tracks['breakdown'].append((t, p if p >= 40 else p + 12, d, 52 + 3 * v))
    SET = {'melody': (112, 70), 'echo': (48, 40), 'leftHand': (96, 56), 'inner': (76, 64), 'breakdown': (100, 60)}
    mid = mido.MidiFile(type=1, ticks_per_beat=TPQ)
    t0 = mido.MidiTrack(); mid.tracks.append(t0)
    t0.append(mido.MetaMessage('text', text='[', time=0))
    t0.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(115), time=0))
    t0.append(mido.MetaMessage('text', text=']', time=END))
    for ch, (name, notes) in enumerate(tracks.items()):
        vol, pan = SET[name]
        ev = []
        for (t, p, d, v) in notes:
            on = int(round(t)); off = int(round(min(t + d, END)))
            if off <= on: continue
            ev.append((on, 1, p, max(1, min(127, v)))); ev.append((off, 0, p, 0))
        ramp = [(int(i * BAR / 4), int(50 + (vol - 50) * i / 8)) for i in range(9)] if name == 'leftHand' else [(0, vol)]
        tr = mido.MidiTrack(); mid.tracks.append(tr)
        tr.append(mido.MetaMessage('track_name', name=name, time=0))
        msgs = [(0, -3, ('program_change', dict(program=0))), (0, -2, ('control_change', dict(control=10, value=pan)))]
        msgs += [(tt, -1, ('control_change', dict(control=7, value=vv))) for tt, vv in ramp]
        msgs += [(on, k, ('note_on' if k else 'note_off', dict(note=p, velocity=vv))) for (on, k, p, vv) in ev]
        msgs.sort(key=lambda m: (m[0], m[1]))
        now = 0
        for tt, _, (typ, kw) in msgs:
            tr.append(mido.Message(typ, channel=ch, time=tt - now, **kw)); now = tt
        tr.append(mido.MetaMessage('end_of_track', time=max(0, END - now)))
    mid.save(OUT)
    return mid, CH
if __name__ == '__main__':
    m, CH = build()
    names = 'C Db D Eb E F Gb G Ab A Bb B'.split()
    print('wrote', OUT, 'length %.1f s' % m.length)
    print(' '.join('%d:%s' % (b, '-' if c is None else names[c[0]] + ('m' if c[1] else '')) for b, c in CH.items()))
