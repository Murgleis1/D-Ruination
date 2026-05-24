	.include "MPlayDef.s"

	.equ	mus_casino_plus_5_grp, voicegroup165
	.equ	mus_casino_plus_5_pri, 0
	.equ	mus_casino_plus_5_rev, reverb_set+50
	.equ	mus_casino_plus_5_mvl, 90
	.equ	mus_casino_plus_5_key, 0
	.equ	mus_casino_plus_5_tbs, 1
	.equ	mus_casino_plus_5_exg, 1
	.equ	mus_casino_plus_5_cmp, 1

	.section .rodata
	.global	mus_casino_plus_5
	.align	2

@**************** Track 1 (Midi-Chn.1) ****************@

mus_casino_plus_5_1:
	.byte	KEYSH , mus_casino_plus_5_key+0
mus_casino_plus_5_1_B1:
@ 000   ----------------------------------------
@ 001   ----------------------------------------
@ 002   ----------------------------------------
@ 003   ----------------------------------------
@ 004   ----------------------------------------
	.byte	TEMPO , 140*mus_casino_plus_5_tbs/2
	.byte		VOICE , 48
	.byte		VOL   , 107*mus_casino_plus_5_mvl/mxv
	.byte		MOD   , 0
	.byte		PAN   , c_v+0
	.byte		N06   , Cs5 , v076
	.byte	W06
	.byte		N05   , Dn5 , v068
	.byte	W06
	.byte		        Ds5 , v072
	.byte	W06
	.byte		        En5 , v068
	.byte	W06
	.byte		TIE   , Fn5 
	.byte	W40
	.byte		MOD   , 0
	.byte	W15
	.byte		        1
	.byte	W07
	.byte		        2
	.byte	W07
	.byte		        3
	.byte	W03
@ 005   ----------------------------------------
	.byte	W05
	.byte		        4
	.byte	W07
	.byte		        5
	.byte	W07
	.byte		        6
	.byte	W08
	.byte		        7
	.byte		        8
	.byte	W68
	.byte	W01
@ 006   ----------------------------------------
	.byte	W44
	.byte	W03
	.byte		EOT   
	.byte	W02
	.byte		MOD   , 8
	.byte		        0
	.byte	W44
	.byte	W02
	.byte		VOICE , 17
	.byte	W01
@ 007   ----------------------------------------
	.byte		N05   , Fs4 
	.byte	W12
	.byte		N04   , Fn4 
	.byte	W12
	.byte		        As4 , v064
	.byte	W12
	.byte		N23   , An4 
	.byte	W24
	.byte		        Cs4 
	.byte	W23
	.byte		N11   , Cn4 
	.byte	W13
@ 008   ----------------------------------------
	.byte	W12
	.byte		N23   , As3 , v068
	.byte	W24
	.byte		N11   , An3 , v064
	.byte	W24
	.byte		N32   , Fs3 , v064, gtp3
	.byte	W36
@ 009   ----------------------------------------
	.byte		VOICE , 52
	.byte	W96
@ 010   ----------------------------------------
	.byte	W96
@ 011   ----------------------------------------
	.byte	W96
@ 012   ----------------------------------------
	.byte	W88
	.byte	W01
	.byte		N04   
	.byte	W06
	.byte		VOICE , 48
	.byte	W01
@ 013   ----------------------------------------
	.byte	W96
@ 014   ----------------------------------------
	.byte		N06   , Gn5 , v084
	.byte	W06
	.byte		TIE   , Gs5 , v076
	.byte	W24
	.byte	W01
	.byte		MOD   , 0
	.byte	W15
	.byte		        1
	.byte	W08
	.byte		        2
	.byte	W08
	.byte		        3
	.byte	W07
	.byte		        4
	.byte	W08
	.byte		        5
	.byte	W07
	.byte		        6
	.byte	W08
	.byte		        7
	.byte		        8
	.byte	W04
@ 015   ----------------------------------------
	.byte	W68
	.byte	W03
	.byte		EOT   
	.byte	W01
	.byte		MOD   , 8
	.byte		        0
	.byte		N05   , Gn5 , v096
	.byte	W06
	.byte		        Fs5 
	.byte	W05
	.byte		        Fn5 , v084
	.byte	W06
	.byte		N06   , En5 , v072
	.byte	W07
@ 016   ----------------------------------------
	.byte		N12   , Fs3 , v100
	.byte	W12
	.byte		N11   , Fn3 
	.byte	W12
	.byte		        Bn3 , v096
	.byte	W12
	.byte		TIE   , As3 
	.byte	W19
	.byte		MOD   , 0
	.byte	W03
	.byte		        1
	.byte	W03
	.byte		        2
	.byte	W03
	.byte		        3
	.byte	W03
	.byte		        4
	.byte	W03
	.byte		        5
	.byte	W03
	.byte		        6
	.byte	W03
	.byte		        7
	.byte	W03
	.byte		        8
	.byte	W17
@ 017   ----------------------------------------
	.byte	W48
	.byte		EOT   
	.byte		MOD   , 0
	.byte		N06   , An3 , v068
	.byte	W06
	.byte		N05   , Gs3 
	.byte	W06
	.byte		        Gn3 , v060
	.byte	W06
	.byte		N04   , Fs3 , v044
	.byte	W30
@ 018   ----------------------------------------
	.byte	W96
@ 019   ----------------------------------------
	.byte	W96
	.byte	GOTO
	 .word	mus_casino_plus_5_1_B1
mus_casino_plus_5_1_B2:
@ 020   ----------------------------------------
	.byte	FINE

@**************** Track 2 (Midi-Chn.2) ****************@

mus_casino_plus_5_2:
	.byte	KEYSH , mus_casino_plus_5_key+0
mus_casino_plus_5_2_B1:
@ 000   ----------------------------------------
@ 001   ----------------------------------------
@ 002   ----------------------------------------
@ 003   ----------------------------------------
@ 004   ----------------------------------------
	.byte		VOICE , 48
	.byte		VOL   , 107*mus_casino_plus_5_mvl/mxv
	.byte		MOD   , 0
	.byte		PAN   , c_v+0
	.byte		N06   , Gs4 , v060
	.byte	W06
	.byte		N05   , An4 , v056
	.byte	W06
	.byte		        As4 , v060
	.byte	W06
	.byte		        Bn4 , v056
	.byte	W06
	.byte		TIE   , Cn5 
	.byte	W40
	.byte		MOD   , 0
	.byte	W15
	.byte		        1
	.byte	W07
	.byte		        2
	.byte	W07
	.byte		        3
	.byte	W03
@ 005   ----------------------------------------
	.byte	W05
	.byte		        4
	.byte	W07
	.byte		        5
	.byte	W07
	.byte		        6
	.byte	W08
	.byte		        7
	.byte		        8
	.byte	W68
	.byte	W01
@ 006   ----------------------------------------
	.byte	W44
	.byte	W03
	.byte		EOT   
	.byte	W02
	.byte		MOD   , 8
	.byte		        0
	.byte	W44
	.byte	W02
	.byte		VOICE , 52
	.byte	W01
@ 007   ----------------------------------------
	.byte	W96
@ 008   ----------------------------------------
	.byte	W92
	.byte	W03
	.byte		N06   , Fn3 , v064
	.byte	W01
@ 009   ----------------------------------------
	.byte	W06
	.byte		N05   , Fs3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Fn3 , v068
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 , v072
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Fn3 , v076
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Fn3 , v080
	.byte	W05
	.byte		        Fs3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 , v084
	.byte	W06
	.byte		N06   , Fn3 , v096
	.byte	W01
@ 010   ----------------------------------------
	.byte	W06
	.byte		N05   , Fs3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 , v092
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Fn3 , v088
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 , v084
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Fn3 , v080
	.byte	W05
	.byte		        Fs3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 , v076
	.byte	W06
	.byte		N06   , Fn3 
	.byte	W01
@ 011   ----------------------------------------
	.byte	W06
	.byte		N05   , Fs3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 , v080
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 , v084
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Fn3 , v088
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 , v092
	.byte	W06
	.byte		        Fn3 
	.byte	W05
	.byte		        Fs3 
	.byte	W06
	.byte		        Fn3 , v096
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N06   , Fn3 , v100
	.byte	W01
@ 012   ----------------------------------------
	.byte	W06
	.byte		N05   , Fs3 , v096
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 , v092
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 , v088
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 , v084
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 , v080
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 , v076
	.byte	W06
	.byte		        Fn3 
	.byte	W05
	.byte		        Fs3 
	.byte	W06
	.byte		N06   , Fn3 , v072
	.byte	W12
	.byte		VOICE , 48
	.byte	W01
@ 013   ----------------------------------------
	.byte	W92
	.byte	W03
	.byte		N07   , Gs4 , v068
	.byte	W01
@ 014   ----------------------------------------
	.byte	W06
	.byte		TIE   , An4 , v064
	.byte	W24
	.byte	W01
	.byte		MOD   , 0
	.byte	W15
	.byte		        1
	.byte	W08
	.byte		        2
	.byte	W08
	.byte		        3
	.byte	W07
	.byte		        4
	.byte	W08
	.byte		        5
	.byte	W07
	.byte		        6
	.byte	W08
	.byte		        7
	.byte		        8
	.byte	W04
@ 015   ----------------------------------------
	.byte	W68
	.byte	W03
	.byte		EOT   
	.byte	W01
	.byte		MOD   , 8
	.byte		        0
	.byte		N06   , Gs4 , v080
	.byte	W05
	.byte		        Gn4 
	.byte	W06
	.byte		        Fs4 , v072
	.byte	W06
	.byte		N04   , Fn4 , v056
	.byte	W07
@ 016   ----------------------------------------
	.byte	W24
	.byte		N11   , Gn3 , v080
	.byte	W12
	.byte		TIE   , Fs3 
	.byte	W19
	.byte		MOD   , 0
	.byte	W03
	.byte		        1
	.byte	W03
	.byte		        2
	.byte	W03
	.byte		        3
	.byte	W03
	.byte		        4
	.byte	W03
	.byte		        5
	.byte	W03
	.byte		        6
	.byte	W03
	.byte		        7
	.byte	W03
	.byte		        8
	.byte	W17
@ 017   ----------------------------------------
	.byte	W48
	.byte		EOT   
	.byte		MOD   , 0
	.byte		N06   , Fn3 , v056
	.byte	W06
	.byte		        En3 , v052
	.byte	W06
	.byte		        Ds3 , v044
	.byte	W06
	.byte		N04   , Dn3 , v028
	.byte	W30
@ 018   ----------------------------------------
	.byte	W96
@ 019   ----------------------------------------
	.byte	W96
	.byte	GOTO
	 .word	mus_casino_plus_5_2_B1
mus_casino_plus_5_2_B2:
@ 020   ----------------------------------------
	.byte	FINE

@**************** Track 3 (Midi-Chn.3) ****************@

mus_casino_plus_5_3:
	.byte		VOL   , 127*mus_casino_plus_5_mvl/mxv
	.byte	KEYSH , mus_casino_plus_5_key+0
mus_casino_plus_5_3_B1:
@ 000   ----------------------------------------
@ 001   ----------------------------------------
@ 002   ----------------------------------------
@ 003   ----------------------------------------
@ 004   ----------------------------------------
	.byte		VOICE , 52
	.byte		N11   , Bn1 , v068
	.byte	W48
	.byte		N09   , Bn1 , v064
	.byte	W44
	.byte	W03
	.byte		N10   , Bn1 , v068
	.byte	W01
@ 005   ----------------------------------------
	.byte	W48
	.byte		N11   , Bn1 , v064
	.byte	W44
	.byte	W03
	.byte		N12   , Bn1 , v068
	.byte	W01
@ 006   ----------------------------------------
	.byte	W48
	.byte		N11   , Bn1 , v064
	.byte	W44
	.byte	W03
	.byte		N10   , Bn1 , v068
	.byte	W01
@ 007   ----------------------------------------
	.byte	W48
	.byte		N09   , Bn1 , v064
	.byte	W44
	.byte	W03
	.byte		N12   , Bn1 , v068
	.byte	W01
@ 008   ----------------------------------------
mus_casino_plus_5_3_008:
	.byte	W48
	.byte		N09   , Bn1 , v064
	.byte	W44
	.byte	W03
	.byte		N10   , Bn1 , v068
	.byte	W01
	.byte	PEND
@ 009   ----------------------------------------
	.byte	W48
	.byte		N11   
	.byte	W44
	.byte	W03
	.byte		N10   , Dn2 , v080
	.byte	W01
@ 010   ----------------------------------------
	.byte	W48
	.byte		N09   , Dn2 , v064
	.byte	W44
	.byte	W03
	.byte		N12   , Bn1 , v052
	.byte	W01
@ 011   ----------------------------------------
	.byte	W48
	.byte		N09   , Bn1 , v060
	.byte	W44
	.byte	W03
	.byte		N10   , Dn2 , v080
	.byte	W01
@ 012   ----------------------------------------
	.byte	W48
	.byte		N09   , Dn2 , v072
	.byte	W44
	.byte	W03
	.byte		N12   , Bn1 , v068
	.byte	W01
@ 013   ----------------------------------------
	.byte	W48
	.byte		N09   , Bn1 , v064
	.byte	W44
	.byte	W03
	.byte		N12   , Bn1 , v080
	.byte	W01
@ 014   ----------------------------------------
	.byte	W48
	.byte		N11   , Bn1 , v084
	.byte	W44
	.byte	W03
	.byte		N12   , Bn1 , v092
	.byte	W01
@ 015   ----------------------------------------
	.byte	W48
	.byte		N11   , Bn1 , v100
	.byte	W44
	.byte	W03
	.byte		N10   , Bn1 , v096
	.byte	W01
@ 016   ----------------------------------------
	.byte	W48
	.byte		N09   , Bn1 , v088
	.byte	W44
	.byte	W03
	.byte		N10   , Bn1 , v068
	.byte	W01
@ 017   ----------------------------------------
	.byte	W48
	.byte		N09   , Bn1 , v064
	.byte	W24
	.byte		N24   , Fs1 , v088
	.byte	W23
	.byte		N14   , Bn1 , v060
	.byte	W01
@ 018   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_5_3_008
@ 019   ----------------------------------------
	.byte	W48
	.byte		N09   , Bn1 , v064
	.byte	W24
	.byte		N05   , Bn1 , v104
	.byte	W05
	.byte		        As1 
	.byte	W06
	.byte		        Gn1 
	.byte	W06
	.byte		        Fs1 
	.byte	W07
	.byte	GOTO
	 .word	mus_casino_plus_5_3_B1
mus_casino_plus_5_3_B2:
@ 020   ----------------------------------------
	.byte	FINE

@**************** Track 4 (Midi-Chn.4) ****************@

mus_casino_plus_5_4:
	.byte	KEYSH , mus_casino_plus_5_key+0
mus_casino_plus_5_4_B1:
@ 000   ----------------------------------------
@ 001   ----------------------------------------
@ 002   ----------------------------------------
@ 003   ----------------------------------------
@ 004   ----------------------------------------
	.byte		VOICE , 7
	.byte		VOL   , 94*mus_casino_plus_5_mvl/mxv
	.byte	W12
	.byte		N04   , Bn1 , v068
	.byte	W11
	.byte		        Dn2 , v064
	.byte	W12
	.byte		        Fn2 
	.byte	W60
	.byte	W01
@ 005   ----------------------------------------
	.byte	W56
	.byte	W03
	.byte		N05   , Dn2 
	.byte	W06
	.byte		        Cs2 
	.byte	W06
	.byte		        Dn2 
	.byte	W06
	.byte		        Cs2 
	.byte	W06
	.byte		        Dn2 
	.byte	W06
	.byte		        Cs2 
	.byte	W07
@ 006   ----------------------------------------
	.byte	W12
	.byte		        Fn1 , v068
	.byte	W05
	.byte		        Fs1 , v064
	.byte	W06
	.byte		        Gn1 
	.byte	W06
	.byte		        Gs1 
	.byte	W30
	.byte		        Fn2 
	.byte	W06
	.byte		        Fs2 
	.byte	W06
	.byte		        Gn2 
	.byte	W06
	.byte		        Gs2 
	.byte	W19
@ 007   ----------------------------------------
	.byte	W96
@ 008   ----------------------------------------
mus_casino_plus_5_4_008:
	.byte	W12
	.byte		N04   , Bn1 , v068
	.byte	W11
	.byte		        Dn2 , v064
	.byte	W12
	.byte		        Fn2 
	.byte	W60
	.byte	W01
	.byte	PEND
@ 009   ----------------------------------------
	.byte	W56
	.byte	W03
	.byte		N05   , Dn2 , v072
	.byte	W06
	.byte		        Cs2 
	.byte	W06
	.byte		        Dn2 
	.byte	W06
	.byte		        Cs2 
	.byte	W06
	.byte		        Dn2 , v076
	.byte	W06
	.byte		        Cs2 
	.byte	W07
@ 010   ----------------------------------------
	.byte	W96
@ 011   ----------------------------------------
	.byte	W12
	.byte		N04   , Bn1 , v048
	.byte	W11
	.byte		        Dn2 , v052
	.byte	W72
	.byte	W01
@ 012   ----------------------------------------
	.byte	W96
@ 013   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_5_4_008
@ 014   ----------------------------------------
	.byte	W12
	.byte		N04   , Bn1 , v076
	.byte	W11
	.byte		        Dn2 , v080
	.byte	W12
	.byte		        As1 
	.byte	W24
	.byte		        Bn1 , v084
	.byte	W12
	.byte		        Dn2 , v088
	.byte	W12
	.byte		        As1 
	.byte	W13
@ 015   ----------------------------------------
	.byte	W12
	.byte		        Bn1 , v092
	.byte	W11
	.byte		        Dn2 , v096
	.byte	W12
	.byte		        As1 
	.byte	W24
	.byte		        Bn1 , v088
	.byte	W12
	.byte		        Dn2 
	.byte	W12
	.byte		        As1 
	.byte	W12
	.byte		N12   , Dn2 
	.byte	W01
@ 016   ----------------------------------------
	.byte	W12
	.byte		N11   , Cs2 , v084
	.byte	W84
@ 017   ----------------------------------------
	.byte	W96
@ 018   ----------------------------------------
	.byte	W96
@ 019   ----------------------------------------
	.byte	W68
	.byte	W03
	.byte		N05   , Bn1 , v104
	.byte	W06
	.byte		        As1 
	.byte	W06
	.byte		        Gn1 
	.byte	W06
	.byte		        Fs1 
	.byte	W07
	.byte	GOTO
	 .word	mus_casino_plus_5_4_B1
mus_casino_plus_5_4_B2:
@ 020   ----------------------------------------
	.byte	FINE

@******************************************************@
	.align	2

mus_casino_plus_5:
	.byte	4	@ NumTrks
	.byte	0	@ NumBlks
	.byte	mus_casino_plus_5_pri	@ Priority
	.byte	mus_casino_plus_5_rev	@ Reverb.

	.word	mus_casino_plus_5_grp

	.word	mus_casino_plus_5_1
	.word	mus_casino_plus_5_2
	.word	mus_casino_plus_5_3
	.word	mus_casino_plus_5_4

	.end
