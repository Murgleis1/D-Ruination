	.include "MPlayDef.s"

	.equ	mus_custom_garden_moon_grp, voicegroup193
	.equ	mus_custom_garden_moon_pri, 4
	.equ	mus_custom_garden_moon_rev, reverb_set+50
	.equ	mus_custom_garden_moon_mvl, 75
	.equ	mus_custom_garden_moon_key, 0
	.equ	mus_custom_garden_moon_tbs, 1
	.equ	mus_custom_garden_moon_exg, 1
	.equ	mus_custom_garden_moon_cmp, 1

	.section .rodata
	.global	mus_custom_garden_moon
	.align	2

@**************** Track 1 (Midi-Chn.1) ****************@

mus_custom_garden_moon_1:
	.byte	KEYSH , mus_custom_garden_moon_key+0
@ 000   ----------------------------------------
	.byte	TEMPO , 120*mus_custom_garden_moon_tbs/2
	.byte		VOICE , 26
	.byte		VOL   , 127*mus_custom_garden_moon_mvl/mxv
	.byte		PAN   , c_v-42
	.byte		BEND  , c_v+0
	.byte		N24   , En3 , v032
	.byte		N24   , En4 , v096
	.byte	W36
	.byte		N12   , An3 
	.byte	W12
	.byte		        En4 
	.byte	W12
	.byte		        Gn4 
	.byte	W12
@ 001   ----------------------------------------
mus_custom_garden_moon_1_001:
	.byte		N24   , Dn4 , v096
	.byte	W36
	.byte		N12   , Fn3 
	.byte	W12
	.byte		        Cn4 
	.byte	W12
	.byte		        Dn4 
	.byte	W12
	.byte	PEND
@ 002   ----------------------------------------
mus_custom_garden_moon_1_002:
	.byte		N24   , Cn4 , v096
	.byte	W36
	.byte		N12   , En3 
	.byte	W12
	.byte		        Cn4 
	.byte	W12
	.byte		        Dn4 
	.byte	W12
	.byte	PEND
@ 003   ----------------------------------------
mus_custom_garden_moon_1_003:
	.byte		N24   , Bn3 , v096
	.byte	W36
	.byte		N12   , An3 
	.byte	W12
	.byte		        En4 
	.byte	W12
	.byte		        Gn4 
	.byte	W12
	.byte	PEND
@ 004   ----------------------------------------
mus_custom_garden_moon_1_004:
	.byte		N24   , En3 , v032
	.byte		N24   , En4 , v096
	.byte	W36
	.byte		N12   , An3 
	.byte	W12
	.byte		        En4 
	.byte	W12
	.byte		        Gn4 
	.byte	W12
	.byte	PEND
@ 005   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_001
@ 006   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_002
@ 007   ----------------------------------------
	.byte		N24   , Bn3 , v096
	.byte	W36
	.byte		        An3 
	.byte	W36
@ 008   ----------------------------------------
mus_custom_garden_moon_1_008:
	.byte		N72   , Cn2 , v096
	.byte		N72   , An2 
	.byte		N72   , Dn3 
	.byte	W48
	.byte		N24   , Gn3 
	.byte	W24
	.byte	PEND
@ 009   ----------------------------------------
mus_custom_garden_moon_1_009:
	.byte		N72   , An1 , v096
	.byte		N72   , Gn2 
	.byte		N36   , Cn3 
	.byte	W36
	.byte		        Dn3 
	.byte	W36
	.byte	PEND
@ 010   ----------------------------------------
mus_custom_garden_moon_1_010:
	.byte		N72   , Dn2 , v096
	.byte		N72   , Cn3 
	.byte		N72   , Fn3 
	.byte		N36   , Gn3 
	.byte	W36
	.byte		        An3 
	.byte	W36
	.byte	PEND
@ 011   ----------------------------------------
mus_custom_garden_moon_1_011:
	.byte		N36   , Gn1 , v096
	.byte		N36   , An2 
	.byte		N36   , Cn3 
	.byte	W36
	.byte		        Gn3 
	.byte	W36
	.byte	PEND
@ 012   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_008
@ 013   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_009
@ 014   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_010
@ 015   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_011
@ 016   ----------------------------------------
mus_custom_garden_moon_1_016:
	.byte		N72   , An1 , v096
	.byte		N72   , Gn2 
	.byte		N48   , Cn3 
	.byte	W48
	.byte		N24   , Dn3 
	.byte	W24
	.byte	PEND
@ 017   ----------------------------------------
mus_custom_garden_moon_1_017:
	.byte		N72   , Gn1 , v096
	.byte		N72   , Fn2 
	.byte		N72   , Bn2 
	.byte	W48
	.byte		N24   , Cn3 
	.byte	W24
	.byte	PEND
@ 018   ----------------------------------------
mus_custom_garden_moon_1_018:
	.byte		N72   , Fn1 , v096
	.byte		N72   , Fn2 
	.byte		N72   , An2 
	.byte		N48   , Cn3 
	.byte	W48
	.byte		N24   , Fn3 
	.byte	W24
	.byte	PEND
@ 019   ----------------------------------------
mus_custom_garden_moon_1_019:
	.byte		N72   , Fn1 , v096
	.byte		N72   , Dn2 
	.byte		N72   , Gs2 
	.byte		N72   , Cn3 
	.byte	W48
	.byte		N24   , Gn3 
	.byte	W24
	.byte	PEND
@ 020   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_016
@ 021   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_017
@ 022   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_018
@ 023   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_019
@ 024   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_008
@ 025   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_009
@ 026   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_010
@ 027   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_011
@ 028   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_008
@ 029   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_009
@ 030   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_010
@ 031   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_011
@ 032   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_004
@ 033   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_001
@ 034   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_002
@ 035   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_003
@ 036   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_004
@ 037   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_001
@ 038   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_1_002
@ 039   ----------------------------------------
	.byte		N06   , Bn3 , v096
	.byte	W06
	.byte		        Cn4 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        En3 
	.byte	W18
	.byte		N12   , An3 
	.byte	W36
@ 040   ----------------------------------------
	.byte		TIE   , Dn3 
	.byte		TIE   , An3 
	.byte		TIE   , Cn4 
	.byte	W72
@ 041   ----------------------------------------
	.byte	W72
	.byte		EOT   , Dn3 
	.byte		        An3 
	.byte		        Cn4 
@ 042   ----------------------------------------
	.byte	FINE

@**************** Track 2 (Midi-Chn.3) ****************@

mus_custom_garden_moon_2:
	.byte	KEYSH , mus_custom_garden_moon_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 24
	.byte		VOL   , 127*mus_custom_garden_moon_mvl/mxv
	.byte		PAN   , c_v+28
	.byte		BEND  , c_v+0
	.byte		N72   , Fn2 , v096
	.byte		N72   , Cn3 
	.byte	W24
	.byte		N48   , An3 
	.byte		N48   , En4 
	.byte	W48
@ 001   ----------------------------------------
mus_custom_garden_moon_2_001:
	.byte		N72   , En2 , v096
	.byte		N72   , Cn3 
	.byte	W24
	.byte		N48   , Gn3 
	.byte		N48   , Dn4 
	.byte	W48
	.byte	PEND
@ 002   ----------------------------------------
mus_custom_garden_moon_2_002:
	.byte		N72   , Dn2 , v096
	.byte		N72   , An2 
	.byte	W24
	.byte		N48   , Fn3 
	.byte		N48   , Cn4 
	.byte	W48
	.byte	PEND
@ 003   ----------------------------------------
mus_custom_garden_moon_2_003:
	.byte		N72   , Cn2 , v096
	.byte		N72   , Gn2 
	.byte	W24
	.byte		N48   , En3 
	.byte		N48   , Bn3 
	.byte	W48
	.byte	PEND
@ 004   ----------------------------------------
	.byte		N72   , Fn2 
	.byte		N72   , Cn3 
	.byte	W24
	.byte		N48   , An3 
	.byte		N48   , En4 
	.byte	W48
@ 005   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_001
@ 006   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_002
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_003
@ 008   ----------------------------------------
mus_custom_garden_moon_2_008:
	.byte	W24
	.byte		N48   , An2 , v096
	.byte		N24   , Gn3 
	.byte		N12   , Cn4 
	.byte	W12
	.byte		        Bn3 
	.byte	W12
	.byte		N24   , En3 
	.byte	W24
	.byte	PEND
@ 009   ----------------------------------------
mus_custom_garden_moon_2_009:
	.byte	W24
	.byte		N48   , Gn2 , v096
	.byte		N48   , Bn2 
	.byte		N12   , Dn3 
	.byte	W12
	.byte		N36   , En3 
	.byte	W12
	.byte		N24   , Gn3 
	.byte	W24
	.byte	PEND
@ 010   ----------------------------------------
mus_custom_garden_moon_2_010:
	.byte	W24
	.byte		N48   , Fn2 , v096
	.byte		N48   , Cn3 
	.byte		N12   , Dn3 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		N24   , Gn3 
	.byte	W24
	.byte	PEND
@ 011   ----------------------------------------
mus_custom_garden_moon_2_011:
	.byte	W24
	.byte		N48   , Gn2 , v096
	.byte		N48   , Bn2 
	.byte		N48   , Cn3 
	.byte	W12
	.byte		N36   , En3 
	.byte	W36
	.byte	PEND
@ 012   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_008
@ 013   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_009
@ 014   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_010
@ 015   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_011
@ 016   ----------------------------------------
mus_custom_garden_moon_2_016:
	.byte	W24
	.byte		N12   , Cn3 , v096
	.byte		N12   , En3 
	.byte	W24
	.byte		        Bn2 
	.byte		N12   , An3 
	.byte	W24
	.byte	PEND
@ 017   ----------------------------------------
mus_custom_garden_moon_2_017:
	.byte		N12   , Bn2 , v096
	.byte		N12   , En3 
	.byte	W24
	.byte		        Dn3 
	.byte		N12   , En3 
	.byte	W24
	.byte		N24   , Cn3 
	.byte		N24   , An3 
	.byte	W24
	.byte	PEND
@ 018   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_016
@ 019   ----------------------------------------
mus_custom_garden_moon_2_019:
	.byte		N12   , Bn2 , v096
	.byte		N12   , En3 
	.byte	W24
	.byte		        Bn2 
	.byte		N12   , Dn3 
	.byte	W24
	.byte		N24   
	.byte		N24   , Bn3 
	.byte	W24
	.byte	PEND
@ 020   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_016
@ 021   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_017
@ 022   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_016
@ 023   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_019
@ 024   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_008
@ 025   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_009
@ 026   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_010
@ 027   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_011
@ 028   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_008
@ 029   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_009
@ 030   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_010
@ 031   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_011
@ 032   ----------------------------------------
mus_custom_garden_moon_2_032:
	.byte		N72   , Cn2 , v096
	.byte		N72   , An2 
	.byte		N72   , Dn3 
	.byte	W48
	.byte		N24   , Gn3 
	.byte	W24
	.byte	PEND
@ 033   ----------------------------------------
mus_custom_garden_moon_2_033:
	.byte		N72   , An1 , v096
	.byte		N72   , Gn2 
	.byte		N48   , Cn3 
	.byte	W48
	.byte		N24   , En3 
	.byte	W24
	.byte	PEND
@ 034   ----------------------------------------
mus_custom_garden_moon_2_034:
	.byte		N72   , Dn2 , v096
	.byte		N72   , Cn3 
	.byte		N48   , Fn3 
	.byte		N48   , Gn3 
	.byte	W48
	.byte		N24   , Dn3 
	.byte	W24
	.byte	PEND
@ 035   ----------------------------------------
mus_custom_garden_moon_2_035:
	.byte		N48   , Gn1 , v096
	.byte		N48   , An2 
	.byte		N48   , Cn3 
	.byte	W48
	.byte		N24   , Gn3 
	.byte	W24
	.byte	PEND
@ 036   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_032
@ 037   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_033
@ 038   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_034
@ 039   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_garden_moon_2_035
@ 040   ----------------------------------------
	.byte		TIE   , Cn2 , v096
	.byte		TIE   , En2 
	.byte		TIE   , Gn2 
	.byte	W72
@ 041   ----------------------------------------
	.byte	W72
	.byte		EOT   , Cn2 
	.byte		        En2 
	.byte		        Gn2 
@ 042   ----------------------------------------
	.byte	FINE

@******************************************************@
	.align	2

mus_custom_garden_moon:
	.byte	2	@ NumTrks
	.byte	0	@ NumBlks
	.byte	mus_custom_garden_moon_pri	@ Priority
	.byte	mus_custom_garden_moon_rev	@ Reverb.

	.word	mus_custom_garden_moon_grp

	.word	mus_custom_garden_moon_1
	.word	mus_custom_garden_moon_2

	.end
