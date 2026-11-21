"""Port one song out of MonoMyth's ROM into ours, note for note (user 2026-11-20: the ice path plays the Old
Headquarters' music).

MonoMyth's songs are ordinary M4A songs (song table at 0x8E3AE10, its pointers carry a stray top bit: masked off).
This copies, as data, everything the song needs:
  * the tracks' bytecode (one contiguous block), with its GOTO / PATT / REPT pointers relocated to labels;
  * a voicegroup of 128 voices: the voices the song selects (VOICE commands) copied from MonoMyth's, every other
    slot a silent square voice; keysplit voices with their sub-voicegroup and key table; drum kits with their
    128-voice sub-voicegroup; DirectSound samples and programmable waves copied byte for byte (shared ones once);
  * the song header (track count, priority, reverb).
Output: sound/songs/<label>.s (assembled into song_data with the other songs) and the samples as
sound/monomyth/<label>/*.bin. The song still has to be listed in sound/song_table.inc and include/constants/songs.h.
Credit: MonoMyth (its music).
Usage: python3 tools/monomyth/port_song.py <song index> <label>     (e.g. 677 mus_dr_old_hq)
Other games (user 2026-11-20: Ghost Grey's Route 1): set the ROM, its song table and the credit by environment:
  PORT_ROM=/home/claude/ghostgrey/Ghost_Grey_EX.gba PORT_TABLE=0x8F8C2C0 PORT_CREDIT="Ghost Grey" PORT_DIR=ghostgrey
  (the samples then go to sound/ported/<PORT_DIR>/<label>/)
"""
import os, sys, struct
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
if 'PORT_ROM' in os.environ: os.environ['MONOMYTH_ROM'] = os.environ['PORT_ROM']
from romlib import ROM, u32
C = os.path.normpath(os.path.join(HERE, '..', '..', 'codebase'))
SONG_TABLE = int(os.environ.get('PORT_TABLE', '0x8E3AE10'), 0)
CREDIT = os.environ.get('PORT_CREDIT', 'MonoMyth')
SDIR = ('sound/ported/' + os.environ['PORT_DIR']) if 'PORT_DIR' in os.environ else 'sound/monomyth'

def o(v): return (v & 0x0FFFFFFF) - 0x08000000
def ptr_ok(v): return 0 <= o(v) < len(ROM)

def decode(start, end):
    """Walk the tracks' block; -> {offset of a 4-byte pointer operand: target address}, programs selected."""
    ptrs, progs, i, last = {}, set(), start, None
    while i < end:
        b = ROM[i]
        if b in (0xB2, 0xB3):                               # GOTO, PATT
            ptrs[i + 1] = u32(i + 1); i += 5; last = None; continue
        if b == 0xB5:                                       # REPT count, address
            ptrs[i + 2] = u32(i + 2); i += 6; last = None; continue
        if b == 0xB9: i += 4; last = None; continue         # MEMACC op, address, data
        if b == 0xBD:                                       # VOICE program
            progs.add(ROM[i + 1]); last = 0xBD; i += 2; continue
        if 0xBA <= b <= 0xCD: last = b; i += 2; continue    # one-argument commands (XCMD's own args follow as < 0x80)
        if b < 0x80:
            if last == 0xBD: progs.add(b)                    # running status: another VOICE
            i += 1; continue
        if b >= 0xCF or b == 0xCE: last = b
        i += 1
    return ptrs, progs

def main(index, label):
    entry = o(SONG_TABLE) + 8 * index
    hdr = o(u32(entry)); nt, nb, pri, rev = ROM[hdr:hdr + 4]; vg = u32(hdr + 4)
    tracks = [u32(hdr + 8 + 4 * k) for k in range(nt)]
    start = min(o(t) for t in tracks); end = hdr                 # the tracks lie just before their header
    ptrs, progs = decode(start, end)
    for at, v in ptrs.items(): assert start <= o(v) < end, f'pointer at {at:#x} -> {v:#x} leaves the song'
    out = [f'@ {label}: {CREDIT} song {index} (header {u32(entry) & 0x0FFFFFFF:#x}), ported by tools/monomyth/port_song.py',
           f'@ Credit: {CREDIT} (its music).', '', '\t.section .rodata', '\t.align 2', '']
    # ---- the tracks ----
    out.append(f'{label}_tracks:')
    starts = {o(t): k for k, t in enumerate(tracks)}
    targets = {o(v) for v in ptrs.values()}
    i = start
    while i < end:
        if i in starts: out.append(f'{label}_{starts[i] + 1}:')
        if i in targets and i not in starts: out.append(f'{label}_at_{i - start:05X}:')
        if i in ptrs:
            t = o(ptrs[i]); name = f'{label}_{starts[t] + 1}' if t in starts else f'{label}_at_{t - start:05X}'
            out.append(f'\t.4byte {name}'); i += 4; continue
        j = i
        while j < end and j - i < 16 and not (j > i and (j in starts or j in targets or j in ptrs)) and j not in ptrs: j += 1
        if j == i: j = i + 1
        out.append('\t.byte ' + ', '.join(f'0x{x:02X}' for x in ROM[i:j])); i = j
    out += ['', '\t.align 2']
    # ---- voices and samples ----
    sdir = os.path.join(C, SDIR, label); os.makedirs(sdir, exist_ok=True)
    samples, waves, groups, tables = {}, {}, {}, {}
    def sample(v):
        a = o(v)
        if a not in samples:
            size = struct.unpack_from('<I', ROM, a + 12)[0]; n = 16 + size + 1
            name = f'{label}_sample_{len(samples):02d}'; samples[a] = name
            open(os.path.join(sdir, name + '.bin'), 'wb').write(ROM[a:a + n])
        return samples[a]
    def wave(v):
        a = o(v)
        if a not in waves: waves[a] = f'{label}_wave_{len(waves):02d}'
        return waves[a]
    def voice(a, used):
        """One 12-byte voice at ROM offset a -> assembly lines (silent if not used)."""
        if not used: return ['\t.byte 0x01, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0   @ unused']
        t = ROM[a]; b = ROM[a:a + 12]
        if t == 0x40:                          # keysplit
            return [f'\t.byte 0x{b[0]:02X}, 0x{b[1]:02X}, 0x{b[2]:02X}, 0x{b[3]:02X}', f'\t.4byte {group(u32(a + 4), keys=u32(a + 8))}',
                    f'\t.4byte {table(u32(a + 8))}']
        if t == 0x80:                                                              # drum kit
            return [f'\t.byte 0x{b[0]:02X}, 0x{b[1]:02X}, 0x{b[2]:02X}, 0x{b[3]:02X}', f'\t.4byte {group(u32(a + 4))}',
                    '\t.byte ' + ', '.join(f'0x{x:02X}' for x in b[8:12])]
        k = t & 0x07
        head = f'\t.byte 0x{b[0]:02X}, 0x{b[1]:02X}, 0x{b[2]:02X}, 0x{b[3]:02X}'
        tail = '\t.byte ' + ', '.join(f'0x{x:02X}' for x in b[8:12])
        if k == 0: return [head, f'\t.4byte {sample(u32(a + 4))}', tail]            # DirectSound
        if k == 3: return [head, f'\t.4byte {wave(u32(a + 4))}', tail]              # programmable wave
        return ['\t.byte ' + ', '.join(f'0x{x:02X}' for x in b)]                    # square / noise
    pending = []
    def group(v, keys=None):
        a = o(v)
        if a not in groups:
            groups[a] = f'{label}_group_{len(groups):02d}'
            used = set(ROM[o(keys) + k] for k in range(128)) if keys else set(range(128))
            pending.append((a, groups[a], used))
        return groups[a]
    def table(v):
        a = o(v)
        if a not in tables:
            tables[a] = f'{label}_keys_{len(tables):02d}'
        return tables[a]
    out.append(f'{label}_voices:')
    for p in range(128): out += voice(o(vg) + 12 * p, p in progs)
    while pending:
        a, name, used = pending.pop(0)
        out += ['', '\t.align 2', f'{name}:']
        for p in range(128): out += voice(a + 12 * p, p in used)
    for a, name in tables.items(): out += ['', f'{name}:', '\t.byte ' + ', '.join(str(x) for x in ROM[a:a + 128])]
    for a, name in waves.items(): out += ['', '\t.align 2', f'{name}:', '\t.byte ' + ', '.join(f'0x{x:02X}' for x in ROM[a:a + 16])]
    for a, name in samples.items(): out += ['', '\t.align 2', f'{name}:', f'\t.incbin "{SDIR}/{label}/{name}.bin"']
    # ---- the header ----
    out += ['', '\t.align 2', f'\t.global {label}', f'{label}:', f'\t.byte {nt}, {nb}, {pri}, 0x{rev:02X}', f'\t.4byte {label}_voices']
    out += [f'\t.4byte {label}_{k + 1}' for k in range(nt)]
    open(os.path.join(C, 'sound', 'songs', label + '.s'), 'w').write('\n'.join(out) + '\n')
    total = sum(16 + struct.unpack_from('<I', ROM, a + 12)[0] + 1 for a in samples)
    print(f'{label}: song {index}, {nt} tracks, {end - start} bytes of tracks, programs {sorted(progs)}, '
          f'{len(groups)} sub-voicegroups, {len(samples)} samples ({total} bytes), reverb {rev:#x}')

if __name__ == '__main__':
    main(int(sys.argv[1]), sys.argv[2])
