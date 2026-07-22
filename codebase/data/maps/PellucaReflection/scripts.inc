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
	setvar VAR_UNUSED_0x404E, 1
		warp MAP_PELLUCA_CITY, 44, 52
	waitstate
	releaseall
	end

PellucaReflection_FaceDown:
	face_down
	step_end

PellucaReflection_LetterIntro:
	.string "You have received a letter.$"

PellucaReflection_LetterA:
	.string "My Prince... far too long\nhas passed since our last\pletter over a year ago. It\nfeels far longer than\pthat.\pWord of your scarred\ncondition has reached me,\palong with the truth of\nwhat happened during the\pSevii campaign. I hear you\nnow wear a mask to cover\pyour burns, and I will not\ninsult you by calling this\panything less than a\ntravesty.\pThere is no shortage of\nfolly and negligence\paround you. Your\ncommanding officer Boran\pSurge's foolish choice to\nstrike Kanto and Johto\pacross two separate fronts\nhas resulted in countless\plosses.\pI have made my...lets just\nsay “unhappiness” known to\pSurge's superiors, and I\nhave been assured that he\pwill be dealt with. This\ndoes not reverse the harms\pthat were done to you...\nbut he may wish he had\pdied in the Sevii campaign\nhe forced your unit into\pbefore\nhis...“punishment”...\pfully plays itself out.$"

PellucaReflection_LetterB:
	.string "However, I have not written\nto you merely out of\pfrustration and anger. As a\nresult of my demands, you\pare now formally reassigned\nto serve under my direct\pcommand as Vizier of\nEducation, and raised to\pthe rank of Rainhawk. You\nhave been discharged from\pthe front lines with the\nhighest of honors.\pFurthermore, you are now\nthe youngest to hold this\ptitle in all of Cormoria's\nhistory. Yes, younger even\pthan “him”. You know of\nwhom I speak. This comes\pwith numerous benefits,\nthough we will speak more\lon that later.$"

PellucaReflection_LetterC:
	.string "My request is this. Please\ncome to my laboratory as\psoon as you are able. I\nchartered a ship, the Pale\pVeluza, to bring you home.\nGeneral Albrecht will fill\pyou in on additional\ndetails about your\parrangements, so go speak\nwith him.\pLastly, please sign your\nreply with the name only\p“you” know, so I may be\ncertain of your “true”\pidentity. The Templar who\nserves near your barracks\pwill deliver it to my hand\ndirectly.\pP.S. Burn this letter.\nThere must be no trail.\pMatters in your homeland\nof Cormoria have grown\pmore delicate than they\nappear, and there are eyes\pand ears in places even I\ncannot know. Be vigilant.$"

PellucaReflection_LetterD:
	.string "Best regards,\nCadmus Umbra$"

PellucaReflection_SignPrompt:
	.string "You take up your pen to\ndraft your reply.$"

PellucaReflection_Reply:
	.string "Request acknowledged and\naccepted. I will make\ppreparations to travel\nimmediately.$"

