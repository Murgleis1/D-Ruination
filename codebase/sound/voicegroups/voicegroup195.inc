@ voicegroup195: Dreamstone Ruination soft "pedal" piano -- the game's multi-sampled piano (voicegroup005: sc88pro
@ piano1 recorded at C3/C4/C5/C6, split by KeySplitTable1) with a smooth envelope: full attack, slow decay to a
@ little sustain, long release, so notes ring on like a held sustain pedal. Used by voicegroup194 program 0
@ (the title theme, MUS_DR_TITLE).
	.align 2
voicegroup195::
	voice_directsound 60, 0, DirectSoundWaveData_sc88pro_piano1_48, 255, 252, 40, 244
	voice_directsound 60, 0, DirectSoundWaveData_sc88pro_piano1_60, 255, 251, 40, 242
	voice_directsound 60, 0, DirectSoundWaveData_sc88pro_piano1_72, 255, 250, 36, 240
	voice_directsound 60, 0, DirectSoundWaveData_sc88pro_piano1_84, 255, 248, 32, 236
