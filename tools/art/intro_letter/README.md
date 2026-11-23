MonoMyth's blackletter (its font slot 4; glyphs 0xAF0448, 240 glyphs of 16x16 2bpp in the latfont layout; widths 0xAF4048,
one byte per glyph). Present in both copies of the ROM. Extracted to assets/intro_reference/monomyth_blackletter/.
dec.py decodes latfont glyph data (bit order: value = (row16 >> (14 - 2*i)) & 3). preview.py renders the parchment-letter
preview (assets/intro_reference/letter_parchment_preview_v1.png).
Credit: MonoMyth (permission still pending).
