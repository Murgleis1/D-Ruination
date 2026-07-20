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
	msgbox PellucaReflection_LetterIntro, MSGBOX_DEFAULT
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
	special DrSetPrinceNameplate
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

PellucaReflection_LetterIntro:
	.string "You have received a letter.$"

PellucaReflection_LetterA:
	.string "My Prince....far too long\nhas passed since our last\pletter over a year ago. It\nwas before you were even\passigned to your formal\nunit, if I'm not mistaken.\pWord of your condition has\nreached me, along with the\ptruth of what happened\nduring the Sevii campaign.\pI hear you now wear a mask\nto cover your burns, and I\pwill not insult you by\ncalling this anything less\lthan a travesty.\pThere is no shortage of\nfolly and negligence around\pyou, my Prince. Your\nsuperior officer and\phandler Boran Surge's\nfoolish choice to strike\pKanto and Johto across two\nseparate fronts has\presulted in countless\nlosses.\pI have made my wrath known\nto your commanders, and I\phave been assured that he\nwill be dealt with. This\pdoes not reverse the harms\nthat were done to you, but\phe will wish he was dead by\nthe end of this process.$"

PellucaReflection_LetterB:
	.string "However, I have not written\nto you merely out of\pfrustration and anger. As a\nresult of my demands, you\pare now formally reassigned\nto serve under my direct\pcommand as Vizier of\nEducation, and raised to\pthe rank of Rainhawk. You\nhave been discharged from\pthe front lines with the\nhighest of honors.\pFurthermore, you are now\nthe youngest to hold this\ptitle in all of Cormoria's\nhistory. Yes, younger even\pthan “him”. You know of\nwhom I speak. This comes\pwith numerous benefits,\nthough we will speak more\lon that later.$"

PellucaReflection_LetterC:
	.string "My request is this. Please\ncome to see me at my\plaboratory as soon as you\nare able. General Albrecht\pwill fill you in on\nadditional details of your\pdeparture aboard the Pale\nVeluza which will be\pdocking near you soon, so\nspeak with him as soon as\lyou can.\pSign your reply with the\nname only “you” know, so I\pmay be certain of your\n“true” identity. The\pTemplar who serves near\nyour barracks will deliver\lit to my hand directly.\pAlso...please burn this\nletter. We must leave no\ptrail. Matters in your\nhomeland of Cormoria have\pgrown more delicate than\nthey appear, and there are\peyes in places even I\ncannot see. Be vigilant.$"

PellucaReflection_LetterD:
	.string "Best regards,\nCadmus Umbra$"

PellucaReflection_SignPrompt:
	.string "You take up your pen to\ndraft your reply.$"

PellucaReflection_Reply:
	.string "Request acknowledged and\naccepted. I will make\ppreparations to travel\nimmediately.$"

