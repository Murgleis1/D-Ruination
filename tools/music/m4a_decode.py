"""Read an M4A (GBA 'Sappy') song out of a ROM into note lists: one pass through each track, up to its loop.

-> (tracks, loop_tick, header): tracks = [dict(notes=[(tick, key, dur, vel)], voice, vol, pan)], ticks at
24 per quarter note (the engine's own clock). Handles waits, notes (N1-N96 with running key/velocity/gate),
TIE/EOT, PATT/PEND (one level), REPT, GOTO (the loop: stops there and reports where it returns to), KEYSH.
Each track also lists played = [(program, key)] for every note (the key before KEYSH), for porting drum kits.
"""
import struct
LEN = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 28, 30, 32, 36,
       40, 42, 44, 48, 52, 54, 56, 60, 64, 66, 68, 72, 76, 78, 80, 84, 88, 90, 92, 96]

def decode(rom, table, index):
    u32 = lambda o: struct.unpack_from('<I', rom, o)[0]
    o = lambda v: (v & 0x0FFFFFFF) - 0x08000000
    h = o(u32(o(table) + 8 * index)); nt = rom[h]
    starts = [o(u32(h + 8 + 4 * k)) for k in range(nt)]
    out, loop_tick, tempo = [], None, None
    for s in starts:
        i, t, notes, ties, nv = s, 0, [], {}, []
        key, vel, gate, last, keysh = 60, 100, 0, None, 0
        stack, voice, vol, pan = [], None, 100, 64
        loop_at = None; labels = {s: 0}
        while True:
            labels.setdefault(i, t)
            b = rom[i]
            if b < 0x80:                       # running status
                if last is None: i += 1; continue
                b = last; i -= 1               # re-read as the last command with this byte as its argument
                rs = True
            else: rs = False
            if 0x80 <= b <= 0xB0:
                t += LEN[b - 0x80]; i += 1; continue           # (a wait keeps the running status)
            if b == 0xB1: break
            if b == 0xB2:
                tgt = o(u32(i + 1)); loop_at = labels.get(tgt); break
            if b == 0xB3: stack.append(i + 5); i = o(u32(i + 1)); continue
            if b == 0xB4:
                if stack: i = stack.pop(); continue
                i += 1; continue
            if b == 0xB5:                       # REPT n: the pattern n times (0: forever, taken once)
                n = max(1, rom[i + 1]); tgt = o(u32(i + 2))
                for _ in range(n - 1): stack.append(tgt)
                stack.append(i + 6); stack.reverse() if False else None
                ret = stack.pop(); stack.append(ret)       # return address on top after the repeats
                i = tgt; continue
            if b == 0xB9: i += 4; continue
            if 0xBA <= b <= 0xCD:
                a = rom[i + 1]
                if b == 0xBB: tempo = a * 2
                elif b == 0xBC: keysh = a - 256 if a > 127 else a
                elif b == 0xBD: voice = a
                elif b == 0xBE: vol = a
                elif b == 0xBF: pan = a
                last = b; i += 2; continue
            if b == 0xCE:                       # EOT [key]
                i += 1
                k = rom[i] if rom[i] < 0x80 else key
                if rom[i] < 0x80: i += 1
                if k in ties:
                    t0, v0 = ties.pop(k); notes.append((t0, k + keysh, t - t0, v0))
                last = 0xCE; continue
            if b >= 0xCF:                       # TIE or N
                last = b; i += 1
                if rom[i] < 0x80: key = rom[i]; i += 1
                if rom[i] < 0x80: vel = rom[i]; i += 1
                if rom[i] < 0x80: gate = rom[i]; i += 1
                if b == 0xCF: ties[key] = (t, vel); nv.append((voice, key))
                else: notes.append((t, key + keysh, LEN[b - 0xCF] + gate, vel)); nv.append((voice, key))
                continue
            i += 1
        out.append(dict(notes=notes, voice=voice, vol=vol, pan=pan, end=t, loop=loop_at, played=nv))
        if loop_at is not None: loop_tick = loop_at
    return out, loop_tick, tempo
