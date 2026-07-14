#ifndef GUARD_CONSTANTS_PORTRAITS_H
#define GUARD_CONSTANTS_PORTRAITS_H

// Portrait dialogue system. Character IDs used by the showportrait/hideportrait
// script macros (asm/macros/event.inc) and by the registry in src/data/portraits.h.
// Defined as #defines (not an enum) so they are visible to the assembler/scripts.
#define PORTRAIT_NONE       0
#define PORTRAIT_OSRID      1
#define PORTRAIT_CADMUS     2
#define PORTRAIT_EDEN       3
#define PORTRAIT_GLAIVE     4
#define PORTRAIT_BARADUS    5
#define PORTRAIT_KIMARIS    6
#define PORTRAIT_AMBROSE    7
#define PORTRAIT_COUNT      8

// Expressions. A portrait renders the requested expression if the character
// defines it; otherwise it falls back to that character's first (default) entry.
#define PORTRAIT_EXPR_NEUTRAL   0
#define PORTRAIT_EXPR_POSITIVE  1
#define PORTRAIT_EXPR_NEGATIVE  2
#define PORTRAIT_EXPR_SMILE     3
#define PORTRAIT_EXPR_ANGER     4

#endif // GUARD_CONSTANTS_PORTRAITS_H
