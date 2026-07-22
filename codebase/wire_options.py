#!/usr/bin/env python3
"""Add Overworld Speed (page 2, var) + Autoheal (page 3, flag) options. Run from codebase/."""
OM='src/option_menu.c'; ST='src/strings.c'; SH='include/strings.h'; FL='include/constants/flags.h'
ok=True
def do(path, anchor, new, mode='after'):
    global ok
    s=open(path).read(); n=s.count(anchor)
    if n==0: print(f'  MISS {path}: {anchor[:52]!r}'); ok=False; return
    if mode!='replace_all' and n!=1: print(f'  WARN {path}: {n}x {anchor[:38]!r} (first only)')
    if   mode=='before':      s=s.replace(anchor, new+anchor, 1)
    elif mode=='after':       s=s.replace(anchor, anchor+new, 1)
    elif mode=='replace':     s=s.replace(anchor, new, 1)
    elif mode=='replace_all': s=s.replace(anchor, new)
    open(path,'w').write(s); print(f'  ok  {path} ({mode}, {n})')

funcs='''static u8 OverworldSpeed_ProcessInput(u8 selection)
{
    if (JOY_NEW(DPAD_RIGHT))
    {
        PlayOptionChangeSE();
        if (selection <= 2)
            selection++;
        else
            selection = 0;
        sArrowPressed = TRUE;
    }
    if (JOY_NEW(DPAD_LEFT))
    {
        PlayOptionChangeSE();
        if (selection != 0)
            selection--;
        else
            selection = 3;
        sArrowPressed = TRUE;
    }
    return selection;
}

static void OverworldSpeed_DrawChoices(u8 selection)
{
    u8 styles[4];
    styles[0] = 0;
    styles[1] = 0;
    styles[2] = 0;
    styles[3] = 0;
    styles[selection] = 1;
    DrawOptionMenuChoice(gText_BattleSpeed1X, 104, YPOS_OVERWORLD_SPEED, styles[0]);
    DrawOptionMenuChoice(gText_BattleSpeed2X, 128, YPOS_OVERWORLD_SPEED, styles[1]);
    DrawOptionMenuChoice(gText_BattleSpeed4X, 152, YPOS_OVERWORLD_SPEED, styles[2]);
    DrawOptionMenuChoice(gText_MoveSpeed8X,   176, YPOS_OVERWORLD_SPEED, styles[3]);
}

static u8 Autoheal_ProcessInput(u8 selection)
{
    if (JOY_NEW(DPAD_LEFT | DPAD_RIGHT))
    {
        PlayOptionChangeSE();
        selection ^= 1;
        sArrowPressed = TRUE;
    }
    return selection;
}

static void Autoheal_DrawChoices(u8 selection)
{
    u8 styles[2];
    styles[0] = 0;
    styles[1] = 0;
    styles[selection] = 1;
    DrawOptionMenuChoice(gText_AutohealOff, 104, YPOS_AUTOHEAL, styles[0]);
    DrawOptionMenuChoice(gText_AutohealOn,  162, YPOS_AUTOHEAL, styles[1]);
}

'''
pg2case='''        case MENUITEM_OVERWORLD_SPEED:
            previousOption = gTasks[taskId].tOverworldSpeed;
            gTasks[taskId].tOverworldSpeed = OverworldSpeed_ProcessInput(gTasks[taskId].tOverworldSpeed);

            if (previousOption != gTasks[taskId].tOverworldSpeed)
                OverworldSpeed_DrawChoices(gTasks[taskId].tOverworldSpeed);
            break;
'''
pg3case='''        case MENUITEM_AUTOHEAL:
            previousOption = gTasks[taskId].tAutoheal;
            gTasks[taskId].tAutoheal = Autoheal_ProcessInput(gTasks[taskId].tAutoheal);

            if (previousOption != gTasks[taskId].tAutoheal)
                Autoheal_DrawChoices(gTasks[taskId].tAutoheal);
            break;
'''
# enums
do(OM, '    MENUITEM_CANCEL_PG2,', '    MENUITEM_OVERWORLD_SPEED,\n', 'before')
do(OM, '    MENUITEM_CANCEL_PG3,', '    MENUITEM_AUTOHEAL,\n', 'before')
# task-data slots
do(OM, '#define tAutoscroll data[15]', '\n#define tOverworldSpeed data[16]\n#define tAutoheal data[17]', 'after')
# YPOS
do(OM, '#define YPOS_QUICKRUN     (MENUITEM_QUICKRUN * 16)', '\n#define YPOS_OVERWORLD_SPEED (MENUITEM_OVERWORLD_SPEED * 16)\n#define YPOS_AUTOHEAL     (MENUITEM_AUTOHEAL * 16)', 'after')
# labels
do(OM, '    [MENUITEM_CANCEL_PG2]  = gText_OptionMenuCancel,', '    [MENUITEM_OVERWORLD_SPEED] = gText_MoveSpeed,\n', 'before')
do(OM, '    [MENUITEM_CANCEL_PG3]  = gText_OptionMenuCancel,', '    [MENUITEM_AUTOHEAL]    = gText_Autoheal,\n', 'before')
# forward decls
do(OM, 'static void BattleSpeed_DrawChoices(u8 selection);', '\nstatic u8   OverworldSpeed_ProcessInput(u8 selection);\nstatic void OverworldSpeed_DrawChoices(u8 selection);\nstatic u8   Autoheal_ProcessInput(u8 selection);\nstatic void Autoheal_DrawChoices(u8 selection);', 'after')
# per-page draw
do(OM, '    BattleStyle_DrawChoices(gTasks[taskId].tBattleStyle);', '\n    OverworldSpeed_DrawChoices(gTasks[taskId].tOverworldSpeed);', 'after')
do(OM, '    Follower_DrawChoices(gTasks[taskId].tFollower);', '\n    Autoheal_DrawChoices(gTasks[taskId].tAutoheal);', 'after')
# dispatch (before the last real case of each page)
do(OM, '        case MENUITEM_BATTLESCENE:', pg2case, 'before')
do(OM, '        case MENUITEM_AFFECTION:', pg3case, 'before')
# read
do(OM, '= FlagGet(FLAG_SYS_AUTOSCROLL);', '= FlagGet(FLAG_SYS_AUTOSCROLL);\n    gTasks[taskId].tOverworldSpeed = VarGet(VAR_OVERWORLD_SPEEDUP);\n    gTasks[taskId].tAutoheal = FlagGet(FLAG_SYS_AUTOHEAL);', 'replace')
# save (BOTH blocks)
do(OM, 'tAutoscroll == 0 ? FlagClear(FLAG_SYS_AUTOSCROLL) : FlagSet(FLAG_SYS_AUTOSCROLL);',
      'tAutoscroll == 0 ? FlagClear(FLAG_SYS_AUTOSCROLL) : FlagSet(FLAG_SYS_AUTOSCROLL);\n    VarSet(VAR_OVERWORLD_SPEEDUP, gTasks[taskId].tOverworldSpeed);\n    gTasks[taskId].tAutoheal == 0 ? FlagClear(FLAG_SYS_AUTOHEAL) : FlagSet(FLAG_SYS_AUTOHEAL);',
      'replace_all')
# functions
do(OM, 'static u8 BikeSurfMus_ProcessInput(u8 selection)\n{', funcs+'static u8 BikeSurfMus_ProcessInput(u8 selection)\n{', 'replace')
# strings.c
do(ST, 'const u8 gText_BattleSpeed4X[] = _("{COLOR GREEN}{SHADOW LIGHT_GREEN}4x");',
      '\nconst u8 gText_MoveSpeed[] = _("Move Speed");\nconst u8 gText_MoveSpeed8X[] = _("{COLOR GREEN}{SHADOW LIGHT_GREEN}8x");\nconst u8 gText_Autoheal[] = _("Autoheal");\nconst u8 gText_AutohealOff[] = _("{COLOR GREEN}{SHADOW LIGHT_GREEN}Off");\nconst u8 gText_AutohealOn[] = _("{COLOR GREEN}{SHADOW LIGHT_GREEN}On");', 'after')
# strings.h
do(SH, 'extern const u8 gText_BattleSpeed4X[];',
      '\nextern const u8 gText_MoveSpeed[];\nextern const u8 gText_MoveSpeed8X[];\nextern const u8 gText_Autoheal[];\nextern const u8 gText_AutohealOff[];\nextern const u8 gText_AutohealOn[];', 'after')
# flags.h
do(FL, '#define FLAG_UNUSED_0x883                           (SYSTEM_FLAGS + 0x23) // Unused Flag',
      '#define FLAG_SYS_AUTOHEAL                           (SYSTEM_FLAGS + 0x23) // Dreamstone Ruination: heal + revive party after every battle (options menu)', 'replace')

print('DONE' if ok else 'SOME MISSED — review')
