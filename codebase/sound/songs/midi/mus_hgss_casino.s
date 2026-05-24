	.include "MPlayDef.s"

	.equ	mus_hgss_casino_grp, voicegroup161
	.equ	mus_hgss_casino_pri, 0
	.equ	mus_hgss_casino_rev, reverb_set+50
	.equ	mus_hgss_casino_mvl, 86
	.equ	mus_hgss_casino_key, 0
	.equ	mus_hgss_casino_tbs, 1
	.equ	mus_hgss_casino_exg, 1
	.equ	mus_hgss_casino_cmp, 1

	.section .rodata
	.global	mus_hgss_casino
	.align	2

@**************** Track 1 (Midi-Chn.1) ****************@

mus_hgss_casino_1:
	.byte	KEYSH , mus_hgss_casino_key+0
@ 000   ----------------------------------------
	.byte	TEMPO , 130*mus_hgss_casino_tbs/2
	.byte		VOICE , 1
	.byte		VOL   , 112*mus_hgss_casino_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		MOD   , 0
	.byte	W96
mus_hgss_casino_1_B1:
@ 001   ----------------------------------------
	.byte	W96
@ 002   ----------------------------------------
	.byte	W96
@ 003   ----------------------------------------
	.byte	W96
@ 004   ----------------------------------------
	.byte	W56
	.byte	W03
	.byte		N05   , As4 , v112
	.byte	W01
	.byte		        Dn5 
	.byte	W17
	.byte		        Gn4 
	.byte	W01
	.byte		        As4 
	.byte	W17
	.byte		        Ds4 
	.byte	W01
@ 005   ----------------------------------------
mus_hgss_casino_1_005:
	.byte		N05   , Gn4 , v112
	.byte	W12
	.byte		        Cn4 
	.byte	W12
	.byte		        Dn4 
	.byte	W12
	.byte		        Ds4 
	.byte	W12
	.byte		        Fn4 
	.byte	W12
	.byte		        Ds4 
	.byte	W12
	.byte		        Fn4 
	.byte	W06
	.byte		        Ds4 
	.byte	W12
	.byte		N17   , Fn4 
	.byte	W06
	.byte	PEND
@ 006   ----------------------------------------
mus_hgss_casino_1_006:
	.byte	W12
	.byte		N23   , Gn4 , v112
	.byte	W24
	.byte		N05   , Fs4 
	.byte	W06
	.byte		        Fn4 
	.byte	W17
	.byte		        As4 
	.byte	W01
	.byte		        Dn5 
	.byte	W17
	.byte		        Gn4 
	.byte	W01
	.byte		        As4 
	.byte	W17
	.byte		        Ds4 
	.byte	W01
	.byte	PEND
@ 007   ----------------------------------------
	.byte		        Gn4 
	.byte	W12
	.byte		        Cn4 
	.byte	W12
	.byte		        Dn4 
	.byte	W12
	.byte		        Ds4 
	.byte	W18
	.byte		        Fn4 
	.byte	W06
	.byte		        Ds4 
	.byte	W12
	.byte		        Gn4 
	.byte	W06
	.byte		        Ds4 
	.byte	W12
	.byte		N17   , As4 
	.byte	W06
@ 008   ----------------------------------------
	.byte	W12
	.byte		N11   , An4 
	.byte	W12
	.byte		N05   , As4 
	.byte	W06
	.byte		        Cn5 
	.byte	W28
	.byte	W01
	.byte		        As4 
	.byte	W01
	.byte		        Dn5 
	.byte	W17
	.byte		        Gn4 
	.byte	W01
	.byte		        As4 
	.byte	W17
	.byte		        Ds4 
	.byte	W01
@ 009   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_1_005
@ 010   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_1_006
@ 011   ----------------------------------------
	.byte		N05   , Gn4 , v112
	.byte	W12
	.byte		        Cn4 
	.byte	W12
	.byte		        Dn4 
	.byte	W12
	.byte		        Ds4 
	.byte	W60
@ 012   ----------------------------------------
	.byte	W96
@ 013   ----------------------------------------
	.byte	W96
@ 014   ----------------------------------------
	.byte	W96
@ 015   ----------------------------------------
	.byte	W96
@ 016   ----------------------------------------
	.byte	W60
	.byte		        As4 
	.byte		N05   , Dn5 
	.byte	W18
	.byte		        Gn4 
	.byte		N05   , As4 
	.byte	W18
@ 017   ----------------------------------------
mus_hgss_casino_1_017:
	.byte		N05   , Ds4 , v112
	.byte		N05   , Gn4 
	.byte	W12
	.byte		        Cn4 
	.byte	W12
	.byte		        Dn4 
	.byte	W12
	.byte		        Ds4 
	.byte	W12
	.byte		        Fn4 
	.byte	W12
	.byte		        Ds4 
	.byte	W12
	.byte		        Fn4 
	.byte	W06
	.byte		        Ds4 
	.byte	W12
	.byte		N17   , Fn4 
	.byte	W06
	.byte	PEND
@ 018   ----------------------------------------
mus_hgss_casino_1_018:
	.byte	W12
	.byte		N23   , Gn4 , v112
	.byte	W24
	.byte		N05   , Fs4 
	.byte	W06
	.byte		        Fn4 
	.byte	W18
	.byte		        As4 
	.byte		N05   , Dn5 
	.byte	W18
	.byte		        Gn4 
	.byte		N05   , As4 
	.byte	W18
	.byte	PEND
@ 019   ----------------------------------------
	.byte		        Ds4 
	.byte		N05   , Gn4 
	.byte	W12
	.byte		        Cn4 
	.byte	W12
	.byte		        Dn4 
	.byte	W12
	.byte		        Ds4 
	.byte	W18
	.byte		        Fn4 
	.byte	W06
	.byte		        Ds4 
	.byte	W12
	.byte		        Gn4 
	.byte	W06
	.byte		        Ds4 
	.byte	W12
	.byte		N17   , As4 
	.byte	W06
@ 020   ----------------------------------------
	.byte	W12
	.byte		N11   , An4 
	.byte	W12
	.byte		N05   , As4 
	.byte	W06
	.byte		        Cn5 
	.byte	W30
	.byte		        As4 
	.byte		N05   , Dn5 
	.byte	W18
	.byte		        Gn4 
	.byte		N05   , As4 
	.byte	W18
@ 021   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_1_017
@ 022   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_1_018
@ 023   ----------------------------------------
	.byte		N05   , Ds4 , v112
	.byte		N05   , Gn4 
	.byte	W12
	.byte		        Cn4 
	.byte	W12
	.byte		        Dn4 
	.byte	W12
	.byte		        Ds4 
	.byte	W12
	.byte		        Fn4 
	.byte	W12
	.byte		        Ds4 
	.byte	W12
	.byte		        Fn4 
	.byte	W06
	.byte		N12   , Ds4 
	.byte	W12
	.byte		N17   , Gn4 
	.byte	W06
@ 024   ----------------------------------------
	.byte	W12
	.byte		N23   , Fn4 
	.byte	W84
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
	 .word	mus_hgss_casino_1_B1
mus_hgss_casino_1_B2:
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 2 (Midi-Chn.2) ****************@

mus_hgss_casino_2:
	.byte	KEYSH , mus_hgss_casino_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 1
	.byte		VOL   , 103*mus_hgss_casino_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		MOD   , 0
	.byte	W60
	.byte		N05   , Ds3 , v116
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		        Ds3 
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
mus_hgss_casino_2_B1:
@ 001   ----------------------------------------
mus_hgss_casino_2_001:
	.byte		N05   , Ds3 , v116
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		        Fn3 , v120
	.byte		N05   , An3 
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		N10   , Fn3 , v120
	.byte		N10   , An3 
	.byte	W24
	.byte		N05   , Ds3 , v116
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		        Ds3 
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte	PEND
@ 002   ----------------------------------------
	.byte		        Fn3 , v120
	.byte		N05   , As3 
	.byte	W12
	.byte		        Fn3 
	.byte		N05   , An3 
	.byte	W12
	.byte		        Ds3 , v116
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		N16   , Fn3 
	.byte		N16   , An3 
	.byte	W30
	.byte		N05   , Ds3 , v116
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		        Ds3 
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
@ 003   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_2_001
@ 004   ----------------------------------------
	.byte		N05   , Fn3 , v120
	.byte		N05   , As3 
	.byte	W12
	.byte		        Fn3 
	.byte		N05   , An3 
	.byte	W12
	.byte		        Fn3 
	.byte		N05   , As3 
	.byte	W06
	.byte		N16   , Fn3 
	.byte		N16   , Cn4 
	.byte	W30
	.byte		N05   , Ds3 , v116
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		        Ds3 
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
@ 005   ----------------------------------------
mus_hgss_casino_2_005:
	.byte		N05   , Ds3 , v116
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		        Fn3 
	.byte		N05   , An3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		N11   , Fn3 
	.byte		N11   , An3 , v120
	.byte	W24
	.byte		N05   , Gs3 , v116
	.byte		N05   , Cn4 , v120
	.byte	W06
	.byte		        Fn3 
	.byte	W12
	.byte		        Gs3 , v116
	.byte		N05   , Cn4 , v120
	.byte	W06
	.byte		        Fn3 
	.byte	W12
	.byte	PEND
@ 006   ----------------------------------------
mus_hgss_casino_2_006:
	.byte		N05   , As3 , v116
	.byte		N05   , Ds4 , v120
	.byte	W12
	.byte		        As3 , v116
	.byte		N05   , Dn4 , v120
	.byte	W12
	.byte		        Gs3 , v116
	.byte		N05   , Cn4 , v120
	.byte	W06
	.byte		N17   , As3 , v116
	.byte		N17   , Dn4 , v120
	.byte	W30
	.byte		N05   , Ds3 , v116
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		        Ds3 
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte	PEND
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_2_005
@ 008   ----------------------------------------
mus_hgss_casino_2_008:
	.byte		N05   , As3 , v116
	.byte		N05   , Ds4 , v120
	.byte	W12
	.byte		        As3 , v116
	.byte		N05   , Dn4 , v120
	.byte	W12
	.byte		        Gs3 , v116
	.byte		N05   , Cn4 , v120
	.byte	W06
	.byte		N11   , As3 , v116
	.byte		N11   , Dn4 , v120
	.byte	W30
	.byte		N05   , Ds3 , v116
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		        Ds3 
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte	PEND
@ 009   ----------------------------------------
mus_hgss_casino_2_009:
	.byte		N05   , Ds3 , v116
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		        Fn3 , v120
	.byte		N05   , An3 
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		N11   , Fn3 , v120
	.byte		N11   , An3 
	.byte	W24
	.byte		N05   , Gs3 
	.byte		N05   , Cn4 
	.byte	W06
	.byte		        Fn3 
	.byte	W12
	.byte		        Gs3 
	.byte		N05   , Cn4 
	.byte	W06
	.byte		        Fn3 
	.byte	W12
	.byte	PEND
@ 010   ----------------------------------------
mus_hgss_casino_2_010:
	.byte		N05   , As3 , v120
	.byte		N05   , Ds4 
	.byte	W12
	.byte		        As3 
	.byte		N05   , Dn4 
	.byte	W12
	.byte		        Gs3 
	.byte		N05   , Cn4 
	.byte	W06
	.byte		N17   , As3 
	.byte		N17   , Dn4 
	.byte	W30
	.byte		N05   , Ds3 , v116
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		        Ds3 
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte	PEND
@ 011   ----------------------------------------
mus_hgss_casino_2_011:
	.byte		N05   , Ds3 , v116
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		        Fn3 , v120
	.byte		N05   , An3 
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		N11   , Fn3 , v120
	.byte		N11   , An3 
	.byte	W24
	.byte		N05   , Gs3 
	.byte		N05   , Cn4 
	.byte	W06
	.byte		        Fn3 
	.byte	W12
	.byte		        Gs3 
	.byte		N05   , Cn4 
	.byte	W12
	.byte		N17   , Gs3 
	.byte		N17   , Ds4 
	.byte	W06
	.byte	PEND
@ 012   ----------------------------------------
	.byte	W12
	.byte		N05   , Gn3 
	.byte		N05   , Dn4 
	.byte	W12
	.byte		        As3 
	.byte		N05   , Ds4 
	.byte	W06
	.byte		N17   , Cn4 
	.byte		N17   , Fn4 
	.byte	W30
	.byte		N05   , Ds3 , v116
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		        Ds3 
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
@ 013   ----------------------------------------
mus_hgss_casino_2_013:
	.byte		N05   , Ds3 , v116
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		        Fn3 
	.byte		N05   , An3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		N11   , Fn3 
	.byte		N11   , An3 , v120
	.byte	W24
	.byte		N05   , Ds3 , v116
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		        Ds3 
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte	PEND
@ 014   ----------------------------------------
	.byte		        Fn3 
	.byte		N05   , As3 , v120
	.byte	W12
	.byte		        Fn3 , v116
	.byte		N05   , An3 , v120
	.byte	W12
	.byte		        Ds3 , v116
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		N17   , Fn3 , v116
	.byte		N17   , An3 , v120
	.byte	W30
	.byte		N05   , Ds3 , v116
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		        Ds3 
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
@ 015   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_2_013
@ 016   ----------------------------------------
	.byte		N05   , Fn3 , v116
	.byte		N05   , As3 , v120
	.byte	W12
	.byte		        Fn3 , v116
	.byte		N05   , An3 , v120
	.byte	W12
	.byte		        Fn3 , v116
	.byte		N05   , As3 , v120
	.byte	W06
	.byte		N17   , Fn3 , v116
	.byte		N17   , Cn4 , v120
	.byte	W30
	.byte		N05   , Ds3 , v116
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		        Ds3 
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
@ 017   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_2_005
@ 018   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_2_006
@ 019   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_2_005
@ 020   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_2_008
@ 021   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_2_009
@ 022   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_2_010
@ 023   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_2_011
@ 024   ----------------------------------------
	.byte	W12
	.byte		N05   , Gn3 , v120
	.byte		N05   , Dn4 
	.byte	W12
	.byte		        As3 , v088
	.byte		N05   , Ds4 
	.byte	W06
	.byte		N17   , Cn4 
	.byte		N17   , Fn4 
	.byte	W18
	.byte		N04   , Fn5 , v060
	.byte	W06
	.byte		        Cn5 , v052
	.byte	W06
	.byte		        Gs4 , v060
	.byte	W06
	.byte		        Cn5 , v052
	.byte	W06
	.byte		        Gs4 , v060
	.byte	W06
	.byte		        Fn4 , v052
	.byte	W06
	.byte		        Gs4 , v060
	.byte	W06
	.byte		        Cn5 , v052
	.byte	W06
@ 025   ----------------------------------------
	.byte		        Fn5 , v060
	.byte	W06
	.byte		        Cn5 , v052
	.byte	W06
	.byte		        Gs4 , v060
	.byte	W06
	.byte		        Cn5 , v052
	.byte	W06
	.byte		        Gs4 , v060
	.byte	W06
	.byte		        Fn4 , v052
	.byte	W06
	.byte		        Gs4 , v060
	.byte	W06
	.byte		        Cn5 
	.byte	W06
	.byte		        Gn5 
	.byte	W06
	.byte		        Dn5 , v052
	.byte	W06
	.byte		        As4 , v060
	.byte	W06
	.byte		        Dn5 , v052
	.byte	W06
	.byte		        As4 , v060
	.byte	W06
	.byte		        Gn4 , v052
	.byte	W06
	.byte		        As4 , v060
	.byte	W06
	.byte		        Dn5 , v052
	.byte	W06
@ 026   ----------------------------------------
	.byte		        Gn5 , v060
	.byte	W06
	.byte		        Dn5 , v052
	.byte	W06
	.byte		        As4 , v060
	.byte	W06
	.byte		        Dn5 , v052
	.byte	W06
	.byte		        As4 , v060
	.byte	W06
	.byte		        Gn4 , v052
	.byte	W06
	.byte		        As4 , v060
	.byte	W06
	.byte		        Dn5 , v052
	.byte	W06
	.byte		        Cn5 , v060
	.byte	W06
	.byte		        Gn4 , v052
	.byte	W06
	.byte		        Ds4 , v060
	.byte	W06
	.byte		        Gn4 , v052
	.byte	W06
	.byte		        Cn4 , v060
	.byte	W06
	.byte		        Ds4 , v052
	.byte	W06
	.byte		        Gn4 , v060
	.byte	W06
	.byte		        Cn5 , v052
	.byte	W06
@ 027   ----------------------------------------
	.byte		        Gn4 , v060
	.byte	W06
	.byte		        Ds4 , v052
	.byte	W06
	.byte		        Gn4 , v060
	.byte	W06
	.byte		        Cn5 , v052
	.byte	W06
	.byte		        Ds5 , v060
	.byte	W06
	.byte		        Cn5 , v052
	.byte	W06
	.byte		        Ds4 , v060
	.byte	W06
	.byte		        As4 , v052
	.byte	W06
	.byte		        Cn5 , v060
	.byte	W06
	.byte		        An4 , v052
	.byte	W06
	.byte		        Fn4 , v060
	.byte	W06
	.byte		        An4 , v052
	.byte	W06
	.byte		        Fn4 , v060
	.byte	W06
	.byte		        Cn4 , v052
	.byte	W06
	.byte		        Fn4 , v060
	.byte	W06
	.byte		        An4 , v052
	.byte	W06
@ 028   ----------------------------------------
	.byte		        Fn5 , v060
	.byte	W06
	.byte		        Fn5 , v052
	.byte	W06
	.byte		        Cn5 , v060
	.byte	W06
	.byte		        An4 , v052
	.byte	W06
	.byte		        Cn5 , v060
	.byte	W06
	.byte		        An4 , v052
	.byte	W06
	.byte		        Fn4 , v060
	.byte	W06
	.byte		        Cn4 , v052
	.byte	W06
	.byte		        Fn5 , v060
	.byte	W06
	.byte		        Cn5 , v052
	.byte	W06
	.byte		        Gs4 , v060
	.byte	W06
	.byte		        Cn5 , v052
	.byte	W06
	.byte		        Gs4 , v060
	.byte	W06
	.byte		        Fn4 , v052
	.byte	W06
	.byte		        Gs4 , v060
	.byte	W06
	.byte		        Cn5 , v052
	.byte	W06
@ 029   ----------------------------------------
	.byte		        Fn5 , v060
	.byte	W06
	.byte		        Cn5 , v052
	.byte	W06
	.byte		        Gs4 , v060
	.byte	W06
	.byte		        Cn5 , v052
	.byte	W06
	.byte		        Gs4 , v060
	.byte	W06
	.byte		        Fn4 , v052
	.byte	W06
	.byte		        Gs4 , v060
	.byte	W06
	.byte		        Cn5 , v052
	.byte	W06
	.byte		        Gn5 , v060
	.byte	W06
	.byte		        Dn5 , v052
	.byte	W06
	.byte		        As4 , v060
	.byte	W06
	.byte		        Dn5 , v052
	.byte	W06
	.byte		        As4 , v060
	.byte	W06
	.byte		        Gn4 , v052
	.byte	W06
	.byte		        As4 , v060
	.byte	W06
	.byte		        Dn5 , v052
	.byte	W06
@ 030   ----------------------------------------
	.byte		        Gn5 , v060
	.byte	W06
	.byte		        Dn5 , v052
	.byte	W06
	.byte		        As4 , v060
	.byte	W06
	.byte		        Dn5 , v052
	.byte	W06
	.byte		        As4 , v060
	.byte	W06
	.byte		        Gn4 , v052
	.byte	W06
	.byte		        As4 , v060
	.byte	W06
	.byte		        Dn5 , v052
	.byte	W06
	.byte		        Gn5 , v060
	.byte	W06
	.byte		        Dn5 , v052
	.byte	W06
	.byte		        Bn4 , v060
	.byte	W06
	.byte		        Dn5 , v052
	.byte	W06
	.byte		        Bn4 , v060
	.byte	W06
	.byte		        Gn4 , v052
	.byte	W06
	.byte		        Bn4 , v060
	.byte	W06
	.byte		        Dn5 , v052
	.byte	W06
@ 031   ----------------------------------------
	.byte		        Bn4 , v060
	.byte	W06
	.byte		        Bn4 , v052
	.byte	W06
	.byte		        Gn4 , v060
	.byte	W06
	.byte		        Bn4 , v052
	.byte	W06
	.byte		        Dn4 , v060
	.byte	W06
	.byte		        Gn4 , v052
	.byte	W06
	.byte		        Bn4 , v060
	.byte	W06
	.byte		        Dn5 , v052
	.byte	W06
	.byte		N05   , Dn4 
	.byte		N05   , Gn4 , v064
	.byte	W06
	.byte		        Dn4 , v048
	.byte		N05   , Gn4 , v060
	.byte	W06
	.byte		        Dn4 , v052
	.byte		N05   , Gn4 , v064
	.byte	W18
	.byte		        Fn4 , v092
	.byte		N05   , As4 , v116
	.byte	W12
	.byte		        Fn4 , v100
	.byte		N05   , As4 , v120
	.byte	W06
@ 032   ----------------------------------------
	.byte	W60
	.byte		        Ds3 , v116
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte		        Ds3 
	.byte		N05   , Gn3 , v120
	.byte	W06
	.byte		        Cn3 , v116
	.byte	W12
	.byte	GOTO
	 .word	mus_hgss_casino_2_B1
mus_hgss_casino_2_B2:
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 3 (Midi-Chn.3) ****************@

mus_hgss_casino_3:
	.byte	KEYSH , mus_hgss_casino_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 126
	.byte		VOL   , 54*mus_hgss_casino_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		MOD   , 0
	.byte	W96
mus_hgss_casino_3_B1:
@ 001   ----------------------------------------
	.byte	W96
@ 002   ----------------------------------------
	.byte	W96
@ 003   ----------------------------------------
	.byte	W96
@ 004   ----------------------------------------
	.byte	W96
@ 005   ----------------------------------------
	.byte	W96
@ 006   ----------------------------------------
	.byte	W96
@ 007   ----------------------------------------
	.byte	W96
@ 008   ----------------------------------------
	.byte	W96
@ 009   ----------------------------------------
	.byte	W96
@ 010   ----------------------------------------
	.byte	W96
@ 011   ----------------------------------------
	.byte	W96
@ 012   ----------------------------------------
	.byte	W84
	.byte		N11   , As6 , v092
	.byte	W12
@ 013   ----------------------------------------
mus_hgss_casino_3_013:
	.byte	W12
	.byte		N11   , As6 , v092
	.byte	W24
	.byte		N11   
	.byte	W24
	.byte		N11   
	.byte	W24
	.byte		N11   
	.byte	W12
	.byte	PEND
@ 014   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_3_013
@ 015   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_3_013
@ 016   ----------------------------------------
mus_hgss_casino_3_016:
	.byte	W12
	.byte		N11   , As6 , v092
	.byte	W72
	.byte		N11   
	.byte	W12
	.byte	PEND
@ 017   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_3_013
@ 018   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_3_013
@ 019   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_3_013
@ 020   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_3_016
@ 021   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_3_013
@ 022   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_3_013
@ 023   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_3_013
@ 024   ----------------------------------------
	.byte	W12
	.byte		N11   , As6 , v092
	.byte	W72
	.byte		        As6 , v096
	.byte	W12
@ 025   ----------------------------------------
mus_hgss_casino_3_025:
	.byte	W12
	.byte		N11   , As6 , v096
	.byte	W24
	.byte		N11   
	.byte	W24
	.byte		N11   
	.byte	W24
	.byte		N11   
	.byte	W12
	.byte	PEND
@ 026   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_3_025
@ 027   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_3_025
@ 028   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_3_025
@ 029   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_3_025
@ 030   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_3_025
@ 031   ----------------------------------------
	.byte	W78
	.byte		N11   , As6 , v112
	.byte	W12
	.byte		N05   
	.byte	W06
@ 032   ----------------------------------------
	.byte	W96
	.byte	GOTO
	 .word	mus_hgss_casino_3_B1
mus_hgss_casino_3_B2:
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 4 (Midi-Chn.4) ****************@

mus_hgss_casino_4:
	.byte	KEYSH , mus_hgss_casino_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 83
	.byte		VOL   , 90*mus_hgss_casino_mvl/mxv
	.byte		PAN   , c_v-1
	.byte		MOD   , 0
	.byte	W48
	.byte		N05   , Cn2 , v036
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
mus_hgss_casino_4_B1:
@ 001   ----------------------------------------
	.byte		N05   , Gn3 , v036
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        An3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		N11   , An3 
	.byte	W12
	.byte		N05   , Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
@ 002   ----------------------------------------
mus_hgss_casino_4_002:
	.byte		N05   , As3 , v036
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        An3 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		N17   , An3 
	.byte	W18
	.byte		N05   , Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte	PEND
@ 003   ----------------------------------------
mus_hgss_casino_4_003:
	.byte		N05   , Gn3 , v036
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        An3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        An3 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte	PEND
@ 004   ----------------------------------------
	.byte		        As3 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        An3 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		N11   , An3 
	.byte	W12
	.byte		N05   , Cn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
@ 005   ----------------------------------------
mus_hgss_casino_4_005:
	.byte		N05   , Gn3 , v036
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        An3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        An3 
	.byte	W12
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte	PEND
@ 006   ----------------------------------------
mus_hgss_casino_4_006:
	.byte		N05   , As3 , v036
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Cn4 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        An3 
	.byte	W06
	.byte		        Cn3 
	.byte	W12
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte	PEND
@ 007   ----------------------------------------
mus_hgss_casino_4_007:
	.byte		N05   , Gn3 , v036
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        An3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        An3 
	.byte	W12
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte	PEND
@ 008   ----------------------------------------
	.byte		        Cn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn4 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        An3 
	.byte	W06
	.byte		N11   , Cn3 
	.byte	W12
	.byte		N05   , Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
@ 009   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_4_005
@ 010   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_4_006
@ 011   ----------------------------------------
	.byte		N05   , Gn3 , v036
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        An3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        An3 
	.byte	W60
@ 012   ----------------------------------------
mus_hgss_casino_4_012:
	.byte	W48
	.byte		N05   , Cn2 , v036
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte	PEND
@ 013   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_4_005
@ 014   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_4_002
@ 015   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_4_003
@ 016   ----------------------------------------
	.byte		N05   , As3 , v036
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        An3 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Cn2 
	.byte		N05   , Gn3 
	.byte	W06
	.byte		N11   , An3 
	.byte	W12
	.byte		N05   , Cn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
@ 017   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_4_005
@ 018   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_4_006
@ 019   ----------------------------------------
	.byte		N05   , Gn3 , v036
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        An3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        An3 
	.byte	W12
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
@ 020   ----------------------------------------
	.byte		        Cn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		N11   
	.byte	W12
	.byte		N05   , Cn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
@ 021   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_4_005
@ 022   ----------------------------------------
	.byte		N05   , As3 , v036
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Cn4 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        An3 
	.byte	W06
	.byte		N11   , Cn3 
	.byte	W12
	.byte		N05   , Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
@ 023   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_4_007
@ 024   ----------------------------------------
	.byte		N05   , Cn3 , v036
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        Cn4 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Cn2 
	.byte	W06
	.byte		        An3 
	.byte	W06
	.byte		        Ds3 , v048
	.byte	W06
	.byte		        Fn4 
	.byte	W06
	.byte		N32   , Gn4 , v056, gtp3
	.byte	W36
	.byte		        Fn4 , v052, gtp3
	.byte	W12
@ 025   ----------------------------------------
	.byte	W24
	.byte		N23   , Cn4 
	.byte	W24
	.byte		N32   , Dn4 , v052, gtp3
	.byte	W36
	.byte		        Ds4 , v052, gtp3
	.byte	W12
@ 026   ----------------------------------------
	.byte	W24
	.byte		N23   , Fn4 
	.byte	W24
	.byte		N32   , Dn4 , v052, gtp3
	.byte	W36
	.byte		        Cn4 , v052, gtp3
	.byte	W12
@ 027   ----------------------------------------
	.byte	W24
	.byte		N23   , As3 
	.byte	W24
	.byte		N44   , An3 , v052, gtp3
	.byte	W48
@ 028   ----------------------------------------
	.byte	W96
@ 029   ----------------------------------------
	.byte	W96
@ 030   ----------------------------------------
	.byte	W96
@ 031   ----------------------------------------
	.byte	W96
@ 032   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_4_012
	.byte	GOTO
	 .word	mus_hgss_casino_4_B1
mus_hgss_casino_4_B2:
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 5 (Midi-Chn.5) ****************@

mus_hgss_casino_5:
	.byte	KEYSH , mus_hgss_casino_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 48
	.byte		PAN   , c_v-1
	.byte		VOL   , 102*mus_hgss_casino_mvl/mxv
	.byte		MOD   , 0
	.byte	W96
mus_hgss_casino_5_B1:
@ 001   ----------------------------------------
	.byte	W96
@ 002   ----------------------------------------
	.byte		VOICE , 73
	.byte		N05   , Cn4 , v056
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn4 
	.byte	W06
	.byte		        Fn4 
	.byte	W06
	.byte		        Cn4 
	.byte	W06
	.byte		        An4 
	.byte	W06
	.byte		        Cn5 , v060
	.byte	W06
	.byte		        Fn5 
	.byte	W54
@ 003   ----------------------------------------
	.byte	W96
@ 004   ----------------------------------------
	.byte		        Cn4 , v056
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn4 
	.byte	W06
	.byte		        Fn4 
	.byte	W06
	.byte		        Cn4 
	.byte	W06
	.byte		        An4 
	.byte	W06
	.byte		        Cn5 , v060
	.byte	W06
	.byte		        Fn5 
	.byte	W06
	.byte		VOICE , 21
	.byte		N05   , Ds2 , v072
	.byte	W18
	.byte		        Ds2 , v064
	.byte	W18
	.byte		        Ds2 , v068
	.byte	W12
@ 005   ----------------------------------------
mus_hgss_casino_5_005:
	.byte		N05   , Ds2 , v072
	.byte	W12
	.byte		N05   
	.byte	W12
	.byte		N05   
	.byte	W12
	.byte		N05   
	.byte	W12
	.byte		N05   
	.byte	W18
	.byte		N05   
	.byte	W18
	.byte		N05   
	.byte	W12
	.byte	PEND
@ 006   ----------------------------------------
mus_hgss_casino_5_006:
	.byte		N05   , Ds2 , v072
	.byte	W12
	.byte		N05   
	.byte	W12
	.byte		N05   
	.byte	W12
	.byte		N05   
	.byte	W12
	.byte		N05   
	.byte	W18
	.byte		        Ds2 , v064
	.byte	W18
	.byte		        Ds2 , v068
	.byte	W12
	.byte	PEND
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_5_006
@ 008   ----------------------------------------
	.byte		N05   , Ds2 , v072
	.byte	W12
	.byte		N05   
	.byte	W12
	.byte		        Fn2 
	.byte	W12
	.byte		        Ds2 
	.byte	W12
	.byte		N05   
	.byte	W18
	.byte		        Ds2 , v064
	.byte	W18
	.byte		        Ds2 , v068
	.byte	W12
@ 009   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_5_005
@ 010   ----------------------------------------
	.byte		N05   , Ds2 , v072
	.byte	W12
	.byte		N05   
	.byte	W12
	.byte		        Fn2 
	.byte	W12
	.byte		        Dn2 
	.byte	W12
	.byte		        Ds2 
	.byte	W18
	.byte		        Ds2 , v064
	.byte	W18
	.byte		        Ds2 , v068
	.byte	W12
@ 011   ----------------------------------------
	.byte		        Ds2 , v072
	.byte	W12
	.byte		N05   
	.byte	W12
	.byte		N05   
	.byte	W12
	.byte		N05   
	.byte	W60
@ 012   ----------------------------------------
	.byte	W48
	.byte		N05   
	.byte	W18
	.byte		        Ds2 , v064
	.byte	W18
	.byte		        Ds2 , v068
	.byte	W12
@ 013   ----------------------------------------
mus_hgss_casino_5_013:
	.byte		N05   , Ds2 , v072
	.byte	W48
	.byte		N05   
	.byte	W18
	.byte		N05   
	.byte	W18
	.byte		N05   
	.byte	W12
	.byte	PEND
@ 014   ----------------------------------------
mus_hgss_casino_5_014:
	.byte		VOICE , 73
	.byte		N05   , Cn4 , v056
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        Cn4 
	.byte	W06
	.byte		        Fn4 
	.byte	W06
	.byte		        Cn4 
	.byte	W06
	.byte		        An4 
	.byte	W06
	.byte		        Cn5 
	.byte	W06
	.byte		        Fn5 
	.byte	W06
	.byte		VOICE , 21
	.byte		N05   , Ds2 , v072
	.byte	W18
	.byte		        Ds2 , v064
	.byte	W18
	.byte		        Ds2 , v068
	.byte	W12
	.byte	PEND
@ 015   ----------------------------------------
mus_hgss_casino_5_015:
	.byte		N05   , Ds2 , v072
	.byte	W48
	.byte		N05   
	.byte	W18
	.byte		        Ds2 , v064
	.byte	W18
	.byte		        Ds2 , v068
	.byte	W12
	.byte	PEND
@ 016   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_5_014
@ 017   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_5_013
@ 018   ----------------------------------------
	.byte		N05   , Gn2 , v072
	.byte	W12
	.byte		        Fn2 
	.byte	W12
	.byte		        Ds2 
	.byte	W06
	.byte		N14   , Fn2 
	.byte	W18
	.byte		N05   , Ds2 
	.byte	W18
	.byte		        Ds2 , v064
	.byte	W18
	.byte		        Ds2 , v068
	.byte	W12
@ 019   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_5_015
@ 020   ----------------------------------------
	.byte		N05   , Gn2 , v072
	.byte	W12
	.byte		        Fn2 
	.byte	W12
	.byte		        Gn2 
	.byte	W06
	.byte		N14   , As2 , v064
	.byte	W18
	.byte		N05   , Ds2 , v072
	.byte	W18
	.byte		        Ds2 , v064
	.byte	W18
	.byte		        Ds2 , v068
	.byte	W12
@ 021   ----------------------------------------
	.byte		        Ds2 , v072
	.byte	W48
	.byte		N05   
	.byte	W18
	.byte		N05   
	.byte	W18
	.byte		        Gn2 , v068
	.byte	W12
@ 022   ----------------------------------------
	.byte		        Gn2 , v072
	.byte	W12
	.byte		        Fn2 
	.byte	W12
	.byte		        Ds2 
	.byte	W06
	.byte		N11   , Fn2 
	.byte	W18
	.byte		N05   , Ds2 
	.byte	W18
	.byte		        Ds2 , v064
	.byte	W18
	.byte		        Ds2 , v068
	.byte	W12
@ 023   ----------------------------------------
	.byte		        Ds2 , v072
	.byte	W48
	.byte		N05   
	.byte	W18
	.byte		        Ds2 , v064
	.byte	W12
	.byte		        Gn2 , v060
	.byte	W12
	.byte		N02   , Gn2 , v032
	.byte	W06
@ 024   ----------------------------------------
	.byte		N11   , Gn2 , v088
	.byte	W12
	.byte		        Fn2 
	.byte	W12
	.byte		VOICE , 58
	.byte		N03   , As1 , v064
	.byte	W03
	.byte		        Cn2 , v052
	.byte		N03   , Gs2 , v072
	.byte	W03
	.byte		        Dn2 
	.byte		N03   , As2 , v080
	.byte	W04
	.byte		        Ds2 , v072
	.byte		N03   , Cn3 , v080
	.byte	W03
	.byte		        Fn2 
	.byte		N03   , Dn3 , v088
	.byte	W04
	.byte		        Gn2 , v080
	.byte		N03   , Ds3 , v088
	.byte	W03
	.byte		        An2 
	.byte		N03   , Fn3 , v096
	.byte	W04
	.byte		N32   , As2 , v080, gtp3
	.byte		N32   , Gn3 , v088, gtp3
	.byte	W36
	.byte		        Gs2 , v080, gtp3
	.byte		N32   , Fn3 , v088, gtp3
	.byte	W12
@ 025   ----------------------------------------
	.byte	W24
	.byte		N23   , Fn2 , v080
	.byte		N23   , Cn3 , v088
	.byte	W24
	.byte		N32   , Fn2 , v080, gtp3
	.byte		N32   , Dn3 , v088, gtp3
	.byte	W36
	.byte		        Gn2 , v080, gtp3
	.byte		N32   , Ds3 , v088, gtp3
	.byte	W12
@ 026   ----------------------------------------
	.byte	W24
	.byte		N23   , As2 , v080
	.byte		N23   , Fn3 , v088
	.byte	W24
	.byte		N32   , Fn2 , v080, gtp3
	.byte		N32   , Dn3 , v088, gtp3
	.byte	W36
	.byte		        Ds2 , v080, gtp3
	.byte		N32   , Cn3 , v088, gtp3
	.byte	W12
@ 027   ----------------------------------------
	.byte	W24
	.byte		N23   , Dn2 , v080
	.byte		N23   , As2 , v088
	.byte	W24
	.byte		N56   , Cn2 , v064, gtp3
	.byte		N56   , An2 , v088, gtp3
	.byte	W36
	.byte		VOL   , 84*mus_hgss_casino_mvl/mxv
	.byte	W03
	.byte		        72*mus_hgss_casino_mvl/mxv
	.byte	W03
	.byte		        65*mus_hgss_casino_mvl/mxv
	.byte	W03
	.byte		        55*mus_hgss_casino_mvl/mxv
	.byte	W03
@ 028   ----------------------------------------
	.byte		        48*mus_hgss_casino_mvl/mxv
	.byte	W03
	.byte		        40*mus_hgss_casino_mvl/mxv
	.byte	W03
	.byte		        33*mus_hgss_casino_mvl/mxv
	.byte	W06
	.byte		VOICE , 48
	.byte	W84
@ 029   ----------------------------------------
	.byte	W96
@ 030   ----------------------------------------
	.byte	W96
@ 031   ----------------------------------------
	.byte	W96
@ 032   ----------------------------------------
	.byte	W90
	.byte		        21
	.byte		VOL   , 102*mus_hgss_casino_mvl/mxv
	.byte	W06
	.byte	GOTO
	 .word	mus_hgss_casino_5_B1
mus_hgss_casino_5_B2:
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 6 (Midi-Chn.6) ****************@

mus_hgss_casino_6:
	.byte	KEYSH , mus_hgss_casino_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 81
	.byte		PAN   , c_v+0
	.byte		VOL   , 88*mus_hgss_casino_mvl/mxv
	.byte		MOD   , 0
	.byte	W48
	.byte		N05   , Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v040
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v040
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v040
	.byte	W06
mus_hgss_casino_6_B1:
@ 001   ----------------------------------------
mus_hgss_casino_6_001:
	.byte		N05   , Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v040
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v040
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v036
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v040
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v040
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v040
	.byte	W06
	.byte	PEND
@ 002   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_001
@ 003   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_001
@ 004   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_001
@ 005   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_001
@ 006   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_001
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_001
@ 008   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_001
@ 009   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_001
@ 010   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_001
@ 011   ----------------------------------------
	.byte		N05   , Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v040
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v040
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v036
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W48
@ 012   ----------------------------------------
	.byte	W48
	.byte		        Gn2 , v072
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v072
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v072
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
@ 013   ----------------------------------------
mus_hgss_casino_6_013:
	.byte		N05   , Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v072
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v072
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v048
	.byte	W06
	.byte		        Gn2 , v072
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v072
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v072
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte	PEND
@ 014   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_013
@ 015   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_013
@ 016   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_013
@ 017   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_013
@ 018   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_013
@ 019   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_013
@ 020   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_013
@ 021   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_013
@ 022   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_013
@ 023   ----------------------------------------
	.byte		N05   , Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v072
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v072
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v048
	.byte	W06
	.byte		        Gn2 , v072
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v072
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		N12   , Gn2 , v060
	.byte	W12
	.byte		N01   , Gn2 , v052
	.byte	W06
@ 024   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_013
@ 025   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_013
@ 026   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_013
@ 027   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_013
@ 028   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_013
@ 029   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_013
@ 030   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_6_013
@ 031   ----------------------------------------
	.byte		N05   , Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v072
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v072
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v048
	.byte	W06
	.byte		        Gn2 , v072
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W18
	.byte		N05   
	.byte	W12
	.byte		N05   
	.byte	W06
@ 032   ----------------------------------------
	.byte	W48
	.byte		N05   
	.byte	W06
	.byte		        Gn2 , v040
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v040
	.byte	W06
	.byte		        Gn2 , v052
	.byte	W06
	.byte		        Gn2 , v060
	.byte	W06
	.byte		        Gn2 , v040
	.byte	W06
	.byte	GOTO
	 .word	mus_hgss_casino_6_B1
mus_hgss_casino_6_B2:
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 7 (Midi-Chn.8) ****************@

mus_hgss_casino_7:
	.byte	KEYSH , mus_hgss_casino_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 1
	.byte		PAN   , c_v-1
	.byte		VOL   , 45*mus_hgss_casino_mvl/mxv
	.byte		MOD   , 0
	.byte	W96
mus_hgss_casino_7_B1:
@ 001   ----------------------------------------
	.byte	W96
@ 002   ----------------------------------------
	.byte	W96
@ 003   ----------------------------------------
	.byte	W96
@ 004   ----------------------------------------
	.byte	W96
@ 005   ----------------------------------------
	.byte	W96
@ 006   ----------------------------------------
	.byte	W96
@ 007   ----------------------------------------
	.byte	W96
@ 008   ----------------------------------------
	.byte	W96
@ 009   ----------------------------------------
	.byte	W96
@ 010   ----------------------------------------
	.byte	W96
@ 011   ----------------------------------------
	.byte	W72
	.byte		N05   , Gs3 , v092
	.byte		N05   , Cn4 , v100
	.byte	W06
	.byte		        Fn3 , v092
	.byte	W12
	.byte		        Gs3 
	.byte		N05   , Cn4 , v100
	.byte	W06
@ 012   ----------------------------------------
	.byte	W06
	.byte		N17   , Gs3 , v092
	.byte		N17   , Ds4 , v100
	.byte	W18
	.byte		N05   , Gn3 , v092
	.byte		N05   , Dn4 , v100
	.byte	W12
	.byte		        As3 , v092
	.byte		N05   , Ds4 , v100
	.byte	W06
	.byte		N17   , Cn4 , v092
	.byte		N17   , Fn4 , v100
	.byte	W54
@ 013   ----------------------------------------
	.byte	W96
@ 014   ----------------------------------------
	.byte	W96
@ 015   ----------------------------------------
	.byte	W96
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
	.byte	W96
@ 025   ----------------------------------------
	.byte		N04   , Fn5 
	.byte	W06
	.byte		        Cn5 , v088
	.byte	W06
	.byte		        Gs4 , v100
	.byte	W06
	.byte		        Cn5 , v088
	.byte	W06
	.byte		        Gs4 , v100
	.byte	W06
	.byte		        Fn4 , v088
	.byte	W06
	.byte		        Gs4 , v100
	.byte	W06
	.byte		        Cn5 , v088
	.byte	W06
	.byte		        Fn5 , v100
	.byte	W06
	.byte		        Cn5 , v088
	.byte	W06
	.byte		        Gs4 , v100
	.byte	W06
	.byte		        Cn5 , v088
	.byte	W06
	.byte		        Gs4 , v100
	.byte	W06
	.byte		        Fn4 , v088
	.byte	W06
	.byte		        Gs4 , v100
	.byte	W06
	.byte		        Cn5 
	.byte	W06
@ 026   ----------------------------------------
mus_hgss_casino_7_026:
	.byte		N04   , Gn5 , v100
	.byte	W06
	.byte		        Dn5 , v088
	.byte	W06
	.byte		        As4 , v100
	.byte	W06
	.byte		        Dn5 , v088
	.byte	W06
	.byte		        As4 , v100
	.byte	W06
	.byte		        Gn4 , v088
	.byte	W06
	.byte		        As4 , v100
	.byte	W06
	.byte		        Dn5 , v088
	.byte	W06
	.byte		        Gn5 , v100
	.byte	W06
	.byte		        Dn5 , v088
	.byte	W06
	.byte		        As4 , v100
	.byte	W06
	.byte		        Dn5 , v088
	.byte	W06
	.byte		        As4 , v100
	.byte	W06
	.byte		        Gn4 , v088
	.byte	W06
	.byte		        As4 , v100
	.byte	W06
	.byte		        Dn5 , v088
	.byte	W06
	.byte	PEND
@ 027   ----------------------------------------
	.byte		        Cn5 , v100
	.byte	W06
	.byte		        Gn4 , v088
	.byte	W06
	.byte		        Ds4 , v100
	.byte	W06
	.byte		        Gn4 , v088
	.byte	W06
	.byte		        Cn4 , v100
	.byte	W06
	.byte		        Ds4 , v088
	.byte	W06
	.byte		        Gn4 , v100
	.byte	W06
	.byte		        Cn5 , v088
	.byte	W06
	.byte		        Gn4 , v100
	.byte	W06
	.byte		        Ds4 , v088
	.byte	W06
	.byte		        Gn4 , v100
	.byte	W06
	.byte		        Cn5 , v088
	.byte	W06
	.byte		        Ds5 , v100
	.byte	W06
	.byte		        Cn5 , v088
	.byte	W06
	.byte		        Ds4 , v100
	.byte	W06
	.byte		        As4 , v088
	.byte	W06
@ 028   ----------------------------------------
	.byte		        Cn5 , v100
	.byte	W06
	.byte		        An4 , v088
	.byte	W06
	.byte		        Fn4 , v100
	.byte	W06
	.byte		        An4 , v088
	.byte	W06
	.byte		        Fn4 , v100
	.byte	W06
	.byte		        Cn4 , v088
	.byte	W06
	.byte		        Fn4 , v100
	.byte	W06
	.byte		        An4 , v088
	.byte	W06
	.byte		        Fn5 , v100
	.byte	W06
	.byte		        Fn5 , v088
	.byte	W06
	.byte		        Cn5 , v100
	.byte	W06
	.byte		        An4 , v088
	.byte	W06
	.byte		        Cn5 , v100
	.byte	W06
	.byte		        An4 , v088
	.byte	W06
	.byte		        Fn4 , v100
	.byte	W06
	.byte		        Cn4 , v088
	.byte	W06
@ 029   ----------------------------------------
	.byte		        Fn5 , v100
	.byte	W06
	.byte		        Cn5 , v088
	.byte	W06
	.byte		        Gs4 , v100
	.byte	W06
	.byte		        Cn5 , v088
	.byte	W06
	.byte		        Gs4 , v100
	.byte	W06
	.byte		        Fn4 , v088
	.byte	W06
	.byte		        Gs4 , v100
	.byte	W06
	.byte		        Cn5 , v088
	.byte	W06
	.byte		        Fn5 , v100
	.byte	W06
	.byte		        Cn5 , v088
	.byte	W06
	.byte		        Gs4 , v100
	.byte	W06
	.byte		        Cn5 , v088
	.byte	W06
	.byte		        Gs4 , v100
	.byte	W06
	.byte		        Fn4 , v088
	.byte	W06
	.byte		        Gs4 , v100
	.byte	W06
	.byte		        Cn5 , v088
	.byte	W06
@ 030   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_7_026
@ 031   ----------------------------------------
	.byte		N04   , Gn5 , v100
	.byte	W06
	.byte		        Dn5 , v088
	.byte	W06
	.byte		        Bn4 , v100
	.byte	W06
	.byte		        Dn5 , v088
	.byte	W06
	.byte		        Bn4 , v100
	.byte	W06
	.byte		        Gn4 , v088
	.byte	W06
	.byte		        Bn4 , v100
	.byte	W06
	.byte		        Dn5 , v088
	.byte	W54
@ 032   ----------------------------------------
	.byte	W96
	.byte	GOTO
	 .word	mus_hgss_casino_7_B1
mus_hgss_casino_7_B2:
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 8 (Midi-Chn.9) ****************@

mus_hgss_casino_8:
	.byte	KEYSH , mus_hgss_casino_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 17
	.byte		PAN   , c_v+0
	.byte		MOD   , 0
	.byte		VOL   , 105*mus_hgss_casino_mvl/mxv
	.byte	W96
mus_hgss_casino_8_B1:
@ 001   ----------------------------------------
	.byte	W96
@ 002   ----------------------------------------
	.byte	W96
@ 003   ----------------------------------------
	.byte	W96
@ 004   ----------------------------------------
	.byte	W96
@ 005   ----------------------------------------
	.byte	W96
@ 006   ----------------------------------------
	.byte	W96
@ 007   ----------------------------------------
	.byte	W96
@ 008   ----------------------------------------
	.byte	W96
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
	.byte	W96
@ 025   ----------------------------------------
	.byte	W96
@ 026   ----------------------------------------
	.byte	W96
@ 027   ----------------------------------------
	.byte	W84
	.byte		N01   , Fn4 , v092
	.byte		N01   , Fn5 
	.byte	W06
	.byte		        Fn4 
	.byte		N01   , Fn5 
	.byte	W06
@ 028   ----------------------------------------
	.byte		N32   , Fn2 , v116, gtp3
	.byte		N32   , Fn3 , v116, gtp3
	.byte	W07
	.byte		BEND  , c_v-5
	.byte	W02
	.byte		        c_v-9
	.byte	W01
	.byte		        c_v-12
	.byte	W02
	.byte		        c_v-14
	.byte	W01
	.byte		        c_v-17
	.byte	W02
	.byte		        c_v-21
	.byte	W01
	.byte		        c_v-24
	.byte	W02
	.byte		        c_v-26
	.byte	W01
	.byte		        c_v-29
	.byte	W02
	.byte		        c_v-33
	.byte	W01
	.byte		        c_v-35
	.byte	W02
	.byte		        c_v-38
	.byte	W01
	.byte		        c_v-42
	.byte	W02
	.byte		        c_v-45
	.byte	W01
	.byte		        c_v-50
	.byte	W02
	.byte		        c_v-55
	.byte	W01
	.byte		        c_v-60
	.byte	W02
	.byte		        c_v-64
	.byte	W03
	.byte		        c_v+0
	.byte		N04   , Cn4 , v104
	.byte	W01
	.byte		BEND  , c_v+0
	.byte		N04   , Ds4 , v116
	.byte	W05
	.byte		        Dn4 , v096
	.byte	W01
	.byte		        Fn4 , v112
	.byte	W05
	.byte		N32   , Ds4 , v104, gtp2
	.byte	W01
	.byte		        Gn4 , v116, gtp2
	.byte	W32
	.byte	W03
	.byte		        Dn4 , v104, gtp2
	.byte	W01
	.byte		        Fn4 , v116, gtp2
	.byte	W11
@ 029   ----------------------------------------
	.byte	W24
	.byte		N22   , Gs3 , v104
	.byte	W01
	.byte		        Cn4 , v116
	.byte	W23
	.byte		N32   , Bn3 , v104, gtp2
	.byte	W01
	.byte		        Dn4 , v116, gtp2
	.byte	W32
	.byte	W03
	.byte		        Bn3 , v104, gtp2
	.byte	W01
	.byte		        Ds4 , v116, gtp2
	.byte	W11
@ 030   ----------------------------------------
	.byte	W24
	.byte		N10   , Bn3 , v104
	.byte	W01
	.byte		        Fn4 , v116
	.byte	W11
	.byte		N11   , An3 , v108
	.byte	W02
	.byte		BEND  , c_v+5
	.byte	W02
	.byte		        c_v+16
	.byte	W02
	.byte		        c_v+21
	.byte	W02
	.byte		        c_v+32
	.byte	W02
	.byte		        c_v+37
	.byte	W02
	.byte		        c_v+0
	.byte		N84   , Bn3 , v104, gtp1
	.byte	W01
	.byte		        Gn4 , v116, gtp1
	.byte	W44
	.byte	W03
@ 031   ----------------------------------------
	.byte	W28
	.byte	W01
	.byte	W03
	.byte	W03
	.byte	W03
	.byte	W03
	.byte	W03
	.byte	W03
	.byte	W01
	.byte		N03   , Bn3 , v108
	.byte	W01
	.byte		        Gn4 , v116
	.byte	W01
	.byte	W04
	.byte		        Bn3 , v108
	.byte	W01
	.byte		        Gn4 , v116
	.byte	W05
	.byte		N04   , Bn3 , v108
	.byte	W01
	.byte		        Gn4 , v116
	.byte	W17
	.byte		        Dn4 , v108
	.byte	W01
	.byte		        As4 , v116
	.byte	W11
	.byte		        Dn4 , v108
	.byte	W01
	.byte		        As4 , v116
	.byte	W05
@ 032   ----------------------------------------
	.byte	W24
	.byte		N22   , Gn2 , v112
	.byte		N22   , Gn3 
	.byte	W03
	.byte		BEND  , c_v-9
	.byte	W01
	.byte		        c_v-13
	.byte	W02
	.byte		        c_v-19
	.byte	W01
	.byte		        c_v-23
	.byte	W02
	.byte		        c_v-29
	.byte	W01
	.byte		        c_v-33
	.byte	W02
	.byte		        c_v-39
	.byte	W01
	.byte		        c_v-44
	.byte	W02
	.byte		        c_v-47
	.byte	W01
	.byte		        c_v-53
	.byte	W02
	.byte		        c_v-59
	.byte	W01
	.byte		        c_v-62
	.byte	W02
	.byte		        c_v-64
	.byte	W02
	.byte		        c_v+0
	.byte	W48
	.byte	W01
	.byte	GOTO
	 .word	mus_hgss_casino_8_B1
mus_hgss_casino_8_B2:
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 9 (Midi-Chn.10) ****************@

mus_hgss_casino_9:
	.byte	KEYSH , mus_hgss_casino_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 0
	.byte		VOL   , 103*mus_hgss_casino_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		MOD   , 0
	.byte		VOL   , 103*mus_hgss_casino_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		MOD   , 0
	.byte		VOL   , 103*mus_hgss_casino_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		MOD   , 0
	.byte		N05   , Cn1 , v092
	.byte		N03   , En1 , v076
	.byte	W04
	.byte		        En1 , v088
	.byte	W04
	.byte		        En1 , v096
	.byte	W04
	.byte		N05   , En1 , v108
	.byte	W06
	.byte		        En1 , v116
	.byte	W06
	.byte		        Cn1 , v108
	.byte		N02   , Bn1 
	.byte	W03
	.byte		        Bn1 , v088
	.byte	W03
	.byte		N05   , Bn1 , v104
	.byte	W06
	.byte		N03   , Cn1 , v108
	.byte		N05   , An1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v108
	.byte		N05   , Fn1 , v104
	.byte	W06
	.byte		        Cn1 , v108
	.byte		N23   , An2 , v112
	.byte	W18
	.byte		N05   , Cn1 , v088
	.byte	W18
	.byte		        Cn1 , v100
	.byte	W12
mus_hgss_casino_9_B1:
@ 001   ----------------------------------------
	.byte		N05   , Cn1 , v108
	.byte	W24
	.byte		N11   , En1 , v112
	.byte	W24
	.byte		N05   , Cn1 , v108
	.byte	W18
	.byte		        Cn1 , v088
	.byte	W18
	.byte		        Cn1 , v108
	.byte	W12
@ 002   ----------------------------------------
	.byte		N05   
	.byte	W24
	.byte		N11   , En1 , v112
	.byte	W18
	.byte		N05   , Cn1 , v088
	.byte	W06
	.byte		        Cn1 , v108
	.byte		N23   , An2 , v112
	.byte	W18
	.byte		N05   , Cn1 , v088
	.byte	W18
	.byte		        Cn1 , v100
	.byte	W12
@ 003   ----------------------------------------
	.byte		        Cn1 , v108
	.byte	W24
	.byte		N11   , En1 , v112
	.byte	W24
	.byte		N05   , Cn1 , v108
	.byte	W06
	.byte		        Cn1 , v088
	.byte	W06
	.byte		        En1 , v100
	.byte	W06
	.byte		        Cn1 , v088
	.byte	W12
	.byte		N11   , En1 , v100
	.byte	W12
	.byte		N05   , Cn1 , v088
	.byte	W06
@ 004   ----------------------------------------
	.byte		        Cn1 , v108
	.byte	W06
	.byte		        Cn1 , v088
	.byte	W06
	.byte		N11   , En1 , v112
	.byte	W12
	.byte		N05   , Cn1 , v108
	.byte	W06
	.byte		        Cn1 , v088
	.byte	W06
	.byte		        An1 , v108
	.byte	W06
	.byte		        Fn1 , v100
	.byte	W06
	.byte		        Cn1 , v108
	.byte		N23   , An2 , v112
	.byte	W18
	.byte		N05   , Cn1 , v088
	.byte	W18
	.byte		        Cn1 , v100
	.byte	W12
@ 005   ----------------------------------------
	.byte		        Cn1 , v108
	.byte	W24
	.byte		N11   , En1 , v112
	.byte	W24
	.byte		N05   , Cn1 , v108
	.byte	W06
	.byte		        Cn1 , v088
	.byte	W06
	.byte		N11   , En1 , v092
	.byte	W12
	.byte		N05   , Cn1 
	.byte	W06
	.byte		        Cn1 , v088
	.byte	W06
	.byte		N11   , En1 , v092
	.byte	W12
@ 006   ----------------------------------------
	.byte		N05   , Cn1 , v108
	.byte	W06
	.byte		N11   , En1 , v100
	.byte	W12
	.byte		N05   , Cn1 , v088
	.byte	W06
	.byte		        Cn1 , v108
	.byte	W06
	.byte		N11   , En1 , v112
	.byte	W12
	.byte		N05   , Cn1 , v088
	.byte	W06
	.byte		        Cn1 , v108
	.byte	W18
	.byte		        Cn1 , v088
	.byte	W18
	.byte		        Cn1 , v100
	.byte	W12
@ 007   ----------------------------------------
	.byte		        Cn1 , v108
	.byte	W24
	.byte		N11   , En1 , v112
	.byte	W18
	.byte		N05   , Cn1 , v088
	.byte	W06
	.byte		        Cn1 , v108
	.byte	W06
	.byte		N11   , En1 , v092
	.byte	W12
	.byte		N05   , Cn1 , v088
	.byte	W06
	.byte		N05   
	.byte	W06
	.byte		N11   , En1 
	.byte	W12
	.byte		N05   , Cn1 
	.byte	W06
@ 008   ----------------------------------------
	.byte		        Cn1 , v108
	.byte	W06
	.byte		N11   , En1 , v096
	.byte	W12
	.byte		N05   , Cn1 , v088
	.byte	W06
	.byte		        Cn1 , v108
	.byte	W06
	.byte		        Cn1 , v088
	.byte	W06
	.byte		        Cn1 , v092
	.byte	W06
	.byte		        Cn1 , v088
	.byte	W06
	.byte		        Cn1 , v108
	.byte		N23   , An2 , v112
	.byte	W18
	.byte		N05   , Cn1 , v088
	.byte	W18
	.byte		        Cn1 , v100
	.byte	W12
@ 009   ----------------------------------------
	.byte		        Cn1 , v108
	.byte	W24
	.byte		N11   , En1 , v112
	.byte	W24
	.byte		N05   , Cn1 , v108
	.byte	W06
	.byte		        Cn1 , v088
	.byte	W06
	.byte		N11   , En1 
	.byte	W12
	.byte		N05   , Cn1 
	.byte	W06
	.byte		N11   , En1 
	.byte	W12
	.byte		N05   , Cn1 
	.byte	W06
@ 010   ----------------------------------------
	.byte		        Cn1 , v108
	.byte	W06
	.byte		N11   , En1 , v096
	.byte	W12
	.byte		N05   , Cn1 , v088
	.byte	W06
	.byte		        Cn1 , v108
	.byte	W12
	.byte		        Gn1 , v112
	.byte	W06
	.byte		        Cn1 , v088
	.byte		N05   , Fn1 , v112
	.byte	W06
	.byte		        Cn1 , v108
	.byte	W18
	.byte		        Cn1 , v088
	.byte	W18
	.byte		        Cn1 , v100
	.byte	W12
@ 011   ----------------------------------------
	.byte		        Cn1 , v108
	.byte		N03   , En1 , v068
	.byte	W04
	.byte		        En1 , v076
	.byte	W04
	.byte		        En1 , v088
	.byte	W04
	.byte		N05   , En1 , v104
	.byte	W06
	.byte		        En1 , v112
	.byte	W06
	.byte		N02   , Bn1 
	.byte	W03
	.byte		        Bn1 , v088
	.byte	W03
	.byte		N05   , Bn1 , v112
	.byte	W06
	.byte		        An1 , v092
	.byte	W06
	.byte		        Fn1 , v112
	.byte	W06
	.byte		N11   , Cn1 , v108
	.byte		N23   , An2 , v112
	.byte	W48
@ 012   ----------------------------------------
	.byte	W24
	.byte		N02   , En1 
	.byte	W03
	.byte		        En1 , v088
	.byte	W03
	.byte		N05   , En1 , v108
	.byte	W05
	.byte		        An1 
	.byte	W07
	.byte		        Gn1 , v104
	.byte	W06
	.byte		        Cn1 , v108
	.byte		N23   , An2 , v112
	.byte	W18
	.byte		N05   , Cn1 , v092
	.byte	W06
	.byte		N11   , En1 , v112
	.byte	W18
	.byte		N05   , Cn1 , v092
	.byte	W06
@ 013   ----------------------------------------
mus_hgss_casino_9_013:
	.byte		N05   , Cn1 , v108
	.byte	W24
	.byte		N11   , En1 , v112
	.byte	W18
	.byte		N05   , Cn1 , v092
	.byte	W06
	.byte		        Cn1 , v108
	.byte	W18
	.byte		        Cn1 , v092
	.byte	W06
	.byte		N11   , En1 , v112
	.byte	W18
	.byte		N05   , Cn1 , v092
	.byte	W06
	.byte	PEND
@ 014   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_9_013
@ 015   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_9_013
@ 016   ----------------------------------------
	.byte		N05   , Cn1 , v108
	.byte	W24
	.byte		        En1 , v112
	.byte	W06
	.byte		        En1 , v092
	.byte	W06
	.byte		        En1 , v104
	.byte	W06
	.byte		        Cn1 , v092
	.byte		N05   , En1 
	.byte	W06
	.byte		        Cn1 , v108
	.byte		N23   , An2 , v112
	.byte	W18
	.byte		N05   , Cn1 , v092
	.byte	W06
	.byte		N11   , En1 , v112
	.byte	W18
	.byte		N05   , Cn1 , v092
	.byte	W06
@ 017   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_9_013
@ 018   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_9_013
@ 019   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_9_013
@ 020   ----------------------------------------
	.byte		N05   , Cn1 , v108
	.byte	W24
	.byte		N11   , En1 , v112
	.byte	W12
	.byte		N05   , Gn1 
	.byte	W06
	.byte		        Cn1 , v092
	.byte		N05   , Fn1 , v112
	.byte	W06
	.byte		        Cn1 , v108
	.byte		N23   , An2 , v112
	.byte	W18
	.byte		N05   , Cn1 , v092
	.byte	W06
	.byte		N11   , En1 , v112
	.byte	W18
	.byte		N05   , Cn1 , v092
	.byte	W06
@ 021   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_9_013
@ 022   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_9_013
@ 023   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_9_013
@ 024   ----------------------------------------
	.byte		N05   , Cn1 , v108
	.byte	W06
	.byte		N02   , En1 , v080
	.byte	W03
	.byte		        En1 , v104
	.byte	W03
	.byte		N05   , En1 , v112
	.byte	W06
	.byte		        En1 , v100
	.byte	W06
	.byte		        An1 , v112
	.byte	W06
	.byte		        An1 , v100
	.byte	W06
	.byte		        Fn1 , v112
	.byte	W06
	.byte		        Cn1 , v092
	.byte		N05   , Fn1 
	.byte	W06
	.byte		        Cn1 , v108
	.byte		N23   , An2 , v112
	.byte	W18
	.byte		N05   , Cn1 , v096
	.byte	W06
	.byte		N11   , En1 , v112
	.byte	W06
	.byte		N05   , Cn1 , v108
	.byte	W12
	.byte		        Cn1 , v096
	.byte	W06
@ 025   ----------------------------------------
mus_hgss_casino_9_025:
	.byte		N05   , Cn1 , v108
	.byte	W06
	.byte		        En1 , v100
	.byte	W12
	.byte		        Cn1 , v096
	.byte	W06
	.byte		N11   , En1 , v112
	.byte	W24
	.byte		N05   , Cn1 , v108
	.byte	W18
	.byte		        Cn1 , v096
	.byte	W06
	.byte		N11   , En1 , v112
	.byte	W06
	.byte		N05   , Cn1 , v108
	.byte	W12
	.byte		        Cn1 , v096
	.byte	W06
	.byte	PEND
@ 026   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_9_025
@ 027   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_9_025
@ 028   ----------------------------------------
	.byte		N05   , Cn1 , v108
	.byte	W06
	.byte		        En1 , v100
	.byte	W12
	.byte		        Cn1 , v096
	.byte	W06
	.byte		        En1 , v112
	.byte	W12
	.byte		        En1 , v100
	.byte	W06
	.byte		        En1 , v112
	.byte	W06
	.byte		        Cn1 , v108
	.byte	W18
	.byte		        Cn1 , v096
	.byte	W06
	.byte		N11   , En1 , v112
	.byte	W06
	.byte		N05   , Cn1 , v108
	.byte	W12
	.byte		        Cn1 , v096
	.byte	W06
@ 029   ----------------------------------------
mus_hgss_casino_9_029:
	.byte		N05   , Cn1 , v096
	.byte	W06
	.byte		        En1 , v100
	.byte	W12
	.byte		        Cn1 , v096
	.byte	W06
	.byte		N11   , En1 , v112
	.byte	W24
	.byte		N05   , Cn1 , v096
	.byte	W18
	.byte		N05   
	.byte	W06
	.byte		N11   , En1 , v112
	.byte	W06
	.byte		N05   , Cn1 , v096
	.byte	W12
	.byte		N05   
	.byte	W06
	.byte	PEND
@ 030   ----------------------------------------
	.byte	PATT
	 .word	mus_hgss_casino_9_029
@ 031   ----------------------------------------
	.byte		N05   , Cn1 , v092
	.byte		N03   , En1 , v080
	.byte	W04
	.byte		        En1 , v092
	.byte	W04
	.byte		        En1 , v104
	.byte	W04
	.byte		N05   , En1 , v112
	.byte	W06
	.byte		        En1 , v120
	.byte	W06
	.byte		        Cn1 , v108
	.byte		N02   , Bn1 , v112
	.byte	W03
	.byte		        Bn1 , v088
	.byte	W03
	.byte		N05   , Bn1 , v112
	.byte	W06
	.byte		N03   , Cn1 , v108
	.byte		N05   , An1 , v092
	.byte	W06
	.byte		N03   , Cn1 , v108
	.byte		N05   , Fn1 , v112
	.byte	W06
	.byte		        En1 
	.byte		N17   , An2 
	.byte	W06
	.byte		N05   , En1 
	.byte	W06
	.byte		N05   
	.byte	W18
	.byte		        Cn1 , v080
	.byte	W12
	.byte		N05   
	.byte	W06
@ 032   ----------------------------------------
	.byte	W24
	.byte		        En1 , v112
	.byte	W06
	.byte		N05   
	.byte	W06
	.byte		        Cn1 , v108
	.byte	W12
	.byte		N05   
	.byte		N23   , An2 , v112
	.byte	W18
	.byte		N05   , Cn1 , v088
	.byte	W18
	.byte		        Cn1 , v100
	.byte	W12
	.byte	GOTO
	 .word	mus_hgss_casino_9_B1
mus_hgss_casino_9_B2:
@ 033   ----------------------------------------
	.byte	FINE

@******************************************************@
	.align	2

mus_hgss_casino:
	.byte	9	@ NumTrks
	.byte	0	@ NumBlks
	.byte	mus_hgss_casino_pri	@ Priority
	.byte	mus_hgss_casino_rev	@ Reverb.

	.word	mus_hgss_casino_grp

	.word	mus_hgss_casino_1
	.word	mus_hgss_casino_2
	.word	mus_hgss_casino_3
	.word	mus_hgss_casino_4
	.word	mus_hgss_casino_5
	.word	mus_hgss_casino_6
	.word	mus_hgss_casino_7
	.word	mus_hgss_casino_8
	.word	mus_hgss_casino_9

	.end
