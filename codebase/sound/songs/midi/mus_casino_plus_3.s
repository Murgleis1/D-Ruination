	.include "MPlayDef.s"

	.equ	mus_casino_plus_3_grp, voicegroup132
	.equ	mus_casino_plus_3_pri, 0
	.equ	mus_casino_plus_3_rev, reverb_set+50
	.equ	mus_casino_plus_3_mvl, 90
	.equ	mus_casino_plus_3_key, 0
	.equ	mus_casino_plus_3_tbs, 1
	.equ	mus_casino_plus_3_exg, 1
	.equ	mus_casino_plus_3_cmp, 1

	.section .rodata
	.global	mus_casino_plus_3
	.align	2

@**************** Track 1 (Midi-Chn.1) ****************@

mus_casino_plus_3_1:
	.byte	KEYSH , mus_casino_plus_3_key+0
@ 000   ----------------------------------------
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte		VOICE , 1
	.byte		VOL   , 127*mus_casino_plus_3_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		N11   , En4 , v124
	.byte		N11   , Cn5 , v127
	.byte	W54
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 180*mus_casino_plus_3_tbs/2
	.byte	W06
mus_casino_plus_3_1_B1:
@ 001   ----------------------------------------
	.byte	TEMPO , 184*mus_casino_plus_3_tbs/2
	.byte		VOICE , 1
	.byte		N05   , Cn3 , v127
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		N06   , Bn3 
	.byte	W05
	.byte		N18   , Cn4 , v124
	.byte	W19
	.byte		N44   , Fn3 , v127, gtp3
	.byte	W06
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 180*mus_casino_plus_3_tbs/2
	.byte	W06
@ 002   ----------------------------------------
	.byte	TEMPO , 184*mus_casino_plus_3_tbs/2
	.byte		N05   , Gs3 
	.byte	W12
	.byte		N04   , Fn3 
	.byte	W12
	.byte		        Bn3 
	.byte	W12
	.byte		N11   , Cn4 
	.byte	W18
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte		N13   , Ds3 
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte		N06   , Dn3 , v124
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte		N17   , Cn3 , v127
	.byte	W06
	.byte	TEMPO , 180*mus_casino_plus_3_tbs/2
	.byte	W06
@ 003   ----------------------------------------
mus_casino_plus_3_1_003:
	.byte	TEMPO , 184*mus_casino_plus_3_tbs/2
	.byte	W12
	.byte		N04   , Cn3 , v127
	.byte	W12
	.byte		N06   , Bn3 
	.byte	W05
	.byte		N18   , Cn4 , v124
	.byte	W19
	.byte		N44   , Fn3 , v127, gtp3
	.byte	W06
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 180*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	PEND
@ 004   ----------------------------------------
mus_casino_plus_3_1_004:
	.byte	TEMPO , 184*mus_casino_plus_3_tbs/2
	.byte		N05   , Gs3 , v127
	.byte	W12
	.byte		N04   , Fn3 
	.byte	W12
	.byte		        Bn3 
	.byte	W12
	.byte		N11   , Cn4 
	.byte	W24
	.byte		N13   , Ds4 
	.byte	W12
	.byte		N06   , Dn4 , v124
	.byte	W12
	.byte		N11   , Cn4 , v127
	.byte	W12
	.byte	PEND
@ 005   ----------------------------------------
mus_casino_plus_3_1_005:
	.byte		N05   , Fn3 , v127
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		N06   , Gn4 
	.byte	W05
	.byte		N18   , Gs4 , v124
	.byte	W19
	.byte		N44   , Fn4 , v127, gtp3
	.byte	W06
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 180*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	PEND
@ 006   ----------------------------------------
mus_casino_plus_3_1_006:
	.byte	TEMPO , 184*mus_casino_plus_3_tbs/2
	.byte		N05   , Gs4 , v127
	.byte	W12
	.byte		N04   , Fn4 
	.byte	W12
	.byte		        Bn4 
	.byte	W12
	.byte		N11   , Cn5 
	.byte	W18
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte		N13   , Ds4 
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte		N06   , Dn4 , v124
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte		N11   , Cn4 , v127
	.byte	W06
	.byte	TEMPO , 180*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	PEND
@ 007   ----------------------------------------
mus_casino_plus_3_1_007:
	.byte	TEMPO , 184*mus_casino_plus_3_tbs/2
	.byte		N05   , Fn3 , v127
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		N06   , Gn4 
	.byte	W05
	.byte		N18   , Gs4 , v124
	.byte	W19
	.byte		N44   , Fn4 , v127, gtp3
	.byte	W06
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 180*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	PEND
@ 008   ----------------------------------------
	.byte	TEMPO , 184*mus_casino_plus_3_tbs/2
	.byte		N05   , Dn4 
	.byte	W12
	.byte		N04   , Gs4 
	.byte	W12
	.byte		        Dn4 
	.byte	W12
	.byte		        Gn4 
	.byte	W12
	.byte		        Dn4 
	.byte	W12
	.byte		        Fs4 
	.byte	W12
	.byte		        As3 
	.byte	W12
	.byte		        Bn3 
	.byte	W12
@ 009   ----------------------------------------
	.byte		N05   , Cn3 
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		N06   , Bn3 
	.byte	W05
	.byte		N18   , Cn4 , v124
	.byte	W19
	.byte		N44   , Fn3 , v127, gtp3
	.byte	W48
@ 010   ----------------------------------------
	.byte		N05   , Gs3 
	.byte	W12
	.byte		N04   , Fn3 
	.byte	W12
	.byte		        Bn3 
	.byte	W12
	.byte		N11   , Cn4 
	.byte	W18
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte		N13   , Ds3 
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte		N06   , Dn3 , v124
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte		N17   , Cn3 , v127
	.byte	W06
	.byte	TEMPO , 180*mus_casino_plus_3_tbs/2
	.byte	W06
@ 011   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_1_003
@ 012   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_1_004
@ 013   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_1_005
@ 014   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_1_006
@ 015   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_1_007
@ 016   ----------------------------------------
	.byte		N05   , Gs3 , v127
	.byte		N05   , Dn4 
	.byte	W12
	.byte		N04   , Gs4 , v120
	.byte		N04   , Dn5 , v127
	.byte	W12
	.byte		        Gs4 , v120
	.byte		N04   , Dn5 , v127
	.byte	W12
	.byte		        Gs3 , v120
	.byte		N04   , Dn4 , v127
	.byte	W12
	.byte		        Gs4 , v124
	.byte		N04   , Dn5 , v127
	.byte	W12
	.byte		        Gs4 , v120
	.byte		N04   , Dn5 , v127
	.byte	W12
	.byte		        Gs3 , v120
	.byte		N04   , Dn4 , v127
	.byte	W12
	.byte		        Gs4 , v120
	.byte		N04   , Dn5 , v127
	.byte	W12
@ 017   ----------------------------------------
	.byte	TEMPO , 184*mus_casino_plus_3_tbs/2
	.byte	W96
@ 018   ----------------------------------------
	.byte	W54
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte	W06
	.byte	TEMPO , 180*mus_casino_plus_3_tbs/2
	.byte	W06
@ 019   ----------------------------------------
	.byte	TEMPO , 184*mus_casino_plus_3_tbs/2
	.byte	W92
	.byte	W03
	.byte		VOICE , 2
	.byte	W01
@ 020   ----------------------------------------
	.byte	W48
	.byte		N06   , Gs4 , v048
	.byte	W06
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte		        Gn4 
	.byte	W06
	.byte	TEMPO , 183*mus_casino_plus_3_tbs/2
	.byte		        Gs4 
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte		        Gn4 
	.byte	W06
	.byte	TEMPO , 182*mus_casino_plus_3_tbs/2
	.byte		        Gs4 
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte		        Gn4 
	.byte	W06
	.byte	TEMPO , 181*mus_casino_plus_3_tbs/2
	.byte		        Gs4 
	.byte	W06
	.byte	TEMPO , 180*mus_casino_plus_3_tbs/2
	.byte		        Gn4 
	.byte	W06
@ 021   ----------------------------------------
	.byte	W96
@ 022   ----------------------------------------
	.byte	W96
@ 023   ----------------------------------------
	.byte	W96
@ 024   ----------------------------------------
	.byte	W48
	.byte		        Dn5 
	.byte	W06
	.byte		        Cs5 
	.byte	W06
	.byte		        Dn5 
	.byte	W06
	.byte		        Cs5 
	.byte	W06
	.byte		        Dn5 
	.byte	W06
	.byte		        Cs5 
	.byte	W06
	.byte		        Dn5 
	.byte	W06
	.byte		        Cs5 
	.byte	W05
	.byte		VOICE , 56
	.byte	W01
@ 025   ----------------------------------------
mus_casino_plus_3_1_025:
	.byte		N05   , Cn3 , v080
	.byte	W12
	.byte		N04   , Cn3 , v076
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Cn3 , v080
	.byte	W12
	.byte		        Cn3 , v076
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		N24   , Cn3 
	.byte	W12
	.byte	PEND
@ 026   ----------------------------------------
mus_casino_plus_3_1_026:
	.byte	W12
	.byte		N04   , Cn3 , v076
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Cn3 , v080
	.byte	W12
	.byte		        Cn3 , v076
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		        Cn3 
	.byte	W12
	.byte	PEND
@ 027   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_1_025
@ 028   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_1_026
@ 029   ----------------------------------------
mus_casino_plus_3_1_029:
	.byte		N05   , Fn3 , v080
	.byte	W12
	.byte		N04   , Fn3 , v076
	.byte	W12
	.byte		        Gn3 
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Fn3 , v080
	.byte	W12
	.byte		        Fn3 , v076
	.byte	W12
	.byte		        Gn3 
	.byte	W12
	.byte		N24   , Fn3 
	.byte	W12
	.byte	PEND
@ 030   ----------------------------------------
mus_casino_plus_3_1_030:
	.byte	W12
	.byte		N04   , Fn3 , v076
	.byte	W12
	.byte		        Gn3 
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Fn3 , v080
	.byte	W12
	.byte		        Fn3 , v076
	.byte	W12
	.byte		        Gn3 
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte	PEND
@ 031   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_1_029
@ 032   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_1_030
	.byte	GOTO
	 .word	mus_casino_plus_3_1_B1
mus_casino_plus_3_1_B2:
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 2 (Midi-Chn.2) ****************@

mus_casino_plus_3_2:
	.byte	KEYSH , mus_casino_plus_3_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 17
	.byte		VOL   , 88*mus_casino_plus_3_mvl/mxv
	.byte	W96
mus_casino_plus_3_2_B1:
@ 001   ----------------------------------------
	.byte		VOICE , 17
	.byte		N06   , Fn3 , v068
	.byte	W11
	.byte		N18   , Gn3 
	.byte	W24
	.byte	W01
	.byte		N05   , Cn4 , v080
	.byte	W12
	.byte		N06   , Ds4 
	.byte	W12
	.byte		N24   , Cn4 
	.byte	W24
	.byte		N06   
	.byte	W12
@ 002   ----------------------------------------
mus_casino_plus_3_2_002:
	.byte		N06   , Fn3 , v080
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		        Gn3 
	.byte	W11
	.byte		N24   , Gs3 
	.byte	W24
	.byte	W01
	.byte		        Fn3 
	.byte	W24
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 003   ----------------------------------------
mus_casino_plus_3_2_003:
	.byte		N06   , Fn3 , v068
	.byte	W11
	.byte		N18   , Gn3 
	.byte	W24
	.byte	W01
	.byte		N05   , Cn4 , v080
	.byte	W12
	.byte		N06   , Ds4 
	.byte	W12
	.byte		N24   , Cn4 
	.byte	W24
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 004   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_2_002
@ 005   ----------------------------------------
mus_casino_plus_3_2_005:
	.byte		N06   , As3 , v068
	.byte	W11
	.byte		N18   , Cn4 
	.byte	W24
	.byte	W01
	.byte		N05   , Fn4 , v080
	.byte	W12
	.byte		N06   , Gs4 
	.byte	W12
	.byte		N24   , Fn4 
	.byte	W24
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 006   ----------------------------------------
mus_casino_plus_3_2_006:
	.byte		N06   , As3 , v080
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		        Cn4 
	.byte	W11
	.byte		N24   , Ds4 
	.byte	W24
	.byte	W01
	.byte		        As3 
	.byte	W24
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_2_005
@ 008   ----------------------------------------
	.byte		N06   , Ds5 , v048
	.byte	W06
	.byte		        Dn5 
	.byte	W06
	.byte		        Ds5 
	.byte	W06
	.byte		        Dn5 
	.byte	W06
	.byte		        Ds5 
	.byte	W06
	.byte		        Dn5 
	.byte	W06
	.byte		        Cs5 
	.byte	W06
	.byte		        Cn5 
	.byte	W06
	.byte		        An4 
	.byte	W06
	.byte		        Gs4 
	.byte	W06
	.byte		        An4 
	.byte	W06
	.byte		        Gs4 
	.byte	W06
	.byte		        Gn4 
	.byte	W06
	.byte		        Fs4 
	.byte	W06
	.byte		        Fn4 
	.byte	W06
	.byte		        Ds4 
	.byte	W06
@ 009   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_2_003
@ 010   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_2_002
@ 011   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_2_003
@ 012   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_2_002
@ 013   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_2_005
@ 014   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_2_006
@ 015   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_2_005
@ 016   ----------------------------------------
	.byte		N05   , Dn4 , v080
	.byte	W12
	.byte		N04   , Gs4 , v076
	.byte	W12
	.byte		        Dn4 
	.byte	W12
	.byte		        Gn4 
	.byte	W12
	.byte		        Dn4 , v080
	.byte	W12
	.byte		        Fs4 , v076
	.byte	W12
	.byte		        As3 
	.byte	W12
	.byte		        Bn3 
	.byte	W12
@ 017   ----------------------------------------
mus_casino_plus_3_2_017:
	.byte		N05   , Fn2 , v064
	.byte	W12
	.byte		N04   , Fn2 , v068
	.byte	W12
	.byte		        Cn3 
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Fn2 , v072
	.byte	W12
	.byte		        Fn2 , v068
	.byte	W12
	.byte		        Cn3 
	.byte	W12
	.byte		N24   , Ds3 
	.byte	W12
	.byte	PEND
@ 018   ----------------------------------------
mus_casino_plus_3_2_018:
	.byte	W12
	.byte		N04   , Ds3 , v068
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Cn3 , v072
	.byte	W12
	.byte		        Cn3 , v068
	.byte	W12
	.byte		        Bn2 
	.byte	W12
	.byte		        Cn3 , v056
	.byte	W12
	.byte	PEND
@ 019   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_2_017
@ 020   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_2_018
@ 021   ----------------------------------------
mus_casino_plus_3_2_021:
	.byte		N05   , As2 , v064
	.byte	W12
	.byte		N04   , As2 , v068
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        As2 , v072
	.byte	W12
	.byte		        As2 , v068
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte		N24   , Gs3 
	.byte	W12
	.byte	PEND
@ 022   ----------------------------------------
mus_casino_plus_3_2_022:
	.byte	W12
	.byte		N04   , Gs3 , v068
	.byte	W12
	.byte		        Gn3 
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Fn3 , v072
	.byte	W12
	.byte		        Fn3 , v068
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte	PEND
@ 023   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_2_021
@ 024   ----------------------------------------
	.byte	W12
	.byte		N04   , Gs3 , v068
	.byte	W12
	.byte		        Gn3 
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Fn3 , v072
	.byte	W12
	.byte		        Fn3 , v068
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Fn3 
	.byte	W11
	.byte		VOICE , 81
	.byte	W01
@ 025   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_2_017
@ 026   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_2_018
@ 027   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_2_017
@ 028   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_2_018
@ 029   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_2_021
@ 030   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_2_022
@ 031   ----------------------------------------
	.byte		N05   , As2 , v064
	.byte	W12
	.byte		N04   , As2 , v068
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        As2 , v072
	.byte	W12
	.byte		        As2 , v068
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte		N11   , Gs3 
	.byte	W12
@ 032   ----------------------------------------
	.byte		N05   , Dn4 , v080
	.byte	W12
	.byte		N04   , Gs4 , v076
	.byte	W12
	.byte		        Dn4 
	.byte	W12
	.byte		        Gn4 
	.byte	W12
	.byte		        Cs4 , v080
	.byte	W12
	.byte		        Fs4 , v076
	.byte	W12
	.byte		        Cn4 
	.byte	W12
	.byte		        Fn4 
	.byte	W12
	.byte	GOTO
	 .word	mus_casino_plus_3_2_B1
mus_casino_plus_3_2_B2:
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 3 (Midi-Chn.3) ****************@

mus_casino_plus_3_3:
	.byte	KEYSH , mus_casino_plus_3_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 82
	.byte		VOL   , 47*mus_casino_plus_3_mvl/mxv
	.byte	W96
mus_casino_plus_3_3_B1:
@ 001   ----------------------------------------
	.byte	W96
@ 002   ----------------------------------------
	.byte	W96
@ 003   ----------------------------------------
	.byte	W96
@ 004   ----------------------------------------
	.byte		N05   , Ds4 , v080
	.byte	W12
	.byte		N04   , Gs4 , v076
	.byte	W12
	.byte		        Dn4 
	.byte	W12
	.byte		        Gn4 
	.byte	W12
	.byte		        As3 , v080
	.byte	W12
	.byte		        Gs4 , v076
	.byte	W12
	.byte		        Dn4 , v080
	.byte	W12
	.byte		        Gs4 
	.byte	W12
@ 005   ----------------------------------------
	.byte	W96
@ 006   ----------------------------------------
	.byte	W96
@ 007   ----------------------------------------
	.byte	W84
	.byte		N03   , Cn3 , v072
	.byte	W03
	.byte		        Dn3 
	.byte	W03
	.byte		        Cn4 
	.byte	W03
	.byte		        Dn4 
	.byte	W03
@ 008   ----------------------------------------
	.byte	W01
	.byte		N05   , Cn2 , v076
	.byte	W12
	.byte		N04   , Cn2 , v072
	.byte	W12
	.byte		        Dn2 
	.byte	W12
	.byte		N04   
	.byte	W11
	.byte		N05   , Cn2 , v076
	.byte	W13
	.byte		N04   , Cn2 , v072
	.byte	W12
	.byte		        Dn2 
	.byte	W12
	.byte		N04   
	.byte	W11
@ 009   ----------------------------------------
	.byte	W96
@ 010   ----------------------------------------
	.byte	W96
@ 011   ----------------------------------------
	.byte	W96
@ 012   ----------------------------------------
	.byte	W96
@ 013   ----------------------------------------
	.byte	W96
@ 014   ----------------------------------------
	.byte	W96
@ 015   ----------------------------------------
	.byte	W96
@ 016   ----------------------------------------
	.byte	W96
@ 017   ----------------------------------------
mus_casino_plus_3_3_017:
	.byte	W01
	.byte		N05   , Cn3 , v100
	.byte	W12
	.byte		N04   , Cn3 , v096
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		N04   
	.byte	W11
	.byte		N05   , Cn3 , v100
	.byte	W13
	.byte		N04   , Cn3 , v096
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		N04   
	.byte	W11
	.byte	PEND
@ 018   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_3_017
@ 019   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_3_017
@ 020   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_3_017
@ 021   ----------------------------------------
mus_casino_plus_3_3_021:
	.byte	W01
	.byte		N05   , Fn3 , v100
	.byte	W12
	.byte		N04   , Fn3 , v096
	.byte	W12
	.byte		        Gn3 
	.byte	W12
	.byte		N04   
	.byte	W11
	.byte		N05   , Fn3 , v100
	.byte	W13
	.byte		N04   , Fn3 , v096
	.byte	W12
	.byte		        Gn3 
	.byte	W12
	.byte		N04   
	.byte	W11
	.byte	PEND
@ 022   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_3_021
@ 023   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_3_017
@ 024   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_3_017
@ 025   ----------------------------------------
	.byte	W96
@ 026   ----------------------------------------
	.byte	W96
@ 027   ----------------------------------------
	.byte	W96
@ 028   ----------------------------------------
	.byte	W96
@ 029   ----------------------------------------
	.byte	W96
@ 030   ----------------------------------------
	.byte	W96
@ 031   ----------------------------------------
	.byte	W96
@ 032   ----------------------------------------
	.byte	W96
	.byte	GOTO
	 .word	mus_casino_plus_3_3_B1
mus_casino_plus_3_3_B2:
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 4 (Midi-Chn.4) ****************@

mus_casino_plus_3_4:
	.byte	KEYSH , mus_casino_plus_3_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 36
	.byte		VOL   , 125*mus_casino_plus_3_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		N11   , En2 , v088
	.byte	W12
	.byte		N04   , Gn1 , v072
	.byte	W12
	.byte		        Gs1 
	.byte	W12
	.byte		        Gn1 
	.byte	W12
	.byte		        As1 , v076
	.byte	W12
	.byte		        Gn1 , v072
	.byte	W12
	.byte		        Bn1 
	.byte	W12
	.byte		        Gn1 
	.byte	W12
mus_casino_plus_3_4_B1:
@ 001   ----------------------------------------
	.byte		N05   , Cn1 , v076
	.byte	W12
	.byte		N04   , Cn1 , v072
	.byte	W12
	.byte		        Dn1 
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Cn1 , v076
	.byte	W12
	.byte		        Cn1 , v072
	.byte	W12
	.byte		        Dn1 
	.byte	W12
	.byte		N24   , Ds1 
	.byte	W12
@ 002   ----------------------------------------
mus_casino_plus_3_4_002:
	.byte	W12
	.byte		N04   , Ds1 , v068
	.byte	W12
	.byte		        Dn1 
	.byte	W12
	.byte		        Dn1 , v064
	.byte	W12
	.byte		        Cn1 , v068
	.byte	W12
	.byte		        Cn1 , v064
	.byte	W12
	.byte		        Dn1 , v072
	.byte	W12
	.byte		        Cn1 , v064
	.byte	W12
	.byte	PEND
@ 003   ----------------------------------------
mus_casino_plus_3_4_003:
	.byte		N05   , Fn1 , v072
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Dn1 
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Cn1 , v076
	.byte	W12
	.byte		        Cn1 , v072
	.byte	W12
	.byte		        Dn1 
	.byte	W12
	.byte		N24   , Ds1 
	.byte	W12
	.byte	PEND
@ 004   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_4_002
@ 005   ----------------------------------------
mus_casino_plus_3_4_005:
	.byte		N05   , Fn1 , v072
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Gn1 
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Fn1 , v076
	.byte	W12
	.byte		        Fn1 , v072
	.byte	W12
	.byte		        Gn1 
	.byte	W12
	.byte		N24   , Gs1 
	.byte	W12
	.byte	PEND
@ 006   ----------------------------------------
mus_casino_plus_3_4_006:
	.byte	W12
	.byte		N04   , Gs1 , v068
	.byte	W12
	.byte		        Gn1 
	.byte	W12
	.byte		        Gn1 , v064
	.byte	W12
	.byte		        Fn1 , v068
	.byte	W12
	.byte		        Fn1 , v064
	.byte	W12
	.byte		        Gn1 , v072
	.byte	W12
	.byte		        Fn1 , v064
	.byte	W12
	.byte	PEND
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_4_005
@ 008   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_4_006
@ 009   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_4_003
@ 010   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_4_002
@ 011   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_4_003
@ 012   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_4_002
@ 013   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_4_005
@ 014   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_4_006
@ 015   ----------------------------------------
	.byte		N05   , Fn1 , v072
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Gn1 
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Fn1 , v076
	.byte	W12
	.byte		        Fn1 , v072
	.byte	W12
	.byte		        Gn1 
	.byte	W12
	.byte		N11   , Gs1 
	.byte	W12
@ 016   ----------------------------------------
	.byte		N05   , Dn1 
	.byte	W12
	.byte		N04   , Gs1 , v064
	.byte	W24
	.byte		        Dn1 
	.byte	W12
	.byte		        Gs1 , v068
	.byte	W24
	.byte		        Dn1 
	.byte	W12
	.byte		        Gs1 , v064
	.byte	W12
@ 017   ----------------------------------------
mus_casino_plus_3_4_017:
	.byte		N05   , Fn0 , v072
	.byte	W12
	.byte		N04   , Fn0 , v064
	.byte	W12
	.byte		        Cn1 , v068
	.byte	W12
	.byte		        Cn1 , v064
	.byte	W12
	.byte		        Fn0 , v068
	.byte	W12
	.byte		        Fn0 , v064
	.byte	W12
	.byte		        Cn1 , v068
	.byte	W12
	.byte		N24   , Ds1 , v064
	.byte	W12
	.byte	PEND
@ 018   ----------------------------------------
mus_casino_plus_3_4_018:
	.byte	W12
	.byte		N04   , Ds1 , v064
	.byte	W12
	.byte		        Dn1 , v068
	.byte	W12
	.byte		        Dn1 , v064
	.byte	W12
	.byte		        Cn1 , v068
	.byte	W12
	.byte		        Cn1 , v064
	.byte	W12
	.byte		        Bn0 , v068
	.byte	W12
	.byte		        Cn1 , v064
	.byte	W12
	.byte	PEND
@ 019   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_4_017
@ 020   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_4_018
@ 021   ----------------------------------------
mus_casino_plus_3_4_021:
	.byte		N05   , As0 , v072
	.byte	W12
	.byte		N04   , As0 , v064
	.byte	W12
	.byte		        Fn1 , v068
	.byte	W12
	.byte		        Fn1 , v064
	.byte	W12
	.byte		        As0 , v068
	.byte	W12
	.byte		        As0 , v064
	.byte	W12
	.byte		        Fn1 , v068
	.byte	W12
	.byte		N24   , Gs1 , v064
	.byte	W12
	.byte	PEND
@ 022   ----------------------------------------
mus_casino_plus_3_4_022:
	.byte	W12
	.byte		N04   , Gs1 , v064
	.byte	W12
	.byte		        Gn1 , v068
	.byte	W12
	.byte		        Gn1 , v064
	.byte	W12
	.byte		        Fn1 , v068
	.byte	W12
	.byte		        Fn1 , v064
	.byte	W12
	.byte		        En1 , v068
	.byte	W12
	.byte		        Fn1 , v064
	.byte	W12
	.byte	PEND
@ 023   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_4_021
@ 024   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_4_022
@ 025   ----------------------------------------
mus_casino_plus_3_4_025:
	.byte		N05   , Fn1 , v072
	.byte	W12
	.byte		N04   , Fn1 , v064
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Fn1 , v068
	.byte	W12
	.byte		        Fn1 , v064
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		N24   
	.byte	W12
	.byte	PEND
@ 026   ----------------------------------------
mus_casino_plus_3_4_026:
	.byte	W12
	.byte		N04   , Fn1 , v064
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Fn1 , v068
	.byte	W12
	.byte		        Fn1 , v064
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Fn1 , v072
	.byte	W12
	.byte	PEND
@ 027   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_4_025
@ 028   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_4_026
@ 029   ----------------------------------------
mus_casino_plus_3_4_029:
	.byte		N05   , As1 , v076
	.byte	W12
	.byte		N04   , As1 , v064
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        As1 , v068
	.byte	W12
	.byte		        As1 , v064
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		N24   
	.byte	W12
	.byte	PEND
@ 030   ----------------------------------------
mus_casino_plus_3_4_030:
	.byte	W12
	.byte		N04   , As1 , v064
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        As1 , v068
	.byte	W12
	.byte		        As1 , v064
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte	PEND
@ 031   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_4_029
@ 032   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_4_030
	.byte	GOTO
	 .word	mus_casino_plus_3_4_B1
mus_casino_plus_3_4_B2:
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 5 (Midi-Chn.5) ****************@

mus_casino_plus_3_5:
	.byte	KEYSH , mus_casino_plus_3_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 1
	.byte		VOL   , 95*mus_casino_plus_3_mvl/mxv
	.byte	W12
	.byte		N04   , Cn1 , v056
	.byte	W12
	.byte		        Cs1 
	.byte	W12
	.byte		        Cn1 
	.byte	W12
	.byte		        Ds1 , v060
	.byte	W12
	.byte		        Cn1 , v056
	.byte	W12
	.byte		        En1 
	.byte	W12
	.byte		        Cn1 
	.byte	W12
mus_casino_plus_3_5_B1:
@ 001   ----------------------------------------
	.byte		VOICE , 81
	.byte		N05   , Fn3 , v064
	.byte	W12
	.byte		N04   , Fn3 , v056
	.byte	W12
	.byte		        Cn4 , v060
	.byte	W12
	.byte		        Cn4 , v056
	.byte	W12
	.byte		        Fn3 , v060
	.byte	W12
	.byte		        Fn3 , v056
	.byte	W12
	.byte		        Cn4 , v060
	.byte	W12
	.byte		N24   , Cn4 , v056
	.byte	W12
@ 002   ----------------------------------------
mus_casino_plus_3_5_002:
	.byte	W12
	.byte		N04   , Cn4 , v056
	.byte	W60
	.byte		        Bn3 , v060
	.byte	W24
	.byte	PEND
@ 003   ----------------------------------------
mus_casino_plus_3_5_003:
	.byte		N05   , Fn3 , v064
	.byte	W12
	.byte		N04   , Fn3 , v056
	.byte	W12
	.byte		        Cn4 , v060
	.byte	W12
	.byte		        Cn4 , v056
	.byte	W12
	.byte		        Fn3 , v060
	.byte	W12
	.byte		        Fn3 , v056
	.byte	W12
	.byte		        Cn4 , v060
	.byte	W12
	.byte		N24   , Cn4 , v056
	.byte	W12
	.byte	PEND
@ 004   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_5_002
@ 005   ----------------------------------------
mus_casino_plus_3_5_005:
	.byte		N05   , As3 , v064
	.byte	W12
	.byte		N04   , As3 , v056
	.byte	W12
	.byte		        Fn4 , v060
	.byte	W12
	.byte		        Fn4 , v056
	.byte	W12
	.byte		        As3 , v060
	.byte	W12
	.byte		        As3 , v056
	.byte	W12
	.byte		        Fn4 , v060
	.byte	W12
	.byte		N24   , Fn4 , v056
	.byte	W12
	.byte	PEND
@ 006   ----------------------------------------
mus_casino_plus_3_5_006:
	.byte	W12
	.byte		N04   , Fn4 , v056
	.byte	W60
	.byte		        En4 , v060
	.byte	W24
	.byte	PEND
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_5_005
@ 008   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_5_006
@ 009   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_5_003
@ 010   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_5_002
@ 011   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_5_003
@ 012   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_5_002
@ 013   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_5_005
@ 014   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_5_006
@ 015   ----------------------------------------
	.byte		N05   , As3 , v064
	.byte	W12
	.byte		N04   , As3 , v056
	.byte	W12
	.byte		        Fn4 , v060
	.byte	W12
	.byte		        Fn4 , v056
	.byte	W12
	.byte		        As3 , v060
	.byte	W12
	.byte		        As3 , v056
	.byte	W12
	.byte		        Fn4 , v060
	.byte	W12
	.byte		N11   , Fn4 , v056
	.byte	W12
@ 016   ----------------------------------------
	.byte	W96
@ 017   ----------------------------------------
	.byte	W96
@ 018   ----------------------------------------
	.byte	W96
@ 019   ----------------------------------------
	.byte	W96
@ 020   ----------------------------------------
	.byte	W96
@ 021   ----------------------------------------
	.byte	W96
@ 022   ----------------------------------------
	.byte	W96
@ 023   ----------------------------------------
	.byte	W96
@ 024   ----------------------------------------
	.byte	W92
	.byte	W03
	.byte		VOICE , 17
	.byte	W01
@ 025   ----------------------------------------
mus_casino_plus_3_5_025:
	.byte		N05   , Fn3 , v108
	.byte	W12
	.byte		N04   , Fn3 , v120
	.byte	W12
	.byte		        Cn4 
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Fn3 , v124
	.byte	W12
	.byte		        Fn3 , v120
	.byte	W12
	.byte		        Cn4 
	.byte	W12
	.byte		N24   , Ds4 
	.byte	W12
	.byte	PEND
@ 026   ----------------------------------------
mus_casino_plus_3_5_026:
	.byte	W12
	.byte		N04   , Ds4 , v120
	.byte	W12
	.byte		        Dn4 
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Cn4 , v124
	.byte	W12
	.byte		        Cn4 , v120
	.byte	W12
	.byte		        Bn3 
	.byte	W12
	.byte		        Cn4 , v100
	.byte	W12
	.byte	PEND
@ 027   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_5_025
@ 028   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_5_026
@ 029   ----------------------------------------
mus_casino_plus_3_5_029:
	.byte		N05   , As3 , v108
	.byte	W12
	.byte		N04   , As3 , v120
	.byte	W12
	.byte		        Fn4 
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        As3 , v124
	.byte	W12
	.byte		        As3 , v120
	.byte	W12
	.byte		        Fn4 
	.byte	W12
	.byte		N24   , Gs4 
	.byte	W12
	.byte	PEND
@ 030   ----------------------------------------
mus_casino_plus_3_5_030:
	.byte	W12
	.byte		N04   , Gs4 , v120
	.byte	W12
	.byte		        Gn4 
	.byte	W12
	.byte		N04   
	.byte	W12
	.byte		        Fn4 , v124
	.byte	W12
	.byte		        Fn4 , v120
	.byte	W12
	.byte		        En4 
	.byte	W12
	.byte		        Fn4 
	.byte	W12
	.byte	PEND
@ 031   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_5_029
@ 032   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_5_030
	.byte	GOTO
	 .word	mus_casino_plus_3_5_B1
mus_casino_plus_3_5_B2:
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 6 (Midi-Chn.10) ****************@

mus_casino_plus_3_6:
	.byte	KEYSH , mus_casino_plus_3_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 0
	.byte		VOL   , 112*mus_casino_plus_3_mvl/mxv
	.byte		        112*mus_casino_plus_3_mvl/mxv
	.byte		N06   , Cn1 , v076
	.byte		N24   , An2 , v068
	.byte	W06
	.byte		N06   , Cn1 , v076
	.byte	W06
	.byte		N06   
	.byte	W12
	.byte		N09   , En1 , v080
	.byte	W12
	.byte		N06   
	.byte		N24   , An2 , v068
	.byte	W24
	.byte		N06   , Cn1 , v076
	.byte	W12
	.byte		N09   , En1 , v080
	.byte		N24   , An2 , v068
	.byte	W12
	.byte		N09   , En1 , v080
	.byte	W12
mus_casino_plus_3_6_B1:
@ 001   ----------------------------------------
mus_casino_plus_3_6_001:
	.byte		N06   , Cn1 , v076
	.byte		N24   , An2 , v068
	.byte	W24
	.byte		N09   , En1 , v080
	.byte	W12
	.byte		N06   
	.byte	W24
	.byte		        Cn1 , v076
	.byte	W12
	.byte		N09   , En1 , v080
	.byte	W12
	.byte		N06   , Cn1 , v076
	.byte	W12
	.byte	PEND
@ 002   ----------------------------------------
mus_casino_plus_3_6_002:
	.byte		N06   , Cn1 , v076
	.byte	W24
	.byte		N09   , En1 , v080
	.byte	W12
	.byte		N06   
	.byte	W24
	.byte		        Cn1 , v076
	.byte	W12
	.byte		N09   , En1 , v080
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 003   ----------------------------------------
mus_casino_plus_3_6_003:
	.byte		N06   , Cn1 , v076
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		N09   , En1 , v080
	.byte	W12
	.byte		N06   
	.byte	W24
	.byte		        Cn1 , v076
	.byte	W12
	.byte		N09   , En1 , v080
	.byte	W12
	.byte		N06   , Cn1 , v076
	.byte	W12
	.byte	PEND
@ 004   ----------------------------------------
mus_casino_plus_3_6_004:
	.byte		N06   , Cn1 , v076
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		N09   , En1 , v080
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		N09   
	.byte	W12
	.byte		N06   , Cn1 , v076
	.byte	W12
	.byte		N09   , En1 , v080
	.byte	W12
	.byte		N09   
	.byte	W12
	.byte	PEND
@ 005   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_001
@ 006   ----------------------------------------
	.byte		N06   , Cn1 , v076
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		N09   , En1 , v080
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		        Cn1 , v076
	.byte	W12
	.byte		N09   , En1 , v080
	.byte	W12
	.byte		N09   
	.byte	W12
	.byte		N06   , Cn1 , v076
	.byte	W12
@ 007   ----------------------------------------
mus_casino_plus_3_6_007:
	.byte		N06   , Cn1 , v076
	.byte	W24
	.byte		N09   , En1 , v080
	.byte	W12
	.byte		N06   
	.byte	W24
	.byte		        Cn1 , v076
	.byte	W12
	.byte		N09   , En1 , v080
	.byte	W12
	.byte		N06   , Cn1 , v076
	.byte	W12
	.byte	PEND
@ 008   ----------------------------------------
mus_casino_plus_3_6_008:
	.byte		N09   , En1 , v080
	.byte		N24   , An2 , v068
	.byte	W12
	.byte		N09   , En1 , v080
	.byte	W12
	.byte		N06   , Cn1 , v076
	.byte	W12
	.byte		N09   , En1 , v080
	.byte		N24   , An2 , v068
	.byte	W12
	.byte		N09   , En1 , v080
	.byte	W12
	.byte		N06   , Cn1 , v076
	.byte	W12
	.byte		N09   , En1 , v080
	.byte		N24   , An2 , v068
	.byte	W06
	.byte		N06   , Cn1 , v076
	.byte	W06
	.byte		N03   , En1 , v080
	.byte	W06
	.byte		N03   
	.byte	W06
	.byte	PEND
@ 009   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_001
@ 010   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_002
@ 011   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_003
@ 012   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_004
@ 013   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_001
@ 014   ----------------------------------------
	.byte		N06   , Cn1 , v076
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		N09   , En1 , v080
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		        Cn1 , v076
	.byte	W12
	.byte		N09   , En1 , v080
	.byte	W12
	.byte		N09   
	.byte	W12
	.byte		N06   
	.byte	W12
@ 015   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_007
@ 016   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_008
@ 017   ----------------------------------------
	.byte		N06   , Cn1 , v076
	.byte		N24   , An2 , v068
	.byte	W24
	.byte		N09   , Ds1 , v080
	.byte	W12
	.byte		N06   
	.byte	W24
	.byte		        Cn1 , v076
	.byte	W12
	.byte		N09   , Ds1 , v080
	.byte	W12
	.byte		N06   , Cn1 , v076
	.byte	W12
@ 018   ----------------------------------------
	.byte		N06   
	.byte	W24
	.byte		N09   , Ds1 , v080
	.byte	W12
	.byte		N06   
	.byte	W24
	.byte		        Cn1 , v076
	.byte	W12
	.byte		N09   , Ds1 , v080
	.byte	W12
	.byte		N06   
	.byte	W12
@ 019   ----------------------------------------
	.byte		        Cn1 , v076
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		N09   , Ds1 , v080
	.byte	W12
	.byte		N06   
	.byte	W24
	.byte		        Cn1 , v076
	.byte	W12
	.byte		N09   , Ds1 , v080
	.byte	W12
	.byte		N06   , Cn1 , v076
	.byte	W12
@ 020   ----------------------------------------
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		N09   , Ds1 , v080
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		N09   
	.byte	W12
	.byte		N06   , Cn1 , v076
	.byte	W12
	.byte		N09   , En1 , v080
	.byte	W12
	.byte		N09   
	.byte	W12
@ 021   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_001
@ 022   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_002
@ 023   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_003
@ 024   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_004
@ 025   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_001
@ 026   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_002
@ 027   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_003
@ 028   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_004
@ 029   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_001
@ 030   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_002
@ 031   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_003
@ 032   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_3_6_004
	.byte	GOTO
	 .word	mus_casino_plus_3_6_B1
mus_casino_plus_3_6_B2:
@ 033   ----------------------------------------
	.byte	FINE

@******************************************************@
	.align	2

mus_casino_plus_3:
	.byte	6	@ NumTrks
	.byte	0	@ NumBlks
	.byte	mus_casino_plus_3_pri	@ Priority
	.byte	mus_casino_plus_3_rev	@ Reverb.

	.word	mus_casino_plus_3_grp

	.word	mus_casino_plus_3_1
	.word	mus_casino_plus_3_2
	.word	mus_casino_plus_3_3
	.word	mus_casino_plus_3_4
	.word	mus_casino_plus_3_5
	.word	mus_casino_plus_3_6

	.end
