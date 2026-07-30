#!/usr/bin/env python3
"""
Arrange the title theme MIDI for the GBA M4A engine.

WHY THIS EXISTS
---------------
Instrument choice in M4A is TWO knobs, and getting one right without the other
produces nonsense:

  1. the voicegroup (-G in midi.cfg) decides which sample sits at each program
  2. the MIDI's own program_change messages decide which programs are requested

The source MIDI asks for GM programs 0 (Acoustic Grand Piano), 88 (Pad 1 new
age) and 107 (Koto). Under the original -G059 those resolve to:

  prog   0 -> voice_keysplit voicegroup001   (a PERCUSSION keysplit)
  prog  88 -> voice_square_2_alt             (a chiptune square wave)
  prog 107 -> past the end of vg059's 89 entries entirely

So the piano line was playing as drums and the pad as a square lead. Whatever
that sounded like, it was accidental rather than chosen.

Voicegroup 193 (already proven in this ROM -- mus_osrid_theme uses it) carries
real orchestral samples, but its low programs are keysplits too, so switching
-G alone would still put the piano part on drums. The programs must be remapped.

CHOSEN MAPPING (voicegroup193)
------------------------------
  melody  ch0  -> 4  steinway_b_piano
  harmony ch1  -> 5  steinway_b_piano
  pad     ch2  -> 6  sc88pro_harp

REJECTED FIRST ATTEMPT -- kept as a warning
-------------------------------------------
The first pass used 79 sd90_enhanced_delay_shaku / 6 harp / 52
classical_choir_voice_ahhs, reasoning from the word "atmospheric". It grated
badly. The mistake was reasoning about sample LABELS instead of about how the
GBA actually plays them back:

  breath and vocal samples (shakuhachi, choir ahhs, whistle, female/male voice)
  turn nasal and piercing once M4A pitch-shifts them away from their root key,
  and sustaining them makes it worse. Struck and plucked samples (piano, harp,
  glockenspiel, tubular bell) resample cleanly and stay listenable.

So: prefer struck/plucked voices in vg193, and treat 52/53/54/77/78/79 as
special-effect voices only, at low volume or short duration if at all.

Alternatives within the piano family, if this still is not right:
  pad     -> 4  steinway_b_piano   (pure piano trio, no harp at all)
          -> 14 sc88pro_tubular_bell (colder, bell-like sustain)
          -> 8  sc88pro_glockenspiel (brighter, music-box)
  melody  -> 6  sc88pro_harp       (softer lead, piano moves to harmony only)

TEMPO
-----
Source is a single 73 BPM set_tempo. Raised to 80 BPM (+9.6%, the "about 10%"
asked for). Applied by rewriting the set_tempo message rather than rescaling
delta times, so note timing stays exactly as sequenced.

LOOPING
-------
mid2agb reads MIDI text meta-events (tools/mid2agb/midi.cpp:287): a text event
of exactly "[" is LoopBegin and "]" is LoopEnd. Both are inserted on track 0,
which makes every track's GOTO target its own _B1 label -- a seamless loop
rather than a restart.

Usage: python3 tools/audio/build_title_music.py [--bpm N] [--melody N]
                                                [--harmony N] [--pad N]
"""
import argparse
from pathlib import Path

import mido

HERE = Path(__file__).resolve().parent
SRC = HERE / "src" / "title_theme_source.mid"
OUT = HERE.parents[1] / "codebase" / "sound" / "songs" / "midi" / "mus_dr_title.mid"

# channel -> voicegroup193 program
DEFAULTS = {"melody": 4, "harmony": 5, "pad": 6}
CHANNEL_ROLE = {0: "melody", 1: "harmony", 2: "pad"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bpm", type=int, default=80)
    for k, v in DEFAULTS.items():
        ap.add_argument(f"--{k}", type=int, default=v)
    a = ap.parse_args()
    prog = {ch: getattr(a, role) for ch, role in CHANNEL_ROLE.items()}

    m = mido.MidiFile(str(SRC))
    print(f"source: {len(m.tracks)} tracks, {m.length:.1f}s, {m.ticks_per_beat} tpb")

    # tempo
    found = 0
    for t in m.tracks:
        for msg in t:
            if msg.type == "set_tempo":
                old = mido.tempo2bpm(msg.tempo)
                msg.tempo = mido.bpm2tempo(a.bpm)
                found += 1
                print(f"  tempo {old:.1f} -> {a.bpm} BPM (+{100*(a.bpm/old-1):.1f}%)")
    assert found, "no set_tempo in source"

    # instruments
    for t in m.tracks:
        for msg in t:
            if msg.type == "program_change" and msg.channel in prog:
                new = prog[msg.channel]
                print(f"  ch{msg.channel} prog {msg.program} -> {new} "
                      f"({CHANNEL_ROLE[msg.channel]})")
                msg.program = new

    # loop markers on track 0
    tr = m.tracks[0]
    tr[:] = [x for x in tr if not (x.is_meta and x.type == "text"
                                   and x.text in ("[", "]"))]
    tr.insert(0, mido.MetaMessage("text", text="[", time=0))
    end = max(sum(x.time for x in t) for t in m.tracks)
    tr.append(mido.MetaMessage("text", text="]",
                               time=max(0, end - sum(x.time for x in tr))))

    m.save(str(OUT))
    print(f"wrote {OUT}  ({mido.MidiFile(str(OUT)).length:.1f}s at {a.bpm} BPM)")


if __name__ == "__main__":
    main()
