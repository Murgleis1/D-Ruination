	.include "MPlayDef.s"

	.equ	mus_casino_plus_1_grp, voicegroup191
	.equ	mus_casino_plus_1_pri, 0
	.equ	mus_casino_plus_1_rev, reverb_set+50
	.equ	mus_casino_plus_1_mvl, 90
	.equ	mus_casino_plus_1_key, 0
	.equ	mus_casino_plus_1_tbs, 1
	.equ	mus_casino_plus_1_exg, 1
	.equ	mus_casino_plus_1_cmp, 1

	.section .rodata
	.global	mus_casino_plus_1
	.align	2

@**************** Track 1 (Midi-Chn.1) ****************@

mus_casino_plus_1_1:
	.byte	KEYSH , mus_casino_plus_1_key+0
@ 000   ----------------------------------------
	.byte	TEMPO , 130*mus_casino_plus_1_tbs/2
	.byte		VOICE , 60
	.byte		VOL   , 121*mus_casino_plus_1_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		BEND  , c_v+0
	.byte		N08   , Cs3 , v088
	.byte	W08
	.byte		N07   , An2 
	.byte	W08
	.byte		        Cs3 
	.byte	W08
	.byte		N04   , Cs3 , v076
	.byte	W24
	.byte		N07   , Cs3 , v088
	.byte	W08
	.byte		        As2 
	.byte	W08
	.byte		        Cs3 
	.byte	W08
	.byte		N04   , Cs3 , v076
	.byte	W24
@ 001   ----------------------------------------
	.byte		VOICE , 1
	.byte	W24
	.byte		N14   , Fs3 
	.byte	W15
	.byte		N08   , Gs3 , v116
	.byte	W24
	.byte		N23   , Bn2 , v127
	.byte	W32
	.byte	W01
mus_casino_plus_1_1_B1:
@ 002   ----------------------------------------
	.byte		VOICE , 48
	.byte	W24
	.byte		N14   , An3 , v076
	.byte	W15
	.byte		N08   , En3 , v072
	.byte	W09
	.byte		N14   , An3 , v076
	.byte	W15
	.byte		N08   , Bn3 
	.byte	W09
	.byte		N14   , Cn4 , v072
	.byte	W15
	.byte		BEND  , c_v+0
	.byte		        c_v-14
	.byte		        c_v-13
	.byte		        c_v-12
	.byte		N32   , Cs4 , v108, gtp1
	.byte	W01
	.byte		BEND  , c_v-11
	.byte		        c_v-10
	.byte	W01
	.byte		        c_v-9
	.byte		        c_v-8
	.byte		        c_v-7
	.byte	W01
	.byte		        c_v-6
	.byte		        c_v-5
	.byte		        c_v-4
	.byte	W01
	.byte		        c_v-3
	.byte		        c_v-2
	.byte	W01
	.byte		        c_v-1
	.byte		        c_v+0
	.byte	W04
@ 003   ----------------------------------------
mus_casino_plus_1_1_003:
	.byte	W36
	.byte	W03
	.byte		N08   , Cs4 , v076
	.byte	W09
	.byte		N14   , Dn4 , v072
	.byte	W15
	.byte		N07   , En4 , v108
	.byte	W23
	.byte		N01   , Dn4 , v076
	.byte	W01
	.byte		N32   , En4 , v084, gtp1
	.byte	W09
	.byte	PEND
@ 004   ----------------------------------------
mus_casino_plus_1_1_004:
	.byte	W24
	.byte		N14   , Dn4 , v084
	.byte	W24
	.byte		        An3 , v072
	.byte	W15
	.byte		N07   , Fs3 , v100
	.byte	W23
	.byte		N01   , Bn3 , v076
	.byte	W01
	.byte		N07   , Cs4 , v084
	.byte	W09
	.byte	PEND
@ 005   ----------------------------------------
	.byte	W16
	.byte		N08   , Cs4 , v100
	.byte	W08
	.byte		N14   , Cn4 , v084
	.byte	W15
	.byte		N32   , Bn3 , v108
	.byte	W56
	.byte	W01
@ 006   ----------------------------------------
	.byte	W24
	.byte		N14   , An3 , v076
	.byte	W15
	.byte		N08   , En3 , v072
	.byte	W09
	.byte		N14   , An3 , v076
	.byte	W15
	.byte		N08   , Bn3 , v084
	.byte	W09
	.byte		N14   , Cn4 , v076
	.byte	W15
	.byte		BEND  , c_v+0
	.byte		        c_v-14
	.byte		        c_v-13
	.byte		N32   , Cs4 , v112, gtp1
	.byte	W01
	.byte		BEND  , c_v-12
	.byte		        c_v-11
	.byte		        c_v-10
	.byte	W01
	.byte		        c_v-9
	.byte		        c_v-8
	.byte		        c_v-7
	.byte	W01
	.byte		        c_v-6
	.byte		        c_v-5
	.byte	W01
	.byte		        c_v-4
	.byte		        c_v-3
	.byte		        c_v-2
	.byte	W01
	.byte		        c_v-1
	.byte		        c_v+0
	.byte	W04
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_1_003
@ 008   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_1_004
@ 009   ----------------------------------------
	.byte	W16
	.byte		N08   , Cs4 , v100
	.byte	W08
	.byte		N14   , Cn4 , v076
	.byte	W15
	.byte		N32   , Bn3 , v100
	.byte	W44
	.byte		VOICE , 60
	.byte	W04
	.byte		N08   , En3 , v076
	.byte	W09
@ 010   ----------------------------------------
	.byte		N24   , Fs3 
	.byte	W24
	.byte		N23   , An3 
	.byte	W24
	.byte		BEND  , c_v+0
	.byte		        c_v-14
	.byte		        c_v-13
	.byte		        c_v-11
	.byte		N14   , Bn3 
	.byte	W01
	.byte		BEND  , c_v-9
	.byte		        c_v-8
	.byte		        c_v-6
	.byte	W01
	.byte		        c_v-4
	.byte		        c_v-2
	.byte	W01
	.byte		        c_v-1
	.byte		        c_v+0
	.byte	W12
	.byte		N07   , An3 , v092
	.byte	W20
	.byte		N04   , En3 , v076
	.byte	W05
	.byte		N32   , Fn3 , v072
	.byte	W08
@ 011   ----------------------------------------
	.byte	W24
	.byte		N14   , An3 , v076
	.byte	W15
	.byte		BEND  , c_v+0
	.byte		        c_v-14
	.byte		N23   , Bn3 
	.byte	W01
	.byte		BEND  , c_v-13
	.byte		        c_v-11
	.byte		        c_v-9
	.byte	W01
	.byte		        c_v-8
	.byte		        c_v-6
	.byte	W01
	.byte		        c_v-4
	.byte		        c_v-2
	.byte		        c_v-1
	.byte		        c_v+0
	.byte	W21
	.byte		N07   , An3 , v092
	.byte	W20
	.byte		N04   , Bn3 , v076
	.byte	W05
	.byte		N32   , Cs4 , v072
	.byte	W08
@ 012   ----------------------------------------
	.byte	W24
	.byte		N23   , Cs4 , v084
	.byte	W24
	.byte		N14   , Cs4 , v076
	.byte	W15
	.byte		N08   , Cn4 
	.byte	W09
	.byte		N14   , Cs4 
	.byte	W15
	.byte		N08   , As3 , v096
	.byte	W09
@ 013   ----------------------------------------
	.byte	W13
	.byte		N01   , Dn4 , v076
	.byte	W02
	.byte		N24   , En4 
	.byte	W24
	.byte		N23   , Dn4 , v092
	.byte	W24
	.byte		N16   , Cs4 
	.byte	W23
	.byte		N01   , Gs3 , v076
	.byte	W01
	.byte		N32   , Cs4 , v092, gtp1
	.byte	W09
@ 014   ----------------------------------------
	.byte	W24
	.byte		N14   , An3 , v076
	.byte	W15
	.byte		N08   , Fs3 
	.byte	W09
	.byte		N14   , An3 
	.byte	W15
	.byte		N07   , Fs3 , v072
	.byte	W22
	.byte		N01   , Cn4 , v076
	.byte	W02
	.byte		N24   , Cs4 , v092, gtp2
	.byte	W09
@ 015   ----------------------------------------
	.byte	W17
	.byte		N02   , Dn4 , v076
	.byte	W03
	.byte		N03   , Cs4 
	.byte	W04
	.byte		N15   , An3 
	.byte	W15
	.byte		N08   , Fs3 
	.byte	W09
	.byte		N14   , An3 
	.byte	W15
	.byte		N07   , Fs3 , v072
	.byte	W23
	.byte		N01   , Cn4 , v076
	.byte	W01
	.byte		N24   , Cs4 , v092
	.byte	W09
@ 016   ----------------------------------------
	.byte	W16
	.byte		N08   , En3 , v076
	.byte	W08
	.byte		N23   , Cs4 , v072
	.byte	W24
	.byte		N14   , Cs4 , v080
	.byte	W15
	.byte		N08   , En3 , v076
	.byte	W09
	.byte		N14   , Cs4 
	.byte	W15
	.byte		N56   , Bn3 , v112
	.byte	W09
@ 017   ----------------------------------------
	.byte	W96
	.byte	GOTO
	 .word	mus_casino_plus_1_1_B1
mus_casino_plus_1_1_B2:
@ 018   ----------------------------------------
	.byte	FINE

@**************** Track 2 (Midi-Chn.2) ****************@

mus_casino_plus_1_2:
	.byte	KEYSH , mus_casino_plus_1_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 56
	.byte		VOL   , 110*mus_casino_plus_1_mvl/mxv
	.byte		N08   , Cs4 , v088
	.byte	W08
	.byte		N07   , An3 
	.byte	W08
	.byte		        Cs4 
	.byte	W08
	.byte		N04   , Cs4 , v076
	.byte	W24
	.byte		N07   , Cs4 , v088
	.byte	W08
	.byte		        As3 
	.byte	W08
	.byte		        Cs4 
	.byte	W08
	.byte		N04   , Cs4 , v076
	.byte	W24
@ 001   ----------------------------------------
	.byte		VOICE , 48
	.byte		N15   , Cs5 , v088
	.byte	W15
	.byte		N08   , An4 
	.byte	W09
	.byte		N14   , Cs5 , v092
	.byte	W15
	.byte		N08   , Bn4 , v127
	.byte	W24
	.byte		N02   , Cs5 , v048
	.byte	W03
	.byte		VOICE , 46
	.byte		N02   , Cn5 , v040
	.byte	W02
	.byte		        Bn4 
	.byte	W03
	.byte		        As4 , v036
	.byte	W02
	.byte		        An4 , v032
	.byte	W03
	.byte		        Gs4 , v028
	.byte	W02
	.byte		        Gn4 
	.byte	W02
	.byte		        Fs4 , v024
	.byte	W03
	.byte		        Fn4 
	.byte	W02
	.byte		        En4 , v020
	.byte	W02
	.byte		        Ds4 , v016
	.byte	W03
	.byte		        Dn4 
	.byte	W02
	.byte		        Cs4 , v012
	.byte	W04
mus_casino_plus_1_2_B1:
@ 002   ----------------------------------------
	.byte	W23
	.byte		VOICE , 9
	.byte	W01
	.byte		N14   , An4 , v060
	.byte	W15
	.byte		N08   , En4 , v056
	.byte	W09
	.byte		N14   , An4 , v060
	.byte	W15
	.byte		N08   , Bn4 
	.byte	W09
	.byte		N14   , Cn5 , v056
	.byte	W15
	.byte		        Cs5 , v092
	.byte	W09
@ 003   ----------------------------------------
mus_casino_plus_1_2_003:
	.byte	W36
	.byte	W03
	.byte		N08   , Cs5 , v060
	.byte	W09
	.byte		N14   , Dn5 , v056
	.byte	W15
	.byte		N07   , En5 , v092
	.byte	W32
	.byte	W01
	.byte	PEND
@ 004   ----------------------------------------
	.byte	W96
@ 005   ----------------------------------------
	.byte	W96
@ 006   ----------------------------------------
	.byte	W24
	.byte		N14   , An4 , v060
	.byte	W15
	.byte		N08   , En4 , v056
	.byte	W09
	.byte		N14   , An4 , v060
	.byte	W15
	.byte		N08   , Bn4 , v064
	.byte	W09
	.byte		N14   , Cn5 , v060
	.byte	W15
	.byte		N16   , Cs5 , v096
	.byte	W09
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_2_003
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
	.byte	GOTO
	 .word	mus_casino_plus_1_2_B1
mus_casino_plus_1_2_B2:
@ 018   ----------------------------------------
	.byte	FINE

@**************** Track 3 (Midi-Chn.3) ****************@

mus_casino_plus_1_3:
	.byte	KEYSH , mus_casino_plus_1_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 56
	.byte		VOL   , 107*mus_casino_plus_1_mvl/mxv
	.byte	W96
@ 001   ----------------------------------------
	.byte	W96
mus_casino_plus_1_3_B1:
@ 002   ----------------------------------------
	.byte	W96
@ 003   ----------------------------------------
	.byte	W96
@ 004   ----------------------------------------
	.byte	W96
@ 005   ----------------------------------------
	.byte	W96
@ 006   ----------------------------------------
	.byte	W24
	.byte		N14   , Cs3 , v084
	.byte	W36
	.byte	W03
	.byte		N08   , Dn3 , v068
	.byte	W09
	.byte		N14   , Ds3 , v064
	.byte	W15
	.byte		N32   , En3 , v100, gtp1
	.byte	W09
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
	.byte	W03
	.byte		N07   , Fs3 , v084
	.byte	W09
@ 013   ----------------------------------------
	.byte	W15
	.byte		N24   , Cs4 , v064
	.byte	W24
	.byte		N23   , Bn3 , v080
	.byte	W24
	.byte		N22   , As3 
	.byte	W24
	.byte		N32   , An3 , v084, gtp1
	.byte	W09
@ 014   ----------------------------------------
	.byte	W84
	.byte	W03
	.byte		N24   , An3 , v084, gtp2
	.byte	W09
@ 015   ----------------------------------------
	.byte	W84
	.byte	W03
	.byte		N23   
	.byte	W09
@ 016   ----------------------------------------
	.byte	W24
	.byte		        An3 , v064
	.byte	W24
	.byte		N14   , An3 , v068
	.byte	W24
	.byte		        An3 , v064
	.byte	W15
	.byte		N56   , Gs3 , v100
	.byte	W09
@ 017   ----------------------------------------
	.byte	W96
	.byte	GOTO
	 .word	mus_casino_plus_1_3_B1
mus_casino_plus_1_3_B2:
@ 018   ----------------------------------------
	.byte	FINE

@**************** Track 4 (Midi-Chn.4) ****************@

mus_casino_plus_1_4:
	.byte	KEYSH , mus_casino_plus_1_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 46
	.byte		VOL   , 109*mus_casino_plus_1_mvl/mxv
	.byte	W24
	.byte		N03   , An3 , v092
	.byte	W08
	.byte		N07   , Cs4 , v088
	.byte	W08
	.byte		N04   , An4 , v084
	.byte	W32
	.byte		N03   , As3 , v092
	.byte	W08
	.byte		N07   , Cs4 , v088
	.byte	W07
	.byte		N03   , An3 
	.byte	W02
	.byte		VOICE , 56
	.byte	W02
	.byte		N04   , Bn3 
	.byte	W05
@ 001   ----------------------------------------
	.byte		N15   , Cs4 
	.byte	W16
	.byte		N08   , An3 
	.byte	W08
	.byte		N14   , Cs4 , v092
	.byte	W15
	.byte		N08   , Bn3 , v127
	.byte	W56
	.byte	W01
mus_casino_plus_1_4_B1:
@ 002   ----------------------------------------
	.byte	W96
@ 003   ----------------------------------------
	.byte		VOICE , 48
	.byte	W84
	.byte	W03
	.byte		N32   , Cs5 , v092, gtp1
	.byte	W03
	.byte		VOICE , 48
	.byte	W06
@ 004   ----------------------------------------
	.byte	W24
	.byte		N14   , An4 , v084
	.byte	W15
	.byte		N08   , Fs4 , v088
	.byte	W09
	.byte		N15   , En4 
	.byte	W15
	.byte		N08   , Dn4 , v112
	.byte	W09
	.byte		VOICE , 1
	.byte	W15
	.byte		N08   , En4 , v092
	.byte	W09
@ 005   ----------------------------------------
	.byte	W16
	.byte		        En4 , v108
	.byte	W23
	.byte		N08   
	.byte	W09
	.byte		N14   , Fs4 , v080
	.byte	W15
	.byte		N07   , An4 , v088
	.byte	W09
	.byte		N14   , Bn4 , v084
	.byte	W15
	.byte		N05   , An4 , v088
	.byte	W05
	.byte		N03   , Bn4 , v076
	.byte	W04
@ 006   ----------------------------------------
	.byte		N24   , Cs5 , v072
	.byte	W96
@ 007   ----------------------------------------
	.byte		VOICE , 48
	.byte	W68
	.byte	W03
	.byte		        73
	.byte	W16
	.byte		N32   , Cs5 , v092, gtp1
	.byte	W09
@ 008   ----------------------------------------
	.byte	W24
	.byte		N14   , An4 , v084
	.byte	W15
	.byte		N08   , Fs4 , v088
	.byte	W09
	.byte		N15   , En4 
	.byte	W15
	.byte		N08   , Dn4 , v112
	.byte	W08
	.byte		VOICE , 48
	.byte	W16
	.byte		N08   , En4 , v092
	.byte	W09
@ 009   ----------------------------------------
	.byte	W16
	.byte		        En4 , v112
	.byte	W08
	.byte		N14   , Ds4 , v092
	.byte	W15
	.byte		N32   , Dn4 , v112
	.byte	W56
	.byte	W01
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
	.byte	W92
	.byte	W03
	.byte		VOICE , 46
	.byte	W01
@ 017   ----------------------------------------
	.byte	W48
	.byte		N07   , Gs3 , v076
	.byte	W08
	.byte		N04   , Bn3 , v072
	.byte	W08
	.byte		N03   , En4 , v076
	.byte	W08
	.byte		N07   , Gs4 
	.byte	W08
	.byte		N04   , Bn4 , v072
	.byte	W07
	.byte		N03   , En5 , v088
	.byte	W09
	.byte	GOTO
	 .word	mus_casino_plus_1_4_B1
mus_casino_plus_1_4_B2:
@ 018   ----------------------------------------
	.byte	FINE

@**************** Track 5 (Midi-Chn.5) ****************@

mus_casino_plus_1_5:
	.byte	KEYSH , mus_casino_plus_1_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 45
	.byte		VOL   , 97*mus_casino_plus_1_mvl/mxv
	.byte	W96
@ 001   ----------------------------------------
	.byte	W96
mus_casino_plus_1_5_B1:
@ 002   ----------------------------------------
mus_casino_plus_1_5_002:
	.byte	W16
	.byte		N03   , En3 , v092
	.byte	W44
	.byte	W03
	.byte		N03   
	.byte	W24
	.byte		N03   
	.byte	W09
	.byte	PEND
@ 003   ----------------------------------------
mus_casino_plus_1_5_003:
	.byte	W16
	.byte		N03   , Fs3 , v092
	.byte	W44
	.byte	W03
	.byte		N03   
	.byte	W32
	.byte	W01
	.byte	PEND
@ 004   ----------------------------------------
mus_casino_plus_1_5_004:
	.byte	W16
	.byte		N03   , Fs3 , v092
	.byte	W44
	.byte	W03
	.byte		        Dn3 
	.byte	W32
	.byte	W01
	.byte	PEND
@ 005   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_5_002
@ 006   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_5_002
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_5_003
@ 008   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_5_004
@ 009   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_5_002
@ 010   ----------------------------------------
	.byte	W16
	.byte		N03   , An3 , v092
	.byte	W44
	.byte	W03
	.byte		N03   
	.byte	W24
	.byte		N03   
	.byte	W09
@ 011   ----------------------------------------
	.byte	W16
	.byte		N03   
	.byte	W44
	.byte	W03
	.byte		N03   
	.byte	W24
	.byte		        Gs3 
	.byte	W09
@ 012   ----------------------------------------
	.byte	W16
	.byte		N03   
	.byte	W44
	.byte	W03
	.byte		        An3 
	.byte	W32
	.byte	W01
@ 013   ----------------------------------------
	.byte	W15
	.byte		        As3 , v088
	.byte	W80
	.byte	W01
@ 014   ----------------------------------------
mus_casino_plus_1_5_014:
	.byte	W16
	.byte		N03   , An3 , v092
	.byte	W44
	.byte	W03
	.byte		N03   
	.byte	W32
	.byte	W01
	.byte	PEND
@ 015   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_5_014
@ 016   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_5_014
@ 017   ----------------------------------------
	.byte	W15
	.byte		N03   , Gs3 , v088
	.byte	W24
	.byte		        An3 , v092
	.byte	W24
	.byte		        Bn3 
	.byte	W24
	.byte		N02   , Dn4 
	.byte	W09
	.byte	GOTO
	 .word	mus_casino_plus_1_5_B1
mus_casino_plus_1_5_B2:
@ 018   ----------------------------------------
	.byte	FINE

@**************** Track 6 (Midi-Chn.6) ****************@

mus_casino_plus_1_6:
	.byte	KEYSH , mus_casino_plus_1_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 33
	.byte		VOL   , 107*mus_casino_plus_1_mvl/mxv
	.byte		N03   , An1 , v092
	.byte	W18
	.byte		N07   , En1 , v088
	.byte	W06
	.byte		N13   , An1 , v084
	.byte	W24
	.byte		N03   , As1 , v092
	.byte	W18
	.byte		N07   , En1 , v088
	.byte	W06
	.byte		N13   , As1 , v084
	.byte	W24
@ 001   ----------------------------------------
	.byte		N06   , Bn1 , v092
	.byte	W06
	.byte		N07   , Bn1 , v088
	.byte	W12
	.byte		N06   , Fs1 
	.byte	W06
	.byte		N07   , Fs1 , v100
	.byte	W06
	.byte		        Dn2 , v088
	.byte	W12
	.byte		        En1 , v124
	.byte	W24
	.byte		N23   , En2 , v116
	.byte	W24
	.byte		N06   , En1 , v088
	.byte	W06
mus_casino_plus_1_6_B1:
@ 002   ----------------------------------------
	.byte		N15   , An1 , v072
	.byte	W15
	.byte		N03   , Cs3 , v080
	.byte	W09
	.byte		N23   , Cs1 , v084
	.byte	W24
	.byte		N14   , En1 , v080
	.byte	W15
	.byte		N03   , Cs3 
	.byte	W09
	.byte		N14   , Fn1 , v084
	.byte	W15
	.byte		N03   , Cs3 , v080
	.byte	W09
@ 003   ----------------------------------------
mus_casino_plus_1_6_003:
	.byte		N15   , Fs1 , v080
	.byte	W15
	.byte		N03   , En3 
	.byte	W09
	.byte		N23   , Cs2 , v084
	.byte	W24
	.byte		N14   , As1 , v080
	.byte	W15
	.byte		N03   , En3 
	.byte	W09
	.byte		N23   , Fs1 , v084
	.byte	W24
	.byte	PEND
@ 004   ----------------------------------------
mus_casino_plus_1_6_004:
	.byte		N15   , Bn1 , v080
	.byte	W15
	.byte		N03   , Dn3 
	.byte	W09
	.byte		N23   , Dn1 , v084
	.byte	W24
	.byte		N14   , Dn1 , v080
	.byte	W15
	.byte		N03   , Bn2 
	.byte	W09
	.byte		N23   , Ds1 , v084
	.byte	W24
	.byte	PEND
@ 005   ----------------------------------------
mus_casino_plus_1_6_005:
	.byte		N15   , En1 , v080
	.byte	W15
	.byte		N03   , Dn3 
	.byte	W09
	.byte		N23   , Bn1 , v084
	.byte	W24
	.byte		N14   , Gs1 , v080
	.byte	W15
	.byte		N03   , Dn3 
	.byte	W09
	.byte		N14   , En1 , v084
	.byte	W15
	.byte		N03   , Dn3 , v080
	.byte	W09
	.byte	PEND
@ 006   ----------------------------------------
	.byte		N15   , An1 
	.byte	W15
	.byte		N03   , Cs3 
	.byte	W09
	.byte		N23   , Cs1 , v084
	.byte	W24
	.byte		N14   , En1 , v080
	.byte	W15
	.byte		N03   , Cs3 
	.byte	W09
	.byte		N14   , Fn1 , v084
	.byte	W15
	.byte		N03   , Cs3 , v080
	.byte	W09
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_6_003
@ 008   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_6_004
@ 009   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_6_005
@ 010   ----------------------------------------
	.byte		N15   , Dn2 , v080
	.byte	W15
	.byte		N03   , Fs3 
	.byte	W09
	.byte		N23   , Dn2 , v084
	.byte	W24
	.byte		N14   , Dn2 , v080
	.byte	W15
	.byte		N03   , Fs3 
	.byte	W09
	.byte		N14   , Dn2 , v084
	.byte	W15
	.byte		N03   , Fn3 , v080
	.byte	W09
@ 011   ----------------------------------------
	.byte		N15   , Dn2 
	.byte	W15
	.byte		N03   , Fn3 
	.byte	W09
	.byte		N23   , Dn2 , v084
	.byte	W24
	.byte		N14   , Dn2 , v080
	.byte	W15
	.byte		N03   , Fn3 
	.byte	W09
	.byte		N14   , Dn2 , v084
	.byte	W15
	.byte		N03   , En3 , v080
	.byte	W09
@ 012   ----------------------------------------
	.byte		N15   , Cs2 
	.byte	W15
	.byte		N03   , En3 
	.byte	W09
	.byte		N23   , Cs2 , v084
	.byte	W24
	.byte		N14   , En2 , v080
	.byte	W15
	.byte		N03   , Fs3 
	.byte	W09
	.byte		N23   , Fn2 , v084
	.byte	W24
@ 013   ----------------------------------------
	.byte		N15   , Fs2 , v080
	.byte	W24
	.byte		N23   , Cs2 , v084
	.byte	W24
	.byte		N14   , As1 , v080
	.byte	W15
	.byte		N03   , Fs3 , v088
	.byte	W09
	.byte		N23   , Fs1 , v084
	.byte	W24
@ 014   ----------------------------------------
	.byte		N15   , Bn1 , v080
	.byte	W15
	.byte		N03   , Dn3 
	.byte	W09
	.byte		N23   , Fs1 , v084
	.byte	W24
	.byte		N14   , An1 , v080
	.byte	W15
	.byte		N03   , Fs3 
	.byte	W09
	.byte		N14   , As1 , v084
	.byte	W15
	.byte		N03   , Dn3 , v088
	.byte	W09
@ 015   ----------------------------------------
	.byte		N15   , Bn1 , v080
	.byte	W15
	.byte		N03   , Fs3 
	.byte	W09
	.byte		N23   , Fs1 , v084
	.byte	W24
	.byte		N14   , Dn2 , v080
	.byte	W15
	.byte		N03   , Fs3 
	.byte	W09
	.byte		N23   , Fs1 , v084
	.byte	W24
@ 016   ----------------------------------------
	.byte		N15   , En1 , v080
	.byte	W15
	.byte		N03   , Fs3 
	.byte	W09
	.byte		N23   , En1 , v084
	.byte	W24
	.byte		N14   , En1 , v080
	.byte	W15
	.byte		N03   , Fs3 
	.byte	W09
	.byte		N14   , En1 , v084
	.byte	W15
	.byte		N03   , Fs3 , v088
	.byte	W09
@ 017   ----------------------------------------
	.byte		N15   , En2 , v080
	.byte	W24
	.byte		N14   , En1 , v084
	.byte	W15
	.byte		N03   , Fs3 , v080
	.byte	W09
	.byte		N14   , Fs1 
	.byte	W15
	.byte		N03   , En3 
	.byte	W09
	.byte		N14   , Gs1 , v084
	.byte	W15
	.byte		N03   , Gs3 , v080
	.byte	W09
	.byte	GOTO
	 .word	mus_casino_plus_1_6_B1
mus_casino_plus_1_6_B2:
@ 018   ----------------------------------------
	.byte	FINE

@**************** Track 7 (Midi-Chn.7) ****************@

mus_casino_plus_1_7:
	.byte	KEYSH , mus_casino_plus_1_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 127
	.byte		VOL   , 75*mus_casino_plus_1_mvl/mxv
	.byte	W96
@ 001   ----------------------------------------
	.byte	W96
mus_casino_plus_1_7_B1:
@ 002   ----------------------------------------
mus_casino_plus_1_7_002:
	.byte	W16
	.byte		N04   , Gs7 , v084
	.byte	W24
	.byte		N04   
	.byte	W24
	.byte		N04   
	.byte	W24
	.byte		N04   
	.byte	W08
	.byte	PEND
@ 003   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_7_002
@ 004   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_7_002
@ 005   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_7_002
@ 006   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_7_002
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_7_002
@ 008   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_7_002
@ 009   ----------------------------------------
mus_casino_plus_1_7_009:
	.byte	W16
	.byte		N04   , Gs7 , v084
	.byte	W24
	.byte		N04   
	.byte	W48
	.byte		N04   
	.byte	W08
	.byte	PEND
@ 010   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_7_002
@ 011   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_7_002
@ 012   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_7_002
@ 013   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_7_002
@ 014   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_7_002
@ 015   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_7_002
@ 016   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_7_002
@ 017   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_7_009
	.byte	GOTO
	 .word	mus_casino_plus_1_7_B1
mus_casino_plus_1_7_B2:
@ 018   ----------------------------------------
	.byte	FINE

@**************** Track 8 (Midi-Chn.8) ****************@

mus_casino_plus_1_8:
	.byte	KEYSH , mus_casino_plus_1_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 126
	.byte		VOL   , 67*mus_casino_plus_1_mvl/mxv
	.byte	W96
@ 001   ----------------------------------------
	.byte	W96
mus_casino_plus_1_8_B1:
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
	.byte	W64
	.byte		N20   , As4 , v084
	.byte	W32
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
	.byte	W64
	.byte		N20   
	.byte	W32
	.byte	GOTO
	 .word	mus_casino_plus_1_8_B1
mus_casino_plus_1_8_B2:
@ 018   ----------------------------------------
	.byte	FINE

@**************** Track 9 (Midi-Chn.10) ****************@

mus_casino_plus_1_9:
	.byte	KEYSH , mus_casino_plus_1_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 0
	.byte		VOL   , 104*mus_casino_plus_1_mvl/mxv
	.byte		        104*mus_casino_plus_1_mvl/mxv
	.byte		N48   , An2 , v092
	.byte	W48
	.byte		N48   
	.byte	W48
@ 001   ----------------------------------------
	.byte		N48   
	.byte	W64
	.byte		N06   , En1 , v084
	.byte	W08
	.byte		N06   
	.byte	W16
	.byte		N06   
	.byte	W08
mus_casino_plus_1_9_B1:
@ 002   ----------------------------------------
mus_casino_plus_1_9_002:
	.byte		N24   , An2 , v092
	.byte	W24
	.byte		N06   , En1 , v084
	.byte	W24
	.byte		        Cn1 
	.byte	W24
	.byte		        En1 
	.byte	W16
	.byte		        Cn1 
	.byte	W08
	.byte	PEND
@ 003   ----------------------------------------
mus_casino_plus_1_9_003:
	.byte		N06   , Cn1 , v084
	.byte	W16
	.byte		N06   
	.byte	W08
	.byte		        En1 
	.byte	W16
	.byte		        Cn1 
	.byte	W08
	.byte		N06   
	.byte	W24
	.byte		        En1 
	.byte	W24
	.byte	PEND
@ 004   ----------------------------------------
mus_casino_plus_1_9_004:
	.byte		N06   , Cn1 , v084
	.byte	W24
	.byte		        En1 
	.byte	W24
	.byte		        Cn1 
	.byte	W24
	.byte		        En1 
	.byte	W16
	.byte		        Cn1 
	.byte	W08
	.byte	PEND
@ 005   ----------------------------------------
	.byte		N06   
	.byte	W16
	.byte		N06   
	.byte	W08
	.byte		        En1 
	.byte	W16
	.byte		        Cn1 
	.byte	W08
	.byte		N06   
	.byte	W24
	.byte		        En1 
	.byte	W16
	.byte		N06   
	.byte	W08
@ 006   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_9_004
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_9_003
@ 008   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_9_004
@ 009   ----------------------------------------
mus_casino_plus_1_9_009:
	.byte		N06   , Cn1 , v084
	.byte	W16
	.byte		N06   
	.byte	W08
	.byte		        En1 
	.byte	W16
	.byte		        Cn1 
	.byte	W08
	.byte		N06   
	.byte	W16
	.byte		        En1 
	.byte	W08
	.byte		N06   
	.byte	W10
	.byte		        Cn1 
	.byte	W06
	.byte		        En1 
	.byte	W08
	.byte	PEND
@ 010   ----------------------------------------
	.byte		N24   , An2 , v092
	.byte	W24
	.byte		N06   , Cn1 , v084
	.byte	W24
	.byte		N06   
	.byte	W24
	.byte		N06   
	.byte	W16
	.byte		N06   
	.byte	W08
@ 011   ----------------------------------------
	.byte		N06   
	.byte	W24
	.byte		N06   
	.byte	W24
	.byte		N06   
	.byte	W16
	.byte		        En1 
	.byte	W08
	.byte		N06   
	.byte	W16
	.byte		N06   
	.byte	W08
@ 012   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_9_002
@ 013   ----------------------------------------
mus_casino_plus_1_9_013:
	.byte		N06   , Cn1 , v084
	.byte	W16
	.byte		N06   
	.byte	W08
	.byte		        En1 
	.byte	W16
	.byte		        Cn1 
	.byte	W08
	.byte		N06   
	.byte	W24
	.byte		        En1 
	.byte	W16
	.byte		        Cn1 
	.byte	W08
	.byte	PEND
@ 014   ----------------------------------------
	.byte		        En1 
	.byte	W16
	.byte		        Cn1 
	.byte	W08
	.byte		        En1 
	.byte	W24
	.byte		        Cn1 
	.byte	W24
	.byte		        En1 
	.byte	W16
	.byte		        Cn1 
	.byte	W08
@ 015   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_9_013
@ 016   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_9_004
@ 017   ----------------------------------------
	.byte	PATT
	 .word	mus_casino_plus_1_9_009
	.byte	GOTO
	 .word	mus_casino_plus_1_9_B1
mus_casino_plus_1_9_B2:
@ 018   ----------------------------------------
	.byte	FINE

@******************************************************@
	.align	2

mus_casino_plus_1:
	.byte	9	@ NumTrks
	.byte	0	@ NumBlks
	.byte	mus_casino_plus_1_pri	@ Priority
	.byte	mus_casino_plus_1_rev	@ Reverb.

	.word	mus_casino_plus_1_grp

	.word	mus_casino_plus_1_1
	.word	mus_casino_plus_1_2
	.word	mus_casino_plus_1_3
	.word	mus_casino_plus_1_4
	.word	mus_casino_plus_1_5
	.word	mus_casino_plus_1_6
	.word	mus_casino_plus_1_7
	.word	mus_casino_plus_1_8
	.word	mus_casino_plus_1_9

	.end
