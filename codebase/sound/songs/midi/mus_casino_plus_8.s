	.include "MPlayDef.s"

	.equ	mus_casino_plus_8_grp, voicegroup166
	.equ	mus_casino_plus_8_pri, 0
	.equ	mus_casino_plus_8_rev, reverb_set+50
	.equ	mus_casino_plus_8_mvl, 76
	.equ	mus_casino_plus_8_key, 0
	.equ	mus_casino_plus_8_tbs, 1
	.equ	mus_casino_plus_8_exg, 1
	.equ	mus_casino_plus_8_cmp, 1

	.section .rodata
	.global	mus_casino_plus_8
	.align	2

@**************** Track 1 (Midi-Chn.1) ****************@

mus_casino_plus_8_1:
	.byte	KEYSH , mus_casino_plus_8_key+0
@ 000   ----------------------------------------
	.byte	TEMPO , 120*mus_casino_plus_8_tbs/2
	.byte		VOICE , 33
	.byte		VOL   , 127*mus_casino_plus_8_mvl/mxv
	.byte		        64*mus_casino_plus_8_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		BEND  , c_v-13
	.byte		        c_v-13
	.byte		        c_v+39
	.byte		        c_v-1
	.byte		N01   , Cn0 , v127
	.byte		N01   , Ds1 
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		VOL   , 45*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N01   , Ds2 
	.byte	W04
	.byte		VOL   , 64*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N02   , Ds1 
	.byte	W05
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N02   , Ds2 
	.byte	W04
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N36   , Ds1 , v127, gtp1
	.byte	W36
	.byte	W02
	.byte		VOL   , 45*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-33
	.byte		N01   
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N02   , Dn1 
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N02   , Cs1 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		        c_v-8
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W02
	.byte		BEND  , c_v-33
	.byte		N02   
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N02   , As0 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		        c_v-32
	.byte		N02   , An0 
	.byte	W02
	.byte		BEND  , c_v+0
	.byte		        c_v-11
	.byte		        c_v+0
	.byte		N02   , Gn0 
	.byte	W03
	.byte		VOL   , 64*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-37
	.byte		        c_v+0
	.byte		N36   , Ds0 
	.byte	W02
@ 001   ----------------------------------------
	.byte	W32
	.byte	W03
	.byte		VOL   , 90*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+41
	.byte		        c_v+0
	.byte		N02   , En1 
	.byte	W02
	.byte		BEND  , c_v-33
	.byte		N02   
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N02   , Ds1 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N02   , Dn1 
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N02   , Cs1 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		        c_v-8
	.byte		        c_v-1
	.byte		N02   , Bn0 
	.byte	W02
	.byte		BEND  , c_v-33
	.byte		N02   
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N02   , As0 
	.byte	W03
	.byte		VOL   , 64*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		        c_v-32
	.byte		N03   , An0 
	.byte	W04
	.byte		BEND  , c_v+0
	.byte		N02   , Gs0 
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N13   , Fn1 
	.byte	W05
@ 002   ----------------------------------------
	.byte	W09
	.byte		BEND  , c_v-6
	.byte		        c_v-1
	.byte		N14   , Dn1 
	.byte	W14
	.byte		BEND  , c_v+56
	.byte		        c_v-1
	.byte		N04   , Bn0 
	.byte	W10
	.byte		BEND  , c_v-56
	.byte		        c_v+0
	.byte		N04   , Ds0 
	.byte	W04
	.byte		N02   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-28
	.byte		        c_v-1
	.byte		N13   , Cn1 
	.byte	W13
	.byte		BEND  , c_v+37
	.byte		        c_v-1
	.byte		N14   , An0 
	.byte	W13
@ 003   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N04   , Fs0 
	.byte	W09
	.byte		BEND  , c_v-39
	.byte		        c_v+0
	.byte		N03   , Gs0 
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N13   , Fn1 
	.byte	W14
	.byte		BEND  , c_v-6
	.byte		        c_v-1
	.byte		N14   , Dn1 
	.byte	W14
	.byte		BEND  , c_v+56
	.byte		        c_v-1
	.byte		N04   , Bn0 
	.byte	W10
	.byte		BEND  , c_v-56
	.byte		        c_v+0
	.byte		N04   , Ds0 
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W01
@ 004   ----------------------------------------
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W04
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-28
	.byte		        c_v-1
	.byte		N13   , Cn1 
	.byte	W14
	.byte		BEND  , c_v+37
	.byte		        c_v-1
	.byte		N14   , An0 
	.byte	W14
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N04   , Fs0 
	.byte	W10
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N08   , Ds1 
	.byte	W09
	.byte		BEND  , c_v-47
	.byte		        c_v+0
	.byte		N04   , Ds0 
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W04
@ 005   ----------------------------------------
	.byte	W01
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N09   , Ds1 
	.byte	W09
	.byte		BEND  , c_v-47
	.byte		        c_v+0
	.byte		N04   , Ds0 
	.byte	W04
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W10
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N14   , An1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		N08   , Fs1 
	.byte	W08
	.byte		BEND  , c_v+48
	.byte		        c_v+0
	.byte		N04   , Fs0 
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-23
	.byte		        c_v-1
	.byte		N09   , Fs1 
	.byte	W09
	.byte		BEND  , c_v+48
	.byte		        c_v+0
	.byte		N04   , Fs0 
	.byte	W04
	.byte		BEND  , c_v-23
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W02
@ 006   ----------------------------------------
	.byte	W08
	.byte		BEND  , c_v-37
	.byte		        c_v-1
	.byte		N14   , Cn2 
	.byte	W14
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N08   , Bn1 
	.byte	W09
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Bn0 
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+9
	.byte		        c_v-1
	.byte		N09   , Bn1 
	.byte	W10
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Bn0 
	.byte	W04
	.byte		BEND  , c_v+9
	.byte		        c_v-1
	.byte		N04   , Bn1 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		        c_v-2
	.byte		N14   , Fn2 
	.byte	W13
@ 007   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v-4
	.byte		        c_v+0
	.byte		N08   , En1 
	.byte	W09
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N09   , Ds2 
	.byte	W09
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N01   , Fn1 
	.byte	W04
	.byte		BEND  , c_v+36
	.byte		        c_v-1
	.byte		N09   , Dn2 
	.byte	W10
	.byte		BEND  , c_v-4
	.byte		        c_v+0
	.byte		N02   , En1 
	.byte	W05
	.byte		BEND  , c_v+9
	.byte		        c_v-1
	.byte		N08   , Cs2 
	.byte	W09
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N02   , Ds1 
	.byte	W05
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N04   , Cn2 
	.byte	W04
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn1 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N04   , As1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v+0
	.byte		        c_v+0
	.byte		N04   , Gs0 
	.byte	W09
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Bn0 
	.byte	W02
@ 008   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v-44
	.byte		        c_v-1
	.byte		N13   , Dn1 
	.byte	W14
	.byte		BEND  , c_v-3
	.byte		        c_v+0
	.byte		N04   , Gs0 
	.byte	W09
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v+52
	.byte		        c_v-1
	.byte		N04   , Dn1 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		        c_v-1
	.byte		N14   , Fn1 
	.byte	W15
	.byte		BEND  , c_v+6
	.byte		        c_v+0
	.byte		N04   , Ds0 
	.byte	W04
	.byte		N02   
	.byte	W04
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W05
	.byte		BEND  , c_v-47
	.byte		        c_v+0
	.byte		N02   , Ds0 
	.byte	W05
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W05
	.byte		BEND  , c_v-47
	.byte		        c_v+0
	.byte		N01   , Ds0 
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W05
	.byte		BEND  , c_v-47
	.byte		        c_v+0
	.byte		N02   , Ds0 
	.byte	W04
@ 009   ----------------------------------------
	.byte		BEND  , c_v+32
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v-56
	.byte		        c_v+32
	.byte		N02   , En0 
	.byte	W04
	.byte		BEND  , c_v+0
	.byte		        c_v+32
	.byte		N04   , Fn0 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+32
	.byte		N02   , Fs0 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v-7
	.byte		        c_v+0
	.byte		N04   , Gs0 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		N02   
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N04   , An0 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-64
	.byte		N03   , As0 
	.byte	W09
	.byte		BEND  , c_v+0
	.byte		N04   , Gs0 
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-44
	.byte		        c_v-1
	.byte		N13   , Dn1 
	.byte	W13
	.byte		BEND  , c_v-3
	.byte		        c_v+0
	.byte		N04   , Gs0 
	.byte	W10
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v+52
	.byte		        c_v-1
	.byte		N04   , Dn1 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		        c_v-1
	.byte		N14   , Fn1 
	.byte	W02
@ 010   ----------------------------------------
	.byte	W09
mus_casino_plus_8_1_B1:
	.byte	W03
	.byte		BEND  , c_v-6
	.byte		        c_v-1
	.byte		N04   , Dn1 , v127
	.byte	W04
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N02   , Dn0 
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+39
	.byte		        c_v-1
	.byte		N04   , Dn1 
	.byte	W05
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N02   , Dn0 
	.byte	W04
	.byte		N01   
	.byte	W04
	.byte		BEND  , c_v+22
	.byte		        c_v-1
	.byte		N02   , Cs1 
	.byte	W03
	.byte		BEND  , c_v+31
	.byte		N24   , Cs1 , v127, gtp1
	.byte	W24
	.byte	W01
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N04   , Dn1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N04   , Cs1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-8
	.byte		        c_v-1
	.byte		N04   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-64
	.byte		N03   , As0 
	.byte	W04
	.byte		BEND  , c_v+0
	.byte		N02   , Gs0 
	.byte	W05
@ 011   ----------------------------------------
	.byte		N04   
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N13   , Fn1 
	.byte	W13
	.byte		BEND  , c_v-6
	.byte		        c_v-1
	.byte		N14   , Dn1 
	.byte	W15
	.byte		BEND  , c_v+56
	.byte		        c_v-1
	.byte		N04   , Bn0 
	.byte	W10
	.byte		BEND  , c_v-56
	.byte		        c_v+0
	.byte		N04   , Ds0 
	.byte	W04
	.byte		N02   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W03
@ 012   ----------------------------------------
	.byte	W02
	.byte		N02   
	.byte	W04
	.byte		BEND  , c_v-28
	.byte		        c_v-1
	.byte		N13   , Cn1 
	.byte	W14
	.byte		BEND  , c_v+37
	.byte		        c_v-1
	.byte		N14   , An0 
	.byte	W15
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N04   , Fs0 
	.byte	W09
	.byte		BEND  , c_v-39
	.byte		        c_v+0
	.byte		N03   , Gs0 
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N13   , Fn1 
	.byte	W14
	.byte		BEND  , c_v-6
	.byte		        c_v-1
	.byte		N14   , Dn1 
	.byte	W01
@ 013   ----------------------------------------
	.byte	W13
	.byte		BEND  , c_v+56
	.byte		        c_v-1
	.byte		N04   , Bn0 
	.byte	W10
	.byte		BEND  , c_v-56
	.byte		        c_v+0
	.byte		N04   , Ds0 
	.byte		N01   , Bn0 
	.byte	W04
	.byte		N02   , Ds0 
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-28
	.byte		        c_v-1
	.byte		N13   , Cn1 
	.byte	W14
	.byte		BEND  , c_v+37
	.byte		        c_v-1
	.byte		N14   , An0 
	.byte	W14
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N04   , Fs0 
	.byte	W08
@ 014   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N08   , Ds1 
	.byte	W09
	.byte		BEND  , c_v-47
	.byte		        c_v+0
	.byte		N04   , Ds0 
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N09   , Ds1 
	.byte	W09
	.byte		BEND  , c_v-47
	.byte		        c_v+0
	.byte		N04   , Ds0 
	.byte	W04
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W10
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N14   , An1 
	.byte	W15
	.byte		BEND  , c_v-1
	.byte		N08   , Fs1 
	.byte	W08
	.byte		BEND  , c_v+48
	.byte		        c_v+0
	.byte		N04   , Fs0 
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W01
@ 015   ----------------------------------------
	.byte	W04
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W04
	.byte		BEND  , c_v-23
	.byte		        c_v-1
	.byte		N09   , Fs1 
	.byte	W10
	.byte		BEND  , c_v+48
	.byte		        c_v+0
	.byte		N04   , Fs0 
	.byte	W04
	.byte		BEND  , c_v-23
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W10
	.byte		BEND  , c_v-37
	.byte		        c_v-1
	.byte		N14   , Cn2 
	.byte	W14
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N08   , Bn1 
	.byte	W09
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Bn0 
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+9
	.byte		        c_v-1
	.byte		N09   , Bn1 
	.byte	W04
@ 016   ----------------------------------------
	.byte	W06
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Bn0 
	.byte	W04
	.byte		BEND  , c_v+9
	.byte		        c_v-1
	.byte		N04   , Bn1 
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		        c_v-2
	.byte		N14   , Fn2 
	.byte	W14
	.byte		BEND  , c_v-4
	.byte		        c_v+0
	.byte		N08   , En1 
	.byte	W09
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N09   , Ds2 
	.byte	W09
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N01   , Fn1 
	.byte	W04
	.byte		BEND  , c_v+36
	.byte		        c_v-1
	.byte		N09   , Dn2 
	.byte	W10
	.byte		BEND  , c_v-4
	.byte		        c_v+0
	.byte		N02   , En1 
	.byte	W05
	.byte		BEND  , c_v+9
	.byte		        c_v-1
	.byte		N08   , Cs2 
	.byte	W09
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N02   , Ds1 
	.byte	W04
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N04   , Cn2 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn1 
	.byte	W02
@ 017   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v-33
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N04   , As1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v+0
	.byte		        c_v+0
	.byte		N04   , Gs0 
	.byte	W09
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-44
	.byte		        c_v-1
	.byte		N13   , Dn1 
	.byte	W14
	.byte		BEND  , c_v-3
	.byte		        c_v+0
	.byte		N04   , Gs0 
	.byte	W09
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v+52
	.byte		        c_v-1
	.byte		N04   , Dn1 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		        c_v-1
	.byte		N14   , Fn1 
	.byte	W14
	.byte		BEND  , c_v+6
	.byte		        c_v+0
	.byte		N04   , Ds0 
	.byte	W04
	.byte		N02   
	.byte	W05
@ 018   ----------------------------------------
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W05
	.byte		BEND  , c_v-47
	.byte		        c_v+0
	.byte		N02   , Ds0 
	.byte	W05
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W05
	.byte		BEND  , c_v-47
	.byte		        c_v+0
	.byte		N01   , Ds0 
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W04
	.byte		BEND  , c_v-47
	.byte		        c_v+0
	.byte		N02   , Ds0 
	.byte	W05
	.byte		BEND  , c_v+32
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v-56
	.byte		        c_v+32
	.byte		N02   , En0 
	.byte	W04
	.byte		BEND  , c_v+0
	.byte		        c_v+32
	.byte		N04   , Fn0 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+32
	.byte		N02   , Fs0 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v-7
	.byte		        c_v+0
	.byte		N04   , Gs0 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		N02   
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N04   , An0 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-64
	.byte		N03   , As0 
	.byte	W09
	.byte		BEND  , c_v+0
	.byte		N04   , Gs0 
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-44
	.byte		        c_v-1
	.byte		N13   , Dn1 
	.byte	W06
@ 019   ----------------------------------------
	.byte	W07
	.byte		BEND  , c_v-3
	.byte		        c_v+0
	.byte		N04   , Gs0 
	.byte	W10
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v+52
	.byte		        c_v-1
	.byte		N04   , Dn1 
	.byte	W04
	.byte		BEND  , c_v-3
	.byte		        c_v-1
	.byte		N14   , Fn1 
	.byte	W12
	.byte	GOTO
	 .word	mus_casino_plus_8_1_B1
mus_casino_plus_8_1_B2:
	.byte	W03
	.byte		BEND  , c_v-6
	.byte		        c_v-1
	.byte		N04   , Dn1 , v127
	.byte	W04
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N02   , Dn0 
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+39
	.byte		        c_v-1
	.byte		N04   , Dn1 
	.byte	W04
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N02   , Dn0 
	.byte	W05
	.byte		N01   
	.byte	W04
	.byte		BEND  , c_v+22
	.byte		        c_v-1
	.byte		N02   , Cs1 
	.byte	W03
	.byte		BEND  , c_v+31
	.byte		N24   , Cs1 , v127, gtp1
	.byte	W21
@ 020   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N04   , Dn1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N04   , Cs1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-8
	.byte		        c_v-1
	.byte		N04   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-64
	.byte		N03   , As0 
	.byte	W04
	.byte		BEND  , c_v+0
	.byte		N02   , Gs0 
	.byte	W05
	.byte		N04   
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N13   , Fn1 
	.byte	W13
	.byte		BEND  , c_v-6
	.byte		        c_v-1
	.byte		N14   , Dn1 
	.byte	W15
	.byte		BEND  , c_v+56
	.byte		        c_v-1
	.byte		N04   , Bn0 
	.byte	W07
@ 021   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-56
	.byte		        c_v+0
	.byte		N04   , Ds0 
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W04
	.byte		BEND  , c_v-28
	.byte		        c_v-1
	.byte		N13   , Cn1 
	.byte	W14
	.byte		BEND  , c_v+37
	.byte		        c_v-1
	.byte		N14   , An0 
	.byte	W15
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N04   , Fs0 
	.byte	W09
	.byte		BEND  , c_v-39
	.byte		        c_v+0
	.byte		N03   , Gs0 
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W05
@ 022   ----------------------------------------
	.byte		N04   
	.byte	W04
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-1
	.byte		N13   , Fn1 
	.byte	W14
	.byte		BEND  , c_v-6
	.byte		        c_v-1
	.byte		N14   , Dn1 
	.byte	W14
	.byte		BEND  , c_v+56
	.byte		        c_v-1
	.byte		N04   , Bn0 
	.byte	W10
	.byte		BEND  , c_v-56
	.byte		        c_v+0
	.byte		N04   , Ds0 
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-28
	.byte		        c_v-1
	.byte		N13   , Cn1 
	.byte	W03
@ 023   ----------------------------------------
	.byte	W11
	.byte		BEND  , c_v+37
	.byte		        c_v-1
	.byte		N14   , An0 
	.byte	W14
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N04   , Fs0 
	.byte	W10
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N08   , Ds1 
	.byte	W08
	.byte		BEND  , c_v-47
	.byte		        c_v+0
	.byte		N04   , Ds0 
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N09   , Ds1 
	.byte	W09
	.byte		BEND  , c_v-47
	.byte		        c_v+0
	.byte		N04   , Ds0 
	.byte	W04
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W10
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N14   , An1 
	.byte	W01
@ 024   ----------------------------------------
	.byte	W13
	.byte		BEND  , c_v-1
	.byte		N08   , Fs1 
	.byte	W09
	.byte		BEND  , c_v+48
	.byte		        c_v+0
	.byte		N04   , Fs0 
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W04
	.byte		BEND  , c_v-23
	.byte		        c_v-1
	.byte		N09   , Fs1 
	.byte	W10
	.byte		BEND  , c_v+48
	.byte		        c_v+0
	.byte		N04   , Fs0 
	.byte	W04
	.byte		BEND  , c_v-23
	.byte		        c_v-1
	.byte		N04   , Fs1 
	.byte	W10
	.byte		BEND  , c_v-37
	.byte		        c_v-1
	.byte		N14   , Cn2 
	.byte	W14
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N08   , Bn1 
	.byte	W08
@ 025   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Bn0 
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		N04   
	.byte	W04
	.byte		N01   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+9
	.byte		        c_v-1
	.byte		N09   , Bn1 
	.byte	W10
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Bn0 
	.byte	W04
	.byte		BEND  , c_v+9
	.byte		        c_v-1
	.byte		N04   , Bn1 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		        c_v-2
	.byte		N14   , Fn2 
	.byte	W15
	.byte		BEND  , c_v-4
	.byte		        c_v+0
	.byte		N08   , En1 
	.byte	W09
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N02   , Fs1 
	.byte	W05
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N09   , Ds2 
	.byte	W09
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N01   , Fn1 
	.byte	W04
	.byte		BEND  , c_v+36
	.byte		        c_v-1
	.byte		N09   , Dn2 
	.byte	W02
@ 026   ----------------------------------------
	.byte	W08
	.byte		BEND  , c_v-4
	.byte		        c_v+0
	.byte		N02   , En1 
	.byte	W05
	.byte		BEND  , c_v+9
	.byte		        c_v-1
	.byte		N08   , Cs2 
	.byte	W09
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N02   , Ds1 
	.byte	W04
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N04   , Cn2 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn1 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-33
	.byte		N04   , As1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v+0
	.byte		        c_v+0
	.byte		N04   , Gs0 
	.byte	W08
	.byte		N04   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-44
	.byte		        c_v-1
	.byte		N13   , Dn1 
	.byte	W14
	.byte		BEND  , c_v-3
	.byte		        c_v+0
	.byte		N04   , Gs0 
	.byte	W09
	.byte		N04   
	.byte	W04
@ 027   ----------------------------------------
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v+52
	.byte		        c_v-1
	.byte		N04   , Dn1 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		        c_v-1
	.byte		N14   , Fn1 
	.byte	W14
	.byte		BEND  , c_v+6
	.byte		        c_v+0
	.byte		N04   , Ds0 
	.byte	W04
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W05
	.byte		BEND  , c_v-47
	.byte		        c_v+0
	.byte		N02   , Ds0 
	.byte	W05
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W05
	.byte		BEND  , c_v-47
	.byte		        c_v+0
	.byte		N01   , Ds0 
	.byte	W04
	.byte		N02   
	.byte	W04
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N04   , Ds1 
	.byte	W05
	.byte		BEND  , c_v-47
	.byte		        c_v+0
	.byte		N02   , Ds0 
	.byte	W05
	.byte		BEND  , c_v+32
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v-56
	.byte		        c_v+32
	.byte		N02   , En0 
	.byte	W04
	.byte		BEND  , c_v+0
	.byte		        c_v+32
	.byte		N04   , Fn0 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+32
	.byte		N02   , Fs0 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v-7
	.byte		        c_v+0
	.byte		N04   , Gs0 
	.byte	W04
	.byte		BEND  , c_v+31
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N04   , An0 
	.byte	W02
@ 028   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		        c_v-64
	.byte		N03   , As0 
	.byte	W09
	.byte		BEND  , c_v+0
	.byte		N04   , Gs0 
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Bn0 
	.byte	W04
	.byte		BEND  , c_v-44
	.byte		        c_v-1
	.byte		N13   , Dn1 
	.byte	W14
	.byte		BEND  , c_v-3
	.byte		        c_v+0
	.byte		N04   , Gs0 
	.byte	W10
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v+52
	.byte		        c_v-1
	.byte		N04   , Dn1 
	.byte	W04
	.byte		BEND  , c_v-3
	.byte		        c_v-1
	.byte	W12
	.byte	FINE

@**************** Track 2 (Midi-Chn.2) ****************@

mus_casino_plus_8_2:
	.byte	KEYSH , mus_casino_plus_8_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 73
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		BEND  , c_v-8
	.byte		        c_v-13
	.byte		N01   , Cn1 , v127
	.byte		N36   
	.byte	W36
	.byte	W01
	.byte		VOL   , 47*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+3
	.byte		        c_v-1
	.byte		N02   , En4 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N02   , An4 
	.byte	W02
	.byte		VOL   , 66*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N02   , An4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N01   , An4 
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N02   , An4 
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N02   , An4 
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N02   , An4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N02   , An4 
	.byte	W02
	.byte		VOL   , 66*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N02   , An4 
	.byte	W02
	.byte		VOL   , 47*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N01   , Fn4 
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N02   , Gs4 
	.byte	W02
	.byte		BEND  , c_v-2
	.byte		N02   , Fn4 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N02   , Gs4 
	.byte	W02
	.byte		BEND  , c_v-2
	.byte		N02   , Fn4 
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N02   , Gs4 
	.byte	W03
	.byte		BEND  , c_v-2
	.byte		N02   , Fn4 
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N02   , Gs4 
	.byte	W03
	.byte		BEND  , c_v-2
	.byte		N02   , Fn4 
	.byte	W02
@ 001   ----------------------------------------
	.byte		VOL   , 57*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , Gs4 
	.byte	W02
	.byte		BEND  , c_v-2
	.byte		N01   , Fn4 
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N02   , Gs4 
	.byte	W02
	.byte		BEND  , c_v-2
	.byte		N02   , Fn4 
	.byte	W03
	.byte		VOL   , 66*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , Gs4 
	.byte	W02
	.byte		BEND  , c_v-2
	.byte		N02   , Fn4 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N02   , Gs4 
	.byte	W02
	.byte		BEND  , c_v-2
	.byte		N02   , Fn4 
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N02   , Gs4 
	.byte	W03
	.byte		VOL   , 73*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Fn4 
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N02   , Gs4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Fn4 
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N01   , Gs4 
	.byte	W02
	.byte		VOL   , 87*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Fn4 
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N02   , Gs4 
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Fn4 
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N02   , Gs4 
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Fn4 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N02   , Gs4 
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Fn4 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N02   , Gs4 
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N02   , Fn4 
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N02   , Gs4 
	.byte	W03
	.byte		VOICE , 48
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-6
	.byte		        c_v-1
	.byte		N04   , Fn2 
	.byte	W04
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+36
	.byte		        c_v-1
	.byte		N13   , Dn3 
	.byte	W05
@ 002   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-3
	.byte	W01
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N14   , Bn2 
	.byte	W08
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-2
	.byte	W03
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+3
	.byte		        c_v-1
	.byte		N04   , Cn2 
	.byte	W04
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N13   , An2 
	.byte	W06
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-2
	.byte	W03
	.byte		        c_v+1
	.byte	W01
	.byte		        c_v-1
	.byte		N14   , Fs2 
	.byte	W09
	.byte		BEND  , c_v-2
	.byte	W03
	.byte		        c_v+1
	.byte	W01
@ 003   ----------------------------------------
	.byte	W02
	.byte		        c_v+8
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		        c_v-1
	.byte		N04   , Fn2 
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+36
	.byte		        c_v-1
	.byte		N13   , Dn3 
	.byte	W09
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-3
	.byte	W02
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N14   , Bn2 
	.byte	W08
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-2
	.byte	W03
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+3
	.byte		        c_v-1
	.byte		N04   , Cn2 
	.byte	W04
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W01
@ 004   ----------------------------------------
	.byte	W04
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N13   , An2 
	.byte	W06
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-2
	.byte	W03
	.byte		        c_v+1
	.byte	W01
	.byte		        c_v-1
	.byte		N14   , Fs2 
	.byte	W09
	.byte		BEND  , c_v-2
	.byte	W03
	.byte		        c_v+1
	.byte	W02
	.byte		        c_v+8
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N08   , Cn3 
	.byte	W07
	.byte		BEND  , c_v-2
	.byte	W02
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , Cn2 
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
@ 005   ----------------------------------------
	.byte	W01
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N09   , Cn3 
	.byte	W08
	.byte		BEND  , c_v+2
	.byte	W01
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , Cn2 
	.byte	W04
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N04   , Cn3 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N14   , Fs3 
	.byte	W08
	.byte		BEND  , c_v-3
	.byte	W03
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-1
	.byte		N08   , Ds3 
	.byte	W06
	.byte		BEND  , c_v-3
	.byte	W02
	.byte		        c_v+5
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N09   , Ds3 
	.byte	W07
	.byte		BEND  , c_v+1
	.byte	W02
	.byte		        c_v+5
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W04
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N04   , Ds3 
	.byte	W02
@ 006   ----------------------------------------
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N14   , An3 
	.byte	W07
	.byte		BEND  , c_v-3
	.byte	W03
	.byte		        c_v+3
	.byte	W03
	.byte		        c_v-3
	.byte	W01
	.byte		        c_v-33
	.byte		        c_v-1
	.byte		N08   , Gs3 
	.byte	W09
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+54
	.byte		        c_v-1
	.byte		N09   , Gs3 
	.byte	W07
	.byte		BEND  , c_v+2
	.byte	W03
	.byte		        c_v+0
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W04
	.byte		BEND  , c_v+54
	.byte		        c_v-1
	.byte		N04   , Gs3 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-3
	.byte		N14   , Dn4 
	.byte	W06
	.byte		BEND  , c_v-5
	.byte	W03
	.byte		        c_v+2
	.byte	W03
	.byte		        c_v-5
	.byte	W01
@ 007   ----------------------------------------
	.byte	W01
	.byte		        c_v-34
	.byte		        c_v-2
	.byte		N08   , Cs4 
	.byte	W08
	.byte		BEND  , c_v+3
	.byte	W01
	.byte		        c_v+3
	.byte		        c_v-1
	.byte		N02   , Ds3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-2
	.byte		N09   , Cn4 
	.byte	W09
	.byte		BEND  , c_v-4
	.byte		        c_v-10
	.byte		        c_v-1
	.byte		N01   , Dn3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N09   , Bn3 
	.byte	W09
	.byte		BEND  , c_v+2
	.byte	W01
	.byte		        c_v-1
	.byte		N02   , Cs3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N08   , As3 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N02   , Cn3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N04   , An3 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , Gs3 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N04   , Gn3 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N04   , Fs3 
	.byte	W05
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N04   , Fn2 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		N04   , Gs2 
	.byte	W02
@ 008   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N13   , Bn2 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte	W04
	.byte		        c_v+1
	.byte	W03
	.byte		        c_v-2
	.byte	W01
	.byte		        c_v-1
	.byte		N04   , Fn2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		BEND  , c_v+4
	.byte		        c_v-1
	.byte		N14   , Dn3 
	.byte	W09
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-3
	.byte	W03
	.byte		        c_v-52
	.byte		        c_v-1
	.byte		N04   , Cn2 
	.byte	W04
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N04   , Cn3 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N02   , Cn2 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N04   , Cn3 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N01   , Cn2 
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N04   , Cn3 
	.byte	W04
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N02   , Cn2 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
@ 009   ----------------------------------------
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Cs2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , Dn2 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N01   
	.byte	W01
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W05
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N02   , En2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		        c_v-1
	.byte		N04   , Fn2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , Fs2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Gn2 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Fn2 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N13   , Bn2 
	.byte	W07
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-2
	.byte	W03
	.byte		        c_v-1
	.byte		N04   , Fn2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		BEND  , c_v+4
	.byte		        c_v-1
	.byte		N14   , Dn3 
	.byte	W02
@ 010   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-3
	.byte	W02
mus_casino_plus_8_2_B1:
	.byte	W01
	.byte		BEND  , c_v+1
	.byte	W02
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn2 , v127
	.byte	W04
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N02   , Bn1 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+9
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W04
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N02   , Bn1 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N02   , As2 
	.byte	W03
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N24   , Bn2 , v127, gtp1
	.byte	W07
	.byte		BEND  , c_v+2
	.byte	W03
	.byte		        c_v-3
	.byte	W03
	.byte		        c_v+2
	.byte	W04
	.byte		        c_v-3
	.byte	W03
	.byte		        c_v+2
	.byte	W03
	.byte		        c_v-3
	.byte	W02
	.byte		        c_v-33
	.byte		        c_v-1
	.byte		N04   , As2 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , An2 
	.byte	W05
	.byte		BEND  , c_v-32
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , Gn2 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Fn2 
	.byte	W04
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
@ 011   ----------------------------------------
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+36
	.byte		        c_v-1
	.byte		N13   , Dn3 
	.byte	W09
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-3
	.byte	W01
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N14   , Bn2 
	.byte	W08
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-2
	.byte	W03
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+3
	.byte		        c_v-1
	.byte		N04   , Cn2 
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W03
@ 012   ----------------------------------------
	.byte	W02
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N13   , An2 
	.byte	W07
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-2
	.byte	W03
	.byte		        c_v+1
	.byte	W01
	.byte		        c_v-1
	.byte		N14   , Fs2 
	.byte	W09
	.byte		BEND  , c_v-2
	.byte	W03
	.byte		        c_v+1
	.byte	W03
	.byte		        c_v+8
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		        c_v-1
	.byte		N04   , Fn2 
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+36
	.byte		        c_v-1
	.byte		N13   , Dn3 
	.byte	W09
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-3
	.byte	W02
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N14   , Bn2 
	.byte	W01
@ 013   ----------------------------------------
	.byte	W07
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-2
	.byte	W03
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+3
	.byte		        c_v-1
	.byte		N04   , Cn2 
	.byte	W04
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N13   , An2 
	.byte	W06
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-2
	.byte	W03
	.byte		        c_v+1
	.byte	W01
	.byte		        c_v-1
	.byte		N14   , Fs2 
	.byte	W08
	.byte		BEND  , c_v-2
	.byte	W04
	.byte		        c_v+1
	.byte	W02
	.byte		        c_v+8
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W03
@ 014   ----------------------------------------
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N08   , Cn3 
	.byte	W07
	.byte		BEND  , c_v-2
	.byte	W02
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , Cn2 
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N09   , Cn3 
	.byte	W08
	.byte		BEND  , c_v+2
	.byte	W01
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , Cn2 
	.byte	W04
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N04   , Cn3 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N14   , Fs3 
	.byte	W08
	.byte		BEND  , c_v-3
	.byte	W03
	.byte		        c_v+1
	.byte	W03
	.byte		        c_v-1
	.byte		N08   , Ds3 
	.byte	W07
	.byte		BEND  , c_v-3
	.byte	W02
	.byte		        c_v+5
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W01
@ 015   ----------------------------------------
	.byte	W04
	.byte		N01   
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N09   , Ds3 
	.byte	W08
	.byte		BEND  , c_v+1
	.byte	W02
	.byte		        c_v+5
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W04
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N14   , An3 
	.byte	W07
	.byte		BEND  , c_v-3
	.byte	W03
	.byte		        c_v+3
	.byte	W03
	.byte		        c_v-3
	.byte	W01
	.byte		        c_v-33
	.byte		        c_v-1
	.byte		N08   , Gs3 
	.byte	W09
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+54
	.byte		        c_v-1
	.byte		N09   , Gs3 
	.byte	W04
@ 016   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v+2
	.byte	W03
	.byte		        c_v+0
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W04
	.byte		BEND  , c_v+54
	.byte		        c_v-1
	.byte		N04   , Gs3 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-3
	.byte		N14   , Dn4 
	.byte	W07
	.byte		BEND  , c_v-5
	.byte	W03
	.byte		        c_v+2
	.byte	W03
	.byte		        c_v-5
	.byte	W02
	.byte		        c_v-34
	.byte		        c_v-2
	.byte		N08   , Cs4 
	.byte	W08
	.byte		BEND  , c_v+3
	.byte	W01
	.byte		        c_v+3
	.byte		        c_v-1
	.byte		N02   , Ds3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-2
	.byte		N09   , Cn4 
	.byte	W08
	.byte		BEND  , c_v-4
	.byte	W01
	.byte		        c_v-10
	.byte		        c_v-1
	.byte		N01   , Dn3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N09   , Bn3 
	.byte	W09
	.byte		BEND  , c_v+2
	.byte	W01
	.byte		        c_v-1
	.byte		N02   , Cs3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N08   , As3 
	.byte	W09
	.byte		BEND  , c_v-1
	.byte		N02   , Cn3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N04   , An3 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , Gs3 
	.byte	W02
@ 017   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N04   , Gn3 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N04   , Fs3 
	.byte	W05
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N04   , Fn2 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N13   , Bn2 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte	W04
	.byte		        c_v+1
	.byte	W03
	.byte		        c_v-2
	.byte	W01
	.byte		        c_v-1
	.byte		N04   , Fn2 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		BEND  , c_v+4
	.byte		        c_v-1
	.byte		N14   , Dn3 
	.byte	W09
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-3
	.byte	W02
	.byte		        c_v-52
	.byte		        c_v-1
	.byte		N04   , Cn2 
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
@ 018   ----------------------------------------
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N04   , Cn3 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N02   , Cn2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N04   , Cn3 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N01   , Cn2 
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N04   , Cn3 
	.byte	W04
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N02   , Cn2 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Cs2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , Dn2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N01   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W05
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N02   , En2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		        c_v-1
	.byte		N04   , Fn2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , Fs2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Gn2 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Fn2 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		N04   , Gs2 
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		N13   , Bn2 
	.byte	W07
@ 019   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-2
	.byte	W03
	.byte		        c_v-1
	.byte		N04   , Fn2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Bn2 
	.byte	W04
	.byte		BEND  , c_v+4
	.byte		        c_v-1
	.byte		N14   , Dn3 
	.byte	W07
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-3
	.byte	W02
	.byte	GOTO
	 .word	mus_casino_plus_8_2_B1
mus_casino_plus_8_2_B2:
	.byte	W01
	.byte		BEND  , c_v+1
	.byte	W02
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn2 , v127
	.byte	W04
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N02   , Bn1 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+9
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W04
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N02   , Bn1 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N02   , As2 
	.byte	W03
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N24   , Bn2 , v127, gtp1
	.byte	W07
	.byte		BEND  , c_v+2
	.byte	W03
	.byte		        c_v-3
	.byte	W03
	.byte		        c_v+2
	.byte	W03
	.byte		        c_v-3
	.byte	W04
	.byte		        c_v+2
	.byte	W01
@ 020   ----------------------------------------
	.byte	W02
	.byte		        c_v-3
	.byte	W02
	.byte		        c_v-33
	.byte		        c_v-1
	.byte		N04   , As2 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , An2 
	.byte	W05
	.byte		BEND  , c_v-32
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , Gn2 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Fn2 
	.byte	W04
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+36
	.byte		        c_v-1
	.byte		N13   , Dn3 
	.byte	W08
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-3
	.byte	W01
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N14   , Bn2 
	.byte	W08
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-2
	.byte	W03
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W02
@ 021   ----------------------------------------
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+3
	.byte		        c_v-1
	.byte		N04   , Cn2 
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N13   , An2 
	.byte	W07
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-2
	.byte	W03
	.byte		        c_v+1
	.byte	W01
	.byte		        c_v-1
	.byte		N14   , Fs2 
	.byte	W09
	.byte		BEND  , c_v-2
	.byte	W03
	.byte		        c_v+1
	.byte	W02
	.byte		        c_v+8
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		        c_v-1
	.byte		N04   , Fn2 
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
@ 022   ----------------------------------------
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+36
	.byte		        c_v-1
	.byte		N13   , Dn3 
	.byte	W09
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-3
	.byte	W02
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N14   , Bn2 
	.byte	W08
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-2
	.byte	W03
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+3
	.byte		        c_v-1
	.byte		N04   , Cn2 
	.byte	W04
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N13   , An2 
	.byte	W03
@ 023   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-2
	.byte	W04
	.byte		        c_v+1
	.byte		        c_v-1
	.byte		N14   , Fs2 
	.byte	W09
	.byte		BEND  , c_v-2
	.byte	W04
	.byte		        c_v+1
	.byte	W02
	.byte		        c_v+8
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte		N01   , An2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   , Ds2 
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N08   , Cn3 
	.byte	W07
	.byte		BEND  , c_v-2
	.byte	W01
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , Cn2 
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N09   , Cn3 
	.byte	W08
	.byte		BEND  , c_v+2
	.byte	W01
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , Cn2 
	.byte	W04
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N04   , Cn3 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N14   , Fs3 
	.byte	W01
@ 024   ----------------------------------------
	.byte	W07
	.byte		BEND  , c_v-3
	.byte	W03
	.byte		        c_v+1
	.byte	W03
	.byte		        c_v-1
	.byte		N08   , Ds3 
	.byte	W07
	.byte		BEND  , c_v-3
	.byte	W02
	.byte		        c_v+5
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N09   , Ds3 
	.byte	W08
	.byte		BEND  , c_v+1
	.byte	W02
	.byte		        c_v+5
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W04
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N14   , An3 
	.byte	W07
	.byte		BEND  , c_v-3
	.byte	W03
	.byte		        c_v+3
	.byte	W03
	.byte		        c_v-3
	.byte	W01
	.byte		        c_v-33
	.byte		        c_v-1
	.byte		N08   , Gs3 
	.byte	W08
@ 025   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+54
	.byte		        c_v-1
	.byte		N09   , Gs3 
	.byte	W06
	.byte		BEND  , c_v+2
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W04
	.byte		BEND  , c_v+54
	.byte		        c_v-1
	.byte		N04   , Gs3 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-3
	.byte		N14   , Dn4 
	.byte	W07
	.byte		BEND  , c_v-5
	.byte	W03
	.byte		        c_v+2
	.byte	W03
	.byte		        c_v-5
	.byte	W02
	.byte		        c_v-34
	.byte		        c_v-2
	.byte		N08   , Cs4 
	.byte	W08
	.byte		BEND  , c_v+3
	.byte	W01
	.byte		        c_v+3
	.byte		        c_v-1
	.byte		N02   , Ds3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-2
	.byte		N09   , Cn4 
	.byte	W09
	.byte		BEND  , c_v-4
	.byte	W01
	.byte		        c_v-10
	.byte		        c_v-1
	.byte		N01   , Dn3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N09   , Bn3 
	.byte	W02
@ 026   ----------------------------------------
	.byte	W07
	.byte		BEND  , c_v+2
	.byte	W01
	.byte		        c_v-1
	.byte		N02   , Cs3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N08   , As3 
	.byte	W08
	.byte		BEND  , c_v-1
	.byte		N02   , Cn3 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N04   , An3 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , Gs3 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N04   , Gn3 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N04   , Fs3 
	.byte	W05
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N04   , Fn2 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N13   , Bn2 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte	W04
	.byte		        c_v+1
	.byte	W03
	.byte		        c_v-2
	.byte	W01
	.byte		        c_v-1
	.byte		N04   , Fn2 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
@ 027   ----------------------------------------
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		BEND  , c_v+4
	.byte		        c_v-1
	.byte		N14   , Dn3 
	.byte	W09
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-3
	.byte	W02
	.byte		        c_v-52
	.byte		        c_v-1
	.byte		N04   , Cn2 
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N04   , Cn3 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N02   , Cn2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N04   , Cn3 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N01   , Cn2 
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N04   , Cn3 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N02   , Cn2 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Cs2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , Dn2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N01   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W05
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N02   , En2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		        c_v-1
	.byte		N04   , Fn2 
	.byte	W04
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , Fs2 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Gn2 
	.byte	W02
@ 028   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N04   , Fn2 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		N04   , Gs2 
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		N13   , Bn2 
	.byte	W08
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-2
	.byte	W03
	.byte		        c_v-1
	.byte		N04   , Fn2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		BEND  , c_v+4
	.byte		        c_v-1
	.byte	W07
	.byte		        c_v+1
	.byte	W03
	.byte		        c_v-3
	.byte	W02
	.byte	FINE

@**************** Track 3 (Midi-Chn.3) ****************@

mus_casino_plus_8_3:
	.byte	KEYSH , mus_casino_plus_8_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 73
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		        109*mus_casino_plus_8_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		BEND  , c_v-13
	.byte		        c_v+17
	.byte		        c_v-1
	.byte		N01   , Cn1 , v127
	.byte		N01   , An4 
	.byte	W02
	.byte		VOL   , 47*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N02   , As4 
	.byte	W03
	.byte		VOL   , 47*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N02   , Bn4 
	.byte	W03
	.byte		VOL   , 47*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+28
	.byte		        c_v-4
	.byte		N02   , Cn5 
	.byte	W02
	.byte		VOL   , 47*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 66*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N02   , An4 
	.byte	W02
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N01   , As4 
	.byte	W01
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N02   , Bn4 
	.byte	W02
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+28
	.byte		        c_v-4
	.byte		N02   , Cn5 
	.byte	W02
	.byte		VOL   , 47*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+28
	.byte		        c_v-4
	.byte		N36   , Cs5 , v127, gtp1
	.byte	W18
	.byte		BEND  , c_v+5
	.byte	W04
	.byte		        c_v-9
	.byte	W04
	.byte		        c_v+5
	.byte	W04
	.byte		        c_v-9
	.byte	W04
	.byte		        c_v+5
	.byte	W04
	.byte		        c_v+29
	.byte		        c_v-3
	.byte		N36   , Dn5 
	.byte	W15
	.byte		BEND  , c_v-7
	.byte	W04
	.byte		        c_v+7
	.byte	W02
@ 001   ----------------------------------------
	.byte	W02
	.byte		        c_v-7
	.byte	W04
	.byte		        c_v+7
	.byte	W04
	.byte		        c_v-7
	.byte	W04
	.byte		        c_v+7
	.byte	W02
	.byte		        c_v-2
	.byte		N36   , Bn4 , v127, gtp1
	.byte	W16
	.byte		BEND  , c_v-6
	.byte	W04
	.byte		        c_v+7
	.byte	W04
	.byte		        c_v-6
	.byte	W04
	.byte		        c_v+7
	.byte	W04
	.byte		        c_v-6
	.byte	W04
	.byte		        c_v+7
	.byte	W02
	.byte		VOICE , 48
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+60
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W04
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		        c_v-2
	.byte		N13   , Fn3 
	.byte	W05
@ 002   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-3
	.byte	W01
	.byte		        c_v-1
	.byte		N14   , Dn3 
	.byte	W08
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-3
	.byte	W03
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-56
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W04
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N13   , Cn3 
	.byte	W06
	.byte		BEND  , c_v+2
	.byte	W03
	.byte		        c_v-2
	.byte	W03
	.byte		        c_v+2
	.byte	W01
	.byte		        c_v-10
	.byte		        c_v-1
	.byte		N14   , An2 
	.byte	W09
	.byte		BEND  , c_v-2
	.byte	W03
	.byte		        c_v+1
	.byte	W01
@ 003   ----------------------------------------
	.byte	W02
	.byte		        c_v-1
	.byte		N04   , Fs2 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N03   , Gs2 
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		        c_v-2
	.byte		N13   , Fn3 
	.byte	W08
	.byte		BEND  , c_v-3
	.byte	W03
	.byte		        c_v+1
	.byte	W03
	.byte		        c_v-1
	.byte		N14   , Dn3 
	.byte	W06
	.byte		BEND  , c_v-3
	.byte	W04
	.byte		        c_v+1
	.byte	W03
	.byte		        c_v-3
	.byte	W01
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-56
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W04
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W01
@ 004   ----------------------------------------
	.byte	W04
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N13   , Cn3 
	.byte	W08
	.byte		BEND  , c_v+2
	.byte	W03
	.byte		        c_v-2
	.byte	W03
	.byte		        c_v-10
	.byte		        c_v-1
	.byte		N14   , An2 
	.byte	W07
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-2
	.byte	W03
	.byte		        c_v+1
	.byte	W01
	.byte		        c_v-1
	.byte		N04   , Fs2 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N08   , Ds3 
	.byte	W09
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
@ 005   ----------------------------------------
	.byte	W01
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N09   , Ds3 
	.byte	W06
	.byte		BEND  , c_v-3
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W04
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N14   , An3 
	.byte	W06
	.byte		BEND  , c_v+3
	.byte	W04
	.byte		        c_v-3
	.byte	W03
	.byte		        c_v+3
	.byte	W02
	.byte		        c_v-2
	.byte		N08   , Fs3 
	.byte	W08
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		        c_v-9
	.byte		        c_v-1
	.byte		N04   , Fs2 
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-14
	.byte		        c_v-2
	.byte		N09   , Fs3 
	.byte	W08
	.byte		BEND  , c_v+1
	.byte	W01
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-1
	.byte		N04   , Fs2 
	.byte	W04
	.byte		BEND  , c_v-14
	.byte		        c_v-2
	.byte		N04   , Fs3 
	.byte	W02
@ 006   ----------------------------------------
	.byte	W03
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-2
	.byte		N14   , Cn4 
	.byte	W09
	.byte		BEND  , c_v-4
	.byte	W03
	.byte		        c_v+3
	.byte	W02
	.byte		        c_v-8
	.byte		        c_v-2
	.byte		N08   , Bn3 
	.byte	W08
	.byte		BEND  , c_v-4
	.byte	W01
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+9
	.byte		        c_v-2
	.byte		N09   , Bn3 
	.byte	W08
	.byte		BEND  , c_v+2
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W04
	.byte		BEND  , c_v+9
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		        c_v-2
	.byte		N14   , Fn4 
	.byte	W08
	.byte		BEND  , c_v-4
	.byte	W03
	.byte		        c_v+4
	.byte	W02
@ 007   ----------------------------------------
	.byte	W01
	.byte		        c_v-33
	.byte		        c_v-1
	.byte		N08   , En4 
	.byte	W06
	.byte		BEND  , c_v-4
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		        c_v-2
	.byte		N02   , Fs3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W07
	.byte		BEND  , c_v+4
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-2
	.byte		N01   , Fn3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-3
	.byte		N09   , Dn4 
	.byte	W08
	.byte		BEND  , c_v-5
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-6
	.byte		        c_v-1
	.byte		N02   , En3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N08   , Cs4 
	.byte	W07
	.byte		BEND  , c_v+3
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+3
	.byte		        c_v-1
	.byte		N02   , Ds3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-2
	.byte		N04   , Cn4 
	.byte	W04
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N04   , As3 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , An3 
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N03   , Gs2 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Bn2 
	.byte	W02
@ 008   ----------------------------------------
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+4
	.byte		        c_v-1
	.byte		N13   , Dn3 
	.byte	W08
	.byte		BEND  , c_v-3
	.byte	W03
	.byte		        c_v+1
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-60
	.byte		        c_v-1
	.byte		N04   , Dn3 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N14   , Fn3 
	.byte	W07
	.byte		BEND  , c_v-3
	.byte	W03
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-3
	.byte	W01
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W04
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N02   , Ds2 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N01   , Ds2 
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N04   , Ds3 
	.byte	W04
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N02   , Ds2 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
@ 009   ----------------------------------------
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N04   , En2 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		        c_v-1
	.byte		N02   , Fn2 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N01   
	.byte	W01
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Fs2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , Gn2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , An2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , As2 
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-64
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+4
	.byte		        c_v-1
	.byte		N13   , Dn3 
	.byte	W08
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-3
	.byte	W01
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-60
	.byte		        c_v-1
	.byte		N04   , Dn3 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N01   , Fn3 
	.byte		N14   
	.byte	W02
@ 010   ----------------------------------------
	.byte	W06
	.byte		BEND  , c_v+1
	.byte	W03
mus_casino_plus_8_3_B1:
	.byte		BEND  , c_v-3
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N04   , Dn3 , v127
	.byte	W04
	.byte		BEND  , c_v-9
	.byte		        c_v-1
	.byte		N02   , Dn2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-40
	.byte		        c_v-1
	.byte		N04   , Dn3 
	.byte	W04
	.byte		BEND  , c_v-9
	.byte		        c_v-1
	.byte		N02   , Dn2 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-55
	.byte		        c_v-1
	.byte		N02   , Cs3 
	.byte	W03
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N24   , Dn3 , v127, gtp1
	.byte	W07
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-4
	.byte	W03
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W03
	.byte		        c_v+1
	.byte	W03
	.byte		        c_v-4
	.byte	W02
	.byte		        c_v-33
	.byte		        c_v-1
	.byte		N04   , Cs3 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , Cn3 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , As2 
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-64
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W04
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
@ 011   ----------------------------------------
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		        c_v-2
	.byte		N13   , Fn3 
	.byte	W05
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W03
	.byte		        c_v+1
	.byte	W01
	.byte		        c_v-1
	.byte		N14   , Dn3 
	.byte	W07
	.byte		BEND  , c_v-4
	.byte	W03
	.byte		        c_v+1
	.byte	W03
	.byte		        c_v-4
	.byte	W02
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-56
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W03
@ 012   ----------------------------------------
	.byte	W02
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N13   , Cn3 
	.byte	W07
	.byte		BEND  , c_v+2
	.byte	W03
	.byte		        c_v-3
	.byte	W03
	.byte		        c_v+2
	.byte	W01
	.byte		        c_v-10
	.byte		        c_v-1
	.byte		N14   , An2 
	.byte	W07
	.byte		BEND  , c_v-3
	.byte	W04
	.byte		        c_v+1
	.byte	W03
	.byte		        c_v-3
	.byte	W01
	.byte		        c_v-1
	.byte		N04   , Fs2 
	.byte	W04
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N03   , Gs2 
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		        c_v-2
	.byte		N13   , Fn3 
	.byte	W07
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W03
	.byte		        c_v-1
	.byte		N14   , Dn3 
	.byte	W01
@ 013   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-4
	.byte	W03
	.byte		        c_v+1
	.byte	W03
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-56
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W04
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N13   , Cn3 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte	W03
	.byte		        c_v+2
	.byte	W03
	.byte		        c_v-3
	.byte	W03
	.byte		        c_v-10
	.byte		        c_v-1
	.byte		N14   , An2 
	.byte	W05
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-3
	.byte	W04
	.byte		        c_v+1
	.byte	W02
	.byte		        c_v-1
	.byte		N04   , Fs2 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W03
@ 014   ----------------------------------------
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N08   , Ds3 
	.byte	W05
	.byte		BEND  , c_v-4
	.byte	W04
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N09   , Ds3 
	.byte	W04
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W01
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W04
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N14   , An3 
	.byte	W06
	.byte		BEND  , c_v+3
	.byte	W04
	.byte		        c_v-4
	.byte	W03
	.byte		        c_v+3
	.byte	W01
	.byte		        c_v-2
	.byte		N08   , Fs3 
	.byte	W07
	.byte		BEND  , c_v-5
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-1
	.byte		N04   , Fs2 
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W01
@ 015   ----------------------------------------
	.byte	W04
	.byte		N01   
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-14
	.byte		        c_v-2
	.byte		N09   , Fs3 
	.byte	W06
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-5
	.byte	W01
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-1
	.byte		N04   , Fs2 
	.byte	W04
	.byte		BEND  , c_v-14
	.byte		        c_v-2
	.byte		N04   , Fs3 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-2
	.byte		N14   , Cn4 
	.byte	W07
	.byte		BEND  , c_v+3
	.byte	W03
	.byte		        c_v-6
	.byte	W03
	.byte		        c_v+3
	.byte	W01
	.byte		        c_v-8
	.byte		        c_v-2
	.byte		N08   , Bn3 
	.byte	W07
	.byte		BEND  , c_v-6
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+9
	.byte		        c_v-2
	.byte		N09   , Bn3 
	.byte	W04
@ 016   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v+2
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W04
	.byte		BEND  , c_v+9
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		        c_v-2
	.byte		N14   , Fn4 
	.byte	W05
	.byte		BEND  , c_v-7
	.byte	W03
	.byte		        c_v+4
	.byte	W04
	.byte		        c_v-7
	.byte	W03
	.byte		        c_v-33
	.byte		        c_v-1
	.byte		N08   , En4 
	.byte	W05
	.byte		BEND  , c_v+5
	.byte	W03
	.byte		        c_v-7
	.byte	W01
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		        c_v-2
	.byte		N02   , Fs3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W07
	.byte		BEND  , c_v+4
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-2
	.byte		N01   , Fn3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-3
	.byte		N09   , Dn4 
	.byte	W06
	.byte		BEND  , c_v-7
	.byte	W03
	.byte		        c_v+2
	.byte	W01
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-6
	.byte		        c_v-1
	.byte		N02   , En3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N08   , Cs4 
	.byte	W07
	.byte		BEND  , c_v-6
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+3
	.byte		        c_v-1
	.byte		N02   , Ds3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-2
	.byte		N04   , Cn4 
	.byte	W05
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W02
@ 017   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N04   , As3 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , An3 
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N03   , Gs2 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+4
	.byte		        c_v-1
	.byte		N13   , Dn3 
	.byte	W06
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W03
	.byte		        c_v+1
	.byte	W01
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-60
	.byte		        c_v-1
	.byte		N04   , Dn3 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N14   , Fn3 
	.byte	W07
	.byte		BEND  , c_v-4
	.byte	W03
	.byte		        c_v+1
	.byte	W04
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-4
	.byte		        c_v+5
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
@ 018   ----------------------------------------
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N02   , Ds2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N01   , Ds2 
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N04   , Ds3 
	.byte	W04
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N02   , Ds2 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N04   , En2 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		        c_v-1
	.byte		N02   , Fn2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N01   
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Fs2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , Gn2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , An2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , As2 
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-64
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Bn2 
	.byte	W04
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+4
	.byte		        c_v-1
	.byte		N13   , Dn3 
	.byte	W07
@ 019   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-4
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-60
	.byte		        c_v-1
	.byte		N04   , Dn3 
	.byte	W04
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N14   , Fn3 
	.byte	W05
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-4
	.byte	W04
	.byte	GOTO
	 .word	mus_casino_plus_8_3_B1
mus_casino_plus_8_3_B2:
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N04   , Dn3 , v127
	.byte	W04
	.byte		BEND  , c_v-9
	.byte		        c_v-1
	.byte		N02   , Dn2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-40
	.byte		        c_v-1
	.byte		N04   , Dn3 
	.byte	W04
	.byte		BEND  , c_v-9
	.byte		        c_v-1
	.byte		N02   , Dn2 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-55
	.byte		        c_v-1
	.byte		N02   , Cs3 
	.byte	W03
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N24   , Dn3 , v127, gtp1
	.byte	W07
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-4
	.byte	W03
	.byte		        c_v+1
	.byte	W03
	.byte		        c_v-4
	.byte	W04
	.byte		        c_v+1
	.byte	W01
@ 020   ----------------------------------------
	.byte	W02
	.byte		        c_v-4
	.byte	W02
	.byte		        c_v-33
	.byte		        c_v-1
	.byte		N04   , Cs3 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , Cn3 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , As2 
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-64
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W04
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		        c_v-2
	.byte		N13   , Fn3 
	.byte	W05
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-4
	.byte	W04
	.byte		        c_v+1
	.byte	W01
	.byte		        c_v-1
	.byte		N14   , Dn3 
	.byte	W07
	.byte		BEND  , c_v-4
	.byte	W03
	.byte		        c_v+1
	.byte	W03
	.byte		        c_v-4
	.byte	W02
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W02
@ 021   ----------------------------------------
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-56
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N13   , Cn3 
	.byte	W07
	.byte		BEND  , c_v+2
	.byte	W03
	.byte		        c_v-3
	.byte	W03
	.byte		        c_v+2
	.byte	W01
	.byte		        c_v-10
	.byte		        c_v-1
	.byte		N14   , An2 
	.byte	W07
	.byte		BEND  , c_v-3
	.byte	W03
	.byte		        c_v+1
	.byte	W04
	.byte		        c_v-3
	.byte		        c_v-1
	.byte		N04   , Fs2 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N03   , Gs2 
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
@ 022   ----------------------------------------
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		        c_v-2
	.byte		N13   , Fn3 
	.byte	W07
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W03
	.byte		        c_v-1
	.byte		N14   , Dn3 
	.byte	W05
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-4
	.byte	W03
	.byte		        c_v+1
	.byte	W03
	.byte		        c_v+12
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-56
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W04
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-1
	.byte		N13   , Cn3 
	.byte	W03
@ 023   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-3
	.byte	W03
	.byte		        c_v+2
	.byte	W03
	.byte		        c_v-3
	.byte	W03
	.byte		        c_v-10
	.byte		        c_v-1
	.byte		N14   , An2 
	.byte	W05
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-3
	.byte	W04
	.byte		        c_v+1
	.byte	W02
	.byte		        c_v-1
	.byte		N04   , Fs2 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+24
	.byte		        c_v-1
	.byte		N08   , Ds3 
	.byte	W05
	.byte		BEND  , c_v-4
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N09   , Ds3 
	.byte	W04
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W01
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W04
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N14   , An3 
	.byte	W01
@ 024   ----------------------------------------
	.byte	W05
	.byte		BEND  , c_v+3
	.byte	W04
	.byte		        c_v-4
	.byte	W03
	.byte		        c_v+3
	.byte	W01
	.byte		        c_v-2
	.byte		N08   , Fs3 
	.byte	W07
	.byte		BEND  , c_v-5
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-1
	.byte		N04   , Fs2 
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N01   
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-14
	.byte		        c_v-2
	.byte		N09   , Fs3 
	.byte	W06
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-5
	.byte	W01
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-1
	.byte		N04   , Fs2 
	.byte	W04
	.byte		BEND  , c_v-14
	.byte		        c_v-2
	.byte		N04   , Fs3 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-2
	.byte		N14   , Cn4 
	.byte	W07
	.byte		BEND  , c_v+3
	.byte	W03
	.byte		        c_v-6
	.byte	W03
	.byte		        c_v+3
	.byte	W01
	.byte		        c_v-8
	.byte		        c_v-2
	.byte		N08   , Bn3 
	.byte	W07
	.byte		BEND  , c_v-6
	.byte	W01
@ 025   ----------------------------------------
	.byte	W01
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N01   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+9
	.byte		        c_v-2
	.byte		N09   , Bn3 
	.byte	W06
	.byte		BEND  , c_v+2
	.byte	W04
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-20
	.byte		        c_v-1
	.byte		N04   , Bn2 
	.byte	W04
	.byte		BEND  , c_v+9
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		        c_v-2
	.byte		N14   , Fn4 
	.byte	W05
	.byte		BEND  , c_v-7
	.byte	W03
	.byte		        c_v+4
	.byte	W04
	.byte		        c_v-7
	.byte	W03
	.byte		        c_v-33
	.byte		        c_v-1
	.byte		N08   , En4 
	.byte	W05
	.byte		BEND  , c_v+5
	.byte	W03
	.byte		        c_v-7
	.byte	W01
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		        c_v-2
	.byte		N02   , Fs3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-1
	.byte		N09   , Ds4 
	.byte	W07
	.byte		BEND  , c_v+4
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-2
	.byte		N01   , Fn3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-3
	.byte		N09   , Dn4 
	.byte	W02
@ 026   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v-7
	.byte	W03
	.byte		        c_v+2
	.byte	W01
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-6
	.byte		        c_v-1
	.byte		N02   , En3 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N08   , Cs4 
	.byte	W07
	.byte		BEND  , c_v-6
	.byte	W01
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+3
	.byte		        c_v-1
	.byte		N02   , Ds3 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v-2
	.byte		N04   , Cn4 
	.byte	W05
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N04   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N04   , As3 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N04   , An3 
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N03   , Gs2 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Bn2 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+4
	.byte		        c_v-1
	.byte		N13   , Dn3 
	.byte	W06
	.byte		BEND  , c_v+1
	.byte	W04
	.byte		        c_v-4
	.byte	W03
	.byte		        c_v+1
	.byte	W01
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
@ 027   ----------------------------------------
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-60
	.byte		        c_v-1
	.byte		N04   , Dn3 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N14   , Fn3 
	.byte	W07
	.byte		BEND  , c_v-4
	.byte	W03
	.byte		        c_v+1
	.byte	W03
	.byte		        c_v-4
	.byte	W01
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N04   , Ds2 
	.byte	W04
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N02   , Ds2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N01   , Ds2 
	.byte	W01
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N04   , Ds3 
	.byte	W05
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N02   , Ds2 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N04   , En2 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		        c_v-1
	.byte		N02   , Fn2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N01   
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , Fs2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , Gn2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W04
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , An2 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N04   , As2 
	.byte	W02
@ 028   ----------------------------------------
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-64
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N04   , Bn2 
	.byte	W04
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+4
	.byte		        c_v-1
	.byte		N13   , Dn3 
	.byte	W08
	.byte		BEND  , c_v+1
	.byte	W03
	.byte		        c_v-4
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N04   , Gs2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_8_mvl/mxv
	.byte		N04   
	.byte	W04
	.byte		N04   
	.byte	W05
	.byte		BEND  , c_v-60
	.byte		        c_v-1
	.byte		N04   , Dn3 
	.byte	W04
	.byte		VOL   , 109*mus_casino_plus_8_mvl/mxv
	.byte		BEND  , c_v-2
	.byte	W05
	.byte		        c_v+1
	.byte	W03
	.byte		        c_v-4
	.byte	W04
	.byte		        c_v+1
	.byte	FINE

@**************** Track 4 (Midi-Chn.4) ****************@

mus_casino_plus_8_4:
	.byte	KEYSH , mus_casino_plus_8_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 47
	.byte		VOL   , 106*mus_casino_plus_8_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		BEND  , c_v+0
	.byte		        c_v-13
	.byte	W96
@ 001   ----------------------------------------
	.byte	W54
	.byte		N02   , Gs1 , v127
	.byte	W18
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W05
@ 002   ----------------------------------------
	.byte	W09
	.byte		N02   
	.byte	W09
	.byte		N02   
	.byte	W15
	.byte		N02   
	.byte	W18
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W03
@ 003   ----------------------------------------
	.byte	W11
	.byte		N02   
	.byte	W19
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W10
@ 004   ----------------------------------------
	.byte	W09
	.byte		N02   
	.byte	W04
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W09
	.byte		N02   
	.byte	W15
	.byte		N02   
	.byte	W18
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W08
@ 005   ----------------------------------------
	.byte	W06
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W15
	.byte		N02   
	.byte	W18
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W02
@ 006   ----------------------------------------
	.byte	W08
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W19
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W13
@ 007   ----------------------------------------
	.byte	W10
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W09
	.byte		N02   
	.byte	W15
	.byte		N02   
	.byte	W18
	.byte		N02   
	.byte	W02
@ 008   ----------------------------------------
	.byte	W03
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W15
	.byte		N02   
	.byte	W18
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W04
@ 009   ----------------------------------------
	.byte	W09
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W19
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W02
@ 010   ----------------------------------------
	.byte	W09
mus_casino_plus_8_4_B1:
	.byte	W03
	.byte		N02   , Gs1 , v127
	.byte	W19
	.byte		N02   
	.byte	W04
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W04
	.byte		N04   , Gs3 
	.byte	W05
	.byte		N04   
	.byte	W15
	.byte		N02   , Gs1 
	.byte	W09
@ 011   ----------------------------------------
	.byte	W09
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W15
	.byte		N02   
	.byte	W18
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W07
@ 012   ----------------------------------------
	.byte	W07
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W19
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W01
@ 013   ----------------------------------------
	.byte	W09
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W18
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W09
	.byte		N02   
	.byte	W13
@ 014   ----------------------------------------
	.byte	W02
	.byte		N02   
	.byte	W18
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W15
	.byte		N02   
	.byte	W18
	.byte		N02   
	.byte	W01
@ 015   ----------------------------------------
	.byte	W04
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W19
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W04
@ 016   ----------------------------------------
	.byte	W10
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W23
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W09
	.byte		N02   
	.byte	W02
@ 017   ----------------------------------------
	.byte	W13
	.byte		N02   
	.byte	W18
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W15
	.byte		N02   
	.byte	W08
@ 018   ----------------------------------------
	.byte	W10
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W19
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W06
@ 019   ----------------------------------------
	.byte	W07
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W09
	.byte		N02   
	.byte	W12
	.byte	GOTO
	 .word	mus_casino_plus_8_4_B1
mus_casino_plus_8_4_B2:
	.byte	W03
	.byte		N02   , Gs1 , v127
	.byte	W18
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W14
@ 020   ----------------------------------------
	.byte		N02   
	.byte	W04
	.byte		N04   , Gs3 
	.byte	W05
	.byte		N04   
	.byte	W15
	.byte		N02   , Gs1 
	.byte	W18
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W12
@ 021   ----------------------------------------
	.byte	W02
	.byte		N02   
	.byte	W19
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W19
@ 022   ----------------------------------------
	.byte		N02   
	.byte	W04
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W09
	.byte		N02   
	.byte	W15
	.byte		N02   
	.byte	W18
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W03
@ 023   ----------------------------------------
	.byte	W11
	.byte		N02   
	.byte	W09
	.byte		N02   
	.byte	W15
	.byte		N02   
	.byte	W18
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W01
@ 024   ----------------------------------------
	.byte	W13
	.byte		N02   
	.byte	W19
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W08
@ 025   ----------------------------------------
	.byte	W11
	.byte		N02   
	.byte	W04
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W09
	.byte		N02   
	.byte	W24
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W06
@ 026   ----------------------------------------
	.byte	W08
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W09
	.byte		N02   
	.byte	W15
	.byte		N02   
	.byte	W18
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W13
@ 027   ----------------------------------------
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W19
	.byte		N02   
	.byte	W05
	.byte		N02   
	.byte	W13
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W10
	.byte		N02   
	.byte	W11
@ 028   ----------------------------------------
	.byte	W03
	.byte		N02   
	.byte	W19
	.byte		N02   
	.byte	W04
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W14
	.byte		N02   
	.byte	W09
	.byte		N02   
	.byte	W12
	.byte	FINE

@**************** Track 5 (Midi-Chn.10) ****************@

mus_casino_plus_8_5:
	.byte	KEYSH , mus_casino_plus_8_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 0
	.byte		VOL   , 81*mus_casino_plus_8_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		BEND  , c_v+0
	.byte		        c_v-13
	.byte	W96
@ 001   ----------------------------------------
	.byte	W60
	.byte	W03
	.byte		N09   , En1 , v127
	.byte	W18
	.byte		N09   
	.byte	W15
@ 002   ----------------------------------------
	.byte	W04
	.byte		N04   
	.byte	W19
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W19
	.byte		N09   
	.byte	W19
	.byte		N04   
	.byte	W17
@ 003   ----------------------------------------
	.byte	W02
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W19
	.byte		N09   
	.byte	W19
	.byte		N04   
	.byte	W18
	.byte		N09   
	.byte	W19
	.byte		N09   
	.byte	W01
@ 004   ----------------------------------------
	.byte	W17
	.byte		N09   
	.byte	W20
	.byte		N04   
	.byte	W18
	.byte		N09   
	.byte	W19
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W04
@ 005   ----------------------------------------
	.byte	W15
	.byte		N04   
	.byte	W19
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W19
	.byte		N09   
	.byte	W19
	.byte		N04   
	.byte	W06
@ 006   ----------------------------------------
	.byte	W13
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W19
	.byte		N09   
	.byte	W19
	.byte		N04   
	.byte	W18
	.byte		N09   
	.byte	W09
@ 007   ----------------------------------------
	.byte	W01
	.byte		N08   
	.byte	W14
	.byte		N09   
	.byte	W13
	.byte		N09   
	.byte	W15
	.byte		N08   
	.byte	W14
	.byte		N04   
	.byte	W09
	.byte		N04   
	.byte	W05
	.byte		N04   
	.byte	W14
	.byte		N09   
	.byte	W11
@ 008   ----------------------------------------
	.byte	W07
	.byte		N09   
	.byte	W19
	.byte		N04   
	.byte	W19
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W19
	.byte		N09   
	.byte	W14
@ 009   ----------------------------------------
	.byte	W05
	.byte		N04   
	.byte	W19
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W19
	.byte		N09   
	.byte	W19
	.byte		N04   
	.byte	W16
@ 010   ----------------------------------------
	.byte	W02
	.byte		N09   
	.byte	W07
mus_casino_plus_8_5_B1:
	.byte	W12
	.byte		N09   , En1 , v127
	.byte	W18
	.byte		N09   
	.byte	W20
	.byte		N04   
	.byte	W18
	.byte		N04   
	.byte	W05
	.byte		N04   
	.byte	W14
@ 011   ----------------------------------------
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W19
	.byte		N04   
	.byte	W19
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W19
	.byte		N09   
	.byte	W03
@ 012   ----------------------------------------
	.byte	W16
	.byte		N04   
	.byte	W19
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W19
	.byte		N09   
	.byte	W19
	.byte		N04   
	.byte	W05
@ 013   ----------------------------------------
	.byte	W13
	.byte		N09   
	.byte	W19
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W20
	.byte		N04   
	.byte	W18
	.byte		N09   
	.byte	W08
@ 014   ----------------------------------------
	.byte	W11
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W19
	.byte		N04   
	.byte	W19
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W11
@ 015   ----------------------------------------
	.byte	W08
	.byte		N09   
	.byte	W19
	.byte		N04   
	.byte	W19
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W19
	.byte		N09   
	.byte	W13
@ 016   ----------------------------------------
	.byte	W06
	.byte		N04   
	.byte	W18
	.byte		N09   
	.byte	W10
	.byte		N08   
	.byte	W14
	.byte		N09   
	.byte	W13
	.byte		N09   
	.byte	W15
	.byte		N08   
	.byte	W13
	.byte		N04   
	.byte	W07
@ 017   ----------------------------------------
	.byte	W03
	.byte		N04   
	.byte	W05
	.byte		N04   
	.byte	W14
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W19
	.byte		N04   
	.byte	W19
	.byte		N09   
	.byte	W18
@ 018   ----------------------------------------
	.byte		N09   
	.byte	W19
	.byte		N09   
	.byte	W19
	.byte		N04   
	.byte	W19
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W03
@ 019   ----------------------------------------
	.byte	W17
	.byte		N04   
	.byte	W18
	.byte		N09   
	.byte	W07
	.byte	GOTO
	 .word	mus_casino_plus_8_5_B1
mus_casino_plus_8_5_B2:
	.byte	W12
	.byte		N09   , En1 , v127
	.byte	W18
	.byte		N09   
	.byte	W20
	.byte		N04   
	.byte	W04
@ 020   ----------------------------------------
	.byte	W14
	.byte		N04   
	.byte	W05
	.byte		N04   
	.byte	W14
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W19
	.byte		N04   
	.byte	W19
	.byte		N09   
	.byte	W07
@ 021   ----------------------------------------
	.byte	W11
	.byte		N09   
	.byte	W19
	.byte		N09   
	.byte	W19
	.byte		N04   
	.byte	W19
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W10
@ 022   ----------------------------------------
	.byte	W08
	.byte		N09   
	.byte	W20
	.byte		N04   
	.byte	W18
	.byte		N09   
	.byte	W19
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W13
@ 023   ----------------------------------------
	.byte	W06
	.byte		N04   
	.byte	W19
	.byte		N09   
	.byte	W19
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W19
	.byte		N04   
	.byte	W15
@ 024   ----------------------------------------
	.byte	W04
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W19
	.byte		N09   
	.byte	W19
	.byte		N04   
	.byte	W18
	.byte		N09   
	.byte	W18
@ 025   ----------------------------------------
	.byte	W01
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W20
	.byte		N04   
	.byte	W18
	.byte		N09   
	.byte	W10
	.byte		N08   
	.byte	W14
	.byte		N09   
	.byte	W13
	.byte		N09   
	.byte	W02
@ 026   ----------------------------------------
	.byte	W13
	.byte		N08   
	.byte	W13
	.byte		N04   
	.byte	W10
	.byte		N04   
	.byte	W05
	.byte		N04   
	.byte	W13
	.byte		N09   
	.byte	W19
	.byte		N09   
	.byte	W19
	.byte		N04   
	.byte	W04
@ 027   ----------------------------------------
	.byte	W15
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W19
	.byte		N09   
	.byte	W19
	.byte		N04   
	.byte	W18
	.byte		N09   
	.byte	W07
@ 028   ----------------------------------------
	.byte	W12
	.byte		N09   
	.byte	W18
	.byte		N09   
	.byte	W20
	.byte		N04   
	.byte	W24
	.byte	W01
	.byte	FINE

@******************************************************@
	.align	2

mus_casino_plus_8:
	.byte	5	@ NumTrks
	.byte	0	@ NumBlks
	.byte	mus_casino_plus_8_pri	@ Priority
	.byte	mus_casino_plus_8_rev	@ Reverb.

	.word	mus_casino_plus_8_grp

	.word	mus_casino_plus_8_1
	.word	mus_casino_plus_8_2
	.word	mus_casino_plus_8_3
	.word	mus_casino_plus_8_4
	.word	mus_casino_plus_8_5

	.end
