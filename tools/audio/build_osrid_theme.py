#!/usr/bin/env python3
"""
Arrange Osrid's Theme for the GBA M4A engine.

SCOPE -- WHY THIS REPLACES THE MIDI RATHER THAN ADDING A SONG
-------------------------------------------------------------
The requested span was "Tenebris's letter through Osrid signing the letter and
arriving at Pelluca Valley". That span is already covered by a single constant:

  src/dr_intro.c:124                     m4aSongNumStart(MUS_OSRID_THEME)
  data/maps/PellucaReflection/header.inc  .2byte MUS_OSRID_THEME

So swapping the MIDI behind MUS_OSRID_THEME (index 628) covers the whole
sequence with no C or script changes. The previous 456s single-track version is
preserved beside this file as osrid_theme_v1_ORIGINAL.mid -- it is NOT deleted,
only superseded, so it can be restored by pointing SRC at it.

SIDE EFFECT, deliberate: PellucaReflection's map music changes too. That map is
part of the same cold open, so this is wanted -- but it is a second place the
change lands, not just the intro.

INSTRUMENT MAPPING
------------------
The source is already piano/harp-led with no channel-9 drum track, so there is
no drum-selector hazard. But three of its GM programs resolve to KEYSPLITS in
voicegroup193 and would have played as percussion:

  ch1  46 Orchestral Harp   -> KEYSPLIT  ->  6 sc88pro_harp
  ch2   2 Electric Grand    -> KEYSPLIT  ->  4 steinway_b_piano
  ch3  24 Nylon Guitar      -> already sc88pro_nylon_str_guitar, left alone
  ch4  50 Synth Strings     -> KEYSPLIT  -> 14 sc88pro_tubular_bell
  ch5  89 Warm Pad          ->           ->  8 sc88pro_glockenspiel
  ch6  24 Nylon Guitar      -> 25 sc88pro_nylon_str_guitar (same sample, own
                                 program so the two guitar lines stay separately
                                 tweakable)

vg193 has NO sustained string ensemble or synth pad -- programs 44-51, where GM
puts strings, are keysplits. So the two sustained parts (synth strings, warm pad)
become the tubular bell and glockenspiel: struck voices with long tails, which
is both what "soothing ethereal bell synths" asks for and what survives M4A
resampling. Breath and vocal samples (52/53/54, 77/78/79) are avoided entirely
after the choir attempt on the title theme grated.

"Light percussive" is carried by the plucked and struck attacks -- harp, nylon
guitar, glockenspiel -- not by a drum kit. There is no percussion track in the
source and none was invented here.

TEMPO
-----
Source is a single 80 BPM set_tempo and is left alone; no speed change was
requested for this piece.

Usage: python3 tools/audio/build_osrid_theme.py [--bpm N] [--harp N]
           [--piano N] [--bell N] [--shimmer N] [--no-loop]
"""
import argparse
from pathlib import Path

import mido

HERE = Path(__file__).resolve().parent
SRC = HERE / "src" / "osrid_theme_source.mid"
OUT = HERE.parents[1] / "codebase" / "sound" / "songs" / "midi" / "mus_osrid_theme.mid"

# midi channel -> voicegroup193 program.  None = leave the source program alone.
ROLES = {1: "harp", 2: "piano", 3: None, 4: "bell", 5: "shimmer", 6: "guitar2"}
DEFAULTS = {"harp": 6, "piano": 4, "bell": 14, "shimmer": 8, "guitar2": 25}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bpm", type=int, default=None, help="override tempo")
    for k, v in DEFAULTS.items():
        ap.add_argument(f"--{k}", type=int, default=v)
    ap.add_argument("--no-loop", action="store_true")
    a = ap.parse_args()
    prog = {ch: getattr(a, role) for ch, role in ROLES.items() if role}

    m = mido.MidiFile(str(SRC))
    print(f"source: {len(m.tracks)} tracks, {m.length:.1f}s, {m.ticks_per_beat} tpb")

    if a.bpm:
        for t in m.tracks:
            for msg in t:
                if msg.type == "set_tempo":
                    old = mido.tempo2bpm(msg.tempo)
                    msg.tempo = mido.bpm2tempo(a.bpm)
                    print(f"  tempo {old:.1f} -> {a.bpm} BPM")

    for t in m.tracks:
        for msg in t:
            if msg.type == "program_change" and msg.channel in prog:
                new = prog[msg.channel]
                if new != msg.program:
                    print(f"  ch{msg.channel} prog {msg.program} -> {new}")
                msg.program = new

    if not a.no_loop:
        tr = m.tracks[0]
        tr[:] = [x for x in tr if not (x.is_meta and x.type == "text"
                                       and x.text in ("[", "]"))]
        tr.insert(0, mido.MetaMessage("text", text="[", time=0))
        end = max(sum(x.time for x in t) for t in m.tracks)
        tr.append(mido.MetaMessage("text", text="]",
                                   time=max(0, end - sum(x.time for x in tr))))
        print("  loop markers written to track 0")

    m.save(str(OUT))
    r = mido.MidiFile(str(OUT))
    notes = sum(1 for t in r.tracks for x in t
                if x.type == "note_on" and x.velocity > 0)
    print(f"wrote {OUT}\n  {r.length:.1f}s, {notes} notes")


if __name__ == "__main__":
    main()
