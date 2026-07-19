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
	.string "My Prince, it has been far\ntoo long since our last\pcorrespondence.\pWord has reached me of your\ncurrent physical condition\pin light of what happened\nduring the Sevii campaign.\pIt is sheer travesty.\pMy fury at Boran Surge's\nnegligence and the\pincompetence of his\ncommanding officers in\ptheir choice of strategy\nagainst both Kanto and\pJohto is a fury I cannot\ntranscribe here in written\pform, for the very ink\nwould turn to fire if I\pwere to try.\pAs you can imagine, I have\nmade my displeasure to your\psuperiors excruciatingly\nknown.$"

PellucaReflection_LetterB:
	.string "You will be given full\ndetails later, I will say\pthat in brief, you are now\nreassigned formally to\pservice under my authority\nas Vizier Of Education,\palong with an honorable\npromotion to the rank of\pRainhawk.\pYou will be the youngest in\nCormoria's history to\pachieve this rank...yes,\neven younger than “him”.$"

PellucaReflection_LetterC:
	.string "I will see you at my\nlaboratories soon. I am\pmaking arrangements with\nthe captain of the Pale\pVeluza to receive you, so\ninquire with General\pAlbrecht for additional\ndetails. By the time you\preceive this, he will have\nmore to share with you.\pP.S. Please burn this\nletter as soon as you have\pdrafted your acceptance, as\nwe must minimize the paper\ptrail. There are many eyes\nin places even I cannot\pgrasp.\pPlease sign your response\nwith the name that only\p“you” know, so I may know\nthis was not intercepted.\pThe Templar near your\ncurrent base of operations\pshould be able to deliver\nyour response to me\pdirectly.$"

PellucaReflection_LetterD:
	.string "My dearest regards,\nCadmus Umbra$"

PellucaReflection_SignPrompt:
	.string "You take up your pen to\ndraft your reply.$"

PellucaReflection_Reply:
	.string "Request acknowledged and\naccepted. I will make\ppreparations to travel\nimmediately.$"

