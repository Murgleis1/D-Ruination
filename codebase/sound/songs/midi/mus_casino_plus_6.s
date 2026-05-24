	.include "MPlayDef.s"

	.equ	mus_casino_plus_6_grp, voicegroup133
	.equ	mus_casino_plus_6_pri, 0
	.equ	mus_casino_plus_6_rev, reverb_set+50
	.equ	mus_casino_plus_6_mvl, 90
	.equ	mus_casino_plus_6_key, 0
	.equ	mus_casino_plus_6_tbs, 1
	.equ	mus_casino_plus_6_exg, 1
	.equ	mus_casino_plus_6_cmp, 1

	.section .rodata
	.global	mus_casino_plus_6
	.align	2

@**************** Track 1 (Midi-Chn.1) ****************@

mus_casino_plus_6_1:
	.byte	KEYSH , mus_casino_plus_6_key+0
@ 000   ----------------------------------------
	.byte	TEMPO , 133*mus_casino_plus_6_tbs/2
	.byte	TEMPO , 133*mus_casino_plus_6_tbs/2
	.byte	TEMPO , 120*mus_casino_plus_6_tbs/2
	.byte		VOICE , 17
	.byte		VOL   , 119*mus_casino_plus_6_mvl/mxv
	.byte		PAN   , c_v+0
	.byte	W72
	.byte		N02   , Ds3 , v108
	.byte	W06
	.byte		        Ds4 , v112
	.byte	W06
	.byte		        En3 
	.byte	W05
	.byte		        En4 , v116
	.byte	W07
mus_casino_plus_6_1_B1:
@ 001   ----------------------------------------
	.byte	W96
@ 002   ----------------------------------------
	.byte	W48
	.byte		PAN   , c_v+0
	.byte	W24
	.byte		        c_v+0
	.byte		N06   , Cs4 , v127
	.byte	W06
	.byte		N05   , Dn4 
	.byte	W11
	.byte		        Ds4 
	.byte	W07
@ 003   ----------------------------------------
	.byte	W96
@ 004   ----------------------------------------
	.byte	W92
	.byte	W03
	.byte		VOICE , 46
	.byte	W01
@ 005   ----------------------------------------
mus_casino_plus_6_1_005:
	.byte		N12   , Bn3 , v100
	.byte	W12
	.byte		N11   , Cn4 , v092
	.byte	W12
	.byte		        Fn4 
	.byte	W12
	.byte		        Bn3 
	.byte	W12
	.byte		        Cn4 , v096
	.byte	W12
	.byte		        Fn4 , v092
	.byte	W12
	.byte		        Bn3 
	.byte	W12
	.byte		        Cn4 
	.byte	W12
	.byte	PEND
@ 006   ----------------------------------------
mus_casino_plus_6_1_006:
	.byte		N12   , Ds4 , v100
	.byte	W12
	.byte		N11   , Dn4 , v092
	.byte	W12
	.byte		        Cs4 
	.byte	W12
	.byte		N06   , Cs4 , v084
	.byte	W06
	.byte		N07   , Gn4 , v068
	.byte	W06
	.byte		N04   , Cs4 , v084
	.byte	W04
	.byte		        Gn4 , v040
	.byte	W05
	.byte		        Cs4 , v052
	.byte	W05
	.byte		        Gn4 
	.byte	W05
	.byte		        Cs4 , v064
	.byte	W04
	.byte		        Gn4 
	.byte	W05
	.byte		        Cs4 , v076
	.byte	W05
	.byte		        Gn4 
	.byte	W05
	.byte		        Cs4 , v088
	.byte	W05
	.byte		N06   , Gn4 
	.byte	W05
	.byte	PEND
@ 007   ----------------------------------------
mus_casino_plus_6_1_007:
	.byte		N12   , Bn3 , v116
	.byte	W12
	.byte		N11   , Cn4 , v108
	.byte	W12
	.byte		        Fn4 , v112
	.byte	W12
	.byte		        Bn3 , v108
	.byte	W12
	.byte		        Cn4 , v112
	.byte	W12
	.byte		        Fn4 , v108
	.byte	W12
	.byte		        Bn3 , v112
	.byte	W12
	.byte		        Cn4 , v108
	.byte	W12
	.byte	PEND
@ 008   ----------------------------------------
	.byte		N04   , An3 , v100
	.byte	W04
	.byte		        Ds4 , v092
	.byte	W05
	.byte		        An3 
	.byte	W05
	.byte		        Ds4 , v076
	.byte	W05
	.byte		        An3 , v072
	.byte	W04
	.byte		        Ds4 , v056
	.byte	W05
	.byte		        An3 , v064
	.byte	W05
	.byte		        Ds4 , v076
	.byte	W05
	.byte		        An3 , v100
	.byte	W05
	.byte		N06   , Ds4 , v108
	.byte	W10
	.byte		VOICE , 1
	.byte	W01
	.byte		N02   , Cn5 , v112
	.byte	W06
	.byte		        As4 
	.byte	W06
	.byte		N03   , Gn4 
	.byte	W06
	.byte		        Cn4 , v116
	.byte	W06
	.byte		N02   , As3 , v112
	.byte	W06
	.byte		        Cn4 
	.byte	W05
	.byte		        En4 
	.byte	W06
	.byte		VOICE , 46
	.byte	W01
@ 009   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_1_005
@ 010   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_1_006
@ 011   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_1_007
@ 012   ----------------------------------------
	.byte		N04   , Cs4 , v084
	.byte	W04
	.byte		        Gn4 , v076
	.byte	W04
	.byte		        Cs4 , v084
	.byte	W05
	.byte		        Gn4 , v080
	.byte	W04
	.byte		        Cs4 , v088
	.byte	W04
	.byte		        Gn4 , v084
	.byte	W05
	.byte		        Cs4 , v092
	.byte	W04
	.byte		        Gn4 , v084
	.byte	W04
	.byte		        Cs4 , v096
	.byte	W05
	.byte		        Gn4 , v088
	.byte	W04
	.byte		        Cs4 , v100
	.byte	W04
	.byte		        Gn4 , v076
	.byte	W05
	.byte		        Cs4 , v084
	.byte	W04
	.byte		        Gn4 , v080
	.byte	W05
	.byte		        Cs4 , v092
	.byte	W04
	.byte		        Gn4 , v088
	.byte	W04
	.byte		        Cs4 , v100
	.byte	W05
	.byte		        Gn4 , v096
	.byte	W04
	.byte		        Cs4 , v104
	.byte	W04
	.byte		        Gn4 , v100
	.byte	W05
	.byte		        Cs4 , v112
	.byte	W04
	.byte		        Gn4 , v108
	.byte	W04
	.byte		VOICE , 17
	.byte	W01
@ 013   ----------------------------------------
	.byte		PAN   , c_v+0
	.byte		N05   , Cn5 , v092
	.byte	W18
	.byte		N06   , Cn5 , v088
	.byte	W12
	.byte		N05   , Cn5 , v092
	.byte	W06
	.byte		        Bn4 
	.byte	W06
	.byte		N06   , Cn5 
	.byte	W06
	.byte		N04   , Cn5 , v076
	.byte		N04   , En5 , v096
	.byte	W18
	.byte		N06   , Cn5 , v092
	.byte	W18
	.byte		N05   , Bn4 
	.byte	W05
	.byte		N06   , Cn5 
	.byte	W07
@ 014   ----------------------------------------
mus_casino_plus_6_1_014:
	.byte	W12
	.byte		N02   , Cs5 , v092
	.byte	W06
	.byte		        Dn5 
	.byte	W18
	.byte		        Cs5 
	.byte	W06
	.byte		        Dn5 
	.byte	W06
	.byte		PAN   , c_v+0
	.byte	W48
	.byte	PEND
@ 015   ----------------------------------------
	.byte		        c_v+0
	.byte		N05   , Cn5 
	.byte	W18
	.byte		N06   , Cn5 , v088
	.byte	W12
	.byte		N05   , Cn5 , v092
	.byte	W06
	.byte		        Bn4 
	.byte	W06
	.byte		N06   , Cn5 
	.byte	W06
	.byte		N04   , En5 , v096
	.byte	W18
	.byte		N06   , Cn5 , v092
	.byte	W18
	.byte		N05   , En5 
	.byte	W05
	.byte		N06   , Gn5 
	.byte	W07
@ 016   ----------------------------------------
	.byte		PAN   , c_v+0
	.byte	W96
@ 017   ----------------------------------------
	.byte		        c_v+0
	.byte		N05   , Cn5 
	.byte	W18
	.byte		N06   , Cn5 , v088
	.byte	W12
	.byte		N05   , Cn5 , v092
	.byte	W06
	.byte		        Bn4 
	.byte	W06
	.byte		N06   , Cn5 
	.byte	W06
	.byte		N04   , En5 , v096
	.byte	W18
	.byte		N06   , Cn5 , v092
	.byte	W18
	.byte		N05   , Bn4 
	.byte	W05
	.byte		N06   , Cn5 
	.byte	W07
@ 018   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_1_014
@ 019   ----------------------------------------
	.byte		PAN   , c_v+0
	.byte		N05   , Cn5 , v092
	.byte	W18
	.byte		N06   , Cn5 , v088
	.byte	W12
	.byte		N05   , Cn5 , v092
	.byte	W06
	.byte		        Bn4 
	.byte	W06
	.byte		N06   , Cn5 
	.byte	W06
	.byte		N04   , En5 , v096
	.byte	W18
	.byte		N06   , Cn5 , v092
	.byte	W18
	.byte		N05   , En5 
	.byte	W05
	.byte		N06   , Gn5 
	.byte	W06
	.byte		VOICE , 1
	.byte	W01
@ 020   ----------------------------------------
	.byte	W06
	.byte		N02   , Cn5 , v084
	.byte	W03
	.byte		        Gn4 
	.byte	W03
	.byte		        As4 
	.byte	W06
	.byte		        Gn4 
	.byte	W03
	.byte		        Cn4 
	.byte	W03
	.byte		        En4 
	.byte	W06
	.byte		        Cn4 
	.byte	W03
	.byte		        Gn3 
	.byte	W03
	.byte		        As3 
	.byte	W06
	.byte		        Gn3 
	.byte	W03
	.byte		N03   , Cn3 
	.byte	W03
	.byte		N02   , En3 , v088
	.byte	W06
	.byte		        Cn3 , v084
	.byte	W06
	.byte		        As2 
	.byte	W06
	.byte		        Gn2 
	.byte	W30
	.byte	GOTO
	 .word	mus_casino_plus_6_1_B1
mus_casino_plus_6_1_B2:
@ 021   ----------------------------------------
	.byte		PAN   , c_v+0
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
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 2 (Midi-Chn.3) ****************@

mus_casino_plus_6_2:
	.byte	KEYSH , mus_casino_plus_6_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 47
	.byte		VOL   , 100*mus_casino_plus_6_mvl/mxv
	.byte	W96
mus_casino_plus_6_2_B1:
@ 001   ----------------------------------------
mus_casino_plus_6_2_001:
	.byte		N06   , Fn1 , v096
	.byte	W24
	.byte		N06   
	.byte	W24
	.byte		N06   
	.byte	W24
	.byte		N06   
	.byte	W24
	.byte	PEND
@ 002   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_2_001
@ 003   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_2_001
@ 004   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_2_001
@ 005   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_2_001
@ 006   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_2_001
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_2_001
@ 008   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_2_001
@ 009   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_2_001
@ 010   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_2_001
@ 011   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_2_001
@ 012   ----------------------------------------
	.byte	W96
@ 013   ----------------------------------------
mus_casino_plus_6_2_013:
	.byte		N06   , Fn1 , v096
	.byte	W18
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte	W18
	.byte		N06   
	.byte	W18
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte	W18
	.byte	PEND
@ 014   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_2_013
@ 015   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_2_013
@ 016   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_2_013
@ 017   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_2_013
@ 018   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_2_013
@ 019   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_2_013
@ 020   ----------------------------------------
	.byte	W96
	.byte	GOTO
	 .word	mus_casino_plus_6_2_B1
mus_casino_plus_6_2_B2:
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
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 3 (Midi-Chn.4) ****************@

mus_casino_plus_6_3:
	.byte		VOL   , 127*mus_casino_plus_6_mvl/mxv
	.byte	KEYSH , mus_casino_plus_6_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 1
	.byte	W96
mus_casino_plus_6_3_B1:
@ 001   ----------------------------------------
	.byte	W92
	.byte	W03
	.byte		VOICE , 1
	.byte	W01
@ 002   ----------------------------------------
	.byte	W72
	.byte		N05   , Fn3 , v108
	.byte	W06
	.byte		        Fs3 
	.byte	W11
	.byte		        Gn3 
	.byte	W07
@ 003   ----------------------------------------
	.byte	W96
@ 004   ----------------------------------------
	.byte	W92
	.byte	W01
	.byte		N12   , Fn3 , v116
	.byte	W02
	.byte		VOICE , 46
	.byte	W01
@ 005   ----------------------------------------
mus_casino_plus_6_3_005:
	.byte	W09
	.byte		N03   , Fn3 , v072
	.byte	W12
	.byte		N14   , Bn3 , v076
	.byte	W12
	.byte		N11   , Fn3 , v072
	.byte	W12
	.byte		N03   , Fn3 , v076
	.byte	W12
	.byte		N14   , Bn3 , v072
	.byte	W12
	.byte		N11   , Fn3 , v076
	.byte	W12
	.byte		N02   , Fn3 , v072
	.byte	W12
	.byte		N15   , An3 , v080
	.byte	W03
	.byte	PEND
@ 006   ----------------------------------------
mus_casino_plus_6_3_006:
	.byte	W09
	.byte		N14   , Gs3 , v072
	.byte	W12
	.byte		        Fn3 , v076
	.byte	W72
	.byte		N12   , Fn3 , v080
	.byte	W03
	.byte	PEND
@ 007   ----------------------------------------
mus_casino_plus_6_3_007:
	.byte	W09
	.byte		N03   , Fn3 , v092
	.byte	W12
	.byte		N14   , Bn3 
	.byte	W12
	.byte		N11   , Fn3 
	.byte	W12
	.byte		N03   , Fn3 , v096
	.byte	W12
	.byte		N14   , Bn3 , v092
	.byte	W12
	.byte		N11   , Fn3 
	.byte	W12
	.byte		N02   
	.byte	W15
	.byte	PEND
@ 008   ----------------------------------------
	.byte	W52
	.byte	W01
	.byte		VOICE , 17
	.byte	W01
	.byte		N02   , En4 , v096
	.byte	W06
	.byte		        Cn4 
	.byte	W06
	.byte		N03   , As3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		N02   , En3 
	.byte	W06
	.byte		        Gn3 
	.byte	W05
	.byte		N03   , Cn4 
	.byte	W04
	.byte		N12   , Fn3 , v080
	.byte	W02
	.byte		VOICE , 46
	.byte	W01
@ 009   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_3_005
@ 010   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_3_006
@ 011   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_3_007
@ 012   ----------------------------------------
	.byte	W92
	.byte	W03
	.byte		VOICE , 81
	.byte	W01
@ 013   ----------------------------------------
	.byte		N05   , En3 , v080
	.byte	W18
	.byte		        En3 , v072
	.byte	W12
	.byte		N05   
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        En3 
	.byte	W24
	.byte		N05   
	.byte	W18
	.byte		        Ds3 
	.byte	W05
	.byte		        En3 
	.byte	W07
@ 014   ----------------------------------------
mus_casino_plus_6_3_014:
	.byte	W12
	.byte		N02   , Gn3 , v072
	.byte	W06
	.byte		        An3 
	.byte	W18
	.byte		        Gn3 
	.byte	W06
	.byte		        An3 
	.byte	W54
	.byte	PEND
@ 015   ----------------------------------------
	.byte		N05   , En3 , v080
	.byte	W18
	.byte		        En3 , v072
	.byte	W12
	.byte		N05   
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        En3 
	.byte	W06
	.byte		N04   , Cn4 , v076
	.byte	W18
	.byte		N05   , En3 , v072
	.byte	W18
	.byte		        Gn3 
	.byte	W05
	.byte		        En4 
	.byte	W07
@ 016   ----------------------------------------
	.byte	W96
@ 017   ----------------------------------------
	.byte		        En3 , v080
	.byte	W18
	.byte		        En3 , v072
	.byte	W12
	.byte		N05   
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        En3 
	.byte	W06
	.byte		N04   , Cn4 , v076
	.byte	W18
	.byte		N05   , En3 , v072
	.byte	W18
	.byte		        Ds3 
	.byte	W05
	.byte		        En3 
	.byte	W07
@ 018   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_3_014
@ 019   ----------------------------------------
	.byte		N05   , En3 , v080
	.byte	W18
	.byte		        En3 , v072
	.byte	W12
	.byte		N05   
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        En3 
	.byte	W06
	.byte		N04   , Cn4 , v076
	.byte	W18
	.byte		N05   , En3 , v072
	.byte	W18
	.byte		        Gn3 
	.byte	W05
	.byte		        En4 
	.byte	W06
	.byte		VOICE , 1
	.byte	W01
@ 020   ----------------------------------------
	.byte	W06
	.byte		N02   , En4 , v084
	.byte	W06
	.byte		        Cn4 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        En3 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        As2 
	.byte	W54
	.byte	GOTO
	 .word	mus_casino_plus_6_3_B1
mus_casino_plus_6_3_B2:
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
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 4 (Midi-Chn.5) ****************@

mus_casino_plus_6_4:
	.byte	KEYSH , mus_casino_plus_6_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 82
	.byte		VOL   , 84*mus_casino_plus_6_mvl/mxv
	.byte	W96
mus_casino_plus_6_4_B1:
@ 001   ----------------------------------------
	.byte	W92
	.byte	W03
	.byte		VOICE , 82
	.byte	W01
@ 002   ----------------------------------------
	.byte	W48
	.byte		PAN   , c_v+0
	.byte		N04   , As2 , v088
	.byte	W04
	.byte		N03   , Cn3 , v084
	.byte	W03
	.byte		N04   , As2 , v088
	.byte	W04
	.byte		        Cn3 , v084
	.byte	W04
	.byte		N03   , As2 , v088
	.byte	W04
	.byte		N04   , Cn3 , v084
	.byte	W05
	.byte		PAN   , c_v+0
	.byte	W24
@ 003   ----------------------------------------
	.byte	W96
@ 004   ----------------------------------------
	.byte	W48
	.byte		N06   , Gs2 , v088
	.byte	W06
	.byte		        As2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Dn3 
	.byte	W06
	.byte		N22   , Ds3 , v084
	.byte	W24
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
	.byte	W92
	.byte	W03
	.byte		VOICE , 1
	.byte	W01
@ 014   ----------------------------------------
mus_casino_plus_6_4_014:
	.byte	W48
	.byte		PAN   , c_v+0
	.byte		N04   , Fn4 , v112
	.byte	W04
	.byte		N03   , Dn4 , v100
	.byte	W03
	.byte		N04   , Fn4 , v112
	.byte	W04
	.byte		        Dn4 , v100
	.byte	W04
	.byte		N03   , Fn4 , v112
	.byte	W04
	.byte		N05   , Dn4 , v100
	.byte	W05
	.byte		N04   , An3 , v112
	.byte	W04
	.byte		N03   , As3 , v100
	.byte	W03
	.byte		N04   , An3 , v112
	.byte	W04
	.byte		        As3 , v100
	.byte	W04
	.byte		N03   , An3 , v112
	.byte	W04
	.byte		N04   , As3 , v100
	.byte	W05
	.byte	PEND
@ 015   ----------------------------------------
	.byte		PAN   , c_v+0
	.byte	W96
@ 016   ----------------------------------------
	.byte		        c_v+0
	.byte		N06   , Bn4 , v120
	.byte	W06
	.byte		N05   , Cn5 , v112
	.byte	W06
	.byte		        Cs5 
	.byte	W06
	.byte		        Cn5 
	.byte	W06
	.byte		        En5 
	.byte	W06
	.byte		        Cn5 
	.byte	W06
	.byte		        Bn4 
	.byte	W06
	.byte		        Cn5 
	.byte	W06
	.byte		        En5 , v116
	.byte	W06
	.byte		        Cn5 , v112
	.byte	W06
	.byte		        Bn4 
	.byte	W06
	.byte		        Cn5 
	.byte	W06
	.byte		        En5 
	.byte	W06
	.byte		        Cn5 
	.byte	W06
	.byte		        En5 
	.byte	W05
	.byte		        Gn5 
	.byte	W07
@ 017   ----------------------------------------
	.byte		PAN   , c_v+0
	.byte	W96
@ 018   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_4_014
@ 019   ----------------------------------------
	.byte		PAN   , c_v+0
	.byte	W96
@ 020   ----------------------------------------
	.byte	W96
	.byte	GOTO
	 .word	mus_casino_plus_6_4_B1
mus_casino_plus_6_4_B2:
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
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 5 (Midi-Chn.6) ****************@

mus_casino_plus_6_5:
	.byte		VOL   , 127*mus_casino_plus_6_mvl/mxv
	.byte	KEYSH , mus_casino_plus_6_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 1
	.byte	W07
	.byte		N02   , An2 , v064
	.byte	W11
	.byte		        As2 , v068
	.byte	W12
	.byte		        Bn2 , v072
	.byte	W12
	.byte		        Cn3 , v076
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte		        Dn3 , v080
	.byte	W12
	.byte		        Ds3 , v084
	.byte	W12
	.byte		        En3 , v088
	.byte	W06
mus_casino_plus_6_5_B1:
@ 001   ----------------------------------------
	.byte	W96
@ 002   ----------------------------------------
	.byte	W96
@ 003   ----------------------------------------
	.byte	W92
	.byte	W03
	.byte		VOICE , 81
	.byte	W01
@ 004   ----------------------------------------
	.byte	W72
	.byte		N02   , Ds3 , v064
	.byte	W03
	.byte		        En3 
	.byte	W03
	.byte		        Fn3 
	.byte	W03
	.byte		        Fs3 
	.byte	W03
	.byte		        Gn3 
	.byte	W03
	.byte		        Gs3 
	.byte	W03
	.byte		        An3 
	.byte	W02
	.byte		        As3 
	.byte	W04
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
	.byte	W48
	.byte		N24   , An2 , v064, gtp2
	.byte	W24
	.byte	W02
	.byte		N03   , As2 
	.byte	W04
	.byte		        Bn2 
	.byte	W03
	.byte		        Cn3 
	.byte	W04
	.byte		        Cs3 
	.byte	W03
	.byte		        Dn3 
	.byte	W04
	.byte		        Ds3 
	.byte	W04
@ 013   ----------------------------------------
	.byte	W96
@ 014   ----------------------------------------
	.byte	W96
@ 015   ----------------------------------------
	.byte	W92
	.byte	W03
	.byte		VOICE , 2
	.byte	W01
@ 016   ----------------------------------------
	.byte	W84
	.byte		N01   , Fs1 
	.byte		N01   , Gn1 
	.byte	W01
	.byte		        Fn1 
	.byte	W01
	.byte		        En1 
	.byte	W01
	.byte		        Ds1 
	.byte	W01
	.byte		        Dn1 
	.byte	W01
	.byte		        Cs1 
	.byte	W07
@ 017   ----------------------------------------
	.byte	W96
@ 018   ----------------------------------------
	.byte	W96
@ 019   ----------------------------------------
	.byte	W96
@ 020   ----------------------------------------
	.byte	W68
	.byte	W01
	.byte		N03   , As1 
	.byte	W24
	.byte	W03
	.byte	GOTO
	 .word	mus_casino_plus_6_5_B1
mus_casino_plus_6_5_B2:
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
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 6 (Midi-Chn.7) ****************@

mus_casino_plus_6_6:
	.byte	KEYSH , mus_casino_plus_6_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 1
	.byte		VOL   , 118*mus_casino_plus_6_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		N03   , An1 , v084
	.byte	W12
	.byte		N02   , As1 , v088
	.byte	W12
	.byte		        Bn1 , v092
	.byte	W12
	.byte		        Cn2 , v096
	.byte	W12
	.byte		        Cs2 , v100
	.byte	W12
	.byte		        Dn2 , v104
	.byte	W12
	.byte		        Ds2 , v108
	.byte	W12
	.byte		        En2 , v112
	.byte	W11
	.byte		VOICE , 36
	.byte	W01
mus_casino_plus_6_6_B1:
@ 001   ----------------------------------------
	.byte		N03   , Fn1 , v124
	.byte	W06
	.byte		N02   , Fn1 , v120
	.byte	W06
	.byte		        Fn2 
	.byte	W06
	.byte		        Fn1 
	.byte	W06
	.byte		        Ds2 
	.byte	W06
	.byte		        En2 
	.byte	W12
	.byte		        Fn2 
	.byte	W06
	.byte		        Fn1 , v072
	.byte	W06
	.byte		        Fn1 , v068
	.byte	W06
	.byte		        Fn2 
	.byte	W06
	.byte		        Fn1 
	.byte	W06
	.byte		        Ds2 
	.byte	W06
	.byte		        En2 
	.byte	W11
	.byte		        Fn2 
	.byte	W07
@ 002   ----------------------------------------
	.byte		N03   , Ds1 , v088
	.byte	W06
	.byte		N02   , Ds1 , v084
	.byte	W06
	.byte		        Ds2 
	.byte	W06
	.byte		        Ds1 
	.byte	W06
	.byte		        Cs2 
	.byte	W06
	.byte		        Dn2 
	.byte	W12
	.byte		        Ds2 
	.byte	W06
	.byte		        Ds1 , v068
	.byte	W06
	.byte		        Ds1 , v064
	.byte	W06
	.byte		        Ds2 , v068
	.byte	W06
	.byte		        Ds1 , v064
	.byte	W06
	.byte		        Cs2 , v068
	.byte	W06
	.byte		        Dn2 
	.byte	W11
	.byte		        Ds2 
	.byte	W07
@ 003   ----------------------------------------
mus_casino_plus_6_6_003:
	.byte		N03   , Fn1 , v092
	.byte	W06
	.byte		N02   , Fn1 , v084
	.byte	W06
	.byte		        Fn2 
	.byte	W06
	.byte		        Fn1 
	.byte	W06
	.byte		        Ds2 
	.byte	W06
	.byte		        En2 
	.byte	W12
	.byte		        Fn2 
	.byte	W06
	.byte		        Fn1 , v088
	.byte	W06
	.byte		        Fn1 , v084
	.byte	W06
	.byte		        Fn2 
	.byte	W06
	.byte		        Fn1 
	.byte	W06
	.byte		N02   
	.byte	W06
	.byte		        Fn2 
	.byte	W06
	.byte		        En1 
	.byte	W05
	.byte		        En2 
	.byte	W07
	.byte	PEND
@ 004   ----------------------------------------
mus_casino_plus_6_6_004:
	.byte		N03   , Ds1 , v088
	.byte	W06
	.byte		N02   , Ds1 , v084
	.byte	W06
	.byte		        Ds2 
	.byte	W06
	.byte		        Ds1 
	.byte	W06
	.byte		        Cs2 
	.byte	W06
	.byte		        Dn2 
	.byte	W12
	.byte		        Ds2 
	.byte	W06
	.byte		        Ds1 , v088
	.byte	W06
	.byte		        Ds1 , v084
	.byte	W06
	.byte		        Ds2 
	.byte	W06
	.byte		        Ds1 
	.byte	W06
	.byte		N02   
	.byte	W06
	.byte		        Ds2 
	.byte	W06
	.byte		        En1 
	.byte	W05
	.byte		        En2 
	.byte	W07
	.byte	PEND
@ 005   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_6_003
@ 006   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_6_004
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_6_003
@ 008   ----------------------------------------
	.byte		N03   , Ds1 , v088
	.byte	W06
	.byte		N02   , Ds1 , v084
	.byte	W06
	.byte		        Ds2 
	.byte	W06
	.byte		        Ds1 
	.byte	W06
	.byte		        Cs2 
	.byte	W06
	.byte		        Dn2 
	.byte	W12
	.byte		        Ds2 
	.byte	W06
	.byte		N04   , Ds1 , v088
	.byte	W21
	.byte		N03   , Bn1 , v084
	.byte	W03
	.byte		N06   , Cn2 , v076
	.byte	W09
	.byte		N03   , Bn1 , v084
	.byte	W03
	.byte		N06   , Cn2 , v076
	.byte	W12
@ 009   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_6_003
@ 010   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_6_004
@ 011   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_6_003
@ 012   ----------------------------------------
	.byte		N11   , Ds1 , v088
	.byte	W12
	.byte		N05   , Ds2 , v084
	.byte	W06
	.byte		        Ds1 
	.byte	W06
	.byte		        Cs2 
	.byte	W06
	.byte		N02   , Dn2 
	.byte	W12
	.byte		        Ds2 
	.byte	W54
@ 013   ----------------------------------------
mus_casino_plus_6_6_013:
	.byte		N03   , Cn1 , v088
	.byte	W06
	.byte		N02   , Cn1 , v080
	.byte	W06
	.byte		N04   , Cn2 , v084
	.byte	W12
	.byte		N04   
	.byte	W24
	.byte		N02   , Cn1 
	.byte	W06
	.byte		        Cn1 , v080
	.byte	W06
	.byte		N04   , Cn2 , v084
	.byte	W12
	.byte		N02   
	.byte	W06
	.byte		N02   
	.byte	W18
	.byte	PEND
@ 014   ----------------------------------------
mus_casino_plus_6_6_014:
	.byte		N03   , Fn1 , v092
	.byte	W06
	.byte		N02   , Fn2 , v084
	.byte	W18
	.byte		        Fn1 
	.byte	W06
	.byte		        Fn2 
	.byte	W66
	.byte	PEND
@ 015   ----------------------------------------
	.byte		N03   , Cn1 , v088
	.byte	W06
	.byte		N02   , Cn1 , v080
	.byte	W06
	.byte		N04   , Cn2 , v084
	.byte	W12
	.byte		N04   
	.byte	W24
	.byte		N02   , Cn1 
	.byte	W06
	.byte		        Cn1 , v080
	.byte	W06
	.byte		N04   , Cn2 , v084
	.byte	W12
	.byte		N02   
	.byte	W06
	.byte		N02   
	.byte	W15
	.byte		N03   , As1 
	.byte	W03
@ 016   ----------------------------------------
	.byte		N07   , Bn1 , v100
	.byte	W09
	.byte		N03   , As1 , v084
	.byte	W03
	.byte		N07   , Bn1 , v100
	.byte	W09
	.byte		N03   , Fs1 , v084
	.byte	W03
	.byte		N07   , Gn1 , v100
	.byte	W09
	.byte		N03   , Fs1 , v084
	.byte	W03
	.byte		N07   , Gn1 , v100
	.byte	W09
	.byte		N03   , As1 , v084
	.byte	W03
	.byte		N07   , Bn1 , v100
	.byte	W09
	.byte		N03   , As1 , v084
	.byte	W03
	.byte		N06   , Bn1 , v100
	.byte	W09
	.byte		N03   , Fs1 , v084
	.byte	W03
	.byte		N05   , Gn1 , v100
	.byte	W12
	.byte		N01   , Fs1 , v084
	.byte	W03
	.byte		N02   , En1 
	.byte	W02
	.byte		N02   
	.byte	W03
	.byte		        Cs1 
	.byte	W04
@ 017   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_6_013
@ 018   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_6_014
@ 019   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_6_013
@ 020   ----------------------------------------
	.byte	W48
	.byte		N02   , Gn2 , v088
	.byte	W06
	.byte		        En2 , v084
	.byte	W03
	.byte		        Gn2 
	.byte	W03
	.byte		        Cn2 
	.byte	W06
	.byte		        As1 
	.byte	W03
	.byte		        Cn2 
	.byte	W03
	.byte		N06   , Bn1 
	.byte	W09
	.byte		N03   , As1 , v068
	.byte	W03
	.byte		N06   , Bn1 , v084
	.byte	W12
	.byte	GOTO
	 .word	mus_casino_plus_6_6_B1
mus_casino_plus_6_6_B2:
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
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 7 (Midi-Chn.8) ****************@

mus_casino_plus_6_7:
	.byte	KEYSH , mus_casino_plus_6_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 126
	.byte		VOL   , 29*mus_casino_plus_6_mvl/mxv
	.byte	W96
mus_casino_plus_6_7_B1:
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
mus_casino_plus_6_7_013:
	.byte		N10   , En4 , v068
	.byte	W12
	.byte		        En4 , v052
	.byte	W12
	.byte		        En4 , v068
	.byte	W12
	.byte		        En4 , v052
	.byte	W12
	.byte		        En4 , v068
	.byte	W12
	.byte		        En4 , v052
	.byte	W12
	.byte		        En4 , v068
	.byte	W12
	.byte		        En4 , v052
	.byte	W12
	.byte	PEND
@ 014   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_7_013
@ 015   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_7_013
@ 016   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_7_013
@ 017   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_7_013
@ 018   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_7_013
@ 019   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_7_013
@ 020   ----------------------------------------
	.byte	W96
	.byte	GOTO
	 .word	mus_casino_plus_6_7_B1
mus_casino_plus_6_7_B2:
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
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 8 (Midi-Chn.9) ****************@

mus_casino_plus_6_8:
	.byte	KEYSH , mus_casino_plus_6_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 127
	.byte		VOL   , 35*mus_casino_plus_6_mvl/mxv
	.byte	W96
mus_casino_plus_6_8_B1:
@ 001   ----------------------------------------
mus_casino_plus_6_8_001:
	.byte		N03   , Fs5 , v068
	.byte	W06
	.byte		        Fs5 , v092
	.byte	W06
	.byte		        Fs5 , v084
	.byte	W06
	.byte		        Fs5 , v076
	.byte	W06
	.byte		        Fs5 , v068
	.byte	W06
	.byte		        Fs5 , v092
	.byte	W06
	.byte		        Fs5 , v084
	.byte	W06
	.byte		        Fs5 , v076
	.byte	W06
	.byte		        Fs5 , v068
	.byte	W06
	.byte		        Fs5 , v092
	.byte	W06
	.byte		        Fs5 , v084
	.byte	W06
	.byte		        Fs5 , v076
	.byte	W06
	.byte		        Fs5 , v068
	.byte	W06
	.byte		        Fs5 , v092
	.byte	W06
	.byte		        Fs5 , v084
	.byte	W06
	.byte		        Fs5 , v076
	.byte	W06
	.byte	PEND
@ 002   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_8_001
@ 003   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_8_001
@ 004   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_8_001
@ 005   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_8_001
@ 006   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_8_001
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_8_001
@ 008   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_8_001
@ 009   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_8_001
@ 010   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_8_001
@ 011   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_8_001
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
	.byte	GOTO
	 .word	mus_casino_plus_6_8_B1
mus_casino_plus_6_8_B2:
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
@ 033   ----------------------------------------
	.byte	FINE

@**************** Track 9 (Midi-Chn.10) ****************@

mus_casino_plus_6_9:
	.byte	KEYSH , mus_casino_plus_6_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 0
	.byte		VOL   , 110*mus_casino_plus_6_mvl/mxv
	.byte		        109*mus_casino_plus_6_mvl/mxv
	.byte	W48
	.byte		N03   , En1 , v104
	.byte	W03
	.byte		        En1 , v092
	.byte	W03
	.byte		        En1 , v064
	.byte	W03
	.byte		        En1 , v040
	.byte	W03
	.byte		        En1 , v036
	.byte	W03
	.byte		        En1 , v032
	.byte	W03
	.byte		        En1 , v024
	.byte	W03
	.byte		        En1 , v020
	.byte	W03
	.byte		        En1 , v016
	.byte		N03   , An1 , v092
	.byte	W03
	.byte		        En1 , v028
	.byte	W03
	.byte		        En1 , v036
	.byte		N03   , Gn1 , v092
	.byte	W03
	.byte		        En1 , v048
	.byte	W03
	.byte		        En1 , v056
	.byte		N03   , Gn1 , v092
	.byte	W03
	.byte		        En1 , v064
	.byte	W03
	.byte		        En1 , v072
	.byte	W03
	.byte		        En1 , v084
	.byte	W03
mus_casino_plus_6_9_B1:
@ 001   ----------------------------------------
	.byte		N48   , An2 , v084
	.byte	W96
@ 002   ----------------------------------------
	.byte	W96
@ 003   ----------------------------------------
	.byte		N48   
	.byte	W96
@ 004   ----------------------------------------
	.byte	W96
@ 005   ----------------------------------------
	.byte		N48   
	.byte	W96
@ 006   ----------------------------------------
	.byte	W96
@ 007   ----------------------------------------
	.byte		N48   
	.byte	W96
@ 008   ----------------------------------------
	.byte	W42
	.byte		N06   , Ds1 
	.byte	W12
	.byte		N06   
	.byte	W06
	.byte		        Ds1 , v068
	.byte	W06
	.byte		        Ds1 , v076
	.byte	W06
	.byte		        Ds1 , v084
	.byte	W12
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte	W06
@ 009   ----------------------------------------
	.byte		N48   , An2 
	.byte	W96
@ 010   ----------------------------------------
	.byte	W96
@ 011   ----------------------------------------
	.byte		N48   
	.byte	W96
@ 012   ----------------------------------------
mus_casino_plus_6_9_012:
	.byte		N48   , An2 , v084
	.byte	W48
	.byte		N03   , En1 , v104
	.byte	W03
	.byte		        En1 , v092
	.byte	W03
	.byte		        En1 , v064
	.byte	W03
	.byte		        En1 , v040
	.byte	W03
	.byte		        En1 , v036
	.byte	W03
	.byte		        En1 , v032
	.byte	W03
	.byte		        En1 , v024
	.byte	W03
	.byte		        En1 , v020
	.byte	W03
	.byte		        En1 , v016
	.byte		N03   , An1 , v092
	.byte	W03
	.byte		        En1 , v028
	.byte	W03
	.byte		        En1 , v036
	.byte		N03   , Gn1 , v092
	.byte	W03
	.byte		        En1 , v048
	.byte	W03
	.byte		        En1 , v056
	.byte		N03   , Gn1 , v092
	.byte	W03
	.byte		        En1 , v064
	.byte	W03
	.byte		        En1 , v072
	.byte	W03
	.byte		        En1 , v084
	.byte	W03
	.byte	PEND
@ 013   ----------------------------------------
mus_casino_plus_6_9_013:
	.byte		N12   , An2 , v084
	.byte	W12
	.byte		N06   , En1 , v096
	.byte	W06
	.byte		N06   
	.byte	W18
	.byte		N06   
	.byte	W24
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte	W18
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 014   ----------------------------------------
mus_casino_plus_6_9_014:
	.byte	W12
	.byte		N06   , En1 , v108
	.byte	W06
	.byte		N06   
	.byte	W18
	.byte		N06   
	.byte	W24
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte	W18
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 015   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_9_014
@ 016   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_9_014
@ 017   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_9_013
@ 018   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_9_014
@ 019   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_9_014
@ 020   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_6_9_012
	.byte	GOTO
	 .word	mus_casino_plus_6_9_B1
mus_casino_plus_6_9_B2:
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
@ 033   ----------------------------------------
	.byte	FINE

@******************************************************@
	.align	2

mus_casino_plus_6:
	.byte	9	@ NumTrks
	.byte	0	@ NumBlks
	.byte	mus_casino_plus_6_pri	@ Priority
	.byte	mus_casino_plus_6_rev	@ Reverb.

	.word	mus_casino_plus_6_grp

	.word	mus_casino_plus_6_1
	.word	mus_casino_plus_6_2
	.word	mus_casino_plus_6_3
	.word	mus_casino_plus_6_4
	.word	mus_casino_plus_6_5
	.word	mus_casino_plus_6_6
	.word	mus_casino_plus_6_7
	.word	mus_casino_plus_6_8
	.word	mus_casino_plus_6_9

	.end
