# Fantasma ROM readers

The ROM is pokeemerald-expansion. Graphics use the expansion's **smol** compression, not LZ77:

- tiles use modes 1 and 6;
- tilemaps use mode 8 (`IS_TILEMAP`);
- palettes are raw.

## Files

- `unsmol.cpp`: decodes smol tile data (modes 1-6). Build it against the expansion's own encoder sources:
  ```
  git clone --filter=blob:none --sparse https://github.com/rh-hideout/pokeemerald-expansion
  # sparse-checkout tools/compresSmol
  g++ -O2 -std=c++17 unsmol.cpp compressAlgo.cpp tANS.cpp fileDispatcher.cpp -o unsmol
  ```
- `fsread.py`: the ROM reader. Env: `FANTASMA_ROM`, `UNSMOL`.
  - `data(ptr)` handles LZ77, smol tiles (via unsmol) and smol tilemaps (`smol_tilemap`, a Python port of
    `SmolDecompressTilemap`: instruction decode, then u16 prefix-sum delta).
  - `TS`/`render` handle map tilesets: 8-entry two-layer metatiles. The primary size is **per tileset**: most
    primaries are 512 tiles / 512 metatiles, but some (e.g. `0x938b14c`) are 640/640. The size comes from the
    decompressed primary. The old fixed 512 gave the magenta "garbled" renders.
- `render_all.py HEADERS.pkl OUT`: renders every unique layout and makes contact sheets. Headers come from
  `tools/monomyth/romlib.find_headers` on this ROM.
- `bbg.py OUT [TABLE]`: walks `gBattleEnvironmentInfo` and renders each background at 240×160.
  - The table is at `0x84b86dc` in rc_Water. It is found by scanning for five data pointers followed by a
    Thumb intro-slide pointer.
  - Entries are 64 bytes: `name[26]`, `naturePower`, `secretPowerAnimation*`, `secretPowerEffect`,
    camouflage, `entry{tileset,tilemap}`, `background{tileset,tilemap}`, `palette*`, `battleIntroSlide`.

Renders are in `assets/fantasma_reference/`.
