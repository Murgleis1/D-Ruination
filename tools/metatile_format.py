"""Ruination metatile format (since 2026-11-15, commit d18a04803): TRIPLE-LAYER.

Each metatile = 12 u16 entries = 24 bytes:
    0-3  bottom -> BG3   (index 0 shows the backdrop)
    4-7  middle -> BG2   (index 0 transparent)
    8-11 top    -> BG1   (index 0 transparent; drawn over object sprites)
drawn regardless of the layer-type attribute. Entry bits: tile 0-9, hflip 10,
vflip 11, palette slot 12-15.
"""
import os, struct, sys

ENTRIES = 12
BYTES = 24

def read(path):
    raw = open(path, 'rb').read()
    if len(raw) % BYTES:
        raise SystemExit(f'{path}: {len(raw)} bytes is not a multiple of {BYTES}; not triple-layer data')
    return [struct.unpack_from('<12H', raw, i * BYTES) for i in range(len(raw) // BYTES)]

def legacy_two_layer_guard(script):
    """Hard stop for scripts written for the old 16-byte, 2-layer format."""
    raise SystemExit(
        f'{os.path.basename(script)} was written for 2-layer (16-byte) metatiles.\n'
        f'Ruination now uses triple-layer metatiles (24 bytes, see tools/metatile_format.py).\n'
        f'Running it unchanged would misread every tileset and could corrupt metatiles.bin.\n'
        f'Port it to metatile_format first.')
