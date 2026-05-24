	.include "MPlayDef.s"

	.equ	mus_casino_plus_2_grp, voicegroup162
	.equ	mus_casino_plus_2_pri, 0
	.equ	mus_casino_plus_2_rev, reverb_set+50
	.equ	mus_casino_plus_2_mvl, 96
	.equ	mus_casino_plus_2_key, 0
	.equ	mus_casino_plus_2_tbs, 1
	.equ	mus_casino_plus_2_exg, 1
	.equ	mus_casino_plus_2_cmp, 1

	.section .rodata
	.global	mus_casino_plus_2
	.align	2

@**************** Track 1 (Midi-Chn.1) ****************@

mus_casino_plus_2_1:
	.byte	KEYSH , mus_casino_plus_2_key+0
@ 000   ----------------------------------------
	.byte	TEMPO , 120*mus_casino_plus_2_tbs/2
	.byte		VOICE , 33
	.byte		VOL   , 127*mus_casino_plus_2_mvl/mxv
	.byte		        64*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-13
	.byte		        c_v+21
	.byte		        c_v+0
	.byte		N01   , Cn0 , v127
	.byte		N02   , Fs0 
	.byte	W01
	.byte		PAN   , c_v+0
	.byte	W09
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N02   , Cs1 
	.byte	W05
	.byte		BEND  , c_v+63
	.byte		N02   
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		        c_v+32
	.byte		N09   , Ds1 
	.byte	W14
	.byte		BEND  , c_v+0
	.byte		        c_v-33
	.byte		N02   , En1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N02   , Cs1 
	.byte	W09
	.byte		BEND  , c_v+24
	.byte		        c_v+0
	.byte		N02   , Fs0 
	.byte	W05
	.byte		N02   
	.byte	W10
	.byte		N09   
	.byte	W14
	.byte		BEND  , c_v+32
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v-7
	.byte		        c_v+0
	.byte		N02   , Gs0 
	.byte	W09
@ 001   ----------------------------------------
	.byte	W06
	.byte		BEND  , c_v+63
	.byte		N02   
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N04   , As0 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N02   , Bn0 
	.byte	W05
	.byte		N02   
	.byte	W04
	.byte		BEND  , c_v-50
	.byte		        c_v+0
	.byte		N02   , Fs0 
	.byte	W05
	.byte		BEND  , c_v+40
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W10
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W09
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		BEND  , c_v+8
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W10
	.byte		N02   
	.byte	W04
	.byte		N02   
	.byte	W04
@ 002   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v-18
	.byte		        c_v-1
	.byte		N02   , As0 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N02   , Ds1 
	.byte	W05
	.byte		BEND  , c_v+15
	.byte		        c_v-1
	.byte		N04   , As1 
	.byte	W10
	.byte		BEND  , c_v-64
	.byte		N02   
	.byte	W04
	.byte		BEND  , c_v+0
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W10
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N02   , En1 
	.byte	W02
mus_casino_plus_2_1_B1:
	.byte	W03
	.byte		BEND  , c_v-33
	.byte		N04   , En1 , v127
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N02   , Ds1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , Cn1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , Ds1 
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , An1 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N04   , En1 
	.byte	W10
	.byte		BEND  , c_v-33
	.byte		N02   
	.byte	W03
@ 003   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N09   , Cs1 
	.byte	W14
	.byte		BEND  , c_v+0
	.byte		N09   , En1 
	.byte	W15
	.byte		BEND  , c_v-61
	.byte		        c_v+0
	.byte		N09   , Gs1 
	.byte	W14
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N09   , En1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		N04   , Cs1 
	.byte	W09
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+46
	.byte		        c_v-1
	.byte		N02   , As0 
	.byte	W05
	.byte		BEND  , c_v-37
	.byte		        c_v-1
	.byte		N02   , Cs1 
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W07
@ 004   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v+14
	.byte		        c_v-1
	.byte		N02   , Cs1 
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N02   , As1 
	.byte	W04
	.byte		BEND  , c_v+14
	.byte		        c_v-1
	.byte		N04   , Cs1 
	.byte	W10
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , As1 
	.byte	W04
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N04   , Cs2 
	.byte	W10
	.byte		BEND  , c_v+15
	.byte		        c_v-1
	.byte		N02   , As1 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		N04   
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N02   , An1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , En2 
	.byte	W10
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N02   , Bn1 
	.byte	W02
@ 005   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N02   , En2 
	.byte	W04
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N02   , Bn1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Gn1 
	.byte	W10
	.byte		BEND  , c_v-33
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-9
	.byte		        c_v+0
	.byte		N04   , En1 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N02   , Cs1 
	.byte	W05
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N09   , Bn0 
	.byte	W15
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N09   , Ds1 
	.byte	W14
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N09   , Fs1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		N09   , As1 
	.byte	W11
@ 006   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn0 
	.byte	W10
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W04
	.byte		BEND  , c_v-50
	.byte		        c_v+0
	.byte		N02   , Fs0 
	.byte	W05
	.byte		BEND  , c_v+40
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W10
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W04
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W10
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		BEND  , c_v+8
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W10
	.byte		N02   
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-18
	.byte		        c_v-1
	.byte		N02   , As0 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N02   , Ds1 
	.byte	W05
	.byte		BEND  , c_v+15
	.byte		        c_v-1
	.byte		N04   , As1 
	.byte	W06
@ 007   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v-64
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W10
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N02   , En1 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		N04   
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N02   , Ds1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , Cn1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , Ds1 
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , An1 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N04   , En1 
	.byte	W10
	.byte		BEND  , c_v-33
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N09   , Cs1 
	.byte	W14
	.byte		BEND  , c_v+0
	.byte		N09   , En1 
	.byte	W01
@ 008   ----------------------------------------
	.byte	W14
	.byte		BEND  , c_v-61
	.byte		        c_v+0
	.byte		N09   , Gs1 
	.byte	W14
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N09   , En1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		N04   , Cs1 
	.byte	W09
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+46
	.byte		        c_v-1
	.byte		N02   , As0 
	.byte	W05
	.byte		BEND  , c_v-37
	.byte		        c_v-1
	.byte		N02   , Cs1 
	.byte	W04
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W10
	.byte		BEND  , c_v+14
	.byte		        c_v-1
	.byte		N02   , Cs1 
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W10
@ 009   ----------------------------------------
	.byte		BEND  , c_v-1
	.byte		N02   , As1 
	.byte	W04
	.byte		BEND  , c_v+14
	.byte		        c_v-1
	.byte		N04   , Cs1 
	.byte	W10
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		N02   , As1 
	.byte	W05
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N04   , Cs2 
	.byte	W10
	.byte		BEND  , c_v+15
	.byte		        c_v-1
	.byte		N02   , As1 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		N04   
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N02   , An1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , As1 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-5
	.byte		        c_v-1
	.byte		N09   , Cn2 
	.byte	W09
	.byte		BEND  , c_v+31
	.byte		N14   
	.byte	W10
@ 010   ----------------------------------------
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn1 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		N04   
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		        c_v-48
	.byte		        c_v-1
	.byte		N02   , As0 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v-2
	.byte		N04   , Fs2 
	.byte	W10
	.byte		BEND  , c_v-9
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		N07   
	.byte	W14
	.byte		BEND  , c_v+0
	.byte		N09   , Gs1 
	.byte	W14
	.byte		BEND  , c_v+31
	.byte		N09   
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N04   , An1 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N02   , As1 
	.byte	W04
@ 011   ----------------------------------------
	.byte		BEND  , c_v-1
	.byte		N09   , Gn1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		N09   , As1 
	.byte	W14
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N09   , Ds2 
	.byte	W15
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N09   , Gs1 
	.byte	W14
	.byte		BEND  , c_v-33
	.byte		N09   
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N09   , Gn1 
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N09   , Fs1 
	.byte	W09
@ 012   ----------------------------------------
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		        c_v+63
	.byte		N09   , Fn1 
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		        c_v+8
	.byte		        c_v-1
	.byte		N02   , Ds1 
	.byte	W10
	.byte		BEND  , c_v-52
	.byte		        c_v-1
	.byte		N04   , Gn1 
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		N04   , As1 
	.byte	W15
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N09   , Gs1 
	.byte	W14
	.byte		BEND  , c_v-33
	.byte		N09   
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N09   , Gn1 
	.byte	W04
@ 013   ----------------------------------------
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N09   , Fs1 
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		        c_v-9
	.byte		        c_v+0
	.byte		N04   , En1 
	.byte	W10
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W05
	.byte		BEND  , c_v+5
	.byte		        c_v+0
	.byte		N02   , En1 
	.byte	W04
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-41
	.byte		        c_v+0
	.byte		N14   , Gs1 
	.byte	W28
	.byte	W01
	.byte		BEND  , c_v-1
	.byte		N04   , Fs1 
	.byte	W10
	.byte		N02   
	.byte	W03
@ 014   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v+14
	.byte		        c_v-1
	.byte		N02   , Cs1 
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W04
	.byte		BEND  , c_v+14
	.byte		        c_v-1
	.byte		N02   , Cs1 
	.byte	W05
	.byte		BEND  , c_v+15
	.byte		        c_v-1
	.byte		N14   , As1 
	.byte	W28
	.byte	W01
	.byte		BEND  , c_v-24
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W10
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W04
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N02   , Ds1 
	.byte	W05
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N09   , Fs1 
	.byte	W10
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N04   , En1 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		N09   
	.byte	W07
@ 015   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		        c_v-12
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W07
	.byte		VOL   , 45*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-41
	.byte		        c_v+0
	.byte		N02   , Gs1 
	.byte	W03
	.byte		VOL   , 64*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		N19   
	.byte	W19
	.byte		BEND  , c_v-1
	.byte		        c_v-32
	.byte		N04   , An1 
	.byte	W14
	.byte		BEND  , c_v+0
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		N04   , As1 
	.byte	W10
	.byte		N02   
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		N09   , Gn1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		N09   , As1 
	.byte	W02
@ 016   ----------------------------------------
	.byte	W12
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N09   , Ds2 
	.byte	W15
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N09   , Gs1 
	.byte	W14
	.byte		BEND  , c_v-33
	.byte		N09   
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N09   , Gn1 
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N09   , Fs1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		        c_v+63
	.byte		N09   , Fn1 
	.byte	W11
@ 017   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		        c_v+8
	.byte		        c_v-1
	.byte		N02   , Ds1 
	.byte	W10
	.byte		BEND  , c_v-52
	.byte		        c_v-1
	.byte		N04   , Gn1 
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		N04   , As1 
	.byte	W15
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W04
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N09   , Gs1 
	.byte	W15
	.byte		BEND  , c_v-33
	.byte		N09   
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N09   , Gn1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N09   , Fs1 
	.byte	W06
@ 018   ----------------------------------------
	.byte	W08
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N04   , Bn1 
	.byte	W10
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N02   , En1 
	.byte	W05
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N02   , Bn1 
	.byte	W04
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N02   , En1 
	.byte	W05
	.byte		BEND  , c_v-61
	.byte		        c_v+0
	.byte		N14   , Gs1 
	.byte	W28
	.byte	W01
	.byte		BEND  , c_v-1
	.byte		N04   , Bn1 
	.byte	W10
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , Fn1 
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		N02   , Bn1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , Fn1 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		N09   , Gs1 
	.byte	W01
@ 019   ----------------------------------------
	.byte	W09
	.byte		BEND  , c_v-33
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v+32
	.byte		N09   , Gn1 
	.byte	W09
	.byte		BEND  , c_v+0
	.byte		        c_v+31
	.byte		N04   , Gs1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W10
	.byte		N02   
	.byte	W04
	.byte		BEND  , c_v-33
	.byte		N09   
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		        c_v-9
	.byte		        c_v+0
	.byte		N09   , En1 
	.byte	W14
	.byte		BEND  , c_v-33
	.byte		N09   
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N09   , Cs1 
	.byte	W10
@ 020   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N09   , Bn0 
	.byte	W15
	.byte		BEND  , c_v-33
	.byte		N09   
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		        c_v-37
	.byte		        c_v-1
	.byte		N09   , Cs1 
	.byte	W15
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W09
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N02   , Cs2 
	.byte	W05
	.byte		BEND  , c_v+63
	.byte		N02   
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N09   , Ds2 
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N02   , En2 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N02   , Cs2 
	.byte	W05
@ 021   ----------------------------------------
	.byte	W05
	.byte		BEND  , c_v+23
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		N02   
	.byte	W09
	.byte		N09   
	.byte	W15
	.byte		BEND  , c_v+31
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v+32
	.byte		N02   , Gn1 
	.byte	W14
	.byte		BEND  , c_v+0
	.byte		        c_v+63
	.byte		N02   , Gs1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn0 
	.byte	W09
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-50
	.byte		        c_v+0
	.byte		N02   , Fs0 
	.byte	W05
	.byte		BEND  , c_v+40
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W04
@ 022   ----------------------------------------
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W10
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W10
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W04
	.byte		BEND  , c_v+8
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W10
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-18
	.byte		        c_v-1
	.byte		N02   , As0 
	.byte	W04
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N02   , Ds1 
	.byte	W05
	.byte		BEND  , c_v+15
	.byte		        c_v-1
	.byte		N04   , As1 
	.byte	W10
	.byte		BEND  , c_v-64
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W09
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N02   , En1 
	.byte	W03
	.byte	GOTO
	 .word	mus_casino_plus_2_1_B1
mus_casino_plus_2_1_B2:
	.byte	W02
	.byte		BEND  , c_v-33
	.byte		N04   , En1 , v127
	.byte	W09
@ 023   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v-1
	.byte		N02   , Ds1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , Cn1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , Ds1 
	.byte	W04
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , An1 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N04   , En1 
	.byte	W09
	.byte		BEND  , c_v-33
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N09   , Cs1 
	.byte	W15
	.byte		BEND  , c_v+0
	.byte		N09   , En1 
	.byte	W14
	.byte		BEND  , c_v-61
	.byte		        c_v+0
	.byte		N09   , Gs1 
	.byte	W15
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N09   , En1 
	.byte	W03
@ 024   ----------------------------------------
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		N04   , Cs1 
	.byte	W10
	.byte		N02   
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+46
	.byte		        c_v-1
	.byte		N02   , As0 
	.byte	W05
	.byte		BEND  , c_v-37
	.byte		        c_v-1
	.byte		N02   , Cs1 
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W10
	.byte		BEND  , c_v+14
	.byte		        c_v-1
	.byte		N02   , Cs1 
	.byte	W04
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N02   , As1 
	.byte	W05
	.byte		BEND  , c_v+14
	.byte		        c_v-1
	.byte		N04   , Cs1 
	.byte	W09
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , As1 
	.byte	W03
@ 025   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N04   , Cs2 
	.byte	W09
	.byte		BEND  , c_v+15
	.byte		        c_v-1
	.byte		N02   , As1 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		N04   
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N02   , An1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , En2 
	.byte	W09
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N02   , Bn1 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N02   , En2 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N02   , Bn1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Gn1 
	.byte	W09
	.byte		BEND  , c_v-33
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-9
	.byte		        c_v+0
	.byte		N04   , En1 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N02   , Cs1 
	.byte	W05
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N09   , Bn0 
	.byte	W07
@ 026   ----------------------------------------
	.byte	W07
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N09   , Ds1 
	.byte	W14
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N09   , Fs1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		N09   , As1 
	.byte	W14
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn0 
	.byte	W10
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-50
	.byte		        c_v+0
	.byte		N02   , Fs0 
	.byte	W05
	.byte		BEND  , c_v+40
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W04
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W10
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W02
@ 027   ----------------------------------------
	.byte	W07
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		BEND  , c_v+8
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W10
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-18
	.byte		        c_v-1
	.byte		N02   , As0 
	.byte	W04
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N02   , Ds1 
	.byte	W05
	.byte		BEND  , c_v+15
	.byte		        c_v-1
	.byte		N04   , As1 
	.byte	W10
	.byte		BEND  , c_v-64
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W09
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N02   , En1 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		N04   
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N02   , Ds1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , Cn1 
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		N02   , Ds1 
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W02
@ 028   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N04   , An1 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N04   , En1 
	.byte	W09
	.byte		BEND  , c_v-33
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N09   , Cs1 
	.byte	W14
	.byte		BEND  , c_v+0
	.byte		N09   , En1 
	.byte	W15
	.byte		BEND  , c_v-61
	.byte		        c_v+0
	.byte		N09   , Gs1 
	.byte	W14
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N09   , En1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		N04   , Cs1 
	.byte	W06
@ 029   ----------------------------------------
	.byte	W04
	.byte		N02   
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+46
	.byte		        c_v-1
	.byte		N02   , As0 
	.byte	W05
	.byte		BEND  , c_v-37
	.byte		        c_v-1
	.byte		N02   , Cs1 
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W09
	.byte		BEND  , c_v+14
	.byte		        c_v-1
	.byte		N02   , Cs1 
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N02   , As1 
	.byte	W05
	.byte		BEND  , c_v+14
	.byte		        c_v-1
	.byte		N04   , Cs1 
	.byte	W09
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , As1 
	.byte	W05
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N04   , Cs2 
	.byte	W09
	.byte		BEND  , c_v+15
	.byte		        c_v-1
	.byte		N02   , As1 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		N04   
	.byte	W01
@ 030   ----------------------------------------
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N02   , An1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , As1 
	.byte	W09
	.byte		BEND  , c_v+31
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-5
	.byte		        c_v-1
	.byte		N09   , Cn2 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		N14   
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn1 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		N04   
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		        c_v-48
	.byte		        c_v-1
	.byte		N02   , As0 
	.byte	W04
	.byte		BEND  , c_v+0
	.byte		        c_v-2
	.byte		N04   , Fs2 
	.byte	W10
	.byte		BEND  , c_v-9
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		N07   
	.byte	W10
@ 031   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v+0
	.byte		N09   , Gs1 
	.byte	W15
	.byte		BEND  , c_v+31
	.byte		N09   
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N04   , An1 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N02   , As1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Gn1 
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		N09   , As1 
	.byte	W15
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N09   , Ds2 
	.byte	W14
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N09   , Gs1 
	.byte	W05
@ 032   ----------------------------------------
	.byte	W10
	.byte		BEND  , c_v-33
	.byte		N09   
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N09   , Gn1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N09   , Fs1 
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		        c_v+63
	.byte		N09   , Fn1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		        c_v+8
	.byte		        c_v-1
	.byte		N02   , Ds1 
	.byte	W09
	.byte		BEND  , c_v-52
	.byte		        c_v-1
	.byte		N04   , Gn1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		N04   , As1 
	.byte	W04
@ 033   ----------------------------------------
	.byte	W10
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N09   , Gs1 
	.byte	W14
	.byte		BEND  , c_v-33
	.byte		N09   
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N09   , Gn1 
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N09   , Fs1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		        c_v-9
	.byte		        c_v+0
	.byte		N04   , En1 
	.byte	W09
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W05
	.byte		BEND  , c_v+5
	.byte		        c_v+0
	.byte		N02   , En1 
	.byte	W04
@ 034   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-41
	.byte		        c_v+0
	.byte		N14   , Gs1 
	.byte	W28
	.byte	W01
	.byte		BEND  , c_v-1
	.byte		N04   , Fs1 
	.byte	W09
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+14
	.byte		        c_v-1
	.byte		N02   , Cs1 
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		BEND  , c_v+14
	.byte		        c_v-1
	.byte		N02   , Cs1 
	.byte	W05
	.byte		BEND  , c_v+15
	.byte		        c_v-1
	.byte		N14   , As1 
	.byte	W28
	.byte	W01
	.byte		BEND  , c_v-24
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W03
@ 035   ----------------------------------------
	.byte	W06
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N02   , Ds1 
	.byte	W05
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W04
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N09   , Fs1 
	.byte	W10
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N04   , En1 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		N09   
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		        c_v-12
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W04
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W08
	.byte		VOL   , 45*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-41
	.byte		        c_v+0
	.byte		N02   , Gs1 
	.byte	W02
	.byte		VOL   , 64*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		N19   
	.byte	W19
	.byte		BEND  , c_v-1
	.byte		        c_v-32
	.byte		N04   , An1 
	.byte	W13
@ 036   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v+0
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		N04   , As1 
	.byte	W10
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Gn1 
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		N09   , As1 
	.byte	W15
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N09   , Ds2 
	.byte	W14
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N09   , Gs1 
	.byte	W15
	.byte		BEND  , c_v-33
	.byte		N09   
	.byte	W07
@ 037   ----------------------------------------
	.byte	W07
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N09   , Gn1 
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N09   , Fs1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		        c_v+63
	.byte		N09   , Fn1 
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		        c_v+8
	.byte		        c_v-1
	.byte		N02   , Ds1 
	.byte	W10
	.byte		BEND  , c_v-52
	.byte		        c_v-1
	.byte		N04   , Gn1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		N04   , As1 
	.byte	W14
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N09   , Gs1 
	.byte	W02
@ 038   ----------------------------------------
	.byte	W12
	.byte		BEND  , c_v-33
	.byte		N09   
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N09   , Gn1 
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N09   , Fs1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N04   , Bn1 
	.byte	W09
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N02   , En1 
	.byte	W05
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N02   , Bn1 
	.byte	W05
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N02   , En1 
	.byte	W05
	.byte		BEND  , c_v-61
	.byte		        c_v+0
	.byte		N14   , Gs1 
	.byte	W11
@ 039   ----------------------------------------
	.byte	W18
	.byte		BEND  , c_v-1
	.byte		N04   , Bn1 
	.byte	W09
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , Fn1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , Bn1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , Fn1 
	.byte	W04
	.byte		BEND  , c_v+0
	.byte		N09   , Gs1 
	.byte	W10
	.byte		BEND  , c_v-33
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v+32
	.byte		N09   , Gn1 
	.byte	W10
	.byte		BEND  , c_v+0
	.byte		        c_v+31
	.byte		N04   , Gs1 
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W10
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		N09   
	.byte	W06
@ 040   ----------------------------------------
	.byte	W08
	.byte		BEND  , c_v-1
	.byte		        c_v-9
	.byte		        c_v+0
	.byte		N09   , En1 
	.byte	W15
	.byte		BEND  , c_v-33
	.byte		N09   
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N09   , Cs1 
	.byte	W15
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N09   , Bn0 
	.byte	W14
	.byte		BEND  , c_v-33
	.byte		N09   
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		        c_v-37
	.byte		        c_v-1
	.byte		N09   , Cs1 
	.byte	W14
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W01
@ 041   ----------------------------------------
	.byte	W09
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N02   , Cs2 
	.byte	W05
	.byte		BEND  , c_v+63
	.byte		N02   
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N09   , Ds2 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N02   , En2 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N02   , Cs2 
	.byte	W09
	.byte		BEND  , c_v+23
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		N02   
	.byte	W10
	.byte		N09   
	.byte	W14
	.byte		BEND  , c_v+31
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v+32
	.byte		N02   , Gn1 
	.byte	W10
@ 042   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v+0
	.byte		        c_v+63
	.byte		N02   , Gs1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn0 
	.byte	W10
	.byte		N02   
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-50
	.byte		        c_v+0
	.byte		N02   , Fs0 
	.byte	W05
	.byte		BEND  , c_v+40
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W09
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W10
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		BEND  , c_v+8
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W09
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W05
@ 043   ----------------------------------------
	.byte		BEND  , c_v-18
	.byte		        c_v-1
	.byte		N02   , As0 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N02   , Ds1 
	.byte	W05
	.byte		BEND  , c_v+15
	.byte		        c_v-1
	.byte		N04   , As1 
	.byte	W09
	.byte		BEND  , c_v-64
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W10
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte	W02
	.byte	FINE

@**************** Track 2 (Midi-Chn.2) ****************@

mus_casino_plus_2_2:
	.byte	KEYSH , mus_casino_plus_2_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 1
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		        98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-13
	.byte		        c_v+46
	.byte		        c_v-1
	.byte		N01   , Cn1 , v127
	.byte		N09   , As2 
	.byte	W01
	.byte		PAN   , c_v+0
	.byte	W09
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		BEND  , c_v-5
	.byte		        c_v-1
	.byte		N09   , Cn3 
	.byte	W09
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Cs3 
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , Cn3 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N09   , Bn2 
	.byte	W09
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , As2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N09   
	.byte	W10
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+1
	.byte		        c_v-2
	.byte		N09   , Cs4 
	.byte	W09
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N09   
	.byte	W10
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N14   , As3 
	.byte	W09
@ 001   ----------------------------------------
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N14   , Fs3 
	.byte	W14
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N14   
	.byte	W15
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N09   , Ds3 
	.byte	W09
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N09   , Ds3 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N19   , Fs3 
	.byte	W17
	.byte		BEND  , c_v+0
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N14   
	.byte	W14
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N09   
	.byte	W04
@ 002   ----------------------------------------
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N09   , Fs3 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N19   , As3 
	.byte	W16
mus_casino_plus_2_2_B1:
	.byte		BEND  , c_v-4
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N14   , As3 , v127
	.byte	W14
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N09   , Fs3 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , An3 
	.byte	W09
	.byte		BEND  , c_v-2
	.byte		N04   , Fs3 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Ds3 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , Cn3 
	.byte	W03
@ 003   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N09   , Ds3 
	.byte	W09
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N09   , Cs3 
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N09   , Cn3 
	.byte	W09
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Cs3 
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N14   
	.byte	W14
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		N09   
	.byte	W10
	.byte		BEND  , c_v+15
	.byte		        c_v-1
	.byte		N04   , As2 
	.byte	W04
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N09   , Cs3 
	.byte	W08
@ 004   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N19   , En3 
	.byte	W16
	.byte		BEND  , c_v+0
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N14   
	.byte	W15
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N09   
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , Cs3 
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		N09   , En3 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N19   , Gs3 
	.byte	W15
	.byte		BEND  , c_v-3
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N14   
	.byte	W15
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N09   , Gn3 
	.byte	W02
@ 005   ----------------------------------------
	.byte	W07
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N04   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-2
	.byte		N09   , Gn3 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , En3 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Cs3 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N04   , En3 
	.byte	W05
	.byte		BEND  , c_v+62
	.byte		        c_v-2
	.byte		N09   , Fs3 
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N09   , Ds3 
	.byte	W09
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N09   , Fs3 
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N09   , As3 
	.byte	W09
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W02
@ 006   ----------------------------------------
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , Bn3 
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N09   , Ds3 
	.byte	W10
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N09   , Ds3 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N19   , Fs3 
	.byte	W14
	.byte		BEND  , c_v+0
	.byte	W04
	.byte		        c_v-3
	.byte	W01
	.byte		        c_v-2
	.byte		N09   , As3 
	.byte	W09
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N09   , Fs3 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N09   , Fs3 
	.byte	W06
@ 007   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v-2
	.byte		N19   , As3 
	.byte	W18
	.byte		BEND  , c_v+0
	.byte	W02
	.byte		        c_v-1
	.byte		N02   , Ds3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N07   
	.byte	W07
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N14   , An3 
	.byte	W15
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N14   , Fs3 
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		N14   , Ds3 
	.byte	W15
	.byte		N09   
	.byte	W09
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N09   , Cs3 
	.byte	W01
@ 008   ----------------------------------------
	.byte	W09
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N09   , Cn3 
	.byte	W09
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Cs3 
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N14   
	.byte	W15
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		N09   
	.byte	W10
	.byte		BEND  , c_v+15
	.byte		        c_v-1
	.byte		N04   , As2 
	.byte	W04
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N09   , Cs3 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N19   , En3 
	.byte	W15
@ 009   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-2
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N14   
	.byte	W15
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N09   
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N04   , Cs3 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , En3 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N19   , Gs3 
	.byte	W16
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v+62
	.byte		        c_v-2
	.byte		N09   , As3 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-7
	.byte		        c_v-2
	.byte		N09   , Cn4 
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N14   , Cs4 
	.byte	W10
@ 010   ----------------------------------------
	.byte	W05
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N04   , As3 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N04   , Cs3 
	.byte	W05
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N32   , Ds4 , v127, gtp1
	.byte	W15
	.byte		BEND  , c_v-4
	.byte	W04
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W04
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N24   
	.byte	W16
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W04
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N09   , Gn4 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Gs4 
	.byte	W04
@ 011   ----------------------------------------
	.byte		BEND  , c_v+62
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		N14   
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v-35
	.byte		        c_v-3
	.byte		N09   , Gn4 
	.byte	W10
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N04   , As3 
	.byte	W05
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N09   , Cs4 
	.byte	W09
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N09   , Cs4 
	.byte	W10
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N14   , Bn3 
	.byte	W14
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N14   , As3 
	.byte	W14
@ 012   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		        c_v-3
	.byte		N09   , Gn4 
	.byte	W09
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v+62
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		BEND  , c_v-4
	.byte		N14   , Cs5 
	.byte	W14
	.byte		BEND  , c_v-2
	.byte		N04   , As4 
	.byte	W05
	.byte		N09   
	.byte	W10
	.byte		BEND  , c_v-3
	.byte		N04   , Gn4 
	.byte	W05
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N09   , As3 
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N09   , As3 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N14   , Gs3 
	.byte	W08
@ 013   ----------------------------------------
	.byte	W06
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N14   , Gn3 
	.byte	W15
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Gs3 
	.byte	W04
	.byte		BEND  , c_v-2
	.byte		N32   , Bn3 , v127, gtp1
	.byte	W15
	.byte		BEND  , c_v+0
	.byte	W04
	.byte		        c_v-4
	.byte	W04
	.byte		        c_v+0
	.byte	W04
	.byte		        c_v-4
	.byte	W04
	.byte		        c_v+0
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N04   , En3 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N09   , Bn3 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N04   , Gs3 
	.byte	W05
	.byte		BEND  , c_v+62
	.byte		        c_v-2
	.byte		N19   , As3 
	.byte	W13
@ 014   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-4
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N19   , Gs3 
	.byte	W15
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-3
	.byte	W01
	.byte		        c_v+62
	.byte		        c_v-2
	.byte		N14   , As3 
	.byte	W14
	.byte		BEND  , c_v-2
	.byte		N32   , Fs3 , v127, gtp1
	.byte	W18
	.byte		BEND  , c_v+0
	.byte	W04
	.byte		        c_v-3
	.byte	W04
	.byte		        c_v+0
	.byte	W04
	.byte		        c_v-3
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N14   , En3 
	.byte	W12
@ 015   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N28   , Ds4 
	.byte	W14
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W04
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N09   
	.byte	W10
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N14   , En4 
	.byte	W14
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Gn4 
	.byte	W09
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v+62
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		N14   
	.byte	W07
@ 016   ----------------------------------------
	.byte	W07
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v-35
	.byte		        c_v-3
	.byte		N09   , Gn4 
	.byte	W10
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N04   , As3 
	.byte	W05
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N09   , Cs4 
	.byte	W09
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N09   , Cs4 
	.byte	W10
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N14   , Bn3 
	.byte	W14
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N14   , As3 
	.byte	W15
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		        c_v-3
	.byte		N09   , Gn4 
	.byte	W09
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Gs4 
	.byte	W02
@ 017   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v+62
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		BEND  , c_v-4
	.byte		N14   , Cs5 
	.byte	W14
	.byte		BEND  , c_v-2
	.byte		N04   , As4 
	.byte	W05
	.byte		N09   
	.byte	W10
	.byte		BEND  , c_v-3
	.byte		N04   , Gn4 
	.byte	W04
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N09   , As3 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N09   , As3 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N14   , Gs3 
	.byte	W14
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N14   , Gn3 
	.byte	W11
@ 018   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Gs3 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N32   , En3 , v127, gtp1
	.byte	W16
	.byte		BEND  , c_v+0
	.byte	W04
	.byte		        c_v-2
	.byte	W04
	.byte		        c_v+0
	.byte	W04
	.byte		        c_v-2
	.byte	W04
	.byte		        c_v+0
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v+62
	.byte		        c_v-2
	.byte		N09   , Fs3 
	.byte	W09
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N04   , Gs3 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N19   , Fn3 
	.byte	W17
	.byte		BEND  , c_v-3
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N19   , En3 
	.byte	W06
@ 019   ----------------------------------------
	.byte	W10
	.byte		BEND  , c_v+0
	.byte	W04
	.byte		        c_v+30
	.byte		        c_v-2
	.byte		N14   , Fn3 
	.byte	W14
	.byte		BEND  , c_v-2
	.byte		N42   , As3 , v127, gtp1
	.byte	W15
	.byte		BEND  , c_v-4
	.byte	W04
	.byte		        c_v+0
	.byte	W04
	.byte		        c_v-4
	.byte	W04
	.byte		        c_v+0
	.byte	W04
	.byte		        c_v-4
	.byte	W04
	.byte		        c_v+0
	.byte	W04
	.byte		        c_v-4
	.byte	W04
	.byte		        c_v-1
	.byte		N04   , Gs3 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N09   
	.byte	W10
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N09   , Fs3 
	.byte	W10
@ 020   ----------------------------------------
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N14   , Cs4 
	.byte	W14
	.byte		BEND  , c_v-4
	.byte		N24   , Cs5 
	.byte	W14
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-9
	.byte	W04
	.byte		        c_v+1
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N09   
	.byte	W10
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N09   , As3 
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-7
	.byte		        c_v-2
	.byte		N09   , Cn4 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , Cs4 
	.byte	W09
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N04   , Cn4 
	.byte	W05
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N09   , Bn3 
	.byte	W05
@ 021   ----------------------------------------
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N04   , As3 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N09   
	.byte	W09
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		        c_v-4
	.byte		N09   , Cs5 
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N09   
	.byte	W10
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N14   , As4 
	.byte	W14
	.byte		BEND  , c_v-3
	.byte		N14   , Fs4 
	.byte	W14
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N14   
	.byte	W15
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+35
	.byte		        c_v-1
	.byte		N09   , Ds3 
	.byte	W10
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W04
@ 022   ----------------------------------------
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N09   , Ds3 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N19   , Fs3 
	.byte	W17
	.byte		BEND  , c_v-3
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N14   
	.byte	W15
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		        c_v-2
	.byte		N09   
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N09   , Fs3 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N19   , As3 
	.byte	W16
	.byte		BEND  , c_v+0
	.byte	W01
	.byte	GOTO
	 .word	mus_casino_plus_2_2_B1
mus_casino_plus_2_2_B2:
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N14   , As3 , v127
	.byte	W09
@ 023   ----------------------------------------
	.byte	W06
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N09   , Fs3 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , An3 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N04   , Fs3 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Ds3 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N04   , Cn3 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Ds3 
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N09   , Cs3 
	.byte	W09
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N09   , Cn3 
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Cs3 
	.byte	W04
@ 024   ----------------------------------------
	.byte	W06
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N14   
	.byte	W14
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		N09   
	.byte	W10
	.byte		BEND  , c_v+15
	.byte		        c_v-1
	.byte		N04   , As2 
	.byte	W05
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N09   , Cs3 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N19   , En3 
	.byte	W16
	.byte		BEND  , c_v+0
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N14   
	.byte	W14
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N09   
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , Cs3 
	.byte	W03
@ 025   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N09   , En3 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N19   , Gs3 
	.byte	W16
	.byte		BEND  , c_v-3
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N14   
	.byte	W14
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N09   , Gn3 
	.byte	W10
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N04   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-2
	.byte		N09   , Gn3 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N04   , En3 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Cs3 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , En3 
	.byte	W05
	.byte		BEND  , c_v+62
	.byte		        c_v-2
	.byte		N09   , Fs3 
	.byte	W07
@ 026   ----------------------------------------
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N09   , Ds3 
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N09   , Fs3 
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N09   , As3 
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , Bn3 
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N09   , Ds3 
	.byte	W09
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N09   , Ds3 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N19   , Fs3 
	.byte	W07
@ 027   ----------------------------------------
	.byte	W07
	.byte		BEND  , c_v+0
	.byte	W04
	.byte		        c_v-3
	.byte	W01
	.byte		        c_v-2
	.byte		N09   , As3 
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N09   , Fs3 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N09   , Fs3 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N19   , As3 
	.byte	W17
	.byte		BEND  , c_v+0
	.byte	W02
	.byte		        c_v-1
	.byte		N02   , Ds3 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N07   
	.byte	W07
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N14   , An3 
	.byte	W14
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W02
@ 028   ----------------------------------------
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N14   , Fs3 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		N14   , Ds3 
	.byte	W14
	.byte		N09   
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N09   , Cs3 
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N09   , Cn3 
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Cs3 
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N14   
	.byte	W06
@ 029   ----------------------------------------
	.byte	W08
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		N09   
	.byte	W10
	.byte		BEND  , c_v+15
	.byte		        c_v-1
	.byte		N04   , As2 
	.byte	W05
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N09   , Cs3 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N19   , En3 
	.byte	W17
	.byte		BEND  , c_v-2
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N14   
	.byte	W14
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N09   
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , Cs3 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , En3 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N19   , Gs3 
	.byte	W06
@ 030   ----------------------------------------
	.byte	W10
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v+62
	.byte		        c_v-2
	.byte		N09   , As3 
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-7
	.byte		        c_v-2
	.byte		N09   , Cn4 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N14   , Cs4 
	.byte	W14
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N04   , As3 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N04   , Cs3 
	.byte	W04
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N32   , Ds4 , v127, gtp1
	.byte	W16
	.byte		BEND  , c_v-4
	.byte	W04
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W01
@ 031   ----------------------------------------
	.byte	W03
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N24   
	.byte	W16
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W04
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N09   , Gn4 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v+62
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W09
	.byte		N14   
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v-35
	.byte		        c_v-3
	.byte		N09   , Gn4 
	.byte	W09
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N04   , As3 
	.byte	W05
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N09   , Cs4 
	.byte	W05
@ 032   ----------------------------------------
	.byte	W05
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N09   , Cs4 
	.byte	W09
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N14   , Bn3 
	.byte	W15
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N14   , As3 
	.byte	W14
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		        c_v-3
	.byte		N09   , Gn4 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Gs4 
	.byte	W04
	.byte		BEND  , c_v+62
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		BEND  , c_v-4
	.byte		N14   , Cs5 
	.byte	W15
	.byte		BEND  , c_v-2
	.byte		N04   , As4 
	.byte	W04
@ 033   ----------------------------------------
	.byte		N09   
	.byte	W10
	.byte		BEND  , c_v-3
	.byte		N04   , Gn4 
	.byte	W05
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N09   , As3 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W04
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N09   , As3 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N14   , Gs3 
	.byte	W14
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N14   , Gn3 
	.byte	W15
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Gs3 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N32   , Bn3 , v127, gtp1
	.byte	W14
	.byte		BEND  , c_v+0
	.byte	W04
	.byte		        c_v-4
	.byte	W04
	.byte		        c_v+0
	.byte	W01
@ 034   ----------------------------------------
	.byte	W03
	.byte		        c_v-4
	.byte	W04
	.byte		        c_v+0
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N04   , En3 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N09   , Bn3 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , Gs3 
	.byte	W05
	.byte		BEND  , c_v+62
	.byte		        c_v-2
	.byte		N19   , As3 
	.byte	W15
	.byte		BEND  , c_v-4
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N19   , Gs3 
	.byte	W14
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-3
	.byte	W01
	.byte		        c_v+62
	.byte		        c_v-2
	.byte		N14   , As3 
	.byte	W14
	.byte		BEND  , c_v-2
	.byte		N32   , Fs3 , v127, gtp1
	.byte	W04
@ 035   ----------------------------------------
	.byte	W14
	.byte		BEND  , c_v+0
	.byte	W04
	.byte		        c_v-3
	.byte	W04
	.byte		        c_v+0
	.byte	W04
	.byte		        c_v-3
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N14   , En3 
	.byte	W15
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , Ds3 
	.byte	W04
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N28   , Ds4 
	.byte	W15
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W04
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N09   
	.byte	W10
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N14   , En4 
	.byte	W03
@ 036   ----------------------------------------
	.byte	W11
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Gn4 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v+62
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W09
	.byte		N14   
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v-35
	.byte		        c_v-3
	.byte		N09   , Gn4 
	.byte	W09
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N04   , As3 
	.byte	W05
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N09   , Cs4 
	.byte	W10
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N09   , Cs4 
	.byte	W07
@ 037   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N14   , Bn3 
	.byte	W15
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N14   , As3 
	.byte	W14
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		        c_v-3
	.byte		N09   , Gn4 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Gs4 
	.byte	W04
	.byte		BEND  , c_v+62
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		BEND  , c_v-4
	.byte		N14   , Cs5 
	.byte	W15
	.byte		BEND  , c_v-2
	.byte		N04   , As4 
	.byte	W04
	.byte		N09   
	.byte	W10
	.byte		BEND  , c_v-3
	.byte		N04   , Gn4 
	.byte	W05
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N09   , As3 
	.byte	W02
@ 038   ----------------------------------------
	.byte	W07
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N09   , As3 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N14   , Gs3 
	.byte	W14
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N14   , Gn3 
	.byte	W15
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Gs3 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N32   , En3 , v127, gtp1
	.byte	W16
	.byte		BEND  , c_v+0
	.byte	W04
	.byte		        c_v-2
	.byte	W04
	.byte		        c_v+0
	.byte	W04
	.byte		        c_v-2
	.byte	W04
	.byte		        c_v+0
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N04   
	.byte	W02
@ 039   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v+62
	.byte		        c_v-2
	.byte		N09   , Fs3 
	.byte	W10
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N04   , Gs3 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N19   , Fn3 
	.byte	W16
	.byte		BEND  , c_v-3
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N19   , En3 
	.byte	W16
	.byte		BEND  , c_v+0
	.byte	W03
	.byte		        c_v+30
	.byte		        c_v-2
	.byte		N14   , Fn3 
	.byte	W14
	.byte		BEND  , c_v-2
	.byte		N42   , As3 , v127, gtp1
	.byte	W16
	.byte		BEND  , c_v-4
	.byte	W04
	.byte		        c_v+0
	.byte	W01
@ 040   ----------------------------------------
	.byte	W03
	.byte		        c_v-4
	.byte	W04
	.byte		        c_v+0
	.byte	W04
	.byte		        c_v-4
	.byte	W04
	.byte		        c_v+0
	.byte	W04
	.byte		        c_v-4
	.byte	W04
	.byte		        c_v-1
	.byte		N04   , Gs3 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N09   
	.byte	W09
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N09   , Fs3 
	.byte	W10
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N14   , Cs4 
	.byte	W14
	.byte		BEND  , c_v-4
	.byte		N24   , Cs5 
	.byte	W15
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-9
	.byte	W04
	.byte		        c_v+1
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N09   
	.byte	W10
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N09   , As3 
	.byte	W01
@ 041   ----------------------------------------
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-7
	.byte		        c_v-2
	.byte		N09   , Cn4 
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , Cs4 
	.byte	W10
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N04   , Cn4 
	.byte	W05
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N09   , Bn3 
	.byte	W09
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N04   , As3 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N09   
	.byte	W10
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		        c_v-4
	.byte		N09   , Cs5 
	.byte	W09
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N09   
	.byte	W10
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N14   , As4 
	.byte	W10
@ 042   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v-3
	.byte		N14   , Fs4 
	.byte	W15
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N14   
	.byte	W14
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+35
	.byte		        c_v-1
	.byte		N09   , Ds3 
	.byte	W10
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N09   , Ds3 
	.byte	W09
	.byte		BEND  , c_v-2
	.byte		N19   , Fs3 
	.byte	W17
	.byte		BEND  , c_v-3
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N14   
	.byte	W14
	.byte		VOL   , 98*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		        c_v-2
	.byte		N09   
	.byte	W05
@ 043   ----------------------------------------
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N09   , Fs3 
	.byte	W09
	.byte		BEND  , c_v-2
	.byte	W16
	.byte		        c_v+0
	.byte	W01
	.byte	FINE

@**************** Track 3 (Midi-Chn.3) ****************@

mus_casino_plus_2_3:
	.byte	KEYSH , mus_casino_plus_2_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 1
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		        109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-13
	.byte		        c_v+32
	.byte		        c_v-2
	.byte		N01   , Cn1 , v127
	.byte		N09   , Fs3 
	.byte	W01
	.byte		PAN   , c_v+0
	.byte	W09
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N04   , Gs3 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , An3 
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , As3 
	.byte	W10
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , An3 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N09   , Gs3 
	.byte	W09
	.byte		BEND  , c_v-2
	.byte		N04   , Fs3 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N09   
	.byte	W10
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+15
	.byte		        c_v-3
	.byte		N09   , Fs4 
	.byte	W10
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N14   , En4 
	.byte	W09
@ 001   ----------------------------------------
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N14   , Cs4 
	.byte	W14
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-3
	.byte		N09   , Dn4 
	.byte	W09
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 
	.byte	W10
	.byte		BEND  , c_v-3
	.byte		N04   , Dn4 
	.byte	W04
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Dn4 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 
	.byte	W04
@ 002   ----------------------------------------
	.byte	W06
	.byte		BEND  , c_v-3
	.byte		N04   , Dn4 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W04
	.byte		BEND  , c_v-3
	.byte		N09   , Dn4 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W02
mus_casino_plus_2_3_B1:
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 , v127
	.byte	W09
	.byte		BEND  , c_v-3
	.byte		N04   , Dn4 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Dn4 
	.byte	W09
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , Ds4 
	.byte	W03
@ 003   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-3
	.byte		N02   , Fs4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N02   , Fs4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N04   , Fs4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W09
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , En4 
	.byte	W10
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cn4 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N02   , Cs4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N02   , As3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N02   , Cs4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N02   , As3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N02   , Cs4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N02   , As3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-2
	.byte		N09   , Cn4 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Cs4 
	.byte	W04
	.byte		BEND  , c_v-3
	.byte		N09   , Fs4 
	.byte	W08
@ 004   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-2
	.byte		N04   , Cn4 
	.byte	W05
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , Cs4 
	.byte	W10
	.byte		BEND  , c_v-3
	.byte		N04   , Fs4 
	.byte	W04
	.byte		BEND  , c_v-2
	.byte		N09   , Cn4 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Fs4 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N04   , Cn4 
	.byte	W04
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , Cs4 
	.byte	W10
	.byte		BEND  , c_v-3
	.byte		N04   , Fs4 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N09   , Cn4 
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Fs4 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N04   , Cn4 
	.byte	W05
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , Cs4 
	.byte	W02
@ 005   ----------------------------------------
	.byte	W07
	.byte		BEND  , c_v-3
	.byte		N04   , Fs4 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N09   , Cn4 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Fs4 
	.byte	W09
	.byte		BEND  , c_v-2
	.byte		N04   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-11
	.byte		        c_v-1
	.byte		N02   , En4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-11
	.byte		        c_v-1
	.byte		N02   , En4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N02   , Ds4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N02   , Ds4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-3
	.byte		N09   , Dn4 
	.byte	W10
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W09
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N02   
	.byte	W02
@ 006   ----------------------------------------
	.byte	W01
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-35
	.byte		        c_v-3
	.byte		N02   , Dn4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-3
	.byte		N09   , Dn4 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 
	.byte	W10
	.byte		BEND  , c_v-3
	.byte		N04   , Dn4 
	.byte	W04
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Dn4 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 
	.byte	W10
	.byte		BEND  , c_v-3
	.byte		N04   , Dn4 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W06
@ 007   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Dn4 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 
	.byte	W09
	.byte		BEND  , c_v-3
	.byte		N04   , Dn4 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Dn4 
	.byte	W09
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N02   , Fs4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N02   , Fs4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N04   , Fs4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W01
@ 008   ----------------------------------------
	.byte	W01
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W09
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , En4 
	.byte	W10
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cn4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N02   , Cs4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N02   , As3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N02   , Cs4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N02   , As3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N02   , Cs4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N02   , As3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-2
	.byte		N09   , Cn4 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Cs4 
	.byte	W04
	.byte		BEND  , c_v-3
	.byte		N09   , Fs4 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N04   , Cn4 
	.byte	W05
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , Cs4 
	.byte	W09
	.byte		BEND  , c_v-3
	.byte		N04   , Fs4 
	.byte	W01
@ 009   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v-2
	.byte		N09   , Cn4 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Fs4 
	.byte	W09
	.byte		BEND  , c_v-2
	.byte		N04   , Cn4 
	.byte	W05
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , Cs4 
	.byte	W10
	.byte		BEND  , c_v-3
	.byte		N04   , Fs4 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N09   , Cn4 
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Fs4 
	.byte	W10
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , An4 
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N14   , As4 
	.byte	W10
@ 010   ----------------------------------------
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N04   , Fs4 
	.byte	W04
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		        c_v-2
	.byte		N04   , Fs3 
	.byte	W05
	.byte		BEND  , c_v-52
	.byte		        c_v-2
	.byte		N09   , Bn4 
	.byte	W10
	.byte		VOL   , 87*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N02   , Fs2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 87*mus_casino_plus_2_mvl/mxv
	.byte		N07   
	.byte	W07
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 87*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N09   , Gs2 
	.byte	W10
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 87*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , An2 
	.byte	W10
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 87*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N02   , An4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W04
@ 011   ----------------------------------------
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N09   , Cs5 
	.byte	W10
	.byte		N14   
	.byte	W15
	.byte		BEND  , c_v-2
	.byte		N04   , Bn4 
	.byte	W04
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 87*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , An4 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N14   , Gs4 
	.byte	W14
	.byte		BEND  , c_v-35
	.byte		        c_v-3
	.byte		N14   , Gn4 
	.byte	W14
@ 012   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , Gs4 
	.byte	W02
	.byte		VOL   , 87*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , An4 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N09   , Cs5 
	.byte	W10
	.byte		BEND  , c_v-4
	.byte		N14   , En5 
	.byte	W14
	.byte		BEND  , c_v-36
	.byte		        c_v-4
	.byte		N04   , Ds5 
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		N09   , Cs5 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N04   , As4 
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		N09   , Cs5 
	.byte	W09
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N04   , Ds5 
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		N09   , Cs5 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N14   , Bn4 
	.byte	W08
@ 013   ----------------------------------------
	.byte	W06
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N14   , As4 
	.byte	W15
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		N32   , Gs4 , v127, gtp1
	.byte	W18
	.byte		BEND  , c_v+2
	.byte	W04
	.byte		        c_v-5
	.byte	W04
	.byte		        c_v+2
	.byte	W04
	.byte		        c_v-5
	.byte	W04
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N04   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N04   , En4 
	.byte	W05
	.byte		BEND  , c_v+61
	.byte		        c_v-3
	.byte		N19   , Fs4 
	.byte	W13
@ 014   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v+0
	.byte	W04
	.byte		        c_v-6
	.byte	W01
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N04   
	.byte	W04
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N19   , En4 
	.byte	W18
	.byte		BEND  , c_v+2
	.byte	W02
	.byte		        c_v+61
	.byte		        c_v-3
	.byte		N14   , Fs4 
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		N32   , Ds4 , v127, gtp1
	.byte	W17
	.byte		BEND  , c_v-4
	.byte	W04
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W04
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W01
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N14   , Cs4 
	.byte	W12
@ 015   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-2
	.byte		N28   , Bn4 
	.byte	W18
	.byte		BEND  , c_v+2
	.byte	W04
	.byte		        c_v-6
	.byte	W04
	.byte		        c_v+2
	.byte	W03
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N04   
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N14   , Cs5 
	.byte	W14
	.byte		BEND  , c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N09   , Cs5 
	.byte	W10
	.byte		N14   
	.byte	W07
@ 016   ----------------------------------------
	.byte	W07
	.byte		BEND  , c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 87*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , An4 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N14   , Gs4 
	.byte	W14
	.byte		BEND  , c_v-35
	.byte		        c_v-3
	.byte		N14   , Gn4 
	.byte	W15
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , Gs4 
	.byte	W02
	.byte		VOL   , 87*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , An4 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W02
@ 017   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N09   , Cs5 
	.byte	W10
	.byte		BEND  , c_v-4
	.byte		N14   , En5 
	.byte	W14
	.byte		BEND  , c_v-36
	.byte		        c_v-4
	.byte		N04   , Ds5 
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		N09   , Cs5 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N04   , As4 
	.byte	W04
	.byte		BEND  , c_v-4
	.byte		N09   , Cs5 
	.byte	W10
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N04   , Ds5 
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		N09   , Cs5 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N14   , Bn4 
	.byte	W14
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N14   , As4 
	.byte	W11
@ 018   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N32   , Gs4 , v127, gtp1
	.byte	W16
	.byte		BEND  , c_v-5
	.byte	W04
	.byte		        c_v+2
	.byte	W04
	.byte		        c_v-5
	.byte	W04
	.byte		        c_v+2
	.byte	W04
	.byte		        c_v-5
	.byte	W02
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v+62
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		N19   
	.byte	W16
	.byte		BEND  , c_v+2
	.byte	W03
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N19   , As4 
	.byte	W06
@ 019   ----------------------------------------
	.byte	W10
	.byte		BEND  , c_v-6
	.byte	W04
	.byte		        c_v+30
	.byte		        c_v-2
	.byte		N14   , Bn4 
	.byte	W14
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N42   , Cs5 , v127, gtp1
	.byte	W14
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-9
	.byte	W05
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-9
	.byte	W04
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-9
	.byte	W04
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-9
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
@ 020   ----------------------------------------
	.byte		BEND  , c_v-3
	.byte		N14   , Fs4 
	.byte	W14
	.byte		N24   , Fs5 
	.byte	W18
	.byte		BEND  , c_v+3
	.byte	W04
	.byte		        c_v-9
	.byte	W02
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		        c_v-3
	.byte		N04   
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		N09   , Fs4 
	.byte	W09
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , An4 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , An4 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N09   , Gs4 
	.byte	W05
@ 021   ----------------------------------------
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N04   , Fs4 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N09   
	.byte	W09
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		N09   , Fs5 
	.byte	W10
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-4
	.byte		N14   , En5 
	.byte	W14
	.byte		BEND  , c_v-4
	.byte		N14   , Cs5 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N02   , Ds4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N02   , Ds4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-3
	.byte		N09   , Dn4 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W04
@ 022   ----------------------------------------
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 
	.byte	W10
	.byte		BEND  , c_v-3
	.byte		N04   , Dn4 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W04
	.byte		BEND  , c_v-3
	.byte		N09   , Dn4 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 
	.byte	W09
	.byte		BEND  , c_v-3
	.byte		N04   , Dn4 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Dn4 
	.byte	W09
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W03
	.byte	GOTO
	 .word	mus_casino_plus_2_3_B1
mus_casino_plus_2_3_B2:
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 , v127
	.byte	W09
@ 023   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v-3
	.byte		N04   , Dn4 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Dn4 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N02   , Fs4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N02   , Fs4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N04   , Fs4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W10
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , En4 
	.byte	W04
@ 024   ----------------------------------------
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cn4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N02   , Cs4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N02   , As3 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N02   , Cs4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N02   , As3 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N02   , Cs4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N02   , As3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-2
	.byte		N09   , Cn4 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Fs4 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N04   , Cn4 
	.byte	W04
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , Cs4 
	.byte	W10
	.byte		BEND  , c_v-3
	.byte		N04   , Fs4 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N09   , Cn4 
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Fs4 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N04   , Cn4 
	.byte	W03
@ 025   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , Cs4 
	.byte	W09
	.byte		BEND  , c_v-3
	.byte		N04   , Fs4 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N09   , Cn4 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Fs4 
	.byte	W09
	.byte		BEND  , c_v-2
	.byte		N04   , Cn4 
	.byte	W05
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , Cs4 
	.byte	W10
	.byte		BEND  , c_v-3
	.byte		N04   , Fs4 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N09   , Cn4 
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Fs4 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N04   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-11
	.byte		        c_v-1
	.byte		N02   , En4 
	.byte	W03
@ 026   ----------------------------------------
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-11
	.byte		        c_v-1
	.byte		N02   , En4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-3
	.byte		N09   , Dn4 
	.byte	W10
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W10
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-35
	.byte		        c_v-3
	.byte		N02   , Dn4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , Ds4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N02   , Ds4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-3
	.byte		N09   , Dn4 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 
	.byte	W10
	.byte		BEND  , c_v-3
	.byte		N04   , Dn4 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W02
@ 027   ----------------------------------------
	.byte	W07
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Dn4 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 
	.byte	W09
	.byte		BEND  , c_v-3
	.byte		N04   , Dn4 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Dn4 
	.byte	W09
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 
	.byte	W10
	.byte		BEND  , c_v-3
	.byte		N04   , Dn4 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W02
@ 028   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v-3
	.byte		N09   , Dn4 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N02   , Fs4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N02   , Fs4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N04   , Fs4 
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cs4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W10
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , En4 
	.byte	W10
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Cn4 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N02   , Cs4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N02   , As3 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N02   , Cs4 
	.byte	W01
@ 029   ----------------------------------------
	.byte	W01
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N02   , As3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N02   , Cs4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N02   , As3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-2
	.byte		N09   , Cn4 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Fs4 
	.byte	W09
	.byte		BEND  , c_v-2
	.byte		N04   , Cn4 
	.byte	W05
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , Cs4 
	.byte	W10
	.byte		BEND  , c_v-3
	.byte		N04   , Fs4 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N09   , Cn4 
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Fs4 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N04   , Cn4 
	.byte	W05
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , Cs4 
	.byte	W09
	.byte		BEND  , c_v-3
	.byte		N04   , Fs4 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N09   , Cn4 
	.byte	W01
@ 030   ----------------------------------------
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Fs4 
	.byte	W09
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , An4 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N14   , As4 
	.byte	W14
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N04   , Fs4 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		        c_v-2
	.byte		N04   , Fs3 
	.byte	W04
	.byte		BEND  , c_v-52
	.byte		        c_v-2
	.byte		N09   , Bn4 
	.byte	W10
	.byte		VOL   , 87*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N02   , Fs2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 87*mus_casino_plus_2_mvl/mxv
	.byte		N07   
	.byte	W07
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W03
@ 031   ----------------------------------------
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 87*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N09   , Gs2 
	.byte	W10
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , An2 
	.byte	W09
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 87*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N02   , An4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N09   , Cs5 
	.byte	W09
	.byte		N14   
	.byte	W15
	.byte		BEND  , c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N02   , Ds4 
	.byte	W03
	.byte		VOL   , 87*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , An4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W05
@ 032   ----------------------------------------
	.byte	W05
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N14   , Gs4 
	.byte	W15
	.byte		BEND  , c_v-35
	.byte		        c_v-3
	.byte		N14   , Gn4 
	.byte	W14
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , Gs4 
	.byte	W03
	.byte		VOL   , 87*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , An4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N09   , Cs5 
	.byte	W09
	.byte		BEND  , c_v-4
	.byte		N14   , En5 
	.byte	W15
	.byte		BEND  , c_v-36
	.byte		        c_v-4
	.byte		N04   , Ds5 
	.byte	W04
@ 033   ----------------------------------------
	.byte		BEND  , c_v-4
	.byte		N09   , Cs5 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N04   , As4 
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		N09   , Cs5 
	.byte	W10
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N04   , Ds5 
	.byte	W04
	.byte		BEND  , c_v-4
	.byte		N09   , Cs5 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N14   , Bn4 
	.byte	W14
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N14   , As4 
	.byte	W15
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N32   , Gs4 , v127, gtp1
	.byte	W17
	.byte		BEND  , c_v+2
	.byte	W04
	.byte		        c_v-5
	.byte	W02
@ 034   ----------------------------------------
	.byte	W02
	.byte		        c_v+2
	.byte	W04
	.byte		        c_v-5
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N04   
	.byte	W04
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N04   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , En4 
	.byte	W05
	.byte		BEND  , c_v+61
	.byte		        c_v-3
	.byte		N19   , Fs4 
	.byte	W14
	.byte		BEND  , c_v+0
	.byte	W04
	.byte		        c_v-6
	.byte	W01
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N19   , En4 
	.byte	W17
	.byte		BEND  , c_v+2
	.byte	W02
	.byte		        c_v+61
	.byte		        c_v-3
	.byte		N14   , Fs4 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		N32   , Ds4 , v127, gtp1
	.byte	W03
@ 035   ----------------------------------------
	.byte	W13
	.byte		BEND  , c_v-4
	.byte	W04
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W04
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W01
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N14   , Cs4 
	.byte	W15
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W04
	.byte		BEND  , c_v+12
	.byte		        c_v-2
	.byte		N28   , Bn4 
	.byte	W18
	.byte		BEND  , c_v+2
	.byte	W04
	.byte		        c_v-6
	.byte	W04
	.byte		        c_v+2
	.byte	W03
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N04   
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N14   , Cs5 
	.byte	W03
@ 036   ----------------------------------------
	.byte	W11
	.byte		BEND  , c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N09   , Cs5 
	.byte	W09
	.byte		N14   
	.byte	W15
	.byte		BEND  , c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N02   , Ds4 
	.byte	W03
	.byte		VOL   , 87*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , An4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W07
@ 037   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N14   , Gs4 
	.byte	W15
	.byte		BEND  , c_v-35
	.byte		        c_v-3
	.byte		N14   , Gn4 
	.byte	W14
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , Gs4 
	.byte	W03
	.byte		VOL   , 87*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , An4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W04
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N09   , Cs5 
	.byte	W10
	.byte		BEND  , c_v-4
	.byte		N14   , En5 
	.byte	W15
	.byte		BEND  , c_v-36
	.byte		        c_v-4
	.byte		N04   , Ds5 
	.byte	W04
	.byte		BEND  , c_v-4
	.byte		N09   , Cs5 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N04   , As4 
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		N09   , Cs5 
	.byte	W02
@ 038   ----------------------------------------
	.byte	W07
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N04   , Ds5 
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		N09   , Cs5 
	.byte	W10
	.byte		BEND  , c_v-2
	.byte		N14   , Bn4 
	.byte	W14
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N14   , As4 
	.byte	W15
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N32   , Gs4 , v127, gtp1
	.byte	W15
	.byte		BEND  , c_v-5
	.byte	W04
	.byte		        c_v+2
	.byte	W04
	.byte		        c_v-5
	.byte	W04
	.byte		        c_v+2
	.byte	W04
	.byte		        c_v-5
	.byte	W02
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W02
@ 039   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v+62
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		N19   
	.byte	W16
	.byte		BEND  , c_v+2
	.byte	W03
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N19   , As4 
	.byte	W15
	.byte		BEND  , c_v-6
	.byte	W04
	.byte		        c_v+30
	.byte		        c_v-2
	.byte		N14   , Bn4 
	.byte	W14
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N42   , Cs5 , v127, gtp1
	.byte	W15
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-9
	.byte	W02
@ 040   ----------------------------------------
	.byte	W02
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-9
	.byte	W04
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-9
	.byte	W04
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-9
	.byte	W01
	.byte		        c_v-2
	.byte		N04   , Bn4 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		BEND  , c_v-3
	.byte		N14   , Fs4 
	.byte	W14
	.byte		N24   , Fs5 
	.byte	W18
	.byte		BEND  , c_v+3
	.byte	W04
	.byte		        c_v-9
	.byte	W03
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		        c_v-3
	.byte		N04   
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		N09   , Fs4 
	.byte	W01
@ 041   ----------------------------------------
	.byte	W09
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , An4 
	.byte	W09
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N09   , As4 
	.byte	W10
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , An4 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N09   , Gs4 
	.byte	W09
	.byte		BEND  , c_v-3
	.byte		N04   , Fs4 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N09   
	.byte	W10
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		N09   , Fs5 
	.byte	W09
	.byte		VOL   , 33*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_2_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-4
	.byte		N14   , En5 
	.byte	W10
@ 042   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v-4
	.byte		N14   , Cs5 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N02   , Bn3 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-3
	.byte		N09   , Dn4 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 
	.byte	W09
	.byte		BEND  , c_v-3
	.byte		N04   , Dn4 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Dn4 
	.byte	W09
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N09   , Gs4 
	.byte	W05
@ 043   ----------------------------------------
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N04   , Dn4 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N04   , Gs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N09   , Dn4 
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte	W02
	.byte	FINE

@**************** Track 4 (Midi-Chn.10) ****************@

mus_casino_plus_2_4:
	.byte	KEYSH , mus_casino_plus_2_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 0
	.byte		VOL   , 95*mus_casino_plus_2_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		        c_v-13
	.byte	W01
	.byte		PAN   , c_v+0
	.byte	W92
	.byte	W03
@ 001   ----------------------------------------
	.byte	W06
	.byte		N03   , Ds1 , v120
	.byte	W14
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W44
	.byte	W03
@ 002   ----------------------------------------
	.byte	W11
	.byte		N04   
	.byte	W24
	.byte	W02
mus_casino_plus_2_4_B1:
	.byte	W03
	.byte		N03   , Ds1 , v120
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W24
	.byte	W03
@ 003   ----------------------------------------
	.byte	W02
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W07
@ 004   ----------------------------------------
	.byte	W21
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W17
@ 005   ----------------------------------------
	.byte	W12
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W24
	.byte	W02
@ 006   ----------------------------------------
	.byte	W03
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W56
	.byte	W02
	.byte		N04   
	.byte	W06
@ 007   ----------------------------------------
	.byte	W23
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W15
@ 008   ----------------------------------------
	.byte	W14
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte		N04   
	.byte	W24
	.byte	W01
@ 009   ----------------------------------------
	.byte	W04
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W05
@ 010   ----------------------------------------
	.byte	W80
	.byte	W02
	.byte		N03   
	.byte	W14
@ 011   ----------------------------------------
	.byte	W15
	.byte		N04   
	.byte	W56
	.byte	W02
	.byte		N04   
	.byte	W23
@ 012   ----------------------------------------
	.byte	W06
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W56
	.byte	W01
	.byte		N04   
	.byte	W04
@ 013   ----------------------------------------
	.byte	W24
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W13
@ 014   ----------------------------------------
	.byte	W16
	.byte		N04   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W22
@ 015   ----------------------------------------
	.byte	W36
	.byte		N04   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W02
@ 016   ----------------------------------------
	.byte	W56
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W11
@ 017   ----------------------------------------
	.byte	W18
	.byte		N04   
	.byte	W56
	.byte	W01
	.byte		N04   
	.byte	W21
@ 018   ----------------------------------------
	.byte	W08
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W01
@ 019   ----------------------------------------
	.byte	W28
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W10
@ 020   ----------------------------------------
	.byte	W19
	.byte		N04   
	.byte	W76
	.byte	W01
@ 021   ----------------------------------------
	.byte	W52
	.byte	W01
	.byte		N03   
	.byte	W15
	.byte		N03   
	.byte	W28
@ 022   ----------------------------------------
	.byte		N03   
	.byte	W56
	.byte	W02
	.byte		N03   
	.byte	W24
	.byte	W03
	.byte	GOTO
	 .word	mus_casino_plus_2_4_B1
mus_casino_plus_2_4_B2:
	.byte	W02
	.byte		N03   , Ds1 , v120
	.byte	W09
@ 023   ----------------------------------------
	.byte	W20
	.byte		N04   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W18
@ 024   ----------------------------------------
	.byte	W11
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W24
	.byte	W03
@ 025   ----------------------------------------
	.byte	W02
	.byte		N04   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W07
@ 026   ----------------------------------------
	.byte	W22
	.byte		N03   
	.byte	W28
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W17
@ 027   ----------------------------------------
	.byte	W40
	.byte	W01
	.byte		N04   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W24
	.byte	W02
@ 028   ----------------------------------------
	.byte	W03
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W06
@ 029   ----------------------------------------
	.byte	W23
	.byte		N04   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W15
@ 030   ----------------------------------------
	.byte	W14
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W52
	.byte	W01
@ 031   ----------------------------------------
	.byte	W32
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W32
	.byte	W02
@ 032   ----------------------------------------
	.byte	W24
	.byte		N04   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W14
@ 033   ----------------------------------------
	.byte	W44
	.byte		N04   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W23
@ 034   ----------------------------------------
	.byte	W06
	.byte		N04   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W03
@ 035   ----------------------------------------
	.byte	W24
	.byte	W01
	.byte		N03   
	.byte	W56
	.byte	W02
	.byte		N04   
	.byte	W13
@ 036   ----------------------------------------
	.byte	W16
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W48
	.byte	W03
@ 037   ----------------------------------------
	.byte	W07
	.byte		N04   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W30
	.byte	W01
@ 038   ----------------------------------------
	.byte	W24
	.byte	W03
	.byte		N04   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W11
@ 039   ----------------------------------------
	.byte	W18
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte		N03   
	.byte	W21
@ 040   ----------------------------------------
	.byte	W08
	.byte		N04   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N04   
	.byte	W30
@ 041   ----------------------------------------
	.byte	W96
@ 042   ----------------------------------------
	.byte	W04
	.byte		N03   
	.byte	W15
	.byte		N03   
	.byte	W28
	.byte	W01
	.byte		N03   
	.byte	W48
@ 043   ----------------------------------------
	.byte	W10
	.byte		N03   
	.byte	W24
	.byte	W02
	.byte	FINE

@******************************************************@
	.align	2

mus_casino_plus_2:
	.byte	4	@ NumTrks
	.byte	0	@ NumBlks
	.byte	mus_casino_plus_2_pri	@ Priority
	.byte	mus_casino_plus_2_rev	@ Reverb.

	.word	mus_casino_plus_2_grp

	.word	mus_casino_plus_2_1
	.word	mus_casino_plus_2_2
	.word	mus_casino_plus_2_3
	.word	mus_casino_plus_2_4

	.end
