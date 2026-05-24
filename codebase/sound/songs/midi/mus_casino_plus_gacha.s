	.include "MPlayDef.s"

	.equ	mus_casino_plus_gacha_grp, voicegroup192
	.equ	mus_casino_plus_gacha_pri, 0
	.equ	mus_casino_plus_gacha_rev, reverb_set+50
	.equ	mus_casino_plus_gacha_mvl, 127
	.equ	mus_casino_plus_gacha_key, 0
	.equ	mus_casino_plus_gacha_tbs, 1
	.equ	mus_casino_plus_gacha_exg, 1
	.equ	mus_casino_plus_gacha_cmp, 1

	.section .rodata
	.global	mus_casino_plus_gacha
	.align	2

@**************** Track 1 (Midi-Chn.1) ****************@

mus_casino_plus_gacha_1:
	.byte	KEYSH , mus_casino_plus_gacha_key+0
@ 000   ----------------------------------------
	.byte	TEMPO , 154*mus_casino_plus_gacha_tbs/2
	.byte		VOICE , 11
	.byte		VOL   , 109*mus_casino_plus_gacha_mvl/mxv
	.byte		MOD   , 0
	.byte		PAN   , c_v+0
	.byte		BEND  , c_v+0
	.byte		N11   , Fs3 , v127
	.byte	W12
	.byte		N11   
	.byte	W12
	.byte		N05   , Fs3 , v040
	.byte	W12
	.byte		N23   , An3 , v127
	.byte	W24
	.byte		N11   , Gs3 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        Bn3 
	.byte	W12
mus_casino_plus_gacha_1_B1:
@ 001   ----------------------------------------
	.byte		N11   , Cs4 , v127
	.byte	W12
	.byte		N05   , Cs4 , v040
	.byte	W12
	.byte		N11   , Cs4 , v127
	.byte	W12
	.byte		N05   , Cs4 , v040
	.byte	W12
	.byte		N11   , Bn3 , v127
	.byte	W12
	.byte		N11   
	.byte	W12
	.byte		N05   , Bn3 , v040
	.byte	W12
	.byte		N11   , An3 , v127
	.byte	W12
@ 002   ----------------------------------------
	.byte		N05   , An3 , v040
	.byte	W12
	.byte		N11   , An3 , v127
	.byte	W12
	.byte		        Gs3 
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        Bn3 
	.byte	W12
	.byte		N05   , Bn3 , v040
	.byte	W12
	.byte		N11   , Cs4 , v127
	.byte	W12
@ 003   ----------------------------------------
	.byte		N05   , Cs4 , v040
	.byte	W24
	.byte		N11   , Cs4 , v127
	.byte	W12
	.byte		N05   , Cs4 , v040
	.byte	W12
	.byte		N11   , Bn3 , v127
	.byte	W12
	.byte		N11   
	.byte	W12
	.byte		N05   , Bn3 , v040
	.byte	W12
	.byte		N11   , An3 , v127
	.byte	W12
@ 004   ----------------------------------------
	.byte		N05   , An3 , v040
	.byte	W12
	.byte		N11   , An3 , v127
	.byte	W12
	.byte		        Gs3 
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        Bn3 
	.byte	W12
	.byte		N05   , Bn3 , v040
	.byte	W12
	.byte		N11   , Dn4 , v127
	.byte	W12
@ 005   ----------------------------------------
mus_casino_plus_gacha_1_005:
	.byte		N05   , Dn4 , v040
	.byte	W24
	.byte		N11   , Dn4 , v127
	.byte	W12
	.byte		N05   , Dn4 , v040
	.byte	W12
	.byte		N11   , Cs4 , v127
	.byte	W12
	.byte		N11   
	.byte	W12
	.byte		N05   , Cs4 , v040
	.byte	W12
	.byte		N11   , Bn3 , v127
	.byte	W12
	.byte	PEND
@ 006   ----------------------------------------
	.byte		N05   , Bn3 , v040
	.byte	W12
	.byte		N11   , Bn3 , v127
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        Gs3 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        Bn3 
	.byte	W12
	.byte		N05   , Bn3 , v040
	.byte	W12
	.byte		N11   , Dn4 , v127
	.byte	W12
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_gacha_1_005
@ 008   ----------------------------------------
	.byte		N05   , Bn3 , v040
	.byte	W12
	.byte		N11   , Bn3 , v127
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        Gs3 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        Gs3 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        Bn3 
	.byte	W11
	.byte	GOTO
	 .word	mus_casino_plus_gacha_1_B1
mus_casino_plus_gacha_1_B2:
	.byte	FINE

@**************** Track 2 (Midi-Chn.2) ****************@

mus_casino_plus_gacha_2:
	.byte	KEYSH , mus_casino_plus_gacha_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 11
	.byte		VOL   , 101*mus_casino_plus_gacha_mvl/mxv
	.byte		MOD   , 0
	.byte		PAN   , c_v-9
	.byte		BEND  , c_v+0
	.byte		N11   , Dn3 , v112
	.byte	W12
	.byte		N11   
	.byte	W24
	.byte		N23   , Fs3 
	.byte	W24
	.byte		N11   , En3 
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte		        Gs3 
	.byte	W12
mus_casino_plus_gacha_2_B1:
@ 001   ----------------------------------------
	.byte		N11   , An3 , v112
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte		        Gs3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Gs3 
	.byte	W12
	.byte		        Fs3 
	.byte	W12
@ 002   ----------------------------------------
	.byte	W12
	.byte		N11   
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte		        Gs3 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte		        An3 
	.byte	W12
@ 003   ----------------------------------------
	.byte		        Cs3 
	.byte	W12
	.byte		N11   
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte		        Gs3 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        Gs3 
	.byte	W12
	.byte		        Fs3 
	.byte	W12
@ 004   ----------------------------------------
	.byte		        Cs3 
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte		        Gs3 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte		        An3 
	.byte	W12
@ 005   ----------------------------------------
	.byte		        Dn3 
	.byte	W12
	.byte		N11   
	.byte	W12
	.byte		        As3 
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte		        As3 
	.byte	W12
	.byte		N11   
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte		        An3 
	.byte	W12
@ 006   ----------------------------------------
	.byte		        Dn3 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte		N11   
	.byte	W12
	.byte		        Gs3 
	.byte	W12
	.byte		        An3 
	.byte	W12
@ 007   ----------------------------------------
	.byte		        Dn3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		N11   
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte		        An3 
	.byte	W12
@ 008   ----------------------------------------
	.byte		        Dn3 
	.byte	W12
	.byte		        Gs3 
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte		        Gs3 
	.byte	W11
	.byte	GOTO
	 .word	mus_casino_plus_gacha_2_B1
mus_casino_plus_gacha_2_B2:
	.byte	FINE

@**************** Track 3 (Midi-Chn.3) ****************@

mus_casino_plus_gacha_3:
	.byte	KEYSH , mus_casino_plus_gacha_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 11
	.byte		VOL   , 100*mus_casino_plus_gacha_mvl/mxv
	.byte		MOD   , 0
	.byte		PAN   , c_v+0
	.byte		BEND  , c_v+0
	.byte		N11   , An2 , v112
	.byte	W12
	.byte		N11   
	.byte	W24
	.byte		N23   , Dn3 
	.byte	W56
	.byte	W03
	.byte		VOICE , 46
	.byte	W01
mus_casino_plus_gacha_3_B1:
@ 001   ----------------------------------------
	.byte		PAN   , c_v+8
	.byte	W48
	.byte		N44   , En4 , v112
	.byte	W48
@ 002   ----------------------------------------
mus_casino_plus_gacha_3_002:
	.byte		N44   , An4 , v112
	.byte	W48
	.byte		        Bn4 
	.byte	W48
	.byte	PEND
@ 003   ----------------------------------------
	.byte		N92   , Gs4 
	.byte	W96
@ 004   ----------------------------------------
	.byte		        Fs4 
	.byte	W96
@ 005   ----------------------------------------
	.byte	W48
	.byte		N44   
	.byte	W48
@ 006   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_gacha_3_002
@ 007   ----------------------------------------
	.byte		N92   , Cs5 , v112
	.byte	W96
@ 008   ----------------------------------------
	.byte		        Bn4 
	.byte	W92
	.byte	W03
	.byte	GOTO
	 .word	mus_casino_plus_gacha_3_B1
mus_casino_plus_gacha_3_B2:
	.byte	FINE

@**************** Track 4 (Midi-Chn.4) ****************@

mus_casino_plus_gacha_4:
	.byte	KEYSH , mus_casino_plus_gacha_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 33
	.byte		VOL   , 100*mus_casino_plus_gacha_mvl/mxv
	.byte		MOD   , 0
	.byte		PAN   , c_v+0
	.byte		BEND  , c_v+0
	.byte		N23   , En1 , v127
	.byte	W24
	.byte		N05   , En1 , v040
	.byte	W12
	.byte		N11   , En1 , v127
	.byte	W12
	.byte		N05   , En1 , v040
	.byte	W12
	.byte		N11   , En1 , v127
	.byte	W12
	.byte		        En2 
	.byte	W12
	.byte		        En1 
	.byte	W12
mus_casino_plus_gacha_4_B1:
@ 001   ----------------------------------------
	.byte		N11   , An1 , v127
	.byte	W12
	.byte		N05   , An1 , v040
	.byte	W24
	.byte		N11   , An1 , v127
	.byte	W12
	.byte		N11   
	.byte	W12
	.byte		N05   , An1 , v040
	.byte	W24
	.byte		N11   , En1 , v127
	.byte	W12
@ 002   ----------------------------------------
	.byte		        An1 
	.byte	W12
	.byte		N05   , An1 , v040
	.byte	W12
	.byte		N11   , En1 , v127
	.byte	W12
	.byte		        An1 
	.byte	W12
	.byte		N05   , An1 , v040
	.byte	W12
	.byte		N11   , En2 , v127
	.byte	W12
	.byte		        En1 
	.byte	W12
	.byte		N05   , En1 , v040
	.byte	W12
@ 003   ----------------------------------------
	.byte		N11   , Fs1 , v127
	.byte	W12
	.byte		N05   , Fs1 , v040
	.byte	W12
	.byte		N11   , Fs2 , v127
	.byte	W12
	.byte		        Fs1 
	.byte	W12
	.byte		N05   , Fs1 , v040
	.byte	W12
	.byte		N11   , Fs1 , v127
	.byte	W12
	.byte		N05   , Fs1 , v040
	.byte	W12
	.byte		N11   , En1 , v127
	.byte	W12
@ 004   ----------------------------------------
	.byte		        Fs1 
	.byte	W12
	.byte		N05   , Fs1 , v040
	.byte	W12
	.byte		N11   , Cs2 , v127
	.byte	W12
	.byte		        Fs1 
	.byte	W12
	.byte		N05   , Fs1 , v040
	.byte	W12
	.byte		N11   , Fs1 , v127
	.byte	W12
	.byte		        Cs2 
	.byte	W12
	.byte		        Fs1 
	.byte	W12
@ 005   ----------------------------------------
	.byte		        Bn1 
	.byte	W12
	.byte		N05   , Bn1 , v040
	.byte	W12
	.byte		N11   , Fs1 , v127
	.byte	W12
	.byte		        Bn1 
	.byte	W12
	.byte		N05   , Bn1 , v040
	.byte	W12
	.byte		N11   , Bn1 , v127
	.byte	W12
	.byte		N05   , Bn1 , v040
	.byte	W12
	.byte		N11   , Fs1 , v127
	.byte	W12
@ 006   ----------------------------------------
	.byte		        Bn1 
	.byte	W12
	.byte		N05   , Bn1 , v040
	.byte	W24
	.byte		N11   , Fs2 , v127
	.byte	W12
	.byte		        En2 
	.byte	W12
	.byte		        Cs2 
	.byte	W12
	.byte		        Bn1 
	.byte	W12
	.byte		        Gs1 
	.byte	W12
@ 007   ----------------------------------------
	.byte		        En1 
	.byte	W12
	.byte		N05   , En1 , v040
	.byte	W24
	.byte		N11   , Bn0 , v127
	.byte	W12
	.byte		        En1 
	.byte	W12
	.byte		N05   , En1 , v040
	.byte	W12
	.byte		N11   , Bn0 , v127
	.byte	W12
	.byte		        En1 
	.byte	W12
@ 008   ----------------------------------------
	.byte		        Gs1 
	.byte	W12
	.byte		        En1 
	.byte	W12
	.byte		N05   , En1 , v040
	.byte	W12
	.byte		N11   , Bn1 , v127
	.byte	W12
	.byte		N05   , Bn1 , v040
	.byte	W12
	.byte		N11   , En2 , v127
	.byte	W12
	.byte		        Dn2 
	.byte	W12
	.byte		        En1 
	.byte	W11
	.byte	GOTO
	 .word	mus_casino_plus_gacha_4_B1
mus_casino_plus_gacha_4_B2:
	.byte	FINE

@**************** Track 5 (Midi-Chn.5) ****************@

mus_casino_plus_gacha_5:
	.byte	KEYSH , mus_casino_plus_gacha_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 0
	.byte		VOL   , 103*mus_casino_plus_gacha_mvl/mxv
	.byte		MOD   , 0
	.byte		PAN   , c_v+0
	.byte		VOL   , 103*mus_casino_plus_gacha_mvl/mxv
	.byte		MOD   , 0
	.byte		PAN   , c_v+0
	.byte		BEND  , c_v+0
	.byte		N11   , Cn1 , v112
	.byte	W12
	.byte		N11   
	.byte	W24
	.byte		N23   
	.byte	W36
	.byte		N11   
	.byte	W24
mus_casino_plus_gacha_5_B1:
@ 001   ----------------------------------------
mus_casino_plus_gacha_5_001:
	.byte		N11   , Cn1 , v112
	.byte	W12
	.byte		N11   
	.byte	W12
	.byte		N12   , En1 , v060
	.byte	W12
	.byte		N11   , Cn1 , v112
	.byte	W12
	.byte		N11   
	.byte	W12
	.byte		N11   
	.byte	W24
	.byte		N11   
	.byte	W12
	.byte	PEND
@ 002   ----------------------------------------
mus_casino_plus_gacha_5_002:
	.byte	W12
	.byte		N11   , Cn1 , v112
	.byte	W12
	.byte		N11   
	.byte	W12
	.byte		N12   , En1 , v060
	.byte	W24
	.byte		N12   
	.byte	W12
	.byte		N11   , Cn1 , v112
	.byte	W12
	.byte		N11   
	.byte	W12
	.byte	PEND
@ 003   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_gacha_5_001
@ 004   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_gacha_5_002
@ 005   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_gacha_5_001
@ 006   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_gacha_5_002
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_gacha_5_001
@ 008   ----------------------------------------
	.byte	W12
	.byte		N11   , Cn1 , v112
	.byte	W12
	.byte		N11   
	.byte	W12
	.byte		N12   , En1 , v060
	.byte	W24
	.byte		N12   
	.byte	W12
	.byte		N11   , Cn1 , v112
	.byte	W12
	.byte		N11   
	.byte	W11
	.byte	GOTO
	 .word	mus_casino_plus_gacha_5_B1
mus_casino_plus_gacha_5_B2:
	.byte	FINE

@******************************************************@
	.align	2

mus_casino_plus_gacha:
	.byte	5	@ NumTrks
	.byte	0	@ NumBlks
	.byte	mus_casino_plus_gacha_pri	@ Priority
	.byte	mus_casino_plus_gacha_rev	@ Reverb.

	.word	mus_casino_plus_gacha_grp

	.word	mus_casino_plus_gacha_1
	.word	mus_casino_plus_gacha_2
	.word	mus_casino_plus_gacha_3
	.word	mus_casino_plus_gacha_4
	.word	mus_casino_plus_gacha_5

	.end
