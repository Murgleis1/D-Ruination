PellucaReflection_MapScripts::
	map_script MAP_SCRIPT_ON_FRAME_TABLE, PellucaReflection_OnFrame
	.byte 0

PellucaReflection_OnFrame:
	map_script_2 VAR_TEMP_1, 0, PellucaReflection_Cutscene
	.2byte 0

PellucaReflection_Cutscene::
	lockall
	setvar VAR_TEMP_1, 1
	special DrSetPlayerOsridSprite
	applymovement OBJ_EVENT_ID_PLAYER, PellucaReflection_FaceDown
	waitmovement 0
	delay 40
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
	msgbox PellucaReflection_LetterA, MSGBOX_DEFAULT
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
	msgbox PellucaReflection_LetterB, MSGBOX_DEFAULT
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
	msgbox PellucaReflection_LetterC, MSGBOX_DEFAULT
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
	msgbox PellucaReflection_LetterD, MSGBOX_DEFAULT
	hideportrait
	msgbox PellucaReflection_SignPrompt, MSGBOX_DEFAULT
	special DrDoPlayerNaming
	waitstate
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
	msgbox PellucaReflection_Reply, MSGBOX_DEFAULT
	hideportrait
	delay 40
	fadescreen FADE_TO_BLACK
	warp MAP_CARABRUE_TOWN_HOME1F, 0
	waitstate
	releaseall
	end

PellucaReflection_FaceDown:
	face_down
	step_end

PellucaReflection_LetterA:
	.string "My Prince. Far too long has\npassed since your last\lletter.\pWord of your condition\nreached me not long ago,\palong with the truth of\nwhat happened during the\pSevii campaign. I will not\ninsult you by calling it\panything less than a\ntravesty.\pBoran Surge's negligence\nhas earned my fury, as has\pthe choice to fight Kanto\nand Johto at once. I have\pmade it known to your\nsuperiors in terms they\lwill not soon forget.$"

PellucaReflection_LetterB:
	.string "I did not write to you in\nanger alone. From this day\pyou are reassigned to serve\nunder my authority as\pVizier of Education, and\nraised to the rank of\lRainhawk.\pThe youngest to hold it in\nall of Cormoria's history.\lYounger even than “him”.$"

PellucaReflection_LetterC:
	.string "Come to my laboratories as\nsoon as you are able. The\pcaptain of the Pale Veluza\nwill carry you to me, and\pGeneral Albrecht holds the\nrest of your instructions.\pSign your reply with the\nname only “you” know, so I\pmay be certain it is truly\nfrom you. The Templar near\pyour post will place it in\nmy hand, and no other's.\pThen burn this letter. We\ncan leave no trail. Matters\pat home have grown more\ndelicate than they appear,\pand there are eyes in\nplaces even I cannot reach.$"

PellucaReflection_LetterD:
	.string "My dearest regards,\nCadmus Umbra$"

PellucaReflection_SignPrompt:
	.string "You take up your pen to\ndraft your reply.$"

PellucaReflection_Reply:
	.string "Request acknowledged and\naccepted. I will make\ppreparations to travel\nimmediately.$"

