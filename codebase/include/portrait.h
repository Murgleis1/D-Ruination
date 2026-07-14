#ifndef GUARD_PORTRAIT_H
#define GUARD_PORTRAIT_H

#include "constants/portraits.h"

struct ScriptContext;

struct PortraitExpr
{
    u8 expression;          // PORTRAIT_EXPR_*
    const u32 *tiles;       // LZ77-compressed 4bpp  (graphics/portraits/<name>.4bpp.lz)
    const u16 *palette;     // 16-color palette      (graphics/portraits/<name>.gbapal)
};

struct Portrait
{
    const u8 *name;         // default nameplate text, or NULL to leave the speaker name untouched
    const struct PortraitExpr *expressions;
    u8 numExpressions;
};

extern const struct Portrait gPortraits[PORTRAIT_COUNT];

// Show/replace the current dialogue portrait: loads its gfx and (unless the
// portrait has no default name) sets the nameplate from the registry. Safe to
// call before or between message boxes; the bust persists until the message box
// closes (HideFieldMessageBox) or hideportrait is used.
void SetMsgPortrait(u8 portraitId, u8 expression);
void FreeMsgPortrait(void);
bool8 IsMsgPortraitActive(void);

// Script natives (callnative) behind the showportrait / hideportrait macros.
void Script_ShowPortrait(struct ScriptContext *ctx);
void Script_HidePortrait(struct ScriptContext *ctx);

#endif // GUARD_PORTRAIT_H
