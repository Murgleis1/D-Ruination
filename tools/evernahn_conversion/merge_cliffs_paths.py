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

    # 2. rebuild evernahn tile sheet into a dedup map so we can append
    ev_sheet = load_sheet(EV); TPR = ev_sheet.shape[1]//8
    n_ev_tiles = 0
    tilemap = OrderedDict()
    for tid in range((ev_sheet.shape[0]//8)*TPR):
        t = tile_at(ev_sheet, tid)
        tilemap[t.tobytes()] = tid
        n_ev_tiles = max(n_ev_tiles, tid+1)
    ev_mt = bytearray(open(EV+'/metatiles.bin','rb').read())
    ev_at = bytearray(open(EV+'/metatile_attributes.bin','rb').read())
    n_ev_meta = len(ev_mt)//16

    def append_autumn_metatile(au_id, ev_palette):
        e = struct.unpack_from('<8H', au_mt, au_id*16)
        new_entries = []
        for v in e:
            tid = v & 0x3FF
            if tid == 0 and not (v & 0xFC00):
                new_entries.append(0); continue
            au_tile = tile_at(au_sheet, tid)          # pixels index autumn palette
            key = au_tile.tobytes()
            if key not in tilemap:
                tilemap[key] = len(tilemap)
            new_tid = tilemap[key]
            xf = (v>>10)&1; yf = (v>>11)&1
            new_entries.append((new_tid & 0x3FF) | (xf<<10) | (yf<<11) | ((ev_palette&15)<<12))
        for ne in new_entries: ev_mt.extend(struct.pack('<H', ne))
        ev_at.extend(L.metatile_attr(0x00, 1))        # MB_NORMAL, walkable terrain

    added = []
    for au_id in cliff_ids + path_ids:
        # decide evernahn palette from which autumn palette this metatile uses
        e = struct.unpack_from('<8H', au_mt, au_id*16)
        aups = {(v>>12)&15 for v in e if v & 0x3FF}
        ev_pal = slot_map.get(3 if 3 in aups else 2, 3)
        append_autumn_metatile(au_id, ev_pal)
        added.append((au_id, ev_pal))

    # 3. write the enlarged tile sheet
    total = len(tilemap)
    rows = (total + TPR - 1)//TPR
    sheet = np.zeros((rows*8, TPR*8), np.uint8)
    for blob, i in tilemap.items():
        sheet[(i//TPR)*8:(i//TPR)*8+8, (i%TPR)*8:(i%TPR)*8+8] = np.frombuffer(blob, np.uint8).reshape(8,8)
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
