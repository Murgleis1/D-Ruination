	.include "MPlayDef.s"

	.equ	mus_title_grp, voicegroup059
	.equ	mus_title_pri, 0
	.equ	mus_title_rev, reverb_set+50
	.equ	mus_title_mvl, 90
	.equ	mus_title_key, 0
	.equ	mus_title_tbs, 1
	.equ	mus_title_exg, 1
	.equ	mus_title_cmp, 1

	.section .rodata
	.global	mus_title
	.align	2

@**************** Track 1 (Midi-Chn.1) ****************@

mus_title_1:
	.byte		VOL   , 127*mus_title_mvl/mxv
	.byte	KEYSH , mus_title_key+0
@ 000   ----------------------------------------
	.byte	TEMPO , 100*mus_title_tbs/2
	.byte		VOICE , 73
	.byte		N48   , An3 , v084
	.byte	W48
	.byte		N12   , Fn3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		N24   , Fn3 
	.byte	W24
@ 001   ----------------------------------------
mus_title_1_001:
	.byte		N72   , Gn3 , v084
	.byte	W72
	.byte		N24   , Dn3 
	.byte	W24
	.byte	PEND
@ 002   ----------------------------------------
mus_title_1_002:
	.byte		N48   , Cn3 , v084
	.byte	W48
	.byte		N24   , An2 
	.byte	W24
	.byte		        Fn2 
	.byte	W24
	.byte	PEND
@ 003   ----------------------------------------
	.byte		N96   , Bn2 
	.byte	W96
@ 004   ----------------------------------------
mus_title_1_004:
	.byte		N48   , An3 , v084
	.byte	W48
	.byte		N12   , Fn3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		N24   , Fn3 
	.byte	W24
	.byte	PEND
@ 005   ----------------------------------------
mus_title_1_005:
	.byte		N12   , Gn3 , v084
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		N48   , Fn3 
	.byte	W48
	.byte		N24   , En3 
	.byte	W24
	.byte	PEND
@ 006   ----------------------------------------
mus_title_1_006:
	.byte		N48   , Dn3 , v084
	.byte	W48
	.byte		        En3 
	.byte	W48
	.byte	PEND
@ 007   ----------------------------------------
	.byte		N96   , Dn3 
	.byte	W96
@ 008   ----------------------------------------
	.byte	PATT
	 .word	mus_title_1_004
@ 009   ----------------------------------------
mus_title_1_009:
	.byte		N24   , Gn3 , v084
	.byte	W24
	.byte		N48   , Dn3 
	.byte	W48
	.byte		N24   
	.byte	W24
	.byte	PEND
@ 010   ----------------------------------------
	.byte	PATT
	 .word	mus_title_1_002
@ 011   ----------------------------------------
	.byte		N96   , Bn2 , v084
	.byte	W96
@ 012   ----------------------------------------
	.byte	PATT
	 .word	mus_title_1_004
@ 013   ----------------------------------------
	.byte	PATT
	 .word	mus_title_1_005
@ 014   ----------------------------------------
	.byte	PATT
	 .word	mus_title_1_006
@ 015   ----------------------------------------
	.byte		N72   , Dn3 , v084
	.byte	W72
	.byte		N24   , An3 , v096
	.byte	W24
@ 016   ----------------------------------------
	.byte		        Gn3 , v084
	.byte	W24
	.byte		        Cn3 
	.byte	W24
	.byte		        Dn3 
	.byte	W24
	.byte		        En3 
	.byte	W24
@ 017   ----------------------------------------
	.byte		N72   , Fn3 
	.byte	W72
	.byte		N24   , Dn3 
	.byte	W24
@ 018   ----------------------------------------
	.byte		N48   , Cn3 
	.byte	W48
	.byte		N24   , An2 
	.byte	W24
	.byte		        Fn2 , v096
	.byte	W24
@ 019   ----------------------------------------
	.byte		N12   , Gn2 , v084
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		        Gn3 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		N48   , Gn3 
	.byte	W48
@ 020   ----------------------------------------
	.byte	PATT
	 .word	mus_title_1_004
@ 021   ----------------------------------------
	.byte	PATT
	 .word	mus_title_1_009
@ 022   ----------------------------------------
mus_title_1_022:
	.byte		N24   , Fn3 , v084
	.byte	W24
	.byte		N12   , En3 
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		N24   , En3 
	.byte	W24
	.byte		        Cn3 
	.byte	W24
	.byte	PEND
@ 023   ----------------------------------------
	.byte		N36   , Dn3 
	.byte	W36
	.byte		N12   , Dn2 
	.byte	W12
	.byte		N48   
	.byte	W24
	.byte		N24   , An3 
	.byte	W24
@ 024   ----------------------------------------
	.byte		N24   
	.byte	W24
	.byte		N12   
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte		N24   , En3 
	.byte	W24
	.byte		N12   , Fn3 
	.byte	W12
	.byte		        Dn3 
	.byte	W12
@ 025   ----------------------------------------
	.byte		N24   , En3 
	.byte	W24
	.byte		        Cn3 
	.byte	W24
	.byte		        Dn3 , v072
	.byte	W24
	.byte		        An3 , v084
	.byte	W24
@ 026   ----------------------------------------
	.byte		N24   
	.byte	W24
	.byte		N24   
	.byte	W24
	.byte		N12   , Fn3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		N24   , Dn3 
	.byte	W24
@ 027   ----------------------------------------
	.byte		N36   , Gn3 
	.byte	W36
	.byte		N12   , Dn2 
	.byte	W12
	.byte		N48   
	.byte	W24
	.byte		N24   , An3 
	.byte	W24
@ 028   ----------------------------------------
	.byte		        Cn4 
	.byte	W24
	.byte		N12   , As3 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		N24   , Gn3 
	.byte	W24
	.byte		        An3 
	.byte	W24
@ 029   ----------------------------------------
	.byte		        Fn3 
	.byte	W24
	.byte		        En3 
	.byte	W24
	.byte		        Dn3 
	.byte	W24
	.byte		        An3 
	.byte	W24
@ 030   ----------------------------------------
	.byte	PATT
	 .word	mus_title_1_022
@ 031   ----------------------------------------
	.byte		N12   , Dn2 , v084
	.byte	W12
	.byte		        An2 
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		        Dn2 
	.byte	W12
@ 032   ----------------------------------------
	.byte		        Cn2 
	.byte	W12
	.byte		        An2 
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		        An2 
	.byte	W12
@ 033   ----------------------------------------
	.byte		        As1 
	.byte	W12
	.byte		        An2 
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		        As1 
	.byte	W12
@ 034   ----------------------------------------
	.byte		        Cn2 
	.byte	W12
	.byte		        An2 
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		        Cn2 
	.byte	W12
@ 035   ----------------------------------------
	.byte		        Dn2 
	.byte	W12
	.byte		        An2 
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Cn4 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Dn2 
	.byte	W12
@ 036   ----------------------------------------
mus_title_1_036:
	.byte		N12   , Cn2 , v084
	.byte	W12
	.byte		        An2 
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Cn4 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte	PEND
@ 037   ----------------------------------------
	.byte		        As1 
	.byte	W12
	.byte		        An2 
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Cn4 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        As1 
	.byte	W12
@ 038   ----------------------------------------
	.byte	PATT
	 .word	mus_title_1_036
@ 039   ----------------------------------------
	.byte		N12   , Dn2 , v084
	.byte	W12
	.byte		        An2 
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Cn4 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        An2 
	.byte	W12
@ 040   ----------------------------------------
	.byte		        Cn2 
	.byte	W12
	.byte		        An2 
	.byte	W12
	.byte		        Dn3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Cn4 
	.byte	W12
	.byte		        Dn4 
	.byte	W12
	.byte		N24   
	.byte	W24
@ 041   ----------------------------------------
	.byte		N72   , As1 
	.byte	W24
	.byte		N24   , Dn3 , v072
	.byte	W24
	.byte		N48   , Gn2 , v084
	.byte	W24
	.byte		N24   , As3 , v096
	.byte	W24
@ 042   ----------------------------------------
mus_title_1_042:
	.byte		N12   , Dn2 , v084
	.byte	W12
	.byte		        An2 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte		N48   , An3 
	.byte	W48
	.byte	PEND
@ 043   ----------------------------------------
mus_title_1_043:
	.byte		N24   , An3 , v084
	.byte	W48
	.byte		N12   , Fn3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte		N24   , Fn3 
	.byte	W24
	.byte	PEND
@ 044   ----------------------------------------
	.byte	PATT
	 .word	mus_title_1_001
@ 045   ----------------------------------------
	.byte	PATT
	 .word	mus_title_1_002
@ 046   ----------------------------------------
	.byte		N96   , Bn2 , v084
	.byte	W96
@ 047   ----------------------------------------
	.byte	PATT
	 .word	mus_title_1_043
@ 048   ----------------------------------------
	.byte	PATT
	 .word	mus_title_1_005
@ 049   ----------------------------------------
	.byte	PATT
	 .word	mus_title_1_006
@ 050   ----------------------------------------
	.byte	PATT
	 .word	mus_title_1_042
@ 051   ----------------------------------------
	.byte	FINE

@**************** Track 2 (Midi-Chn.2) ****************@

mus_title_2:
	.byte		VOL   , 127*mus_title_mvl/mxv
	.byte	KEYSH , mus_title_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 49
	.byte	W96
@ 001   ----------------------------------------
	.byte	W24
	.byte		N76   , Dn3 , v048
	.byte	W72
@ 002   ----------------------------------------
	.byte	W24
	.byte		N36   , An2 , v048, gtp2
	.byte	W72
@ 003   ----------------------------------------
	.byte	W96
@ 004   ----------------------------------------
	.byte	W96
@ 005   ----------------------------------------
	.byte	W96
@ 006   ----------------------------------------
	.byte	W96
@ 007   ----------------------------------------
	.byte		TIE   , An2 , v044
	.byte	W96
@ 008   ----------------------------------------
	.byte		N56   , An2 , v044, gtp1
	.byte		N36   , Dn3 , v044, gtp2
	.byte		N76   , Fn3 
	.byte	W24
	.byte		N14   , Dn3 , v048
	.byte	W24
	.byte		N76   , Gn2 , v044
	.byte		N76   , Cn3 
	.byte	W09
	.byte		EOT   , An2 
	.byte	W36
	.byte	W03
@ 009   ----------------------------------------
	.byte	W96
@ 010   ----------------------------------------
mus_title_2_010:
	.byte		N36   , An2 , v044, gtp2
	.byte	W24
	.byte		N14   , An2 , v048
	.byte	W72
	.byte	PEND
@ 011   ----------------------------------------
	.byte	W96
@ 012   ----------------------------------------
mus_title_2_012:
	.byte		N76   , An2 , v044
	.byte		N36   , Dn3 , v044, gtp2
	.byte		N76   , Fn3 
	.byte	W24
	.byte		N14   , Dn3 , v048
	.byte	W24
	.byte		N76   , Gn2 , v044
	.byte		N76   , Cn3 
	.byte	W48
	.byte	PEND
@ 013   ----------------------------------------
	.byte	W96
@ 014   ----------------------------------------
mus_title_2_014:
	.byte	W24
	.byte		N36   , As2 , v048, gtp2
	.byte	W48
	.byte		        Cn3 , v048, gtp2
	.byte	W24
	.byte	PEND
@ 015   ----------------------------------------
	.byte		TIE   , An2 , v044
	.byte	W96
@ 016   ----------------------------------------
	.byte	W19
	.byte		EOT   
	.byte	W76
	.byte	W01
@ 017   ----------------------------------------
	.byte	W96
@ 018   ----------------------------------------
	.byte	PATT
	 .word	mus_title_2_010
@ 019   ----------------------------------------
	.byte	W96
@ 020   ----------------------------------------
	.byte	PATT
	 .word	mus_title_2_012
@ 021   ----------------------------------------
	.byte	W96
@ 022   ----------------------------------------
	.byte	W96
@ 023   ----------------------------------------
	.byte		N56   , An2 , v044, gtp1
	.byte	W96
@ 024   ----------------------------------------
mus_title_2_024:
	.byte		N36   , An2 , v044, gtp2
	.byte		N36   , Dn3 , v044, gtp2
	.byte		N36   , Gn3 , v044, gtp2
	.byte	W96
	.byte	PEND
@ 025   ----------------------------------------
	.byte		        An2 , v044, gtp2
	.byte		N36   , Cn3 , v044, gtp2
	.byte	W96
@ 026   ----------------------------------------
	.byte	PATT
	 .word	mus_title_2_024
@ 027   ----------------------------------------
	.byte		N56   , As2 , v044, gtp1
	.byte		N56   , Dn3 , v044, gtp1
	.byte	W96
@ 028   ----------------------------------------
	.byte		N36   , Dn3 , v044, gtp2
	.byte		N36   , Fn3 , v044, gtp2
	.byte	W96
@ 029   ----------------------------------------
	.byte		        En3 , v044, gtp2
	.byte	W96
@ 030   ----------------------------------------
	.byte	W48
	.byte		N76   , Gn2 
	.byte		N36   , Cn3 , v044, gtp2
	.byte	W48
@ 031   ----------------------------------------
	.byte	W96
@ 032   ----------------------------------------
	.byte	W96
@ 033   ----------------------------------------
	.byte	W96
@ 034   ----------------------------------------
	.byte	W96
@ 035   ----------------------------------------
	.byte	W96
@ 036   ----------------------------------------
	.byte	W96
@ 037   ----------------------------------------
	.byte	W96
@ 038   ----------------------------------------
	.byte	W96
@ 039   ----------------------------------------
	.byte	W96
@ 040   ----------------------------------------
	.byte	W96
@ 041   ----------------------------------------
	.byte	W24
	.byte		        Fn2 , v036, gtp2
	.byte		N36   , An2 , v036, gtp2
	.byte	W48
	.byte		        Dn3 , v048, gtp2
	.byte		N36   , Fn3 , v048, gtp2
	.byte	W24
@ 042   ----------------------------------------
	.byte	W96
@ 043   ----------------------------------------
	.byte	PATT
	 .word	mus_title_2_012
@ 044   ----------------------------------------
	.byte	W24
	.byte		N76   , Dn3 , v048
	.byte	W72
@ 045   ----------------------------------------
	.byte	PATT
	 .word	mus_title_2_010
@ 046   ----------------------------------------
	.byte	W96
@ 047   ----------------------------------------
	.byte	PATT
	 .word	mus_title_2_012
@ 048   ----------------------------------------
	.byte	W96
@ 049   ----------------------------------------
	.byte	PATT
	 .word	mus_title_2_014
@ 050   ----------------------------------------
	.byte	W96
@ 051   ----------------------------------------
	.byte	FINE

@**************** Track 3 (Midi-Chn.3) ****************@

mus_title_3:
	.byte		VOL   , 127*mus_title_mvl/mxv
	.byte	KEYSH , mus_title_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 42
	.byte		N36   , Dn3 , v048
	.byte	W24
	.byte		N12   , Dn3 , v056
	.byte	W24
	.byte		N72   , Cn3 , v048
	.byte	W48
@ 001   ----------------------------------------
	.byte		TIE   , As2 
	.byte	W96
@ 002   ----------------------------------------
	.byte		        Fn2 
	.byte	W12
	.byte		EOT   , As2 
	.byte	W84
@ 003   ----------------------------------------
	.byte		TIE   , Gn2 
	.byte	W12
	.byte		EOT   , Fn2 
	.byte	W84
@ 004   ----------------------------------------
	.byte		N36   , Dn3 
	.byte	W24
	.byte		N12   , Dn3 , v056
	.byte	W24
	.byte		EOT   , Gn2 
	.byte		N72   , Cn3 , v048
	.byte	W48
@ 005   ----------------------------------------
	.byte		TIE   , As2 
	.byte	W72
	.byte		N36   , An2 
	.byte	W24
@ 006   ----------------------------------------
	.byte		N12   , As2 
	.byte	W12
	.byte		EOT   
	.byte	W12
	.byte		N12   , As2 , v056
	.byte	W24
	.byte		N36   , Cn3 , v048
	.byte	W24
	.byte		N12   , Cn3 , v056
	.byte	W24
@ 007   ----------------------------------------
	.byte		TIE   , Dn2 , v048
	.byte	W96
@ 008   ----------------------------------------
	.byte		N48   
	.byte	W48
	.byte		EOT   
	.byte		N72   , Cn2 
	.byte	W48
@ 009   ----------------------------------------
	.byte		TIE   , As1 
	.byte	W96
@ 010   ----------------------------------------
	.byte		        Fn2 
	.byte	W12
	.byte		EOT   , As1 
	.byte	W84
@ 011   ----------------------------------------
	.byte		TIE   , Gn2 
	.byte	W12
	.byte		EOT   , Fn2 
	.byte	W84
@ 012   ----------------------------------------
	.byte		N72   , Dn2 
	.byte	W48
	.byte		EOT   , Gn2 
	.byte		N72   , Cn2 
	.byte	W48
@ 013   ----------------------------------------
mus_title_3_013:
	.byte		TIE   , As1 , v048
	.byte	W72
	.byte		N36   , An1 
	.byte	W24
	.byte	PEND
@ 014   ----------------------------------------
	.byte		N12   , As1 
	.byte	W12
	.byte		EOT   
	.byte	W36
	.byte		N72   , An1 
	.byte	W48
@ 015   ----------------------------------------
	.byte		TIE   , Dn2 
	.byte	W96
@ 016   ----------------------------------------
	.byte		N12   
	.byte	W12
	.byte		EOT   
	.byte	W36
	.byte		TIE   , As1 
	.byte	W48
@ 017   ----------------------------------------
	.byte	W96
@ 018   ----------------------------------------
	.byte		        Fn2 
	.byte	W36
	.byte		EOT   , As1 
	.byte	W60
@ 019   ----------------------------------------
	.byte	W12
	.byte		        Fn2 
	.byte	W84
@ 020   ----------------------------------------
mus_title_3_020:
	.byte		N72   , Dn2 , v048
	.byte	W48
	.byte		        Cn2 
	.byte	W48
	.byte	PEND
@ 021   ----------------------------------------
	.byte		TIE   , As1 
	.byte	W96
@ 022   ----------------------------------------
	.byte		N12   
	.byte	W12
	.byte		EOT   
	.byte	W36
	.byte		N72   , An1 
	.byte	W48
@ 023   ----------------------------------------
	.byte		N54   , Dn2 
	.byte	W96
@ 024   ----------------------------------------
	.byte		N36   
	.byte	W96
@ 025   ----------------------------------------
	.byte		N36   
	.byte	W96
@ 026   ----------------------------------------
	.byte		N36   
	.byte	W36
	.byte		N90   , Dn2 , v056
	.byte	W60
@ 027   ----------------------------------------
	.byte		N30   , Dn2 , v048
	.byte	W96
@ 028   ----------------------------------------
	.byte		N36   , As2 
	.byte	W96
@ 029   ----------------------------------------
	.byte		        Cn3 
	.byte	W96
@ 030   ----------------------------------------
	.byte		N72   , As1 
	.byte	W48
	.byte		        Cn2 
	.byte	W48
@ 031   ----------------------------------------
	.byte	W96
@ 032   ----------------------------------------
	.byte	W96
@ 033   ----------------------------------------
	.byte	W96
@ 034   ----------------------------------------
	.byte	W96
@ 035   ----------------------------------------
	.byte	W96
@ 036   ----------------------------------------
	.byte	W96
@ 037   ----------------------------------------
	.byte	W96
@ 038   ----------------------------------------
	.byte	W96
@ 039   ----------------------------------------
	.byte	W96
@ 040   ----------------------------------------
	.byte	W96
@ 041   ----------------------------------------
	.byte	W96
@ 042   ----------------------------------------
	.byte	W96
@ 043   ----------------------------------------
	.byte	PATT
	 .word	mus_title_3_020
@ 044   ----------------------------------------
	.byte		TIE   , As1 , v048
	.byte	W96
@ 045   ----------------------------------------
	.byte		        Fn2 
	.byte	W12
	.byte		EOT   , As1 
	.byte	W84
@ 046   ----------------------------------------
	.byte		TIE   , Gn2 
	.byte	W12
	.byte		EOT   , Fn2 
	.byte	W84
@ 047   ----------------------------------------
	.byte		N72   , Dn2 
	.byte	W48
	.byte		EOT   , Gn2 
	.byte		N72   , Cn2 
	.byte	W48
@ 048   ----------------------------------------
	.byte	PATT
	 .word	mus_title_3_013
@ 049   ----------------------------------------
	.byte		N12   , As1 , v048
	.byte	W12
	.byte		EOT   
	.byte	W36
	.byte		N72   , An1 
	.byte	W48
@ 050   ----------------------------------------
	.byte	W96
@ 051   ----------------------------------------
	.byte	FINE

@******************************************************@
	.align	2

mus_title:
	.byte	3	@ NumTrks
	.byte	0	@ NumBlks
	.byte	mus_title_pri	@ Priority
	.byte	mus_title_rev	@ Reverb.

	.word	mus_title_grp

	.word	mus_title_1
	.word	mus_title_2
	.word	mus_title_3

	.end
