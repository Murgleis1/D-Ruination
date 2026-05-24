	.include "MPlayDef.s"

	.equ	bw_accumula_town_grp, voicegroup193
	.equ	bw_accumula_town_pri, 4
	.equ	bw_accumula_town_rev, reverb_set+50
	.equ	bw_accumula_town_mvl, 75
	.equ	bw_accumula_town_key, 0
	.equ	bw_accumula_town_tbs, 1
	.equ	bw_accumula_town_exg, 1
	.equ	bw_accumula_town_cmp, 1

	.section .rodata
	.global	bw_accumula_town
	.align	2

@**************** Track 1 (Midi-Chn.1) ****************@

bw_accumula_town_1:
	.byte	KEYSH , bw_accumula_town_key+0
bw_accumula_town_1_B1:
@ 000   ----------------------------------------
@ 001   ----------------------------------------
	.byte	TEMPO , 112*bw_accumula_town_tbs/2
	.byte		VOICE , 73
	.byte		VOL   , 120*bw_accumula_town_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		MOD   , 0
	.byte		N05   , Gs4 , v116
	.byte	W06
	.byte		        An4 , v112
	.byte	W06
	.byte		        Bn4 , v120
	.byte	W06
	.byte		N02   , An4 , v116
	.byte	W12
	.byte		N17   , Gs4 , v120
	.byte	W18
	.byte		N01   , En4 , v112
	.byte	W12
	.byte		N21   , Cs4 , v120
	.byte	W36
@ 002   ----------------------------------------
	.byte		N03   , En4 , v116
	.byte	W12
	.byte		N11   , Cs4 , v120
	.byte	W18
	.byte		N17   , Cs4 , v116
	.byte	W18
	.byte		N03   , En4 , v108
	.byte	W09
	.byte		N04   , Gs4 , v116
	.byte	W03
	.byte		N11   , An4 , v124
	.byte	W12
	.byte		N02   , Gs4 , v116
	.byte	W12
	.byte		N11   , Fs4 , v124
	.byte	W12
@ 003   ----------------------------------------
	.byte		N02   , Ds4 , v116
	.byte	W10
	.byte		        Ds4 , v108
	.byte	W02
	.byte		N05   , En4 , v124
	.byte	W18
	.byte		        En4 , v120
	.byte	W18
	.byte		        En4 , v124
	.byte	W48
@ 004   ----------------------------------------
	.byte	W96
@ 005   ----------------------------------------
	.byte		        Gs4 , v116
	.byte	W06
	.byte		        An4 , v112
	.byte	W06
	.byte		        Bn4 , v120
	.byte	W06
	.byte		N02   , An4 , v116
	.byte	W12
	.byte		N17   , Gs4 , v120
	.byte	W18
	.byte		N01   , En4 , v112
	.byte	W12
	.byte		N21   , Cs4 , v120
	.byte	W36
@ 006   ----------------------------------------
	.byte		N03   , En4 , v116
	.byte	W12
	.byte		N11   , Cs4 , v120
	.byte	W18
	.byte		N18   , Cs4 , v116
	.byte	W18
	.byte		N03   , En4 , v108
	.byte	W10
	.byte		N04   , Gs4 
	.byte	W02
	.byte		N11   , An4 , v124
	.byte	W12
	.byte		N02   , Gs4 , v116
	.byte	W12
	.byte		N11   , Fs4 , v124
	.byte	W12
@ 007   ----------------------------------------
	.byte		N02   , Bn4 , v116
	.byte	W10
	.byte		        Ds4 , v112
	.byte	W02
	.byte		N05   , En4 , v124
	.byte	W18
	.byte		        En4 , v120
	.byte	W18
	.byte		        En4 , v124
	.byte	W48
@ 008   ----------------------------------------
	.byte	W06
	.byte		N01   , Bn4 , v096
	.byte	W02
	.byte		        Cs5 , v084
	.byte	W02
	.byte		N02   , Ds5 , v100
	.byte	W02
	.byte		N05   , En5 , v104
	.byte	W18
	.byte		        En5 , v100
	.byte	W18
	.byte		        En5 , v104
	.byte	W44
	.byte	W02
	.byte		N02   , Ds4 , v112
	.byte	W02
@ 009   ----------------------------------------
	.byte		N11   , En4 , v120
	.byte	W12
	.byte		N32   , Cs4 , v120, gtp2
	.byte	W18
	.byte	W06
	.byte	W06
	.byte	W06
	.byte		N01   , En4 
	.byte	W06
	.byte		N15   , Bn4 
	.byte	W18
	.byte		N10   , An4 , v124
	.byte	W12
	.byte		N08   , Gs4 , v120
	.byte	W12
@ 010   ----------------------------------------
	.byte		N11   , Bn4 
	.byte	W12
	.byte		N23   , Gs4 
	.byte	W12
	.byte	W06
	.byte	W06
	.byte		N12   , En4 , v124
	.byte	W12
	.byte		N02   , Fs4 , v120
	.byte	W06
	.byte		N32   , En4 , v124, gtp3
	.byte	W21
	.byte	W03
	.byte	W03
	.byte	W03
	.byte	W03
	.byte	W03
	.byte	W06
@ 011   ----------------------------------------
	.byte		N11   , Dn4 , v120
	.byte	W12
	.byte		N21   , Cs4 , v116
	.byte	W12
	.byte	W06
	.byte	W06
	.byte		N09   , Ds4 , v120
	.byte	W12
	.byte		N03   , En4 , v116
	.byte	W06
	.byte		N15   , Cn4 , v124
	.byte	W18
	.byte		N10   , Ds4 , v116
	.byte	W12
	.byte		N11   , En4 , v124
	.byte	W12
@ 012   ----------------------------------------
	.byte		N06   , Fs4 , v116
	.byte	W12
	.byte		N22   , Fs4 , v124
	.byte	W12
	.byte	W06
	.byte	W06
	.byte		N11   , En4 , v120
	.byte	W12
	.byte		N01   , Fs4 , v112
	.byte	W06
	.byte		N40   , Gs4 , v120, gtp1
	.byte	W24
	.byte	W03
	.byte	W03
	.byte	W03
	.byte	W03
	.byte	W03
	.byte	W03
@ 013   ----------------------------------------
	.byte	W06
	.byte	W06
	.byte		N22   , En4 , v124
	.byte	W12
	.byte	W06
	.byte	W06
	.byte		N09   , Cs4 , v120
	.byte	W12
	.byte		N01   , En4 , v116
	.byte	W06
	.byte		N16   , Bn4 , v120
	.byte	W18
	.byte		N11   , An4 , v124
	.byte	W12
	.byte		N06   , Gs4 , v120
	.byte	W12
@ 014   ----------------------------------------
	.byte		N11   , En5 , v124
	.byte	W12
	.byte		        Ds5 , v116
	.byte	W12
	.byte		N04   , Bn4 , v120
	.byte	W12
	.byte		N10   , Gs4 
	.byte	W12
	.byte		N04   , Bn4 
	.byte	W06
	.byte		N32   , En4 , v120, gtp3
	.byte	W18
	.byte	W03
	.byte	W03
	.byte	W03
	.byte	W03
	.byte	W03
	.byte	W09
@ 015   ----------------------------------------
	.byte		N11   , Dn4 
	.byte	W12
	.byte		N36   , Cs4 , v116
	.byte	W36
	.byte		N07   , En4 , v120
	.byte	W09
	.byte		N03   , Ds4 
	.byte	W03
	.byte		N20   , En4 
	.byte	W24
	.byte		N21   , Fs4 
	.byte	W12
@ 016   ----------------------------------------
	.byte	W12
	.byte		N72   , En4 
	.byte	W42
	.byte	W06
	.byte	W06
	.byte	W06
	.byte	W06
	.byte	W06
	.byte	W06
	.byte	W06
	.byte	GOTO
	 .word	bw_accumula_town_1_B1
bw_accumula_town_1_B2:
@ 017   ----------------------------------------
	.byte	FINE

@**************** Track 2 (Midi-Chn.2) ****************@

bw_accumula_town_2:
	.byte	KEYSH , bw_accumula_town_key+0
bw_accumula_town_2_B1:
@ 000   ----------------------------------------
	.byte		VOICE , 32
	.byte		VOL   , 124*bw_accumula_town_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		MOD   , 0
	.byte	W12
	.byte		N05   , En1 , v124
	.byte	W06
	.byte		        En1 , v052
	.byte	W12
	.byte		        Bn0 , v112
	.byte	W06
	.byte		N06   , Bn0 , v040
	.byte	W12
	.byte		N05   , En1 , v124
	.byte	W06
	.byte		        En1 , v052
	.byte	W18
	.byte		        An0 , v124
	.byte	W12
	.byte		N11   , An0 , v120
	.byte	W12
@ 001   ----------------------------------------
	.byte		        Gs0 , v112
	.byte	W12
	.byte		        Fs0 , v124
	.byte	W18
	.byte		N10   , Cs1 , v112
	.byte	W18
	.byte		N09   , Fs0 , v120
	.byte	W24
	.byte		N06   , Bn0 , v116
	.byte	W12
	.byte		N23   , Bn0 , v112
	.byte	W12
@ 002   ----------------------------------------
	.byte	W12
	.byte		N08   , En1 , v124
	.byte	W18
	.byte		        En1 , v116
	.byte	W18
	.byte		        En1 , v120
	.byte	W48
@ 003   ----------------------------------------
	.byte	W12
	.byte		        En1 , v124
	.byte	W18
	.byte		        En1 , v120
	.byte	W18
	.byte		        En1 , v124
	.byte	W24
	.byte		N11   , Bn0 , v112
	.byte	W12
	.byte		N05   , Cs1 , v104
	.byte	W12
@ 004   ----------------------------------------
	.byte		        Ds1 , v112
	.byte	W12
	.byte		        En1 , v124
	.byte	W06
	.byte		        En1 , v052
	.byte	W12
	.byte		        En1 , v112
	.byte	W06
	.byte		N06   , En1 , v040
	.byte	W12
	.byte		N05   , Gs0 , v124
	.byte	W06
	.byte		        Gs0 , v052
	.byte	W18
	.byte		        An0 , v124
	.byte	W12
	.byte		N10   , An0 , v120
	.byte	W12
@ 005   ----------------------------------------
	.byte		        Gs0 , v124
	.byte	W12
	.byte		N11   , Fs0 
	.byte	W18
	.byte		N10   , Cs1 , v116
	.byte	W18
	.byte		N09   , Fs0 , v120
	.byte	W24
	.byte		N06   , Bn0 , v124
	.byte	W12
	.byte		N23   , Bn0 , v120
	.byte	W12
@ 006   ----------------------------------------
	.byte	W12
	.byte		N08   , En1 , v124
	.byte	W18
	.byte		        En1 , v120
	.byte	W18
	.byte		        En1 , v124
	.byte	W48
@ 007   ----------------------------------------
	.byte	W12
	.byte		        En1 , v127
	.byte	W18
	.byte		        En1 , v120
	.byte	W18
	.byte		        En1 , v124
	.byte	W48
@ 008   ----------------------------------------
	.byte	W12
	.byte		N13   , An0 , v120
	.byte	W18
	.byte		N03   , An0 , v112
	.byte	W06
	.byte		N17   , En1 , v116
	.byte	W24
	.byte		N15   , Dn1 , v120
	.byte	W18
	.byte		N04   , Dn1 , v112
	.byte	W06
	.byte		N15   , An1 , v120
	.byte	W12
@ 009   ----------------------------------------
	.byte	W06
	.byte		N04   , An1 , v112
	.byte	W06
	.byte		N13   , Gs0 , v120
	.byte	W18
	.byte		N03   , Gs0 , v112
	.byte	W06
	.byte		N17   , Ds1 , v116
	.byte	W24
	.byte		N15   , Gn0 , v120
	.byte	W18
	.byte		N04   , Gn0 , v112
	.byte	W06
	.byte		N15   , Dn1 , v120
	.byte	W12
@ 010   ----------------------------------------
	.byte	W06
	.byte		N04   , Dn1 , v112
	.byte	W06
	.byte		N13   , Fs0 , v120
	.byte	W18
	.byte		N03   , Fs0 , v112
	.byte	W06
	.byte		N13   , Cs1 , v120
	.byte	W18
	.byte		N03   , Cs1 , v112
	.byte	W06
	.byte		N15   , Gs0 , v120
	.byte	W18
	.byte		N04   , Gs0 , v112
	.byte	W06
	.byte		N15   , Ds1 , v120
	.byte	W12
@ 011   ----------------------------------------
	.byte	W06
	.byte		N04   , Ds1 , v112
	.byte	W06
	.byte		N13   , Bn0 , v120
	.byte	W18
	.byte		N03   , Bn0 , v112
	.byte	W06
	.byte		N17   , Fs1 , v116
	.byte	W24
	.byte		N15   , As0 , v120
	.byte	W18
	.byte		N04   , As0 , v112
	.byte	W06
	.byte		N15   , As0 , v120
	.byte	W12
@ 012   ----------------------------------------
	.byte	W06
	.byte		N04   , As0 , v112
	.byte	W06
	.byte		N13   , An0 , v120
	.byte	W18
	.byte		N03   , An0 , v112
	.byte	W06
	.byte		N13   , En1 , v120
	.byte	W18
	.byte		N03   , En1 , v112
	.byte	W06
	.byte		N15   , An1 , v120
	.byte	W18
	.byte		N04   , An1 , v112
	.byte	W06
	.byte		N15   , En1 , v120
	.byte	W12
@ 013   ----------------------------------------
	.byte	W06
	.byte		N04   , En1 , v112
	.byte	W06
	.byte		N13   , Gs0 , v120
	.byte	W18
	.byte		N03   , Gs0 , v112
	.byte	W06
	.byte		N13   , Ds1 , v120
	.byte	W18
	.byte		N03   , Ds1 , v112
	.byte	W06
	.byte		N15   , Cs1 , v120
	.byte	W18
	.byte		N04   , Cs1 , v112
	.byte	W06
	.byte		N15   , Gs0 , v120
	.byte	W12
@ 014   ----------------------------------------
	.byte	W06
	.byte		N04   , Gs0 , v112
	.byte	W06
	.byte		N13   , Fs0 , v120
	.byte	W18
	.byte		N03   , Fs0 , v112
	.byte	W06
	.byte		N13   , Cs1 , v120
	.byte	W18
	.byte		N03   , Cs1 , v112
	.byte	W06
	.byte		N15   , Fn1 , v120
	.byte	W18
	.byte		N04   , Fn1 , v112
	.byte	W06
	.byte		N15   , Cn1 , v120
	.byte	W12
@ 015   ----------------------------------------
	.byte	W06
	.byte		N04   , Cn1 , v112
	.byte	W06
	.byte		N13   , En0 , v120
	.byte	W18
	.byte		N03   , En0 , v112
	.byte	W06
	.byte		N13   , Bn0 , v120
	.byte	W18
	.byte		N03   , Bn0 , v112
	.byte	W06
	.byte		N15   , En1 , v120
	.byte	W18
	.byte		N04   , En1 , v112
	.byte	W06
	.byte		N01   , Bn0 , v120
	.byte	W12
	.byte	GOTO
	 .word	bw_accumula_town_2_B1
bw_accumula_town_2_B2:
@ 016   ----------------------------------------
	.byte	FINE

@**************** Track 3 (Midi-Chn.3) ****************@

bw_accumula_town_3:
	.byte	KEYSH , bw_accumula_town_key+0
bw_accumula_town_3_B1:
@ 000   ----------------------------------------
	.byte		VOICE , 25
	.byte		PAN   , c_v-1
	.byte		VOL   , 112*bw_accumula_town_mvl/mxv
	.byte		MOD   , 0
	.byte	W12
	.byte		N15   , En2 , v108
	.byte		N15   , Gs2 , v104
	.byte		N15   , Bn2 , v096
	.byte		N15   , En3 
	.byte	W18
	.byte		        En2 , v100
	.byte		N15   , Gs2 , v096
	.byte		N15   , Bn2 , v092
	.byte		N15   , En3 
	.byte	W18
	.byte		N04   , En2 , v104
	.byte		N04   , Gs2 , v100
	.byte		N04   , Bn2 , v096
	.byte		N04   , En3 
	.byte	W24
	.byte		N02   , Cs2 , v100
	.byte		N02   , En2 , v096
	.byte		N02   , An2 , v092
	.byte		N02   , Cs3 , v096
	.byte	W12
	.byte		N22   , Cs2 , v100
	.byte		N22   , En2 , v096
	.byte		N22   , An2 , v092
	.byte		N22   , Cs3 , v096
	.byte	W12
@ 001   ----------------------------------------
	.byte	W12
	.byte		N15   , Fs2 , v108
	.byte		N15   , An2 , v096
	.byte		N15   , Cs3 
	.byte		N15   , En3 , v104
	.byte	W18
	.byte		        Fs2 , v100
	.byte		N15   , An2 , v092
	.byte		N15   , Cs3 
	.byte		N15   , En3 , v096
	.byte	W18
	.byte		N04   , Fs2 , v104
	.byte		N04   , An2 , v096
	.byte		N04   , Cs3 
	.byte		N04   , En3 , v100
	.byte	W24
	.byte		N02   , Cs2 
	.byte		N02   , En2 , v096
	.byte		N02   , An2 , v092
	.byte		N02   , Cs3 , v096
	.byte	W12
	.byte		N21   , Ds2 , v100
	.byte		N21   , Fs2 , v096
	.byte		N21   , Bn2 , v092
	.byte		N21   , Ds3 , v096
	.byte	W12
@ 002   ----------------------------------------
	.byte	W12
	.byte		N15   , En2 , v108
	.byte		N15   , Gs2 , v104
	.byte		N15   , Bn2 , v096
	.byte		N15   , En3 
	.byte	W18
	.byte		        En2 , v100
	.byte		N15   , Gs2 , v096
	.byte		N15   , Bn2 , v092
	.byte		N15   , En3 
	.byte	W18
	.byte		N05   , En2 , v104
	.byte		N05   , Gs2 , v100
	.byte		N05   , Bn2 , v096
	.byte		N05   , En3 
	.byte	W48
@ 003   ----------------------------------------
	.byte	W12
	.byte		N15   , En2 , v108
	.byte		N15   , Gs2 , v104
	.byte		N15   , Bn2 , v096
	.byte		N15   , En3 
	.byte	W18
	.byte		        En2 , v100
	.byte		N15   , Gs2 , v096
	.byte		N15   , Bn2 , v092
	.byte		N15   , En3 
	.byte	W18
	.byte		N06   , En2 , v104
	.byte		N06   , Gs2 , v100
	.byte		N06   , Bn2 , v096
	.byte		N06   , En3 
	.byte	W48
@ 004   ----------------------------------------
	.byte	W12
	.byte		N15   , En2 , v108
	.byte		N15   , Gs2 , v104
	.byte		N15   , Bn2 , v096
	.byte		N15   , En3 
	.byte	W18
	.byte		        En2 , v100
	.byte		N15   , Gs2 , v096
	.byte		N15   , Bn2 , v092
	.byte		N15   , En3 
	.byte	W18
	.byte		N04   , En2 , v108
	.byte		N04   , Gs2 , v100
	.byte		N04   , Bn2 , v096
	.byte		N04   , En3 
	.byte	W24
	.byte		N02   , Cs2 , v100
	.byte		N02   , En2 , v096
	.byte		N02   , An2 , v092
	.byte		N02   , Cs3 , v096
	.byte	W12
	.byte		N22   , Cs2 , v100
	.byte		N22   , En2 , v096
	.byte		N22   , An2 , v092
	.byte		N22   , Cs3 , v096
	.byte	W12
@ 005   ----------------------------------------
	.byte	W12
	.byte		N15   , Fs2 , v108
	.byte		N15   , An2 , v096
	.byte		N15   , Cs3 
	.byte		N15   , En3 , v104
	.byte	W18
	.byte		        Fs2 , v100
	.byte		N15   , An2 , v092
	.byte		N15   , Cs3 
	.byte		N15   , En3 , v096
	.byte	W18
	.byte		N04   , Fs2 , v108
	.byte		N04   , An2 , v096
	.byte		N04   , Cs3 
	.byte		N04   , En3 , v100
	.byte	W24
	.byte		N02   , Cs2 
	.byte		N02   , En2 , v096
	.byte		N02   , An2 , v092
	.byte		N02   , Cs3 , v096
	.byte	W12
	.byte		N22   , Ds2 , v100
	.byte		N22   , Fs2 , v096
	.byte		N22   , Bn2 , v092
	.byte		N22   , Ds3 , v096
	.byte	W12
@ 006   ----------------------------------------
bw_accumula_town_3_006:
	.byte	W12
	.byte		N15   , En2 , v108
	.byte		N15   , Gs2 , v104
	.byte		N15   , Bn2 , v096
	.byte		N15   , En3 
	.byte	W18
	.byte		        En2 , v100
	.byte		N15   , Gs2 , v096
	.byte		N15   , Bn2 , v092
	.byte		N15   , En3 
	.byte	W18
	.byte		N04   , En2 , v108
	.byte		N04   , Gs2 , v100
	.byte		N04   , Bn2 , v096
	.byte		N04   , En3 
	.byte	W48
	.byte	PEND
@ 007   ----------------------------------------
	.byte	PATT
	 .word	bw_accumula_town_3_006
@ 008   ----------------------------------------
	.byte	W12
	.byte		N23   , An1 , v112
	.byte	W06
	.byte		N17   , Gs2 , v104
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		N11   , En3 , v108
	.byte	W06
	.byte		        En2 , v112
	.byte	W06
	.byte		N17   , Gs2 , v100
	.byte	W06
	.byte		N11   , An1 , v096
	.byte		N11   , Cs3 , v104
	.byte	W06
	.byte		N05   , En3 , v108
	.byte	W06
	.byte		N23   , Dn2 , v116
	.byte	W06
	.byte		N17   , An2 , v100
	.byte	W06
	.byte		        Cn3 , v104
	.byte	W06
	.byte		N11   , En3 , v108
	.byte	W06
	.byte		N23   , An1 , v104
	.byte	W06
	.byte		N11   , Cn3 , v108
	.byte	W06
@ 009   ----------------------------------------
	.byte		        En3 , v104
	.byte	W06
	.byte		N05   , Gn3 
	.byte	W06
	.byte		N23   , Gs1 , v112
	.byte	W05
	.byte		N17   , Fs2 , v104
	.byte	W07
	.byte		        Bn2 
	.byte	W05
	.byte		N11   , Ds3 , v108
	.byte	W06
	.byte		        Ds2 , v112
	.byte	W06
	.byte		N17   , Fs2 , v096
	.byte	W06
	.byte		N11   , Gs1 
	.byte	W01
	.byte		        Bn2 , v104
	.byte	W05
	.byte		N05   , Ds3 , v108
	.byte	W06
	.byte		N23   , Gn1 , v116
	.byte	W06
	.byte		N17   , As2 , v108
	.byte	W06
	.byte		        Dn3 , v104
	.byte	W07
	.byte		N11   , Fn3 , v108
	.byte	W06
	.byte		N23   , Dn2 , v104
	.byte	W06
	.byte		N11   , Fn2 , v108
	.byte	W06
@ 010   ----------------------------------------
	.byte		        As2 , v104
	.byte	W05
	.byte		N05   , Dn3 , v112
	.byte	W07
	.byte		N23   , Fs1 
	.byte	W05
	.byte		N17   , En2 , v104
	.byte	W07
	.byte		        An2 
	.byte	W05
	.byte		N11   , Cs3 , v108
	.byte	W06
	.byte		        Cs2 , v112
	.byte	W06
	.byte		N17   , En2 , v096
	.byte	W06
	.byte		N11   , Fs1 
	.byte	W01
	.byte		        An2 , v104
	.byte	W05
	.byte		N05   , Cs3 , v108
	.byte	W07
	.byte		N23   , Gs1 , v116
	.byte	W06
	.byte		N17   , Fs2 , v108
	.byte	W05
	.byte		        Cn3 , v104
	.byte	W07
	.byte		N11   , Ds3 , v108
	.byte	W06
	.byte		N23   , Cn2 , v104
	.byte	W06
	.byte		N11   , Fs2 , v108
	.byte	W06
@ 011   ----------------------------------------
	.byte		        Cn3 , v104
	.byte	W06
	.byte		N05   , Ds3 , v112
	.byte	W06
	.byte		N23   , Bn1 
	.byte	W05
	.byte		N17   , An2 , v104
	.byte	W07
	.byte		        Dn3 
	.byte	W05
	.byte		N11   , Fs3 , v108
	.byte	W07
	.byte		        Fs1 , v112
	.byte	W06
	.byte		N17   , Fs2 , v096
	.byte	W05
	.byte		N11   , Bn1 
	.byte	W01
	.byte		        Bn2 , v104
	.byte	W06
	.byte		N05   , Dn3 , v108
	.byte	W06
	.byte		N23   , As1 , v116
	.byte	W06
	.byte		N17   , Gs2 , v108
	.byte	W06
	.byte		        Cn3 , v104
	.byte	W06
	.byte		N11   , En3 , v108
	.byte	W06
	.byte		N23   , As1 , v104
	.byte	W06
	.byte		N11   , En2 , v108
	.byte	W06
@ 012   ----------------------------------------
	.byte		        Gs2 , v104
	.byte	W06
	.byte		N05   , Cs3 , v112
	.byte	W06
	.byte		N23   , An1 
	.byte	W06
	.byte		N17   , Gs2 , v104
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		N11   , En3 , v108
	.byte	W06
	.byte		        En2 , v112
	.byte	W06
	.byte		N17   , Gs2 , v096
	.byte	W06
	.byte		N11   , An1 
	.byte		N11   , Cs3 , v104
	.byte	W06
	.byte		N05   , En3 , v108
	.byte	W06
	.byte		N23   , An1 , v116
	.byte	W06
	.byte		N17   , Fs2 , v108
	.byte	W06
	.byte		N11   , Bn2 , v104
	.byte	W06
	.byte		        Ds3 , v108
	.byte	W06
	.byte		N23   , An1 , v104
	.byte	W06
	.byte		N11   , Bn2 , v108
	.byte	W06
@ 013   ----------------------------------------
	.byte		        Ds3 , v104
	.byte	W06
	.byte		N05   , Fs3 , v112
	.byte	W06
	.byte		N23   , Gs1 
	.byte	W05
	.byte		N17   , Fs2 , v104
	.byte	W07
	.byte		        Bn2 
	.byte	W05
	.byte		N11   , Ds3 , v108
	.byte	W06
	.byte		        Ds2 , v112
	.byte	W06
	.byte		N17   , Fs2 , v096
	.byte	W06
	.byte		N11   , Gs1 
	.byte	W01
	.byte		        Bn2 , v104
	.byte	W05
	.byte		N05   , Ds3 , v108
	.byte	W07
	.byte		N23   , Cs2 , v116
	.byte	W05
	.byte		N17   , Fn2 , v108
	.byte	W07
	.byte		        Bn2 , v104
	.byte	W06
	.byte		N11   , Dn3 , v108
	.byte	W06
	.byte		N23   , Gs1 , v104
	.byte	W06
	.byte		N11   , Fn2 , v108
	.byte	W06
@ 014   ----------------------------------------
	.byte		        Bn2 , v104
	.byte	W05
	.byte		N05   , Dn3 , v112
	.byte	W07
	.byte		N23   , Fs1 
	.byte	W05
	.byte		N17   , En2 , v104
	.byte	W07
	.byte		        An2 
	.byte	W05
	.byte		N11   , Cs3 , v108
	.byte	W06
	.byte		        Cs2 , v112
	.byte	W06
	.byte		N17   , En2 , v096
	.byte	W06
	.byte		N11   , Fs1 
	.byte	W01
	.byte		        An2 , v104
	.byte	W05
	.byte		N05   , Cs3 , v108
	.byte	W07
	.byte		N23   , Fn1 , v116
	.byte	W06
	.byte		N17   , En2 , v108
	.byte	W06
	.byte		N11   , An2 , v104
	.byte	W06
	.byte		        Cn3 , v108
	.byte	W06
	.byte		N23   , Cn2 , v104
	.byte	W06
	.byte		N11   , An2 , v108
	.byte	W06
@ 015   ----------------------------------------
	.byte		        Cn3 , v104
	.byte	W06
	.byte		N05   , En3 , v112
	.byte	W06
	.byte		N23   , En1 
	.byte	W06
	.byte		N17   , Gs2 , v104
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		N11   , Ds3 , v108
	.byte	W06
	.byte		        Bn1 , v112
	.byte	W06
	.byte		        En2 , v104
	.byte	W05
	.byte		        En1 , v096
	.byte	W01
	.byte		        Gs2 , v108
	.byte	W06
	.byte		N05   , Bn2 
	.byte	W06
	.byte		N23   , En1 , v112
	.byte	W06
	.byte		N17   , Bn2 , v104
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		N11   , Gs3 , v108
	.byte	W06
	.byte		        Bn1 , v112
	.byte	W06
	.byte		N05   , Gs2 , v104
	.byte	W05
	.byte		N01   , En1 , v096
	.byte	W01
	.byte	GOTO
	 .word	bw_accumula_town_3_B1
bw_accumula_town_3_B2:
@ 016   ----------------------------------------
	.byte	FINE

@**************** Track 4 (Midi-Chn.5) ****************@

bw_accumula_town_4:
	.byte	KEYSH , bw_accumula_town_key+0
bw_accumula_town_4_B1:
@ 000   ----------------------------------------
	.byte		VOICE , 73
	.byte		PAN   , c_v+0
	.byte		VOL   , 52*bw_accumula_town_mvl/mxv
	.byte		MOD   , 0
	.byte	W06
	.byte		N05   , Gs4 , v116
	.byte	W06
	.byte		        An4 , v112
	.byte	W06
	.byte		        Bn4 , v120
	.byte	W06
	.byte		N02   , An4 , v116
	.byte	W12
	.byte		N17   , Gs4 , v120
	.byte	W18
	.byte		N01   , En4 , v112
	.byte	W12
	.byte		N21   , Cs4 , v120
	.byte	W30
@ 001   ----------------------------------------
	.byte	W06
	.byte		N03   , En4 , v116
	.byte	W12
	.byte		N11   , Cs4 , v120
	.byte	W18
	.byte		N18   , Cs4 , v116
	.byte	W18
	.byte		N03   , En4 , v108
	.byte	W09
	.byte		N04   , Gs4 , v116
	.byte	W03
	.byte		N11   , An4 , v124
	.byte	W12
	.byte		N02   , Gs4 , v116
	.byte	W12
	.byte		N11   , Fs4 , v124
	.byte	W06
@ 002   ----------------------------------------
	.byte	W06
	.byte		N02   , Ds4 , v116
	.byte	W10
	.byte		        Ds4 , v120
	.byte	W02
	.byte		N05   , En4 , v124
	.byte	W18
	.byte		        En4 , v120
	.byte	W18
	.byte		        En4 , v124
	.byte	W42
@ 003   ----------------------------------------
	.byte	W96
@ 004   ----------------------------------------
	.byte	W06
	.byte		        Gs4 , v116
	.byte	W06
	.byte		        An4 , v112
	.byte	W06
	.byte		        Bn4 , v120
	.byte	W06
	.byte		N02   , An4 , v116
	.byte	W12
	.byte		N17   , Gs4 , v120
	.byte	W18
	.byte		N01   , En4 , v112
	.byte	W12
	.byte		N21   , Cs4 , v120
	.byte	W30
@ 005   ----------------------------------------
	.byte	W06
	.byte		N03   , En4 , v116
	.byte	W12
	.byte		N11   , Cs4 , v120
	.byte	W18
	.byte		N18   , Cs4 , v116
	.byte	W18
	.byte		N03   , En4 , v108
	.byte	W10
	.byte		N04   , Gs4 , v116
	.byte	W02
	.byte		N11   , An4 , v124
	.byte	W12
	.byte		N02   , Gs4 , v116
	.byte	W12
	.byte		N11   , Fs4 , v124
	.byte	W06
@ 006   ----------------------------------------
	.byte	W06
	.byte		N02   , Bn4 , v116
	.byte	W10
	.byte		        Ds4 , v120
	.byte	W02
	.byte		N05   , En4 , v124
	.byte	W18
	.byte		        En4 , v120
	.byte	W18
	.byte		        En4 , v124
	.byte	W42
@ 007   ----------------------------------------
	.byte	W12
	.byte		N01   , Bn4 , v096
	.byte	W02
	.byte		        Cs5 , v084
	.byte	W02
	.byte		N02   , Ds5 , v100
	.byte	W02
	.byte		N05   , En5 , v104
	.byte	W18
	.byte		        En5 , v100
	.byte	W18
	.byte		        En5 , v104
	.byte	W42
@ 008   ----------------------------------------
	.byte	W04
	.byte		        Ds4 , v112
	.byte	W02
	.byte		N11   , En4 , v120
	.byte	W12
	.byte		N32   , Cs4 , v120, gtp2
	.byte	W18
	.byte	W06
	.byte	W06
	.byte	W06
	.byte		N01   , En4 
	.byte	W06
	.byte		N15   , Bn4 
	.byte	W18
	.byte		N10   , An4 , v124
	.byte	W12
	.byte		N08   , Gs4 , v120
	.byte	W06
@ 009   ----------------------------------------
	.byte	W06
	.byte		N11   , Bn4 
	.byte	W12
	.byte		N23   , Gs4 
	.byte	W12
	.byte	W06
	.byte	W06
	.byte		N12   , En4 , v124
	.byte	W12
	.byte		N05   , Fs4 , v120
	.byte	W06
	.byte		N32   , En4 , v124, gtp3
	.byte	W21
	.byte	W03
	.byte	W03
	.byte	W03
	.byte	W03
	.byte	W03
@ 010   ----------------------------------------
	.byte	W06
	.byte		N11   , Dn4 , v120
	.byte	W12
	.byte		N21   , Cs4 , v116
	.byte	W12
	.byte	W06
	.byte	W06
	.byte		N09   , Ds4 , v120
	.byte	W12
	.byte		N03   , En4 , v116
	.byte	W06
	.byte		N15   , Cn4 , v124
	.byte	W18
	.byte		N10   , Ds4 , v116
	.byte	W12
	.byte		N11   , En4 , v124
	.byte	W06
@ 011   ----------------------------------------
	.byte	W06
	.byte		N06   , Fs4 , v116
	.byte	W12
	.byte		N22   , Fs4 , v124
	.byte	W12
	.byte	W06
	.byte	W06
	.byte		N11   , En4 , v120
	.byte	W12
	.byte		N01   , Fs4 , v112
	.byte	W06
	.byte		N40   , Gs4 , v120, gtp1
	.byte	W24
	.byte	W03
	.byte	W03
	.byte	W03
	.byte	W03
@ 012   ----------------------------------------
	.byte	W03
	.byte	W09
	.byte	W06
	.byte		N22   , En4 , v124
	.byte	W12
	.byte	W06
	.byte	W06
	.byte		N09   , Cs4 , v120
	.byte	W12
	.byte		N01   , En4 , v116
	.byte	W06
	.byte		N16   , Bn4 , v120
	.byte	W18
	.byte		N11   , An4 , v124
	.byte	W12
	.byte		N06   , Gs4 , v120
	.byte	W06
@ 013   ----------------------------------------
	.byte	W06
	.byte		N11   , En5 , v124
	.byte	W12
	.byte		        Ds5 , v116
	.byte	W12
	.byte		N05   , Bn4 , v120
	.byte	W12
	.byte		N08   , Gs4 
	.byte	W12
	.byte		N05   , Bn4 
	.byte	W06
	.byte		N32   , En4 , v120, gtp3
	.byte	W18
	.byte	W03
	.byte	W03
	.byte	W03
	.byte	W03
	.byte	W03
	.byte	W03
@ 014   ----------------------------------------
	.byte	W06
	.byte		N11   , Dn4 
	.byte	W12
	.byte		N36   , Cs4 , v116
	.byte	W36
	.byte		N07   , En4 , v120
	.byte	W09
	.byte		N03   , Ds4 , v116
	.byte	W03
	.byte		N20   , En4 , v120
	.byte	W24
	.byte		N21   , Fs4 
	.byte	W06
@ 015   ----------------------------------------
	.byte	W18
	.byte		N72   , En4 
	.byte	W42
	.byte	W06
	.byte	W06
	.byte	W06
	.byte	W06
	.byte	W06
	.byte	W06
	.byte	GOTO
	 .word	bw_accumula_town_4_B1
bw_accumula_town_4_B2:
@ 016   ----------------------------------------
	.byte	FINE

@**************** Track 5 (Midi-Chn.7) ****************@

bw_accumula_town_5:
	.byte	KEYSH , bw_accumula_town_key+0
bw_accumula_town_5_B1:
@ 000   ----------------------------------------
	.byte		VOICE , 0
	.byte		PAN   , c_v-1
	.byte		VOL   , 120*bw_accumula_town_mvl/mxv
	.byte		MOD   , 0
	.byte	W12
	.byte		N05   , Gs3 , v108
	.byte		N05   , En4 
	.byte	W18
	.byte		        Gs3 , v104
	.byte		N05   , En4 
	.byte	W18
	.byte		        Gs3 
	.byte		N05   , En4 , v108
	.byte	W24
	.byte		        En3 
	.byte		N05   , Cs4 
	.byte	W12
	.byte		N17   , En3 , v104
	.byte		N17   , Cs4 , v100
	.byte	W12
@ 001   ----------------------------------------
	.byte	W12
	.byte		N05   , An3 , v104
	.byte		N05   , Cs4 , v100
	.byte	W18
	.byte		        An3 , v108
	.byte		N05   , Cs4 , v096
	.byte	W18
	.byte		        An3 , v104
	.byte		N05   , Cs4 , v084
	.byte	W24
	.byte		        An3 , v096
	.byte		N05   , Cs4 , v100
	.byte	W12
	.byte		N17   , Fs3 , v104
	.byte		N17   , Ds4 
	.byte	W12
@ 002   ----------------------------------------
	.byte	W12
	.byte		N04   , Gs3 , v108
	.byte		N04   , En4 , v112
	.byte	W18
	.byte		        Gs3 , v100
	.byte		N04   , En4 , v104
	.byte	W18
	.byte		        Gs3 , v108
	.byte		N04   , En4 
	.byte	W48
@ 003   ----------------------------------------
	.byte	W12
	.byte		        Bn3 , v120
	.byte		N04   , En4 , v116
	.byte	W18
	.byte		        Bn3 , v108
	.byte		N04   , En4 
	.byte	W18
	.byte		        Bn3 , v112
	.byte		N04   , En4 , v108
	.byte	W48
@ 004   ----------------------------------------
	.byte	W12
	.byte		N05   , Gs3 
	.byte		N05   , En4 , v112
	.byte	W18
	.byte		        Gs3 , v104
	.byte		N05   , En4 , v108
	.byte	W18
	.byte		        Gs3 , v104
	.byte		N05   , En4 , v112
	.byte	W24
	.byte		        An3 , v108
	.byte		N05   , Cs4 
	.byte	W12
	.byte		N17   , An3 , v104
	.byte		N17   , Cs4 
	.byte	W12
@ 005   ----------------------------------------
	.byte	W12
	.byte		N05   , An3 , v112
	.byte		N05   , Cs4 
	.byte	W18
	.byte		        An3 , v104
	.byte		N05   , Cs4 , v108
	.byte	W18
	.byte		        An3 , v112
	.byte		N05   , Cs4 
	.byte	W24
	.byte		        An3 , v104
	.byte		N05   , En4 
	.byte	W12
	.byte		N17   , An3 , v112
	.byte		N17   , Fs4 , v108
	.byte	W12
@ 006   ----------------------------------------
	.byte	W12
	.byte		N05   , Gs3 
	.byte		N05   , En4 , v112
	.byte	W18
	.byte		        Gs3 , v100
	.byte		N05   , En4 , v108
	.byte	W18
	.byte		        Gs3 , v100
	.byte		N05   , En4 , v112
	.byte	W48
@ 007   ----------------------------------------
	.byte	W06
	.byte		N01   , Bn4 , v104
	.byte	W02
	.byte		        Cs5 , v092
	.byte	W02
	.byte		        Ds5 , v096
	.byte	W02
	.byte		N05   , Gs4 , v104
	.byte		N05   , En5 , v108
	.byte	W18
	.byte		        Gs4 , v104
	.byte		N05   , En5 , v108
	.byte	W18
	.byte		        Gs4 
	.byte		N05   , En5 
	.byte	W48
@ 008   ----------------------------------------
	.byte	W24
	.byte		        Cs4 , v120
	.byte	W12
	.byte		        Ds4 , v112
	.byte	W06
	.byte		        En4 , v108
	.byte	W12
	.byte		N17   , Bn4 , v120
	.byte	W18
	.byte		N05   , An4 , v112
	.byte	W12
	.byte		N11   , Gs4 , v120
	.byte	W12
@ 009   ----------------------------------------
	.byte		N05   , Bn4 , v112
	.byte	W22
	.byte		        Ds4 , v096
	.byte	W02
	.byte		N11   , En4 , v116
	.byte	W12
	.byte		N05   , Fs4 , v112
	.byte	W06
	.byte		        Gs4 , v108
	.byte	W12
	.byte		N11   , Fs4 , v116
	.byte	W12
	.byte		N05   , En4 , v120
	.byte	W12
	.byte		N02   , Dn4 , v108
	.byte	W06
	.byte		N05   , En4 , v120
	.byte	W12
@ 010   ----------------------------------------
	.byte		        Dn4 , v116
	.byte	W24
	.byte		        An3 , v104
	.byte	W06
	.byte		        Gs3 , v096
	.byte	W06
	.byte		        An3 , v112
	.byte	W06
	.byte		        Bn3 , v100
	.byte	W06
	.byte		        Cs4 , v116
	.byte	W06
	.byte		        Cn4 , v108
	.byte	W12
	.byte		        Cn4 , v112
	.byte	W06
	.byte		        Ds4 , v108
	.byte	W06
	.byte		        En4 , v116
	.byte	W06
	.byte		        Fs4 , v104
	.byte	W06
	.byte		        Gs4 , v120
	.byte	W06
@ 011   ----------------------------------------
	.byte		        An4 , v108
	.byte	W06
	.byte		        Bn4 , v116
	.byte	W06
	.byte		N11   , En5 , v127
	.byte	W12
	.byte		N05   , Dn5 , v112
	.byte	W12
	.byte		        Cs5 
	.byte	W06
	.byte		        Bn4 
	.byte	W10
	.byte		N04   , As4 
	.byte	W02
	.byte		N05   , Bn4 
	.byte	W12
	.byte		        An4 , v108
	.byte	W18
	.byte		        Gs4 
	.byte	W12
@ 012   ----------------------------------------
	.byte		        Fs4 , v116
	.byte	W24
	.byte		        Ds4 , v120
	.byte	W06
	.byte		        En4 , v112
	.byte	W06
	.byte		        Cs4 , v116
	.byte	W06
	.byte		        Ds4 , v108
	.byte	W12
	.byte		        En4 , v116
	.byte	W12
	.byte		        En4 , v120
	.byte	W06
	.byte		        Fs4 , v112
	.byte	W06
	.byte		        Gs4 , v120
	.byte	W06
	.byte		        An4 , v116
	.byte	W06
	.byte		        Bn4 , v108
	.byte	W06
@ 013   ----------------------------------------
	.byte		        Cs5 , v116
	.byte	W06
	.byte		        Ds5 , v112
	.byte	W06
	.byte		N11   , En5 , v120
	.byte	W12
	.byte		N05   , Ds5 , v108
	.byte	W12
	.byte		        En5 , v116
	.byte	W06
	.byte		        Fs5 , v112
	.byte	W10
	.byte		N02   
	.byte	W02
	.byte		N11   , Gs5 , v120
	.byte	W12
	.byte		N05   , Fs5 , v116
	.byte	W12
	.byte		        En5 , v120
	.byte	W06
	.byte		        Ds5 , v112
	.byte	W12
@ 014   ----------------------------------------
	.byte		        Dn5 , v120
	.byte	W21
	.byte		        Bn4 , v104
	.byte	W03
	.byte		N11   , Cs5 , v120
	.byte	W12
	.byte		N05   , Bn4 , v116
	.byte	W06
	.byte		        An4 , v104
	.byte	W12
	.byte		        Gs4 , v112
	.byte	W12
	.byte		        Gs4 , v108
	.byte	W06
	.byte		        An4 , v116
	.byte	W06
	.byte		        Bn4 , v108
	.byte	W06
	.byte		        Gs4 , v116
	.byte	W12
@ 015   ----------------------------------------
	.byte		        En4 , v108
	.byte	W12
	.byte		        En4 , v116
	.byte	W12
	.byte		        Bn3 , v104
	.byte	W06
	.byte		        En4 , v112
	.byte	W12
	.byte		        Bn3 , v108
	.byte	W12
	.byte		N11   , An3 
	.byte	W12
	.byte		N05   , Gs3 , v104
	.byte	W06
	.byte		        An3 , v100
	.byte	W12
	.byte		        Fs3 , v108
	.byte	W12
	.byte	GOTO
	 .word	bw_accumula_town_5_B1
bw_accumula_town_5_B2:
@ 016   ----------------------------------------
	.byte	FINE

@**************** Track 6 (Midi-Chn.8) ****************@

bw_accumula_town_6:
	.byte	KEYSH , bw_accumula_town_key+0
bw_accumula_town_6_B1:
@ 000   ----------------------------------------
	.byte		VOICE , 0
	.byte		PAN   , c_v+0
	.byte		VOL   , 60*bw_accumula_town_mvl/mxv
	.byte		MOD   , 0
	.byte	W96
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
	.byte	W30
	.byte		N05   , Cs4 , v116
	.byte	W12
	.byte		        Ds4 , v108
	.byte	W06
	.byte		        En4 , v104
	.byte	W12
	.byte		N17   , Bn4 , v116
	.byte	W18
	.byte		N05   , An4 , v108
	.byte	W12
	.byte		N11   , Gs4 , v116
	.byte	W06
@ 009   ----------------------------------------
	.byte	W06
	.byte		N05   , Bn4 , v108
	.byte	W22
	.byte		        Ds4 , v092
	.byte	W02
	.byte		N11   , En4 , v112
	.byte	W12
	.byte		N05   , Fs4 , v108
	.byte	W06
	.byte		        Gs4 , v104
	.byte	W12
	.byte		N11   , Fs4 , v112
	.byte	W12
	.byte		N05   , En4 , v116
	.byte	W12
	.byte		N02   , Dn4 , v108
	.byte	W06
	.byte		N05   , En4 , v116
	.byte	W06
@ 010   ----------------------------------------
	.byte	W06
	.byte		        Dn4 , v112
	.byte	W24
	.byte		        An3 , v100
	.byte	W06
	.byte		        Gs3 , v092
	.byte	W06
	.byte		        An3 , v108
	.byte	W06
	.byte		        Bn3 , v096
	.byte	W06
	.byte		        Cs4 , v112
	.byte	W06
	.byte		        Cn4 , v100
	.byte	W12
	.byte		        Cn4 , v108
	.byte	W06
	.byte		        Ds4 , v104
	.byte	W06
	.byte		        En4 , v112
	.byte	W06
	.byte		        Fs4 , v100
	.byte	W06
@ 011   ----------------------------------------
	.byte		        Gs4 , v116
	.byte	W06
	.byte		        An4 , v104
	.byte	W06
	.byte		        Bn4 , v112
	.byte	W06
	.byte		N11   , En5 , v124
	.byte	W12
	.byte		N05   , Dn5 , v108
	.byte	W12
	.byte		        Cs5 
	.byte	W06
	.byte		        Bn4 
	.byte	W10
	.byte		        As4 , v112
	.byte	W02
	.byte		        Bn4 , v108
	.byte	W12
	.byte		        An4 , v104
	.byte	W18
	.byte		        Gs4 
	.byte	W06
@ 012   ----------------------------------------
	.byte	W06
	.byte		        Fs4 , v112
	.byte	W24
	.byte		        Ds4 , v116
	.byte	W06
	.byte		        En4 , v108
	.byte	W06
	.byte		        Cs4 , v112
	.byte	W06
	.byte		        Ds4 , v104
	.byte	W12
	.byte		        En4 , v112
	.byte	W12
	.byte		        En4 , v116
	.byte	W06
	.byte		        Fs4 , v108
	.byte	W06
	.byte		        Gs4 , v116
	.byte	W06
	.byte		        An4 , v112
	.byte	W06
@ 013   ----------------------------------------
	.byte		        Bn4 , v104
	.byte	W06
	.byte		        Cs5 , v112
	.byte	W06
	.byte		        Ds5 , v108
	.byte	W06
	.byte		N11   , En5 , v116
	.byte	W12
	.byte		N05   , Ds5 , v104
	.byte	W12
	.byte		        En5 , v112
	.byte	W06
	.byte		        Fs5 , v108
	.byte	W10
	.byte		N02   , Fs5 , v116
	.byte	W02
	.byte		N11   , Gs5 
	.byte	W12
	.byte		N05   , Fs5 , v108
	.byte	W12
	.byte		        En5 
	.byte	W06
	.byte		        Ds5 
	.byte	W06
@ 014   ----------------------------------------
	.byte	W06
	.byte		        Dn5 
	.byte	W21
	.byte		        Bn4 , v100
	.byte	W03
	.byte		N11   , Cs5 , v116
	.byte	W12
	.byte		N05   , Bn4 , v112
	.byte	W06
	.byte		        An4 , v100
	.byte	W12
	.byte		        Gs4 , v108
	.byte	W12
	.byte		        Gs4 , v104
	.byte	W06
	.byte		        An4 , v112
	.byte	W06
	.byte		        Bn4 , v104
	.byte	W06
	.byte		        Gs4 , v112
	.byte	W06
@ 015   ----------------------------------------
	.byte	W06
	.byte		        En4 , v104
	.byte	W12
	.byte		        En4 , v112
	.byte	W12
	.byte		        Bn3 , v100
	.byte	W06
	.byte		        En4 , v108
	.byte	W12
	.byte		        Bn3 , v104
	.byte	W12
	.byte		N11   , An3 
	.byte	W12
	.byte		N05   , Gs3 , v100
	.byte	W06
	.byte		        An3 , v096
	.byte	W12
	.byte		        Fs3 , v104
	.byte	W06
	.byte	GOTO
	 .word	bw_accumula_town_6_B1
bw_accumula_town_6_B2:
@ 016   ----------------------------------------
	.byte	FINE

@**************** Track 7 (Midi-Chn.11) ****************@

bw_accumula_town_7:
	.byte		VOL   , 127*bw_accumula_town_mvl/mxv
	.byte	KEYSH , bw_accumula_town_key+0
bw_accumula_town_7_B1:
@ 000   ----------------------------------------
	.byte		VOICE , 13
	.byte	W11
	.byte		N03   , Cn1 , v120
	.byte		N23   , Cs2 , v100
	.byte	W18
	.byte		N03   , Cn1 
	.byte	W06
	.byte		N11   , En1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v092
	.byte	W06
	.byte		N03   , Cn1 , v112
	.byte		N04   , Fs1 , v076
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N03   , Ds1 , v124
	.byte		N04   , Fs1 , v100
	.byte	W12
	.byte		N03   , Cn1 , v116
	.byte		N03   , Ds1 , v120
	.byte		N04   , Fs1 , v080
	.byte	W13
@ 001   ----------------------------------------
	.byte	W11
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v108
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v100
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N11   , En1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N11   , As1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v112
	.byte	W06
	.byte		        Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		N11   , En1 , v108
	.byte		N04   , Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		        Fs1 , v080
	.byte	W06
	.byte		N11   , En1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		        Fs1 , v096
	.byte	W01
@ 002   ----------------------------------------
	.byte	W05
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		        Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v100
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N07   , En1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v112
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N03   , Ds1 , v124
	.byte		N11   , As1 , v096
	.byte	W12
	.byte		N03   , Ds1 , v120
	.byte		N07   , En1 
	.byte		N04   , Fs1 , v080
	.byte	W12
	.byte		        Fs1 , v100
	.byte	W01
@ 003   ----------------------------------------
	.byte	W05
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		        Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v100
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N11   , En1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v112
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N03   , Ds1 , v124
	.byte		N11   , As1 , v096
	.byte	W12
	.byte		N03   , Cn1 , v116
	.byte		N03   , Ds1 , v120
	.byte		N04   , Fs1 , v080
	.byte	W13
@ 004   ----------------------------------------
	.byte	W11
	.byte		N03   , Cn1 , v120
	.byte		N23   , Cs2 , v100
	.byte	W12
	.byte		N03   , Cn1 , v108
	.byte	W06
	.byte		        Cn1 , v100
	.byte	W06
	.byte		N07   , En1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v112
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N03   , Ds1 , v124
	.byte		N11   , As1 , v096
	.byte	W12
	.byte		N03   , Ds1 , v120
	.byte		N07   , En1 
	.byte		N04   , Fs1 , v080
	.byte	W12
	.byte		        Fs1 , v100
	.byte	W01
@ 005   ----------------------------------------
	.byte	W05
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v108
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v100
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N07   , En1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v112
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		N05   , En1 , v112
	.byte		N04   , Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		        Fs1 , v080
	.byte	W06
	.byte		N07   , En1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N11   , As1 , v096
	.byte	W01
@ 006   ----------------------------------------
	.byte	W05
	.byte		N03   , Cn1 , v116
	.byte	W06
	.byte		        Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v108
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v100
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N07   , En1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v112
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N03   , Ds1 , v124
	.byte		N11   , As1 , v096
	.byte	W12
	.byte		N03   , Ds1 , v120
	.byte		N07   , En1 
	.byte		N04   , Fs1 , v080
	.byte	W12
	.byte		        Fs1 , v100
	.byte	W01
@ 007   ----------------------------------------
	.byte	W05
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v108
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v100
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N07   , En1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v112
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		N02   , En1 , v060
	.byte		N04   , Fs1 , v088
	.byte	W03
	.byte		N02   , En1 , v076
	.byte	W03
	.byte		N03   , Cn1 , v116
	.byte		N03   , Ds1 , v124
	.byte		N02   , En1 , v084
	.byte		N11   , As1 , v096
	.byte	W03
	.byte		N02   , En1 , v100
	.byte	W03
	.byte		N05   , En1 , v096
	.byte	W06
	.byte		N03   , Ds1 , v120
	.byte		N05   , En1 , v124
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N05   , En1 , v112
	.byte	W06
	.byte		N11   , Fn1 , v100
	.byte	W01
@ 008   ----------------------------------------
	.byte	W05
	.byte		N03   , Cn1 , v116
	.byte	W06
	.byte		        Cn1 , v120
	.byte		N23   , Cs2 , v100
	.byte	W12
	.byte		N03   , Cn1 , v108
	.byte	W06
	.byte		        Cn1 , v100
	.byte	W06
	.byte		N07   , En1 , v127
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v112
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N11   , As1 , v096
	.byte	W12
	.byte		N07   , En1 , v127
	.byte		N04   , Fs1 , v080
	.byte	W13
@ 009   ----------------------------------------
	.byte	W05
	.byte		N03   , Cn1 , v116
	.byte	W06
	.byte		        Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v108
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v100
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N07   , En1 , v127
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v112
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		N05   , En1 , v120
	.byte		N04   , Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		        Fs1 , v080
	.byte	W06
	.byte		N07   , En1 , v127
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N11   , As1 , v096
	.byte	W01
@ 010   ----------------------------------------
bw_accumula_town_7_010:
	.byte	W05
	.byte		N03   , Cn1 , v116
	.byte	W06
	.byte		        Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v108
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v100
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N07   , En1 , v127
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v112
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N11   , As1 , v096
	.byte	W12
	.byte		N07   , En1 , v127
	.byte		N04   , Fs1 , v080
	.byte	W12
	.byte		        Fs1 , v100
	.byte	W01
	.byte	PEND
@ 011   ----------------------------------------
	.byte	W05
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v108
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v100
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N07   , En1 , v127
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v112
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N11   , As1 , v096
	.byte	W12
	.byte		N07   , En1 , v127
	.byte		N04   , Fs1 , v080
	.byte	W12
	.byte		        Fs1 , v100
	.byte	W01
@ 012   ----------------------------------------
	.byte	W05
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N23   , Cs2 , v100
	.byte	W12
	.byte		N03   , Cn1 , v108
	.byte	W06
	.byte		        Cn1 , v100
	.byte	W06
	.byte		N07   , En1 , v127
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v112
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N11   , As1 , v096
	.byte	W12
	.byte		N07   , En1 , v127
	.byte		N04   , Fs1 , v080
	.byte	W12
	.byte		        Fs1 , v100
	.byte	W01
@ 013   ----------------------------------------
	.byte	W05
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v108
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v100
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N07   , En1 , v127
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v112
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		N05   , En1 , v120
	.byte		N04   , Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		        Fs1 , v080
	.byte	W06
	.byte		N07   , En1 , v127
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N11   , As1 , v096
	.byte	W01
@ 014   ----------------------------------------
	.byte	PATT
	 .word	bw_accumula_town_7_010
@ 015   ----------------------------------------
	.byte	W05
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v108
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v100
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N07   , En1 , v127
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N04   , Fs1 , v096
	.byte	W06
	.byte		N03   , Cn1 , v112
	.byte		N04   , Fs1 , v080
	.byte	W06
	.byte		N03   , Cn1 , v120
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		N07   , En1 , v112
	.byte		N04   , Fs1 , v088
	.byte	W06
	.byte		N03   , Cn1 , v116
	.byte		N11   , As1 , v096
	.byte	W12
	.byte		N07   , En1 , v127
	.byte		N04   , Fs1 , v100
	.byte	W06
	.byte		        Fs1 , v088
	.byte	W06
	.byte		N01   , Fn1 , v104
	.byte	W01
	.byte	GOTO
	 .word	bw_accumula_town_7_B1
bw_accumula_town_7_B2:
@ 016   ----------------------------------------
	.byte	FINE

@******************************************************@
	.align	2

bw_accumula_town:
	.byte	7	@ NumTrks
	.byte	0	@ NumBlks
	.byte	bw_accumula_town_pri	@ Priority
	.byte	bw_accumula_town_rev	@ Reverb.

	.word	bw_accumula_town_grp

	.word	bw_accumula_town_1
	.word	bw_accumula_town_2
	.word	bw_accumula_town_3
	.word	bw_accumula_town_4
	.word	bw_accumula_town_5
	.word	bw_accumula_town_6
	.word	bw_accumula_town_7

	.end
