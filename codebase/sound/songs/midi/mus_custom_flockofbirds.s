	.include "MPlayDef.s"

	.equ	mus_custom_flockofbirds_grp, voicegroup193
	.equ	mus_custom_flockofbirds_pri, 4
	.equ	mus_custom_flockofbirds_rev, reverb_set+50
	.equ	mus_custom_flockofbirds_mvl, 75
	.equ	mus_custom_flockofbirds_key, 0
	.equ	mus_custom_flockofbirds_tbs, 1
	.equ	mus_custom_flockofbirds_exg, 1
	.equ	mus_custom_flockofbirds_cmp, 1

	.section .rodata
	.global	mus_custom_flockofbirds
	.align	2

@**************** Track 1 (Midi-Chn.1) ****************@

mus_custom_flockofbirds_1:
	.byte	KEYSH , mus_custom_flockofbirds_key+0
@ 000   ----------------------------------------
	.byte	TEMPO , 100*mus_custom_flockofbirds_tbs/2
	.byte		VOICE , 28
	.byte		VOL   , 96*mus_custom_flockofbirds_mvl/mxv
	.byte		PAN   , c_v-45
	.byte		BEND  , c_v+0
	.byte	W96
@ 001   ----------------------------------------
mus_custom_flockofbirds_1_001:
	.byte		N12   , En1 , v096
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N24   , Fs3 
	.byte	W12
	.byte		N18   , En3 
	.byte	W12
	.byte		N06   , Bn2 
	.byte	W06
	.byte		N12   , Gs1 
	.byte		N12   , Fs2 
	.byte		N12   , Bn2 
	.byte	W18
	.byte		N24   , Cs3 
	.byte	W12
	.byte		N12   , Bn2 
	.byte	W12
	.byte		N06   , Fs2 
	.byte	W06
	.byte	PEND
@ 002   ----------------------------------------
mus_custom_flockofbirds_1_002:
	.byte		N12   , As2 , v096
	.byte		N12   , Cs3 
	.byte	W18
	.byte		N24   , Ds3 
	.byte	W12
	.byte		N18   , Bn2 
	.byte	W12
	.byte		N06   , Fs2 
	.byte	W06
	.byte		N30   , En2 
	.byte		N06   , Ds3 
	.byte	W06
	.byte		        En3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		N12   , Cs3 
	.byte	W12
	.byte		        Bn2 
	.byte	W12
	.byte		N06   , Fs3 
	.byte	W06
	.byte	PEND
@ 003   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_001
@ 004   ----------------------------------------
mus_custom_flockofbirds_1_004:
	.byte		N12   , Bn1 , v096
	.byte		N12   , As2 
	.byte		N12   , Cs3 
	.byte	W18
	.byte		N24   , Ds3 
	.byte	W12
	.byte		N18   , Bn2 
	.byte	W12
	.byte		N06   , Fs2 
	.byte	W06
	.byte		N18   , Gs2 
	.byte		N06   , Ds3 
	.byte	W06
	.byte		        En3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		N18   , Fs2 
	.byte		N18   , Cs3 
	.byte	W30
	.byte	PEND
@ 005   ----------------------------------------
mus_custom_flockofbirds_1_005:
	.byte		N12   , En1 , v096
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N24   , Fs3 
	.byte	W12
	.byte		N18   , En3 
	.byte	W12
	.byte		N06   , Bn2 
	.byte	W06
	.byte		        Gs1 
	.byte	W06
	.byte		        Fs2 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		N30   , Cs3 
	.byte	W12
	.byte		N18   , Bn2 
	.byte	W12
	.byte		N06   , Fs2 
	.byte	W06
	.byte	PEND
@ 006   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_002
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_005
@ 008   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_004
@ 009   ----------------------------------------
	.byte		N01   , En2 , v096
	.byte		N01   , Bn2 
	.byte	W06
	.byte		N06   , En2 
	.byte		N06   , Bn2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        En2 
	.byte		N06   , Bn2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        En2 
	.byte		N06   , Bn2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		N12   , En1 
	.byte	W12
	.byte		        Gs2 , v112
	.byte		N12   , Fs3 , v096
	.byte	W18
	.byte		N18   , Bn2 
	.byte		N18   , Ds3 
	.byte	W24
	.byte		        En3 , v112
	.byte	W06
	.byte		        Fs3 , v096
	.byte	W06
	.byte		N06   , Ds4 , v112
	.byte	W06
@ 010   ----------------------------------------
mus_custom_flockofbirds_1_010:
	.byte		N06   , Bn3 , v112
	.byte	W06
	.byte		N18   , Fs3 
	.byte	W06
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        Cs4 
	.byte	W12
	.byte		        Gs2 
	.byte		N06   , Ds3 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N24   , Cs3 
	.byte		N24   , As3 
	.byte	W12
	.byte		N12   , Fs3 
	.byte	W12
	.byte		        Cs2 
	.byte		N12   , Gs2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		        En3 
	.byte	W12
	.byte	PEND
@ 011   ----------------------------------------
	.byte	W06
	.byte		N06   , En2 , v096
	.byte		N06   , Bn2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        En2 , v112
	.byte		N06   , Bn2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        En2 , v096
	.byte		N06   , Bn2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		N12   , En1 
	.byte	W12
	.byte		        Bn2 , v112
	.byte		N12   , Fs3 
	.byte		N12   , As3 
	.byte	W18
	.byte		N42   , En1 
	.byte		N18   , Bn2 
	.byte		N18   , Fs3 
	.byte		N18   , As3 , v096
	.byte	W18
	.byte		N48   , Bn2 , v112
	.byte	W06
	.byte		N18   , En3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N06   , Cs4 , v096
	.byte	W06
@ 012   ----------------------------------------
	.byte		        Bn3 , v112
	.byte	W06
	.byte		N18   , Fs3 
	.byte	W06
	.byte		N06   , Bn3 , v096
	.byte	W06
	.byte		        Cs4 , v112
	.byte	W12
	.byte		        Gs2 
	.byte		N06   , Ds3 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte		N24   , As3 
	.byte	W12
	.byte		N12   , Fs3 
	.byte	W12
	.byte		N06   , Cs2 
	.byte		N06   , Gs2 
	.byte		N06   , En3 , v096
	.byte	W12
	.byte		        Ds2 , v112
	.byte		N06   , As2 
	.byte		N06   , Ds3 , v096
	.byte	W12
	.byte		        Cs3 
	.byte	W06
@ 013   ----------------------------------------
	.byte	W12
	.byte		N12   , Bn2 
	.byte	W12
	.byte		        En1 
	.byte	W12
	.byte		N18   , Bn1 , v112
	.byte		N18   , Fs2 
	.byte		N18   , Cs3 
	.byte	W18
	.byte		N12   , Cs2 
	.byte		N12   , Gs2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N48   , Bn2 
	.byte	W06
	.byte		N18   , En3 
	.byte	W06
	.byte		N06   , Fs3 
	.byte	W06
	.byte		N12   , As3 , v096
	.byte	W06
@ 014   ----------------------------------------
	.byte		N06   , Bn3 , v112
	.byte	W06
	.byte		N18   , Fs3 
	.byte	W06
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        Cs4 , v096
	.byte	W12
	.byte		        Gs2 , v112
	.byte		N06   , Ds3 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte		N24   , As3 
	.byte	W12
	.byte		N12   , Fs3 
	.byte	W18
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N12   , Ds3 
	.byte	W06
@ 015   ----------------------------------------
	.byte	W06
	.byte		N06   , En2 , v096
	.byte		N06   , Bn2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        En2 
	.byte		N06   , Bn2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        En2 
	.byte		N06   , Bn2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		N12   , En1 
	.byte	W12
	.byte		        Bn2 , v112
	.byte		N12   , Fs3 
	.byte		N12   , As3 
	.byte	W18
	.byte		N42   , En1 
	.byte		N18   , Bn2 
	.byte		N18   , Fs3 
	.byte		N18   , As3 
	.byte	W18
	.byte		N48   , Bn2 
	.byte	W06
	.byte		N18   , En3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N06   , Ds4 
	.byte	W06
@ 016   ----------------------------------------
mus_custom_flockofbirds_1_016:
	.byte		N06   , Bn3 , v096
	.byte	W06
	.byte		N18   , Fs3 , v112
	.byte	W06
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        Cs4 
	.byte	W12
	.byte		        Gs2 
	.byte		N06   , Ds3 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N48   , Fs2 
	.byte		N48   , Cs3 
	.byte		N48   , As3 
	.byte	W12
	.byte		N36   , Fs3 
	.byte	W42
	.byte	PEND
@ 017   ----------------------------------------
mus_custom_flockofbirds_1_017:
	.byte		N48   , En2 , v096
	.byte		N48   , Cs3 
	.byte	W54
	.byte		N42   , En2 
	.byte		N42   , Fs3 
	.byte	W18
	.byte		N12   , Bn2 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte	PEND
@ 018   ----------------------------------------
mus_custom_flockofbirds_1_018:
	.byte		N12   , Ds2 , v096
	.byte		N12   , Bn2 
	.byte	W12
	.byte		N06   , Fs3 
	.byte	W18
	.byte		        Ds2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N24   , Ds2 
	.byte		N24   , Bn2 
	.byte	W18
	.byte		N06   , Fs3 
	.byte	W18
	.byte		        Ds2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N18   , Gs2 
	.byte		N18   , Bn2 
	.byte	W06
	.byte	PEND
@ 019   ----------------------------------------
mus_custom_flockofbirds_1_019:
	.byte	W12
	.byte		N36   , Ds3 , v096
	.byte	W06
	.byte		N30   , Bn2 
	.byte	W18
	.byte		N12   , Gs2 
	.byte	W18
	.byte		N42   
	.byte		N18   , Bn2 
	.byte		N30   , Ds3 
	.byte	W18
	.byte		N24   , Bn2 
	.byte	W12
	.byte		N12   , Ds3 
	.byte	W12
	.byte	PEND
@ 020   ----------------------------------------
mus_custom_flockofbirds_1_020:
	.byte		N12   , Fs2 , v096
	.byte		N12   , Bn2 
	.byte	W12
	.byte		N06   , Cs3 
	.byte	W18
	.byte		        Fs2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N18   , Fs2 
	.byte		N18   , Bn2 
	.byte	W18
	.byte		N06   , Cs3 
	.byte	W18
	.byte		        Fs2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		        En2 
	.byte		N06   , Cs3 
	.byte	W06
	.byte	PEND
@ 021   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_017
@ 022   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_018
@ 023   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_019
@ 024   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_020
@ 025   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_017
@ 026   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_018
@ 027   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_019
@ 028   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_020
@ 029   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_017
@ 030   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_018
@ 031   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_019
@ 032   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_020
@ 033   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_017
@ 034   ----------------------------------------
mus_custom_flockofbirds_1_034:
	.byte		N48   , Ds2 , v096
	.byte		N48   , Bn2 
	.byte	W48
	.byte		N01   , Ds2 
	.byte		N01   , Bn2 
	.byte	W06
	.byte		N24   , Ds2 
	.byte		N24   , Bn2 
	.byte	W18
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        Ds2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N18   , Gs2 
	.byte		N18   , Bn2 
	.byte	W06
	.byte	PEND
@ 035   ----------------------------------------
	.byte	W12
	.byte		N36   , Ds3 
	.byte	W06
	.byte		N30   , Bn2 
	.byte	W18
	.byte		N12   , Gs2 
	.byte	W18
	.byte		N30   
	.byte		N18   , Bn2 
	.byte		N30   , Ds3 
	.byte	W18
	.byte		N24   , Bn2 
	.byte	W12
	.byte		N12   , Gn2 
	.byte		N12   , Ds3 
	.byte	W12
@ 036   ----------------------------------------
	.byte		        Fs2 
	.byte		N12   , Bn2 
	.byte	W12
	.byte		N06   , Cs3 
	.byte	W18
	.byte		        Fs2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N18   , Fs2 
	.byte		N18   , Bn2 
	.byte	W18
	.byte		N06   , Cs3 
	.byte	W18
	.byte		N18   , Cs3 , v032
	.byte		N18   , Fs3 
	.byte		N18   , Cs4 , v096
	.byte		N18   , Fs4 
	.byte	W18
@ 037   ----------------------------------------
mus_custom_flockofbirds_1_037:
	.byte		N18   , Ds3 , v096
	.byte	W06
	.byte		N30   , En2 
	.byte	W06
	.byte		TIE   , Bn2 
	.byte	W06
	.byte		N18   , Ds3 
	.byte	W18
	.byte		N60   , Bn1 
	.byte	W18
	.byte		N18   , Fs3 
	.byte		N18   , As3 
	.byte	W24
	.byte		        En3 , v112
	.byte	W06
	.byte		        Fs3 , v096
	.byte	W06
	.byte		N06   , Ds4 , v112
	.byte	W06
	.byte	PEND
@ 038   ----------------------------------------
mus_custom_flockofbirds_1_038:
	.byte		N06   , Bn3 , v112
	.byte	W06
	.byte		N18   , Fs3 
	.byte	W06
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        Cs4 
	.byte	W06
	.byte	PEND
	.byte		EOT   , Bn2 
	.byte	W06
	.byte		N06   , Gs2 
	.byte		N06   , Ds3 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N24   , Cs3 
	.byte		N24   , As3 
	.byte	W12
	.byte		N12   , Fs3 
	.byte	W12
	.byte		        Cs2 
	.byte		N12   , Gs2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		        En3 , v096
	.byte	W12
@ 039   ----------------------------------------
	.byte		N24   , Ds3 , v032
	.byte		N24   , Ds4 , v096
	.byte	W06
	.byte		N18   , En2 
	.byte	W06
	.byte		N36   , Fs3 , v032
	.byte		N36   , Fs4 , v096
	.byte	W12
	.byte		N24   , En2 
	.byte	W12
	.byte		N36   , As3 , v032
	.byte		N36   , As4 , v096
	.byte	W12
	.byte		N24   , En2 
	.byte	W06
	.byte		N18   , Fs3 , v032
	.byte		N18   , Fs4 , v096
	.byte	W18
	.byte		N48   , Bn2 
	.byte		N24   , En3 
	.byte		N30   , Fs3 
	.byte		N24   , As3 
	.byte	W24
@ 040   ----------------------------------------
	.byte		N06   , Bn3 , v112
	.byte	W06
	.byte		N18   , Fs3 
	.byte	W06
	.byte		N06   , Bn3 , v096
	.byte	W06
	.byte		        Cs4 , v112
	.byte	W12
	.byte		        Gs2 
	.byte		N06   , Ds3 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N24   , As3 
	.byte	W12
	.byte		N12   , Ds3 , v096
	.byte	W12
	.byte		N06   , En3 
	.byte	W12
	.byte		        Ds3 
	.byte	W12
	.byte		        Cs3 
	.byte	W06
@ 041   ----------------------------------------
mus_custom_flockofbirds_1_041:
	.byte	W12
	.byte		N12   , Bn2 , v096
	.byte	W12
	.byte		        En1 
	.byte	W12
	.byte		N18   , Bn1 , v112
	.byte		N18   , Fs2 
	.byte		N18   , Cs3 
	.byte	W18
	.byte		N12   , Cs2 
	.byte		N12   , Gs2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N30   , Bn2 
	.byte	W06
	.byte		N18   , En3 
	.byte	W06
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        As3 , v096
	.byte	W06
	.byte	PEND
@ 042   ----------------------------------------
mus_custom_flockofbirds_1_042:
	.byte		N06   , Bn2 , v096
	.byte		N06   , Fs3 
	.byte		N06   , Bn3 , v112
	.byte	W12
	.byte		        Bn2 , v096
	.byte		N06   , Fs3 
	.byte		N06   , As3 
	.byte	W18
	.byte		        Fs2 
	.byte		N06   , Bn2 
	.byte		N06   , Ds3 
	.byte	W12
	.byte		N24   , Fn2 
	.byte		N24   , Bn2 
	.byte		N24   , Cs3 
	.byte	W30
	.byte		N06   , Bn3 , v112
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte	PEND
@ 043   ----------------------------------------
	.byte		N12   , En2 , v096
	.byte		N12   , Bn2 
	.byte		N12   , Fs3 
	.byte	W12
	.byte		        En1 
	.byte	W12
	.byte		N06   , Fs3 
	.byte	W06
	.byte		N12   , Gs3 
	.byte	W12
	.byte		N06   , As3 
	.byte	W06
	.byte		N12   , Gs1 
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte		N12   , Bn3 
	.byte	W24
	.byte		        Cs2 
	.byte		N12   , Gs2 
	.byte		N12   , Fn3 
	.byte	W24
@ 044   ----------------------------------------
mus_custom_flockofbirds_1_044:
	.byte		N24   , En1 , v096
	.byte	W03
	.byte		N21   , En2 
	.byte	W03
	.byte		N18   , Bn2 
	.byte	W03
	.byte		N15   , Ds3 
	.byte	W32
	.byte	W01
	.byte		N36   , Ds2 
	.byte		N36   , As2 
	.byte		N36   , Cs3 
	.byte	W54
	.byte	PEND
@ 045   ----------------------------------------
	.byte		N12   , Cs2 
	.byte		N12   , Bn2 
	.byte	W30
	.byte		N06   , Ds2 
	.byte		N06   , Cs3 
	.byte	W12
	.byte		N36   , Ds2 
	.byte		N36   , Cs3 
	.byte	W42
	.byte		N06   , Bn2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
@ 046   ----------------------------------------
mus_custom_flockofbirds_1_046:
	.byte		N24   , Ds3 , v096
	.byte	W12
	.byte		N12   , En2 
	.byte	W18
	.byte		N12   
	.byte		N12   , Gs2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N18   , Ds2 
	.byte		N18   , Fs2 
	.byte		N18   , Cs3 
	.byte	W18
	.byte		N06   , Gs3 
	.byte	W18
	.byte		N24   , Cs2 
	.byte		N24   , Bn2 
	.byte	W12
	.byte	PEND
@ 047   ----------------------------------------
mus_custom_flockofbirds_1_047:
	.byte	W12
	.byte		N24   , Gs1 , v096
	.byte	W12
	.byte		N12   , As2 
	.byte		N12   , Bn2 
	.byte	W24
	.byte		N06   , Cs2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N12   , Cs2 
	.byte		N12   , Bn2 
	.byte	W18
	.byte		        Ds2 
	.byte		N12   , Cs3 
	.byte	W18
	.byte	PEND
@ 048   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_046
@ 049   ----------------------------------------
mus_custom_flockofbirds_1_049:
	.byte	W12
	.byte		N24   , Gs1 , v096
	.byte	W12
	.byte		N12   , As2 
	.byte		N12   , Bn2 
	.byte	W24
	.byte		N24   , Fs1 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N12   
	.byte	W12
	.byte		N18   , Fn1 
	.byte	W06
	.byte		N12   , Cs3 
	.byte	W18
	.byte	PEND
@ 050   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_046
@ 051   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_047
@ 052   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_046
@ 053   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_049
@ 054   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_046
@ 055   ----------------------------------------
	.byte	W12
	.byte		N24   , Gs1 , v096
	.byte	W12
	.byte		N12   , As2 
	.byte		N12   , Bn2 
	.byte	W24
	.byte		N06   , Cs2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N12   , Cs2 
	.byte		N12   , Bn2 
	.byte	W18
	.byte		N18   , As2 
	.byte		N18   , Bn2 
	.byte	W18
@ 056   ----------------------------------------
	.byte		N24   , Ds3 
	.byte	W12
	.byte		N12   , En2 
	.byte	W18
	.byte		N12   
	.byte		N12   , Gs2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N18   , Ds2 
	.byte		N18   , Fs2 
	.byte		N18   , Cs3 
	.byte	W18
	.byte		N06   , Gs3 
	.byte	W18
	.byte		N24   , Cs2 
	.byte		N12   , Bn2 
	.byte	W12
@ 057   ----------------------------------------
	.byte		        As2 
	.byte		N12   , Bn2 
	.byte	W12
	.byte		N24   , Gs1 
	.byte	W12
	.byte		N12   , As2 
	.byte		N12   , Bn2 
	.byte	W24
	.byte		N24   , Fs1 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N12   
	.byte	W12
	.byte		N18   , Fn1 
	.byte	W06
	.byte		N12   , Cs3 
	.byte	W18
@ 058   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_046
@ 059   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_047
@ 060   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_046
@ 061   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_049
@ 062   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_046
@ 063   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_047
@ 064   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_046
@ 065   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_049
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
	.byte		N48   , En2 , v096
	.byte		N48   , Cs3 
	.byte	W54
	.byte		N42   , En2 
	.byte		N42   , Fs3 
	.byte	W18
	.byte		N24   , As3 
	.byte	W24
@ 083   ----------------------------------------
	.byte		N48   , Bn2 
	.byte		N48   , Ds3 
	.byte		N48   , Fs3 
	.byte		N48   , Bn3 
	.byte	W96
@ 084   ----------------------------------------
	.byte	W96
@ 085   ----------------------------------------
mus_custom_flockofbirds_1_085:
	.byte	W12
	.byte		N06   , En3 , v096
	.byte	W03
	.byte		N32   , Ds3 , v096, gtp1
	.byte	W03
	.byte		N18   , Bn2 
	.byte	W18
	.byte		N12   , Gs2 
	.byte	W18
	.byte		N18   
	.byte		N18   , Bn2 
	.byte		N18   , Ds3 
	.byte	W18
	.byte		N60   , Bn2 
	.byte		N24   , Fs3 
	.byte		N60   , As3 
	.byte	W24
	.byte	PEND
@ 086   ----------------------------------------
	.byte		N36   , Ds3 
	.byte	W36
	.byte		N60   , Fs2 
	.byte		N24   , Bn2 
	.byte	W24
	.byte		N06   
	.byte	W06
	.byte		N30   , Cs3 
	.byte	W06
	.byte		N72   , Bn2 
	.byte	W24
@ 087   ----------------------------------------
	.byte	W96
@ 088   ----------------------------------------
	.byte	W96
@ 089   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_085
@ 090   ----------------------------------------
	.byte		N36   , Ds3 , v096
	.byte	W36
	.byte		N30   , Fs2 
	.byte		N24   , Bn2 
	.byte	W24
	.byte		N36   
	.byte	W06
	.byte		N30   , En3 
	.byte	W06
	.byte		N24   , Bn3 
	.byte	W24
@ 091   ----------------------------------------
	.byte	W96
@ 092   ----------------------------------------
	.byte	W96
@ 093   ----------------------------------------
	.byte	W96
@ 094   ----------------------------------------
	.byte	W96
@ 095   ----------------------------------------
	.byte	W96
@ 096   ----------------------------------------
	.byte	W96
@ 097   ----------------------------------------
	.byte	W96
@ 098   ----------------------------------------
	.byte	W96
@ 099   ----------------------------------------
mus_custom_flockofbirds_1_099:
	.byte		N96   , En1 , v096
	.byte	W12
	.byte		N84   , Bn2 
	.byte	W03
	.byte		N80   , Gs3 , v096, gtp1
	.byte	W03
	.byte		N78   , As3 
	.byte	W03
	.byte		N72   , Fs4 , v096, gtp3
	.byte	W72
	.byte	W03
	.byte	PEND
@ 100   ----------------------------------------
	.byte	W96
@ 101   ----------------------------------------
	.byte	W96
@ 102   ----------------------------------------
	.byte	W96
@ 103   ----------------------------------------
	.byte	W96
@ 104   ----------------------------------------
	.byte	W96
@ 105   ----------------------------------------
	.byte	W96
@ 106   ----------------------------------------
	.byte	W96
@ 107   ----------------------------------------
	.byte	W96
@ 108   ----------------------------------------
	.byte	W96
@ 109   ----------------------------------------
	.byte	W96
@ 110   ----------------------------------------
	.byte	W96
@ 111   ----------------------------------------
	.byte		N12   , En1 
	.byte		N12   , Ds2 
	.byte		N12   , Bn2 
	.byte	W18
	.byte		N24   , Ds3 
	.byte	W12
	.byte		N12   , Fs3 
	.byte	W18
	.byte		        Gs1 
	.byte		N12   , Fs2 
	.byte		N12   , Bn2 
	.byte	W18
	.byte		N24   , Cs3 
	.byte	W12
	.byte		N12   , Bn2 
	.byte	W12
	.byte		N06   , Cs3 
	.byte	W06
@ 112   ----------------------------------------
	.byte		N12   , En3 
	.byte	W18
	.byte		N24   , Ds3 
	.byte	W12
	.byte		N12   , Bn2 
	.byte	W18
	.byte		N24   , Gs1 
	.byte		N24   , En2 
	.byte		N24   , Bn2 
	.byte		N24   , Ds3 
	.byte	W24
	.byte		        Fn1 
	.byte		N24   , Fs2 
	.byte		N24   , Gs2 
	.byte		N24   , Cs3 
	.byte	W24
@ 113   ----------------------------------------
mus_custom_flockofbirds_1_113:
	.byte		N12   , En2 , v096
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte		N12   , Fs3 
	.byte	W18
	.byte		N24   
	.byte	W12
	.byte		N12   , Ds3 
	.byte	W12
	.byte		N06   , As3 
	.byte	W06
	.byte		N12   , Bn1 
	.byte		N12   , Gs2 
	.byte		N12   , Cs3 
	.byte	W18
	.byte		N24   
	.byte	W12
	.byte		N12   , Bn2 
	.byte	W12
	.byte		N06   , Fs3 
	.byte	W06
	.byte	PEND
@ 114   ----------------------------------------
mus_custom_flockofbirds_1_114:
	.byte		N12   , Bn1 , v096
	.byte		N12   , As2 
	.byte		N12   , En3 
	.byte	W18
	.byte		N24   , Ds3 
	.byte	W12
	.byte		N18   , Bn2 
	.byte	W12
	.byte		N06   , Fs2 
	.byte	W06
	.byte		N18   , As1 
	.byte		N18   , Gs2 
	.byte		N18   , Cs3 
	.byte		N06   , Ds3 
	.byte	W06
	.byte		        En3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		N24   , Bn1 
	.byte		N24   , As2 
	.byte		N24   , Cs3 
	.byte		N24   , Fs3 
	.byte	W30
	.byte	PEND
@ 115   ----------------------------------------
	.byte	W96
@ 116   ----------------------------------------
	.byte	W96
@ 117   ----------------------------------------
	.byte	W96
@ 118   ----------------------------------------
	.byte	W96
@ 119   ----------------------------------------
	.byte	W96
@ 120   ----------------------------------------
	.byte	W96
@ 121   ----------------------------------------
	.byte	W96
@ 122   ----------------------------------------
	.byte	W96
@ 123   ----------------------------------------
	.byte	W96
@ 124   ----------------------------------------
	.byte	W96
@ 125   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_099
@ 126   ----------------------------------------
	.byte	W96
@ 127   ----------------------------------------
	.byte	W96
@ 128   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_037
@ 129   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_038
	.byte		EOT   , Bn2 
	.byte	W06
	.byte		N06   , Gs2 , v112
	.byte		N06   , Ds3 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N24   , Cs3 
	.byte		N24   , As3 
	.byte	W12
	.byte		N12   , Fs3 
	.byte	W12
	.byte		        Cs2 
	.byte		N12   , Gs2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		        En3 , v096
	.byte	W12
@ 130   ----------------------------------------
	.byte		N24   , Ds3 , v032
	.byte		N24   , Ds4 , v096
	.byte	W06
	.byte		N18   , En2 
	.byte	W06
	.byte		N36   , Fs3 , v032
	.byte		N36   , Fs4 , v096
	.byte	W12
	.byte		N24   , En2 
	.byte	W12
	.byte		N36   , As3 , v032
	.byte		N36   , As4 , v096
	.byte	W12
	.byte		N24   , En2 
	.byte	W06
	.byte		N18   , Fs3 , v032
	.byte		N18   , Fs4 , v096
	.byte	W42
@ 131   ----------------------------------------
	.byte		N06   , Bn3 , v112
	.byte	W06
	.byte		N18   , Fs3 
	.byte	W06
	.byte		N06   , Bn3 , v096
	.byte	W06
	.byte		        Cs4 , v112
	.byte	W12
	.byte		        Gs2 
	.byte		N06   , Ds3 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte		N24   , As3 
	.byte	W12
	.byte		N12   , Fs3 
	.byte	W24
	.byte		N06   , Ds3 , v096
	.byte	W12
	.byte		        Cs3 
	.byte	W06
@ 132   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_041
@ 133   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_042
@ 134   ----------------------------------------
	.byte		N12   , En2 , v096
	.byte		N12   , Bn2 
	.byte		N12   , Fs3 
	.byte	W12
	.byte		        En1 
	.byte	W12
	.byte		N06   , Fs3 
	.byte	W06
	.byte		N12   , Gs3 
	.byte	W12
	.byte		N06   , As3 
	.byte	W06
	.byte		N12   , Gs1 
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W24
	.byte		        Cs2 
	.byte		N12   , Gs2 
	.byte		N12   , Fn3 
	.byte	W24
@ 135   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_044
@ 136   ----------------------------------------
	.byte	W96
@ 137   ----------------------------------------
	.byte	W96
@ 138   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_010
@ 139   ----------------------------------------
	.byte		N12   , En2 , v096
	.byte	W12
	.byte		N06   , Ds3 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		N42   , En2 
	.byte	W18
	.byte		N24   , Fs3 
	.byte		N48   , As3 
	.byte	W24
	.byte		N24   , En2 
	.byte	W06
	.byte		N18   , Fs3 , v032
	.byte		N18   , Fs4 , v096
	.byte	W30
@ 140   ----------------------------------------
	.byte	W96
@ 141   ----------------------------------------
	.byte	W96
@ 142   ----------------------------------------
	.byte	W96
@ 143   ----------------------------------------
mus_custom_flockofbirds_1_143:
	.byte		N48   , En2 , v096
	.byte		N48   , Cs3 
	.byte	W54
	.byte		N66   , En2 
	.byte		N18   , Fs3 
	.byte	W18
	.byte		N24   , Ds3 
	.byte	W12
	.byte		N12   , Cs3 
	.byte	W12
	.byte	PEND
@ 144   ----------------------------------------
mus_custom_flockofbirds_1_144:
	.byte		N12   , Gs2 , v096
	.byte		N36   , As2 
	.byte	W12
	.byte		N24   , Ds3 
	.byte	W12
	.byte		N12   , Fs3 
	.byte	W12
	.byte		N18   , Bn2 
	.byte		N18   , Cs3 
	.byte	W18
	.byte		        Ds2 
	.byte		N18   , Bn2 
	.byte	W18
	.byte		N36   , Gs2 
	.byte	W01
	.byte		N32   , Bn2 , v096, gtp2
	.byte	W23
	.byte	PEND
@ 145   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_085
@ 146   ----------------------------------------
mus_custom_flockofbirds_1_146:
	.byte		N36   , Ds3 , v096
	.byte	W36
	.byte		N60   , Fs2 
	.byte		N24   , Bn2 
	.byte	W24
	.byte		N06   
	.byte	W06
	.byte		N30   , Cs3 
	.byte	W06
	.byte		N24   , Bn2 
	.byte	W24
	.byte	PEND
@ 147   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_143
@ 148   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_144
@ 149   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_085
@ 150   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_146
@ 151   ----------------------------------------
	.byte		N12   , En1 , v096
	.byte		N12   , Ds2 
	.byte		N12   , Bn2 
	.byte	W18
	.byte		N24   , Ds3 
	.byte	W12
	.byte		N12   , Fs3 
	.byte	W18
	.byte		        Gs1 
	.byte		N12   , Fs2 
	.byte		N12   , Bn2 
	.byte	W18
	.byte		N24   , Cs3 
	.byte	W12
	.byte		N12   , Bn2 
	.byte	W18
@ 152   ----------------------------------------
	.byte		        Cs2 
	.byte		N12   , As2 
	.byte		N12   , Cs3 
	.byte	W18
	.byte		N24   , Ds3 
	.byte	W12
	.byte		N18   , Bn2 
	.byte	W18
	.byte		N24   , Gs1 
	.byte		N24   , En2 
	.byte		N24   , Bn2 
	.byte		N24   , Ds3 
	.byte	W24
	.byte		        Bn1 
	.byte		N24   , Gs2 
	.byte		N24   , Cs3 
	.byte		N24   , Ds3 
	.byte	W24
@ 153   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_113
@ 154   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_114
@ 155   ----------------------------------------
	.byte	W96
@ 156   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_017
@ 157   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_034
@ 158   ----------------------------------------
	.byte	W12
	.byte		N36   , Ds3 , v096
	.byte	W06
	.byte		N30   , Bn2 
	.byte	W18
	.byte		N12   , Gs2 
	.byte	W18
	.byte		N18   
	.byte		N18   , Bn2 
	.byte		N30   , Ds3 
	.byte	W18
	.byte		N24   , Bn2 
	.byte	W12
	.byte		N12   , Gn2 
	.byte		N12   , Ds3 
	.byte	W12
@ 159   ----------------------------------------
	.byte		        Fs2 
	.byte		N12   , Bn2 
	.byte	W12
	.byte		N06   , Cs3 
	.byte	W18
	.byte		        Fs2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N54   , Fs2 
	.byte		N54   , Bn2 
	.byte	W18
	.byte		N36   , Cs3 
	.byte	W36
@ 160   ----------------------------------------
	.byte	W96
@ 161   ----------------------------------------
	.byte	W96
@ 162   ----------------------------------------
	.byte	W96
@ 163   ----------------------------------------
	.byte	W96
@ 164   ----------------------------------------
	.byte	W96
@ 165   ----------------------------------------
	.byte	W96
@ 166   ----------------------------------------
	.byte	W96
@ 167   ----------------------------------------
	.byte	W96
@ 168   ----------------------------------------
	.byte	W96
@ 169   ----------------------------------------
	.byte	W96
@ 170   ----------------------------------------
	.byte	W96
@ 171   ----------------------------------------
	.byte	W96
@ 172   ----------------------------------------
	.byte	W96
@ 173   ----------------------------------------
	.byte	W96
@ 174   ----------------------------------------
	.byte	W96
@ 175   ----------------------------------------
	.byte	W96
@ 176   ----------------------------------------
	.byte	W12
	.byte		N06   , Ds3 
	.byte	W18
	.byte		        En2 
	.byte		N06   , Cs3 
	.byte	W12
	.byte		N24   , En2 
	.byte		N24   , Cs3 
	.byte	W18
	.byte		N06   , Ds3 
	.byte	W18
	.byte		        Ds2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N18   , Ds2 
	.byte		N18   , Bn2 
	.byte	W06
@ 177   ----------------------------------------
	.byte	W12
	.byte		N06   , Fs3 
	.byte	W18
	.byte		        Ds2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N24   , Ds2 
	.byte		N24   , Bn2 
	.byte	W18
	.byte		N06   , Fs3 
	.byte	W18
	.byte		        Ds2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N18   , Gs2 
	.byte		N18   , Bn2 
	.byte	W06
@ 178   ----------------------------------------
	.byte	W12
	.byte		N06   , Ds3 
	.byte	W18
	.byte		        Gs2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N18   , Gs2 
	.byte		N18   , Bn2 
	.byte	W18
	.byte		N06   , Ds3 
	.byte	W18
	.byte		        Gs2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N18   , Fs2 
	.byte		N18   , Bn2 
	.byte	W06
@ 179   ----------------------------------------
	.byte	W12
	.byte		N06   , Cs3 
	.byte	W18
	.byte		        Fs2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N18   , Fs2 
	.byte		N18   , Bn2 
	.byte	W18
	.byte		N06   , Cs3 
	.byte	W18
	.byte		        En2 
	.byte		N06   , Cs3 
	.byte	W12
	.byte		        En2 
	.byte		N06   , Cs3 
	.byte	W06
@ 180   ----------------------------------------
	.byte	W96
@ 181   ----------------------------------------
	.byte		        Bn3 , v112
	.byte	W06
	.byte		N18   , Fs3 
	.byte	W06
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        Cs4 
	.byte	W12
	.byte		        Gs2 
	.byte		N06   , Ds3 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte		N24   , As3 
	.byte	W12
	.byte		N12   , Fs3 
	.byte	W12
	.byte		N06   , Cs2 
	.byte		N06   , Gs2 
	.byte		N06   , Ds3 
	.byte	W12
	.byte		N12   , Ds2 
	.byte		N12   , As2 
	.byte		N12   , Fs3 
	.byte	W18
@ 182   ----------------------------------------
	.byte	W06
	.byte		N06   , Bn2 
	.byte	W06
	.byte		N12   
	.byte	W12
	.byte		        En1 , v096
	.byte	W12
	.byte		N18   , Bn1 , v112
	.byte		N18   , Fs2 
	.byte		N18   , Cs3 
	.byte	W18
	.byte		N12   , Cs2 
	.byte		N12   , Gs2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N24   , Bn2 
	.byte	W06
	.byte		N18   , En3 
	.byte	W06
	.byte		N12   , Fs3 
	.byte	W06
	.byte		N06   , Ds4 
	.byte	W06
@ 183   ----------------------------------------
	.byte	W96
@ 184   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_001
@ 185   ----------------------------------------
	.byte	W96
@ 186   ----------------------------------------
	.byte		N06   , Bn3 , v112
	.byte	W06
	.byte		N18   , Fs3 
	.byte	W06
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        Cs4 
	.byte	W12
	.byte		        Gs2 
	.byte		N06   , Ds3 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N24   , Cs3 
	.byte		N24   , As3 
	.byte	W12
	.byte		N12   , Fs3 
	.byte	W12
	.byte		        Cs2 , v096
	.byte		N12   , Gs2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		        En3 
	.byte	W12
@ 187   ----------------------------------------
	.byte	W96
@ 188   ----------------------------------------
mus_custom_flockofbirds_1_188:
	.byte		N12   , En1 , v096
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W12
	.byte		N06   , En1 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        En3 
	.byte	W06
	.byte		        Fs3 
	.byte	W12
	.byte		        Bn2 
	.byte	W30
	.byte		        Fs2 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		N12   , Bn2 
	.byte	W12
	.byte	PEND
@ 189   ----------------------------------------
mus_custom_flockofbirds_1_189:
	.byte		N12   , Gs1 , v096
	.byte		N12   , Fs2 
	.byte		N12   , Bn2 
	.byte	W18
	.byte		N06   
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W12
	.byte		N18   , Fs1 
	.byte		N18   , Fs2 
	.byte		N12   , Bn2 
	.byte	W12
	.byte		N06   , As2 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		        Fs2 
	.byte	W18
	.byte		N12   
	.byte	W12
	.byte	PEND
@ 190   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_188
@ 191   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_189
@ 192   ----------------------------------------
mus_custom_flockofbirds_1_192:
	.byte		N48   , Bn2 , v096
	.byte		N48   , Fs3 
	.byte		N48   , Ds4 
	.byte	W54
	.byte		N18   , Ds3 
	.byte		N18   , Bn3 
	.byte		N18   , Fs4 
	.byte	W18
	.byte		N12   , Cs3 
	.byte		N12   , Gs3 
	.byte		N12   , Ds4 
	.byte	W12
	.byte		N48   , Cs3 
	.byte		N48   , Fs3 
	.byte		N48   , Cs4 
	.byte	W12
	.byte	PEND
@ 193   ----------------------------------------
mus_custom_flockofbirds_1_193:
	.byte	W42
	.byte		N06   , Bn3 , v096
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		N48   , En1 
	.byte		N48   , Bn2 
	.byte		N48   , En3 
	.byte	W24
	.byte	PEND
@ 194   ----------------------------------------
	.byte	W24
	.byte		N36   , En1 
	.byte		N36   , Bn2 
	.byte		N36   , En3 
	.byte	W18
	.byte		N18   , Gs3 
	.byte	W18
	.byte		N36   , Fs1 
	.byte		N36   , As2 
	.byte		N36   , Fs3 
	.byte	W36
@ 195   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_192
@ 196   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_193
@ 197   ----------------------------------------
	.byte	W24
	.byte		N36   , En1 , v096
	.byte		N36   , Bn2 
	.byte		N36   , En3 
	.byte	W18
	.byte		N18   , Gs3 
	.byte	W18
	.byte		N36   , Fs1 
	.byte		N36   , As2 
	.byte		N18   , Fs3 
	.byte	W18
	.byte		        En3 
	.byte	W18
@ 198   ----------------------------------------
	.byte		        Ds3 
	.byte	W96
@ 199   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_016
@ 200   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_017
@ 201   ----------------------------------------
	.byte		N12   , Ds2 , v096
	.byte		N12   , Bn2 
	.byte	W12
	.byte		N06   , Fs3 
	.byte	W18
	.byte		        Ds2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N24   , Ds2 
	.byte		N24   , Bn2 
	.byte	W18
	.byte		N06   , Fs3 
	.byte	W18
	.byte		        Ds2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		        Gs2 
	.byte		N06   , Bn2 
	.byte	W06
@ 202   ----------------------------------------
	.byte	W96
@ 203   ----------------------------------------
mus_custom_flockofbirds_1_203:
	.byte		N24   , Fs1 , v096
	.byte		N06   , As2 
	.byte	W06
	.byte		N18   , Bn2 
	.byte	W06
	.byte		N12   , Cs3 
	.byte	W06
	.byte		N06   , Fs3 
	.byte	W06
	.byte		N01   , En2 
	.byte		N01   , Cs3 
	.byte	W12
	.byte		N36   , Gs1 
	.byte		N36   , Bn2 
	.byte	W24
	.byte		N12   , Cs3 
	.byte	W12
	.byte		N01   , En2 
	.byte		N01   , Cs3 
	.byte	W12
	.byte		N66   , En1 
	.byte		N66   , Gs2 
	.byte	W12
	.byte	PEND
@ 204   ----------------------------------------
mus_custom_flockofbirds_1_204:
	.byte	W12
	.byte		N12   , Ds3 , v096
	.byte	W12
	.byte		N01   , En2 
	.byte		N01   , Cs3 
	.byte	W30
	.byte		N18   , Bn2 
	.byte	W18
	.byte		N12   , Gs2 
	.byte	W12
	.byte		        As2 
	.byte	W12
	.byte	PEND
@ 205   ----------------------------------------
mus_custom_flockofbirds_1_205:
	.byte		N24   , Fs1 , v096
	.byte		N06   , As2 
	.byte	W06
	.byte		N18   , Bn2 
	.byte	W06
	.byte		N12   , Cs3 
	.byte	W06
	.byte		N06   , Fs3 
	.byte	W06
	.byte		N01   , En2 
	.byte		N01   , Cs3 
	.byte	W12
	.byte		N36   , Gs1 
	.byte		N36   , Bn2 
	.byte	W24
	.byte		N12   , Cs3 
	.byte	W12
	.byte		N01   , En2 
	.byte		N01   , Cs3 
	.byte	W12
	.byte		TIE   , Bn1 
	.byte		N84   , En3 
	.byte	W12
	.byte	PEND
@ 206   ----------------------------------------
mus_custom_flockofbirds_1_206:
	.byte	W12
	.byte		N42   , Bn3 , v096
	.byte	W24
	.byte		N18   , As3 
	.byte	W18
	.byte		        Ds3 
	.byte	W18
	.byte		N06   , En3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte	PEND
@ 207   ----------------------------------------
mus_custom_flockofbirds_1_207:
	.byte		N06   , An1 , v096
	.byte		N06   , Cs3 
	.byte	W06
	.byte		N18   , Dn3 
	.byte	W06
	.byte		N12   , En3 
	.byte	W06
	.byte		N06   , An3 
	.byte	W06
	.byte	PEND
	.byte		EOT   , Bn1 
	.byte		N01   , En1 
	.byte		N01   , Gn2 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N36   , Bn1 
	.byte		N36   , Dn3 
	.byte	W24
	.byte		N12   , En3 
	.byte	W12
	.byte		N01   , En1 
	.byte		N01   , Gn2 
	.byte		N01   , En3 
	.byte	W12
	.byte		N36   , Gn1 
	.byte		N36   , Bn2 
	.byte	W12
@ 208   ----------------------------------------
mus_custom_flockofbirds_1_208:
	.byte	W12
	.byte		N12   , Fs3 , v096
	.byte	W12
	.byte		N01   , En1 
	.byte		N01   , Gn2 
	.byte		N01   , En3 
	.byte	W30
	.byte		N18   , Dn3 
	.byte	W18
	.byte		N12   , Bn2 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte	PEND
@ 209   ----------------------------------------
mus_custom_flockofbirds_1_209:
	.byte		N24   , An1 , v096
	.byte		N06   , Cs3 
	.byte	W06
	.byte		N18   , Dn3 
	.byte	W06
	.byte		N12   , En3 
	.byte	W06
	.byte		N06   , An3 
	.byte	W06
	.byte		N01   , En1 
	.byte		N01   , Gn2 
	.byte		N01   , En3 
	.byte	W12
	.byte		N36   , Bn1 
	.byte		N36   , Dn3 
	.byte	W24
	.byte		N12   , En3 
	.byte	W12
	.byte		N01   , En1 
	.byte		N01   , Gn2 
	.byte		N01   , En3 
	.byte	W12
	.byte		N54   , Dn2 
	.byte		N78   , Gn3 
	.byte	W12
	.byte	PEND
@ 210   ----------------------------------------
mus_custom_flockofbirds_1_210:
	.byte	W12
	.byte		N30   , Dn4 , v096
	.byte	W24
	.byte		        Cs4 
	.byte	W06
	.byte		N24   , En1 
	.byte	W12
	.byte		N12   , Dn4 
	.byte	W12
	.byte		N06   , Fs1 
	.byte	W06
	.byte		N24   , Fs4 
	.byte	W24
	.byte	PEND
@ 211   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_203
@ 212   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_204
@ 213   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_205
@ 214   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_206
@ 215   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_207
	.byte		EOT   , Bn1 
	.byte		N01   , En1 , v096
	.byte		N01   , Gn2 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N36   , Bn1 
	.byte		N36   , Dn3 
	.byte	W24
	.byte		N12   , En3 
	.byte	W12
	.byte		N01   , En1 
	.byte		N01   , Gn2 
	.byte		N01   , En3 
	.byte	W12
	.byte		N36   , Gn1 
	.byte		N36   , Bn2 
	.byte	W12
@ 216   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_208
@ 217   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_209
@ 218   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_1_210
@ 219   ----------------------------------------
	.byte		N96   , Gn1 , v127
	.byte	W01
	.byte		N92   , Dn2 , v096, gtp2
	.byte	W02
	.byte		        Bn2 , v096, gtp1
	.byte	W01
	.byte		N90   , Cs3 , v096, gtp1
	.byte	W02
	.byte		        An3 
	.byte	W90
@ 220   ----------------------------------------
	.byte	FINE

@**************** Track 2 (Midi-Chn.2) ****************@

mus_custom_flockofbirds_2:
	.byte	KEYSH , mus_custom_flockofbirds_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 28
	.byte		VOL   , 96*mus_custom_flockofbirds_mvl/mxv
	.byte		PAN   , c_v-45
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
mus_custom_flockofbirds_2_013:
	.byte		BEND  , c_v+0
	.byte		N12   , Cs3 , v096
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
	.byte	PEND
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
	.byte	PATT
	 .word	mus_custom_flockofbirds_2_013
@ 042   ----------------------------------------
	.byte	W96
@ 043   ----------------------------------------
	.byte	W96
@ 044   ----------------------------------------
	.byte	W96
@ 045   ----------------------------------------
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		N12   , En3 , v096
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
	.byte	W72
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
	.byte	W96
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
	.byte	W96
@ 094   ----------------------------------------
	.byte	W96
@ 095   ----------------------------------------
	.byte	W96
@ 096   ----------------------------------------
	.byte	W96
@ 097   ----------------------------------------
	.byte	W96
@ 098   ----------------------------------------
	.byte	W96
@ 099   ----------------------------------------
	.byte	W96
@ 100   ----------------------------------------
	.byte	W96
@ 101   ----------------------------------------
	.byte	W96
@ 102   ----------------------------------------
	.byte	W96
@ 103   ----------------------------------------
	.byte	W96
@ 104   ----------------------------------------
	.byte	W96
@ 105   ----------------------------------------
	.byte	W96
@ 106   ----------------------------------------
	.byte	W96
@ 107   ----------------------------------------
	.byte	W96
@ 108   ----------------------------------------
	.byte	W96
@ 109   ----------------------------------------
	.byte	W96
@ 110   ----------------------------------------
	.byte	W96
@ 111   ----------------------------------------
	.byte	W96
@ 112   ----------------------------------------
	.byte	W96
@ 113   ----------------------------------------
	.byte	W96
@ 114   ----------------------------------------
	.byte	W96
@ 115   ----------------------------------------
	.byte	W96
@ 116   ----------------------------------------
	.byte	W96
@ 117   ----------------------------------------
	.byte	W96
@ 118   ----------------------------------------
	.byte	W96
@ 119   ----------------------------------------
	.byte	W96
@ 120   ----------------------------------------
	.byte	W96
@ 121   ----------------------------------------
	.byte	W96
@ 122   ----------------------------------------
	.byte	W96
@ 123   ----------------------------------------
	.byte	W96
@ 124   ----------------------------------------
	.byte	W96
@ 125   ----------------------------------------
	.byte	W96
@ 126   ----------------------------------------
	.byte	W96
@ 127   ----------------------------------------
	.byte	W96
@ 128   ----------------------------------------
	.byte	W96
@ 129   ----------------------------------------
	.byte	W96
@ 130   ----------------------------------------
	.byte	W96
@ 131   ----------------------------------------
	.byte	W96
@ 132   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_2_013
@ 133   ----------------------------------------
	.byte	W96
@ 134   ----------------------------------------
	.byte	W96
@ 135   ----------------------------------------
	.byte	W96
@ 136   ----------------------------------------
	.byte	W96
@ 137   ----------------------------------------
	.byte	W96
@ 138   ----------------------------------------
	.byte	W96
@ 139   ----------------------------------------
	.byte	W96
@ 140   ----------------------------------------
	.byte	W96
@ 141   ----------------------------------------
	.byte	W96
@ 142   ----------------------------------------
	.byte	W96
@ 143   ----------------------------------------
	.byte	W96
@ 144   ----------------------------------------
	.byte	W96
@ 145   ----------------------------------------
	.byte	W96
@ 146   ----------------------------------------
	.byte	W96
@ 147   ----------------------------------------
	.byte	W96
@ 148   ----------------------------------------
	.byte	W96
@ 149   ----------------------------------------
	.byte	W96
@ 150   ----------------------------------------
	.byte	W96
@ 151   ----------------------------------------
	.byte	W96
@ 152   ----------------------------------------
	.byte	W96
@ 153   ----------------------------------------
	.byte	W96
@ 154   ----------------------------------------
	.byte	W96
@ 155   ----------------------------------------
	.byte	W96
@ 156   ----------------------------------------
	.byte	W96
@ 157   ----------------------------------------
	.byte	W96
@ 158   ----------------------------------------
	.byte	W96
@ 159   ----------------------------------------
	.byte	W96
@ 160   ----------------------------------------
	.byte	W96
@ 161   ----------------------------------------
	.byte	W96
@ 162   ----------------------------------------
	.byte	W96
@ 163   ----------------------------------------
	.byte	W96
@ 164   ----------------------------------------
	.byte	W96
@ 165   ----------------------------------------
	.byte	W96
@ 166   ----------------------------------------
	.byte	W96
@ 167   ----------------------------------------
	.byte	W96
@ 168   ----------------------------------------
	.byte	W96
@ 169   ----------------------------------------
	.byte	W96
@ 170   ----------------------------------------
	.byte	W96
@ 171   ----------------------------------------
	.byte	W96
@ 172   ----------------------------------------
	.byte	W96
@ 173   ----------------------------------------
	.byte	W96
@ 174   ----------------------------------------
	.byte	W96
@ 175   ----------------------------------------
	.byte	W96
@ 176   ----------------------------------------
	.byte	W96
@ 177   ----------------------------------------
	.byte	W96
@ 178   ----------------------------------------
	.byte	W96
@ 179   ----------------------------------------
	.byte	W96
@ 180   ----------------------------------------
	.byte	W96
@ 181   ----------------------------------------
	.byte	W90
	.byte		BEND  , c_v+27
	.byte		N09   , Ds3 , v112
	.byte	W04
	.byte		BEND  , c_v+27
	.byte	W02
@ 182   ----------------------------------------
	.byte		        c_v+27
	.byte		        c_v+26
	.byte		        c_v+25
	.byte		        c_v+24
	.byte	W01
	.byte		        c_v+23
	.byte		        c_v+22
	.byte		        c_v+21
	.byte		        c_v+20
	.byte		        c_v+19
	.byte		        c_v+18
	.byte		        c_v+17
	.byte		        c_v+16
	.byte		        c_v+15
	.byte		        c_v+14
	.byte		        c_v+13
	.byte		        c_v+12
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+10
	.byte		        c_v+9
	.byte		        c_v+8
	.byte		        c_v+7
	.byte		        c_v+6
	.byte		        c_v+5
	.byte		        c_v+4
	.byte		        c_v+3
	.byte		        c_v+2
	.byte		        c_v+1
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W92
	.byte	W01
@ 183   ----------------------------------------
	.byte	W96
@ 184   ----------------------------------------
	.byte	W96
@ 185   ----------------------------------------
	.byte	W96
@ 186   ----------------------------------------
	.byte	W96
@ 187   ----------------------------------------
	.byte	W96
@ 188   ----------------------------------------
mus_custom_flockofbirds_2_188:
	.byte	W54
	.byte		BEND  , c_v+11
	.byte		N12   , Cs3 , v096
	.byte	W04
	.byte		BEND  , c_v+11
	.byte		        c_v+10
	.byte		        c_v+9
	.byte		        c_v+8
	.byte		        c_v+7
	.byte		        c_v+6
	.byte		        c_v+5
	.byte		        c_v+4
	.byte		        c_v+3
	.byte		        c_v+2
	.byte		        c_v+1
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v+0
	.byte	W03
	.byte		        c_v+0
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W30
	.byte	PEND
@ 189   ----------------------------------------
mus_custom_flockofbirds_2_189:
	.byte	W72
	.byte		N12   , Gs2 , v096
	.byte	W04
	.byte		BEND  , c_v+0
	.byte	W04
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+0
	.byte	W12
	.byte	PEND
@ 190   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_2_188
@ 191   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_2_189
@ 192   ----------------------------------------
	.byte	W96
@ 193   ----------------------------------------
	.byte	W96
@ 194   ----------------------------------------
	.byte	W96
@ 195   ----------------------------------------
	.byte	W96
@ 196   ----------------------------------------
	.byte	W96
@ 197   ----------------------------------------
	.byte	W96
@ 198   ----------------------------------------
	.byte	W96
@ 199   ----------------------------------------
	.byte	W96
@ 200   ----------------------------------------
	.byte	W96
@ 201   ----------------------------------------
	.byte	W96
@ 202   ----------------------------------------
	.byte	W96
@ 203   ----------------------------------------
	.byte	W96
@ 204   ----------------------------------------
mus_custom_flockofbirds_2_204:
	.byte	W32
	.byte	W02
	.byte		N01   , Cs3 , v127
	.byte	W02
	.byte		N18   , Cs3 , v096
	.byte	W60
	.byte	PEND
@ 205   ----------------------------------------
	.byte	W96
@ 206   ----------------------------------------
	.byte	W96
@ 207   ----------------------------------------
	.byte	W96
@ 208   ----------------------------------------
mus_custom_flockofbirds_2_208:
	.byte	W32
	.byte	W02
	.byte		N01   , Fs3 , v127
	.byte	W02
	.byte		N18   , En3 , v096
	.byte	W60
	.byte	PEND
@ 209   ----------------------------------------
	.byte	W96
@ 210   ----------------------------------------
	.byte	W96
@ 211   ----------------------------------------
	.byte	W96
@ 212   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_2_204
@ 213   ----------------------------------------
	.byte	W96
@ 214   ----------------------------------------
	.byte	W96
@ 215   ----------------------------------------
	.byte	W96
@ 216   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_2_208
@ 217   ----------------------------------------
	.byte	W96
@ 218   ----------------------------------------
	.byte	W96
@ 219   ----------------------------------------
	.byte	W96
@ 220   ----------------------------------------
	.byte	FINE

@**************** Track 3 (Midi-Chn.3) ****************@

mus_custom_flockofbirds_3:
	.byte	KEYSH , mus_custom_flockofbirds_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 26
	.byte		VOL   , 96*mus_custom_flockofbirds_mvl/mxv
	.byte		PAN   , c_v+41
	.byte		BEND  , c_v+0
	.byte	W96
@ 001   ----------------------------------------
mus_custom_flockofbirds_3_001:
	.byte		N12   , En1 , v096
	.byte	W18
	.byte		N06   , Cs3 
	.byte	W06
	.byte		N12   , Bn2 
	.byte	W06
	.byte		N18   , As2 
	.byte	W06
	.byte		N06   , Gs2 
	.byte	W06
	.byte		        Fs2 
	.byte	W06
	.byte		N12   , Gs1 
	.byte	W12
	.byte		N30   , Gs2 
	.byte	W06
	.byte		N12   , Cs3 
	.byte	W12
	.byte		N18   , Ds3 
	.byte	W12
	.byte		N06   , Bn2 
	.byte	W06
	.byte	PEND
@ 002   ----------------------------------------
mus_custom_flockofbirds_3_002:
	.byte		N12   , Fs1 , v096
	.byte	W18
	.byte		N06   , Ds3 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		        En3 
	.byte	W06
	.byte		        Fs2 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N24   , Cs2 
	.byte		N24   , En2 
	.byte		N24   , Cs3 
	.byte	W24
	.byte		        Ds2 
	.byte	W06
	.byte		N18   , Bn2 
	.byte	W18
	.byte	PEND
@ 003   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_001
@ 004   ----------------------------------------
mus_custom_flockofbirds_3_004:
	.byte		N12   , Bn1 , v096
	.byte	W18
	.byte		N06   , Ds3 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		        En3 
	.byte	W06
	.byte		        Fs2 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N24   , Cs2 
	.byte		N24   , Bn2 
	.byte	W24
	.byte		N06   , Ds2 
	.byte		N06   , Cs3 
	.byte	W24
	.byte	PEND
@ 005   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_001
@ 006   ----------------------------------------
	.byte		N12   , Fs1 , v096
	.byte	W18
	.byte		N06   , Ds3 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		        En3 
	.byte	W06
	.byte		        Fs2 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N24   , Cs2 
	.byte		N48   , En2 
	.byte		N24   , Cs3 
	.byte	W24
	.byte		        Ds2 
	.byte	W06
	.byte		N18   , Bn2 
	.byte	W18
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_001
@ 008   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_004
@ 009   ----------------------------------------
	.byte	W06
	.byte		N18   , Fs2 , v096
	.byte		N18   , Fs3 
	.byte	W18
	.byte		N12   , En1 , v112
	.byte	W12
	.byte		        As3 , v096
	.byte	W12
	.byte		N06   , Ds3 
	.byte	W06
	.byte		N18   , Fs3 
	.byte	W18
	.byte		N12   
	.byte	W12
	.byte		        En3 
	.byte	W12
@ 010   ----------------------------------------
	.byte		        Gs2 , v112
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N06   , Gs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		N24   , Cs3 
	.byte	W24
	.byte		N03   , Ds4 
	.byte	W03
	.byte		        Cs4 
	.byte	W03
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
@ 011   ----------------------------------------
	.byte	W06
	.byte		N18   , Fs2 
	.byte		N18   , Fs3 , v096
	.byte	W18
	.byte		N12   , En1 , v112
	.byte	W12
	.byte		        As3 , v096
	.byte	W12
	.byte		N06   , Fs3 
	.byte	W06
	.byte		N12   , Ds3 
	.byte	W12
	.byte		N06   , Bn2 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		N18   , Fs3 
	.byte	W18
@ 012   ----------------------------------------
	.byte		N12   , Gs2 , v112
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N06   , Gs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		N24   , Cs3 
	.byte	W48
	.byte		N06   , Cs3 , v096
	.byte	W06
@ 013   ----------------------------------------
mus_custom_flockofbirds_3_013:
	.byte	W12
	.byte		N12   , En2 , v112
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 , v096
	.byte	W12
	.byte		        En1 , v112
	.byte	W24
	.byte		N01   , Gs3 , v096
	.byte	W06
	.byte		N18   , As3 
	.byte	W18
	.byte		N12   , Fs3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte	PEND
@ 014   ----------------------------------------
	.byte		        Gs2 , v112
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N06   , Gs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		N24   , Cs3 
	.byte	W24
	.byte		N12   , Cs2 
	.byte		N12   , Gs2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		        En3 
	.byte	W12
@ 015   ----------------------------------------
	.byte	W06
	.byte		N18   , Fs2 
	.byte		N18   , Fs3 
	.byte	W18
	.byte		N12   , En1 
	.byte	W24
	.byte		N06   , Cs4 , v096
	.byte	W24
	.byte		N12   , En2 
	.byte		N12   , Fs3 
	.byte	W12
	.byte		        Ds2 
	.byte		N12   , En3 
	.byte	W12
@ 016   ----------------------------------------
	.byte		        Gs2 , v112
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N06   , Gs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		N24   , Cs3 
	.byte	W30
	.byte		N06   , Bn2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 , v096
	.byte	W06
	.byte		        Fs3 
	.byte	W06
@ 017   ----------------------------------------
	.byte		N12   , Ds3 , v080
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
	.byte		N72   , En2 , v096
	.byte		N72   , Bn2 
	.byte		N72   , Ds3 
	.byte	W96
@ 034   ----------------------------------------
	.byte	W96
@ 035   ----------------------------------------
	.byte	W96
@ 036   ----------------------------------------
	.byte	W96
@ 037   ----------------------------------------
mus_custom_flockofbirds_3_037:
	.byte	W24
	.byte		N24   , En1 , v096
	.byte	W12
	.byte		N12   , Bn2 
	.byte		N18   , As3 
	.byte	W36
	.byte		N12   , En2 
	.byte		N12   , Fs3 
	.byte	W12
	.byte		N30   , Ds2 
	.byte		N12   , En3 
	.byte	W12
	.byte	PEND
@ 038   ----------------------------------------
mus_custom_flockofbirds_3_038:
	.byte		N18   , Gs1 , v096
	.byte	W18
	.byte		N06   , Gs3 , v112
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		N24   , Cs3 
	.byte	W30
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte	PEND
@ 039   ----------------------------------------
	.byte		N24   , Fs3 , v096
	.byte	W24
	.byte		N12   , En1 , v112
	.byte	W24
	.byte		N06   , Cs4 , v096
	.byte	W24
	.byte		N12   , Fs3 
	.byte	W12
	.byte		        En3 
	.byte	W12
@ 040   ----------------------------------------
	.byte		        Gs2 , v112
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N06   , Gs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W12
	.byte		N24   , Bn1 , v096
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte	W24
	.byte		        Gn1 
	.byte		N24   , Dn2 
	.byte		N24   , Bn2 
	.byte	W24
@ 041   ----------------------------------------
	.byte		        Fs1 
	.byte		N24   , Cs2 
	.byte		N24   , Bn2 
	.byte	W24
	.byte		N12   , En1 
	.byte	W24
	.byte		N01   , Gs3 
	.byte	W06
	.byte		N18   , As3 
	.byte	W18
	.byte		N12   , Fs3 
	.byte	W12
	.byte		        En3 
	.byte	W12
@ 042   ----------------------------------------
mus_custom_flockofbirds_3_042:
	.byte		N12   , Gs1 , v096
	.byte		N12   , Gs2 
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N06   , Gs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Fs1 
	.byte		N06   , Cs3 
	.byte	W12
	.byte		N24   , Fn1 
	.byte		N24   , Cs3 
	.byte	W24
	.byte		N12   , Cs2 , v112
	.byte		N12   , Gs2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		        En3 
	.byte	W12
	.byte	PEND
@ 043   ----------------------------------------
mus_custom_flockofbirds_3_043:
	.byte	W12
	.byte		N12   , En1 , v096
	.byte	W36
	.byte		        Gs2 
	.byte		N12   , Ds3 
	.byte		N12   , Bn3 
	.byte	W12
	.byte		        As3 
	.byte	W12
	.byte		        Fn2 
	.byte		N12   , Cs3 
	.byte		N12   , Gs3 
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte	PEND
@ 044   ----------------------------------------
	.byte		        En2 
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N06   , Gs3 , v112
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		N24   , Cs3 
	.byte	W30
	.byte		N06   , Bn3 , v096
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
@ 045   ----------------------------------------
	.byte		N12   , Bn2 
	.byte	W42
	.byte		        Cs3 
	.byte	W42
	.byte		N06   , Bn2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
@ 046   ----------------------------------------
	.byte		        Ds3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        En3 
	.byte	W12
	.byte		N12   , Ds3 
	.byte	W12
	.byte		N06   , Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		N12   , Cs3 
	.byte	W12
	.byte		N06   , Ds3 
	.byte	W06
	.byte		        Bn2 
	.byte	W12
	.byte		        As2 
	.byte	W06
	.byte		TIE   , Gs2 
	.byte	W12
@ 047   ----------------------------------------
	.byte	W96
	.byte		EOT   
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
	.byte	W96
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
	.byte		N12   , Ds3 , v080
	.byte	W24
	.byte		        En3 , v096
	.byte	W12
	.byte		        Ds3 
	.byte	W24
	.byte		        Cs3 
	.byte	W24
	.byte		        As3 
	.byte	W12
@ 083   ----------------------------------------
mus_custom_flockofbirds_3_083:
	.byte		N24   , Fs1 , v096
	.byte		N06   , As2 
	.byte	W06
	.byte		N18   , Bn2 
	.byte	W06
	.byte		N12   , Cs3 
	.byte	W06
	.byte		N06   , Fs3 
	.byte	W06
	.byte		N01   , En2 
	.byte		N01   , Cs3 
	.byte	W12
	.byte		N36   , Gs1 
	.byte		N36   , Bn2 
	.byte	W24
	.byte		N12   , Cs3 
	.byte	W12
	.byte		N01   , En2 
	.byte		N01   , Cs3 
	.byte	W12
	.byte		N66   , En1 
	.byte		N66   , Gs2 
	.byte	W12
	.byte	PEND
@ 084   ----------------------------------------
mus_custom_flockofbirds_3_084:
	.byte	W12
	.byte		N12   , Ds3 , v096
	.byte	W12
	.byte		N01   , En2 
	.byte		N01   , Cs3 
	.byte	W30
	.byte		N18   , Bn2 
	.byte	W18
	.byte		N12   , Gs2 
	.byte	W12
	.byte		        As2 
	.byte	W12
	.byte	PEND
@ 085   ----------------------------------------
mus_custom_flockofbirds_3_085:
	.byte		N24   , Fs1 , v096
	.byte		N06   , As2 
	.byte	W06
	.byte		N18   , Bn2 
	.byte	W06
	.byte		N12   , Cs3 
	.byte	W06
	.byte		N06   , Fs3 
	.byte	W06
	.byte		N01   , En2 
	.byte		N01   , Cs3 
	.byte	W12
	.byte		N36   , Gs1 
	.byte		N36   , Bn2 
	.byte	W24
	.byte		N12   , Cs3 
	.byte	W12
	.byte		N01   , En2 
	.byte		N01   , Cs3 
	.byte	W12
	.byte		N84   , Bn1 
	.byte		N84   , En3 
	.byte	W12
	.byte	PEND
@ 086   ----------------------------------------
mus_custom_flockofbirds_3_086:
	.byte	W12
	.byte		N42   , Bn3 , v096
	.byte	W24
	.byte		N18   , As3 
	.byte	W18
	.byte		        Ds3 
	.byte	W18
	.byte		N06   , En3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte	PEND
@ 087   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_083
@ 088   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_084
@ 089   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_085
@ 090   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_086
@ 091   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_083
@ 092   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_084
@ 093   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_085
@ 094   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_086
@ 095   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_083
@ 096   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_084
@ 097   ----------------------------------------
mus_custom_flockofbirds_3_097:
	.byte		N24   , Fs1 , v096
	.byte		N06   , As2 
	.byte	W06
	.byte		N18   , Bn2 
	.byte	W06
	.byte		N12   , Cs3 
	.byte	W06
	.byte		N06   , Fs3 
	.byte	W06
	.byte		N01   , En2 
	.byte		N01   , Cs3 
	.byte	W12
	.byte		N36   , Gs1 
	.byte		N36   , Bn2 
	.byte	W24
	.byte		N12   , Cs3 
	.byte	W12
	.byte		N01   , En2 
	.byte		N01   , Cs3 
	.byte	W12
	.byte		N78   , Bn1 
	.byte		N78   , En3 
	.byte	W12
	.byte	PEND
@ 098   ----------------------------------------
mus_custom_flockofbirds_3_098:
	.byte	W12
	.byte		N30   , Bn3 , v096
	.byte	W24
	.byte		        As3 
	.byte	W06
	.byte		N24   , Cs2 
	.byte	W12
	.byte		N12   , Bn3 
	.byte	W12
	.byte		N30   , Ds2 
	.byte	W06
	.byte		N24   , Ds4 
	.byte	W24
	.byte	PEND
@ 099   ----------------------------------------
mus_custom_flockofbirds_3_099:
	.byte		N96   , En1 , v096
	.byte	W12
	.byte		N84   , Bn2 
	.byte	W03
	.byte		N80   , Gs3 , v096, gtp1
	.byte	W03
	.byte		N78   , As3 
	.byte	W03
	.byte		N72   , Fs4 , v096, gtp3
	.byte	W72
	.byte	W03
	.byte	PEND
@ 100   ----------------------------------------
	.byte	W96
@ 101   ----------------------------------------
	.byte	W96
@ 102   ----------------------------------------
	.byte	W96
@ 103   ----------------------------------------
	.byte	W96
@ 104   ----------------------------------------
	.byte	W96
@ 105   ----------------------------------------
	.byte	W96
@ 106   ----------------------------------------
	.byte	W96
@ 107   ----------------------------------------
	.byte	W96
@ 108   ----------------------------------------
	.byte	W96
@ 109   ----------------------------------------
	.byte	W96
@ 110   ----------------------------------------
	.byte	W96
@ 111   ----------------------------------------
mus_custom_flockofbirds_3_111:
	.byte		N12   , Fs2 , v096
	.byte	W18
	.byte		        Bn2 
	.byte	W12
	.byte		        Ds3 
	.byte	W06
	.byte		N06   , Cs3 
	.byte	W12
	.byte		N12   , Gs1 
	.byte	W18
	.byte		        Cs3 
	.byte	W12
	.byte		N18   , Ds3 
	.byte	W12
	.byte		N06   , Bn2 
	.byte	W06
	.byte	PEND
@ 112   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_002
@ 113   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_001
@ 114   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_004
@ 115   ----------------------------------------
	.byte	W96
@ 116   ----------------------------------------
	.byte	W96
@ 117   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_083
@ 118   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_084
@ 119   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_085
@ 120   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_086
@ 121   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_083
@ 122   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_084
@ 123   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_097
@ 124   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_098
@ 125   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_099
@ 126   ----------------------------------------
	.byte	W96
@ 127   ----------------------------------------
	.byte	W96
@ 128   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_037
@ 129   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_038
@ 130   ----------------------------------------
mus_custom_flockofbirds_3_130:
	.byte		N24   , Fs3 , v096
	.byte	W24
	.byte		N12   , En1 , v112
	.byte	W24
	.byte		N06   , Cs4 , v096
	.byte	W48
	.byte	PEND
@ 131   ----------------------------------------
	.byte		N12   , Gs2 , v112
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N06   , Gs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W24
	.byte		N48   , Bn1 , v096
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte	W24
	.byte		N12   , Gs1 
	.byte		N24   , Ds2 
	.byte		N24   , As2 
	.byte	W12
@ 132   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_013
@ 133   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_042
@ 134   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_043
@ 135   ----------------------------------------
	.byte		N12   , En2 , v096
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N06   , Gs3 , v112
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		N24   , Cs3 
	.byte	W30
	.byte		N06   , Bn2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 , v096
	.byte	W06
	.byte		        Fs3 
	.byte	W06
@ 136   ----------------------------------------
	.byte	W96
@ 137   ----------------------------------------
	.byte	W96
@ 138   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_038
@ 139   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_130
@ 140   ----------------------------------------
	.byte	W96
@ 141   ----------------------------------------
	.byte	W96
@ 142   ----------------------------------------
	.byte	W96
@ 143   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_083
@ 144   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_084
@ 145   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_085
@ 146   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_086
@ 147   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_083
@ 148   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_084
@ 149   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_085
@ 150   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_086
@ 151   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_111
@ 152   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_002
@ 153   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_001
@ 154   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_004
@ 155   ----------------------------------------
	.byte	W96
@ 156   ----------------------------------------
	.byte	W96
@ 157   ----------------------------------------
	.byte	W96
@ 158   ----------------------------------------
	.byte	W96
@ 159   ----------------------------------------
	.byte	W96
@ 160   ----------------------------------------
	.byte	W96
@ 161   ----------------------------------------
	.byte	W96
@ 162   ----------------------------------------
	.byte	W96
@ 163   ----------------------------------------
	.byte	W96
@ 164   ----------------------------------------
	.byte	W96
@ 165   ----------------------------------------
	.byte	W96
@ 166   ----------------------------------------
	.byte	W96
@ 167   ----------------------------------------
	.byte	W96
@ 168   ----------------------------------------
	.byte	W96
@ 169   ----------------------------------------
	.byte	W96
@ 170   ----------------------------------------
	.byte	W96
@ 171   ----------------------------------------
	.byte	W96
@ 172   ----------------------------------------
	.byte	W96
@ 173   ----------------------------------------
	.byte	W96
@ 174   ----------------------------------------
	.byte	W96
@ 175   ----------------------------------------
	.byte	W96
@ 176   ----------------------------------------
	.byte	W96
@ 177   ----------------------------------------
	.byte	W96
@ 178   ----------------------------------------
	.byte	W96
@ 179   ----------------------------------------
	.byte	W96
@ 180   ----------------------------------------
	.byte	W96
@ 181   ----------------------------------------
	.byte		N12   , Gs2 , v112
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N06   , Gs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		N24   , Cs3 
	.byte	W54
@ 182   ----------------------------------------
	.byte	W06
	.byte		N06   , En2 
	.byte		N06   , Bn2 
	.byte	W06
	.byte		N12   , En2 
	.byte		N12   , Bn2 
	.byte	W12
	.byte		        En1 
	.byte	W24
	.byte		N01   , Gs3 , v096
	.byte	W24
	.byte		N12   , Fs3 , v112
	.byte	W12
	.byte		        En3 
	.byte	W12
@ 183   ----------------------------------------
	.byte	W96
@ 184   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_001
@ 185   ----------------------------------------
	.byte	W96
@ 186   ----------------------------------------
	.byte		N12   , Gs2 , v112
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N06   , Gs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		N24   , Cs3 
	.byte	W24
	.byte		N03   , Ds4 , v096
	.byte	W03
	.byte		        Cs4 
	.byte	W03
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
@ 187   ----------------------------------------
	.byte	W96
@ 188   ----------------------------------------
mus_custom_flockofbirds_3_188:
	.byte		N12   , En2 , v096
	.byte		N12   , Fs3 
	.byte		N12   , Bn3 
	.byte	W12
	.byte		N30   , Fs3 
	.byte	W06
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        Cs4 
	.byte	W06
	.byte		N12   , Ds4 
	.byte	W12
	.byte		        Bn2 
	.byte		N12   , Bn3 
	.byte	W12
	.byte		N06   , As2 
	.byte		N06   , As3 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N12   , Gs3 
	.byte	W12
	.byte		        Fs3 
	.byte	W12
	.byte	PEND
@ 189   ----------------------------------------
mus_custom_flockofbirds_3_189:
	.byte		N30   , Ds2 , v096
	.byte		N30   , Bn2 
	.byte	W12
	.byte		N06   , Gs3 
	.byte	W06
	.byte		N12   , Fs3 
	.byte	W12
	.byte		N06   , En3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Bn2 
	.byte	W12
	.byte		N06   
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W18
	.byte		N12   , Bn2 
	.byte	W12
	.byte	PEND
@ 190   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_188
@ 191   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_189
@ 192   ----------------------------------------
	.byte	W96
@ 193   ----------------------------------------
	.byte	W96
@ 194   ----------------------------------------
	.byte	W96
@ 195   ----------------------------------------
	.byte	W96
@ 196   ----------------------------------------
	.byte	W96
@ 197   ----------------------------------------
	.byte	W96
@ 198   ----------------------------------------
	.byte	W96
@ 199   ----------------------------------------
	.byte		N12   , Gs2 , v112
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N06   , Gs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		N24   , Cs3 
	.byte	W30
	.byte		N06   , Bn2 , v096
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
@ 200   ----------------------------------------
	.byte		N12   , Ds3 
	.byte	W96
@ 201   ----------------------------------------
	.byte	W96
@ 202   ----------------------------------------
	.byte	W96
@ 203   ----------------------------------------
	.byte	W96
@ 204   ----------------------------------------
	.byte	W96
@ 205   ----------------------------------------
	.byte	W96
@ 206   ----------------------------------------
	.byte	W96
@ 207   ----------------------------------------
	.byte	W96
@ 208   ----------------------------------------
	.byte	W96
@ 209   ----------------------------------------
	.byte	W96
@ 210   ----------------------------------------
	.byte	W96
@ 211   ----------------------------------------
	.byte	W96
@ 212   ----------------------------------------
	.byte	W96
@ 213   ----------------------------------------
	.byte	W96
@ 214   ----------------------------------------
	.byte	W96
@ 215   ----------------------------------------
	.byte	W96
@ 216   ----------------------------------------
	.byte	W96
@ 217   ----------------------------------------
	.byte	W96
@ 218   ----------------------------------------
	.byte	W96
@ 219   ----------------------------------------
	.byte	W96
@ 220   ----------------------------------------
	.byte	W96
@ 221   ----------------------------------------
	.byte	W66
	.byte		N06   , Cs3 , v127
	.byte	W06
	.byte		        Dn3 
	.byte	W06
	.byte		        En3 
	.byte	W06
	.byte		        An3 
	.byte	W06
	.byte		        Bn3 
	.byte	W06
@ 222   ----------------------------------------
	.byte		N12   , Cs4 
	.byte	W36
	.byte		        Gn3 
	.byte		N12   , An3 
	.byte		N12   , Cs4 
	.byte	W60
@ 223   ----------------------------------------
	.byte		N24   , En1 
	.byte	W06
	.byte		N18   , Bn1 
	.byte	W06
	.byte		N12   , Fs2 
	.byte	W06
	.byte		N06   , Gn2 
	.byte	W06
	.byte		N24   , Fs1 
	.byte	W06
	.byte		N18   , Dn2 
	.byte	W06
	.byte		N12   , En2 
	.byte	W06
	.byte		N06   , An2 
	.byte	W06
	.byte		N48   , Gn1 
	.byte	W06
	.byte		N42   , Dn2 
	.byte	W06
	.byte		N36   , An2 
	.byte	W06
	.byte		N30   , Fs3 
	.byte	W30
@ 224   ----------------------------------------
	.byte	W96
@ 225   ----------------------------------------
	.byte	W96
@ 226   ----------------------------------------
	.byte	W96
@ 227   ----------------------------------------
	.byte	W96
@ 228   ----------------------------------------
mus_custom_flockofbirds_3_228:
	.byte		N36   , Cs2 , v096
	.byte		N36   , En3 
	.byte		N12   , Gs3 
	.byte	W12
	.byte		        An3 
	.byte	W12
	.byte		        Bn3 
	.byte	W12
	.byte		N18   , An1 
	.byte		N18   , Cs3 
	.byte		N18   , En3 
	.byte	W24
	.byte		N24   
	.byte		N24   , Gs3 
	.byte	W24
	.byte		N60   , Fs1 
	.byte		N12   , Gs3 
	.byte	W12
	.byte	PEND
@ 229   ----------------------------------------
mus_custom_flockofbirds_3_229:
	.byte		N48   , Fs3 , v096
	.byte	W48
	.byte		N24   , Gs2 
	.byte		N24   , En3 
	.byte	W24
	.byte		        Gs2 
	.byte		N24   , Fs3 
	.byte	W24
	.byte	PEND
@ 230   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_228
@ 231   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_3_229
@ 232   ----------------------------------------
	.byte	FINE

@**************** Track 4 (Midi-Chn.4) ****************@

mus_custom_flockofbirds_4:
	.byte	KEYSH , mus_custom_flockofbirds_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 26
	.byte		VOL   , 96*mus_custom_flockofbirds_mvl/mxv
	.byte		PAN   , c_v+41
	.byte	W96
@ 001   ----------------------------------------
	.byte	W96
@ 002   ----------------------------------------
	.byte	W96
@ 003   ----------------------------------------
	.byte	W96
@ 004   ----------------------------------------
mus_custom_flockofbirds_4_004:
	.byte	W78
	.byte		BEND  , c_v+0
	.byte		N18   , Ds3 , v096
	.byte	W10
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte	W01
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
	.byte	PEND
@ 005   ----------------------------------------
	.byte		        c_v+16
	.byte		        c_v+0
	.byte	W96
@ 006   ----------------------------------------
	.byte	W96
@ 007   ----------------------------------------
	.byte	W96
@ 008   ----------------------------------------
	.byte	W84
	.byte		        c_v+0
	.byte		        c_v+0
	.byte		N12   , Ds2 , v112
	.byte		N12   , Ds3 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+10
	.byte		        c_v+11
	.byte		        c_v+11
	.byte		        c_v+12
	.byte		        c_v+12
	.byte		        c_v+13
	.byte		        c_v+13
	.byte		        c_v+14
	.byte		        c_v+14
	.byte		        c_v+15
	.byte		        c_v+15
	.byte		        c_v+16
	.byte		        c_v+16
	.byte	W01
	.byte		        c_v+16
	.byte		        c_v+16
	.byte	W06
@ 009   ----------------------------------------
	.byte		        c_v+16
	.byte		        c_v+0
	.byte		        c_v+16
	.byte		        c_v+0
	.byte	W96
@ 010   ----------------------------------------
	.byte	W96
@ 011   ----------------------------------------
	.byte	W96
@ 012   ----------------------------------------
	.byte	W96
@ 013   ----------------------------------------
	.byte		        c_v+0
	.byte		N12   , Cs3 , v096
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
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		N12   , Gs3 
	.byte	W01
	.byte		BEND  , c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W48
@ 014   ----------------------------------------
	.byte	W96
@ 015   ----------------------------------------
mus_custom_flockofbirds_4_015:
	.byte	W36
	.byte		BEND  , c_v+0
	.byte		N12   , Bn3 , v096
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
	.byte	W06
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		N18   , Gs3 
	.byte	W01
	.byte		BEND  , c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W05
	.byte		        c_v+11
	.byte	W09
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W24
	.byte	PEND
@ 016   ----------------------------------------
	.byte	W96
@ 017   ----------------------------------------
	.byte	W12
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		N12   , Bn2 , v080
	.byte	W01
	.byte		BEND  , c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W72
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
	.byte	PATT
	 .word	mus_custom_flockofbirds_4_015
@ 040   ----------------------------------------
	.byte	W96
@ 041   ----------------------------------------
mus_custom_flockofbirds_4_041:
	.byte	W36
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		N12   , Gs3 , v096
	.byte	W01
	.byte		BEND  , c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W48
	.byte	PEND
@ 042   ----------------------------------------
	.byte	W96
@ 043   ----------------------------------------
	.byte	W96
@ 044   ----------------------------------------
	.byte	W96
@ 045   ----------------------------------------
	.byte	W12
	.byte		        c_v+0
	.byte		N12   , En3 
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
	.byte	W06
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		N12   , Cs3 
	.byte	W01
	.byte		BEND  , c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W54
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
	.byte	W96
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
	.byte	W96
@ 084   ----------------------------------------
mus_custom_flockofbirds_4_084:
	.byte	W32
	.byte	W02
	.byte		N01   , Cs3 , v127
	.byte	W02
	.byte		N18   , Cs3 , v096
	.byte	W60
	.byte	PEND
@ 085   ----------------------------------------
	.byte	W96
@ 086   ----------------------------------------
	.byte	W96
@ 087   ----------------------------------------
	.byte	W96
@ 088   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_4_084
@ 089   ----------------------------------------
	.byte	W96
@ 090   ----------------------------------------
	.byte	W96
@ 091   ----------------------------------------
	.byte	W96
@ 092   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_4_084
@ 093   ----------------------------------------
	.byte	W96
@ 094   ----------------------------------------
	.byte	W96
@ 095   ----------------------------------------
	.byte	W96
@ 096   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_4_084
@ 097   ----------------------------------------
	.byte	W96
@ 098   ----------------------------------------
	.byte	W96
@ 099   ----------------------------------------
	.byte	W96
@ 100   ----------------------------------------
	.byte	W96
@ 101   ----------------------------------------
	.byte	W96
@ 102   ----------------------------------------
	.byte	W96
@ 103   ----------------------------------------
	.byte	W96
@ 104   ----------------------------------------
	.byte	W96
@ 105   ----------------------------------------
	.byte	W96
@ 106   ----------------------------------------
	.byte	W96
@ 107   ----------------------------------------
	.byte	W96
@ 108   ----------------------------------------
	.byte	W96
@ 109   ----------------------------------------
	.byte	W96
@ 110   ----------------------------------------
	.byte	W96
@ 111   ----------------------------------------
	.byte	W96
@ 112   ----------------------------------------
	.byte	W96
@ 113   ----------------------------------------
	.byte	W96
@ 114   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_4_004
@ 115   ----------------------------------------
	.byte		BEND  , c_v+16
	.byte		        c_v+0
	.byte	W96
@ 116   ----------------------------------------
	.byte	W96
@ 117   ----------------------------------------
	.byte	W96
@ 118   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_4_084
@ 119   ----------------------------------------
	.byte	W96
@ 120   ----------------------------------------
	.byte	W96
@ 121   ----------------------------------------
	.byte	W96
@ 122   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_4_084
@ 123   ----------------------------------------
	.byte	W96
@ 124   ----------------------------------------
	.byte	W96
@ 125   ----------------------------------------
	.byte	W96
@ 126   ----------------------------------------
	.byte	W96
@ 127   ----------------------------------------
	.byte	W96
@ 128   ----------------------------------------
	.byte	W96
@ 129   ----------------------------------------
	.byte	W96
@ 130   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_4_015
@ 131   ----------------------------------------
	.byte	W96
@ 132   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_4_041
@ 133   ----------------------------------------
	.byte	W96
@ 134   ----------------------------------------
	.byte	W96
@ 135   ----------------------------------------
	.byte	W96
@ 136   ----------------------------------------
	.byte	W96
@ 137   ----------------------------------------
	.byte	W96
@ 138   ----------------------------------------
	.byte	W96
@ 139   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_4_015
@ 140   ----------------------------------------
	.byte	W96
@ 141   ----------------------------------------
	.byte	W96
@ 142   ----------------------------------------
	.byte	W96
@ 143   ----------------------------------------
	.byte	W96
@ 144   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_4_084
@ 145   ----------------------------------------
	.byte	W96
@ 146   ----------------------------------------
	.byte	W96
@ 147   ----------------------------------------
	.byte	W96
@ 148   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_4_084
@ 149   ----------------------------------------
	.byte	W96
@ 150   ----------------------------------------
	.byte	W96
@ 151   ----------------------------------------
	.byte	W96
@ 152   ----------------------------------------
	.byte	W96
@ 153   ----------------------------------------
	.byte	W96
@ 154   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_4_004
@ 155   ----------------------------------------
	.byte		BEND  , c_v+16
	.byte		        c_v+0
	.byte	W96
@ 156   ----------------------------------------
	.byte	W96
@ 157   ----------------------------------------
	.byte	W96
@ 158   ----------------------------------------
	.byte	W96
@ 159   ----------------------------------------
	.byte	W96
@ 160   ----------------------------------------
	.byte	W96
@ 161   ----------------------------------------
	.byte	W96
@ 162   ----------------------------------------
	.byte	W96
@ 163   ----------------------------------------
	.byte	W96
@ 164   ----------------------------------------
	.byte	W96
@ 165   ----------------------------------------
	.byte	W96
@ 166   ----------------------------------------
	.byte	W96
@ 167   ----------------------------------------
	.byte	W96
@ 168   ----------------------------------------
	.byte	W96
@ 169   ----------------------------------------
	.byte	W96
@ 170   ----------------------------------------
	.byte	W96
@ 171   ----------------------------------------
	.byte	W96
@ 172   ----------------------------------------
	.byte	W96
@ 173   ----------------------------------------
	.byte	W96
@ 174   ----------------------------------------
	.byte	W96
@ 175   ----------------------------------------
	.byte	W96
@ 176   ----------------------------------------
	.byte	W96
@ 177   ----------------------------------------
	.byte	W96
@ 178   ----------------------------------------
	.byte	W96
@ 179   ----------------------------------------
	.byte	W96
@ 180   ----------------------------------------
	.byte	W96
@ 181   ----------------------------------------
	.byte	W96
@ 182   ----------------------------------------
	.byte	W36
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		N12   , Gs3 , v096
	.byte	W01
	.byte		BEND  , c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		N18   
	.byte	W01
	.byte		BEND  , c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W05
	.byte		        c_v+11
	.byte	W09
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W24
@ 183   ----------------------------------------
	.byte	W96
@ 184   ----------------------------------------
	.byte	W96
@ 185   ----------------------------------------
	.byte	W96
@ 186   ----------------------------------------
	.byte	W96
@ 187   ----------------------------------------
	.byte	W96
@ 188   ----------------------------------------
	.byte	W96
@ 189   ----------------------------------------
mus_custom_flockofbirds_4_189:
	.byte	W72
	.byte		BEND  , c_v+0
	.byte		N12   , Bn2 , v096
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
@ 190   ----------------------------------------
	.byte	W96
@ 191   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_4_189
@ 192   ----------------------------------------
	.byte	W96
@ 193   ----------------------------------------
	.byte	W96
@ 194   ----------------------------------------
	.byte	W96
@ 195   ----------------------------------------
	.byte	W96
@ 196   ----------------------------------------
	.byte	W96
@ 197   ----------------------------------------
	.byte	W96
@ 198   ----------------------------------------
	.byte	W96
@ 199   ----------------------------------------
	.byte	W96
@ 200   ----------------------------------------
	.byte	W96
@ 201   ----------------------------------------
	.byte	W96
@ 202   ----------------------------------------
	.byte	W96
@ 203   ----------------------------------------
	.byte	W96
@ 204   ----------------------------------------
	.byte	W96
@ 205   ----------------------------------------
	.byte	W96
@ 206   ----------------------------------------
	.byte	W96
@ 207   ----------------------------------------
	.byte	W96
@ 208   ----------------------------------------
	.byte	W96
@ 209   ----------------------------------------
	.byte	W96
@ 210   ----------------------------------------
	.byte	W96
@ 211   ----------------------------------------
	.byte	W96
@ 212   ----------------------------------------
	.byte	W96
@ 213   ----------------------------------------
	.byte	W96
@ 214   ----------------------------------------
	.byte	W96
@ 215   ----------------------------------------
	.byte	W96
@ 216   ----------------------------------------
	.byte	W96
@ 217   ----------------------------------------
	.byte	W96
@ 218   ----------------------------------------
	.byte	W96
@ 219   ----------------------------------------
	.byte	W96
@ 220   ----------------------------------------
	.byte	W96
@ 221   ----------------------------------------
	.byte	W96
@ 222   ----------------------------------------
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		N12   , Bn3 , v127
	.byte	W01
	.byte		BEND  , c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W72
@ 223   ----------------------------------------
	.byte	W96
@ 224   ----------------------------------------
	.byte	W96
@ 225   ----------------------------------------
	.byte	W96
@ 226   ----------------------------------------
	.byte	W96
@ 227   ----------------------------------------
	.byte	W96
@ 228   ----------------------------------------
	.byte	W96
@ 229   ----------------------------------------
	.byte	W96
@ 230   ----------------------------------------
	.byte	W96
@ 231   ----------------------------------------
	.byte	W96
@ 232   ----------------------------------------
	.byte	FINE

@**************** Track 5 (Midi-Chn.5) ****************@

mus_custom_flockofbirds_5:
	.byte	KEYSH , mus_custom_flockofbirds_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 33
	.byte		VOL   , 127*mus_custom_flockofbirds_mvl/mxv
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
mus_custom_flockofbirds_5_005:
	.byte		N12   , En0 , v096
	.byte	W18
	.byte		N06   
	.byte	W18
	.byte		N12   
	.byte	W12
	.byte		        Gs0 
	.byte	W18
	.byte		N06   
	.byte	W18
	.byte		N12   
	.byte	W12
	.byte	PEND
@ 006   ----------------------------------------
	.byte		        Fs0 
	.byte	W18
	.byte		N06   
	.byte	W18
	.byte		N06   
	.byte	W12
	.byte		N24   , Cs1 
	.byte	W24
	.byte		        Ds1 
	.byte	W24
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_005
@ 008   ----------------------------------------
	.byte		N12   , Bn0 , v096
	.byte	W18
	.byte		N06   
	.byte	W18
	.byte		        Fs0 
	.byte	W12
	.byte		N24   , Cs1 
	.byte	W24
	.byte		N06   , Ds1 
	.byte	W12
	.byte		N12   
	.byte	W12
@ 009   ----------------------------------------
mus_custom_flockofbirds_5_009:
	.byte	W06
	.byte		N18   , En1 , v096
	.byte	W18
	.byte		N12   , En0 
	.byte	W12
	.byte		        Gs0 , v112
	.byte	W18
	.byte		N06   , Gs1 
	.byte	W06
	.byte		        Fs1 
	.byte	W06
	.byte		        Ds1 
	.byte	W06
	.byte		        Cs1 
	.byte	W06
	.byte		        Bn0 
	.byte	W06
	.byte		N12   , Fs0 
	.byte	W12
	.byte	PEND
@ 010   ----------------------------------------
mus_custom_flockofbirds_5_010:
	.byte		N24   , Gs0 , v112
	.byte	W30
	.byte		N06   
	.byte	W12
	.byte		N24   , Fs0 
	.byte	W24
	.byte		N12   , Cs1 
	.byte	W18
	.byte		        Ds1 
	.byte	W12
	.byte	PEND
@ 011   ----------------------------------------
mus_custom_flockofbirds_5_011:
	.byte	W06
	.byte		N06   , En1 , v112
	.byte	W06
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte	W06
	.byte		        En0 
	.byte	W18
	.byte		N12   
	.byte	W12
	.byte		N12   
	.byte	W12
	.byte		N06   
	.byte	W06
	.byte		N24   
	.byte	W24
	.byte	PEND
@ 012   ----------------------------------------
	.byte		        Gs0 
	.byte	W36
	.byte		N06   
	.byte	W06
	.byte		N24   , Fs0 
	.byte	W24
	.byte		N06   , Cs1 , v096
	.byte	W12
	.byte		        Ds1 
	.byte	W12
	.byte		N06   
	.byte	W06
@ 013   ----------------------------------------
mus_custom_flockofbirds_5_013:
	.byte	W06
	.byte		N06   , En1 , v096
	.byte	W06
	.byte		N12   , En1 , v112
	.byte	W12
	.byte		        En0 , v096
	.byte	W12
	.byte		        Bn0 , v112
	.byte	W18
	.byte		        Cs1 
	.byte	W18
	.byte		        En1 
	.byte	W12
	.byte		        Ds1 
	.byte	W12
	.byte	PEND
@ 014   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_010
@ 015   ----------------------------------------
	.byte	W06
	.byte		N06   , En1 , v112
	.byte	W06
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte	W06
	.byte		        En0 
	.byte	W18
	.byte		N12   
	.byte	W12
	.byte		N12   
	.byte	W12
	.byte		N06   
	.byte	W06
	.byte		N12   , En1 , v096
	.byte	W12
	.byte		        Ds1 
	.byte	W12
@ 016   ----------------------------------------
mus_custom_flockofbirds_5_016:
	.byte		N24   , Gs0 , v112
	.byte	W36
	.byte		N06   
	.byte	W06
	.byte		N24   , Fs0 
	.byte	W24
	.byte		N06   , Fs0 , v096
	.byte	W12
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte	W06
	.byte	PEND
@ 017   ----------------------------------------
mus_custom_flockofbirds_5_017:
	.byte		N18   , En0 , v096
	.byte	W18
	.byte		N12   
	.byte	W12
	.byte		N12   
	.byte	W24
	.byte		N12   
	.byte	W18
	.byte		N18   
	.byte	W24
	.byte	PEND
@ 018   ----------------------------------------
mus_custom_flockofbirds_5_018:
	.byte		N12   , Ds1 , v096
	.byte	W12
	.byte		N06   
	.byte	W18
	.byte		N06   
	.byte	W12
	.byte		N18   
	.byte	W18
	.byte		N06   
	.byte	W18
	.byte		N06   
	.byte	W12
	.byte		N18   , Gs0 
	.byte	W06
	.byte	PEND
@ 019   ----------------------------------------
mus_custom_flockofbirds_5_019:
	.byte	W12
	.byte		N12   , Gs0 , v096
	.byte	W24
	.byte		N12   
	.byte	W18
	.byte		N18   
	.byte	W18
	.byte		N12   
	.byte	W12
	.byte		N12   
	.byte	W12
	.byte	PEND
@ 020   ----------------------------------------
mus_custom_flockofbirds_5_020:
	.byte		N06   , Fs0 , v096
	.byte	W12
	.byte		N12   
	.byte	W24
	.byte		N06   
	.byte	W06
	.byte		N12   
	.byte	W18
	.byte		N12   
	.byte	W18
	.byte		N12   
	.byte	W18
	.byte	PEND
@ 021   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_017
@ 022   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_018
@ 023   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_019
@ 024   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_020
@ 025   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_017
@ 026   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_018
@ 027   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_019
@ 028   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_020
@ 029   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_017
@ 030   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_018
@ 031   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_019
@ 032   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_020
@ 033   ----------------------------------------
	.byte		N54   , En0 , v096
	.byte	W54
	.byte		N18   , Fs1 
	.byte	W18
	.byte		N12   , Bn0 
	.byte	W12
	.byte		        Cs1 
	.byte	W12
@ 034   ----------------------------------------
	.byte		N84   , Ds1 
	.byte	W90
	.byte		N78   , Gs0 
	.byte	W06
@ 035   ----------------------------------------
	.byte	W72
	.byte		N12   
	.byte	W12
	.byte		        Gn0 
	.byte	W12
@ 036   ----------------------------------------
	.byte		N96   , Fs0 
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
	.byte	W48
	.byte		N24   
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte		        Fn0 
	.byte	W24
@ 050   ----------------------------------------
mus_custom_flockofbirds_5_050:
	.byte		N48   , En1 , v096
	.byte	W48
	.byte		N36   , Ds1 
	.byte	W36
	.byte		N24   , Cs1 
	.byte	W12
	.byte	PEND
@ 051   ----------------------------------------
mus_custom_flockofbirds_5_051:
	.byte	W12
	.byte		N24   , Gs0 , v096
	.byte	W36
	.byte		        Cs1 
	.byte	W24
	.byte		        Ds1 
	.byte	W24
	.byte	PEND
@ 052   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_050
@ 053   ----------------------------------------
mus_custom_flockofbirds_5_053:
	.byte	W12
	.byte		N24   , Gs0 , v096
	.byte	W36
	.byte		        Fs0 
	.byte	W24
	.byte		        Fn0 
	.byte	W24
	.byte	PEND
@ 054   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_050
@ 055   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_051
@ 056   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_050
@ 057   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_053
@ 058   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_050
@ 059   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_051
@ 060   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_050
@ 061   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_053
@ 062   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_050
@ 063   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_051
@ 064   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_050
@ 065   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_053
@ 066   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_009
@ 067   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_010
@ 068   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_011
@ 069   ----------------------------------------
mus_custom_flockofbirds_5_069:
	.byte		N24   , Gs0 , v112
	.byte	W36
	.byte		N06   
	.byte	W06
	.byte		N24   , Fs0 
	.byte	W24
	.byte		N06   , Cs1 
	.byte	W12
	.byte		N18   , Ds1 
	.byte	W18
	.byte	PEND
@ 070   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_013
@ 071   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_010
@ 072   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_011
@ 073   ----------------------------------------
mus_custom_flockofbirds_5_073:
	.byte		N24   , Gs0 , v112
	.byte	W36
	.byte		N06   
	.byte	W06
	.byte		N12   , Fs0 
	.byte	W12
	.byte		N06   , Fs0 , v096
	.byte	W06
	.byte		N06   
	.byte	W12
	.byte		N24   
	.byte	W24
	.byte	PEND
@ 074   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_009
@ 075   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_010
@ 076   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_011
@ 077   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_069
@ 078   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_009
@ 079   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_010
@ 080   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_011
@ 081   ----------------------------------------
	.byte		N24   , Gs0 , v112
	.byte	W36
	.byte		N06   
	.byte	W06
	.byte		N24   , Fs0 
	.byte	W24
	.byte		N06   , Fs0 , v096
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte	W06
@ 082   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_017
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
mus_custom_flockofbirds_5_091:
	.byte		N24   , Fs0 , v096
	.byte	W36
	.byte		N18   , Gs0 
	.byte	W18
	.byte		N24   
	.byte	W30
	.byte		N60   , En0 
	.byte	W12
	.byte	PEND
@ 092   ----------------------------------------
mus_custom_flockofbirds_5_092:
	.byte	W54
	.byte		N18   , En1 , v096
	.byte	W18
	.byte		N24   , Ds1 
	.byte	W24
	.byte	PEND
@ 093   ----------------------------------------
	.byte		        Fs0 
	.byte	W36
	.byte		N18   , Gs0 
	.byte	W18
	.byte		N24   
	.byte	W30
	.byte		N60   , Bn0 
	.byte	W12
@ 094   ----------------------------------------
	.byte	W54
	.byte		N18   , Ds1 
	.byte	W18
	.byte		N24   , En1 
	.byte	W24
@ 095   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_091
@ 096   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_092
@ 097   ----------------------------------------
	.byte		N24   , Fs0 , v096
	.byte	W36
	.byte		N18   , Gs0 
	.byte	W18
	.byte		N24   
	.byte	W30
	.byte		N54   , Bn0 
	.byte	W12
@ 098   ----------------------------------------
	.byte	W42
	.byte		N24   , Cs1 
	.byte	W24
	.byte		N30   , Ds1 
	.byte	W30
@ 099   ----------------------------------------
	.byte		N96   , En0 
	.byte	W96
@ 100   ----------------------------------------
	.byte	W96
@ 101   ----------------------------------------
	.byte	W96
@ 102   ----------------------------------------
	.byte	W96
@ 103   ----------------------------------------
	.byte	W96
@ 104   ----------------------------------------
	.byte	W96
@ 105   ----------------------------------------
	.byte	W96
@ 106   ----------------------------------------
	.byte	W96
@ 107   ----------------------------------------
	.byte	W96
@ 108   ----------------------------------------
	.byte	W96
@ 109   ----------------------------------------
	.byte	W96
@ 110   ----------------------------------------
	.byte	W96
@ 111   ----------------------------------------
	.byte	W96
@ 112   ----------------------------------------
	.byte	W96
@ 113   ----------------------------------------
	.byte	W96
@ 114   ----------------------------------------
	.byte	W96
@ 115   ----------------------------------------
	.byte	W96
@ 116   ----------------------------------------
	.byte	W96
@ 117   ----------------------------------------
	.byte	W96
@ 118   ----------------------------------------
	.byte	W96
@ 119   ----------------------------------------
	.byte	W96
@ 120   ----------------------------------------
	.byte	W96
@ 121   ----------------------------------------
	.byte	W96
@ 122   ----------------------------------------
	.byte	W96
@ 123   ----------------------------------------
	.byte	W96
@ 124   ----------------------------------------
	.byte	W96
@ 125   ----------------------------------------
	.byte	W96
@ 126   ----------------------------------------
	.byte	W96
@ 127   ----------------------------------------
	.byte	W96
@ 128   ----------------------------------------
	.byte	W96
@ 129   ----------------------------------------
	.byte	W96
@ 130   ----------------------------------------
	.byte	W96
@ 131   ----------------------------------------
	.byte	W96
@ 132   ----------------------------------------
	.byte	W96
@ 133   ----------------------------------------
	.byte	W96
@ 134   ----------------------------------------
	.byte	W96
@ 135   ----------------------------------------
	.byte	W96
@ 136   ----------------------------------------
	.byte	W96
@ 137   ----------------------------------------
	.byte	W96
@ 138   ----------------------------------------
	.byte	W96
@ 139   ----------------------------------------
	.byte	W96
@ 140   ----------------------------------------
	.byte	W96
@ 141   ----------------------------------------
	.byte	W96
@ 142   ----------------------------------------
	.byte	W96
@ 143   ----------------------------------------
	.byte	W96
@ 144   ----------------------------------------
	.byte	W96
@ 145   ----------------------------------------
	.byte	W96
@ 146   ----------------------------------------
	.byte	W96
@ 147   ----------------------------------------
	.byte	W96
@ 148   ----------------------------------------
	.byte	W96
@ 149   ----------------------------------------
	.byte	W96
@ 150   ----------------------------------------
	.byte	W96
@ 151   ----------------------------------------
	.byte	W96
@ 152   ----------------------------------------
	.byte	W96
@ 153   ----------------------------------------
	.byte	W96
@ 154   ----------------------------------------
	.byte	W96
@ 155   ----------------------------------------
	.byte	W96
@ 156   ----------------------------------------
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		N12   
	.byte	W18
	.byte		N12   
	.byte	W18
	.byte		N12   
	.byte	W12
	.byte		N12   
	.byte	W12
@ 157   ----------------------------------------
	.byte		N06   , Ds1 
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		N12   
	.byte	W18
	.byte		N12   
	.byte	W18
	.byte		N12   
	.byte	W12
	.byte		N12   
	.byte	W12
@ 158   ----------------------------------------
	.byte		N06   , Gs0 
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		N12   
	.byte	W18
	.byte		N12   
	.byte	W18
	.byte		N12   
	.byte	W12
	.byte		N12   
	.byte	W12
@ 159   ----------------------------------------
	.byte		N06   , Fs0 
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		N12   
	.byte	W18
	.byte		N12   
	.byte	W18
	.byte		N12   
	.byte	W12
	.byte		N12   
	.byte	W12
@ 160   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_009
@ 161   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_010
@ 162   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_011
@ 163   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_069
@ 164   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_013
@ 165   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_010
@ 166   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_011
@ 167   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_073
@ 168   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_009
@ 169   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_010
@ 170   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_011
@ 171   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_069
@ 172   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_009
@ 173   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_010
@ 174   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_011
@ 175   ----------------------------------------
	.byte	W96
@ 176   ----------------------------------------
	.byte	W96
@ 177   ----------------------------------------
	.byte	W96
@ 178   ----------------------------------------
	.byte	W96
@ 179   ----------------------------------------
	.byte	W96
@ 180   ----------------------------------------
	.byte	W96
@ 181   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_069
@ 182   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_013
@ 183   ----------------------------------------
	.byte	W96
@ 184   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_005
@ 185   ----------------------------------------
	.byte	W96
@ 186   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_010
@ 187   ----------------------------------------
	.byte	W96
@ 188   ----------------------------------------
mus_custom_flockofbirds_5_188:
	.byte		N12   , En0 , v096
	.byte	W18
	.byte		N06   
	.byte	W06
	.byte		        Fs1 
	.byte	W06
	.byte		        Gs1 
	.byte	W06
	.byte		N12   , Bn1 
	.byte	W12
	.byte		N18   , Gs0 
	.byte	W18
	.byte		        Gs1 
	.byte	W18
	.byte		N12   , Fs1 
	.byte	W12
	.byte	PEND
@ 189   ----------------------------------------
mus_custom_flockofbirds_5_189:
	.byte		N12   , Fs0 , v096
	.byte	W18
	.byte		N06   
	.byte	W06
	.byte		        Ds1 
	.byte	W06
	.byte		        En1 
	.byte	W06
	.byte		N12   , Cs1 
	.byte	W12
	.byte		N18   , Bn0 
	.byte	W18
	.byte		        Cs1 
	.byte	W18
	.byte		N12   , Bn0 
	.byte	W12
	.byte	PEND
@ 190   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_188
@ 191   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_189
@ 192   ----------------------------------------
	.byte	W96
@ 193   ----------------------------------------
	.byte	W96
@ 194   ----------------------------------------
	.byte	W96
@ 195   ----------------------------------------
	.byte	W96
@ 196   ----------------------------------------
	.byte	W96
@ 197   ----------------------------------------
	.byte	W96
@ 198   ----------------------------------------
	.byte	W96
@ 199   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_5_016
@ 200   ----------------------------------------
	.byte		N96   , En0 , v096
	.byte	W96
@ 201   ----------------------------------------
	.byte	FINE

@**************** Track 6 (Midi-Chn.10) ****************@

mus_custom_flockofbirds_6:
	.byte	KEYSH , mus_custom_flockofbirds_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 0
	.byte		VOL   , 107*mus_custom_flockofbirds_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		BEND  , c_v+0
	.byte	W96
@ 001   ----------------------------------------
mus_custom_flockofbirds_6_001:
	.byte		N06   , As1 , v096
	.byte		N06   
	.byte	W12
	.byte		        Gs1 
	.byte		N06   
	.byte	W18
	.byte		N06   
	.byte		N06   
	.byte	W18
	.byte		N03   
	.byte		N03   
	.byte	W03
	.byte		N02   
	.byte	W03
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W18
	.byte		N06   
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 002   ----------------------------------------
mus_custom_flockofbirds_6_002:
	.byte		N06   , As1 , v096
	.byte		N06   
	.byte	W12
	.byte		        Gs1 
	.byte		N06   
	.byte	W18
	.byte		N06   
	.byte		N06   
	.byte	W18
	.byte		N03   
	.byte		N03   
	.byte	W03
	.byte		N02   
	.byte	W03
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Gn2 
	.byte		N06   
	.byte	W18
	.byte		        An2 
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 003   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_001
@ 004   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_002
@ 005   ----------------------------------------
mus_custom_flockofbirds_6_005:
	.byte		N06   , Cn1 , v096
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W12
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte		N03   , Gs1 
	.byte		N03   
	.byte	W03
	.byte		N02   
	.byte	W03
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W18
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 006   ----------------------------------------
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
	.byte	W12
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte		N03   , Gs1 
	.byte		N03   
	.byte	W03
	.byte		N02   
	.byte	W03
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Gn2 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte	W12
	.byte		        An2 
	.byte		N06   
	.byte	W12
@ 007   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_005
@ 008   ----------------------------------------
	.byte		N06   , Cn1 , v096
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W12
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte		N03   , Gs1 
	.byte		N03   
	.byte	W03
	.byte		N02   
	.byte	W03
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Gn2 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 , v112
	.byte		N06   
	.byte	W12
	.byte		        Cn1 , v096
	.byte		N06   
	.byte		N06   , An2 
	.byte		N06   
	.byte	W12
@ 009   ----------------------------------------
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , An2 
	.byte		N06   
	.byte	W18
	.byte		N12   , Cn1 
	.byte		N12   
	.byte		N12   , Cs2 
	.byte		N12   
	.byte	W12
	.byte		N06   , Cn1 , v112
	.byte		N06   
	.byte	W06
	.byte		        En1 , v096
	.byte		N06   
	.byte	W06
	.byte		        As1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 , v112
	.byte		N06   
	.byte	W06
	.byte		        As1 , v096
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        An1 
	.byte		N06   
	.byte	W06
	.byte		        Gn1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
@ 010   ----------------------------------------
mus_custom_flockofbirds_6_010:
	.byte		N12   , Cn1 , v112
	.byte		N12   
	.byte		N12   , An2 
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
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        As1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte	PEND
@ 011   ----------------------------------------
mus_custom_flockofbirds_6_011:
	.byte	W06
	.byte		N06   , Cn1 , v112
	.byte		N06   
	.byte		N06   , An2 
	.byte		N06   
	.byte	W18
	.byte		N12   , Cn1 , v096
	.byte		N12   
	.byte		N12   , Cs2 
	.byte		N12   
	.byte	W12
	.byte		N06   , Cn1 , v112
	.byte		N06   
	.byte	W06
	.byte		        En1 , v096
	.byte		N06   
	.byte	W06
	.byte		        As1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 , v112
	.byte	W06
	.byte		        En1 , v096
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        An1 
	.byte		N06   
	.byte	W06
	.byte		        Gn1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte	PEND
@ 012   ----------------------------------------
mus_custom_flockofbirds_6_012:
	.byte		N12   , Cn1 , v112
	.byte		N12   
	.byte		N12   , An2 
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
	.byte		N06   , Cn1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        As1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 , v096
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W06
	.byte	PEND
@ 013   ----------------------------------------
mus_custom_flockofbirds_6_013:
	.byte	W06
	.byte		N06   , Cn1 , v096
	.byte		N06   
	.byte		N06   , An2 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 , v112
	.byte		N06   
	.byte		N06   , An2 
	.byte		N06   
	.byte	W12
	.byte		N12   , Cn1 , v096
	.byte		N12   
	.byte		N12   , Cs2 
	.byte		N12   
	.byte	W12
	.byte		N06   , Cn1 , v112
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
	.byte		N06   , As1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 , v096
	.byte		N06   
	.byte		N06   , Gs1 , v112
	.byte		N06   
	.byte	W06
	.byte		        En1 , v096
	.byte		N06   
	.byte	W06
	.byte		        An1 
	.byte		N06   
	.byte	W06
	.byte		        Gn1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte	PEND
@ 014   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_010
@ 015   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_011
@ 016   ----------------------------------------
mus_custom_flockofbirds_6_016:
	.byte		N12   , Cn1 , v112
	.byte		N12   
	.byte		N12   , An2 
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
	.byte		N06   , Cn1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        As1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 , v096
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N05   
	.byte	W06
	.byte		N06   , An1 
	.byte		N06   
	.byte	W06
	.byte	PEND
@ 017   ----------------------------------------
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , As1 
	.byte	W12
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        Cs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        Gs1 
	.byte		N06   
	.byte	W18
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W06
	.byte		        Cs1 
	.byte		N06   
	.byte	W06
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W12
	.byte		        Cs1 , v112
	.byte		N06   
	.byte		N06   , Gn2 , v096
	.byte		N06   
	.byte	W12
@ 018   ----------------------------------------
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cs1 
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W18
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        Cs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        As1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W06
@ 019   ----------------------------------------
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		N04   
	.byte		N04   
	.byte	W04
	.byte		        Cs1 
	.byte	W04
	.byte		N04   
	.byte		N04   
	.byte	W04
	.byte		N06   , Cn1 
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cs1 
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
@ 020   ----------------------------------------
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        Cs1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W18
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        Cs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        As1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
@ 021   ----------------------------------------
mus_custom_flockofbirds_6_021:
	.byte		N06   , Cn1 , v096
	.byte		N06   
	.byte		N06   , As1 
	.byte	W12
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        Gs1 
	.byte		N06   
	.byte	W18
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W12
	.byte		        Gn2 
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 022   ----------------------------------------
mus_custom_flockofbirds_6_022:
	.byte		N06   , Cn1 , v096
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W18
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        As1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W06
	.byte	PEND
@ 023   ----------------------------------------
mus_custom_flockofbirds_6_023:
	.byte	W12
	.byte		N06   , Cn1 , v096
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		N04   
	.byte		N04   
	.byte	W04
	.byte		        Cs1 
	.byte	W04
	.byte		N04   
	.byte		N04   
	.byte	W04
	.byte		N06   , Cn1 
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte	PEND
@ 024   ----------------------------------------
mus_custom_flockofbirds_6_024:
	.byte		N06   , Cn1 , v096
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        En1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W18
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        As1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte	PEND
@ 025   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_021
@ 026   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_022
@ 027   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_023
@ 028   ----------------------------------------
	.byte		N06   , Cn1 , v096
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		        En1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N05   
	.byte	W06
	.byte		N06   , Gs1 , v112
	.byte		N06   
	.byte	W06
	.byte		        Cn1 , v096
	.byte		N06   
	.byte		N06   , En1 , v112
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 , v096
	.byte		N06   
	.byte	W06
	.byte		        En1 , v112
	.byte		N06   
	.byte		N06   , As1 , v096
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
@ 029   ----------------------------------------
	.byte		N06   
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   , As1 , v112
	.byte	W12
	.byte		        Gs1 , v096
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        Gs1 
	.byte		N06   
	.byte	W18
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W12
	.byte		        Gn2 
	.byte		N06   
	.byte	W12
@ 030   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_022
@ 031   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_023
@ 032   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_024
@ 033   ----------------------------------------
	.byte		N06   , Cn1 , v096
	.byte		N06   
	.byte		N06   , An2 
	.byte		N06   
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
	.byte	W60
	.byte		        Fs1 , v016
	.byte	W06
	.byte		        Fs1 , v032
	.byte	W06
	.byte		N12   , As1 , v048
	.byte	W12
	.byte		N06   , Fs1 , v064
	.byte	W06
	.byte		N06   
	.byte	W06
@ 050   ----------------------------------------
mus_custom_flockofbirds_6_050:
	.byte		N12   , Cn1 , v064
	.byte		N12   , Cn1 , v096
	.byte		N12   , Gn2 
	.byte	W12
	.byte		        En0 
	.byte	W24
	.byte		N12   
	.byte	W12
	.byte		N06   , Cn1 
	.byte		N06   
	.byte	W06
	.byte		        Fn0 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En0 
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 051   ----------------------------------------
mus_custom_flockofbirds_6_051:
	.byte		N06   , Ds0 , v096
	.byte	W06
	.byte		N06   
	.byte	W06
	.byte		N12   , Cn1 
	.byte		N12   
	.byte	W12
	.byte		N06   , Ds0 
	.byte	W06
	.byte		        Fn0 
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		N12   , Cn1 
	.byte		N12   
	.byte	W12
	.byte		N12   
	.byte		N12   
	.byte	W12
	.byte		N06   , En0 
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En0 
	.byte	W06
	.byte		N06   
	.byte	W06
	.byte	PEND
@ 052   ----------------------------------------
mus_custom_flockofbirds_6_052:
	.byte		N12   , Cn1 , v064
	.byte		N12   , Cn1 , v096
	.byte	W12
	.byte		        En0 
	.byte	W24
	.byte		N12   
	.byte	W12
	.byte		N06   , Cn1 
	.byte		N06   
	.byte	W06
	.byte		        Fn0 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En0 
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 053   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_051
@ 054   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_050
@ 055   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_051
@ 056   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_052
@ 057   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_051
@ 058   ----------------------------------------
	.byte		N12   , Cn1 , v064
	.byte		N12   , Cn1 , v096
	.byte		N12   , Gn2 
	.byte	W12
	.byte		        En0 
	.byte	W24
	.byte		N12   
	.byte	W12
	.byte		N06   , Cn1 
	.byte		N06   
	.byte	W12
	.byte		        En0 
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En0 
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
@ 059   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_051
@ 060   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_052
@ 061   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_051
@ 062   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_050
@ 063   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_051
@ 064   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_052
@ 065   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_051
@ 066   ----------------------------------------
mus_custom_flockofbirds_6_066:
	.byte		N06   , An1 , v096
	.byte		N05   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		N12   , Cn1 
	.byte		N12   
	.byte		N12   , Cs2 
	.byte		N12   
	.byte	W12
	.byte		N06   , Cn1 , v112
	.byte		N06   
	.byte	W06
	.byte		        En1 , v096
	.byte		N06   
	.byte	W06
	.byte		        As1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 , v112
	.byte		N06   
	.byte	W06
	.byte		        As1 , v096
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        An1 
	.byte		N06   
	.byte	W06
	.byte		        Gn1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte	PEND
@ 067   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_010
@ 068   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_011
@ 069   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_012
@ 070   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_013
@ 071   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_010
@ 072   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_011
@ 073   ----------------------------------------
mus_custom_flockofbirds_6_073:
	.byte		N12   , Cn1 , v112
	.byte		N12   
	.byte		N12   , An2 
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
	.byte		N06   , Cn1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        As1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 , v096
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte		N06   , Cs2 
	.byte		N06   
	.byte	W12
	.byte		        En1 
	.byte		N05   
	.byte	W06
	.byte		N06   , An1 
	.byte		N06   
	.byte	W06
	.byte	PEND
@ 074   ----------------------------------------
mus_custom_flockofbirds_6_074:
	.byte		N06   , En1 , v096
	.byte		N05   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		N12   , Cn1 
	.byte		N12   
	.byte	W12
	.byte		N06   , Cn1 , v112
	.byte		N06   
	.byte	W18
	.byte		        Cn1 , v096
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        An1 
	.byte		N06   
	.byte	W06
	.byte		        Gn1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte	PEND
@ 075   ----------------------------------------
mus_custom_flockofbirds_6_075:
	.byte		N12   , Cn1 , v112
	.byte		N12   
	.byte		N12   , Cs2 , v096
	.byte		N12   
	.byte	W12
	.byte		N06   , Cn1 , v112
	.byte		N06   
	.byte		N06   , As1 , v096
	.byte		N06   
	.byte	W06
	.byte		N03   , En1 
	.byte	W03
	.byte		N03   
	.byte		N03   
	.byte	W03
	.byte		N06   
	.byte		N06   
	.byte		N06   , An2 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 , v112
	.byte		N06   
	.byte	W06
	.byte		        As1 , v096
	.byte		N06   
	.byte	W06
	.byte		        Cn1 , v112
	.byte		N06   
	.byte	W06
	.byte		        As1 , v096
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 , v112
	.byte		N06   
	.byte		N06   , An2 , v096
	.byte		N06   
	.byte	W18
	.byte		        Cn1 , v112
	.byte		N06   
	.byte		N06   , Gn2 , v096
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 076   ----------------------------------------
mus_custom_flockofbirds_6_076:
	.byte	W06
	.byte		N06   , Cn1 , v112
	.byte		N06   
	.byte		N06   , An2 
	.byte		N06   
	.byte	W12
	.byte		        En1 , v096
	.byte		N06   
	.byte	W06
	.byte		N12   , Cn1 
	.byte		N12   
	.byte		N12   , Cs2 
	.byte		N12   
	.byte	W12
	.byte		N06   , Cn1 , v112
	.byte		N06   
	.byte	W06
	.byte		        En1 , v096
	.byte		N06   
	.byte	W06
	.byte		        As1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 , v112
	.byte	W06
	.byte		        En1 , v096
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        An1 
	.byte		N06   
	.byte	W06
	.byte		        Gn1 
	.byte		N06   
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte	PEND
@ 077   ----------------------------------------
mus_custom_flockofbirds_6_077:
	.byte		N12   , Cn1 , v112
	.byte		N12   
	.byte		N12   , An2 
	.byte		N12   
	.byte	W12
	.byte		        Cn1 
	.byte		N12   
	.byte		N12   , As1 , v096
	.byte		N12   
	.byte	W12
	.byte		        En1 , v112
	.byte		N12   
	.byte		N12   , As1 
	.byte		N12   
	.byte	W12
	.byte		N06   , Cn1 
	.byte		N06   
	.byte		N06   , As1 , v096
	.byte		N06   
	.byte	W06
	.byte		        Cn1 , v112
	.byte		N06   
	.byte	W06
	.byte		        As1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte		N06   , As1 , v096
	.byte		N06   
	.byte	W06
	.byte		        Cn1 , v112
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 , v096
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W06
	.byte	PEND
@ 078   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_074
@ 079   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_010
@ 080   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_076
@ 081   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_077
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
	.byte	W96
@ 094   ----------------------------------------
	.byte	W96
@ 095   ----------------------------------------
	.byte	W96
@ 096   ----------------------------------------
	.byte	W96
@ 097   ----------------------------------------
	.byte	W96
@ 098   ----------------------------------------
	.byte	W96
@ 099   ----------------------------------------
	.byte	W96
@ 100   ----------------------------------------
	.byte	W96
@ 101   ----------------------------------------
	.byte	W96
@ 102   ----------------------------------------
	.byte	W96
@ 103   ----------------------------------------
	.byte	W96
@ 104   ----------------------------------------
	.byte	W96
@ 105   ----------------------------------------
	.byte	W96
@ 106   ----------------------------------------
	.byte	W96
@ 107   ----------------------------------------
	.byte	W96
@ 108   ----------------------------------------
	.byte	W96
@ 109   ----------------------------------------
	.byte	W96
@ 110   ----------------------------------------
	.byte	W96
@ 111   ----------------------------------------
	.byte	W96
@ 112   ----------------------------------------
	.byte	W96
@ 113   ----------------------------------------
	.byte	W96
@ 114   ----------------------------------------
	.byte	W96
@ 115   ----------------------------------------
	.byte	W96
@ 116   ----------------------------------------
	.byte	W96
@ 117   ----------------------------------------
	.byte	W96
@ 118   ----------------------------------------
	.byte	W96
@ 119   ----------------------------------------
	.byte	W96
@ 120   ----------------------------------------
	.byte	W96
@ 121   ----------------------------------------
	.byte	W96
@ 122   ----------------------------------------
	.byte	W96
@ 123   ----------------------------------------
	.byte	W96
@ 124   ----------------------------------------
	.byte	W96
@ 125   ----------------------------------------
	.byte	W96
@ 126   ----------------------------------------
	.byte	W96
@ 127   ----------------------------------------
	.byte	W96
@ 128   ----------------------------------------
	.byte	W96
@ 129   ----------------------------------------
	.byte	W96
@ 130   ----------------------------------------
	.byte	W96
@ 131   ----------------------------------------
	.byte	W96
@ 132   ----------------------------------------
	.byte	W96
@ 133   ----------------------------------------
	.byte	W96
@ 134   ----------------------------------------
	.byte	W96
@ 135   ----------------------------------------
	.byte	W96
@ 136   ----------------------------------------
	.byte	W96
@ 137   ----------------------------------------
	.byte	W96
@ 138   ----------------------------------------
	.byte	W96
@ 139   ----------------------------------------
	.byte	W96
@ 140   ----------------------------------------
	.byte	W96
@ 141   ----------------------------------------
	.byte	W96
@ 142   ----------------------------------------
	.byte	W96
@ 143   ----------------------------------------
	.byte	W96
@ 144   ----------------------------------------
	.byte	W96
@ 145   ----------------------------------------
	.byte	W96
@ 146   ----------------------------------------
	.byte	W96
@ 147   ----------------------------------------
	.byte	W96
@ 148   ----------------------------------------
	.byte	W96
@ 149   ----------------------------------------
	.byte	W96
@ 150   ----------------------------------------
	.byte	W96
@ 151   ----------------------------------------
	.byte	W96
@ 152   ----------------------------------------
	.byte	W96
@ 153   ----------------------------------------
	.byte	W96
@ 154   ----------------------------------------
	.byte	W96
@ 155   ----------------------------------------
	.byte	W96
@ 156   ----------------------------------------
mus_custom_flockofbirds_6_156:
	.byte		N06   , Cn1 , v096
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		N03   , An1 
	.byte		N03   
	.byte	W03
	.byte		N03   
	.byte		N03   
	.byte	W03
	.byte		        Cn1 
	.byte		N03   
	.byte	W06
	.byte		        An1 
	.byte		N03   
	.byte	W03
	.byte		N03   
	.byte		N03   
	.byte	W03
	.byte		        Cn1 
	.byte		N03   
	.byte	W06
	.byte		        An1 
	.byte		N03   
	.byte	W06
	.byte		N03   
	.byte		N03   
	.byte	W03
	.byte		N03   
	.byte		N03   
	.byte	W03
	.byte		N06   , Cn1 
	.byte		N06   
	.byte	W12
	.byte		N03   , An1 
	.byte		N03   
	.byte	W03
	.byte		N03   
	.byte		N03   
	.byte	W03
	.byte		N06   , Cn1 
	.byte		N06   
	.byte	W06
	.byte		N03   , An1 
	.byte		N03   
	.byte	W03
	.byte		N03   
	.byte		N03   
	.byte	W09
	.byte		N03   
	.byte		N03   
	.byte	W03
	.byte		N03   
	.byte		N03   
	.byte	W03
	.byte	PEND
@ 157   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_156
@ 158   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_156
@ 159   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_156
@ 160   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_066
@ 161   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_010
@ 162   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_011
@ 163   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_012
@ 164   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_013
@ 165   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_010
@ 166   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_011
@ 167   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_073
@ 168   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_074
@ 169   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_075
@ 170   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_076
@ 171   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_077
@ 172   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_074
@ 173   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_010
@ 174   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_076
@ 175   ----------------------------------------
	.byte	W96
@ 176   ----------------------------------------
	.byte	W96
@ 177   ----------------------------------------
	.byte	W96
@ 178   ----------------------------------------
	.byte	W96
@ 179   ----------------------------------------
	.byte	W96
@ 180   ----------------------------------------
	.byte	W96
@ 181   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_012
@ 182   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_013
@ 183   ----------------------------------------
	.byte	W96
@ 184   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_005
@ 185   ----------------------------------------
	.byte	W96
@ 186   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_010
@ 187   ----------------------------------------
	.byte	W96
@ 188   ----------------------------------------
	.byte		N06   , Cn1 , v096
	.byte		N06   
	.byte		N06   , Ds2 
	.byte		N06   
	.byte	W18
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte		N06   , Ds2 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte		N06   , Ds2 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Ds2 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte	W06
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W12
@ 189   ----------------------------------------
mus_custom_flockofbirds_6_189:
	.byte		N06   , Cn1 , v096
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W12
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W12
	.byte		        Ds2 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		        Ds2 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Ds2 
	.byte		N06   
	.byte	W12
	.byte		        An2 
	.byte		N06   
	.byte	W12
	.byte	PEND
@ 190   ----------------------------------------
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Ds2 
	.byte		N06   
	.byte	W18
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte		N06   , Ds2 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte		N06   , Ds2 
	.byte		N06   
	.byte	W06
	.byte		        En1 , v080
	.byte	W12
	.byte		        Cn1 , v096
	.byte		N06   
	.byte		N06   , Ds2 
	.byte		N06   
	.byte	W06
	.byte		        En1 , v080
	.byte	W06
	.byte		N06   
	.byte	W06
	.byte		        Cn1 , v096
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W12
@ 191   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_189
@ 192   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_021
@ 193   ----------------------------------------
	.byte		N06   , Cn1 , v096
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , En2 
	.byte		N06   
	.byte	W12
	.byte		        Cs2 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W12
	.byte		        Ds2 
	.byte		N06   
	.byte	W12
@ 194   ----------------------------------------
	.byte	W06
	.byte		N06   
	.byte		N06   
	.byte	W18
	.byte		N06   
	.byte		N06   
	.byte	W72
@ 195   ----------------------------------------
	.byte	W96
@ 196   ----------------------------------------
	.byte	W96
@ 197   ----------------------------------------
	.byte	W96
@ 198   ----------------------------------------
	.byte	W96
@ 199   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_016
@ 200   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_6_021
@ 201   ----------------------------------------
	.byte		N06   , Cn1 , v096
	.byte		N06   
	.byte		N06   , Gs1 
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        Gs1 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , Gn2 
	.byte		N06   
	.byte	W12
	.byte		        Cn1 
	.byte		N06   
	.byte	W06
	.byte		        En2 
	.byte		N06   
	.byte	W06
	.byte		        Cs2 
	.byte		N06   
	.byte	W06
	.byte		        Cn1 
	.byte		N06   
	.byte		N06   , As1 
	.byte		N06   
	.byte	W12
	.byte		        Ds2 
	.byte		N06   
	.byte	W06
	.byte	FINE

@**************** Track 7 (Midi-Chn.7) ****************@

mus_custom_flockofbirds_7:
	.byte	KEYSH , mus_custom_flockofbirds_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 119
	.byte		VOL   , 127*mus_custom_flockofbirds_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		BEND  , c_v+0
	.byte	W42
	.byte		N66   , Fn3 , v096
	.byte		N66   , Gs3 
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
@ 001   ----------------------------------------
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W84
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
mus_custom_flockofbirds_7_036:
	.byte	W42
	.byte		N54   , Fn3 , v096
	.byte		N54   , Gs3 
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	PEND
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
	.byte	W96
@ 061   ----------------------------------------
	.byte	W96
@ 062   ----------------------------------------
	.byte	W96
@ 063   ----------------------------------------
	.byte	W96
@ 064   ----------------------------------------
	.byte	W96
@ 065   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_7_036
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
	.byte	W96
@ 094   ----------------------------------------
	.byte	W96
@ 095   ----------------------------------------
	.byte	W96
@ 096   ----------------------------------------
	.byte	W96
@ 097   ----------------------------------------
	.byte	W96
@ 098   ----------------------------------------
	.byte	W96
@ 099   ----------------------------------------
	.byte	W96
@ 100   ----------------------------------------
	.byte	W96
@ 101   ----------------------------------------
	.byte	W96
@ 102   ----------------------------------------
	.byte	W96
@ 103   ----------------------------------------
	.byte	W96
@ 104   ----------------------------------------
	.byte	W96
@ 105   ----------------------------------------
	.byte	W96
@ 106   ----------------------------------------
	.byte	W96
@ 107   ----------------------------------------
	.byte	W96
@ 108   ----------------------------------------
	.byte	W96
@ 109   ----------------------------------------
	.byte	W96
@ 110   ----------------------------------------
	.byte	W96
@ 111   ----------------------------------------
	.byte	W96
@ 112   ----------------------------------------
	.byte	W96
@ 113   ----------------------------------------
	.byte	W96
@ 114   ----------------------------------------
	.byte	W96
@ 115   ----------------------------------------
	.byte	W96
@ 116   ----------------------------------------
	.byte	W96
@ 117   ----------------------------------------
	.byte	W96
@ 118   ----------------------------------------
	.byte	W96
@ 119   ----------------------------------------
	.byte	W96
@ 120   ----------------------------------------
	.byte	W96
@ 121   ----------------------------------------
	.byte	W96
@ 122   ----------------------------------------
	.byte	W96
@ 123   ----------------------------------------
	.byte	W96
@ 124   ----------------------------------------
	.byte	W96
@ 125   ----------------------------------------
	.byte	W96
@ 126   ----------------------------------------
	.byte	W96
@ 127   ----------------------------------------
	.byte	W96
@ 128   ----------------------------------------
	.byte	W96
@ 129   ----------------------------------------
	.byte	W96
@ 130   ----------------------------------------
	.byte	W96
@ 131   ----------------------------------------
	.byte	W96
@ 132   ----------------------------------------
	.byte	W96
@ 133   ----------------------------------------
	.byte	W96
@ 134   ----------------------------------------
	.byte	W96
@ 135   ----------------------------------------
	.byte	W96
@ 136   ----------------------------------------
	.byte	W96
@ 137   ----------------------------------------
	.byte	W96
@ 138   ----------------------------------------
	.byte	W96
@ 139   ----------------------------------------
	.byte	W96
@ 140   ----------------------------------------
	.byte	W96
@ 141   ----------------------------------------
	.byte	W96
@ 142   ----------------------------------------
	.byte	W96
@ 143   ----------------------------------------
	.byte	W96
@ 144   ----------------------------------------
	.byte	W96
@ 145   ----------------------------------------
	.byte	W96
@ 146   ----------------------------------------
	.byte	W96
@ 147   ----------------------------------------
	.byte	W96
@ 148   ----------------------------------------
	.byte	W96
@ 149   ----------------------------------------
	.byte	W96
@ 150   ----------------------------------------
	.byte	W96
@ 151   ----------------------------------------
	.byte	W96
@ 152   ----------------------------------------
	.byte	W96
@ 153   ----------------------------------------
	.byte	W96
@ 154   ----------------------------------------
	.byte	W96
@ 155   ----------------------------------------
	.byte	W96
@ 156   ----------------------------------------
	.byte	W96
@ 157   ----------------------------------------
	.byte	W96
@ 158   ----------------------------------------
	.byte	W96
@ 159   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_7_036
@ 160   ----------------------------------------
	.byte	FINE

@**************** Track 8 (Midi-Chn.9) ****************@

mus_custom_flockofbirds_8:
	.byte	KEYSH , mus_custom_flockofbirds_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 29
	.byte		VOL   , 95*mus_custom_flockofbirds_mvl/mxv
	.byte		PAN   , c_v+41
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
mus_custom_flockofbirds_8_016:
	.byte	W72
	.byte		N06   , Bn2 , v048
	.byte	W06
	.byte		        Cs3 , v064
	.byte	W06
	.byte		        Ds3 , v080
	.byte	W06
	.byte		        Fs3 , v096
	.byte	W06
	.byte	PEND
@ 017   ----------------------------------------
	.byte		N12   , Ds3 
	.byte	W54
	.byte		N03   , Cs3 
	.byte	W03
	.byte		        Dn3 
	.byte	W03
	.byte		N06   , Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		N06   
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
@ 018   ----------------------------------------
	.byte		        Bn2 
	.byte	W06
	.byte		        Gs2 
	.byte	W48
	.byte		N02   
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		N06   , Ds3 
	.byte	W24
@ 019   ----------------------------------------
	.byte	W12
	.byte		        As3 
	.byte	W06
	.byte		N12   , Fs3 
	.byte	W42
	.byte		N06   , As3 
	.byte	W06
	.byte		        Fs3 
	.byte	W24
	.byte		        Bn2 
	.byte	W06
@ 020   ----------------------------------------
	.byte		N24   , Cs3 
	.byte	W60
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		        Ds4 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		        Bn3 
	.byte	W06
	.byte		        Cs4 
	.byte	W06
@ 021   ----------------------------------------
	.byte		N03   , Dn4 
	.byte	W03
	.byte		        Cs4 
	.byte	W03
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        Cs4 
	.byte	W24
	.byte		        Fs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Dn3 
	.byte	W06
	.byte		N06   
	.byte	W06
	.byte		        Cs3 
	.byte	W12
	.byte		        Bn2 
	.byte	W12
	.byte		N12   , Gs2 
	.byte	W12
@ 022   ----------------------------------------
	.byte	W12
	.byte		N06   , Ds3 
	.byte	W06
	.byte		        Bn2 
	.byte	W12
	.byte		        As2 
	.byte	W06
	.byte		N12   , Fs2 
	.byte	W18
	.byte		N06   , As2 
	.byte	W12
	.byte		        Bn2 
	.byte	W06
	.byte		N08   , Cs3 
	.byte	W08
	.byte		        Ds3 
	.byte	W08
	.byte		        Cs3 
	.byte	W08
@ 023   ----------------------------------------
	.byte		N18   , Fs3 
	.byte	W18
	.byte		N06   , Ds3 
	.byte	W36
	.byte		N12   , Fs3 
	.byte	W12
	.byte		N06   , Cs3 
	.byte	W06
	.byte		        As2 
	.byte	W06
	.byte		        Bn2 
	.byte	W12
	.byte		        Cs3 
	.byte	W06
@ 024   ----------------------------------------
	.byte		        Ds3 
	.byte	W12
	.byte		        Fs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		N03   , Gn3 
	.byte	W03
	.byte		        Gs3 
	.byte	W03
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Fs3 
	.byte	W24
	.byte		        Cs3 
	.byte	W06
	.byte		N04   , Ds3 
	.byte	W04
	.byte		        Fs3 
	.byte	W04
	.byte		        Gs3 
	.byte	W04
	.byte		        Cs4 
	.byte	W04
	.byte		        Ds4 
	.byte	W04
	.byte		        Bn3 
	.byte	W04
@ 025   ----------------------------------------
	.byte		N36   , As3 
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
	.byte	W48
	.byte		N12   , Fs4 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		N06   , As3 
	.byte	W06
	.byte		        Gn4 
	.byte	W06
	.byte		        Gs4 
	.byte	W06
	.byte		        En4 
	.byte	W06
	.byte		        Ds4 
	.byte	W06
	.byte		        Bn3 
	.byte	W06
@ 033   ----------------------------------------
	.byte		N96   , Bn3 , v032
	.byte		N96   , Cs4 , v096
	.byte		N96   , Bn4 
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
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
	.byte		N72   , Ds3 
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
	.byte	W12
	.byte		N48   , Gs2 
	.byte	W06
	.byte		N42   , Bn2 
	.byte	W06
@ 050   ----------------------------------------
	.byte		N36   , Ds3 
	.byte	W18
	.byte		N18   , Gs3 
	.byte	W48
	.byte		N06   , Cs2 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		        Bn2 
	.byte	W18
@ 051   ----------------------------------------
	.byte		N12   , Gs2 
	.byte	W12
	.byte		N06   , Bn2 
	.byte	W06
	.byte		N01   
	.byte	W06
	.byte		N01   
	.byte	W06
	.byte		N12   
	.byte	W12
	.byte		N01   
	.byte	W06
	.byte		N01   
	.byte	W06
	.byte		N06   
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		        Fs2 
	.byte	W18
@ 052   ----------------------------------------
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N36   , As2 
	.byte	W12
	.byte		N24   , Bn2 
	.byte	W12
	.byte		N36   , Fs3 
	.byte	W24
	.byte		N24   , Bn2 
	.byte	W12
	.byte		N12   , As2 
	.byte	W12
	.byte		        Gs2 
	.byte	W06
@ 053   ----------------------------------------
	.byte	W12
	.byte		N01   
	.byte	W06
	.byte		N06   
	.byte	W18
	.byte		N06   
	.byte	W06
	.byte		        En2 
	.byte	W06
	.byte		N03   , Fs2 
	.byte	W03
	.byte		        Gs2 
	.byte	W03
	.byte		N06   , Bn2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		N03   , Dn3 
	.byte	W03
	.byte		        Cs3 
	.byte	W03
	.byte		N06   , Bn2 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
@ 054   ----------------------------------------
	.byte		N12   , Gs3 
	.byte	W18
	.byte		N06   , An3 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Bn3 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W18
	.byte		        Bn2 
	.byte	W06
	.byte		N04   , As2 
	.byte	W04
	.byte		        Bn2 
	.byte	W04
	.byte		        Cs3 
	.byte	W04
	.byte		N06   , Ds3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
@ 055   ----------------------------------------
	.byte		        Ds3 
	.byte	W06
	.byte		N01   , Gn2 
	.byte	W03
	.byte		N01   
	.byte	W03
	.byte		N06   , Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		N12   , As2 
	.byte	W12
	.byte		N01   , Gn2 
	.byte	W06
	.byte		N06   , Bn2 
	.byte	W06
	.byte		N01   
	.byte	W06
	.byte		N06   
	.byte	W06
	.byte		N01   , Gn2 
	.byte	W06
	.byte		N01   
	.byte	W06
	.byte		N04   , As2 
	.byte	W04
	.byte		        Bn2 
	.byte	W04
	.byte		        Cs3 
	.byte	W04
	.byte		        Ds3 
	.byte	W04
	.byte		        Fs3 
	.byte	W04
	.byte		        Gs3 
	.byte	W04
@ 056   ----------------------------------------
	.byte		N12   , As3 
	.byte	W30
	.byte		N03   , An3 
	.byte	W03
	.byte		        Gs3 
	.byte	W03
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Bn2 
	.byte	W12
	.byte		        Ds3 
	.byte	W06
	.byte		N12   , As2 
	.byte	W12
@ 057   ----------------------------------------
	.byte		N06   , Fs2 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		N06   
	.byte	W48
	.byte		        Cs2 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		        Bn2 
	.byte	W18
@ 058   ----------------------------------------
	.byte		N12   , Gs3 
	.byte	W36
	.byte		N06   , Cs4 
	.byte	W06
	.byte		N18   , As3 
	.byte	W36
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
@ 059   ----------------------------------------
	.byte	W12
	.byte		N12   , Gs2 
	.byte	W24
	.byte		N06   
	.byte	W06
	.byte		        Fs2 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		N06   
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		        Bn3 
	.byte	W06
@ 060   ----------------------------------------
	.byte		        Gs3 
	.byte	W06
	.byte		        Bn3 
	.byte	W06
	.byte		        Cs4 
	.byte	W06
	.byte		N12   , Gs3 
	.byte	W12
	.byte		N06   , Cs4 
	.byte	W06
	.byte		        Dn4 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		        Ds4 
	.byte	W06
	.byte		N03   , En4 
	.byte	W03
	.byte		        Ds4 
	.byte	W03
	.byte		N06   , Cs4 
	.byte	W06
	.byte		        Bn3 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		        Gn3 
	.byte	W06
	.byte		        En3 
	.byte	W06
@ 061   ----------------------------------------
	.byte		        Ds3 , v080
	.byte	W06
	.byte		        Fs3 , v112
	.byte	W06
	.byte		N01   , Bn2 , v096
	.byte	W06
	.byte		N01   
	.byte	W06
	.byte		N06   , Ds3 
	.byte	W12
	.byte		N03   
	.byte	W03
	.byte		        En3 
	.byte	W03
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N03   
	.byte	W03
	.byte		        Fs3 
	.byte	W03
	.byte		N12   , Ds3 
	.byte	W12
	.byte		N06   , Gs2 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
@ 062   ----------------------------------------
	.byte		        Dn3 
	.byte	W06
	.byte		N02   , Gs2 
	.byte	W06
	.byte		N06   , Ds3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N02   , Gs2 
	.byte	W06
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		N12   , Ds3 
	.byte	W12
	.byte		N03   , En3 
	.byte	W03
	.byte		        Ds3 
	.byte	W03
	.byte		N06   , Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
@ 063   ----------------------------------------
	.byte		        Gs3 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		N04   , Bn3 
	.byte	W04
	.byte		        As3 
	.byte	W04
	.byte		        Gn3 
	.byte	W16
	.byte		N06   , Ds3 
	.byte	W06
	.byte		        Bn2 
	.byte	W12
	.byte		        Gs2 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Dn3 
	.byte	W06
	.byte		        Ds3 
	.byte	W18
@ 064   ----------------------------------------
	.byte		N18   
	.byte	W18
	.byte		        Bn3 
	.byte	W42
	.byte		        Gs3 
	.byte	W30
	.byte		TIE   , Bn2 
	.byte	W06
@ 065   ----------------------------------------
	.byte		N96   , As2 
	.byte		N96   , Gs3 
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte		EOT   , Bn2 
@ 066   ----------------------------------------
mus_custom_flockofbirds_8_066:
	.byte	W06
	.byte		N06   , Fs2 , v096
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        Fs2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        Fs2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		N12   , En1 , v112
	.byte	W24
	.byte		N01   , Gs3 , v096
	.byte	W24
	.byte		N12   , Fs3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte	PEND
@ 067   ----------------------------------------
mus_custom_flockofbirds_8_067:
	.byte		N12   , Gs2 , v112
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N06   , Gs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		N24   , Cs3 
	.byte	W24
	.byte		N03   , Ds4 
	.byte	W03
	.byte		        Cs4 
	.byte	W03
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte	PEND
@ 068   ----------------------------------------
mus_custom_flockofbirds_8_068:
	.byte	W06
	.byte		N18   , Fs2 , v112
	.byte		N18   , Fs3 
	.byte	W18
	.byte		N12   , En1 
	.byte	W24
	.byte		N01   , Gs3 , v096
	.byte	W24
	.byte		N12   , Fs3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte	PEND
@ 069   ----------------------------------------
mus_custom_flockofbirds_8_069:
	.byte		N12   , Gs2 , v112
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N06   , Gs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		N24   , Cs3 
	.byte	W54
	.byte	PEND
@ 070   ----------------------------------------
mus_custom_flockofbirds_8_070:
	.byte	W06
	.byte		N06   , En2 , v112
	.byte		N06   , Bn2 
	.byte	W06
	.byte		N12   , En2 
	.byte		N12   , Bn2 
	.byte	W12
	.byte		        En1 
	.byte	W24
	.byte		N01   , Gs3 , v096
	.byte	W24
	.byte		N12   , En2 
	.byte		N12   , Fs3 , v112
	.byte	W12
	.byte		        Ds2 , v096
	.byte		N12   , En3 , v112
	.byte	W12
	.byte	PEND
@ 071   ----------------------------------------
mus_custom_flockofbirds_8_071:
	.byte		N12   , Gs2 , v112
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N06   , Gs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		N24   , Cs3 
	.byte	W24
	.byte		N12   , Cs2 
	.byte		N12   , Gs2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		        En3 
	.byte	W12
	.byte	PEND
@ 072   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_068
@ 073   ----------------------------------------
mus_custom_flockofbirds_8_073:
	.byte		N12   , Gs2 , v112
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N06   , Gs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		N24   , Cs3 
	.byte	W30
	.byte		N06   , Bn2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 , v096
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte	PEND
@ 074   ----------------------------------------
mus_custom_flockofbirds_8_074:
	.byte	W06
	.byte		N06   , Fs2 , v096
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        Fs2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        Fs2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		N12   , En1 , v112
	.byte	W12
	.byte		        En4 , v096
	.byte	W12
	.byte		N01   , Gs3 
	.byte	W06
	.byte		N18   , Ds4 
	.byte	W30
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte	PEND
@ 075   ----------------------------------------
mus_custom_flockofbirds_8_075:
	.byte		N06   , Gs3 , v096
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Gs3 , v112
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		N24   , Cs3 
	.byte	W24
	.byte		N03   , Ds4 
	.byte	W03
	.byte		        Cs4 
	.byte	W03
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Fs3 
	.byte	W12
	.byte	PEND
@ 076   ----------------------------------------
mus_custom_flockofbirds_8_076:
	.byte	W06
	.byte		N12   , Fs2 , v112
	.byte	W12
	.byte		N06   , Gs2 , v096
	.byte	W06
	.byte		N12   , En1 , v112
	.byte	W24
	.byte		N01   , Gs3 , v096
	.byte	W24
	.byte		N12   , Fs3 
	.byte	W12
	.byte		        En3 
	.byte	W12
	.byte	PEND
@ 077   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_069
@ 078   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_074
@ 079   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_071
@ 080   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_076
@ 081   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_069
@ 082   ----------------------------------------
	.byte		N12   , Ds3 , v096
	.byte	W84
	.byte		TIE   , Bn2 
	.byte		TIE   , Fs3 
	.byte		TIE   , Bn3 
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
@ 083   ----------------------------------------
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte		EOT   , Bn2 
	.byte		        Fs3 
	.byte		        Bn3 
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
	.byte	W96
@ 094   ----------------------------------------
	.byte	W96
@ 095   ----------------------------------------
	.byte	W96
@ 096   ----------------------------------------
	.byte	W96
@ 097   ----------------------------------------
	.byte	W96
@ 098   ----------------------------------------
	.byte	W96
@ 099   ----------------------------------------
	.byte	W96
@ 100   ----------------------------------------
	.byte	W96
@ 101   ----------------------------------------
	.byte	W96
@ 102   ----------------------------------------
	.byte	W96
@ 103   ----------------------------------------
	.byte	W96
@ 104   ----------------------------------------
	.byte	W96
@ 105   ----------------------------------------
	.byte	W96
@ 106   ----------------------------------------
	.byte	W96
@ 107   ----------------------------------------
	.byte	W96
@ 108   ----------------------------------------
	.byte	W96
@ 109   ----------------------------------------
	.byte	W96
@ 110   ----------------------------------------
	.byte	W96
@ 111   ----------------------------------------
	.byte	W96
@ 112   ----------------------------------------
	.byte	W96
@ 113   ----------------------------------------
	.byte	W96
@ 114   ----------------------------------------
	.byte	W96
@ 115   ----------------------------------------
	.byte	W96
@ 116   ----------------------------------------
	.byte	W96
@ 117   ----------------------------------------
	.byte	W96
@ 118   ----------------------------------------
	.byte	W96
@ 119   ----------------------------------------
	.byte	W96
@ 120   ----------------------------------------
	.byte	W96
@ 121   ----------------------------------------
	.byte	W96
@ 122   ----------------------------------------
	.byte	W96
@ 123   ----------------------------------------
	.byte	W96
@ 124   ----------------------------------------
	.byte	W96
@ 125   ----------------------------------------
	.byte	W96
@ 126   ----------------------------------------
	.byte	W96
@ 127   ----------------------------------------
	.byte	W96
@ 128   ----------------------------------------
	.byte	W96
@ 129   ----------------------------------------
	.byte	W96
@ 130   ----------------------------------------
	.byte	W96
@ 131   ----------------------------------------
	.byte	W96
@ 132   ----------------------------------------
	.byte	W96
@ 133   ----------------------------------------
	.byte	W96
@ 134   ----------------------------------------
	.byte	W96
@ 135   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_016
@ 136   ----------------------------------------
	.byte	W96
@ 137   ----------------------------------------
	.byte	W96
@ 138   ----------------------------------------
	.byte	W96
@ 139   ----------------------------------------
	.byte	W96
@ 140   ----------------------------------------
	.byte	W96
@ 141   ----------------------------------------
	.byte	W96
@ 142   ----------------------------------------
	.byte	W96
@ 143   ----------------------------------------
	.byte	W96
@ 144   ----------------------------------------
	.byte	W96
@ 145   ----------------------------------------
	.byte	W96
@ 146   ----------------------------------------
	.byte	W96
@ 147   ----------------------------------------
	.byte	W96
@ 148   ----------------------------------------
	.byte	W96
@ 149   ----------------------------------------
	.byte	W96
@ 150   ----------------------------------------
	.byte	W96
@ 151   ----------------------------------------
	.byte	W96
@ 152   ----------------------------------------
	.byte	W96
@ 153   ----------------------------------------
	.byte	W96
@ 154   ----------------------------------------
	.byte	W96
@ 155   ----------------------------------------
	.byte	W96
@ 156   ----------------------------------------
	.byte		N06   , Cs4 , v096
	.byte	W06
	.byte		N01   , Bn2 
	.byte	W03
	.byte		N01   
	.byte	W03
	.byte		N06   , Cs4 
	.byte	W06
	.byte		N01   , Bn2 
	.byte	W18
	.byte		N12   , Bn3 
	.byte	W12
	.byte		N01   , Bn2 
	.byte	W03
	.byte		N01   
	.byte	W03
	.byte		N06   , Cs4 
	.byte	W12
	.byte		N01   
	.byte	W18
	.byte		N12   , Bn3 
	.byte	W12
@ 157   ----------------------------------------
	.byte	W96
@ 158   ----------------------------------------
	.byte	W96
@ 159   ----------------------------------------
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
@ 160   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_066
@ 161   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_067
@ 162   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_068
@ 163   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_069
@ 164   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_070
@ 165   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_071
@ 166   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_068
@ 167   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_073
@ 168   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_074
@ 169   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_075
@ 170   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_076
@ 171   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_069
@ 172   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_074
@ 173   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_071
@ 174   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_8_076
@ 175   ----------------------------------------
	.byte	FINE

@**************** Track 9 (Midi-Chn.11) ****************@

mus_custom_flockofbirds_9:
	.byte	KEYSH , mus_custom_flockofbirds_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 29
	.byte		VOL   , 95*mus_custom_flockofbirds_mvl/mxv
	.byte		PAN   , c_v+41
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
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		N12   , Bn2 , v096
	.byte	W01
	.byte		BEND  , c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W72
@ 018   ----------------------------------------
	.byte	W12
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		N12   , Fs2 
	.byte	W01
	.byte		BEND  , c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte		        c_v+10
	.byte		        c_v+9
	.byte		        c_v+8
	.byte	W01
	.byte		        c_v+7
	.byte		        c_v+6
	.byte		        c_v+5
	.byte		        c_v+4
	.byte	W01
	.byte		        c_v+3
	.byte		        c_v+2
	.byte		        c_v+1
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W54
	.byte		        c_v+0
	.byte		N12   , Fs3 
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
	.byte	W06
@ 019   ----------------------------------------
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		N12   
	.byte	W01
	.byte		BEND  , c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W36
	.byte		        c_v+0
	.byte		N12   , Gs3 
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
	.byte	W18
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		N12   , Cs3 
	.byte	W01
	.byte		BEND  , c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte		        c_v+10
	.byte		        c_v+9
	.byte		        c_v+8
	.byte		        c_v+7
	.byte		        c_v+6
	.byte	W01
	.byte		        c_v+5
	.byte		        c_v+4
	.byte		        c_v+3
	.byte		        c_v+2
	.byte		        c_v+1
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W06
@ 020   ----------------------------------------
	.byte	W54
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		N06   , Fs3 
	.byte	W01
	.byte		BEND  , c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte		        c_v+11
	.byte	W02
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W36
@ 021   ----------------------------------------
	.byte	W24
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		N12   , Gs3 
	.byte	W01
	.byte		BEND  , c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W60
@ 022   ----------------------------------------
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		N12   , Bn2 
	.byte	W01
	.byte		BEND  , c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W84
@ 023   ----------------------------------------
	.byte	W24
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		N12   , Gs2 
	.byte	W01
	.byte		BEND  , c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte		        c_v+10
	.byte		        c_v+9
	.byte		        c_v+8
	.byte	W01
	.byte		        c_v+7
	.byte		        c_v+6
	.byte		        c_v+5
	.byte		        c_v+4
	.byte	W01
	.byte		        c_v+3
	.byte		        c_v+2
	.byte		        c_v+1
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W60
@ 024   ----------------------------------------
	.byte	W48
	.byte		        c_v+11
	.byte		N12   , Bn2 
	.byte	W09
	.byte		BEND  , c_v+11
	.byte		        c_v+10
	.byte		        c_v+9
	.byte		        c_v+8
	.byte	W01
	.byte		        c_v+7
	.byte		        c_v+6
	.byte		        c_v+5
	.byte		        c_v+4
	.byte	W01
	.byte		        c_v+3
	.byte		        c_v+2
	.byte		        c_v+1
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W36
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
mus_custom_flockofbirds_9_033:
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	PEND
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
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W24
@ 050   ----------------------------------------
	.byte	W36
	.byte		BEND  , c_v+11
	.byte		N24   , Cs3 , v096
	.byte	W12
	.byte		BEND  , c_v+11
	.byte		        c_v+10
	.byte		        c_v+9
	.byte		        c_v+8
	.byte		        c_v+7
	.byte		        c_v+6
	.byte	W01
	.byte		        c_v+5
	.byte		        c_v+4
	.byte		        c_v+3
	.byte		        c_v+2
	.byte		        c_v+1
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v+0
	.byte	W10
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W24
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
@ 051   ----------------------------------------
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W84
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
@ 052   ----------------------------------------
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W96
@ 053   ----------------------------------------
	.byte	W96
@ 054   ----------------------------------------
	.byte	W54
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		N12   
	.byte	W01
	.byte		BEND  , c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte		        c_v+10
	.byte		        c_v+9
	.byte		        c_v+8
	.byte		        c_v+7
	.byte		        c_v+6
	.byte		        c_v+5
	.byte		        c_v+4
	.byte		        c_v+3
	.byte		        c_v+2
	.byte		        c_v+1
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W30
@ 055   ----------------------------------------
	.byte	W96
@ 056   ----------------------------------------
	.byte	W24
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		N06   , Gs3 
	.byte	W01
	.byte		BEND  , c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte		        c_v+11
	.byte	W02
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W66
@ 057   ----------------------------------------
	.byte	W84
	.byte		        c_v+27
	.byte		N12   , Ds3 
	.byte	W06
	.byte		BEND  , c_v+27
	.byte		        c_v+26
	.byte		        c_v+25
	.byte		        c_v+24
	.byte		        c_v+23
	.byte		        c_v+22
	.byte		        c_v+21
	.byte		        c_v+20
	.byte		        c_v+19
	.byte		        c_v+18
	.byte		        c_v+17
	.byte		        c_v+16
	.byte		        c_v+15
	.byte		        c_v+14
	.byte		        c_v+13
	.byte		        c_v+12
	.byte		        c_v+11
	.byte		        c_v+10
	.byte		        c_v+9
	.byte		        c_v+8
	.byte		        c_v+7
	.byte		        c_v+6
	.byte		        c_v+5
	.byte		        c_v+4
	.byte		        c_v+3
	.byte		        c_v+2
	.byte		        c_v+1
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v+0
	.byte	W05
@ 058   ----------------------------------------
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W24
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		N12   , Gs3 
	.byte	W01
	.byte		BEND  , c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte		        c_v+12
	.byte		        c_v+13
	.byte		        c_v+14
	.byte		        c_v+15
	.byte	W01
	.byte		        c_v+16
	.byte		        c_v+16
	.byte	W01
	.byte		        c_v+16
	.byte	W09
	.byte		        c_v+16
	.byte		        c_v+0
	.byte	W60
@ 059   ----------------------------------------
	.byte		        c_v+11
	.byte		N12   , Bn2 
	.byte	W06
	.byte		BEND  , c_v+11
	.byte		        c_v+10
	.byte		        c_v+9
	.byte		        c_v+8
	.byte		        c_v+7
	.byte		        c_v+6
	.byte		        c_v+5
	.byte		        c_v+4
	.byte		        c_v+3
	.byte		        c_v+2
	.byte		        c_v+1
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W84
@ 060   ----------------------------------------
	.byte	W96
@ 061   ----------------------------------------
	.byte	W96
@ 062   ----------------------------------------
	.byte	W96
@ 063   ----------------------------------------
	.byte	W24
	.byte		        c_v+11
	.byte		N12   , Gs3 
	.byte	W06
	.byte		BEND  , c_v+11
	.byte		        c_v+10
	.byte		        c_v+9
	.byte		        c_v+8
	.byte		        c_v+7
	.byte		        c_v+6
	.byte		        c_v+5
	.byte		        c_v+4
	.byte		        c_v+3
	.byte		        c_v+2
	.byte		        c_v+1
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W48
	.byte		        c_v+0
	.byte		N12   , Fs3 
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
@ 064   ----------------------------------------
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W36
	.byte		        c_v+11
	.byte		N24   , Cs3 
	.byte	W12
	.byte		BEND  , c_v+11
	.byte		        c_v+10
	.byte		        c_v+9
	.byte		        c_v+8
	.byte		        c_v+7
	.byte		        c_v+6
	.byte	W01
	.byte		        c_v+5
	.byte		        c_v+4
	.byte		        c_v+3
	.byte		        c_v+2
	.byte		        c_v+1
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v+0
	.byte	W10
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W18
	.byte		        c_v+11
	.byte		N12   
	.byte	W06
	.byte		BEND  , c_v+11
	.byte		        c_v+10
	.byte		        c_v+9
	.byte		        c_v+8
	.byte		        c_v+7
	.byte		        c_v+6
	.byte		        c_v+5
	.byte		        c_v+4
	.byte		        c_v+3
	.byte		        c_v+2
	.byte		        c_v+1
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W06
@ 065   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_9_033
@ 066   ----------------------------------------
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+10
	.byte		        c_v+11
	.byte		        c_v+11
	.byte		        c_v+12
	.byte		        c_v+12
	.byte		        c_v+13
	.byte		        c_v+13
	.byte		N06   , Ds2 , v096
	.byte		N06   , Ds3 
	.byte	W01
	.byte		BEND  , c_v+14
	.byte		        c_v+14
	.byte		        c_v+15
	.byte		        c_v+15
	.byte		        c_v+16
	.byte		        c_v+16
	.byte		        c_v+16
	.byte		        c_v+16
	.byte	W05
	.byte		        c_v+16
	.byte		        c_v+0
	.byte		        c_v+16
	.byte		        c_v+0
	.byte	W30
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		N12   , Gs3 
	.byte	W01
	.byte		BEND  , c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		N18   
	.byte	W01
	.byte		BEND  , c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W05
	.byte		        c_v+11
	.byte	W09
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W24
@ 067   ----------------------------------------
	.byte	W96
@ 068   ----------------------------------------
mus_custom_flockofbirds_9_068:
	.byte	W36
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		N12   , Gs3 , v096
	.byte	W01
	.byte		BEND  , c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		N18   
	.byte	W01
	.byte		BEND  , c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W05
	.byte		        c_v+11
	.byte	W09
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W24
	.byte	PEND
@ 069   ----------------------------------------
	.byte	W96
@ 070   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_9_068
@ 071   ----------------------------------------
	.byte	W96
@ 072   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_9_068
@ 073   ----------------------------------------
	.byte	W96
@ 074   ----------------------------------------
mus_custom_flockofbirds_9_074:
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+10
	.byte		        c_v+11
	.byte		        c_v+11
	.byte		        c_v+12
	.byte		        c_v+12
	.byte		        c_v+13
	.byte		        c_v+13
	.byte		N06   , Ds2 , v096
	.byte		N06   , Ds3 
	.byte	W01
	.byte		BEND  , c_v+14
	.byte		        c_v+14
	.byte		        c_v+15
	.byte		        c_v+15
	.byte		        c_v+16
	.byte		        c_v+16
	.byte		        c_v+16
	.byte		        c_v+16
	.byte	W05
	.byte		        c_v+16
	.byte		        c_v+0
	.byte		        c_v+16
	.byte		        c_v+0
	.byte	W66
	.byte		        c_v+0
	.byte		N12   , Cs4 
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
@ 075   ----------------------------------------
mus_custom_flockofbirds_9_075:
	.byte	W90
	.byte		BEND  , c_v+0
	.byte		N12   , Ds3 , v112
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
	.byte	PEND
@ 076   ----------------------------------------
mus_custom_flockofbirds_9_076:
	.byte		BEND  , c_v+16
	.byte	W06
	.byte		        c_v+16
	.byte		        c_v+0
	.byte	W30
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		N12   , Gs3 , v096
	.byte	W01
	.byte		BEND  , c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		N18   
	.byte	W01
	.byte		BEND  , c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W05
	.byte		        c_v+11
	.byte	W09
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W24
	.byte	PEND
@ 077   ----------------------------------------
	.byte	W96
@ 078   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_9_074
@ 079   ----------------------------------------
	.byte	W96
@ 080   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_9_068
@ 081   ----------------------------------------
	.byte	W96
@ 082   ----------------------------------------
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		N12   , Bn2 , v096
	.byte	W01
	.byte		BEND  , c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W60
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
@ 083   ----------------------------------------
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W02
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
	.byte	W96
@ 094   ----------------------------------------
	.byte	W96
@ 095   ----------------------------------------
	.byte	W96
@ 096   ----------------------------------------
	.byte	W96
@ 097   ----------------------------------------
	.byte	W96
@ 098   ----------------------------------------
	.byte	W96
@ 099   ----------------------------------------
	.byte	W96
@ 100   ----------------------------------------
	.byte	W96
@ 101   ----------------------------------------
	.byte	W96
@ 102   ----------------------------------------
	.byte	W96
@ 103   ----------------------------------------
	.byte	W96
@ 104   ----------------------------------------
	.byte	W96
@ 105   ----------------------------------------
	.byte	W96
@ 106   ----------------------------------------
	.byte	W96
@ 107   ----------------------------------------
	.byte	W96
@ 108   ----------------------------------------
	.byte	W96
@ 109   ----------------------------------------
	.byte	W96
@ 110   ----------------------------------------
	.byte	W96
@ 111   ----------------------------------------
	.byte	W96
@ 112   ----------------------------------------
	.byte	W96
@ 113   ----------------------------------------
	.byte	W96
@ 114   ----------------------------------------
	.byte	W96
@ 115   ----------------------------------------
	.byte	W96
@ 116   ----------------------------------------
	.byte	W96
@ 117   ----------------------------------------
	.byte	W96
@ 118   ----------------------------------------
	.byte	W96
@ 119   ----------------------------------------
	.byte	W96
@ 120   ----------------------------------------
	.byte	W96
@ 121   ----------------------------------------
	.byte	W96
@ 122   ----------------------------------------
	.byte	W96
@ 123   ----------------------------------------
	.byte	W96
@ 124   ----------------------------------------
	.byte	W96
@ 125   ----------------------------------------
	.byte	W96
@ 126   ----------------------------------------
	.byte	W96
@ 127   ----------------------------------------
	.byte	W96
@ 128   ----------------------------------------
	.byte	W96
@ 129   ----------------------------------------
	.byte	W96
@ 130   ----------------------------------------
	.byte	W96
@ 131   ----------------------------------------
	.byte	W96
@ 132   ----------------------------------------
	.byte	W96
@ 133   ----------------------------------------
	.byte	W96
@ 134   ----------------------------------------
	.byte	W96
@ 135   ----------------------------------------
	.byte	W96
@ 136   ----------------------------------------
	.byte	W96
@ 137   ----------------------------------------
	.byte	W96
@ 138   ----------------------------------------
	.byte	W96
@ 139   ----------------------------------------
	.byte	W96
@ 140   ----------------------------------------
	.byte	W96
@ 141   ----------------------------------------
	.byte	W96
@ 142   ----------------------------------------
	.byte	W96
@ 143   ----------------------------------------
	.byte	W96
@ 144   ----------------------------------------
	.byte	W96
@ 145   ----------------------------------------
	.byte	W96
@ 146   ----------------------------------------
	.byte	W96
@ 147   ----------------------------------------
	.byte	W96
@ 148   ----------------------------------------
	.byte	W96
@ 149   ----------------------------------------
	.byte	W96
@ 150   ----------------------------------------
	.byte	W96
@ 151   ----------------------------------------
	.byte	W96
@ 152   ----------------------------------------
	.byte	W96
@ 153   ----------------------------------------
	.byte	W96
@ 154   ----------------------------------------
	.byte	W96
@ 155   ----------------------------------------
	.byte	W96
@ 156   ----------------------------------------
	.byte	W24
	.byte		        c_v+0
	.byte		N12   , Cs4 
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
@ 157   ----------------------------------------
	.byte	W96
@ 158   ----------------------------------------
	.byte	W96
@ 159   ----------------------------------------
	.byte		        c_v+0
	.byte		        c_v+0
	.byte		N96   , Cs2 
	.byte		N96   , Cs3 
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+1
	.byte	W01
	.byte		        c_v+2
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+3
	.byte	W01
	.byte		        c_v+4
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+5
	.byte	W01
	.byte		        c_v+6
	.byte		        c_v+6
	.byte	W01
	.byte		        c_v+7
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+8
	.byte	W01
	.byte		        c_v+9
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+10
	.byte	W01
	.byte		        c_v+11
	.byte		        c_v+11
	.byte		        c_v+12
	.byte		        c_v+12
	.byte	W01
	.byte		        c_v+13
	.byte		        c_v+13
	.byte	W01
	.byte		        c_v+14
	.byte		        c_v+14
	.byte		        c_v+15
	.byte		        c_v+15
	.byte	W01
	.byte		        c_v+16
	.byte		        c_v+16
	.byte		        c_v+17
	.byte		        c_v+17
	.byte	W01
	.byte		        c_v+18
	.byte		        c_v+18
	.byte		        c_v+19
	.byte		        c_v+19
	.byte	W01
	.byte		        c_v+20
	.byte		        c_v+20
	.byte	W01
	.byte		        c_v+21
	.byte		        c_v+21
	.byte		        c_v+22
	.byte		        c_v+22
	.byte	W01
	.byte		        c_v+23
	.byte		        c_v+23
	.byte		        c_v+24
	.byte		        c_v+24
	.byte	W01
	.byte		        c_v+25
	.byte		        c_v+25
	.byte		        c_v+26
	.byte		        c_v+26
	.byte	W01
	.byte		        c_v+27
	.byte		        c_v+27
	.byte	W01
	.byte		        c_v+27
	.byte		        c_v+27
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
	.byte	W01
@ 160   ----------------------------------------
	.byte		        c_v+27
	.byte		        c_v+0
	.byte		        c_v+27
	.byte		        c_v+0
	.byte		        c_v+0
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+6
	.byte		        c_v+7
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+10
	.byte		        c_v+11
	.byte		        c_v+11
	.byte		        c_v+12
	.byte		        c_v+12
	.byte		        c_v+13
	.byte		        c_v+13
	.byte		N06   , Ds2 
	.byte		N06   , Ds3 
	.byte	W01
	.byte		BEND  , c_v+14
	.byte		        c_v+14
	.byte		        c_v+15
	.byte		        c_v+15
	.byte		        c_v+16
	.byte		        c_v+16
	.byte		        c_v+16
	.byte		        c_v+16
	.byte	W05
	.byte		        c_v+16
	.byte		        c_v+0
	.byte		        c_v+16
	.byte		        c_v+0
	.byte	W30
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		N12   , Gs3 
	.byte	W01
	.byte		BEND  , c_v+6
	.byte		        c_v+7
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W03
	.byte		        c_v+11
	.byte	W06
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		N18   
	.byte	W01
	.byte		BEND  , c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+11
	.byte	W05
	.byte		        c_v+11
	.byte	W09
	.byte		        c_v+11
	.byte		        c_v+0
	.byte	W24
@ 161   ----------------------------------------
	.byte	W96
@ 162   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_9_068
@ 163   ----------------------------------------
	.byte	W96
@ 164   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_9_068
@ 165   ----------------------------------------
	.byte	W96
@ 166   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_9_068
@ 167   ----------------------------------------
	.byte	W96
@ 168   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_9_074
@ 169   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_9_075
@ 170   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_9_076
@ 171   ----------------------------------------
	.byte	W96
@ 172   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_9_074
@ 173   ----------------------------------------
	.byte	W96
@ 174   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_9_068
@ 175   ----------------------------------------
	.byte	FINE

@**************** Track 10 (Midi-Chn.12) ****************@

mus_custom_flockofbirds_10:
	.byte	KEYSH , mus_custom_flockofbirds_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 30
	.byte		VOL   , 96*mus_custom_flockofbirds_mvl/mxv
	.byte		PAN   , c_v-45
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
	.byte	W18
	.byte		N18   , Ds3 , v096
	.byte	W18
	.byte		N12   , Fs3 
	.byte	W12
	.byte		N36   , Gs3 
	.byte	W18
	.byte		N30   , Ds3 
	.byte	W18
	.byte		N48   , Cs3 
	.byte	W12
@ 026   ----------------------------------------
	.byte	W18
	.byte		N18   , Fs2 
	.byte	W18
	.byte		BEND  , c_v+11
	.byte		N24   , Cs3 
	.byte	W12
	.byte		BEND  , c_v+11
	.byte		        c_v+10
	.byte		        c_v+9
	.byte		        c_v+8
	.byte		        c_v+7
	.byte		        c_v+6
	.byte	W01
	.byte		        c_v+5
	.byte		        c_v+4
	.byte		        c_v+3
	.byte		        c_v+2
	.byte		        c_v+1
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v+0
	.byte	W10
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W12
	.byte		N06   , As2 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		BEND  , c_v+0
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
	.byte		        c_v+12
	.byte		        c_v+13
	.byte		        c_v+14
	.byte		        c_v+15
	.byte		        c_v+16
	.byte	W01
	.byte		        c_v+16
	.byte	W06
@ 027   ----------------------------------------
	.byte		        c_v+16
	.byte		        c_v+0
	.byte		N06   , Gs2 
	.byte	W12
	.byte		        Ds3 
	.byte	W06
	.byte		N12   , Bn2 
	.byte	W18
	.byte		N06   , Gs2 
	.byte	W12
	.byte		        Cs3 
	.byte	W06
	.byte		N12   , Bn2 
	.byte	W18
	.byte		N06   , Gn2 
	.byte	W12
	.byte		        Cs3 
	.byte	W06
	.byte		N18   , As2 
	.byte	W06
@ 028   ----------------------------------------
	.byte	W12
	.byte		        Fs2 
	.byte	W30
	.byte		N06   
	.byte	W06
	.byte		        As2 
	.byte	W06
	.byte		N01   , Gn2 
	.byte	W06
	.byte		N06   , Bn2 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		N01   , Cs3 , v112
	.byte	W06
	.byte		N06   , Bn2 , v096
	.byte	W06
	.byte		        Fs3 
	.byte	W12
@ 029   ----------------------------------------
	.byte		BEND  , c_v+0
	.byte		N18   , Cs3 
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte		        c_v+11
	.byte	W05
	.byte		        c_v+11
	.byte		        c_v+0
	.byte		N12   , Bn2 
	.byte	W36
	.byte		N03   , As2 , v112
	.byte	W03
	.byte		        Bn2 
	.byte	W03
	.byte		N06   , Fs3 , v096
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        As2 , v112
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte		        Fs2 
	.byte	W06
@ 030   ----------------------------------------
	.byte		BEND  , c_v+0
	.byte		N18   , Bn2 , v096
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		        c_v+2
	.byte		        c_v+3
	.byte		        c_v+4
	.byte		        c_v+5
	.byte		        c_v+6
	.byte		        c_v+7
	.byte	W01
	.byte		        c_v+8
	.byte		        c_v+9
	.byte		        c_v+10
	.byte		        c_v+11
	.byte		        c_v+11
	.byte	W05
	.byte		        c_v+11
	.byte		        c_v+0
	.byte		N12   , Fs2 
	.byte	W36
	.byte	W02
	.byte		N04   , Dn2 
	.byte	W04
	.byte		        Ds2 
	.byte	W04
	.byte		        Fs2 
	.byte	W04
	.byte		        As2 
	.byte	W04
	.byte		N06   , Cs3 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        As3 
	.byte	W06
@ 031   ----------------------------------------
	.byte	W06
	.byte		        Gs2 
	.byte	W12
	.byte		        Ds3 
	.byte	W12
	.byte		        Fs3 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		N01   , Ds3 
	.byte	W06
	.byte		N06   
	.byte	W06
	.byte		        Dn3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		N01   
	.byte	W06
	.byte		N06   , Gs2 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
@ 032   ----------------------------------------
	.byte		        Bn3 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		BEND  , c_v+11
	.byte		N12   , Bn2 
	.byte	W06
	.byte		BEND  , c_v+11
	.byte		        c_v+10
	.byte		        c_v+9
	.byte		        c_v+8
	.byte		        c_v+7
	.byte		        c_v+6
	.byte		        c_v+5
	.byte		        c_v+4
	.byte		        c_v+3
	.byte		        c_v+2
	.byte		        c_v+1
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v+0
	.byte		        c_v+0
	.byte		N12   , Gs2 
	.byte	W06
	.byte		N54   , Bn2 
	.byte	W06
	.byte		N48   , Fs3 
	.byte	W54
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
	.byte	W96
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
mus_custom_flockofbirds_10_066:
	.byte		N06   , En2 , v096
	.byte		N06   , Bn2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        En2 
	.byte		N06   , Bn2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        En2 
	.byte		N06   , Bn2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        En2 
	.byte		N06   , Bn2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		N12   , En1 
	.byte	W12
	.byte		        Gs2 , v112
	.byte		N12   , Ds3 
	.byte		N12   , As3 
	.byte	W18
	.byte		N18   , Gs2 
	.byte		N18   , Ds3 
	.byte		N18   , As3 
	.byte	W18
	.byte		N48   , Bn2 
	.byte	W06
	.byte		N18   , En3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N06   , Ds4 
	.byte	W06
	.byte	PEND
@ 067   ----------------------------------------
mus_custom_flockofbirds_10_067:
	.byte		N06   , Bn3 , v112
	.byte	W06
	.byte		N18   , Fs3 
	.byte	W06
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        Cs4 
	.byte	W12
	.byte		        Gs2 
	.byte		N06   , Ds3 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N24   , Cs3 
	.byte		N24   , As3 
	.byte	W12
	.byte		N12   , Fs3 
	.byte	W12
	.byte		        Cs2 
	.byte		N12   , Gs2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		        En3 
	.byte	W12
	.byte	PEND
@ 068   ----------------------------------------
mus_custom_flockofbirds_10_068:
	.byte	W06
	.byte		N06   , En2 , v096
	.byte		N06   , Bn2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        En2 , v112
	.byte		N06   , Bn2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        En2 , v096
	.byte		N06   , Bn2 
	.byte		N06   , Fs3 
	.byte	W06
	.byte		N12   , En1 
	.byte	W12
	.byte		        Bn2 , v112
	.byte		N12   , Fs3 
	.byte		N12   , As3 
	.byte	W18
	.byte		N42   , En1 
	.byte		N18   , Bn2 
	.byte		N18   , Fs3 
	.byte		N18   , As3 
	.byte	W18
	.byte		N48   , Bn2 
	.byte	W06
	.byte		N18   , En3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N06   , Ds4 
	.byte	W06
	.byte	PEND
@ 069   ----------------------------------------
mus_custom_flockofbirds_10_069:
	.byte		N06   , Bn3 , v112
	.byte	W06
	.byte		N18   , Fs3 
	.byte	W06
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        Cs4 
	.byte	W12
	.byte		        Gs2 
	.byte		N06   , Ds3 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte		N24   , As3 
	.byte	W12
	.byte		N12   , Fs3 
	.byte	W12
	.byte		N06   , Cs2 
	.byte		N06   , Gs2 
	.byte		N06   , Ds3 
	.byte	W12
	.byte		        Ds2 
	.byte		N06   , As2 
	.byte		N06   , Fs3 
	.byte	W12
	.byte		        Gs3 , v096
	.byte	W06
	.byte	PEND
@ 070   ----------------------------------------
mus_custom_flockofbirds_10_070:
	.byte		BEND  , c_v+0
	.byte		N12   , Gs3 , v096
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
	.byte		N12   , Fs3 
	.byte	W12
	.byte		        En1 
	.byte	W12
	.byte		N18   , Bn1 , v112
	.byte		N18   , Fs2 
	.byte		N18   , Cs3 
	.byte	W18
	.byte		N12   , Cs2 
	.byte		N12   , Gs2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N48   , Bn2 
	.byte	W06
	.byte		N18   , En3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N06   , Ds4 
	.byte	W06
	.byte	PEND
@ 071   ----------------------------------------
mus_custom_flockofbirds_10_071:
	.byte		N06   , Bn3 , v112
	.byte	W06
	.byte		N18   , Fs3 
	.byte	W06
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        Cs4 
	.byte	W12
	.byte		        Gs2 
	.byte		N06   , Ds3 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte		N24   , As3 
	.byte	W12
	.byte		N12   , Fs3 
	.byte	W12
	.byte		N03   , Ds4 
	.byte	W03
	.byte		        Cs4 
	.byte	W03
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N12   , Ds3 
	.byte	W06
	.byte	PEND
@ 072   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_068
@ 073   ----------------------------------------
mus_custom_flockofbirds_10_073:
	.byte		N06   , Bn3 , v096
	.byte	W06
	.byte		N18   , Fs3 , v112
	.byte	W06
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        Cs4 
	.byte	W12
	.byte		        Gs2 
	.byte		N06   , Ds3 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte		N24   , As3 
	.byte	W12
	.byte		N12   , Fs3 
	.byte	W18
	.byte		N06   , Ds3 , v096
	.byte	W06
	.byte		        En3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte	PEND
@ 074   ----------------------------------------
mus_custom_flockofbirds_10_074:
	.byte		N06   , Bn3 , v096
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		N12   , Ds4 
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
	.byte		N36   , Gs2 
	.byte	W06
	.byte		N30   , Ds3 
	.byte	W06
	.byte		N24   , As3 
	.byte	W06
	.byte		N18   , Bn3 
	.byte	W18
	.byte		N48   , Bn2 , v112
	.byte	W06
	.byte		N18   , En3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N06   , Ds4 
	.byte	W06
	.byte	PEND
@ 075   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_067
@ 076   ----------------------------------------
mus_custom_flockofbirds_10_076:
	.byte	W06
	.byte		N12   , Cs3 , v096
	.byte		N12   , Fs3 
	.byte	W12
	.byte		N06   , Ds3 
	.byte		N06   , Gs3 
	.byte	W06
	.byte		N12   , En1 
	.byte	W12
	.byte		        Bn2 , v112
	.byte		N12   , Fs3 
	.byte		N12   , As3 
	.byte	W18
	.byte		N42   , En1 
	.byte		N18   , Bn2 
	.byte		N18   , Fs3 
	.byte		N18   , As3 
	.byte	W18
	.byte		N48   , Bn2 
	.byte	W06
	.byte		N18   , En3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		N06   , Ds4 
	.byte	W06
	.byte	PEND
@ 077   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_069
@ 078   ----------------------------------------
mus_custom_flockofbirds_10_078:
	.byte		BEND  , c_v+0
	.byte		N12   , Gs3 , v096
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
	.byte		N06   , Fs3 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		N12   , Ds4 
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
	.byte		N06   , As3 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		N18   , Bn3 
	.byte	W18
	.byte		N48   , Bn2 , v112
	.byte	W06
	.byte		N18   , En3 
	.byte	W06
	.byte		N12   , Fs3 
	.byte	W06
	.byte		N06   , Ds4 
	.byte	W06
	.byte	PEND
@ 079   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_071
@ 080   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_076
@ 081   ----------------------------------------
mus_custom_flockofbirds_10_081:
	.byte		N06   , Bn3 , v096
	.byte	W06
	.byte		N18   , Fs3 , v112
	.byte	W06
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        Cs4 
	.byte	W12
	.byte		        Gs2 
	.byte		N06   , Ds3 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N48   , Fs2 
	.byte		N48   , Cs3 
	.byte		N48   , As3 
	.byte	W12
	.byte		N36   , Fs3 
	.byte	W42
	.byte	PEND
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
	.byte	W96
@ 094   ----------------------------------------
	.byte	W96
@ 095   ----------------------------------------
	.byte	W96
@ 096   ----------------------------------------
	.byte	W96
@ 097   ----------------------------------------
	.byte	W96
@ 098   ----------------------------------------
	.byte	W96
@ 099   ----------------------------------------
	.byte	W96
@ 100   ----------------------------------------
	.byte	W96
@ 101   ----------------------------------------
	.byte	W96
@ 102   ----------------------------------------
	.byte	W96
@ 103   ----------------------------------------
	.byte	W96
@ 104   ----------------------------------------
	.byte	W96
@ 105   ----------------------------------------
	.byte	W96
@ 106   ----------------------------------------
	.byte	W96
@ 107   ----------------------------------------
	.byte	W96
@ 108   ----------------------------------------
	.byte	W96
@ 109   ----------------------------------------
	.byte	W96
@ 110   ----------------------------------------
	.byte	W96
@ 111   ----------------------------------------
	.byte	W96
@ 112   ----------------------------------------
	.byte	W96
@ 113   ----------------------------------------
	.byte	W96
@ 114   ----------------------------------------
	.byte	W96
@ 115   ----------------------------------------
	.byte	W96
@ 116   ----------------------------------------
	.byte	W96
@ 117   ----------------------------------------
	.byte	W96
@ 118   ----------------------------------------
	.byte	W96
@ 119   ----------------------------------------
	.byte	W96
@ 120   ----------------------------------------
	.byte	W96
@ 121   ----------------------------------------
	.byte	W96
@ 122   ----------------------------------------
	.byte	W96
@ 123   ----------------------------------------
	.byte	W96
@ 124   ----------------------------------------
	.byte	W96
@ 125   ----------------------------------------
	.byte	W96
@ 126   ----------------------------------------
	.byte	W96
@ 127   ----------------------------------------
	.byte	W96
@ 128   ----------------------------------------
	.byte	W96
@ 129   ----------------------------------------
	.byte	W96
@ 130   ----------------------------------------
	.byte	W96
@ 131   ----------------------------------------
	.byte	W96
@ 132   ----------------------------------------
	.byte	W96
@ 133   ----------------------------------------
	.byte	W96
@ 134   ----------------------------------------
	.byte	W96
@ 135   ----------------------------------------
	.byte	W96
@ 136   ----------------------------------------
	.byte	W96
@ 137   ----------------------------------------
	.byte	W96
@ 138   ----------------------------------------
	.byte	W96
@ 139   ----------------------------------------
	.byte	W96
@ 140   ----------------------------------------
	.byte	W96
@ 141   ----------------------------------------
	.byte	W96
@ 142   ----------------------------------------
	.byte	W96
@ 143   ----------------------------------------
	.byte	W96
@ 144   ----------------------------------------
	.byte	W96
@ 145   ----------------------------------------
	.byte	W96
@ 146   ----------------------------------------
	.byte	W96
@ 147   ----------------------------------------
	.byte	W96
@ 148   ----------------------------------------
	.byte	W96
@ 149   ----------------------------------------
	.byte	W96
@ 150   ----------------------------------------
	.byte	W96
@ 151   ----------------------------------------
	.byte	W96
@ 152   ----------------------------------------
	.byte	W96
@ 153   ----------------------------------------
	.byte	W96
@ 154   ----------------------------------------
	.byte	W96
@ 155   ----------------------------------------
	.byte	W96
@ 156   ----------------------------------------
	.byte	W96
@ 157   ----------------------------------------
	.byte	W96
@ 158   ----------------------------------------
	.byte	W96
@ 159   ----------------------------------------
	.byte	W96
@ 160   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_066
@ 161   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_067
@ 162   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_068
@ 163   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_069
@ 164   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_070
@ 165   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_071
@ 166   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_068
@ 167   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_073
@ 168   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_074
@ 169   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_067
@ 170   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_076
@ 171   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_069
@ 172   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_078
@ 173   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_071
@ 174   ----------------------------------------
	.byte	W06
	.byte		N12   , Cs3 , v096
	.byte		N12   , Fs3 
	.byte	W12
	.byte		N06   , Ds3 
	.byte		N06   , Gs3 
	.byte	W06
	.byte		N12   , En1 
	.byte	W12
	.byte		        Bn2 , v112
	.byte		N12   , Fs3 
	.byte		N12   , As3 
	.byte	W18
	.byte		N42   , En1 
	.byte		N18   , Bn2 
	.byte		N18   , Fs3 
	.byte		N18   , As3 
	.byte	W18
	.byte		N24   , Bn2 
	.byte	W06
	.byte		N18   , En3 
	.byte	W06
	.byte		N12   , Fs3 
	.byte	W06
	.byte		N06   , Ds4 
	.byte	W06
@ 175   ----------------------------------------
	.byte	W96
@ 176   ----------------------------------------
	.byte	W12
	.byte		        Ds3 , v096
	.byte	W18
	.byte		        En2 
	.byte		N06   , Cs3 
	.byte	W12
	.byte		N24   , En2 
	.byte		N24   , Cs3 
	.byte	W18
	.byte		N06   , Ds3 
	.byte	W18
	.byte		        Ds2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N18   , Ds2 
	.byte		N18   , Bn2 
	.byte	W06
@ 177   ----------------------------------------
	.byte	W12
	.byte		N06   , Fs3 
	.byte	W18
	.byte		        Ds2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N24   , Ds2 
	.byte		N24   , Bn2 
	.byte	W18
	.byte		N06   , Fs3 
	.byte	W18
	.byte		        Ds2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N18   , Gs2 
	.byte		N18   , Bn2 
	.byte	W06
@ 178   ----------------------------------------
	.byte	W12
	.byte		N06   , Ds3 
	.byte	W18
	.byte		        Gs2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N18   , Gs2 
	.byte		N18   , Bn2 
	.byte	W18
	.byte		N06   , Ds3 
	.byte	W18
	.byte		        Gs2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N18   , Fs2 
	.byte		N18   , Bn2 
	.byte	W06
@ 179   ----------------------------------------
	.byte	W12
	.byte		N06   , Cs3 
	.byte	W18
	.byte		        Fs2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N18   , Fs2 
	.byte		N18   , Bn2 
	.byte	W18
	.byte		N06   , Cs3 
	.byte	W18
	.byte		        En2 
	.byte		N06   , Cs3 
	.byte	W12
	.byte		        En2 
	.byte		N06   , Cs3 
	.byte	W06
@ 180   ----------------------------------------
	.byte	W96
@ 181   ----------------------------------------
	.byte		        Bn3 , v112
	.byte	W06
	.byte		N18   , Fs3 
	.byte	W06
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        Cs4 
	.byte	W12
	.byte		        Gs2 
	.byte		N06   , Ds3 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N24   , Fs2 
	.byte		N24   , Cs3 
	.byte		N24   , As3 
	.byte	W12
	.byte		N12   , Fs3 
	.byte	W12
	.byte		N06   , Cs2 
	.byte		N06   , Gs2 
	.byte		N06   , Ds3 
	.byte	W12
	.byte		N12   , Ds2 
	.byte		N12   , As2 
	.byte		N12   , Fs3 
	.byte	W12
	.byte		BEND  , c_v+27
	.byte		N09   , Ds3 
	.byte	W04
	.byte		BEND  , c_v+27
	.byte	W02
@ 182   ----------------------------------------
	.byte		        c_v+27
	.byte		        c_v+26
	.byte		        c_v+25
	.byte		        c_v+24
	.byte	W01
	.byte		        c_v+23
	.byte		        c_v+22
	.byte		        c_v+21
	.byte		        c_v+20
	.byte		        c_v+19
	.byte		        c_v+18
	.byte		        c_v+17
	.byte		        c_v+16
	.byte		        c_v+15
	.byte		        c_v+14
	.byte		        c_v+13
	.byte		        c_v+12
	.byte		        c_v+11
	.byte	W01
	.byte		        c_v+10
	.byte		        c_v+9
	.byte		        c_v+8
	.byte		        c_v+7
	.byte		        c_v+6
	.byte		        c_v+5
	.byte		        c_v+4
	.byte		        c_v+3
	.byte		        c_v+2
	.byte		        c_v+1
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W03
	.byte		N06   , Bn2 
	.byte	W06
	.byte		N12   
	.byte	W12
	.byte		        En1 , v096
	.byte	W12
	.byte		N18   , Bn1 , v112
	.byte		N18   , Fs2 
	.byte		N18   , Cs3 
	.byte	W18
	.byte		N12   , Cs2 
	.byte		N12   , Gs2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N24   , Bn2 
	.byte	W06
	.byte		N18   , En3 
	.byte	W06
	.byte		N12   , Fs3 
	.byte	W06
	.byte		N06   , Ds4 
	.byte	W06
@ 183   ----------------------------------------
	.byte	W96
@ 184   ----------------------------------------
	.byte		N12   , En1 , v096
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		N24   , Fs3 
	.byte	W12
	.byte		N18   , En3 
	.byte	W12
	.byte		N06   , Bn2 
	.byte	W06
	.byte		N12   , Gs1 
	.byte		N12   , Fs2 
	.byte		N12   , Bn2 
	.byte	W18
	.byte		N24   , Cs3 
	.byte	W12
	.byte		N12   , Bn2 
	.byte	W12
	.byte		N06   , Fs2 
	.byte	W06
@ 185   ----------------------------------------
	.byte	W96
@ 186   ----------------------------------------
	.byte		        Bn3 , v112
	.byte	W06
	.byte		N18   , Fs3 
	.byte	W06
	.byte		N06   , Bn3 
	.byte	W06
	.byte		        Cs4 
	.byte	W12
	.byte		        Gs2 
	.byte		N06   , Ds3 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N24   , Cs3 
	.byte		N24   , As3 
	.byte	W12
	.byte		N12   , Fs3 
	.byte	W12
	.byte		        Cs2 , v096
	.byte		N12   , Gs2 
	.byte		N12   , Ds3 
	.byte	W18
	.byte		        En3 
	.byte	W12
@ 187   ----------------------------------------
	.byte	W96
@ 188   ----------------------------------------
mus_custom_flockofbirds_10_188:
	.byte		N12   , En1 , v096
	.byte		N12   , Bn2 
	.byte		N12   , Ds3 
	.byte	W12
	.byte		N06   , En1 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        En3 
	.byte	W06
	.byte		        Fs3 
	.byte	W12
	.byte		        Bn2 
	.byte	W12
	.byte		BEND  , c_v+11
	.byte		N12   , Cs3 
	.byte	W04
	.byte		BEND  , c_v+11
	.byte		        c_v+10
	.byte		        c_v+9
	.byte		        c_v+8
	.byte		        c_v+7
	.byte		        c_v+6
	.byte		        c_v+5
	.byte		        c_v+4
	.byte		        c_v+3
	.byte		        c_v+2
	.byte		        c_v+1
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v+0
	.byte	W03
	.byte		        c_v+0
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		N06   , Fs2 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		N12   , Bn2 
	.byte	W12
	.byte	PEND
@ 189   ----------------------------------------
mus_custom_flockofbirds_10_189:
	.byte		N12   , Gs1 , v096
	.byte		N12   , Fs2 
	.byte		N12   , Bn2 
	.byte	W18
	.byte		N06   
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W12
	.byte		N18   , Fs1 
	.byte		N18   , Fs2 
	.byte		N12   , Bn2 
	.byte	W12
	.byte		N06   , As2 
	.byte	W06
	.byte		        Gs2 
	.byte	W06
	.byte		        Fs2 
	.byte	W06
	.byte		N12   , Gs2 
	.byte	W04
	.byte		BEND  , c_v+0
	.byte	W04
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+1
	.byte		        c_v+0
	.byte		N12   , Fs2 
	.byte	W12
	.byte	PEND
@ 190   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_188
@ 191   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_189
@ 192   ----------------------------------------
mus_custom_flockofbirds_10_192:
	.byte		N48   , Bn2 , v096
	.byte		N48   , Fs3 
	.byte		N48   , Ds4 
	.byte	W54
	.byte		N18   , Ds3 
	.byte		N18   , Bn3 
	.byte		N18   , Fs4 
	.byte	W18
	.byte		N12   , Cs3 
	.byte		N12   , Gs3 
	.byte		N12   , Ds4 
	.byte	W12
	.byte		N48   , Cs3 
	.byte		N48   , Fs3 
	.byte		N48   , Cs4 
	.byte	W12
	.byte	PEND
@ 193   ----------------------------------------
mus_custom_flockofbirds_10_193:
	.byte	W42
	.byte		N06   , Bn3 , v096
	.byte	W06
	.byte		        As3 
	.byte	W06
	.byte		        Gs3 
	.byte	W06
	.byte		        Fs3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		N48   , En1 
	.byte		N48   , Bn2 
	.byte		N48   , En3 
	.byte	W24
	.byte	PEND
@ 194   ----------------------------------------
	.byte	W24
	.byte		N36   , En1 
	.byte		N36   , Bn2 
	.byte		N36   , En3 
	.byte	W18
	.byte		N18   , Gs3 
	.byte	W18
	.byte		N36   , Fs1 
	.byte		N36   , As2 
	.byte		N36   , Fs3 
	.byte	W36
@ 195   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_192
@ 196   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_193
@ 197   ----------------------------------------
	.byte	W24
	.byte		N36   , En1 , v096
	.byte		N36   , Bn2 
	.byte		N36   , En3 
	.byte	W18
	.byte		N18   , Gs3 
	.byte	W18
	.byte		N36   , Fs1 
	.byte		N36   , As2 
	.byte		N18   , Fs3 
	.byte	W18
	.byte		        En3 
	.byte	W18
@ 198   ----------------------------------------
	.byte		        Ds3 
	.byte	W96
@ 199   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_081
@ 200   ----------------------------------------
	.byte		N48   , En2 , v096
	.byte		N48   , Cs3 
	.byte	W54
	.byte		N42   , En2 
	.byte		N42   , Fs3 
	.byte	W18
	.byte		N12   , Bn2 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
@ 201   ----------------------------------------
	.byte		        Ds2 
	.byte		N12   , Bn2 
	.byte	W12
	.byte		N06   , Fs3 
	.byte	W18
	.byte		        Ds2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		N24   , Ds2 
	.byte		N24   , Bn2 
	.byte	W18
	.byte		N06   , Fs3 
	.byte	W18
	.byte		        Ds2 
	.byte		N06   , Bn2 
	.byte	W12
	.byte		        Gs2 
	.byte		N06   , Bn2 
	.byte	W06
@ 202   ----------------------------------------
	.byte	W96
@ 203   ----------------------------------------
mus_custom_flockofbirds_10_203:
	.byte		N24   , Fs1 , v096
	.byte		N06   , As2 
	.byte	W06
	.byte		N18   , Bn2 
	.byte	W06
	.byte		N12   , Cs3 
	.byte	W06
	.byte		N06   , Fs3 
	.byte	W06
	.byte		N01   , En2 
	.byte		N01   , Cs3 
	.byte	W12
	.byte		N36   , Gs1 
	.byte		N36   , Bn2 
	.byte	W24
	.byte		N12   , Cs3 
	.byte	W12
	.byte		N01   , En2 
	.byte		N01   , Cs3 
	.byte	W12
	.byte		N66   , En1 
	.byte		N66   , Gs2 
	.byte	W12
	.byte	PEND
@ 204   ----------------------------------------
mus_custom_flockofbirds_10_204:
	.byte	W12
	.byte		N12   , Ds3 , v096
	.byte	W12
	.byte		N01   , En2 
	.byte		N01   , Cs3 
	.byte	W10
	.byte		        Cs3 , v127
	.byte	W02
	.byte		N18   , Cs3 , v096
	.byte	W18
	.byte		        Bn2 
	.byte	W18
	.byte		N12   , Gs2 
	.byte	W12
	.byte		        As2 
	.byte	W12
	.byte	PEND
@ 205   ----------------------------------------
mus_custom_flockofbirds_10_205:
	.byte		N24   , Fs1 , v096
	.byte		N06   , As2 
	.byte	W06
	.byte		N18   , Bn2 
	.byte	W06
	.byte		N12   , Cs3 
	.byte	W06
	.byte		N06   , Fs3 
	.byte	W06
	.byte		N01   , En2 
	.byte		N01   , Cs3 
	.byte	W12
	.byte		N36   , Gs1 
	.byte		N36   , Bn2 
	.byte	W24
	.byte		N12   , Cs3 
	.byte	W12
	.byte		N01   , En2 
	.byte		N01   , Cs3 
	.byte	W12
	.byte		TIE   , Bn1 
	.byte		N84   , En3 
	.byte	W12
	.byte	PEND
@ 206   ----------------------------------------
mus_custom_flockofbirds_10_206:
	.byte	W12
	.byte		N42   , Bn3 , v096
	.byte	W24
	.byte		N18   , As3 
	.byte	W18
	.byte		        Ds3 
	.byte	W18
	.byte		N06   , En3 
	.byte	W06
	.byte		        Ds3 
	.byte	W06
	.byte		        Cs3 
	.byte	W06
	.byte		        Bn2 
	.byte	W06
	.byte	PEND
@ 207   ----------------------------------------
mus_custom_flockofbirds_10_207:
	.byte		N06   , An1 , v096
	.byte		N06   , Cs3 
	.byte	W06
	.byte		N18   , Dn3 
	.byte	W06
	.byte		N12   , En3 
	.byte	W06
	.byte		N06   , An3 
	.byte	W06
	.byte	PEND
	.byte		EOT   , Bn1 
	.byte		N01   , En1 
	.byte		N01   , Gn2 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N36   , Bn1 
	.byte		N36   , Dn3 
	.byte	W24
	.byte		N12   , En3 
	.byte	W12
	.byte		N01   , En1 
	.byte		N01   , Gn2 
	.byte		N01   , En3 
	.byte	W12
	.byte		N36   , Gn1 
	.byte		N36   , Bn2 
	.byte	W12
@ 208   ----------------------------------------
mus_custom_flockofbirds_10_208:
	.byte	W12
	.byte		N12   , Fs3 , v096
	.byte	W12
	.byte		N01   , En1 
	.byte		N01   , Gn2 
	.byte		N01   , En3 
	.byte	W10
	.byte		        Fs3 , v127
	.byte	W02
	.byte		N18   , En3 , v096
	.byte	W18
	.byte		        Dn3 
	.byte	W18
	.byte		N12   , Bn2 
	.byte	W12
	.byte		        Cs3 
	.byte	W12
	.byte	PEND
@ 209   ----------------------------------------
mus_custom_flockofbirds_10_209:
	.byte		N24   , An1 , v096
	.byte		N06   , Cs3 
	.byte	W06
	.byte		N18   , Dn3 
	.byte	W06
	.byte		N12   , En3 
	.byte	W06
	.byte		N06   , An3 
	.byte	W06
	.byte		N01   , En1 
	.byte		N01   , Gn2 
	.byte		N01   , En3 
	.byte	W12
	.byte		N36   , Bn1 
	.byte		N36   , Dn3 
	.byte	W24
	.byte		N12   , En3 
	.byte	W12
	.byte		N01   , En1 
	.byte		N01   , Gn2 
	.byte		N01   , En3 
	.byte	W12
	.byte		N54   , Dn2 
	.byte		N78   , Gn3 
	.byte	W12
	.byte	PEND
@ 210   ----------------------------------------
mus_custom_flockofbirds_10_210:
	.byte	W12
	.byte		N30   , Dn4 , v096
	.byte	W24
	.byte		        Cs4 
	.byte	W06
	.byte		N24   , En1 
	.byte	W12
	.byte		N12   , Dn4 
	.byte	W12
	.byte		N06   , Fs1 
	.byte	W06
	.byte		N24   , Fs4 
	.byte	W24
	.byte	PEND
@ 211   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_203
@ 212   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_204
@ 213   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_205
@ 214   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_206
@ 215   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_207
	.byte		EOT   , Bn1 
	.byte		N01   , En1 , v096
	.byte		N01   , Gn2 
	.byte		N06   , Bn3 
	.byte	W12
	.byte		N36   , Bn1 
	.byte		N36   , Dn3 
	.byte	W24
	.byte		N12   , En3 
	.byte	W12
	.byte		N01   , En1 
	.byte		N01   , Gn2 
	.byte		N01   , En3 
	.byte	W12
	.byte		N36   , Gn1 
	.byte		N36   , Bn2 
	.byte	W12
@ 216   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_208
@ 217   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_209
@ 218   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_10_210
@ 219   ----------------------------------------
	.byte		N96   , Gn1 , v127
	.byte	W01
	.byte		N92   , Dn2 , v096, gtp2
	.byte	W02
	.byte		        Bn2 , v096, gtp1
	.byte	W01
	.byte		N90   , Cs3 , v096, gtp1
	.byte	W02
	.byte		        An3 
	.byte	W90
@ 220   ----------------------------------------
	.byte	FINE

@**************** Track 11 (Midi-Chn.13) ****************@

mus_custom_flockofbirds_11:
	.byte	KEYSH , mus_custom_flockofbirds_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 10
	.byte		VOL   , 46*mus_custom_flockofbirds_mvl/mxv
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
	.byte	W96
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
mus_custom_flockofbirds_11_091:
	.byte		N12   , Fs4 , v096
	.byte	W12
	.byte		N12   
	.byte	W12
	.byte		        Bn3 
	.byte	W12
	.byte		        As4 
	.byte	W18
	.byte		N18   
	.byte	W18
	.byte		N06   , Fs4 
	.byte	W06
	.byte		        En4 
	.byte	W06
	.byte		N48   , Ds4 
	.byte	W12
	.byte	PEND
@ 092   ----------------------------------------
mus_custom_flockofbirds_11_092:
	.byte	W36
	.byte		N18   , Cs4 , v096
	.byte	W18
	.byte		        Bn3 
	.byte	W18
	.byte		N24   , Fs3 
	.byte	W24
	.byte	PEND
@ 093   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_11_091
@ 094   ----------------------------------------
mus_custom_flockofbirds_11_094:
	.byte	W36
	.byte		N48   , As3 , v096
	.byte		N48   , Cs4 
	.byte	W60
	.byte	PEND
@ 095   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_11_091
@ 096   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_11_092
@ 097   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_11_091
@ 098   ----------------------------------------
	.byte	W36
	.byte		N48   , Cs4 , v096
	.byte	W60
@ 099   ----------------------------------------
	.byte	W96
@ 100   ----------------------------------------
	.byte	W96
@ 101   ----------------------------------------
	.byte	W96
@ 102   ----------------------------------------
	.byte	W96
@ 103   ----------------------------------------
	.byte	W96
@ 104   ----------------------------------------
	.byte	W96
@ 105   ----------------------------------------
	.byte	W96
@ 106   ----------------------------------------
	.byte	W96
@ 107   ----------------------------------------
	.byte	W96
@ 108   ----------------------------------------
	.byte	W96
@ 109   ----------------------------------------
	.byte	W96
@ 110   ----------------------------------------
	.byte	W96
@ 111   ----------------------------------------
	.byte	W96
@ 112   ----------------------------------------
	.byte	W96
@ 113   ----------------------------------------
	.byte	W96
@ 114   ----------------------------------------
	.byte	W96
@ 115   ----------------------------------------
	.byte	W96
@ 116   ----------------------------------------
	.byte	W96
@ 117   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_11_091
@ 118   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_11_092
@ 119   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_11_091
@ 120   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_11_094
@ 121   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_11_091
@ 122   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_11_092
@ 123   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_11_091
@ 124   ----------------------------------------
	.byte	W36
	.byte		N48   , Cs4 , v096
	.byte	W48
	.byte	FINE

@**************** Track 12 (Midi-Chn.15) ****************@

mus_custom_flockofbirds_12:
	.byte	KEYSH , mus_custom_flockofbirds_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 8
	.byte		VOL   , 69*mus_custom_flockofbirds_mvl/mxv
	.byte		PAN   , c_v+51
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
	.byte	W96
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
mus_custom_flockofbirds_12_091:
	.byte		N12   , Fs4 , v096
	.byte	W12
	.byte		N12   
	.byte	W12
	.byte		        Bn3 
	.byte	W12
	.byte		        As4 
	.byte	W18
	.byte		N18   
	.byte	W18
	.byte		N06   , Fs4 
	.byte	W06
	.byte		        En4 
	.byte	W06
	.byte		N48   , Ds4 
	.byte	W12
	.byte	PEND
@ 092   ----------------------------------------
mus_custom_flockofbirds_12_092:
	.byte	W36
	.byte		N18   , Cs4 , v096
	.byte	W18
	.byte		        Bn3 
	.byte	W18
	.byte		N24   , Fs3 
	.byte	W24
	.byte	PEND
@ 093   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_12_091
@ 094   ----------------------------------------
mus_custom_flockofbirds_12_094:
	.byte	W36
	.byte		N48   , As3 , v096
	.byte		N48   , Cs4 
	.byte	W60
	.byte	PEND
@ 095   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_12_091
@ 096   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_12_092
@ 097   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_12_091
@ 098   ----------------------------------------
	.byte	W36
	.byte		N48   , Cs4 , v096
	.byte	W60
@ 099   ----------------------------------------
	.byte	W96
@ 100   ----------------------------------------
	.byte	W96
@ 101   ----------------------------------------
	.byte	W96
@ 102   ----------------------------------------
	.byte	W96
@ 103   ----------------------------------------
	.byte	W96
@ 104   ----------------------------------------
	.byte	W96
@ 105   ----------------------------------------
	.byte	W96
@ 106   ----------------------------------------
	.byte	W96
@ 107   ----------------------------------------
	.byte	W96
@ 108   ----------------------------------------
	.byte	W96
@ 109   ----------------------------------------
	.byte	W96
@ 110   ----------------------------------------
	.byte	W96
@ 111   ----------------------------------------
	.byte	W96
@ 112   ----------------------------------------
	.byte	W96
@ 113   ----------------------------------------
	.byte	W96
@ 114   ----------------------------------------
	.byte	W96
@ 115   ----------------------------------------
	.byte	W96
@ 116   ----------------------------------------
	.byte	W96
@ 117   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_12_091
@ 118   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_12_092
@ 119   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_12_091
@ 120   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_12_094
@ 121   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_12_091
@ 122   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_12_092
@ 123   ----------------------------------------
	.byte	PATT
	 .word	mus_custom_flockofbirds_12_091
@ 124   ----------------------------------------
	.byte	W36
	.byte		N48   , Cs4 , v096
	.byte	W48
	.byte	FINE

@******************************************************@
	.align	2

mus_custom_flockofbirds:
	.byte	12	@ NumTrks
	.byte	0	@ NumBlks
	.byte	mus_custom_flockofbirds_pri	@ Priority
	.byte	mus_custom_flockofbirds_rev	@ Reverb.

	.word	mus_custom_flockofbirds_grp

	.word	mus_custom_flockofbirds_1
	.word	mus_custom_flockofbirds_2
	.word	mus_custom_flockofbirds_3
	.word	mus_custom_flockofbirds_4
	.word	mus_custom_flockofbirds_5
	.word	mus_custom_flockofbirds_6
	.word	mus_custom_flockofbirds_7
	.word	mus_custom_flockofbirds_8
	.word	mus_custom_flockofbirds_9
	.word	mus_custom_flockofbirds_10
	.word	mus_custom_flockofbirds_11
	.word	mus_custom_flockofbirds_12

	.end
