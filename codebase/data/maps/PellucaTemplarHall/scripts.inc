PellucaTemplarHall_MapScripts::
# 8 "data/maps/PellucaTemplarHall/scripts.pory"
	map_script MAP_SCRIPT_ON_TRANSITION, PellucaTemplarHall_MapScripts_MAP_SCRIPT_ON_TRANSITION
	.byte 0

PellucaTemplarHall_MapScripts_MAP_SCRIPT_ON_TRANSITION:
# 9 "data/maps/PellucaTemplarHall/scripts.pory"
	goto_if_set FLAG_DR_CHURCH_BLASTED, PellucaTemplarHall_MapScripts_MAP_SCRIPT_ON_TRANSITION_1
	return

PellucaTemplarHall_MapScripts_MAP_SCRIPT_ON_TRANSITION_1:
# 10 "data/maps/PellucaTemplarHall/scripts.pory"
	setmaplayoutindex LAYOUT_PELLUCA_TEMPLAR_HALL_RUINED
	return

