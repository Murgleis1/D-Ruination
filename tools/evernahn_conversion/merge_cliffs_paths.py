#!/usr/bin/env python3
"""
THE IMMEDIATE NEXT STEP (awaiting user OK on autumn_cliffs.png/autumn_paths.png).

Merge the selected gTileset_Autumn cliff/path metatiles INTO gTileset_Evernahn.
Autumn palettes 2+3 won a colour-distance match against the layout reference
(cliff 23.0, path 13.4 - best on both). They go into Evernahn's FREE sub-palette
slots 3 and 4, so the colours copy across with NO quantising.

Run from repo root:  python3 tools/evernahn_conversion/merge_cliffs_paths.py
Then:  cd codebase && timeout 290 make modern

Reads the committed selection:
  assets/pelluca_dock_spec/autumn_cliff_path_selection.json

WHAT IT DOES
  1. Load Evernahn's current tiles/metatiles/attrs/palettes (46 metatiles).
  2. Load autumn's tiles + palettes 2,3.
  3. Put autumn pal2 -> Evernahn slot 3, autumn pal3 -> Evernahn slot 4.
  4. For each selected autumn metatile: pull its four 8x8 tiles, remap any pixel
     drawn with autumn pal2/pal3 so it indexes the SAME colour in the new slot
     (autumn pal2/3 -> evernahn 3/4 is a straight slot swap since colours are
     copied identically), append the tiles (deduped) into evernahn/tiles.png,
     append the metatile entry (with palette field rewritten to 3 or 4) and its
     attribute (behaviour MB_NORMAL for cliff+path; they are walkable terrain).
  5. Write everything back. Budget check printed at the end.

CAUTION - autumn metatiles may reference tiles by ids that assume autumn's
tiles.png; you MUST re-extract each referenced 8x8 tile from autumn's sheet and
re-add it to evernahn's sheet under a NEW id, not copy the raw id. The code does
this. Verify afterwards by rendering (render_tileset below) + present_files.

This script is deliberately conservative: it appends, never reorders existing
Evernahn metatiles (0-45), so any map already painted keeps its ids.
"""
import sys, os, json, struct
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from PIL import Image
from collections import OrderedDict
import lib_convert as L

EV = 'codebase/data/tilesets/primary/evernahn'
AU = 'codebase/data/tilesets/primary/autumn'
SEL = 'assets/pelluca_dock_spec/autumn_cliff_path_selection.json'

def load_sheet(D):
    return np.array(Image.open(D+'/tiles.png').convert('P'))

def tile_at(sheet, tid):
    TPR = sheet.shape[1]//8
    r = (tid//TPR)*8; c = (tid%TPR)*8
    if r+8 > sheet.shape[0] or c+8 > sheet.shape[1]: return np.zeros((8,8), np.uint8)
    return sheet[r:r+8, c:c+8].copy()

def main():
    sel = json.load(open(SEL))
    cliff_ids = sel['cliff_metatile_ids']; path_ids = sel['path_metatile_ids']
    print('selection: %d cliff + %d path autumn metatiles' % (len(cliff_ids), len(path_ids)))

    au_sheet = load_sheet(AU)
    au_mt = open(AU+'/metatiles.bin','rb').read()
    au_pal2 = L.read_gbapal(AU+'/palettes/02.gbapal')
    au_pal3 = L.read_gbapal(AU+'/palettes/03.gbapal')

    # 1. autumn pal2 -> evernahn slot 3, pal3 -> slot 4
    L.write_gbapal(EV+'/palettes/03.gbapal', au_pal2); L.write_jasc(EV+'/palettes/03.pal', au_pal2)
    L.write_gbapal(EV+'/palettes/04.gbapal', au_pal3); L.write_jasc(EV+'/palettes/04.pal', au_pal3)
    slot_map = {2:3, 3:4}   # autumn palette slot -> evernahn palette slot

    # 2. index evernahn's EXISTING tiles by content. FIRST occurrence wins and the
    #    id IS the grid slot, so existing metatiles 0-45 keep pointing at the right
    #    pixels. New tiles are appended at ids >= n_ev_tiles, so a new tile can
    #    NEVER land on an existing slot. (The old code numbered new tiles from
    #    len(tilemap)=146 while existing slots ran to 159 - they collided, and the
    #    deduped blank tile at 159 got overwritten, corrupting every "empty" entry.)
    ev_sheet = load_sheet(EV); TPR = ev_sheet.shape[1]//8
    n_ev_tiles = (ev_sheet.shape[0]//8)*TPR
    tilemap = OrderedDict()
    for tid in range(n_ev_tiles):
        key = tile_at(ev_sheet, tid).tobytes()
        if key not in tilemap:
            tilemap[key] = tid
    appended = []                       # new 8x8 tiles, in id order from n_ev_tiles
    ev_mt = bytearray(open(EV+'/metatiles.bin','rb').read())
    ev_at = bytearray(open(EV+'/metatile_attributes.bin','rb').read())
    n_ev_meta = len(ev_mt)//16

    def append_autumn_metatile(au_id):
        e = struct.unpack_from('<8H', au_mt, au_id*16)
        new_entries = []
        for v in e:
            tid = v & 0x3FF
            # NOTE: do NOT shortcut tid==0 to a literal 0 entry. Evernahn's tile 0
            # is a grass tile (50/64 non-transparent px), while autumn's tile 0 is
            # blank - emitting 0 would draw grass where autumn draws nothing.
            # Everything is mapped by CONTENT, so autumn's blank resolves to
            # evernahn's blank tile and renders identically in software and on HW.
            au_tile = tile_at(au_sheet, tid)          # pixels index autumn palette
            key = au_tile.tobytes()
            if key not in tilemap:
                tilemap[key] = n_ev_tiles + len(appended)
                appended.append(au_tile)
            new_tid = tilemap[key]
            xf = (v>>10)&1; yf = (v>>11)&1
            au_pal = (v>>12)&15
            ev_pal = slot_map.get(au_pal, au_pal)     # per-ENTRY remap: pal2->3, pal3->4
            new_entries.append((new_tid & 0x3FF) | (xf<<10) | (yf<<11) | ((ev_pal&15)<<12))
        for ne in new_entries: ev_mt.extend(struct.pack('<H', ne))
        ev_at.extend(L.metatile_attr(0x00, 1))        # MB_NORMAL, walkable terrain

    added = []
    for au_id in cliff_ids + path_ids:
        # palette is remapped per tile-entry inside append_autumn_metatile
        # (pal2->slot3, pal3->slot4), so mixed-palette metatiles stay correct
        append_autumn_metatile(au_id)
        added.append(au_id)

    # 3. write the enlarged tile sheet: existing pixels copied VERBATIM (so every
    #    existing grid slot keeps its exact content), new tiles appended after.
    total = n_ev_tiles + len(appended)
    rows = (total + TPR - 1)//TPR
    sheet = np.zeros((rows*8, TPR*8), np.uint8)
    sheet[:ev_sheet.shape[0], :ev_sheet.shape[1]] = ev_sheet
    for k, t in enumerate(appended):
        i = n_ev_tiles + k
        sheet[(i//TPR)*8:(i//TPR)*8+8, (i%TPR)*8:(i%TPR)*8+8] = t
    img = Image.fromarray(sheet, 'P')
    # keep the existing palette table in the PNG (cosmetic); runtime uses .gbapal
    img.putpalette(Image.open(EV+'/tiles.png').getpalette())
    img.save(EV+'/tiles.png')
    open(EV+'/metatiles.bin','wb').write(bytes(ev_mt))
    open(EV+'/metatile_attributes.bin','wb').write(bytes(ev_at))

    print('appended %d metatiles (now %d total, budget 512)' % (len(added), len(ev_mt)//16))
    print('tiles now %d (budget 512)' % total)
    print('new metatile id ranges: cliff/path start at %d' % n_ev_meta)
    print('DONE - now: cd codebase && timeout 290 make modern, then render + present_files to verify')

if __name__ == '__main__':
    main()
