"""Ethereal title-screen arrangement of "Conquest" (MapleStory2 MML, assets/music_source/conquest.ms2mml).

User (2026-11-17): original tempo 115 BPM; the whole song (60 bars) loops. First version (choir, strings, harp,
bells) was rejected -- "Do just a simpler more ethereal atmospheric piano instead". This is that version:
ONE soft piano (voicegroup194 program 0: Steinway sample, slow decay, long pedal-like release), heavy reverb.

  right hand  chord5 (part 5)  the main tune
  left hand   melody (part 0)  the slow bass progression Ab-Bb-C-G
  middle      chord6 (part 6)  one sustained harmony line, kept under the tune, very soft
  breakdown   chord1 (part 1)  only bars 38-43, where every other part rests: its soft broken chords
Everything else is left out so it breathes. Very high notes are folded down an octave.
Output: codebase/sound/songs/midi/mus_dr_title.mid (mid2agb flags in midi.cfg: -E -R110 -G194 -V100)."""
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
    ('rightHand', 5, 0, 118, 72, 88, None),
    ('leftHand',  0, 0, 110, 56, 72, None),
    ('middle',    6, 0,  80, 64, 76, None),
    ('breakdown', 1, 0,  96, 60, 84, lambda t: 37 * BAR <= t < 43 * BAR),   # bars 38-43: the broken chords carry it
]
def vel(v):
    return max(1, min(127, 40 + 5 * v))          # soft touch: v7 -> 75, v9 -> 85, v11 -> 95
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
        if name == 'leftHand':                                           # gentle swell into each loop
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
