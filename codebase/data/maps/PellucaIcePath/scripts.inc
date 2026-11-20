PellucaIcePath_MapScripts::
# 10 "data/maps/PellucaIcePath/scripts.pory"
	map_script MAP_SCRIPT_ON_LOAD, PellucaIcePath_MapScripts_MAP_SCRIPT_ON_LOAD
# 21 "data/maps/PellucaIcePath/scripts.pory"
	map_script MAP_SCRIPT_ON_RESUME, PellucaIcePath_MapScripts_MAP_SCRIPT_ON_RESUME
# 24 "data/maps/PellucaIcePath/scripts.pory"
	map_script MAP_SCRIPT_ON_FRAME_TABLE, PellucaIcePath_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE
	.byte 0

PellucaIcePath_MapScripts_MAP_SCRIPT_ON_LOAD:
# 11 "data/maps/PellucaIcePath/scripts.pory"
	goto_if_set FLAG_DR_ICE_PATH_SOLVED, PellucaIcePath_MapScripts_MAP_SCRIPT_ON_LOAD_1
# 18 "data/maps/PellucaIcePath/scripts.pory"
	special DrIcePathReset
	return

PellucaIcePath_MapScripts_MAP_SCRIPT_ON_LOAD_1:
# 12 "data/maps/PellucaIcePath/scripts.pory"
	setvar VAR_ICE_STEP_COUNT, 999
# 13 "data/maps/PellucaIcePath/scripts.pory"
	call PellucaIcePath_EventScript_SetSolved
# 14 "data/maps/PellucaIcePath/scripts.pory"
	goto_if_set FLAG_DR_STATUE_AWAKENED, PellucaIcePath_MapScripts_MAP_SCRIPT_ON_LOAD_4
	return

PellucaIcePath_MapScripts_MAP_SCRIPT_ON_LOAD_4:
# 15 "data/maps/PellucaIcePath/scripts.pory"
	call PellucaIcePath_EventScript_SetAwakened
	return

PellucaIcePath_MapScripts_MAP_SCRIPT_ON_RESUME:
# 22 "data/maps/PellucaIcePath/scripts.pory"
	setstepcallback STEP_CB_SOOTOPOLIS_ICE
	return

PellucaIcePath_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE:
# 25 "data/maps/PellucaIcePath/scripts.pory"
	map_script_2 VAR_ICE_STEP_COUNT, 87, PellucaIcePath_EventScript_Solved
# 26 "data/maps/PellucaIcePath/scripts.pory"
	map_script_2 VAR_ICE_STEP_COUNT, 0, PellucaIcePath_EventScript_FallThroughIce
	.2byte 0


PellucaIcePath_EventScript_SetSolved::
# 31 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 12, METATILE_PellucaIcePath_GateOpen, FALSE
# 32 "data/maps/PellucaIcePath/scripts.pory"
	special DrIcePathFreeze
	return


PellucaIcePath_EventScript_Solved::
# 37 "data/maps/PellucaIcePath/scripts.pory"
	lockall
# 38 "data/maps/PellucaIcePath/scripts.pory"
	setvar VAR_ICE_STEP_COUNT, 999
# 39 "data/maps/PellucaIcePath/scripts.pory"
	delay 40
# 40 "data/maps/PellucaIcePath/scripts.pory"
	playse SE_ICE_STAIRS
# 41 "data/maps/PellucaIcePath/scripts.pory"
	call PellucaIcePath_EventScript_SetSolved
# 42 "data/maps/PellucaIcePath/scripts.pory"
	special DrawWholeMapView
# 43 "data/maps/PellucaIcePath/scripts.pory"
	setflag FLAG_DR_ICE_PATH_SOLVED
# 44 "data/maps/PellucaIcePath/scripts.pory"
	releaseall
	end


PellucaIcePath_EventScript_FallThroughIce::
# 49 "data/maps/PellucaIcePath/scripts.pory"
	lockall
# 50 "data/maps/PellucaIcePath/scripts.pory"
	delay 20
# 51 "data/maps/PellucaIcePath/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaIcePath_Movement_FallThroughIce
# 52 "data/maps/PellucaIcePath/scripts.pory"
	waitmovement 0
# 53 "data/maps/PellucaIcePath/scripts.pory"
	playse SE_FALL
# 54 "data/maps/PellucaIcePath/scripts.pory"
	delay 60
# 55 "data/maps/PellucaIcePath/scripts.pory"
	warpsilent MAP_PELLUCA_ICE_PATH, 0
# 56 "data/maps/PellucaIcePath/scripts.pory"
	waitstate
	end


# 60 "data/maps/PellucaIcePath/scripts.pory"
PellucaIcePath_Movement_FallThroughIce:
# 61 "data/maps/PellucaIcePath/scripts.pory"
	set_invisible
	step_end

PellucaIcePath_EventScript_SetAwakened::
# 65 "data/maps/PellucaIcePath/scripts.pory"
	call PellucaIcePath_EventScript_Melt4
# 66 "data/maps/PellucaIcePath/scripts.pory"
	call PellucaIcePath_EventScript_LightLeftFire
# 67 "data/maps/PellucaIcePath/scripts.pory"
	call PellucaIcePath_EventScript_LightRightFire
	return


PellucaIcePath_EventScript_Statue::
# 75 "data/maps/PellucaIcePath/scripts.pory"
	goto_if_set FLAG_DR_STATUE_AWAKENED, PellucaIcePath_EventScript_Statue_2
# 78 "data/maps/PellucaIcePath/scripts.pory"
	lockall
# 79 "data/maps/PellucaIcePath/scripts.pory"
	playbgm MUS_RAYQUAZA_APPEARS, FALSE
# 80 "data/maps/PellucaIcePath/scripts.pory"
	delay 16
# 81 "data/maps/PellucaIcePath/scripts.pory"
	playse SE_M_EARTHQUAKE
# 82 "data/maps/PellucaIcePath/scripts.pory"
	setvar VAR_0x8004, 1
# 83 "data/maps/PellucaIcePath/scripts.pory"
	setvar VAR_0x8005, 1
# 84 "data/maps/PellucaIcePath/scripts.pory"
	setvar VAR_0x8006, 12
# 85 "data/maps/PellucaIcePath/scripts.pory"
	setvar VAR_0x8007, 4
# 86 "data/maps/PellucaIcePath/scripts.pory"
	special ShakeCamera
# 87 "data/maps/PellucaIcePath/scripts.pory"
	waitstate
# 88 "data/maps/PellucaIcePath/scripts.pory"
	delay 20
# 89 "data/maps/PellucaIcePath/scripts.pory"
	playse SE_M_MORNING_SUN
# 90 "data/maps/PellucaIcePath/scripts.pory"
	call PellucaIcePath_EventScript_Melt0
# 91 "data/maps/PellucaIcePath/scripts.pory"
	special DrawWholeMapView
# 92 "data/maps/PellucaIcePath/scripts.pory"
	delay 24
# 93 "data/maps/PellucaIcePath/scripts.pory"
	call PellucaIcePath_EventScript_Melt1
# 94 "data/maps/PellucaIcePath/scripts.pory"
	special DrawWholeMapView
# 95 "data/maps/PellucaIcePath/scripts.pory"
	delay 24
# 96 "data/maps/PellucaIcePath/scripts.pory"
	call PellucaIcePath_EventScript_Melt2
# 97 "data/maps/PellucaIcePath/scripts.pory"
	special DrawWholeMapView
# 98 "data/maps/PellucaIcePath/scripts.pory"
	delay 24
# 99 "data/maps/PellucaIcePath/scripts.pory"
	call PellucaIcePath_EventScript_Melt3
# 100 "data/maps/PellucaIcePath/scripts.pory"
	special DrawWholeMapView
# 101 "data/maps/PellucaIcePath/scripts.pory"
	delay 24
# 102 "data/maps/PellucaIcePath/scripts.pory"
	call PellucaIcePath_EventScript_Melt4
# 103 "data/maps/PellucaIcePath/scripts.pory"
	special DrawWholeMapView
# 104 "data/maps/PellucaIcePath/scripts.pory"
	delay 24
# 105 "data/maps/PellucaIcePath/scripts.pory"
	waitse
# 106 "data/maps/PellucaIcePath/scripts.pory"
	fadescreenspeed FADE_TO_WHITE, 4
# 107 "data/maps/PellucaIcePath/scripts.pory"
	special DrPlayEchoCry
# 108 "data/maps/PellucaIcePath/scripts.pory"
	delay 30
# 109 "data/maps/PellucaIcePath/scripts.pory"
	fadescreenspeed FADE_FROM_WHITE, 4
# 110 "data/maps/PellucaIcePath/scripts.pory"
	waitmoncry
# 111 "data/maps/PellucaIcePath/scripts.pory"
	special DrEndEchoCry
# 112 "data/maps/PellucaIcePath/scripts.pory"
	delay 20
# 113 "data/maps/PellucaIcePath/scripts.pory"
	call PellucaIcePath_EventScript_LightLeftFire
# 114 "data/maps/PellucaIcePath/scripts.pory"
	special DrawWholeMapView
# 115 "data/maps/PellucaIcePath/scripts.pory"
	playse SE_M_SACRED_FIRE
# 116 "data/maps/PellucaIcePath/scripts.pory"
	delay 30
# 117 "data/maps/PellucaIcePath/scripts.pory"
	call PellucaIcePath_EventScript_LightRightFire
# 118 "data/maps/PellucaIcePath/scripts.pory"
	special DrawWholeMapView
# 119 "data/maps/PellucaIcePath/scripts.pory"
	playse SE_M_SACRED_FIRE
# 120 "data/maps/PellucaIcePath/scripts.pory"
	waitse
# 121 "data/maps/PellucaIcePath/scripts.pory"
	delay 30
# 122 "data/maps/PellucaIcePath/scripts.pory"
	fadedefaultbgm
# 123 "data/maps/PellucaIcePath/scripts.pory"
	delay 40
# 124 "data/maps/PellucaIcePath/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 125 "data/maps/PellucaIcePath/scripts.pory"
	special DrSetPrinceNameplate
# 126 "data/maps/PellucaIcePath/scripts.pory"
	msgbox PellucaIcePath_EventScript_Statue_Text_0
# 127 "data/maps/PellucaIcePath/scripts.pory"
	hideportrait
# 128 "data/maps/PellucaIcePath/scripts.pory"
	closemessage
# 129 "data/maps/PellucaIcePath/scripts.pory"
	setvar VAR_0x8004, ITEM_SPARKLING_OPAL
# 130 "data/maps/PellucaIcePath/scripts.pory"
	setvar VAR_0x8005, 1
# 131 "data/maps/PellucaIcePath/scripts.pory"
	setvar VAR_0x8006, ITEM_SPARKLING_OPAL
# 132 "data/maps/PellucaIcePath/scripts.pory"
	setvar VAR_0x8007, TRUE
# 133 "data/maps/PellucaIcePath/scripts.pory"
	additem ITEM_SPARKLING_OPAL
# 134 "data/maps/PellucaIcePath/scripts.pory"
	bufferitemname STR_VAR_2, ITEM_SPARKLING_OPAL
# 135 "data/maps/PellucaIcePath/scripts.pory"
	checkitemtype ITEM_SPARKLING_OPAL
# 136 "data/maps/PellucaIcePath/scripts.pory"
	call EventScript_BufferPocketNameAndTryFanfare
# 137 "data/maps/PellucaIcePath/scripts.pory"
	message PellucaIcePath_EventScript_Statue_Text_1
# 138 "data/maps/PellucaIcePath/scripts.pory"
	showitemdescription
# 139 "data/maps/PellucaIcePath/scripts.pory"
	waitfanfare
# 140 "data/maps/PellucaIcePath/scripts.pory"
	waitmessage
# 141 "data/maps/PellucaIcePath/scripts.pory"
	msgbox gText_PutItemInPocket, MSGBOX_DEFAULT
# 142 "data/maps/PellucaIcePath/scripts.pory"
	hideitemdescription
# 143 "data/maps/PellucaIcePath/scripts.pory"
	setflag FLAG_DR_STATUE_AWAKENED
# 144 "data/maps/PellucaIcePath/scripts.pory"
	releaseall
	end

PellucaIcePath_EventScript_Statue_2:
	end


PellucaIcePath_EventScript_Melt0::
# 149 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 6, 4, 0x20B, FALSE
# 150 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 6, 5, 0x24E, FALSE
# 151 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 1, 0x205, TRUE
# 152 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 2, 0x244, TRUE
# 153 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 3, 0x247, TRUE
# 154 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 4, 0x24A, TRUE
# 155 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 5, 0x24F, TRUE
# 156 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 6, 0x253, FALSE
# 157 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 1, 0x243, TRUE
# 158 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 2, 0x245, TRUE
# 159 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 3, 0x248, TRUE
# 160 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 4, 0x24B, TRUE
# 161 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 5, 0x250, TRUE
# 162 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 6, 0x254, FALSE
# 163 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 1, 0x207, TRUE
# 164 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 2, 0x246, TRUE
# 165 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 3, 0x249, TRUE
# 166 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 4, 0x24C, TRUE
# 167 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 5, 0x251, TRUE
# 168 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 6, 0x255, FALSE
# 169 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 10, 3, 0x20B, FALSE
# 170 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 10, 4, 0x24D, FALSE
# 171 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 10, 5, 0x252, FALSE
	return


PellucaIcePath_EventScript_Melt1::
# 176 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 6, 4, 0x20B, FALSE
# 177 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 6, 5, 0x25E, FALSE
# 178 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 1, 0x205, TRUE
# 179 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 2, 0x244, TRUE
# 180 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 3, 0x258, TRUE
# 181 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 4, 0x25B, TRUE
# 182 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 5, 0x25F, TRUE
# 183 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 6, 0x263, FALSE
# 184 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 1, 0x243, TRUE
# 185 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 2, 0x257, TRUE
# 186 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 3, 0x259, TRUE
# 187 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 4, 0x25C, TRUE
# 188 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 5, 0x260, TRUE
# 189 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 6, 0x264, FALSE
# 190 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 1, 0x256, TRUE
# 191 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 2, 0x246, TRUE
# 192 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 3, 0x25A, TRUE
# 193 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 4, 0x25D, TRUE
# 194 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 5, 0x261, TRUE
# 195 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 6, 0x265, FALSE
# 196 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 10, 3, 0x20B, FALSE
# 197 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 10, 4, 0x20B, FALSE
# 198 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 10, 5, 0x262, FALSE
	return


PellucaIcePath_EventScript_Melt2::
# 203 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 6, 4, 0x20B, FALSE
# 204 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 6, 5, 0x20B, FALSE
# 205 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 1, 0x205, TRUE
# 206 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 2, 0x244, TRUE
# 207 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 3, 0x258, TRUE
# 208 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 4, 0x266, TRUE
# 209 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 5, 0x269, TRUE
# 210 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 6, 0x26C, FALSE
# 211 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 1, 0x243, TRUE
# 212 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 2, 0x257, TRUE
# 213 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 3, 0x259, TRUE
# 214 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 4, 0x267, TRUE
# 215 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 5, 0x26A, TRUE
# 216 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 6, 0x26D, FALSE
# 217 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 1, 0x256, TRUE
# 218 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 2, 0x246, TRUE
# 219 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 3, 0x25A, TRUE
# 220 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 4, 0x268, TRUE
# 221 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 5, 0x26B, TRUE
# 222 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 6, 0x26E, FALSE
# 223 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 10, 3, 0x20B, FALSE
# 224 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 10, 4, 0x20B, FALSE
# 225 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 10, 5, 0x20B, FALSE
	return


PellucaIcePath_EventScript_Melt3::
# 230 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 6, 4, 0x20B, FALSE
# 231 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 6, 5, 0x20B, FALSE
# 232 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 1, 0x205, TRUE
# 233 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 2, 0x244, TRUE
# 234 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 3, 0x258, TRUE
# 235 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 4, 0x266, TRUE
# 236 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 5, 0x26F, TRUE
# 237 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 6, 0x272, FALSE
# 238 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 1, 0x243, TRUE
# 239 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 2, 0x257, TRUE
# 240 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 3, 0x259, TRUE
# 241 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 4, 0x267, TRUE
# 242 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 5, 0x270, TRUE
# 243 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 6, 0x273, FALSE
# 244 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 1, 0x256, TRUE
# 245 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 2, 0x246, TRUE
# 246 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 3, 0x25A, TRUE
# 247 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 4, 0x268, TRUE
# 248 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 5, 0x271, TRUE
# 249 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 6, 0x274, FALSE
# 250 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 10, 3, 0x20B, FALSE
# 251 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 10, 4, 0x20B, FALSE
# 252 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 10, 5, 0x20B, FALSE
	return


PellucaIcePath_EventScript_Melt4::
# 257 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 6, 4, 0x20B, FALSE
# 258 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 6, 5, 0x20B, FALSE
# 259 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 1, 0x205, TRUE
# 260 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 2, 0x244, TRUE
# 261 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 3, 0x258, TRUE
# 262 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 4, 0x266, TRUE
# 263 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 5, 0x275, TRUE
# 264 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 7, 6, 0x278, FALSE
# 265 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 1, 0x243, TRUE
# 266 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 2, 0x257, TRUE
# 267 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 3, 0x259, TRUE
# 268 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 4, 0x267, TRUE
# 269 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 5, 0x276, TRUE
# 270 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 6, 0x279, FALSE
# 271 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 1, 0x256, TRUE
# 272 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 2, 0x246, TRUE
# 273 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 3, 0x25A, TRUE
# 274 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 4, 0x268, TRUE
# 275 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 5, 0x277, TRUE
# 276 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 9, 6, 0x27A, FALSE
# 277 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 10, 3, 0x20B, FALSE
# 278 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 10, 4, 0x20B, FALSE
# 279 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 10, 5, 0x20B, FALSE
	return


PellucaIcePath_EventScript_LightLeftFire::
# 284 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 5, 5, 0x280, TRUE
	return


PellucaIcePath_EventScript_LightRightFire::
# 289 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 11, 5, 0x280, TRUE
	return


PellucaIcePath_EventScript_Statue_Text_0:
# 126 "data/maps/PellucaIcePath/scripts.pory"
	.string "Something fell down out of the ice...\n"
	.string "Could this be...!!$"

PellucaIcePath_EventScript_Statue_Text_1:
# 137 "data/maps/PellucaIcePath/scripts.pory"
	.string "{PLAYER} found the Sparkling Opal!$"
