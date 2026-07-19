// Portrait graphics (LZ 4bpp) + palettes, built from graphics/portraits/*.png
// (see tools/portraits/build_portraits.py and the rules in spritesheet_rules.mk).
// Included by src/portrait.c.

static const u32 sPortraitGfx_Osrid[]           = INCBIN_U32("graphics/portraits/osrid.4bpp.lz");
static const u16 sPortraitPal_Osrid[]           = INCBIN_U16("graphics/portraits/osrid.gbapal");

static const u32 sPortraitGfx_CadmusNeutral[]   = INCBIN_U32("graphics/portraits/cadmus_neutral.4bpp.lz");
static const u16 sPortraitPal_CadmusNeutral[]   = INCBIN_U16("graphics/portraits/cadmus_neutral.gbapal");
static const u32 sPortraitGfx_CadmusSmile[]     = INCBIN_U32("graphics/portraits/cadmus_smile.4bpp.lz");
static const u16 sPortraitPal_CadmusSmile[]     = INCBIN_U16("graphics/portraits/cadmus_smile.gbapal");

static const u32 sPortraitGfx_Eden[]            = INCBIN_U32("graphics/portraits/eden.4bpp.lz");
static const u16 sPortraitPal_Eden[]            = INCBIN_U16("graphics/portraits/eden.gbapal");

static const u32 sPortraitGfx_GlaiveNeutral[]   = INCBIN_U32("graphics/portraits/glaive_neutral.4bpp.lz");
static const u16 sPortraitPal_GlaiveNeutral[]   = INCBIN_U16("graphics/portraits/glaive_neutral.gbapal");
static const u32 sPortraitGfx_GlaivePositive[]  = INCBIN_U32("graphics/portraits/glaive_positive.4bpp.lz");
static const u16 sPortraitPal_GlaivePositive[]  = INCBIN_U16("graphics/portraits/glaive_positive.gbapal");
static const u32 sPortraitGfx_GlaiveNegative[]  = INCBIN_U32("graphics/portraits/glaive_negative.4bpp.lz");
static const u16 sPortraitPal_GlaiveNegative[]  = INCBIN_U16("graphics/portraits/glaive_negative.gbapal");

static const u32 sPortraitGfx_BaradusPositive[] = INCBIN_U32("graphics/portraits/baradus_positive.4bpp.lz");
static const u16 sPortraitPal_BaradusPositive[] = INCBIN_U16("graphics/portraits/baradus_positive.gbapal");
static const u32 sPortraitGfx_BaradusAnger[]    = INCBIN_U32("graphics/portraits/baradus_anger.4bpp.lz");
static const u16 sPortraitPal_BaradusAnger[]    = INCBIN_U16("graphics/portraits/baradus_anger.gbapal");
static const u32 sPortraitGfx_BaradusNegative[] = INCBIN_U32("graphics/portraits/baradus_negative.4bpp.lz");
static const u16 sPortraitPal_BaradusNegative[] = INCBIN_U16("graphics/portraits/baradus_negative.gbapal");

static const u32 sPortraitGfx_KimarisNeutral[]  = INCBIN_U32("graphics/portraits/kimaris_neutral.4bpp.lz");
static const u16 sPortraitPal_KimarisNeutral[]  = INCBIN_U16("graphics/portraits/kimaris_neutral.gbapal");
static const u32 sPortraitGfx_KimarisPositive[] = INCBIN_U32("graphics/portraits/kimaris_positive.4bpp.lz");
static const u16 sPortraitPal_KimarisPositive[] = INCBIN_U16("graphics/portraits/kimaris_positive.gbapal");
static const u32 sPortraitGfx_KimarisNegative[] = INCBIN_U32("graphics/portraits/kimaris_negative.4bpp.lz");
static const u16 sPortraitPal_KimarisNegative[] = INCBIN_U16("graphics/portraits/kimaris_negative.gbapal");
static const u32 sPortraitGfx_KimarisSmile[]    = INCBIN_U32("graphics/portraits/kimaris_smile.4bpp.lz");
static const u16 sPortraitPal_KimarisSmile[]    = INCBIN_U16("graphics/portraits/kimaris_smile.gbapal");

static const u32 sPortraitGfx_AmbroseNeutral[]  = INCBIN_U32("graphics/portraits/ambrose_neutral.4bpp.lz");
static const u16 sPortraitPal_AmbroseNeutral[]  = INCBIN_U16("graphics/portraits/ambrose_neutral.gbapal");
static const u32 sPortraitGfx_AmbrosePositive[] = INCBIN_U32("graphics/portraits/ambrose_positive.4bpp.lz");
static const u16 sPortraitPal_AmbrosePositive[] = INCBIN_U16("graphics/portraits/ambrose_positive.gbapal");
static const u32 sPortraitGfx_AmbroseNegative[] = INCBIN_U32("graphics/portraits/ambrose_negative.4bpp.lz");
static const u16 sPortraitPal_AmbroseNegative[] = INCBIN_U16("graphics/portraits/ambrose_negative.gbapal");

// Default nameplate strings (edit freely). Osrid is scene-dependent
// (Prince ??? -> Nomad Alban -> true name), so his default is NULL and scripts
// set the name explicitly (setspeaker / SetSpeakerName after showportrait).
static const u8 sPortraitName_Osrid[]   = _("Prince ???");
static const u8 sPortraitName_Cadmus[]  = _("Cadmus");
static const u8 sPortraitName_Eden[]    = _("Eden");
static const u8 sPortraitName_Glaive[]  = _("Glaive");
static const u8 sPortraitName_Baradus[] = _("Baradus");
static const u8 sPortraitName_Kimaris[] = _("Kimaris");
static const u8 sPortraitName_Ambrose[] = _("Ambrose");

static const struct PortraitExpr sPortraitExpr_Osrid[] = {
    { PORTRAIT_EXPR_NEUTRAL,  sPortraitGfx_Osrid,          sPortraitPal_Osrid          },
};

static const struct PortraitExpr sPortraitExpr_Cadmus[] = {
    { PORTRAIT_EXPR_NEUTRAL,  sPortraitGfx_CadmusNeutral,  sPortraitPal_CadmusNeutral  },
    { PORTRAIT_EXPR_SMILE,    sPortraitGfx_CadmusSmile,    sPortraitPal_CadmusSmile    },
};

static const struct PortraitExpr sPortraitExpr_Eden[] = {
    { PORTRAIT_EXPR_NEUTRAL,  sPortraitGfx_Eden,           sPortraitPal_Eden           },
};

static const struct PortraitExpr sPortraitExpr_Glaive[] = {
    { PORTRAIT_EXPR_NEUTRAL,  sPortraitGfx_GlaiveNeutral,  sPortraitPal_GlaiveNeutral  },
    { PORTRAIT_EXPR_POSITIVE, sPortraitGfx_GlaivePositive, sPortraitPal_GlaivePositive },
    { PORTRAIT_EXPR_NEGATIVE, sPortraitGfx_GlaiveNegative, sPortraitPal_GlaiveNegative },
};

static const struct PortraitExpr sPortraitExpr_Baradus[] = {
    { PORTRAIT_EXPR_POSITIVE, sPortraitGfx_BaradusPositive, sPortraitPal_BaradusPositive },
    { PORTRAIT_EXPR_ANGER,    sPortraitGfx_BaradusAnger,    sPortraitPal_BaradusAnger    },
    { PORTRAIT_EXPR_NEGATIVE, sPortraitGfx_BaradusNegative, sPortraitPal_BaradusNegative },
};

static const struct PortraitExpr sPortraitExpr_Kimaris[] = {
    { PORTRAIT_EXPR_NEUTRAL,  sPortraitGfx_KimarisNeutral,  sPortraitPal_KimarisNeutral  },
    { PORTRAIT_EXPR_POSITIVE, sPortraitGfx_KimarisPositive, sPortraitPal_KimarisPositive },
    { PORTRAIT_EXPR_NEGATIVE, sPortraitGfx_KimarisNegative, sPortraitPal_KimarisNegative },
    { PORTRAIT_EXPR_SMILE,    sPortraitGfx_KimarisSmile,    sPortraitPal_KimarisSmile    },
};

static const struct PortraitExpr sPortraitExpr_Ambrose[] = {
    { PORTRAIT_EXPR_NEUTRAL,  sPortraitGfx_AmbroseNeutral,  sPortraitPal_AmbroseNeutral  },
    { PORTRAIT_EXPR_POSITIVE, sPortraitGfx_AmbrosePositive, sPortraitPal_AmbrosePositive },
    { PORTRAIT_EXPR_NEGATIVE, sPortraitGfx_AmbroseNegative, sPortraitPal_AmbroseNegative },
};

const struct Portrait gPortraits[PORTRAIT_COUNT] = {
    [PORTRAIT_OSRID]   = { sPortraitName_Osrid,   sPortraitExpr_Osrid,   ARRAY_COUNT(sPortraitExpr_Osrid)   },
    [PORTRAIT_CADMUS]  = { sPortraitName_Cadmus,  sPortraitExpr_Cadmus,  ARRAY_COUNT(sPortraitExpr_Cadmus)  },
    [PORTRAIT_EDEN]    = { sPortraitName_Eden,    sPortraitExpr_Eden,    ARRAY_COUNT(sPortraitExpr_Eden)    },
    [PORTRAIT_GLAIVE]  = { sPortraitName_Glaive,  sPortraitExpr_Glaive,  ARRAY_COUNT(sPortraitExpr_Glaive)  },
    [PORTRAIT_BARADUS] = { sPortraitName_Baradus, sPortraitExpr_Baradus, ARRAY_COUNT(sPortraitExpr_Baradus) },
    [PORTRAIT_KIMARIS] = { sPortraitName_Kimaris, sPortraitExpr_Kimaris, ARRAY_COUNT(sPortraitExpr_Kimaris) },
    [PORTRAIT_AMBROSE] = { sPortraitName_Ambrose, sPortraitExpr_Ambrose, ARRAY_COUNT(sPortraitExpr_Ambrose) },
};
