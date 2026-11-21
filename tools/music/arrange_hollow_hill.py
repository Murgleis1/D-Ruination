"""Hollow Hill's theme: Ghost Grey's Route 1 theme (its song 291), re-arranged on our own instruments.

User 2026-11-20: Ghost Grey's Route 1 "with a piano base" sounded great; slower and slower (124 -> 72 bpm), the
tapping percussion out, "smoother, with your own piano and ethereal-ness", and in the gaps where the song almost
drops off "a ghostly echo ... or the sound of the wind ... something eerie". It became Hollow Hill's theme (foggy,
haunted, the thinnest place between worlds) rather than Route 11's.

The song is 24 bars, looped: bars 0-11 carry the tune over slow chords; in bars 12-23 the tune falls silent and
only the chords go on, every third bar empty. The arrangement (all decoded from the ROM: tools/music/m4a_decode.py):
  melody   the tune, on the soft "pedal" piano (voicegroup195 via 196, program 0): short key presses, the release
           tail is the ring
  chords   Ghost Grey's own piano chords, softer
  counter  its four-note counter-line, piano
  echo     the ghostly echo: in the silent half the tune comes back as a far-off voice (the soft female voice,
           program 53, slow to swell): the first note of each half bar of bar b-12, held two beats, panned away.
           (A first try used a sine on the wave channel; the user heard it as random beeps.)
  wind     gusts of noise (the GBA's noise channel, program 83), swelling in and dying away, over the empty bars
           and the hush at the end of the first half
The wind uses the GBA's own noise channel; the echo plays only where the tune is silent, so with the chords it
stays within the five sampled voices the game allows (too many at once is what made the first port crackle). Engine reverb is turned well up (midi.cfg).
Credit: Ghost Grey (the composition).
Output: codebase/sound/songs/midi/mus_dr_hollow_hill.mid
"""
import os, sys
import mido
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import m4a_decode as D
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(ROOT, 'codebase', 'sound', 'songs', 'midi', 'mus_dr_hollow_hill.mid')
GG_ROM, GG_TABLE, GG_SONG = '/home/claude/ghostgrey/Ghost_Grey_EX.gba', 0x8F8C2C0, 291
BPM = 72
S = 4                          # MIDI ticks per engine tick (96 per quarter here, 24 in the engine)
BAR = 96                       # engine ticks per bar
NBARS = 24

def build():
    tr, loop, tempo = D.decode(open(GG_ROM, 'rb').read(), GG_TABLE, GG_SONG)
    mel, chords, counter = tr[0]['notes'], tr[1]['notes'], tr[2]['notes']
    end = NBARS * BAR
    parts = {}
    parts['melody'] = [(t, p, max(d, 10), 84) for t, p, d, v in mel]
    parts['chords'] = [(t, p, d, 54) for t, p, d, v in chords]
    parts['counter'] = [(t, p, d, 62) for t, p, d, v in counter]
    echo = []
    for t, p, d, v in mel:                                   # bars 0-11 -> 12-23: the tune's first note of each
        if t % 48: continue                                  # half bar, held two beats, a voice far off
        echo.append((t + 12 * BAR, p, 46, 60))
    parts['echo'] = echo
    wind = []
    for i, b in enumerate((11, 14, 17, 20, 23)):             # the hush and the empty bars
        key = (62, 59, 64, 58, 61)[i]                        # (a high hiss: low noise keys thud like a drum)
        wind.append((b * BAR, key, BAR + 24 if b < 23 else BAR, 36 if b == 11 else 48))
    parts['wind'] = wind
    SET = {  # program, volume, pan
        'melody': (0, 100, 58), 'chords': (0, 72, 64), 'counter': (0, 70, 70), 'echo': (53, 58, 80), 'wind': (83, 34, 64)}
    mid = mido.MidiFile(type=1, ticks_per_beat=24 * S)
    t0 = mido.MidiTrack(); mid.tracks.append(t0)
    t0.append(mido.MetaMessage('text', text='[', time=0))
    t0.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(BPM), time=0))
    t0.append(mido.MetaMessage('text', text=']', time=end * S))
    for ch, (name, notes) in enumerate(parts.items()):
        prog, vol, pan = SET[name]
        ev = []
        for (t, p, d, v) in notes:
            on, off = t * S, min(t + d, end) * S
            if off <= on: continue
            ev.append((on, 1, p, v)); ev.append((off, 0, p, 0))
        tr_ = mido.MidiTrack(); mid.tracks.append(tr_)
        tr_.append(mido.MetaMessage('track_name', name=name, time=0))
        msgs = [(0, -3, ('program_change', dict(program=prog))), (0, -2, ('control_change', dict(control=10, value=pan))),
                (0, -1, ('control_change', dict(control=7, value=vol)))]
        msgs += [(on, k, ('note_on' if k else 'note_off', dict(note=p, velocity=vv))) for (on, k, p, vv) in ev]
        msgs.sort(key=lambda m: (m[0], m[1]))
        now = 0
        for tt, _, (typ, kw) in msgs:
            tr_.append(mido.Message(typ, channel=ch, time=tt - now, **kw)); now = tt
        tr_.append(mido.MetaMessage('end_of_track', time=max(0, end * S - now)))
    mid.save(OUT)
    return mid

if __name__ == '__main__':
    m = build(); print('wrote', OUT, 'loop %.1f s' % m.length)
