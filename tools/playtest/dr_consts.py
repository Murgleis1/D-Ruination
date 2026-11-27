"""Evaluate the game's C constants (flags, vars, trainer ids) from the headers, so harness scripts never carry stale
numbers when flag space moves (MAX_TRAINERS_COUNT went 864 -> 1024 on 2026-11-27 and every system flag moved).
Also SaveBlock1's flag and var offsets, measured with offsetof."""
import subprocess, os, re, functools
C = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'codebase')
CC1 = '/usr/lib/gcc/arm-none-eabi/13.2.1/cc1'

def _cpp(src):
    return subprocess.run(['arm-none-eabi-cpp', '-iquote', 'include', '-DMODERN=1', '-DTESTING=0', '-'], input=src,
                          capture_output=True, text=True, cwd=C, check=True).stdout

@functools.lru_cache(None)
def const(name):
    """The integer value of a #define (e.g. FLAG_DR_STATUE_AWAKENED, TRAINER_DR_R11_FISHER_TAM)."""
    out = _cpp('#include "global.h"\n#include "constants/flags.h"\n#include "constants/vars.h"\n'
               '#include "constants/opponents.h"\n@@@ ' + name + '\n')
    expr = out.split('@@@', 1)[1].strip().splitlines()[0]
    return int(eval(re.sub(r'\b(0x[0-9A-Fa-f]+|\d+)[uU]?\b', r'\1', expr)))

@functools.lru_cache(None)
def saveblock1_offsets():
    src = '#include "global.h"\nconst int kF = offsetof(struct SaveBlock1, flags);\nconst int kV = offsetof(struct SaveBlock1, vars);\n'
    asm = subprocess.run([CC1, '-quiet', '-mthumb', '-O2', '-mabi=apcs-gnu', '-march=armv4t', '-std=gnu17', '-o', '-'],
                         input=_cpp(src), capture_output=True, text=True, cwd=C).stdout
    f = int(re.search(r'kF:\s*\.word\s+(\d+)', asm).group(1)); v = int(re.search(r'kV:\s*\.word\s+(\d+)', asm).group(1))
    return f, v

if __name__ == '__main__':
    import sys
    for n in sys.argv[1:]: print(n, hex(const(n)))
    print('SaveBlock1 flags/vars offsets', saveblock1_offsets())
