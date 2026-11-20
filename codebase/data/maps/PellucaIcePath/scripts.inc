PellucaIcePath_MapScripts::
# 10 "data/maps/PellucaIcePath/scripts.pory"
	map_script MAP_SCRIPT_ON_LOAD, PellucaIcePath_MapScripts_MAP_SCRIPT_ON_LOAD
# 18 "data/maps/PellucaIcePath/scripts.pory"
	map_script MAP_SCRIPT_ON_RESUME, PellucaIcePath_MapScripts_MAP_SCRIPT_ON_RESUME
# 21 "data/maps/PellucaIcePath/scripts.pory"
	map_script MAP_SCRIPT_ON_FRAME_TABLE, PellucaIcePath_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE
	.byte 0

PellucaIcePath_MapScripts_MAP_SCRIPT_ON_LOAD:
# 11 "data/maps/PellucaIcePath/scripts.pory"
	goto_if_set FLAG_DR_ICE_PATH_SOLVED, PellucaIcePath_MapScripts_MAP_SCRIPT_ON_LOAD_1
# 15 "data/maps/PellucaIcePath/scripts.pory"
	special DrIcePathReset
	return

PellucaIcePath_MapScripts_MAP_SCRIPT_ON_LOAD_1:
# 12 "data/maps/PellucaIcePath/scripts.pory"
	setvar VAR_ICE_STEP_COUNT, 999
# 13 "data/maps/PellucaIcePath/scripts.pory"
	call PellucaIcePath_EventScript_SetSolved
	return

PellucaIcePath_MapScripts_MAP_SCRIPT_ON_RESUME:
# 19 "data/maps/PellucaIcePath/scripts.pory"
	setstepcallback STEP_CB_SOOTOPOLIS_ICE
	return

PellucaIcePath_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE:
# 22 "data/maps/PellucaIcePath/scripts.pory"
	map_script_2 VAR_ICE_STEP_COUNT, 87, PellucaIcePath_EventScript_Solved
# 23 "data/maps/PellucaIcePath/scripts.pory"
	map_script_2 VAR_ICE_STEP_COUNT, 0, PellucaIcePath_EventScript_FallThroughIce
	.2byte 0


PellucaIcePath_EventScript_SetSolved::
# 28 "data/maps/PellucaIcePath/scripts.pory"
	setmetatile 8, 12, METATILE_PellucaIcePath_GateOpen, FALSE
# 29 "data/maps/PellucaIcePath/scripts.pory"
	special DrIcePathFreeze
	return


PellucaIcePath_EventScript_Solved::
# 34 "data/maps/PellucaIcePath/scripts.pory"
	lockall
# 35 "data/maps/PellucaIcePath/scripts.pory"
	setvar VAR_ICE_STEP_COUNT, 999
# 36 "data/maps/PellucaIcePath/scripts.pory"
	delay 40
# 37 "data/maps/PellucaIcePath/scripts.pory"
	playse SE_ICE_STAIRS
# 38 "data/maps/PellucaIcePath/scripts.pory"
	call PellucaIcePath_EventScript_SetSolved
# 39 "data/maps/PellucaIcePath/scripts.pory"
	special DrawWholeMapView
# 40 "data/maps/PellucaIcePath/scripts.pory"
	setflag FLAG_DR_ICE_PATH_SOLVED
# 41 "data/maps/PellucaIcePath/scripts.pory"
	releaseall
	end


PellucaIcePath_EventScript_FallThroughIce::
# 46 "data/maps/PellucaIcePath/scripts.pory"
	lockall
# 47 "data/maps/PellucaIcePath/scripts.pory"
	delay 20
# 48 "data/maps/PellucaIcePath/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaIcePath_Movement_FallThroughIce
# 49 "data/maps/PellucaIcePath/scripts.pory"
	waitmovement 0
# 50 "data/maps/PellucaIcePath/scripts.pory"
	playse SE_FALL
# 51 "data/maps/PellucaIcePath/scripts.pory"
	delay 60
# 52 "data/maps/PellucaIcePath/scripts.pory"
	warpsilent MAP_PELLUCA_ICE_PATH, 0
# 53 "data/maps/PellucaIcePath/scripts.pory"
	waitstate
	end


# 57 "data/maps/PellucaIcePath/scripts.pory"
PellucaIcePath_Movement_FallThroughIce:
# 58 "data/maps/PellucaIcePath/scripts.pory"
	set_invisible
	step_end
