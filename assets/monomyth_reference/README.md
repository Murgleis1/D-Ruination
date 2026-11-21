MonoMyth (Pokémon MonoMyth) reference renders and cut pieces.
- koi_painting.png: the framed koi painting from a New Old Bay City house (MonoMyth map header 0x886B3B0, cells 13-14,
  rows 0-1), cut to its frame (the right edge closed with its outline column). Cadmus's office (frame in walnut).
- wave_rug.png: the blue wave-pattern rug from a Watercress Port house (map header 0x886ABD0, cells 2-5, rows 7-8), cut
  off its floor. Cadmus's office.
- pieces/web_strand.png, web_corner_l.png, web_corner_r.png: the Webbed Woods' webbing (0x886DD40: the zig-zag strand
  strung between trees, cells 42-44 x 10-11; the drapes on the webbed trees, cells 0-2 x 7), keyed out by their two
  web colours. The haunted teachers' lounge (user).
- pieces/painting_starry.png, painting_dunes.png, painting_harbour.png, painting_figures.png: the four framed paintings
  of North Edelweiss's museum (map header 0x886AA48). In the map the frames are blank; the paintings are object events
  (graphics ids 316-319) decoded by the game itself (tools/monomyth/mm_paintings.py). Each keeps its name plaque below.
  Used (recoloured) in Cadmus's manor (tools/art/manor/manor_mock.py).
- pieces/tarragon_tusk_arch.png, tarragon_post.png, tarragon_fire_ring.png, tarragon_blue_flowers.png: Camp Tarragon's
  (map header 0x88695F0) double tusk arch with its hanging horn charm (cells 29-34 x 16-20, the snowy tree dropped), a
  standing log post (29, 11-12), the stone fire ring (31, 11), blue snow flowers (34, 6); cut against the snow with the
  snow and ice-path colours dropped. Used round the Arceus statue in the ice path's shrine (user: ancient worship site).
- pieces/rubble_pile_a.png, rubble_pile_b.png, rubble_pile_c.png, rubble_stones.png, rubble_stone.png: rubble piles and
  loose stones from Mt. Thunder (map 0x886D608, cells (29,28), (39,34), (42,33), (32,30), (30,32)), cut against its icy
  floor. Used (turned grey) to choke the cell doorway in the church after Eden's blast (tools/art/templar/blast_mock.py).
- pieces/webtree_fan_l.png, webtree_drape.png, webtree_fan_r.png, webtree_join.png, webtree_strand.png: the web layer of the Webbed Woods' webbed trees (0x886DD40: the left fan 236/21e, the drape under the crown 234/22c, the right fan 237/21f, the fans two trees share 235 233 / 21d 21b, the strand across a gap 279 277 275 26e 26f / 27a 278 272 273 274), keyed out by the two web colours. Hollow Hill's blood-red webbing (user).
- pieces/druddighul_ow.png: Druddighul's overworld sprite (32x32, graphics id 0x128, palette tag 0x124B), the decrepit dragon of the Apocryphal Bastion's ruined castle (its top map, header 0x86E034), decoded by the game (tools/monomyth/mm_bigsprites.py). Turned to stone for the Necropolis yard (user).
