"""Ethereal title-screen arrangement of "Conquest" (MapleStory2 MML, assets/music_source/conquest.ms2mml).

User choices (2026-11-17): original tempo 115 BPM; choir + strings + harp + bells; the whole song (60 bars) loops.
Voicegroup 194 = voicegroup 193 with soft-attack / long-release choir, voice and strings.

Part roles in the MML and their voices here:
  melody (part 0)  slow bass progression Ab-Bb-C-G   -> soft low strings (48), swell in at the loop start
  chord1 (part 1)  bass doubled an octave down, later arpeggios -> doubling dropped (airier); bars 33+ on harp (6)
  chord5 (part 5)  the main tune                     -> female voice 'aah' (53)
  chord6/7         sustained harmony + high shimmer  -> choir 'aahs' (52), panned left / right
  chord8           counter-melody, high accents      -> glockenspiel (8)
  chord2/3         second-half fills                 -> harp (6/7)
  chord4           three accent notes                -> tubular bell (14)
Very high notes are folded down an octave per voice (thin, chirpy samples up there).
Output: codebase/sound/songs/midi/mus_dr_title.mid (mid2agb flags in midi.cfg: -E -R100 -G194 -V090)."""
import sys, os
import mido
sys.path.insert(0, os.path.dirname(__file__))
import ms2mml
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(ROOT, 'assets', 'music_source', 'conquest.ms2mml')
OUT = os.path.join(ROOT, 'codebase', 'sound', 'songs', 'midi', 'mus_dr_title.mid')
TPQ = ms2mml.TPQ
BAR = 4 * TPQ
END = 60 * BAR
# (part, program, track volume, pan, fold-above, keep(start_tick) predicate)
TRACKS = [
    ('tune',    5, 53, 104, 64, 84, None),
    ('choirL',  6, 52,  74, 40, 81, None),
    ('choirR',  7, 52,  74, 88, 81, None),
    ('strings', 0, 48,  84, 64, 96, None),
    ('harpArp', 1,  6,  78, 92, 96, lambda t: t >= 32 * BAR),
    ('glock',   8,  8,  60, 32, 96, None),
    ('harpA',   2,  6,  70, 30, 96, None),
    ('harpB',   3,  7,  66, 98, 96, None),
    ('bell',    4, 14,  64, 64, 84, None),
]
def vel(v):
    return max(1, min(127, 30 + 7 * v))
def build():
    parts = ms2mml.load(SRC)
    mid = mido.MidiFile(type=1, ticks_per_beat=TPQ)
    t0 = mido.MidiTrack(); mid.tracks.append(t0)
    t0.append(mido.MetaMessage('text', text='[', time=0))                 # loop start (mid2agb)
    t0.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(115), time=0))
    t0.append(mido.MetaMessage('text', text=']', time=END))               # loop end: the whole song
    for ch, (name, part, prog, vol, pan, fold, keep) in enumerate(TRACKS):
        notes, _, _ = parts[part]
        ev = []
        for (t, p, d, v) in notes:
            if keep and not keep(t): continue
            if t >= END: continue
            while p > fold: p -= 12
            on = int(round(t)); off = int(round(min(t + d, END)))
            if off <= on: continue
            ev.append((on, 1, p, vel(v))); ev.append((off, 0, p, 0))
        if name == 'strings':                                            # gentle swell into each loop
            ramp = [(int(i * BAR / 4), int(40 + (vol - 40) * i / 8)) for i in range(9)]
        else:
            ramp = [(0, vol)]
        tr = mido.MidiTrack(); mid.tracks.append(tr)
        tr.append(mido.MetaMessage('track_name', name=name, time=0))
        msgs = [(0, -3, ('program_change', dict(program=prog))), (0, -2, ('control_change', dict(control=10, value=pan)))]
        msgs += [(tt, -1, ('control_change', dict(control=7, value=vv))) for tt, vv in ramp]
        ev.sort(key=lambda e: (e[0], e[1]))                              # note-offs before note-ons at a tick
        msgs += [(on, k, ('note_on' if k else 'note_off', dict(note=p, velocity=vv))) for (on, k, p, vv) in ev]
        msgs.sort(key=lambda m: (m[0], m[1]))
        now = 0
        for tt, _, (typ, kw) in msgs:
            tr.append(mido.Message(typ, channel=ch, time=tt - now, **kw)); now = tt
        tr.append(mido.MetaMessage('end_of_track', time=max(0, END - now)))
    mid.save(OUT)
    return mid
if __name__ == '__main__':
    m = build()
    print('wrote', OUT, 'tracks', len(m.tracks), 'length %.1f s' % m.length)
