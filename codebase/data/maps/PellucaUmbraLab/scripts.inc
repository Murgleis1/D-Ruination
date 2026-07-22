PellucaUmbraLab_MapScripts::
	map_script MAP_SCRIPT_ON_FRAME_TABLE, PellucaUmbraLab_OnFrame
	.byte 0

PellucaUmbraLab_OnFrame:
	map_script_2 VAR_TEMP_1, 0, PellucaUmbraLab_Briefing
	.2byte 0

PellucaUmbraLab_Briefing::
	lockall
	setvar VAR_TEMP_1, 1
	delay 30
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
	msgbox PellucaUmbraLab_Text_Brief1, MSGBOX_DEFAULT
	msgbox PellucaUmbraLab_Text_Brief2, MSGBOX_DEFAULT
	msgbox PellucaUmbraLab_Text_Brief3, MSGBOX_DEFAULT
	msgbox PellucaUmbraLab_Text_Brief4, MSGBOX_DEFAULT
	msgbox PellucaUmbraLab_Text_Brief5, MSGBOX_DEFAULT
	msgbox PellucaUmbraLab_Text_Brief6, MSGBOX_DEFAULT
	hideportrait
	releaseall
	end

PellucaUmbraLab_EventScript_Umbra::
	lock
	faceplayer
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
	msgbox PellucaUmbraLab_Text_UmbraTalk, MSGBOX_DEFAULT
	hideportrait
	release
	end

PellucaUmbraLab_Text_Brief1:
	.string "Welcome to Pelluca Valley,\nmy Prince. Or rather... to\pthe only corner of this\nempire where I can be\pcertain we are not\noverheard.$"

PellucaUmbraLab_Text_Brief2:
	.string "From this moment, you are\nno longer Osrid. To the\pworld, you are Nomad Alban:\na Rainhawk honorably\pdischarged from the front,\nnow serving as my personal\lassistant.$"

PellucaUmbraLab_Text_Brief3:
	.string "Publicly, you will serve as\nhead of security for the\pAcademy. A house in the\nvalley has been made ready\pas your residence. The\ncover is sound. Wear it\lwell.$"

PellucaUmbraLab_Text_Brief4:
	.string "Your task is twofold. The\nfirst, all the world may\psee: become a true Trainer,\nand earn every Trial Badge\lin Cormoria.$"

PellucaUmbraLab_Text_Brief5:
	.string "That is how you will win\nthe standing to challenge\pthe Champion... your\nsister, Rhydia... and from\pthat stage, at last, reveal\nwho you truly are.$"

PellucaUmbraLab_Text_Brief6:
	.string "The second task, no one may\nsee. Nine shards of a\pshattered Mega-Dreamstone\nlie hidden across the\pempire. You will recover\nthem, quietly, before the\pcults do. Fail... and there\nmay be no empire left to\lreveal yourself to.$"

PellucaUmbraLab_Text_UmbraTalk:
	.string "Take the time you need.\nWhen you are ready, we will\lbegin in earnest.$"
