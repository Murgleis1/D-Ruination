	.include "MPlayDef.s"

	.equ	mus_custom_jetlag_grp, voicegroup193
	.equ	mus_custom_jetlag_pri, 4
	.equ	mus_custom_jetlag_rev, reverb_set+50
	.equ	mus_custom_jetlag_mvl, 75
	.equ	mus_custom_jetlag_key, 0
	.equ	mus_custom_jetlag_tbs, 1
	.equ	mus_custom_jetlag_exg, 1
	.equ	mus_custom_jetlag_cmp, 1

	.section .rodata
	.global	mus_custom_jetlag
	.align	2

@**************** Track 1 (Midi-Chn.1) ****************@

mus_custom_jetlag_1:
	.byte	KEYSH , mus_custom_jetlag_key+0
@ 000   ----------------------------------------
	.byte	TEMPO , 120*mus_custom_jetlag_tbs/2
	.byte		VOICE , 26
	.byte		VOL   , 95*mus_custom_jetlag_mvl/mxv
	.byte		PAN   , c_v-44
	.byte		BEND  , c_v+0
	.byte		N36   , Ds3 , v096
	.byte	W01
	.byte		N32   , Gs3 , v096, gtp2
	.byte	W02
	.byte		        Cs4 , v096, gtp1
	.byte	W32
	.byte	W01
	.byte		N48   , Fn3 
	.byte	W01
	.byte		N32   , Gs3 , v096, gtp2
	.byte	W02
	.byte		N21   , Ds4 
	.byte	W21
	.byte		N36   , Fn4 
	.byte	W12
	.byte		N24   , Cs4 
	.byte	W24
@ 001   ----------------------------------------
mus_custom_jetlag_1_001:
	.byte		N36   , Cn3 , v096
	.byte		N32   , Ds3 , v096, gtp3
	.byte	W01
	.byte		N10   , Gs3 
	.byte	W11
	.byte		N12   , As3 
	.byte	W12
	.byte		        Cs4 
	.byte	W12
	.byte		N60   , Cs3 
	.byte	W01
	.byte		N32   , Fn3 , v096, gtp2
	.byte	W02
	.byte		N21   , As3 
	.byte	W21
	.byte		N36   , Gs3 
	.byte	W12
	.byte		N24   , Cs3 
	.byte	W24
	.byte	PEND
@ 002   ----------------------------------------
mus_custom_jetlag_1_002:
	.byte		N24   , Gs2 , v096
	.byte		N24   , Cs3 
	.byte		N24   , Fn3 
	.byte	W36
	.byte		N48   , Cs2 
	.byte	W01
	.byte		N44   , As2 , v096, gtp2
	.byte	W02
	.byte		        Cs3 , v096, gtp1
	.byte	W01
	.byte		N42   , Gs3 , v096, gtp1
	.byte	W56
	.byte	PEND
@ 003   ----------------------------------------
mus_custom_jetlag_1_003:
	.byte		N84   , As1 , v096
	.byte	W01
	.byte		N80   , Gs2 , v096, gtp2
	.byte	W02
	.byte		N32   , Cn3 , v096, gtp1
	.byte	W32
	.byte	W01
	.byte		N48   , Cs3 
	.byte	W48
	.byte		N06   , Cs2 
	.byte	W06
	.byte		        Ds2 
	.byte	W06
	.byte	PEND
@ 004   ----------------------------------------
mus_custom_jetlag_1_004:
	.byte		N36   , Ds2 , v096
	.byte		N36   , Fn3 
	.byte	W12
	.byte		N12   , Gs3 
	.byte	W12
	.byte		        As3 
	.byte	W12
	.byte		N36   , As2 
	.byte		N36   , Fs3 
	.byte	W24
	.byte		        Cs3 
	.byte	W12
	.byte		N12   , Ds3 
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte	PEND
@ 005   ----------------------------------------
	.byte		N36   , Ds2 
	.byte		N36   , Cs3 
	.byte		N36   , Fn3 
	.byte	W36
	.byte		N48   , Ds3 
	.byte	W60
@ 006   ----------------------------------------
mus_custom_jetlag_1_006:
	.byte		N36   , Fs1 , v096
	.byte		N36   , Cs3 
	.byte	W12
	.byte		N24   , Cn3 
	.byte	W12
	.byte		N12   , Gs3 
	.byte	W12
	.byte		N48   , Cs2 
	.byte		N24   , Ds3 
	.byte	W24
	.byte		        Fn3 
	.byte	W24
	.byte		N06   , Cn3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte	PEND
@ 007   ----------------------------------------
	.byte		N36   , Ds2 
	.byte		N36   , Cs3 
	.byte		N36   , Fn3 
	.byte	W36
	.byte		N60   , Cs3 
	.byte	W24
	.byte		N36   , Gs2 
	.byte	W36
@ 008   ----------------------------------------
	.byte		N18   , As1 
	.byte		N18   , Cs3 
	.byte		N18   , As3 
	.byte	W18
	.byte		N06   , As2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		N18   , As2 
	.byte	W06
	.byte		N12   , Cs3 
	.byte	W06
	.byte		N06   , Fs3 
	.byte	W18
	.byte		N18   , Gs1 
	.byte		N18   , Gs2 
	.byte		N18   , Fn3 
	.byte	W12
@ 009   ----------------------------------------
	.byte	W06
	.byte		N06   , Fn2 
	.byte	W06
	.byte		        Fs2 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N18   , Fs2 
	.byte	W06
	.byte		N12   , Cs3 
	.byte	W06
	.byte		N06   , Fn3 
	.byte	W18
	.byte		N30   , Ds2 
	.byte		N30   , As2 
	.byte		N30   , Cs3 
	.byte	W12
@ 010   ----------------------------------------
mus_custom_jetlag_1_010:
	.byte	W18
	.byte		N18   , Fs2 , v096
	.byte		N18   , Fn3 
	.byte	W06
	.byte		N12   , Ds3 
	.byte	W12
	.byte		        Cn3 
	.byte	W12
	.byte		N36   , Fn1 
	.byte		N36   , As2 
	.byte		N12   , Ds3 
	.byte	W12
	.byte		        Gs3 
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte		N24   , As1 
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte	W12
	.byte	PEND
@ 011   ----------------------------------------
mus_custom_jetlag_1_011:
	.byte	W12
	.byte		N12   , Fn2 , v096
	.byte		N11   , Cs3 
	.byte	W01
	.byte		N10   , Fn3 
	.byte	W23
	.byte		N12   , Gs2 
	.byte		N12   , Cs3 
	.byte		N12   , Fn3 
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte		N24   , Cn2 
	.byte		N24   , Cn3 
	.byte		N24   , Ds3 
	.byte	W24
	.byte	PEND
@ 012   ----------------------------------------
	.byte		N18   , As1 
	.byte		N18   , Cs3 
	.byte		N18   , As3 
	.byte	W18
	.byte		N06   , As2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N12   , Ds2 
	.byte		N12   , Gs3 
	.byte	W18
	.byte		        Fn2 
	.byte		N12   , Fs3 
	.byte	W18
	.byte		N18   , Fs2 
	.byte		N12   , Cs3 
	.byte		N18   , Fn3 
	.byte	W12
@ 013   ----------------------------------------
	.byte	W06
	.byte		N06   , Fn2 
	.byte	W06
	.byte		        Fs2 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		N12   , Cs2 
	.byte		N12   , Ds3 
	.byte		N12   , Fs3 
	.byte	W18
	.byte		        As1 
	.byte		N12   , Cs3 
	.byte		N12   , Fn3 
	.byte	W18
	.byte		N30   , Ds2 
	.byte		N12   , As2 
	.byte		N30   , Cs3 
	.byte	W12
@ 014   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_010
@ 015   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_011
@ 016   ----------------------------------------
mus_custom_jetlag_1_016:
	.byte		N48   , Gs2 , v096
	.byte		N48   , Cs3 
	.byte		N48   , Ds3 
	.byte	W60
	.byte		N24   , Fn2 
	.byte		N24   , Cs3 
	.byte		N24   , Gs3 
	.byte	W24
	.byte		N12   , Fn2 
	.byte		N12   , Cs3 
	.byte		N12   , Fn3 
	.byte	W12
	.byte	PEND
@ 017   ----------------------------------------
mus_custom_jetlag_1_017:
	.byte		N18   , Fs2 , v096
	.byte		N18   , Cs3 
	.byte		N18   , Gs3 
	.byte	W18
	.byte		N06   , Fn3 
	.byte	W06
	.byte		N12   , As2 
	.byte	W12
	.byte		N06   , Fn3 
	.byte	W06
	.byte		N12   , Ds3 
	.byte	W12
	.byte		N06   , Cs3 
	.byte	W06
	.byte		N24   , As1 
	.byte		N24   , Cs3 
	.byte		N24   , Fn3 
	.byte	W24
	.byte		N12   , Gs1 
	.byte		N12   , Fn2 
	.byte		N12   , Cs3 
	.byte	W12
	.byte	PEND
@ 018   ----------------------------------------
mus_custom_jetlag_1_018:
	.byte		N18   , Fn2 , v096
	.byte		N18   , Ds3 
	.byte		N18   , Fs3 
	.byte	W18
	.byte		N06   , Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Gs3 
	.byte	W36
	.byte		        Fn3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte	PEND
@ 019   ----------------------------------------
mus_custom_jetlag_1_019:
	.byte		N24   , Gs1 , v096
	.byte		N12   , Fn2 
	.byte		N24   , Ds3 
	.byte	W12
	.byte		N12   , Fn2 
	.byte	W12
	.byte		        Gs3 
	.byte	W12
	.byte		N48   , As1 
	.byte		N48   , Cs3 
	.byte		N48   , Fn3 
	.byte	W48
	.byte		N06   , Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte	PEND
@ 020   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_016
@ 021   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_017
@ 022   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_018
@ 023   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_019
@ 024   ----------------------------------------
	.byte		N06   , As3 , v096
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Fn3 
	.byte	W12
	.byte		        As2 
	.byte	W12
	.byte		N42   , Gs2 
	.byte	W42
	.byte		N12   , As2 
	.byte	W12
@ 025   ----------------------------------------
	.byte	W06
	.byte		N06   , Cn3 
	.byte	W18
	.byte		N48   , Ds3 
	.byte		N48   , Cn4 
	.byte	W12
	.byte		N36   , Cs3 
	.byte	W36
	.byte		N12   , As2 
	.byte	W12
	.byte		        Fn3 , v032
	.byte		N12   , Fn4 , v096
	.byte	W12
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
	.byte		N18   , Fs1 
	.byte	W18
	.byte		N18   
	.byte	W18
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte		N24   , Fn3 
	.byte	W30
	.byte		N03   , Fs2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		N06   , Gs3 
	.byte	W06
	.byte		        As3 
	.byte	W06
@ 042   ----------------------------------------
mus_custom_jetlag_1_042:
	.byte		N18   , Gs1 , v096
	.byte	W18
	.byte		N42   
	.byte	W18
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte		N24   , Fs3 
	.byte	W24
	.byte		N36   , Gs1 
	.byte	W12
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte		N24   , Fn3 
	.byte	W24
	.byte	PEND
@ 043   ----------------------------------------
mus_custom_jetlag_1_043:
	.byte		N18   , Fs1 , v096
	.byte	W18
	.byte		N18   
	.byte	W18
	.byte		N36   , Fs2 
	.byte		N36   , As2 
	.byte		N36   , Cs3 
	.byte	W36
	.byte		N24   , Fs2 , v032
	.byte		N24   , As2 
	.byte		N24   , Cs3 
	.byte		N24   , Fs3 , v096
	.byte		N24   , As3 
	.byte		N24   , Cs4 
	.byte	W24
	.byte	PEND
@ 044   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_042
@ 045   ----------------------------------------
	.byte		N18   , Fs1 , v096
	.byte	W18
	.byte		N18   
	.byte	W18
	.byte		N06   
	.byte		N06   , Cs2 
	.byte	W12
	.byte		        Fs2 
	.byte		N06   , As2 
	.byte	W12
	.byte		        Cs3 
	.byte		N06   , Fn3 
	.byte	W12
	.byte		N06   
	.byte		N06   , Gs3 
	.byte	W12
	.byte		        Cs3 
	.byte		N06   , Fn3 
	.byte	W12
@ 046   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_042
@ 047   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_043
@ 048   ----------------------------------------
	.byte		N18   , Gs1 , v096
	.byte	W18
	.byte		N06   
	.byte	W30
	.byte		N48   , An1 
	.byte	W24
	.byte		N24   , Fs2 
	.byte		N24   , Cn3 
	.byte	W24
@ 049   ----------------------------------------
	.byte	W96
@ 050   ----------------------------------------
	.byte	W96
@ 051   ----------------------------------------
	.byte	W96
@ 052   ----------------------------------------
	.byte	W96
@ 053   ----------------------------------------
	.byte	W96
@ 054   ----------------------------------------
	.byte	W96
@ 055   ----------------------------------------
	.byte	W96
@ 056   ----------------------------------------
	.byte	W96
@ 057   ----------------------------------------
mus_custom_jetlag_1_057:
	.byte		N24   , As1 , v096
	.byte		N12   , As2 
	.byte		N24   , Cs3 
	.byte	W12
	.byte		N12   , Cn3 
	.byte	W12
	.byte		        Gs3 
	.byte	W12
	.byte		N60   , Cs2 
	.byte		N60   , Cs3 
	.byte		N60   , Ds3 
	.byte	W36
	.byte		N24   , Fn2 
	.byte	W24
	.byte	PEND
@ 058   ----------------------------------------
mus_custom_jetlag_1_058:
	.byte		N24   , Gs1 , v096
	.byte		N24   , Gs2 
	.byte		N12   , Cn3 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte		        Fn3 
	.byte	W72
	.byte	PEND
@ 059   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_057
@ 060   ----------------------------------------
	.byte		N24   , Gs1 , v096
	.byte		N24   , Gs2 
	.byte		N12   , Cn3 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte		        Gs2 
	.byte	W48
	.byte		N06   , Fn3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
@ 061   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_057
@ 062   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_058
@ 063   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_057
@ 064   ----------------------------------------
	.byte		N24   , Gs1 , v096
	.byte		N24   , Gs2 
	.byte		N12   , Cn3 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte		N18   , Fn3 
	.byte	W18
	.byte		        Ds3 
	.byte	W18
	.byte		        Cs3 
	.byte	W18
	.byte		        As2 
	.byte	W18
@ 065   ----------------------------------------
	.byte		N36   , Fs1 
	.byte		N36   , Fs2 
	.byte		N36   , Cs3 
	.byte	W36
	.byte		N36   
	.byte		N36   , Fn3 
	.byte	W60
@ 066   ----------------------------------------
	.byte		        Fn2 
	.byte		N36   , Cn3 
	.byte		N36   , Fn3 
	.byte		N36   , Gs3 
	.byte	W36
	.byte		N60   , Ds3 
	.byte		N60   , Fs3 
	.byte	W60
@ 067   ----------------------------------------
mus_custom_jetlag_1_067:
	.byte		N72   , As1 , v096
	.byte		N72   , Gs2 
	.byte		N72   , Cs3 
	.byte	W72
	.byte		N12   , Gs3 
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte	PEND
@ 068   ----------------------------------------
	.byte		N72   , Cn2 
	.byte		N72   , Gs2 
	.byte		N72   , Ds3 
	.byte	W72
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
@ 069   ----------------------------------------
	.byte		N36   , Fs1 
	.byte		N36   , Fs2 
	.byte		N36   , Cs3 
	.byte	W36
	.byte		N36   
	.byte		N36   , Fn3 
	.byte	W36
	.byte		N24   , Cn3 
	.byte		N24   , Ds3 
	.byte	W24
@ 070   ----------------------------------------
	.byte		N36   , Fn2 
	.byte		N36   , Cn3 
	.byte		N36   , Fn3 
	.byte		N36   , Gs3 
	.byte	W36
	.byte		N48   , Ds3 
	.byte		N48   , Fs3 
	.byte	W60
@ 071   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_067
@ 072   ----------------------------------------
	.byte		N72   , Cn2 , v096
	.byte		N72   , Gs2 
	.byte		N72   , Ds3 
	.byte	W96
@ 073   ----------------------------------------
	.byte		N36   , Fs1 
	.byte		N36   , Fs2 
	.byte		N36   , Cs3 
	.byte	W36
	.byte		        Fs3 
	.byte		N36   , As3 
	.byte	W36
	.byte		N24   , Fn3 
	.byte		N24   , Gs3 
	.byte	W24
@ 074   ----------------------------------------
	.byte		N36   , Fn2 
	.byte		N36   , Cn3 
	.byte		N36   , Ds3 
	.byte		N36   , Gs3 
	.byte	W36
	.byte		N48   , Ds3 
	.byte		N48   , Fs3 
	.byte	W48
	.byte		N12   , Fn3 
	.byte	W12
@ 075   ----------------------------------------
	.byte		N48   , As1 
	.byte		N48   , Gs2 
	.byte		N48   , Cs3 
	.byte		N48   , Cn4 
	.byte	W84
	.byte		N06   , Cs4 
	.byte	W12
@ 076   ----------------------------------------
	.byte		N72   , Ds4 
	.byte	W72
	.byte		N06   , Fs4 
	.byte	W06
	.byte		        Fn4 
	.byte	W06
	.byte		        Cs4 
	.byte	W06
	.byte		        Ds4 
	.byte	W06
@ 077   ----------------------------------------
mus_custom_jetlag_1_077:
	.byte		N36   , Fs3 , v096
	.byte		N36   , Cs4 
	.byte	W54
	.byte		N18   , Cn4 
	.byte		N18   , Ds4 
	.byte	W30
	.byte		N12   , Fn4 
	.byte		N12   , Gs4 
	.byte	W12
	.byte	PEND
@ 078   ----------------------------------------
mus_custom_jetlag_1_078:
	.byte		N36   , Fn2 , v096
	.byte		N36   , Cn3 
	.byte		N36   , Ds3 
	.byte		N36   , Gs3 
	.byte	W36
	.byte		N18   , Ds3 
	.byte		N18   , Fs3 
	.byte	W36
	.byte		N12   , Gs3 
	.byte		N12   , Cn4 
	.byte	W24
	.byte	PEND
@ 079   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_077
@ 080   ----------------------------------------
	.byte		N36   , Fn2 , v096
	.byte		N36   , Cn3 
	.byte		N36   , Ds3 
	.byte		N36   , Gs3 
	.byte	W36
	.byte		N18   , Ds3 
	.byte		N18   , Fs3 
	.byte	W36
	.byte		N24   , Gs3 
	.byte		N24   , Cs4 
	.byte	W24
@ 081   ----------------------------------------
	.byte		N60   , Fs3 
	.byte	W06
	.byte		N54   , Cn4 
	.byte	W06
	.byte		N48   , Cs4 
	.byte	W48
	.byte		N18   , Cn4 
	.byte		N18   , Ds4 
	.byte	W24
	.byte		N12   
	.byte		N12   , Fs4 
	.byte	W12
@ 082   ----------------------------------------
	.byte		N36   , Fn2 
	.byte		N36   , Cn3 
	.byte		N36   , Ds3 
	.byte		N36   , Gs3 
	.byte	W36
	.byte		N18   , Ds3 
	.byte		N18   , Fs3 
	.byte	W36
	.byte		N06   , Gs3 
	.byte		N06   , Cn4 
	.byte	W12
	.byte		        Gs3 
	.byte		N06   , Ds4 
	.byte	W12
@ 083   ----------------------------------------
	.byte		N36   , Cs4 
	.byte	W54
	.byte		N18   , Cn4 
	.byte		N18   , Ds4 
	.byte	W30
	.byte		N12   , Fn4 
	.byte		N12   , Gs4 
	.byte	W12
@ 084   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_078
@ 085   ----------------------------------------
	.byte		N96   , Cs2 , v096
	.byte	W01
	.byte		N32   , Ds3 , v096, gtp2
	.byte	W02
	.byte		        Gs3 , v096, gtp1
	.byte	W01
	.byte		N30   , Cs4 , v096, gtp1
	.byte	W32
	.byte		N48   , Fn3 
	.byte	W01
	.byte		N32   , Gs3 , v096, gtp2
	.byte	W02
	.byte		N21   , Ds4 
	.byte	W21
	.byte		N36   , Fn4 
	.byte	W12
	.byte		N24   , Cs4 
	.byte	W24
@ 086   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_001
@ 087   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_002
@ 088   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_003
@ 089   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_004
@ 090   ----------------------------------------
	.byte		N36   , Ds2 , v096
	.byte		N36   , Cs3 
	.byte		N36   , Fn3 
	.byte	W36
	.byte		N24   , Cs3 
	.byte	W24
	.byte		N36   , Cn3 
	.byte	W36
@ 091   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_1_006
@ 092   ----------------------------------------
	.byte		N36   , Ds2 , v096
	.byte		N36   , Cs3 
	.byte		N36   , Fn3 
	.byte	W36
	.byte		TIE   , Gs3 
	.byte	W60
@ 093   ----------------------------------------
	.byte	W48
	.byte		EOT   
	.byte	FINE

@**************** Track 2 (Midi-Chn.2) ****************@

mus_custom_jetlag_2:
	.byte	KEYSH , mus_custom_jetlag_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 26
	.byte		VOL   , 95*mus_custom_jetlag_mvl/mxv
	.byte		PAN   , c_v-44
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
	.byte	W96
@ 044   ----------------------------------------
	.byte	W96
@ 045   ----------------------------------------
	.byte	W96
@ 046   ----------------------------------------
	.byte	W96
@ 047   ----------------------------------------
	.byte	W96
@ 048   ----------------------------------------
	.byte	W96
@ 049   ----------------------------------------
	.byte	W96
@ 050   ----------------------------------------
	.byte	W96
@ 051   ----------------------------------------
	.byte	W96
@ 052   ----------------------------------------
	.byte	W96
@ 053   ----------------------------------------
	.byte	W96
@ 054   ----------------------------------------
	.byte	W96
@ 055   ----------------------------------------
	.byte	W96
@ 056   ----------------------------------------
	.byte	W96
@ 057   ----------------------------------------
	.byte	W96
@ 058   ----------------------------------------
	.byte	W96
@ 059   ----------------------------------------
	.byte	W96
@ 060   ----------------------------------------
	.byte	W60
	.byte		BEND  , c_v+0
	.byte		N12   , Fs3 , v096
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W24
@ 061   ----------------------------------------
	.byte	W96
@ 062   ----------------------------------------
	.byte	W96
@ 063   ----------------------------------------
	.byte	W96
@ 064   ----------------------------------------
	.byte	W96
@ 065   ----------------------------------------
	.byte	W96
@ 066   ----------------------------------------
	.byte	W96
@ 067   ----------------------------------------
	.byte	W96
@ 068   ----------------------------------------
	.byte	W96
@ 069   ----------------------------------------
	.byte	W96
@ 070   ----------------------------------------
	.byte	W96
@ 071   ----------------------------------------
	.byte	W96
@ 072   ----------------------------------------
	.byte	W96
@ 073   ----------------------------------------
	.byte	W96
@ 074   ----------------------------------------
	.byte	W96
@ 075   ----------------------------------------
	.byte	W96
@ 076   ----------------------------------------
	.byte	W96
@ 077   ----------------------------------------
	.byte	W96
@ 078   ----------------------------------------
	.byte	W96
@ 079   ----------------------------------------
	.byte	W96
@ 080   ----------------------------------------
	.byte	W96
@ 081   ----------------------------------------
	.byte	W96
@ 082   ----------------------------------------
	.byte	W96
@ 083   ----------------------------------------
	.byte		N04   , Gs3 , v127
	.byte	W04
	.byte		N30   , As3 , v096, gtp1
	.byte	W92
@ 084   ----------------------------------------
	.byte	W96
@ 085   ----------------------------------------
	.byte	W96
@ 086   ----------------------------------------
	.byte	W96
@ 087   ----------------------------------------
	.byte	W96
@ 088   ----------------------------------------
	.byte	W96
@ 089   ----------------------------------------
	.byte	W96
@ 090   ----------------------------------------
	.byte	W96
@ 091   ----------------------------------------
	.byte	W96
@ 092   ----------------------------------------
	.byte	W96
@ 093   ----------------------------------------
	.byte	W48
	.byte	FINE

@**************** Track 3 (Midi-Chn.3) ****************@

mus_custom_jetlag_3:
	.byte	KEYSH , mus_custom_jetlag_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 26
	.byte		VOL   , 94*mus_custom_jetlag_mvl/mxv
	.byte		PAN   , c_v+49
	.byte		BEND  , c_v+0
	.byte		N36   , Gs2 , v096
	.byte		N36   , Fn3 
	.byte		N12   , Gs3 
	.byte	W12
	.byte		N12   
	.byte	W12
	.byte		        Cs4 
	.byte	W12
	.byte		N60   , Gn2 
	.byte		N24   , As2 
	.byte		N60   , As3 
	.byte	W24
	.byte		N12   , Fn3 
	.byte	W12
	.byte		        Ds3 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
@ 001   ----------------------------------------
mus_custom_jetlag_3_001:
	.byte		N36   , Ds2 , v096
	.byte		N36   , Cs3 
	.byte		N12   , Ds3 
	.byte	W12
	.byte		N24   
	.byte	W12
	.byte		N12   , Gs3 
	.byte	W12
	.byte		N48   , Gs2 
	.byte		N24   , Cs3 
	.byte		N48   , Fn3 
	.byte	W24
	.byte		N24   , Cs3 
	.byte	W24
	.byte		N12   , Gs2 
	.byte	W12
	.byte	PEND
@ 002   ----------------------------------------
mus_custom_jetlag_3_002:
	.byte		N36   , Cs2 , v096
	.byte		N12   , As2 
	.byte		N12   , Ds3 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte		        As2 
	.byte	W12
	.byte		N60   , As1 
	.byte		N24   , Gs2 
	.byte		N36   , Cs3 
	.byte	W24
	.byte		N12   
	.byte	W12
	.byte		        Cn3 
	.byte	W12
	.byte		        Gs2 
	.byte	W12
	.byte	PEND
@ 003   ----------------------------------------
mus_custom_jetlag_3_003:
	.byte		N24   , As1 , v096
	.byte		N24   , As2 
	.byte		N24   , Ds3 
	.byte	W12
	.byte		N12   , Fn3 
	.byte	W12
	.byte		        Ds3 
	.byte	W12
	.byte		N60   , Cs2 
	.byte		N60   , As2 
	.byte		N60   , Cs3 
	.byte	W24
	.byte		N36   , Gs1 
	.byte	W36
	.byte	PEND
@ 004   ----------------------------------------
mus_custom_jetlag_3_004:
	.byte		TIE   , Ds2 , v096
	.byte		N96   , Cs3 
	.byte		N36   , Fn3 
	.byte	W36
	.byte		N24   , Ds3 
	.byte	W24
	.byte		N36   , Fn3 
	.byte	W12
	.byte		N24   , Gs3 
	.byte	W24
	.byte	PEND
@ 005   ----------------------------------------
	.byte		N60   , As1 
	.byte		N12   , Ds3 
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte		TIE   , Cs3 
	.byte	W12
	.byte		N24   , Gs2 
	.byte	W24
	.byte		N36   , Gs1 
	.byte	W36
@ 006   ----------------------------------------
mus_custom_jetlag_3_006:
	.byte		N36   , As1 , v096
	.byte		N36   , Gs2 
	.byte		N36   , Fn3 
	.byte	W36
	.byte		N24   , Ds3 
	.byte	W24
	.byte		N12   , Cs3 
	.byte	W12
	.byte	PEND
	.byte		EOT   
	.byte		N24   , Gs2 
	.byte	W24
	.byte		EOT   , Ds2 
@ 007   ----------------------------------------
	.byte		N60   , As1 
	.byte		N12   , Ds3 
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte		        Ds3 
	.byte	W12
	.byte		N24   , Cs3 
	.byte	W24
	.byte		N36   , Gs1 
	.byte		N36   , Cn3 
	.byte	W36
@ 008   ----------------------------------------
	.byte		N96   , Cs3 
	.byte	W96
@ 009   ----------------------------------------
	.byte	W96
@ 010   ----------------------------------------
	.byte	W96
@ 011   ----------------------------------------
	.byte	W96
@ 012   ----------------------------------------
	.byte		N36   , As1 
	.byte		N36   , Fn2 
	.byte		N36   , Cs3 
	.byte	W54
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        Gs3 
	.byte	W12
	.byte		        Ds3 
	.byte	W06
	.byte		        Fn3 
	.byte	W12
	.byte		N42   , Cs3 
	.byte	W06
@ 013   ----------------------------------------
	.byte		N36   , Gs1 
	.byte		N36   , Gs2 
	.byte	W54
	.byte		N06   , Ds3 
	.byte	W06
	.byte		        Fn3 
	.byte	W12
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W12
	.byte		        Cs3 
	.byte	W06
@ 014   ----------------------------------------
	.byte		N36   , Fs1 
	.byte		N36   , As2 
	.byte		N36   , Ds3 
	.byte	W60
	.byte		N06   
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
@ 015   ----------------------------------------
	.byte		N12   
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte		N36   , Ds3 
	.byte	W36
	.byte		N24   , Cs3 
	.byte		N24   , Gs3 
	.byte	W24
@ 016   ----------------------------------------
mus_custom_jetlag_3_016:
	.byte		N18   , Gs1 , v096
	.byte		N18   , Fn2 
	.byte		N18   , Cs3 
	.byte	W18
	.byte		N06   , Cn3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N12   , Fn3 
	.byte	W12
	.byte		N24   , Cs2 
	.byte		N24   , Fn2 
	.byte		N24   , Cs3 
	.byte	W24
	.byte		N06   
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte	PEND
@ 017   ----------------------------------------
	.byte		N18   , Gs1 
	.byte		N18   , Fs2 
	.byte		N18   , Fn3 
	.byte	W18
	.byte		N42   , Cs3 
	.byte	W18
	.byte		N24   , Gs3 
	.byte	W12
	.byte		N12   , Ds3 
	.byte	W12
	.byte		N24   , As1 
	.byte		N24   , Fn2 
	.byte		N24   , Cs3 
	.byte	W24
	.byte		N06   
	.byte	W06
	.byte		        Ds3 
	.byte	W06
@ 018   ----------------------------------------
mus_custom_jetlag_3_018:
	.byte		N18   , An2 , v096
	.byte		N18   , Ds3 
	.byte		N18   , Fs3 
	.byte	W48
	.byte		N12   , Fn3 
	.byte	W12
	.byte		N24   , Fn2 
	.byte		N24   , Gs2 
	.byte		N24   , Cs3 
	.byte	W24
	.byte		N06   
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte	PEND
@ 019   ----------------------------------------
mus_custom_jetlag_3_019:
	.byte		N12   , Ds3 , v096
	.byte	W12
	.byte		N06   , Fn3 
	.byte	W06
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N48   , As1 
	.byte		N48   , Gs2 
	.byte		N48   , Cs3 
	.byte	W60
	.byte	PEND
@ 020   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_016
@ 021   ----------------------------------------
	.byte		N18   , Gs1 , v096
	.byte		N18   , Fs2 
	.byte		N18   , Fn3 
	.byte	W18
	.byte		N42   , Cs3 
	.byte	W18
	.byte		N24   , Gs3 
	.byte	W12
	.byte		N12   , Ds3 
	.byte	W12
	.byte		N24   , Cs2 
	.byte		N24   , Fn2 
	.byte		N24   , Cs3 
	.byte	W24
	.byte		N06   
	.byte	W06
	.byte		        Ds3 
	.byte	W06
@ 022   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_018
@ 023   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_019
@ 024   ----------------------------------------
	.byte	W48
	.byte		N18   , Fn2 , v096
	.byte		N18   , Ds3 
	.byte	W18
	.byte		N12   , Cn3 
	.byte	W18
	.byte		N18   , Cs2 
	.byte		N18   , As2 
	.byte	W12
@ 025   ----------------------------------------
	.byte	W06
	.byte		N42   , Cn3 
	.byte	W06
	.byte		N36   , Fs1 
	.byte	W03
	.byte		N32   , Cs2 , v096, gtp1
	.byte	W32
	.byte	W01
	.byte		N03   , As1 
	.byte	W06
	.byte		        Fn2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Cs3 
	.byte	W18
	.byte		N06   , Gs1 
	.byte	W06
	.byte		        Gn1 
	.byte	W06
@ 026   ----------------------------------------
	.byte		N18   , Fs1 
	.byte	W18
	.byte		N18   
	.byte	W18
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte		N24   , Fn3 
	.byte	W30
	.byte		N03   , Fs2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		N06   , Gs3 
	.byte	W06
	.byte		        As3 
	.byte	W06
@ 027   ----------------------------------------
mus_custom_jetlag_3_027:
	.byte		N18   , Gs1 , v096
	.byte	W18
	.byte		N42   
	.byte	W18
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte		N24   , Fs3 
	.byte	W24
	.byte		N36   , Gs1 
	.byte	W12
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte		N24   , Fn3 
	.byte	W24
	.byte	PEND
@ 028   ----------------------------------------
	.byte		        As1 
	.byte	W24
	.byte		        Fn2 
	.byte		N24   , Gs2 
	.byte		N24   , Cs3 
	.byte	W24
	.byte		N12   , Cn2 
	.byte		N12   , As2 
	.byte		N12   , Ds3 
	.byte	W12
	.byte		        Fn3 
	.byte	W24
	.byte		N60   , Cs2 
	.byte		N60   , Gs2 
	.byte		N60   , Ds3 
	.byte	W12
@ 029   ----------------------------------------
	.byte	W48
	.byte		N48   , Gs1 
	.byte		N96   , Fs2 
	.byte		N48   , As2 
	.byte		N24   , Cs3 
	.byte	W24
	.byte		        Ds3 
	.byte	W24
@ 030   ----------------------------------------
mus_custom_jetlag_3_030:
	.byte		N24   , Ds2 , v096
	.byte		N24   , As2 
	.byte		N12   , Fs3 
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte		N24   , Fn1 
	.byte		N24   , Gs2 
	.byte		N12   , Ds3 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte		        Fs1 
	.byte		N48   , Fs2 
	.byte		N48   , As2 
	.byte	W12
	.byte		N12   , Fs1 
	.byte	W18
	.byte		N12   
	.byte	W18
	.byte	PEND
@ 031   ----------------------------------------
mus_custom_jetlag_3_031:
	.byte		N12   , Fn1 , v096
	.byte		N48   , Ds2 
	.byte		N48   , An2 
	.byte		N48   , Cs3 
	.byte	W12
	.byte		N12   , Fn1 
	.byte	W18
	.byte		N18   
	.byte	W18
	.byte		N48   , As1 
	.byte		N48   , Fn2 
	.byte		N48   , Cn3 
	.byte	W48
	.byte	PEND
@ 032   ----------------------------------------
	.byte		        Gs2 
	.byte	W03
	.byte		N44   , Bn2 , v096, gtp1
	.byte	W03
	.byte		N42   , Cs3 
	.byte	W03
	.byte		N36   , As3 , v096, gtp3
	.byte	W36
	.byte	W03
	.byte		N24   , As2 
	.byte	W03
	.byte		N21   , Cs3 
	.byte	W03
	.byte		N18   , Ds3 
	.byte	W03
	.byte		N15   , Cn4 
	.byte	W36
	.byte	W03
@ 033   ----------------------------------------
	.byte		N42   , As2 
	.byte	W12
	.byte		N30   , Cs3 
	.byte		N30   , Ds3 
	.byte		N18   , Cn4 
	.byte	W18
	.byte		N12   , Gs3 
	.byte	W18
	.byte		N36   , Gs2 
	.byte		N36   , As2 
	.byte		N36   , Ds3 
	.byte		N36   , Gn3 
	.byte	W36
	.byte		N06   , Gs1 
	.byte		N06   , Gs2 
	.byte	W06
	.byte		        Gn1 
	.byte		N06   , Gn2 
	.byte	W06
@ 034   ----------------------------------------
	.byte		N18   , Fs1 
	.byte		N18   , Fs2 
	.byte	W18
	.byte		        Fs1 
	.byte		N18   , Fs2 
	.byte	W18
	.byte		N24   
	.byte		N24   , Cs3 
	.byte		N24   , Fn3 
	.byte	W30
	.byte		N03   , Fs2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		N06   , Gs3 
	.byte	W06
	.byte		        As3 
	.byte	W06
@ 035   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_027
@ 036   ----------------------------------------
	.byte		N24   , As1 , v096
	.byte	W24
	.byte		        Fn2 
	.byte		N24   , Gs2 
	.byte		N24   , Cs3 
	.byte	W24
	.byte		N12   , Cn2 
	.byte		N12   , As2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		        Cn2 
	.byte		N12   , As2 
	.byte		N12   , Fn3 
	.byte	W18
	.byte		N60   , Cs2 
	.byte		N60   , Gs2 
	.byte		N60   , Ds3 
	.byte	W12
@ 037   ----------------------------------------
	.byte	W48
	.byte		N48   , Gs1 
	.byte		N96   , Fs2 
	.byte		N48   , As2 
	.byte		N48   , Cs3 
	.byte	W48
@ 038   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_030
@ 039   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_031
@ 040   ----------------------------------------
	.byte		N48   , Gs2 , v096
	.byte	W03
	.byte		N44   , Bn2 , v096, gtp1
	.byte	W03
	.byte		N42   , Cs3 
	.byte	W03
	.byte		N36   , As3 , v096, gtp3
	.byte	W36
	.byte	W03
	.byte		N12   , As2 
	.byte		N11   , Cs3 
	.byte	W01
	.byte		N10   , Ds3 
	.byte	W01
	.byte		N09   , Cn4 
	.byte	W44
	.byte	W02
@ 041   ----------------------------------------
mus_custom_jetlag_3_041:
	.byte	W24
	.byte		N06   , As2 , v096
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Gs3 
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte		        Ds3 
	.byte	W12
	.byte	PEND
@ 042   ----------------------------------------
mus_custom_jetlag_3_042:
	.byte		N06   , Cs3 , v096
	.byte	W06
	.byte		        As2 
	.byte	W12
	.byte		N06   
	.byte	W18
	.byte		        Gs3 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Cs4 
	.byte	W06
	.byte		        Ds4 
	.byte	W06
	.byte		        Fn4 
	.byte	W06
	.byte		        Cs4 
	.byte	W06
	.byte		N12   , Ds4 
	.byte	W12
	.byte		        Cs4 
	.byte	W12
	.byte	PEND
@ 043   ----------------------------------------
mus_custom_jetlag_3_043:
	.byte		N24   , Gs3 , v096
	.byte	W30
	.byte		N06   , Fn2 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		        As2 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Dn3 
	.byte	W06
	.byte		        En3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		        An3 
	.byte	W06
	.byte		        Cs4 
	.byte	W06
	.byte	PEND
@ 044   ----------------------------------------
	.byte		        Cn4 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W12
	.byte		N12   , Cs3 
	.byte	W12
	.byte		N54   , Gs3 
	.byte	W06
	.byte		N48   , Cn3 
	.byte	W54
@ 045   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_041
@ 046   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_042
@ 047   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_043
@ 048   ----------------------------------------
	.byte		N06   , Cn4 , v096
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W12
	.byte		N12   , Cs3 
	.byte	W12
	.byte		N36   , Gs3 
	.byte	W06
	.byte		N30   , Cn3 
	.byte	W30
	.byte		N24   , Fs2 
	.byte		N24   , Cn3 
	.byte		N24   , Ds3 
	.byte	W24
@ 049   ----------------------------------------
	.byte	W96
@ 050   ----------------------------------------
	.byte	W96
@ 051   ----------------------------------------
	.byte	W96
@ 052   ----------------------------------------
	.byte	W96
@ 053   ----------------------------------------
	.byte	W96
@ 054   ----------------------------------------
	.byte	W96
@ 055   ----------------------------------------
	.byte	W96
@ 056   ----------------------------------------
	.byte	W96
@ 057   ----------------------------------------
mus_custom_jetlag_3_057:
	.byte	W24
	.byte		N06   , Gs3 , v096
	.byte	W06
	.byte		        Fn3 
	.byte	W12
	.byte		N18   , Ds3 
	.byte	W18
	.byte		N06   , As2 
	.byte	W06
	.byte		        Gs2 
	.byte	W12
	.byte		        Cs3 
	.byte	W18
	.byte	PEND
@ 058   ----------------------------------------
	.byte		N36   , Ds3 
	.byte	W12
	.byte		N24   , Cs3 
	.byte	W12
	.byte		N12   , As2 
	.byte	W48
	.byte		N06   , Gs2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
@ 059   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_057
@ 060   ----------------------------------------
	.byte		N36   , Ds3 , v096
	.byte	W12
	.byte		N24   , Cs3 
	.byte	W12
	.byte		N12   , As2 
	.byte	W72
@ 061   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_057
@ 062   ----------------------------------------
	.byte		N12   , Ds3 , v096
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte		        As2 
	.byte	W72
@ 063   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_057
@ 064   ----------------------------------------
	.byte		N12   , Ds3 , v096
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte		N18   , As2 
	.byte	W18
	.byte		        Gs2 
	.byte	W18
	.byte		        Fs2 
	.byte	W18
	.byte		        Fn2 
	.byte	W18
@ 065   ----------------------------------------
mus_custom_jetlag_3_065:
	.byte		N36   , Cs2 , v096
	.byte		N36   , As2 
	.byte		N36   , Fn3 
	.byte	W72
	.byte		N24   , Fn2 
	.byte		N24   , Gs2 
	.byte		N24   , Ds3 
	.byte		N24   , Gs3 
	.byte	W24
	.byte	PEND
@ 066   ----------------------------------------
mus_custom_jetlag_3_066:
	.byte	W24
	.byte		N36   , Gs2 , v096
	.byte		N36   , Fn3 
	.byte		N36   , Fs3 
	.byte	W36
	.byte		        Ds3 
	.byte		N36   , Gs3 
	.byte	W36
	.byte	PEND
@ 067   ----------------------------------------
	.byte	W24
	.byte		        Gs2 
	.byte		N36   , Fn3 
	.byte	W36
	.byte		N12   , As2 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte		        Fn3 
	.byte	W12
@ 068   ----------------------------------------
	.byte		N36   , Cn3 
	.byte		N36   , Ds3 
	.byte	W36
	.byte		        Fn3 
	.byte	W36
	.byte		N24   , Cn2 
	.byte		N24   , As2 
	.byte		N24   , Ds3 
	.byte	W24
@ 069   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_065
@ 070   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_066
@ 071   ----------------------------------------
	.byte	W24
	.byte		N36   , Gs2 , v096
	.byte		N36   , Fn3 
	.byte		N36   , Gs3 
	.byte	W36
	.byte		N12   , Fn3 
	.byte	W12
	.byte		        As2 
	.byte	W12
	.byte		        Gs2 
	.byte	W12
@ 072   ----------------------------------------
mus_custom_jetlag_3_072:
	.byte		N36   , Ds2 , v096
	.byte		N36   , Gs2 
	.byte		N36   , Cn3 
	.byte	W48
	.byte		N24   , Cn2 
	.byte		N24   , Cn3 
	.byte		N24   , Fn3 
	.byte	W24
	.byte		        Gs3 
	.byte	W24
	.byte	PEND
@ 073   ----------------------------------------
	.byte		N36   , Cn3 
	.byte		N36   , Fn3 
	.byte		N36   , Gs3 
	.byte	W72
	.byte		N24   , Fn2 
	.byte		N24   , Gs2 
	.byte		N24   , Ds3 
	.byte		N24   , Gs3 
	.byte	W24
@ 074   ----------------------------------------
	.byte	W24
	.byte		N36   , Gs2 
	.byte		N36   , Fn3 
	.byte		N36   , Fs3 
	.byte	W36
	.byte		N18   , Ds3 
	.byte		N18   , Gs3 
	.byte	W18
	.byte		N36   , Cn4 
	.byte	W18
@ 075   ----------------------------------------
	.byte	W24
	.byte		        Cn3 
	.byte		N36   , Gs3 
	.byte	W12
	.byte		N24   , Fn4 
	.byte	W36
	.byte		N12   , Ds3 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
@ 076   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_072
@ 077   ----------------------------------------
mus_custom_jetlag_3_077:
	.byte		N36   , Cn3 , v096
	.byte		N36   , Fn3 
	.byte		N36   , Gs3 
	.byte	W36
	.byte		N18   , Fs3 
	.byte		N18   , As3 
	.byte	W36
	.byte		N12   , Cs4 
	.byte		N12   , Fn4 
	.byte	W24
	.byte	PEND
@ 078   ----------------------------------------
mus_custom_jetlag_3_078:
	.byte		N36   , Fn2 , v096
	.byte		N36   , Gs2 
	.byte		N36   , Ds3 
	.byte		N36   , Gs3 
	.byte	W54
	.byte		N18   , Fn3 
	.byte		N18   , Gs3 
	.byte	W30
	.byte		N12   
	.byte		N12   , Ds4 
	.byte	W12
	.byte	PEND
@ 079   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_077
@ 080   ----------------------------------------
	.byte		N36   , Fn2 , v096
	.byte		N36   , Gs2 
	.byte		N36   , Ds3 
	.byte		N36   , Gs3 
	.byte	W54
	.byte		N18   , Fn3 
	.byte		N18   , Gs3 
	.byte	W18
	.byte		N24   , Fs3 
	.byte		N24   , Gs3 
	.byte	W24
@ 081   ----------------------------------------
	.byte		N36   , Cn3 
	.byte		N36   , Fn3 
	.byte		N36   , Gs3 
	.byte	W36
	.byte		N18   , Fs3 
	.byte		N18   , As3 
	.byte	W36
	.byte		N12   , Ds4 
	.byte		N12   , Gs4 
	.byte	W24
@ 082   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_078
@ 083   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_077
@ 084   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_078
@ 085   ----------------------------------------
	.byte		N36   , Gs2 , v096
	.byte		N12   , Fn3 
	.byte		N12   , Gs3 
	.byte	W12
	.byte		N24   
	.byte	W12
	.byte		N12   , Cs4 
	.byte	W12
	.byte		N60   , Gn2 
	.byte		N24   , As2 
	.byte		N60   , As3 
	.byte	W24
	.byte		N12   , Fn3 
	.byte	W12
	.byte		        Ds3 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
@ 086   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_001
@ 087   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_002
@ 088   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_003
@ 089   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_004
@ 090   ----------------------------------------
	.byte		N60   , As1 , v096
	.byte		N12   , Ds3 
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte		        Ds3 
	.byte	W12
	.byte		TIE   , Cs3 
	.byte	W24
	.byte		N36   , Gs1 
	.byte	W36
@ 091   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_3_006
	.byte		EOT   , Cs3 
	.byte		N24   , Gs2 , v096
	.byte	W24
	.byte		EOT   , Ds2 
@ 092   ----------------------------------------
	.byte		N84   , As1 
	.byte		N12   , Ds3 
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte		        Ds3 
	.byte	W12
	.byte		TIE   , Cs3 
	.byte	W60
@ 093   ----------------------------------------
	.byte	W48
	.byte		EOT   
	.byte	FINE

@**************** Track 4 (Midi-Chn.4) ****************@

mus_custom_jetlag_4:
	.byte	KEYSH , mus_custom_jetlag_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 26
	.byte		VOL   , 94*mus_custom_jetlag_mvl/mxv
	.byte		PAN   , c_v+49
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
	.byte	W96
@ 044   ----------------------------------------
	.byte	W96
@ 045   ----------------------------------------
	.byte	W96
@ 046   ----------------------------------------
	.byte	W96
@ 047   ----------------------------------------
	.byte	W96
@ 048   ----------------------------------------
	.byte	W96
@ 049   ----------------------------------------
	.byte	W96
@ 050   ----------------------------------------
	.byte	W96
@ 051   ----------------------------------------
	.byte	W96
@ 052   ----------------------------------------
	.byte	W96
@ 053   ----------------------------------------
	.byte	W96
@ 054   ----------------------------------------
	.byte	W96
@ 055   ----------------------------------------
	.byte	W96
@ 056   ----------------------------------------
	.byte	W96
@ 057   ----------------------------------------
mus_custom_jetlag_4_057:
	.byte	W84
	.byte		BEND  , c_v+0
	.byte		N12   , Ds3 , v096
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W06
	.byte	PEND
@ 058   ----------------------------------------
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W96
@ 059   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_4_057
@ 060   ----------------------------------------
	.byte		BEND  , c_v+11
	.byte		        c_v+0
	.byte	W96
@ 061   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_4_057
@ 062   ----------------------------------------
	.byte		BEND  , c_v+11
	.byte		        c_v+0
	.byte	W96
@ 063   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_4_057
@ 064   ----------------------------------------
	.byte		BEND  , c_v+11
	.byte		        c_v+0
	.byte	W96
@ 065   ----------------------------------------
	.byte	W96
@ 066   ----------------------------------------
	.byte	W96
@ 067   ----------------------------------------
	.byte	W96
@ 068   ----------------------------------------
	.byte	W96
@ 069   ----------------------------------------
	.byte	W96
@ 070   ----------------------------------------
	.byte	W96
@ 071   ----------------------------------------
	.byte	W96
@ 072   ----------------------------------------
	.byte	W96
@ 073   ----------------------------------------
	.byte	W96
@ 074   ----------------------------------------
	.byte	W96
@ 075   ----------------------------------------
	.byte	W96
@ 076   ----------------------------------------
	.byte	W96
@ 077   ----------------------------------------
	.byte	W96
@ 078   ----------------------------------------
	.byte	W96
@ 079   ----------------------------------------
	.byte	W96
@ 080   ----------------------------------------
	.byte	W96
@ 081   ----------------------------------------
	.byte	W96
@ 082   ----------------------------------------
	.byte	W96
@ 083   ----------------------------------------
	.byte	W96
@ 084   ----------------------------------------
	.byte	W96
@ 085   ----------------------------------------
	.byte	W96
@ 086   ----------------------------------------
	.byte	W96
@ 087   ----------------------------------------
	.byte	W96
@ 088   ----------------------------------------
	.byte	W96
@ 089   ----------------------------------------
	.byte	W96
@ 090   ----------------------------------------
	.byte	W96
@ 091   ----------------------------------------
	.byte	W96
@ 092   ----------------------------------------
	.byte	W96
@ 093   ----------------------------------------
	.byte	W48
	.byte	FINE

@**************** Track 5 (Midi-Chn.5) ****************@

mus_custom_jetlag_5:
	.byte	KEYSH , mus_custom_jetlag_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 33
	.byte		VOL   , 127*mus_custom_jetlag_mvl/mxv
	.byte		PAN   , c_v-1
	.byte		BEND  , c_v+0
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
mus_custom_jetlag_5_008:
	.byte		N48   , As0 , v096
	.byte	W48
	.byte		N12   , Cs1 
	.byte	W18
	.byte		N06   , Cn1 
	.byte	W18
	.byte		N60   , Gs0 
	.byte	W12
	.byte	PEND
@ 009   ----------------------------------------
mus_custom_jetlag_5_009:
	.byte	W48
	.byte		N12   , Gs0 , v096
	.byte	W18
	.byte		N06   , Fs0 
	.byte	W18
	.byte		N60   , Ds1 
	.byte	W12
	.byte	PEND
@ 010   ----------------------------------------
mus_custom_jetlag_5_010:
	.byte	W48
	.byte		N24   , Fn0 , v096
	.byte	W36
	.byte		N60   , Fs0 
	.byte	W12
	.byte	PEND
@ 011   ----------------------------------------
mus_custom_jetlag_5_011:
	.byte	W60
	.byte		N12   , Gs0 , v096
	.byte	W12
	.byte		N24   , An0 
	.byte	W24
	.byte	PEND
@ 012   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_5_008
@ 013   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_5_009
@ 014   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_5_010
@ 015   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_5_011
@ 016   ----------------------------------------
	.byte		N48   , Cs1 , v096
	.byte	W60
	.byte		N24   
	.byte	W24
	.byte		N06   , Fn0 
	.byte	W06
	.byte		N06   
	.byte	W06
@ 017   ----------------------------------------
mus_custom_jetlag_5_017:
	.byte		N18   , Fs0 , v096
	.byte	W18
	.byte		N06   
	.byte	W06
	.byte		N12   
	.byte	W12
	.byte		        Gs0 
	.byte	W24
	.byte		N36   , As0 
	.byte	W36
	.byte	PEND
@ 018   ----------------------------------------
mus_custom_jetlag_5_018:
	.byte		N18   , An0 , v096
	.byte	W18
	.byte		N06   
	.byte	W06
	.byte		N12   
	.byte	W12
	.byte		N12   
	.byte	W24
	.byte		N18   , Fs0 
	.byte	W18
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte	W06
	.byte	PEND
@ 019   ----------------------------------------
mus_custom_jetlag_5_019:
	.byte		N18   , Gs0 , v096
	.byte	W18
	.byte		N18   
	.byte	W18
	.byte		N48   , As0 
	.byte	W60
	.byte	PEND
@ 020   ----------------------------------------
	.byte		        Cs1 
	.byte	W60
	.byte		N24   
	.byte	W24
	.byte		N12   , Fn0 
	.byte	W12
@ 021   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_5_017
@ 022   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_5_018
@ 023   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_5_019
@ 024   ----------------------------------------
	.byte	W96
@ 025   ----------------------------------------
	.byte	W84
	.byte		N06   , Gs0 , v096
	.byte	W06
	.byte		        Gn0 
	.byte	W06
@ 026   ----------------------------------------
mus_custom_jetlag_5_026:
	.byte		N18   , Fs0 , v096
	.byte	W18
	.byte		N18   
	.byte	W18
	.byte		N48   
	.byte	W48
	.byte		N12   
	.byte	W12
	.byte	PEND
@ 027   ----------------------------------------
mus_custom_jetlag_5_027:
	.byte		N18   , Gs0 , v096
	.byte	W18
	.byte		N18   
	.byte	W18
	.byte		N24   
	.byte	W24
	.byte		N12   
	.byte	W12
	.byte		N24   
	.byte	W24
	.byte	PEND
@ 028   ----------------------------------------
	.byte		N48   , As0 
	.byte	W48
	.byte		N12   , Cn1 
	.byte	W12
	.byte		N12   
	.byte	W24
	.byte		N24   , Cs1 
	.byte	W12
@ 029   ----------------------------------------
mus_custom_jetlag_5_029:
	.byte	W12
	.byte		N18   , Cs1 , v096
	.byte	W18
	.byte		N18   
	.byte	W18
	.byte		N48   , Gs0 
	.byte	W48
	.byte	PEND
@ 030   ----------------------------------------
mus_custom_jetlag_5_030:
	.byte		N24   , Ds1 , v096
	.byte	W24
	.byte		        Fn1 
	.byte	W24
	.byte		N12   , Fs0 
	.byte	W12
	.byte		N12   
	.byte	W18
	.byte		N18   
	.byte	W18
	.byte	PEND
@ 031   ----------------------------------------
mus_custom_jetlag_5_031:
	.byte		N12   , Fn0 , v096
	.byte	W12
	.byte		N12   
	.byte	W18
	.byte		N06   , Gs0 
	.byte	W06
	.byte		N12   , An0 
	.byte	W12
	.byte		N48   , As0 
	.byte	W48
	.byte	PEND
@ 032   ----------------------------------------
	.byte		        Cs1 
	.byte	W48
	.byte		N24   , Ds1 
	.byte	W48
@ 033   ----------------------------------------
	.byte		N12   , Cs1 
	.byte	W12
	.byte		        Cn1 
	.byte	W18
	.byte		        Gs0 
	.byte	W18
	.byte		N36   , As0 
	.byte	W36
	.byte		N06   , Gs0 
	.byte	W06
	.byte		        Gn0 
	.byte	W06
@ 034   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_5_026
@ 035   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_5_027
@ 036   ----------------------------------------
	.byte		N48   , As0 , v096
	.byte	W48
	.byte		N12   , Cn1 
	.byte	W18
	.byte		N12   
	.byte	W18
	.byte		N24   , Cs1 
	.byte	W12
@ 037   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_5_029
@ 038   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_5_030
@ 039   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_5_031
@ 040   ----------------------------------------
	.byte		N48   , Cs1 , v096
	.byte	W48
	.byte		N12   , Ds1 
	.byte	W48
@ 041   ----------------------------------------
mus_custom_jetlag_5_041:
	.byte		N18   , Fs0 , v096
	.byte	W18
	.byte		N54   
	.byte	W54
	.byte		N24   
	.byte	W24
	.byte	PEND
@ 042   ----------------------------------------
mus_custom_jetlag_5_042:
	.byte		N18   , Gs0 , v096
	.byte	W18
	.byte		N54   
	.byte	W54
	.byte		N24   
	.byte	W24
	.byte	PEND
@ 043   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_5_041
@ 044   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_5_042
@ 045   ----------------------------------------
	.byte		N18   , Fs0 , v096
	.byte	W18
	.byte		N12   
	.byte	W18
	.byte		N06   
	.byte	W12
	.byte		        As0 
	.byte	W12
	.byte		        Cs1 
	.byte	W12
	.byte		        Fn1 
	.byte	W12
	.byte		        Fs0 
	.byte	W12
@ 046   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_5_042
@ 047   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_5_041
@ 048   ----------------------------------------
	.byte		N18   , Gs0 , v096
	.byte	W18
	.byte		N06   
	.byte	W30
	.byte		N18   , An0 
	.byte	W18
	.byte		N06   , Cn1 
	.byte	W06
	.byte		        Cs1 
	.byte	W06
	.byte		        Ds1 
	.byte	W06
	.byte		        Fn1 
	.byte	W06
	.byte		        Gs1 
	.byte	W06
@ 049   ----------------------------------------
	.byte	W12
	.byte		N12   , As0 
	.byte	W18
	.byte		N06   , Fs1 
	.byte	W06
	.byte		        Fn1 
	.byte	W06
	.byte		        Ds1 
	.byte	W06
	.byte		        Cs1 
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte	W12
	.byte		N60   , Gs0 
	.byte	W12
@ 050   ----------------------------------------
	.byte	W48
	.byte		N12   
	.byte	W18
	.byte		        Fs0 
	.byte	W18
	.byte		N60   , Ds1 
	.byte	W12
@ 051   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_5_010
@ 052   ----------------------------------------
	.byte	W60
	.byte		N12   , An0 , v096
	.byte	W12
	.byte		N24   , An1 
	.byte	W24
@ 053   ----------------------------------------
	.byte		N18   , As0 
	.byte	W18
	.byte		        Fn1 
	.byte	W18
	.byte		N12   , Cn2 
	.byte	W12
	.byte		N06   , Cs1 
	.byte		N06   , Cs2 
	.byte	W06
	.byte		        Cs1 
	.byte		N06   , Cs2 
	.byte	W12
	.byte		N12   , Cn1 
	.byte		N12   , Cn2 
	.byte	W18
	.byte		N18   , Gs0 
	.byte		N18   , Gs1 
	.byte	W12
@ 054   ----------------------------------------
	.byte	W06
	.byte		N03   , Gs0 
	.byte	W06
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte	W24
	.byte		N12   , Fs0 
	.byte		N12   , Fs1 
	.byte	W18
	.byte		N06   , Fs0 
	.byte		N06   , Fs1 
	.byte	W06
	.byte		N12   , Fs0 
	.byte		N12   , Fs1 
	.byte	W12
	.byte		N60   , Ds1 
	.byte	W12
@ 055   ----------------------------------------
	.byte	W48
	.byte		N18   , Fn0 
	.byte	W18
	.byte		N12   
	.byte	W18
	.byte		N60   , Fs0 
	.byte	W12
@ 056   ----------------------------------------
	.byte	W60
	.byte		N12   , Gs0 
	.byte	W12
	.byte		N24   
	.byte	W24
@ 057   ----------------------------------------
mus_custom_jetlag_5_057:
	.byte		N06   , As0 , v096
	.byte	W12
	.byte		N06   
	.byte	W06
	.byte		N12   
	.byte	W18
	.byte		N48   , Cs1 
	.byte	W60
	.byte	PEND
@ 058   ----------------------------------------
	.byte		N36   , Gs0 
	.byte	W96
@ 059   ----------------------------------------
mus_custom_jetlag_5_059:
	.byte		N06   , As0 , v096
	.byte	W12
	.byte		N06   
	.byte	W06
	.byte		N12   
	.byte	W18
	.byte		N48   , Ds1 
	.byte	W48
	.byte		N12   , Fn1 
	.byte	W12
	.byte	PEND
@ 060   ----------------------------------------
	.byte		N36   , Cs1 
	.byte	W96
@ 061   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_5_057
@ 062   ----------------------------------------
	.byte		N36   , Gs0 , v096
	.byte	W96
@ 063   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_5_059
@ 064   ----------------------------------------
	.byte		N96   , Cs1 , v096
	.byte	W96
@ 065   ----------------------------------------
	.byte		        Fs0 
	.byte	W96
@ 066   ----------------------------------------
	.byte		        Gs0 
	.byte	W96
@ 067   ----------------------------------------
	.byte		        As0 
	.byte	W96
@ 068   ----------------------------------------
	.byte		        Cn1 
	.byte	W96
@ 069   ----------------------------------------
	.byte		        Fs0 
	.byte	W96
@ 070   ----------------------------------------
	.byte		        Gs0 
	.byte	W96
@ 071   ----------------------------------------
	.byte		        As0 
	.byte	W96
@ 072   ----------------------------------------
	.byte		        Cn1 
	.byte	W96
@ 073   ----------------------------------------
	.byte		        Fs0 
	.byte	W96
@ 074   ----------------------------------------
	.byte		        Gs0 
	.byte	W96
@ 075   ----------------------------------------
	.byte		        As0 
	.byte	W96
@ 076   ----------------------------------------
	.byte		        Cn1 
	.byte	W96
@ 077   ----------------------------------------
	.byte		        Fs0 
	.byte	W96
@ 078   ----------------------------------------
	.byte		        Gs0 
	.byte	W96
@ 079   ----------------------------------------
	.byte		        Fs0 
	.byte	W96
@ 080   ----------------------------------------
	.byte		        Gs0 
	.byte	W96
@ 081   ----------------------------------------
	.byte		        Fs0 
	.byte	W96
@ 082   ----------------------------------------
	.byte		        Gs0 
	.byte	W96
@ 083   ----------------------------------------
	.byte		        Fs0 
	.byte	W96
@ 084   ----------------------------------------
	.byte		        Gs0 
	.byte	W96
@ 085   ----------------------------------------
	.byte		TIE   , Cs1 
	.byte	W96
@ 086   ----------------------------------------
	.byte	W96
	.byte		EOT   
@ 087   ----------------------------------------
	.byte	FINE

@**************** Track 6 (Midi-Chn.6) ****************@

mus_custom_jetlag_6:
	.byte	KEYSH , mus_custom_jetlag_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 33
	.byte		VOL   , 127*mus_custom_jetlag_mvl/mxv
	.byte		PAN   , c_v-1
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
	.byte	W96
@ 044   ----------------------------------------
	.byte	W96
@ 045   ----------------------------------------
	.byte	W96
@ 046   ----------------------------------------
	.byte	W96
@ 047   ----------------------------------------
	.byte	W96
@ 048   ----------------------------------------
	.byte	W96
@ 049   ----------------------------------------
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		N12   , Gs1 , v096
	.byte	W01
	.byte		BEND  , c_v+2
	.byte		        c_v+3
	.byte	W01
	.byte		        c_v+4
	.byte		        c_v+5
	.byte	W01
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte	W01
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W84
@ 050   ----------------------------------------
	.byte	W96
@ 051   ----------------------------------------
	.byte	W96
@ 052   ----------------------------------------
	.byte	W96
@ 053   ----------------------------------------
	.byte	W96
@ 054   ----------------------------------------
	.byte	W36
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		N12   , Fn1 
	.byte	W01
	.byte		BEND  , c_v+2
	.byte		        c_v+3
	.byte	W01
	.byte		        c_v+4
	.byte	W01
	.byte		        c_v+5
	.byte		        c_v+5
	.byte	W09
	.byte		        c_v+5
	.byte		        c_v+0
	.byte	W48
@ 055   ----------------------------------------
	.byte	W96
@ 056   ----------------------------------------
	.byte	W96
@ 057   ----------------------------------------
	.byte	W96
@ 058   ----------------------------------------
	.byte	W96
@ 059   ----------------------------------------
	.byte	W96
@ 060   ----------------------------------------
	.byte	W96
@ 061   ----------------------------------------
	.byte	W96
@ 062   ----------------------------------------
	.byte	W72
	.byte		        c_v+0
	.byte		N24   , As0 
	.byte	W01
	.byte		BEND  , c_v-1
	.byte	W02
	.byte		        c_v-2
	.byte	W01
	.byte		        c_v-3
	.byte	W02
	.byte		        c_v-4
	.byte	W02
	.byte		        c_v-5
	.byte	W01
	.byte		        c_v-6
	.byte	W02
	.byte		        c_v-7
	.byte	W02
	.byte		        c_v-8
	.byte	W01
	.byte		        c_v-9
	.byte	W02
	.byte		        c_v-10
	.byte	W01
	.byte		        c_v-11
	.byte	W01
	.byte		        c_v-11
	.byte	W06
@ 063   ----------------------------------------
	.byte		        c_v-11
	.byte		        c_v+0
	.byte	W96
@ 064   ----------------------------------------
	.byte	W96
@ 065   ----------------------------------------
	.byte	W96
@ 066   ----------------------------------------
	.byte	W96
@ 067   ----------------------------------------
	.byte	W96
@ 068   ----------------------------------------
	.byte	W96
@ 069   ----------------------------------------
	.byte	W96
@ 070   ----------------------------------------
	.byte	W96
@ 071   ----------------------------------------
	.byte	W96
@ 072   ----------------------------------------
	.byte	W96
@ 073   ----------------------------------------
	.byte	W96
@ 074   ----------------------------------------
	.byte	W96
@ 075   ----------------------------------------
	.byte	W96
@ 076   ----------------------------------------
	.byte	W96
@ 077   ----------------------------------------
	.byte	W96
@ 078   ----------------------------------------
	.byte	W96
@ 079   ----------------------------------------
	.byte	W96
@ 080   ----------------------------------------
	.byte	W96
@ 081   ----------------------------------------
	.byte	W96
@ 082   ----------------------------------------
	.byte	W96
@ 083   ----------------------------------------
	.byte	W96
@ 084   ----------------------------------------
	.byte	W96
@ 085   ----------------------------------------
	.byte	W96
@ 086   ----------------------------------------
	.byte	W96
@ 087   ----------------------------------------
	.byte	FINE

@**************** Track 7 (Midi-Chn.10) ****************@

mus_custom_jetlag_7:
	.byte	KEYSH , mus_custom_jetlag_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 0
	.byte		VOL   , 86*mus_custom_jetlag_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		BEND  , c_v+0
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
	.byte	W72
	.byte		N12   , As1 , v096
	.byte		N12   
	.byte	W12
	.byte		N06   , En1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
@ 028   ----------------------------------------
mus_custom_jetlag_7_028:
	.byte		N12   , Cn1 , v096
	.byte		N12   
	.byte		N12   , As1 
	.byte		N12   
	.byte	W12
	.byte		        Cn1 
	.byte		N12   
	.byte	W12
	.byte		N06   , En1 
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		N12   
	.byte		N12   
	.byte		N12   , As1 
	.byte		N12   
	.byte	W18
	.byte		N06   , En1 
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 029   ----------------------------------------
mus_custom_jetlag_7_029:
	.byte		N12   , As1 , v096
	.byte		N12   
	.byte	W12
	.byte		        Cn1 
	.byte		N12   
	.byte	W12
	.byte		N06   , As1 
	.byte		N06   
	.byte	W06
	.byte		N12   , Cn1 
	.byte		N12   
	.byte	W18
	.byte		N24   
	.byte		N24   
	.byte		N24   , As1 
	.byte		N24   
	.byte	W24
	.byte		N12   , En1 
	.byte		N11   
	.byte	W12
	.byte		N12   , Cn1 
	.byte		N12   
	.byte	W12
	.byte	PEND
@ 030   ----------------------------------------
mus_custom_jetlag_7_030:
	.byte		N06   , Cn1 , v096
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   , Gn2 
	.byte	W06
	.byte		        Bn1 
	.byte		N06   
	.byte	W06
	.byte		N12   
	.byte		N12   
	.byte	W12
	.byte		        An1 
	.byte		N12   
	.byte		N12   , As1 
	.byte		N12   , Gn2 
	.byte	W12
	.byte		        An1 
	.byte		N12   
	.byte	W12
	.byte		        Cn1 
	.byte		N12   
	.byte		N12   , As1 
	.byte		N12   
	.byte		N12   , Gn2 
	.byte	W12
	.byte		        Cn1 
	.byte		N12   
	.byte	W12
	.byte		N06   , As1 
	.byte		N06   
	.byte	W06
	.byte		N12   , Cn1 
	.byte		N12   
	.byte	W18
	.byte	PEND
@ 031   ----------------------------------------
mus_custom_jetlag_7_031:
	.byte		N12   , Cn1 , v096
	.byte		N12   
	.byte		N12   , As1 
	.byte		N12   
	.byte	W12
	.byte		        Cn1 
	.byte		N12   
	.byte	W12
	.byte		        En1 
	.byte		N12   
	.byte		N12   , As1 
	.byte		N12   
	.byte	W24
	.byte		N24   , Cn1 
	.byte		N24   
	.byte		N24   , As1 
	.byte		N24   
	.byte	W24
	.byte		        En1 
	.byte		N24   
	.byte		N24   , As1 
	.byte		N24   
	.byte	W24
	.byte	PEND
@ 032   ----------------------------------------
	.byte		N12   , Cn1 
	.byte		N12   
	.byte		N12   , As1 
	.byte		N12   
	.byte	W12
	.byte		        Cn1 
	.byte		N12   
	.byte	W12
	.byte		        En1 
	.byte		N12   
	.byte		N12   , As1 
	.byte		N12   
	.byte	W12
	.byte		        Cn1 
	.byte		N12   
	.byte	W12
	.byte		N24   
	.byte		N24   
	.byte		N24   , As1 
	.byte		N24   
	.byte	W24
	.byte		N12   , En1 
	.byte		N12   
	.byte		N12   , Gs1 
	.byte		N12   
	.byte	W24
@ 033   ----------------------------------------
	.byte		        Cn1 
	.byte		N12   
	.byte		N12   , As1 
	.byte		N12   
	.byte	W12
	.byte		        Cn1 
	.byte		N12   
	.byte	W12
	.byte		N06   , As1 
	.byte		N06   
	.byte	W06
	.byte		N12   , Cn1 
	.byte		N12   
	.byte	W18
	.byte		N24   
	.byte		N24   
	.byte		N24   , As1 
	.byte		N24   
	.byte	W24
	.byte		N12   , En1 
	.byte		N11   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
@ 034   ----------------------------------------
	.byte		N12   , Cn1 
	.byte		N12   
	.byte		N12   , As1 
	.byte		N12   
	.byte		N12   , Cs2 
	.byte		N12   
	.byte	W18
	.byte		N06   , Cn1 
	.byte		N06   
	.byte		N06   , Cs2 
	.byte		N06   
	.byte	W06
	.byte		N12   , As1 
	.byte		N12   
	.byte	W12
	.byte		        En1 
	.byte		N12   
	.byte	W12
	.byte		        As1 
	.byte		N12   
	.byte	W12
	.byte		        Cn1 
	.byte		N12   
	.byte	W12
	.byte		        En1 
	.byte		N12   
	.byte		N12   , As1 
	.byte		N12   
	.byte	W12
	.byte		N06   , En1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
@ 035   ----------------------------------------
	.byte		N12   , Cn1 
	.byte		N12   
	.byte		N12   , As1 
	.byte		N12   
	.byte	W18
	.byte		N06   , Cn1 
	.byte		N06   
	.byte	W06
	.byte		N12   , As1 
	.byte		N12   
	.byte	W12
	.byte		        En1 
	.byte		N12   
	.byte	W12
	.byte		        As1 
	.byte		N12   
	.byte	W12
	.byte		        Cn1 
	.byte		N12   
	.byte	W12
	.byte		N06   , As1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		N12   , Cn1 
	.byte		N12   
	.byte	W12
@ 036   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_028
@ 037   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_029
@ 038   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_030
@ 039   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_031
@ 040   ----------------------------------------
	.byte		N12   , Cn1 , v096
	.byte		N12   
	.byte		N12   , As1 
	.byte		N12   
	.byte	W12
	.byte		        Cn1 
	.byte		N12   
	.byte	W12
	.byte		        En1 
	.byte		N12   
	.byte		N12   , As1 
	.byte		N12   
	.byte	W12
	.byte		        Cn1 
	.byte		N12   
	.byte	W12
	.byte		N24   
	.byte		N24   
	.byte		N24   , As1 
	.byte		N24   
	.byte	W24
	.byte		N06   , En1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cs2 
	.byte		N06   
	.byte	W12
@ 041   ----------------------------------------
	.byte		N96   , Cn1 
	.byte		N96   
	.byte		N96   , As1 
	.byte		N96   
	.byte		N96   , Gn2 
	.byte		N96   
	.byte	W96
@ 042   ----------------------------------------
	.byte	W84
	.byte		N12   , Cn1 
	.byte		N12   
	.byte	W12
@ 043   ----------------------------------------
mus_custom_jetlag_7_043:
	.byte		N24   , Cn1 , v096
	.byte		N24   
	.byte		N24   , As1 
	.byte		N24   
	.byte		N24   , Gn2 
	.byte		N24   
	.byte	W24
	.byte		        Fs2 
	.byte		N24   
	.byte	W24
	.byte		N24   
	.byte		N24   
	.byte	W24
	.byte		N24   
	.byte		N24   
	.byte	W24
	.byte	PEND
@ 044   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_043
@ 045   ----------------------------------------
mus_custom_jetlag_7_045:
	.byte		N18   , Cn1 , v096
	.byte		N18   
	.byte		N18   , As1 
	.byte		N18   
	.byte		N18   , Gn2 
	.byte		N18   
	.byte	W18
	.byte		        Cn1 
	.byte		N18   
	.byte		N18   , As1 
	.byte		N18   
	.byte		N18   , Gn2 
	.byte		N18   
	.byte	W18
	.byte		N06   , Cs1 
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Fs2 
	.byte		N06   
	.byte	W12
	.byte		        Cs1 
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte		N06   , Fs2 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 046   ----------------------------------------
	.byte		N06   
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W12
	.byte		        Cs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W06
	.byte		        Fs2 
	.byte		N06   
	.byte	W06
	.byte		        Cs1 
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Fs2 
	.byte		N06   
	.byte	W06
	.byte		        Cs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte		N06   , Cs1 
	.byte		N06   
	.byte		N06   , Fs2 
	.byte		N06   
	.byte	W12
	.byte		        Cs1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
@ 047   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_045
@ 048   ----------------------------------------
	.byte		N06   , Cn1 , v096
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   , Fs2 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte	W06
	.byte		        Cs1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        Cs1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		N12   , Cn1 
	.byte		N12   
	.byte	W12
	.byte		N12   
	.byte		N12   
	.byte	W12
	.byte		N06   , En1 
	.byte		N05   
	.byte	W06
	.byte		N06   , Cn1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        An1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        An1 
	.byte		N06   
	.byte	W06
@ 049   ----------------------------------------
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte	W12
	.byte		        En1 
	.byte		N05   
	.byte	W06
	.byte		N06   , An1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Cs2 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En2 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W12
@ 050   ----------------------------------------
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W12
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		        En1 
	.byte		N05   
	.byte	W06
	.byte		N06   , Fs2 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , En1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W12
@ 051   ----------------------------------------
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W12
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		        Gs1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W12
	.byte		        En1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W12
@ 052   ----------------------------------------
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        As1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W24
@ 053   ----------------------------------------
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , En1 
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , En1 
	.byte		N06   
	.byte	W06
	.byte		        An1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , An1 
	.byte		N06   , An1 , v080
	.byte	W06
	.byte		        An1 , v096
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Cs2 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En2 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W12
@ 054   ----------------------------------------
	.byte		        Fs2 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte		N06   , Fs2 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Cs1 
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , En1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W12
	.byte		        Fs2 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W12
@ 055   ----------------------------------------
	.byte	W12
	.byte		        Fs2 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte		N06   , Fs2 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		        En1 
	.byte		N06   , Fs2 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte		N06   , Fs2 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W12
@ 056   ----------------------------------------
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte	W12
	.byte		        En1 
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Fs2 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W60
@ 057   ----------------------------------------
mus_custom_jetlag_7_057:
	.byte		N06   , Cn1 , v096
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W18
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        Gs1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , En1 
	.byte		N06   
	.byte	W12
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 058   ----------------------------------------
mus_custom_jetlag_7_058:
	.byte		N06   , Gs1 , v096
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Gs1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , En1 
	.byte		N06   
	.byte	W60
	.byte	PEND
@ 059   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_057
@ 060   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_058
@ 061   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_057
@ 062   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_058
@ 063   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_057
@ 064   ----------------------------------------
	.byte		N06   , Gs1 , v096
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Gn2 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Bn1 
	.byte		N06   
	.byte	W06
	.byte		        En2 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , An1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn1 
	.byte		N06   
	.byte	W06
	.byte		        An2 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Fn1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Cs2 
	.byte		N06   
	.byte	W18
@ 065   ----------------------------------------
mus_custom_jetlag_7_065:
	.byte		N06   , Cn1 , v096
	.byte		N06   
	.byte		N06   , An2 
	.byte		N06   
	.byte	W12
	.byte		        An0 
	.byte		N06   
	.byte	W12
	.byte		        As1 
	.byte		N06   
	.byte	W06
	.byte		        An0 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		        An0 
	.byte		N06   
	.byte		N06   , Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        An0 
	.byte		N06   
	.byte	W06
	.byte		        As1 
	.byte		N06   
	.byte	W12
	.byte		        An0 
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 066   ----------------------------------------
mus_custom_jetlag_7_066:
	.byte		N06   , Cn1 , v096
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        An0 
	.byte		N06   
	.byte	W12
	.byte		        As1 
	.byte		N06   
	.byte	W06
	.byte		        An0 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		        An0 
	.byte		N06   
	.byte		N06   , Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        An0 
	.byte		N06   
	.byte	W06
	.byte		        As1 
	.byte		N06   
	.byte	W12
	.byte		        An0 
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 067   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_066
@ 068   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_066
@ 069   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_065
@ 070   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_066
@ 071   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_066
@ 072   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_066
@ 073   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_065
@ 074   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_066
@ 075   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_066
@ 076   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_066
@ 077   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_065
@ 078   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_066
@ 079   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_065
@ 080   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_066
@ 081   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_065
@ 082   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_066
@ 083   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_065
@ 084   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_7_066
@ 085   ----------------------------------------
	.byte		N96   , Cs2 , v096
	.byte		N96   
	.byte		N96   
	.byte		N96   , An2 
	.byte		N96   
	.byte		N96   
	.byte	W96
@ 086   ----------------------------------------
	.byte	FINE

@**************** Track 8 (Midi-Chn.9) ****************@

mus_custom_jetlag_8:
	.byte	KEYSH , mus_custom_jetlag_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 29
	.byte		VOL   , 83*mus_custom_jetlag_mvl/mxv
	.byte		PAN   , c_v-38
	.byte		BEND  , c_v+0
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
	.byte		N84   , Cs3 , v096
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte		N06   
	.byte	W06
	.byte		        Ds3 
	.byte	W06
@ 024   ----------------------------------------
	.byte		        As3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Fn3 
	.byte	W12
	.byte		        As2 
	.byte	W12
	.byte		N42   , Gs2 
	.byte	W42
	.byte		N12   , As2 
	.byte	W12
@ 025   ----------------------------------------
	.byte	W06
	.byte		        Cn3 
	.byte	W18
	.byte		N48   , Ds3 
	.byte		N48   , Cn4 
	.byte	W12
	.byte		N36   , Cs3 
	.byte	W36
	.byte		N72   , As2 
	.byte	W12
	.byte		N60   , Fn3 
	.byte	W12
@ 026   ----------------------------------------
	.byte	W84
	.byte		        Ds3 
	.byte	W12
@ 027   ----------------------------------------
	.byte	W66
	.byte		N06   , Cs3 
	.byte	W06
	.byte		        As2 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
@ 028   ----------------------------------------
	.byte	W24
	.byte		N12   
	.byte	W12
	.byte		N06   , As2 
	.byte	W06
	.byte		N12   , Cs3 
	.byte	W12
	.byte		N06   , Ds3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		N12   , Ds3 
	.byte	W12
	.byte		N06   , Cs3 
	.byte	W06
	.byte		N12   , Cn3 
	.byte	W12
@ 029   ----------------------------------------
	.byte	W06
	.byte		N06   , Fs2 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		        As2 
	.byte	W06
	.byte		N12   , Cs3 
	.byte	W18
	.byte		N06   , Ds3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Gs3 
	.byte	W18
	.byte		N12   , Ds3 
	.byte	W12
@ 030   ----------------------------------------
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte		        Ds3 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte		N42   , As2 
	.byte	W12
	.byte		N30   , Ds3 
	.byte	W06
	.byte		N24   , Gs3 
	.byte	W30
@ 031   ----------------------------------------
	.byte		N12   , Gs2 
	.byte	W12
	.byte		N06   , Cs3 
	.byte	W06
	.byte		N12   , Cn3 
	.byte	W12
	.byte		N06   , Cs3 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Fn3 
	.byte	W18
	.byte		N12   , Cs3 
	.byte	W24
	.byte		N06   , Fn2 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
@ 032   ----------------------------------------
	.byte		        As2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		N12   , Fn3 
	.byte	W12
	.byte		N24   , Cs3 
	.byte	W36
	.byte		N06   , Gs3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
@ 033   ----------------------------------------
	.byte	W30
	.byte		N18   , Gs3 
	.byte	W18
	.byte		        Gn3 
	.byte	W18
	.byte		N12   , Fn3 
	.byte	W12
	.byte		N06   , Cn3 
	.byte	W06
	.byte		        Fn2 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
@ 034   ----------------------------------------
	.byte		N12   , As2 
	.byte	W24
	.byte		        Cs3 
	.byte	W12
	.byte		        Fn3 
	.byte	W24
	.byte		N06   
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		N12   , Fn3 
	.byte	W12
	.byte		N06   , Cs3 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
@ 035   ----------------------------------------
	.byte		N12   , Gs2 
	.byte	W24
	.byte		        Cs3 
	.byte	W12
	.byte		        Ds3 
	.byte	W36
	.byte		N12   
	.byte	W12
	.byte		N06   , Cs3 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
@ 036   ----------------------------------------
	.byte		        Cs3 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		N12   , Fn3 
	.byte		N12   , Gs3 
	.byte	W18
	.byte		        Ds3 
	.byte		N12   , Fs3 
	.byte	W18
	.byte		N18   , Cs3 
	.byte		N18   , Fn3 
	.byte	W18
	.byte		N06   , Gs2 
	.byte	W06
	.byte		        As2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
@ 037   ----------------------------------------
	.byte		N36   , Ds3 
	.byte	W18
	.byte		N42   , As2 
	.byte	W18
	.byte		N24   , Gs2 
	.byte	W24
	.byte		N06   , Ds3 
	.byte	W06
	.byte		        Fn3 
	.byte	W18
	.byte		        Cs3 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
@ 038   ----------------------------------------
	.byte		N12   , Cs3 
	.byte	W12
	.byte		N24   , Cn3 
	.byte	W12
	.byte		        Gs3 
	.byte	W12
	.byte		N48   , Cn3 
	.byte	W12
	.byte		N36   , As3 
	.byte	W48
@ 039   ----------------------------------------
	.byte		N24   , Cn4 
	.byte	W48
	.byte		N06   , Cs4 
	.byte	W06
	.byte		        As3 
	.byte	W12
	.byte		N12   , Gs3 
	.byte	W12
	.byte		N06   , Cs4 
	.byte	W12
	.byte		        Cn4 
	.byte	W06
@ 040   ----------------------------------------
	.byte		        Ds4 
	.byte	W06
	.byte		        Fn4 
	.byte	W06
	.byte		        Gs4 
	.byte	W18
	.byte		        Ds4 
	.byte	W06
	.byte		        Cs4 
	.byte	W06
	.byte		        Cn4 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		        Cn4 
	.byte	W06
	.byte		        Ds4 
	.byte	W06
	.byte		        Fn4 
	.byte	W18
	.byte		N12   , Cn4 
	.byte	W12
@ 041   ----------------------------------------
	.byte	W96
@ 042   ----------------------------------------
	.byte	W96
@ 043   ----------------------------------------
	.byte	W96
@ 044   ----------------------------------------
	.byte	W96
@ 045   ----------------------------------------
	.byte	W96
@ 046   ----------------------------------------
	.byte	W96
@ 047   ----------------------------------------
	.byte	W96
@ 048   ----------------------------------------
	.byte	W48
	.byte		N48   , Cs3 
	.byte		N48   , As3 
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
@ 049   ----------------------------------------
	.byte		N18   , As1 
	.byte		N18   , Cs3 
	.byte		N18   , As3 
	.byte	W18
	.byte		N06   , As2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		N18   , As2 
	.byte	W06
	.byte		N12   , Cs3 
	.byte	W06
	.byte		N06   , Fs3 
	.byte	W18
	.byte		N18   , Fs2 
	.byte		N18   , Cs3 
	.byte		N18   , Fn3 
	.byte	W12
@ 050   ----------------------------------------
	.byte	W06
	.byte		N06   , Fn2 
	.byte	W06
	.byte		        Fs2 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte	W12
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        Fn3 
	.byte	W18
	.byte		N30   , Ds2 
	.byte		N12   , As2 
	.byte		N30   , Cs3 
	.byte	W12
@ 051   ----------------------------------------
	.byte	W18
	.byte		N18   , Fs2 
	.byte		N18   , Fn3 
	.byte	W06
	.byte		N12   , Ds3 
	.byte	W12
	.byte		        Cn3 
	.byte	W12
	.byte		N36   , Fn2 
	.byte		N36   , Ds3 
	.byte	W12
	.byte		N12   , Gs3 
	.byte	W12
	.byte		N36   , Fn3 
	.byte	W12
	.byte		N24   , Fs2 
	.byte		N24   , Gs2 
	.byte		N24   , Cs3 
	.byte	W12
@ 052   ----------------------------------------
	.byte	W12
	.byte		N12   , Fn2 
	.byte		N11   , Cs3 
	.byte	W01
	.byte		N10   , Fn3 
	.byte	W23
	.byte		N06   , Gs2 
	.byte		N06   , Cs3 
	.byte		N06   , Fn3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N12   , Fn3 
	.byte	W24
	.byte		        Cs3 
	.byte	W12
	.byte		        An2 
	.byte	W12
@ 053   ----------------------------------------
	.byte	W12
	.byte		N06   , Gs3 
	.byte	W06
	.byte		        Cs3 
	.byte	W12
	.byte		        Cn3 
	.byte	W12
	.byte		        Ds3 
	.byte	W06
	.byte		N12   , As2 
	.byte		N12   , Cs4 
	.byte	W12
	.byte		N06   , Cn4 
	.byte	W06
	.byte		N18   , Gs2 
	.byte		N18   , As3 
	.byte	W18
	.byte		N36   , Fs2 
	.byte		N36   , Cs3 
	.byte		N36   , Gs3 
	.byte	W12
@ 054   ----------------------------------------
	.byte	W24
	.byte		N06   , Cn3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		N12   , Gs3 
	.byte	W12
	.byte		N36   , Fs2 
	.byte		N12   , Fs3 
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte		N30   , Ds2 
	.byte		N30   , As2 
	.byte		N30   , Cs3 
	.byte	W12
@ 055   ----------------------------------------
	.byte	W18
	.byte		N18   , Fs2 
	.byte		N06   , Fn3 
	.byte	W06
	.byte		N12   , Ds3 
	.byte	W12
	.byte		        Cn3 
	.byte	W12
	.byte		N36   , Fn1 
	.byte		N36   , As2 
	.byte		N12   , Ds3 
	.byte	W12
	.byte		        Gs3 
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte		N24   , As1 
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte	W12
@ 056   ----------------------------------------
	.byte	W12
	.byte		N12   , Fn2 
	.byte		N11   , Cs3 
	.byte	W01
	.byte		N10   , Fn3 
	.byte	W23
	.byte		N36   , Fs2 
	.byte		N36   , Ds3 
	.byte		N24   , Gs3 
	.byte	W24
	.byte		N12   , As3 
	.byte	W24
	.byte		N48   , Cs3 
	.byte		N48   , Cn4 
	.byte		N48   , Fn4 
	.byte	W12
@ 057   ----------------------------------------
	.byte	W36
	.byte	FINE

@**************** Track 9 (Midi-Chn.11) ****************@

mus_custom_jetlag_9:
	.byte	KEYSH , mus_custom_jetlag_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 29
	.byte		VOL   , 83*mus_custom_jetlag_mvl/mxv
	.byte		PAN   , c_v-38
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
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W12
@ 024   ----------------------------------------
	.byte	W96
@ 025   ----------------------------------------
	.byte	W96
@ 026   ----------------------------------------
	.byte	W72
	.byte		BEND  , c_v+0
	.byte		N12   , Fn3 , v096
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte		        c_v+12
	.byte		        c_v+13
	.byte		        c_v+14
	.byte		        c_v+15
	.byte		        c_v+16
	.byte	W01
	.byte		        c_v+16
	.byte	W06
	.byte		        c_v+16
	.byte		        c_v+0
	.byte	W12
@ 027   ----------------------------------------
	.byte	W96
@ 028   ----------------------------------------
	.byte		        c_v+0
	.byte		N12   , Ds3 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W84
@ 029   ----------------------------------------
mus_custom_jetlag_9_029:
	.byte	W72
	.byte		BEND  , c_v+0
	.byte		N12   , Ds3 , v096
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W12
	.byte	PEND
@ 030   ----------------------------------------
	.byte		        c_v+0
	.byte		N12   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte		        c_v+12
	.byte		        c_v+13
	.byte		        c_v+14
	.byte		        c_v+15
	.byte		        c_v+16
	.byte	W01
	.byte		        c_v+16
	.byte	W06
	.byte		        c_v+16
	.byte		        c_v+0
	.byte	W84
@ 031   ----------------------------------------
	.byte	W48
	.byte		        c_v+0
	.byte		N12   , Cs3 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W36
@ 032   ----------------------------------------
	.byte	W60
	.byte		        c_v+0
	.byte		N12   , Gs3 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W24
@ 033   ----------------------------------------
	.byte	W12
	.byte		        c_v+0
	.byte		N18   , As3 
	.byte	W07
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte	W01
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W09
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W66
@ 034   ----------------------------------------
	.byte	W96
@ 035   ----------------------------------------
	.byte	W60
	.byte		        c_v+0
	.byte		N12   , Ds3 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W24
@ 036   ----------------------------------------
	.byte	W96
@ 037   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_jetlag_9_029
@ 038   ----------------------------------------
	.byte	W96
@ 039   ----------------------------------------
	.byte	W96
@ 040   ----------------------------------------
	.byte	W18
	.byte		BEND  , c_v+0
	.byte		N12   , Ds4 , v096
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte		        c_v+12
	.byte		        c_v+13
	.byte		        c_v+14
	.byte		        c_v+15
	.byte		        c_v+16
	.byte		        c_v+17
	.byte		        c_v+18
	.byte		        c_v+19
	.byte		        c_v+20
	.byte		        c_v+21
	.byte		        c_v+22
	.byte		        c_v+23
	.byte		        c_v+24
	.byte		        c_v+25
	.byte		        c_v+26
	.byte		        c_v+27
	.byte	W01
	.byte		        c_v+27
	.byte	W06
	.byte		        c_v+27
	.byte		        c_v+0
	.byte	W42
	.byte		        c_v+0
	.byte		N12   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W12
@ 041   ----------------------------------------
	.byte	W96
@ 042   ----------------------------------------
	.byte	W96
@ 043   ----------------------------------------
	.byte	W96
@ 044   ----------------------------------------
	.byte	W96
@ 045   ----------------------------------------
	.byte	W96
@ 046   ----------------------------------------
	.byte	W96
@ 047   ----------------------------------------
	.byte	W96
@ 048   ----------------------------------------
	.byte	W48
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
@ 049   ----------------------------------------
	.byte	W96
@ 050   ----------------------------------------
	.byte	W96
@ 051   ----------------------------------------
	.byte	W96
@ 052   ----------------------------------------
	.byte	W60
	.byte		        c_v+0
	.byte		N12   , Cn3 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte	W01
	.byte		        c_v+5
	.byte		        c_v+5
	.byte	W06
	.byte		        c_v+5
	.byte		        c_v+0
	.byte	W24
@ 053   ----------------------------------------
	.byte		        c_v+0
	.byte		N12   , Bn3 
	.byte	W03
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte	W01
	.byte		        c_v+5
	.byte		        c_v+5
	.byte	W02
	.byte		        c_v+5
	.byte	W05
	.byte		        c_v+5
	.byte	W01
	.byte		        c_v+5
	.byte		        c_v+0
	.byte	W84
@ 054   ----------------------------------------
	.byte	W96
@ 055   ----------------------------------------
	.byte	W96
@ 056   ----------------------------------------
	.byte	W96
@ 057   ----------------------------------------
	.byte	W36
	.byte	FINE

@**************** Track 10 (Midi-Chn.12) ****************@

mus_custom_jetlag_10:
	.byte	KEYSH , mus_custom_jetlag_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 26
	.byte		VOL   , 115*mus_custom_jetlag_mvl/mxv
	.byte		PAN   , c_v+44
	.byte		BEND  , c_v+0
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
	.byte	W96
@ 044   ----------------------------------------
	.byte	W96
@ 045   ----------------------------------------
	.byte	W96
@ 046   ----------------------------------------
	.byte	W96
@ 047   ----------------------------------------
	.byte	W96
@ 048   ----------------------------------------
	.byte	W48
	.byte		N48   , Cs3 , v096
	.byte		N48   , As3 
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
@ 049   ----------------------------------------
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+2
	.byte		N18   , Gs2 
	.byte		N18   , Gs3 
	.byte	W01
	.byte		BEND  , c_v+3
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+4
	.byte	W01
	.byte		        c_v+5
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+9
	.byte	W01
	.byte		        c_v+10
	.byte		        c_v+10
	.byte		        c_v+11
	.byte		        c_v+11
	.byte		        c_v+11
	.byte		        c_v+11
	.byte	W05
	.byte		        c_v+11
	.byte		        c_v+11
	.byte		        c_v+10
	.byte		        c_v+10
	.byte		        c_v+9
	.byte		        c_v+9
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+8
	.byte		        c_v+7
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+6
	.byte		        c_v+6
	.byte		        c_v+5
	.byte		        c_v+5
	.byte		        c_v+4
	.byte		        c_v+4
	.byte	W01
	.byte		        c_v+3
	.byte		        c_v+3
	.byte		        c_v+2
	.byte		        c_v+2
	.byte	W01
	.byte		        c_v+1
	.byte		        c_v+1
	.byte		        c_v+0
	.byte		        c_v+0
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v+0
	.byte		        c_v+0
	.byte		N06   , As2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		N18   , As2 
	.byte	W06
	.byte		N12   , Cs3 
	.byte	W06
	.byte		N06   , Fs3 
	.byte	W18
	.byte		N18   , Fs2 
	.byte		N18   , Cs3 
	.byte		N18   , Fn3 
	.byte	W12
@ 050   ----------------------------------------
	.byte	W06
	.byte		N06   , Fn2 
	.byte	W06
	.byte		        Fs2 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		N12   , Gs3 
	.byte	W04
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte	W01
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		N42   , Cs4 
	.byte	W12
	.byte		N30   , Ds2 
	.byte		N30   , As2 
	.byte		N30   , Cs3 
	.byte	W12
@ 051   ----------------------------------------
	.byte	W18
	.byte		N18   , Fs2 
	.byte		N18   , Fn3 
	.byte	W06
	.byte		N12   , Ds3 
	.byte	W12
	.byte		        Cn3 
	.byte	W12
	.byte		N36   , Fn2 
	.byte		N36   , Ds3 
	.byte	W12
	.byte		N12   , Gs3 
	.byte	W12
	.byte		N36   , Fn3 
	.byte	W12
	.byte		N24   , Fs2 
	.byte		N24   , Gs2 
	.byte		N24   , Cs3 
	.byte	W12
@ 052   ----------------------------------------
	.byte	W12
	.byte		N12   , Fn2 
	.byte		N11   , Cs3 
	.byte	W01
	.byte		N10   , Fn3 
	.byte	W23
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte		N06   , Fn3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N12   , Fn3 
	.byte	W12
	.byte		N36   , An2 
	.byte	W12
	.byte		N24   , Fs3 
	.byte		N24   , An3 
	.byte	W24
@ 053   ----------------------------------------
	.byte		N48   , As2 
	.byte		N36   , Ds3 
	.byte		N48   , As3 
	.byte	W18
	.byte		N30   , Fn3 
	.byte	W18
	.byte		N12   , Cs3 
	.byte	W12
	.byte		        As2 
	.byte		N12   , Gs3 
	.byte	W06
	.byte		N06   , Ds3 
	.byte	W12
	.byte		N12   , Cn3 
	.byte		N12   , As3 
	.byte	W18
	.byte		N18   , Cs3 
	.byte		N18   , Fn3 
	.byte	W12
@ 054   ----------------------------------------
	.byte	W06
	.byte		N24   , Ds2 
	.byte	W06
	.byte		N06   , Cn3 
	.byte	W06
	.byte		N12   , Cs3 
	.byte	W06
	.byte		N06   , Gs3 
	.byte	W12
	.byte		N12   , Fs1 , v112
	.byte		N12   , Cs2 
	.byte		N12   , Gs2 
	.byte	W12
	.byte		N30   , Fs1 
	.byte		N30   , Cs2 
	.byte		N30   , Gs2 
	.byte	W12
	.byte		N06   , Ds3 , v096
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W12
	.byte		        Cs3 
	.byte	W06
@ 055   ----------------------------------------
	.byte		N36   , Fs1 
	.byte		N36   , As2 
	.byte		N36   , Ds3 
	.byte	W60
	.byte		N06   
	.byte	W06
	.byte		        Fn3 
	.byte	W06
	.byte		        Cn3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Fn3 
	.byte	W06
@ 056   ----------------------------------------
	.byte		N12   
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte		        Fn3 
	.byte	W12
	.byte		N36   , Ds3 
	.byte	W36
	.byte		N24   , Cs3 
	.byte		N24   , Gs3 
	.byte	W24
@ 057   ----------------------------------------
	.byte	FINE

@**************** Track 11 (Midi-Chn.7) ****************@

mus_custom_jetlag_11:
	.byte	KEYSH , mus_custom_jetlag_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 119
	.byte		VOL   , 127*mus_custom_jetlag_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		BEND  , c_v+0
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
	.byte	W24
	.byte		N72   , Fn3 , v096
	.byte		N72   , Gs3 
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
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
	.byte	W96
@ 044   ----------------------------------------
	.byte	W96
@ 045   ----------------------------------------
	.byte	W96
@ 046   ----------------------------------------
	.byte	W96
@ 047   ----------------------------------------
	.byte	W96
@ 048   ----------------------------------------
	.byte	W96
@ 049   ----------------------------------------
	.byte	W96
@ 050   ----------------------------------------
	.byte	W96
@ 051   ----------------------------------------
	.byte	W96
@ 052   ----------------------------------------
	.byte	W96
@ 053   ----------------------------------------
	.byte	W96
@ 054   ----------------------------------------
	.byte	W96
@ 055   ----------------------------------------
	.byte	W96
@ 056   ----------------------------------------
	.byte	W36
	.byte		N60   , Fn3 
	.byte		N60   , Gs3 
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
@ 057   ----------------------------------------
	.byte	FINE

@******************************************************@
	.align	2

mus_custom_jetlag:
	.byte	11	@ NumTrks
	.byte	0	@ NumBlks
	.byte	mus_custom_jetlag_pri	@ Priority
	.byte	mus_custom_jetlag_rev	@ Reverb.

	.word	mus_custom_jetlag_grp

	.word	mus_custom_jetlag_1
	.word	mus_custom_jetlag_2
	.word	mus_custom_jetlag_3
	.word	mus_custom_jetlag_4
	.word	mus_custom_jetlag_5
	.word	mus_custom_jetlag_6
	.word	mus_custom_jetlag_7
	.word	mus_custom_jetlag_8
	.word	mus_custom_jetlag_9
	.word	mus_custom_jetlag_10
	.word	mus_custom_jetlag_11

	.end
