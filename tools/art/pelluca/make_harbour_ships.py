"""The harbour's vessels as overworld objects (user 2026-11-24: "pick a fitting ship for the Pale Veluza... two other
ships for each of the other docks"; the approved mock's recolours, waterfront_mock.py):
  OBJ_EVENT_GFX_PALE_VELUZA      Crown's wooden ship (credit Blah and the Crown team), bleached pale, ivory sail, 128x64
  OBJ_EVENT_GFX_MERCHANTMAN      the same hull mirrored, tarred, a madder sail, 128x64
  OBJ_EVENT_GFX_FISHING_SLOOP    Lazarus' sailboat (credit the Lazarus team) in wood and canvas, 64x64
  OBJ_EVENT_GFX_WOODEN_ROWBOAT   Crown's rowboat, 64x32
Two palettes: the two ships share one, the sloop and the rowboat the other (15 colours each, quantised together).
A 128x64 sprite is drawn by two 64x32... (OAM's largest square is 64x64): the png is stored 64 wide with its
quarters stacked (tl, tr, bl, br) so each 64x32 subsprite's tiles are consecutive. Every sprite is shifted 8 px left
of its anchor cell's centre, so a ship of width w spans the cells (anchor - w/32) .. (anchor + w/32 - 1).
Writes the pngs and palettes, and wires the four graphics ids into the C sources (idempotent).
Usage: python3 tools/art/pelluca/make_harbour_ships.py"""
import os, sys, re
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..')); C = os.path.join(ROOT, 'codebase')
OUT = os.path.join(C, 'graphics/object_events/pics/misc')

def ramp_map(rgb, m, ramp):
    out = rgb.copy(); lum = rgb.astype(int).mean(-1)
    if not m.any(): return out
    lo, hi = np.percentile(lum[m], 2), np.percentile(lum[m], 98) + 1
    k = ((hi - lum) / (hi - lo) * len(ramp)).clip(0, len(ramp) - 1).astype(int)
    for i, c in enumerate(ramp): out[m & (k == i)] = c
    return out

def ship(kind):
    """the same recolours as the approved mock"""
    if kind in ('veluza', 'merchant'): q = np.array(Image.open(os.path.join(ROOT, 'assets/crown_reference/pieces/ship_galleon.png')).convert('RGBA'))
    elif kind == 'rowboat': q = np.array(Image.open(os.path.join(ROOT, 'assets/crown_reference/pieces/rowboat.png')).convert('RGBA'))
    else: q = np.array(Image.open(os.path.join(ROOT, 'assets/lazarus_reference/sailboat.png')).convert('RGBA'))
    rgb, m = q[..., :3].copy(), q[..., 3] > 0
    r_, g_, b_ = [rgb[..., i].astype(int) for i in range(3)]
    yy = np.arange(m.shape[0])[:, None] * np.ones((1, m.shape[1]), int)
    water = m & (b_ > r_ + 25) & (yy >= m.shape[0] - 8)
    if kind == 'veluza':
        sail = m & (b_ > r_ + 10) & ~water
        rgb = ramp_map(rgb, m & ~sail & ~water, [(244, 240, 230), (222, 216, 204), (196, 190, 180), (164, 160, 156), (124, 122, 126), (80, 78, 90)])
        rgb = ramp_map(rgb, sail, [(252, 250, 242), (232, 228, 214), (206, 204, 196), (170, 176, 186)])
    elif kind == 'merchant':
        sail = m & (b_ > r_ + 10) & ~water
        rgb = ramp_map(rgb, m & ~sail & ~water, [(150, 110, 70), (120, 84, 54), (96, 66, 44), (72, 48, 34), (50, 34, 26)])
        rgb = ramp_map(rgb, sail, [(196, 96, 72), (164, 72, 56), (130, 54, 46), (96, 40, 38)])
        rgb, m = rgb[:, ::-1].copy(), m[:, ::-1].copy()
    elif kind == 'sloop':
        sail = m & (g_ > 190) & (r_ > 150)
        rgb = ramp_map(rgb, m & ~sail, [(176, 132, 84), (150, 108, 66), (120, 84, 52), (88, 60, 40), (56, 40, 30)])
        rgb = ramp_map(rgb, sail, [(234, 222, 190), (212, 198, 162), (186, 170, 134)])
    return rgb, m

def palette(images, n=15):
    """one 15-colour palette for several sprites (k-means on their opaque pixels; GBA 5-bit colours)"""
    px = np.concatenate([rgb[m] for rgb, m in images]).astype(float)
    cols = np.unique((px // 8 * 8).astype(int), axis=0)
    if len(cols) <= n: cents = cols.astype(float)
    else:
        rng = np.random.RandomState(3); cents = px[rng.choice(len(px), n, replace=False)]
        for _ in range(30):
            d = ((px[:, None, :] - cents[None]) ** 2).sum(-1); lab = d.argmin(1)
            for k in range(n):
                if (lab == k).any(): cents[k] = px[lab == k].mean(0)
    cents = (np.clip(np.round(cents), 0, 255).astype(int) // 8 * 8)
    return [(0, 255, 0)] + [tuple(c) for c in cents] + [(0, 0, 0)] * (15 - len(cents))

def index(rgb, m, pal):
    P = np.array(pal[1:], float); flat = rgb.reshape(-1, 3).astype(float)
    k = ((flat[:, None, :] - P[None]) ** 2).sum(-1).argmin(1) + 1
    idx = k.reshape(m.shape).astype(np.uint8); idx[~m] = 0
    return idx

def save(idx, pal, name, stacked):
    if stacked:                                  # 128x64 -> 64x128, quarters tl, tr, bl, br
        q = [idx[0:32, 0:64], idx[0:32, 64:128], idx[32:64, 0:64], idx[32:64, 64:128]]
        idx = np.concatenate(q, 0)
    im = Image.fromarray(idx, 'P'); im.putpalette([v for c in pal for v in c] + [0] * (768 - 48))
    im.save(os.path.join(OUT, name + '.png'))

SUBS = r'''
// Dreamstone Ruination: Pelluca Harbour's vessels (tools/art/pelluca/make_harbour_ships.py). Each is drawn 8 px left of
// its anchor cell's centre. A 128x64 ship is two rows of two 64x32 subsprites (its png stores the quarters stacked).
static const struct Subsprite sOamTable_DrShip128x64[] = {
    {.x = -72, .y = -32, .shape = SPRITE_SHAPE(64x32), .size = SPRITE_SIZE(64x32), .tileOffset = 0,  .priority = 2},
    {.x =  -8, .y = -32, .shape = SPRITE_SHAPE(64x32), .size = SPRITE_SIZE(64x32), .tileOffset = 32, .priority = 2},
    {.x = -72, .y =   0, .shape = SPRITE_SHAPE(64x32), .size = SPRITE_SIZE(64x32), .tileOffset = 64, .priority = 2},
    {.x =  -8, .y =   0, .shape = SPRITE_SHAPE(64x32), .size = SPRITE_SIZE(64x32), .tileOffset = 96, .priority = 2},
};
static const struct SubspriteTable sOamTables_DrShip128x64[] = {
    {ARRAY_COUNT(sOamTable_DrShip128x64), sOamTable_DrShip128x64}, {ARRAY_COUNT(sOamTable_DrShip128x64), sOamTable_DrShip128x64},
    {ARRAY_COUNT(sOamTable_DrShip128x64), sOamTable_DrShip128x64}, {ARRAY_COUNT(sOamTable_DrShip128x64), sOamTable_DrShip128x64},
    {ARRAY_COUNT(sOamTable_DrShip128x64), sOamTable_DrShip128x64}, {ARRAY_COUNT(sOamTable_DrShip128x64), sOamTable_DrShip128x64},
};
static const struct Subsprite sOamTable_DrBoat64x64[] = {
    {.x = -40, .y = -32, .shape = SPRITE_SHAPE(64x64), .size = SPRITE_SIZE(64x64), .tileOffset = 0, .priority = 2},
};
static const struct SubspriteTable sOamTables_DrBoat64x64[] = {
    {1, sOamTable_DrBoat64x64}, {1, sOamTable_DrBoat64x64}, {1, sOamTable_DrBoat64x64},
    {1, sOamTable_DrBoat64x64}, {1, sOamTable_DrBoat64x64}, {1, sOamTable_DrBoat64x64},
};
static const struct Subsprite sOamTable_DrBoat64x32[] = {
    {.x = -40, .y = -16, .shape = SPRITE_SHAPE(64x32), .size = SPRITE_SIZE(64x32), .tileOffset = 0, .priority = 2},
};
static const struct SubspriteTable sOamTables_DrBoat64x32[] = {
    {1, sOamTable_DrBoat64x32}, {1, sOamTable_DrBoat64x32}, {1, sOamTable_DrBoat64x32},
    {1, sOamTable_DrBoat64x32}, {1, sOamTable_DrBoat64x32}, {1, sOamTable_DrBoat64x32},
};
'''
SHIPS = [  # (gfx id name, symbol, file, w, h, subsprite tables, palette tag)
    ('PALE_VELUZA', 'PaleVeluza', 'dr_pale_veluza', 128, 64, 'sOamTables_DrShip128x64', 'OBJ_EVENT_PAL_TAG_DR_SHIPS'),
    ('MERCHANTMAN', 'Merchantman', 'dr_merchantman', 128, 64, 'sOamTables_DrShip128x64', 'OBJ_EVENT_PAL_TAG_DR_SHIPS'),
    ('FISHING_SLOOP', 'FishingSloop', 'dr_fishing_sloop', 64, 64, 'sOamTables_DrBoat64x64', 'OBJ_EVENT_PAL_TAG_DR_BOATS'),
    ('WOODEN_ROWBOAT', 'WoodenRowboat', 'dr_wooden_rowboat', 64, 32, 'sOamTables_DrBoat64x32', 'OBJ_EVENT_PAL_TAG_DR_BOATS')]

def add_after(path, anchor, text, marker):
    s = open(path).read()
    if marker in s: return
    i = s.index(anchor) + len(anchor); s = s[:i] + text + s[i:]; open(path, 'w').write(s)

def wire():
    ev = os.path.join(C, 'include/constants/event_objects.h'); s = open(ev).read()
    if 'OBJ_EVENT_GFX_PALE_VELUZA' not in s:
        s = s.replace('#define NUM_OBJ_EVENT_GFX                          285',
                      '#define OBJ_EVENT_GFX_PALE_VELUZA                  285   // Pelluca Harbour (make_harbour_ships.py)\n'
                      '#define OBJ_EVENT_GFX_MERCHANTMAN                  286\n#define OBJ_EVENT_GFX_FISHING_SLOOP                287\n'
                      '#define OBJ_EVENT_GFX_WOODEN_ROWBOAT               288\n\n#define NUM_OBJ_EVENT_GFX                          289')
        s = s.replace('#define OBJ_EVENT_PAL_TAG_DR_SHRINE             0x1130',
                      '#define OBJ_EVENT_PAL_TAG_DR_SHRINE             0x1130\n#define OBJ_EVENT_PAL_TAG_DR_SHIPS              0x1131\n'
                      '#define OBJ_EVENT_PAL_TAG_DR_BOATS              0x1132')
        open(ev, 'w').write(s)
    g = os.path.join(C, 'src/data/object_events/object_event_graphics.h')
    add_after(g, 'const u16 gObjectEventPal_DrShrine[] = INCBIN_U16("graphics/object_events/pics/misc/dr_shrine.gbapal");\n',
              ''.join('const u32 gObjectEventPic_%s[] = INCBIN_U32("graphics/object_events/pics/misc/%s.4bpp");\n' % (sym, f)
                      for (_, sym, f, *_r) in SHIPS) +
              'const u16 gObjectEventPal_DrShips[] = INCBIN_U16("graphics/object_events/pics/misc/dr_ships.gbapal");\n'
              'const u16 gObjectEventPal_DrBoats[] = INCBIN_U16("graphics/object_events/pics/misc/dr_boats.gbapal");\n',
              'gObjectEventPic_PaleVeluza')
    pt = os.path.join(C, 'src/data/object_events/object_event_pic_tables.h')
    add_after(pt, 'static const struct SpriteFrameImage sPicTable_DrShrine[] = { obj_frame_tiles(gObjectEventPic_DrShrine), };\n',
              ''.join('static const struct SpriteFrameImage sPicTable_%s[] = { obj_frame_tiles(gObjectEventPic_%s), };\n' % (sym, sym)
                      for (_, sym, *_r) in SHIPS), 'sPicTable_PaleVeluza')
    sub = os.path.join(C, 'src/data/object_events/object_event_subsprites.h'); s = open(sub).read()
    if 'sOamTable_DrShip128x64' not in s: open(sub, 'a').write(SUBS)
    gi = os.path.join(C, 'src/data/object_events/object_event_graphics_info.h')
    text = ''
    for (_, sym, f, w, h, tables, tag) in SHIPS:
        text += '''
const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_%s = {
    .tileTag = TAG_NONE,
    .paletteTag = %s,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_NONE,
    .size = %d,
    .width = %d,
    .height = %d,
    .paletteSlot = PALSLOT_NPC_SPECIAL,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = TRUE,
    .compressed = FALSE,
    .tracks = TRACKS_NONE,
    .oam = &gObjectEventBaseOam_8x8,
    .subspriteTables = %s,
    .anims = sAnimTable_Inanimate,
    .images = sPicTable_%s,
    .affineAnims = gDummySpriteAffineAnimTable,
};
''' % (sym, tag, w * h // 2, w, h, tables, sym)
    add_after(gi, '    .images = sPicTable_DrShrine,\n    .affineAnims = gDummySpriteAffineAnimTable,\n};\n', text, 'gObjectEventGraphicsInfo_PaleVeluza')
    pp = os.path.join(C, 'src/data/object_events/object_event_graphics_info_pointers.h')
    add_after(pp, 'extern const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_DrShrine;\n',
              ''.join('extern const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_%s;\n' % sym for (_, sym, *_r) in SHIPS),
              'extern const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_PaleVeluza;')
    add_after(pp, '    [OBJ_EVENT_GFX_DR_SHRINE] = &gObjectEventGraphicsInfo_DrShrine,\n',
              ''.join('    [OBJ_EVENT_GFX_%s] = &gObjectEventGraphicsInfo_%s,\n' % (gid, sym) for (gid, sym, *_r) in SHIPS),
              '[OBJ_EVENT_GFX_PALE_VELUZA]')
    em = os.path.join(C, 'src/event_object_movement.c')
    add_after(em, '    {gObjectEventPal_DrShrine, OBJ_EVENT_PAL_TAG_DR_SHRINE},\n',
              '    {gObjectEventPal_DrShips, OBJ_EVENT_PAL_TAG_DR_SHIPS},\n    {gObjectEventPal_DrBoats, OBJ_EVENT_PAL_TAG_DR_BOATS},\n',
              'OBJ_EVENT_PAL_TAG_DR_SHIPS}')

def main():
    imgs = {k: ship(k) for k in ('veluza', 'merchant', 'sloop', 'rowboat')}
    pa = palette([imgs['veluza'], imgs['merchant']]); pb = palette([imgs['sloop'], imgs['rowboat']])
    save(index(*imgs['veluza'], pa), pa, 'dr_pale_veluza', True)
    save(index(*imgs['merchant'], pa), pa, 'dr_merchantman', True)
    save(index(*imgs['sloop'], pb), pb, 'dr_fishing_sloop', False)
    save(index(*imgs['rowboat'], pb), pb, 'dr_wooden_rowboat', False)
    for name, pal in (('dr_ships', pa), ('dr_boats', pb)):
        with open(os.path.join(OUT, name + '.pal'), 'w', newline='') as f:
            f.write('JASC-PAL\r\n0100\r\n16\r\n' + ''.join('%d %d %d\r\n' % c for c in pal))
    wire()
    print('ships written and wired')

if __name__ == '__main__':
    main()
