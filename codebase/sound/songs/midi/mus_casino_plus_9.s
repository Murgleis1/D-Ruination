	.include "MPlayDef.s"

	.equ	mus_casino_plus_9_grp, voicegroup163
	.equ	mus_casino_plus_9_pri, 0
	.equ	mus_casino_plus_9_rev, reverb_set+50
	.equ	mus_casino_plus_9_mvl, 90
	.equ	mus_casino_plus_9_key, 0
	.equ	mus_casino_plus_9_tbs, 1
	.equ	mus_casino_plus_9_exg, 1
	.equ	mus_casino_plus_9_cmp, 1

	.section .rodata
	.global	mus_casino_plus_9
	.align	2

@**************** Track 1 (Midi-Chn.1) ****************@

mus_casino_plus_9_1:
	.byte	KEYSH , mus_casino_plus_9_key+0
@ 000   ----------------------------------------
	.byte	TEMPO , 120*mus_casino_plus_9_tbs/2
	.byte		VOICE , 33
	.byte		VOL   , 127*mus_casino_plus_9_mvl/mxv
	.byte		        64*mus_casino_plus_9_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		BEND  , c_v-13
	.byte		        c_v+50
	.byte		        c_v-1
	.byte		N01   , Cn0 , v127
	.byte		N01   
	.byte		N05   , Bn0 
	.byte		N01   , Cn1 
	.byte	W40
	.byte	W01
	.byte		BEND  , c_v-50
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W11
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W24
	.byte		N05   
	.byte	W11
mus_casino_plus_9_1_B1:
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N05   , En1 , v127
	.byte		N01   , Fs1 
	.byte		N01   , Bn1 
	.byte	W04
@ 001   ----------------------------------------
	.byte	W08
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+5
	.byte		        c_v-3
	.byte		N01   , Cs1 
	.byte		N01   , En1 
	.byte		N02   , Gn3 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N03   , Gs3 
	.byte	W06
	.byte		N03   
	.byte	W11
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N06   , Fs0 
	.byte		N01   , Gs3 
	.byte		N01   , As3 
	.byte	W07
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W22
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W23
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N05   , As0 
	.byte	W08
@ 002   ----------------------------------------
	.byte	W32
	.byte	W01
	.byte		BEND  , c_v-1
	.byte		        c_v-50
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N06   , An0 
	.byte	W12
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W23
	.byte		N06   
	.byte	W12
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Fs1 
	.byte		N01   , Bn1 
	.byte	W11
@ 003   ----------------------------------------
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+5
	.byte		        c_v-3
	.byte		N01   , Cs1 
	.byte		N01   , En1 
	.byte		N03   , Gn3 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		N03   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N03   , Gs3 
	.byte	W07
	.byte		N02   
	.byte	W11
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Gs3 
	.byte		N01   , As3 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W23
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W23
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N05   , As0 
	.byte	W15
@ 004   ----------------------------------------
	.byte	W24
	.byte	W01
	.byte		BEND  , c_v-1
	.byte		        c_v-50
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Bn0 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W11
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W24
	.byte		N05   
	.byte	W11
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Fs1 
	.byte		N01   , Bn1 
	.byte	W19
@ 005   ----------------------------------------
	.byte	W21
	.byte		BEND  , c_v-8
	.byte		        c_v+0
	.byte		N06   , Fs0 
	.byte		N01   , Dn1 
	.byte		N01   , En1 
	.byte	W07
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W22
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W23
	.byte		BEND  , c_v-1
	.byte		        c_v-37
	.byte		        c_v-1
	.byte		N01   , As0 
	.byte		N05   , Cs1 
	.byte	W23
@ 006   ----------------------------------------
	.byte	W17
	.byte		BEND  , c_v+24
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Cs1 
	.byte	W06
	.byte		BEND  , c_v+14
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N06   , As0 
	.byte	W12
	.byte		BEND  , c_v-46
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W23
	.byte		N06   
	.byte	W12
	.byte		BEND  , c_v+8
	.byte		        c_v-1
	.byte		N05   , Ds1 
	.byte		N01   , Fs1 
	.byte		N01   , An1 
	.byte	W24
	.byte	W02
@ 007   ----------------------------------------
	.byte	W14
	.byte		BEND  , c_v-40
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Ds1 
	.byte	W06
	.byte		BEND  , c_v-39
	.byte		        c_v+0
	.byte		N01   , Fs0 
	.byte		N05   , Gs0 
	.byte	W23
	.byte		BEND  , c_v+63
	.byte		N05   
	.byte	W23
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N05   , As0 
	.byte	W30
@ 008   ----------------------------------------
	.byte	W10
	.byte		BEND  , c_v-1
	.byte		        c_v-50
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Bn0 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W11
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W24
	.byte		N05   
	.byte	W11
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Fs1 
	.byte		N01   , Bn1 
	.byte	W32
	.byte	W02
@ 009   ----------------------------------------
	.byte	W06
	.byte		BEND  , c_v-3
	.byte		        c_v+0
	.byte		N06   , Gs0 
	.byte		N01   , Cn1 
	.byte		N01   , En1 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N01   , Gs0 
	.byte		N05   , Bn0 
	.byte	W23
	.byte		BEND  , c_v+5
	.byte		        c_v+0
	.byte		N01   
	.byte		N05   , En1 
	.byte	W23
	.byte		N05   
	.byte	W36
	.byte	W02
@ 010   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N05   , Cs1 
	.byte		N01   , En1 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Cs1 
	.byte		N06   , Fs1 
	.byte	W12
	.byte		BEND  , c_v-1
	.byte		N01   
	.byte		N05   , As1 
	.byte	W23
	.byte		N06   
	.byte	W12
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W40
	.byte	W01
@ 011   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		        c_v-20
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , Bn1 
	.byte	W44
	.byte	W03
	.byte		N05   , Bn0 
	.byte	W40
	.byte		BEND  , c_v-50
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Bn0 
	.byte	W05
@ 012   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W11
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W23
	.byte		N05   
	.byte	W12
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Fs1 
	.byte		N01   , Bn1 
	.byte	W12
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+5
	.byte		        c_v-3
	.byte		N01   , Cs1 
	.byte		N01   , En1 
	.byte		N02   , Gn3 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N03   , Gs3 
	.byte	W06
	.byte		N03   
	.byte	W11
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N06   , Fs0 
	.byte		N01   , Gs3 
	.byte		N01   , As3 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W03
@ 013   ----------------------------------------
	.byte	W20
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W23
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N05   , As0 
	.byte	W40
	.byte		BEND  , c_v-1
	.byte		        c_v-50
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Bn0 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N06   , An0 
	.byte	W07
@ 014   ----------------------------------------
	.byte	W05
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W22
	.byte		N06   
	.byte	W13
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Fs1 
	.byte		N01   , Bn1 
	.byte	W11
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+5
	.byte		        c_v-3
	.byte		N01   , Cs1 
	.byte		N01   , En1 
	.byte		N03   , Gn3 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		N03   
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N03   , Gs3 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Gs3 
	.byte		N01   , As3 
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W11
@ 015   ----------------------------------------
	.byte	W13
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-10
	.byte		        c_v-2
	.byte		N01   
	.byte		N23   , Fn3 
	.byte	W23
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , Fn3 
	.byte		N01   , An5 
	.byte	W11
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-38
	.byte		        c_v-3
	.byte		N01   , Bn0 
	.byte		N05   , Dn4 
	.byte	W06
	.byte		BEND  , c_v+28
	.byte		N03   
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		N03   , Ds4 
	.byte	W06
	.byte		N03   
	.byte	W12
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , As3 
	.byte		N01   , Ds4 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W11
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W03
@ 016   ----------------------------------------
	.byte	W20
	.byte		N05   
	.byte	W12
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Fs1 
	.byte		N01   , Bn1 
	.byte	W12
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-53
	.byte		        c_v-4
	.byte		N01   , En1 
	.byte		N05   , Ds4 
	.byte	W05
	.byte		BEND  , c_v+28
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v-4
	.byte		N03   , En4 
	.byte	W05
	.byte		N03   
	.byte	W12
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N06   , Fs0 
	.byte		N01   , As3 
	.byte		N01   , En4 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W18
@ 017   ----------------------------------------
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W23
	.byte		BEND  , c_v-1
	.byte		        c_v-37
	.byte		        c_v-1
	.byte		N01   , As0 
	.byte		N05   , Cs1 
	.byte	W11
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+43
	.byte		        c_v-4
	.byte		N01   
	.byte		N06   , Ds4 
	.byte	W07
	.byte		BEND  , c_v+28
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		N02   , En4 
	.byte	W06
	.byte		N02   
	.byte	W11
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , As3 
	.byte		N01   , En4 
	.byte	W06
	.byte		BEND  , c_v+14
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N06   , As0 
	.byte	W12
	.byte		BEND  , c_v-46
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W10
@ 018   ----------------------------------------
	.byte	W12
	.byte		N06   
	.byte	W12
	.byte		BEND  , c_v+8
	.byte		        c_v-1
	.byte		N05   , Ds1 
	.byte		N01   , Fs1 
	.byte		N01   , An1 
	.byte	W12
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-25
	.byte		        c_v-3
	.byte		N01   , Ds1 
	.byte		N05   , Dn4 
	.byte	W05
	.byte		BEND  , c_v+28
	.byte		N03   
	.byte	W06
	.byte		BEND  , c_v-4
	.byte		N03   , Ds4 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , As3 
	.byte		N01   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-39
	.byte		        c_v+0
	.byte		N01   , Fs0 
	.byte		N05   , Gs0 
	.byte	W23
	.byte		BEND  , c_v+63
	.byte		N05   
	.byte	W03
@ 019   ----------------------------------------
	.byte	W21
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N05   , As0 
	.byte	W11
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		        c_v-38
	.byte		        c_v-3
	.byte		N01   , Bn0 
	.byte		N05   , Dn4 
	.byte	W06
	.byte		BEND  , c_v+28
	.byte		N03   
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		N03   , Ds4 
	.byte	W06
	.byte		N03   
	.byte	W12
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , As3 
	.byte		N01   , Ds4 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W11
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W18
@ 020   ----------------------------------------
	.byte	W05
	.byte		N05   
	.byte	W11
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Fs1 
	.byte		N01   , Bn1 
	.byte	W13
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-53
	.byte		        c_v-4
	.byte		N01   , En1 
	.byte		N05   , Ds4 
	.byte	W05
	.byte		BEND  , c_v+28
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v-4
	.byte		N03   , En4 
	.byte	W05
	.byte		N03   
	.byte	W12
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-4
	.byte		        c_v+0
	.byte		N06   , Gs0 
	.byte		N01   , Cs3 
	.byte		N01   , En4 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N01   , Gs0 
	.byte		N05   , Bn0 
	.byte	W23
	.byte		BEND  , c_v+5
	.byte		        c_v+0
	.byte		N01   
	.byte		N05   , En1 
	.byte	W10
@ 021   ----------------------------------------
	.byte	W13
	.byte		N05   
	.byte	W11
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-53
	.byte		        c_v-4
	.byte		N01   
	.byte		N06   , Ds4 
	.byte	W07
	.byte		BEND  , c_v+28
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		N02   , En4 
	.byte	W06
	.byte		N02   
	.byte	W11
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		        c_v-1
	.byte		N05   , Cs1 
	.byte		N01   , Fs3 
	.byte		N01   , En4 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Cs1 
	.byte		N06   , Fs1 
	.byte	W12
	.byte		BEND  , c_v-1
	.byte		N01   
	.byte		N05   , As1 
	.byte	W22
	.byte		N06   
	.byte	W03
@ 022   ----------------------------------------
	.byte	W09
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W12
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		        c_v+6
	.byte		        c_v-3
	.byte		N01   , Gs1 
	.byte		N01   , Bn1 
	.byte		N05   , Dn4 
	.byte	W05
	.byte		BEND  , c_v+28
	.byte		N03   
	.byte	W06
	.byte		BEND  , c_v-4
	.byte		N03   , Ds4 
	.byte	W06
	.byte		N02   
	.byte	W11
	.byte		N03   
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , Ds4 
	.byte		N01   , An5 
	.byte	W06
	.byte		BEND  , c_v-35
	.byte		        c_v-4
	.byte		N01   , Bn0 
	.byte		N03   , Ds4 
	.byte	W12
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W11
	.byte		N03   
	.byte	W11
	.byte		N03   
	.byte	W01
@ 023   ----------------------------------------
	.byte	W06
	.byte		BEND  , c_v-14
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Ds4 
	.byte		N01   , Ds6 
	.byte	W22
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-39
	.byte		        c_v-3
	.byte		N01   , En1 
	.byte		N05   , Gn4 
	.byte	W06
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		N03   
	.byte	W12
	.byte		BEND  , c_v-1
	.byte		        c_v-14
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Gs4 
	.byte		N01   , Ds6 
	.byte	W11
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , En1 
	.byte	W11
	.byte		BEND  , c_v-64
	.byte		        c_v-1
	.byte		N01   , Bn0 
	.byte		N06   , Ds2 
	.byte	W07
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		        c_v-4
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , En2 
	.byte		N01   , As2 
	.byte	W06
	.byte		BEND  , c_v-11
	.byte		        c_v-1
	.byte		N01   , Dn1 
	.byte		N01   , En1 
	.byte		N05   , En2 
	.byte	W04
@ 024   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N05   , Ds1 
	.byte		N01   , En2 
	.byte		N01   , Gn2 
	.byte	W24
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-13
	.byte		        c_v-2
	.byte		N01   , Ds1 
	.byte		N05   , Fn4 
	.byte	W05
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+29
	.byte		N03   
	.byte	W11
	.byte		BEND  , c_v-3
	.byte		        c_v-4
	.byte		        c_v-1
	.byte		N06   , Ds1 
	.byte		N01   , Fs4 
	.byte		N01   , An4 
	.byte	W13
	.byte		BEND  , c_v-3
	.byte		        c_v+0
	.byte		N05   , Gs0 
	.byte		N01   , Cn1 
	.byte		N01   , Ds1 
	.byte	W11
	.byte		BEND  , c_v+21
	.byte		        c_v-1
	.byte		N01   , Gs0 
	.byte		N05   , Dn2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W12
	.byte		BEND  , c_v-1
	.byte		        c_v+5
	.byte		        c_v-1
	.byte		N05   , Ds1 
	.byte		N01   , Ds2 
	.byte		N01   , Gn2 
	.byte	W06
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N01   , Ds1 
	.byte		N05   , Ds2 
	.byte	W06
	.byte		BEND  , c_v-17
	.byte		        c_v-1
	.byte		N05   , Cs1 
	.byte		N01   , Ds2 
	.byte	W02
@ 025   ----------------------------------------
	.byte	W21
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+43
	.byte		        c_v-4
	.byte		N01   , Cs1 
	.byte		N05   , Ds4 
	.byte	W06
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+28
	.byte		N02   
	.byte	W11
	.byte		BEND  , c_v-4
	.byte		        c_v-3
	.byte		        c_v-1
	.byte		N05   , Cs1 
	.byte		N01   , Fs3 
	.byte		N01   , En4 
	.byte	W12
	.byte		BEND  , c_v+24
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Cs1 
	.byte	W11
	.byte		BEND  , c_v-41
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , Cn2 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		        c_v+23
	.byte		        c_v-1
	.byte		N06   , Fs1 
	.byte		N01   , Cs2 
	.byte	W07
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N01   , Fs1 
	.byte		N05   , Cs2 
	.byte	W05
	.byte		BEND  , c_v+7
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , Cs2 
	.byte		N01   , An2 
	.byte	W06
@ 026   ----------------------------------------
	.byte	W17
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-38
	.byte		        c_v-3
	.byte		N01   , Bn0 
	.byte		N06   , Dn4 
	.byte	W06
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+28
	.byte		N02   
	.byte	W11
	.byte		BEND  , c_v-4
	.byte		        c_v-12
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , Ds4 
	.byte		N01   , An5 
	.byte	W12
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   , An0 
	.byte		N01   , Bn0 
	.byte		N05   , Fs1 
	.byte	W12
	.byte		N05   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N01   
	.byte		N05   , An1 
	.byte	W12
	.byte		BEND  , c_v-1
	.byte		N05   , Fs1 
	.byte		N01   , An1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N01   , Fs1 
	.byte		N06   , An1 
	.byte	W07
	.byte		BEND  , c_v+55
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , An1 
	.byte	W09
@ 027   ----------------------------------------
	.byte	W13
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-39
	.byte		        c_v-3
	.byte		N01   , En1 
	.byte		N05   , Gn4 
	.byte	W06
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		N03   
	.byte	W12
	.byte		BEND  , c_v-1
	.byte		        c_v-14
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Gs4 
	.byte		N01   , Ds6 
	.byte	W11
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , En1 
	.byte	W11
	.byte		BEND  , c_v-64
	.byte		        c_v-1
	.byte		N01   , Bn0 
	.byte		N06   , Ds2 
	.byte	W07
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		        c_v-4
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , En2 
	.byte		N01   , As2 
	.byte	W06
	.byte		BEND  , c_v-11
	.byte		        c_v-1
	.byte		N01   , Dn1 
	.byte		N01   , En1 
	.byte		N05   , En2 
	.byte	W05
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N05   , Ds1 
	.byte		N01   , En2 
	.byte		N01   , Gn2 
	.byte	W14
@ 028   ----------------------------------------
	.byte	W10
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-13
	.byte		        c_v-2
	.byte		N01   , Ds1 
	.byte		N05   , Fn4 
	.byte	W05
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+29
	.byte		N03   
	.byte	W11
	.byte		BEND  , c_v-3
	.byte		        c_v-4
	.byte		        c_v-1
	.byte		N06   , Ds1 
	.byte		N01   , Fs4 
	.byte		N01   , An4 
	.byte	W12
	.byte		BEND  , c_v-3
	.byte		        c_v+0
	.byte		N05   , Gs0 
	.byte		N01   , Cn1 
	.byte		N01   , Ds1 
	.byte	W12
	.byte		BEND  , c_v+21
	.byte		        c_v-1
	.byte		N01   , Gs0 
	.byte		N05   , Dn2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W12
	.byte		BEND  , c_v-1
	.byte		        c_v+5
	.byte		        c_v-1
	.byte		N05   , Ds1 
	.byte		N01   , Ds2 
	.byte		N01   , Gn2 
	.byte	W06
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N01   , Ds1 
	.byte		N05   , Ds2 
	.byte	W06
	.byte		BEND  , c_v-17
	.byte		        c_v-1
	.byte		N05   , Cs1 
	.byte		N01   , Ds2 
	.byte	W17
@ 029   ----------------------------------------
	.byte	W06
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+43
	.byte		        c_v-4
	.byte		N01   , Cs1 
	.byte		N05   , Ds4 
	.byte	W06
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+28
	.byte		N02   
	.byte	W11
	.byte		BEND  , c_v-4
	.byte		        c_v-3
	.byte		        c_v-1
	.byte		N05   , Cs1 
	.byte		N01   , Fs3 
	.byte		N01   , En4 
	.byte	W12
	.byte		BEND  , c_v+24
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Cs1 
	.byte	W11
	.byte		BEND  , c_v-41
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , Cn2 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		        c_v+23
	.byte		        c_v-1
	.byte		N06   , Fs1 
	.byte		N01   , Cs2 
	.byte	W06
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N01   , Fs1 
	.byte		N05   , Cs2 
	.byte	W06
	.byte		BEND  , c_v+7
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , Cs2 
	.byte		N01   , An2 
	.byte	W21
@ 030   ----------------------------------------
	.byte	W02
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-38
	.byte		        c_v-3
	.byte		N01   , Bn0 
	.byte		N06   , Dn4 
	.byte	W06
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+28
	.byte		N02   
	.byte	W11
	.byte		BEND  , c_v-4
	.byte		        c_v-12
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , Ds4 
	.byte		N01   , An5 
	.byte	W11
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   , An0 
	.byte		N01   , Bn0 
	.byte		N05   , Fs1 
	.byte	W13
	.byte		N05   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N01   
	.byte		N05   , An1 
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		N05   , Fs1 
	.byte		N01   , An1 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N01   , Fs1 
	.byte		N06   , An1 
	.byte	W06
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+55
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , An1 
	.byte	W23
	.byte		BEND  , c_v-39
	.byte		        c_v-3
	.byte		N01   , En1 
	.byte		N05   , Gn4 
	.byte	W02
@ 031   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v+31
	.byte		N03   
	.byte	W12
	.byte		BEND  , c_v-1
	.byte		        c_v-14
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Gs4 
	.byte		N01   , Ds6 
	.byte	W11
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , En1 
	.byte	W11
	.byte		BEND  , c_v-64
	.byte		        c_v-1
	.byte		N01   , Bn0 
	.byte		N06   , Ds2 
	.byte	W07
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		        c_v-4
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , En2 
	.byte		N01   , As2 
	.byte	W05
	.byte		BEND  , c_v-11
	.byte		        c_v-1
	.byte		N01   , Dn1 
	.byte		N01   , En1 
	.byte		N05   , En2 
	.byte	W06
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N05   , Ds1 
	.byte		N01   , En2 
	.byte		N01   , Gn2 
	.byte	W23
	.byte		BEND  , c_v-13
	.byte		        c_v-2
	.byte		N01   , Ds1 
	.byte		N05   , Fn4 
	.byte	W06
@ 032   ----------------------------------------
	.byte		BEND  , c_v+29
	.byte		N03   
	.byte	W11
	.byte		BEND  , c_v-3
	.byte		        c_v-4
	.byte		        c_v-1
	.byte		N06   , Ds1 
	.byte		N01   , Fs4 
	.byte		N01   , An4 
	.byte	W12
	.byte		BEND  , c_v-3
	.byte		        c_v+0
	.byte		N05   , Gs0 
	.byte		N01   , Cn1 
	.byte		N01   , Ds1 
	.byte	W12
	.byte		BEND  , c_v+21
	.byte		        c_v-1
	.byte		N01   , Gs0 
	.byte		N05   , Dn2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W12
	.byte		BEND  , c_v-1
	.byte		        c_v+5
	.byte		        c_v-1
	.byte		N05   , Ds1 
	.byte		N01   , Ds2 
	.byte		N01   , Gn2 
	.byte	W06
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N01   , Ds1 
	.byte		N05   , Ds2 
	.byte	W06
	.byte		BEND  , c_v-17
	.byte		        c_v-1
	.byte		N05   , Cs1 
	.byte		N01   , Ds2 
	.byte	W23
	.byte		BEND  , c_v+43
	.byte		        c_v-4
	.byte		N01   , Cs1 
	.byte		N05   , Ds4 
	.byte	W05
	.byte		BEND  , c_v+28
	.byte		N02   
	.byte	W04
@ 033   ----------------------------------------
	.byte	W08
	.byte		BEND  , c_v-4
	.byte		        c_v-3
	.byte		        c_v-1
	.byte		N05   , Cs1 
	.byte		N01   , Fs3 
	.byte		N01   , En4 
	.byte	W12
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Cs1 
	.byte		N05   , Fs1 
	.byte	W11
	.byte		BEND  , c_v-37
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Cn2 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		        c_v+23
	.byte		        c_v-1
	.byte		N06   , Fs1 
	.byte		N01   , Cs2 
	.byte	W06
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N01   , Fs1 
	.byte		N05   , Cs2 
	.byte	W06
	.byte		BEND  , c_v+63
	.byte		N02   
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		N03   , Ds2 
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		N06   , Cn2 
	.byte		N01   , Ds2 
	.byte	W07
	.byte		BEND  , c_v+31
	.byte		N02   , Cn2 
	.byte	W07
@ 034   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N03   , Cs2 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N03   , Dn2 
	.byte	W23
	.byte		BEND  , c_v-1
	.byte		        c_v+32
	.byte		        c_v-2
	.byte		N01   , Ds2 
	.byte		N02   , As3 
	.byte	W02
	.byte		BEND  , c_v-3
	.byte		N03   , Fs3 
	.byte		N01   , As3 
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		N03   , En3 
	.byte		N01   , Fs3 
	.byte	W03
	.byte		BEND  , c_v-2
	.byte		N02   , Cs3 
	.byte		N01   , En3 
	.byte	W02
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N03   , As2 
	.byte		N01   , Cs3 
	.byte		N01   , Ds6 
	.byte	W04
	.byte		BEND  , c_v-2
	.byte		N02   , Fs2 
	.byte		N01   , As2 
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N03   , En2 
	.byte		N01   , Fs2 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N03   , Cs2 
	.byte		N01   , En2 
	.byte	W03
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+7
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , Cs2 
	.byte		N01   , An2 
	.byte	W40
@ 035   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v-50
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W11
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W24
	.byte		N05   
	.byte	W11
	.byte	GOTO
	 .word	mus_casino_plus_9_1_B1
mus_casino_plus_9_1_B2:
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N05   , En1 , v127
	.byte		N01   , Fs1 
	.byte		N01   , Bn1 
	.byte	W12
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+5
	.byte		        c_v-3
	.byte		N01   , Cs1 
	.byte		N01   , En1 
	.byte		N02   , Gn3 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N03   , Gs3 
	.byte	W06
	.byte		N03   
	.byte	W11
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N06   , Fs0 
	.byte		N01   , Gs3 
	.byte		N01   , As3 
	.byte	W04
@ 036   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W22
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W23
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N05   , As0 
	.byte	W40
	.byte	W01
	.byte		BEND  , c_v-1
	.byte		        c_v-50
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Bn0 
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N06   , An0 
	.byte	W02
@ 037   ----------------------------------------
	.byte	W10
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W23
	.byte		N06   
	.byte	W12
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Fs1 
	.byte		N01   , Bn1 
	.byte	W11
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+5
	.byte		        c_v-3
	.byte		N01   , Cs1 
	.byte		N01   , En1 
	.byte		N03   , Gn3 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		N03   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N03   , Gs3 
	.byte	W07
	.byte		N02   
	.byte	W11
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Gs3 
	.byte		N01   , As3 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W05
@ 038   ----------------------------------------
	.byte	W18
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W23
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N05   , As0 
	.byte	W40
	.byte		BEND  , c_v-1
	.byte		        c_v-50
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Bn0 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W09
@ 039   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W24
	.byte		N05   
	.byte	W11
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Fs1 
	.byte		N01   , Bn1 
	.byte	W40
	.byte		BEND  , c_v-8
	.byte		        c_v+0
	.byte		N06   , Fs0 
	.byte		N01   , Dn1 
	.byte		N01   , En1 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W13
@ 040   ----------------------------------------
	.byte	W10
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W23
	.byte		BEND  , c_v-1
	.byte		        c_v-37
	.byte		        c_v-1
	.byte		N01   , As0 
	.byte		N05   , Cs1 
	.byte	W40
	.byte		BEND  , c_v+24
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Cs1 
	.byte	W06
	.byte		BEND  , c_v+14
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N06   , As0 
	.byte	W12
	.byte		BEND  , c_v-46
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W05
@ 041   ----------------------------------------
	.byte	W18
	.byte		N06   
	.byte	W12
	.byte		BEND  , c_v+8
	.byte		        c_v-1
	.byte		N05   , Ds1 
	.byte		N01   , Fs1 
	.byte		N01   , An1 
	.byte	W40
	.byte		BEND  , c_v-40
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Ds1 
	.byte	W06
	.byte		BEND  , c_v-39
	.byte		        c_v+0
	.byte		N01   , Fs0 
	.byte		N05   , Gs0 
	.byte	W20
@ 042   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v+63
	.byte		N05   
	.byte	W23
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N05   , As0 
	.byte	W40
	.byte		BEND  , c_v-1
	.byte		        c_v-50
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Bn0 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W11
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W13
@ 043   ----------------------------------------
	.byte	W10
	.byte		N05   
	.byte	W12
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Fs1 
	.byte		N01   , Bn1 
	.byte	W40
	.byte		BEND  , c_v-3
	.byte		        c_v+0
	.byte		N06   , Gs0 
	.byte		N01   , Cn1 
	.byte		N01   , En1 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N01   , Gs0 
	.byte		N05   , Bn0 
	.byte	W23
	.byte		BEND  , c_v+5
	.byte		        c_v+0
	.byte		N01   
	.byte		N05   , En1 
	.byte	W05
@ 044   ----------------------------------------
	.byte	W18
	.byte		N05   
	.byte	W40
	.byte		BEND  , c_v-1
	.byte		N05   , Cs1 
	.byte		N01   , En1 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Cs1 
	.byte		N06   , Fs1 
	.byte	W12
	.byte		BEND  , c_v-1
	.byte		N01   
	.byte		N05   , As1 
	.byte	W20
@ 045   ----------------------------------------
	.byte	W03
	.byte		N06   
	.byte	W12
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W44
	.byte	W01
	.byte		BEND  , c_v-1
	.byte		        c_v-20
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , Bn1 
	.byte	W36
@ 046   ----------------------------------------
	.byte	W11
	.byte		N05   , Bn0 
	.byte	W40
	.byte		BEND  , c_v-50
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Bn0 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W11
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W23
	.byte		N05   
	.byte	W05
@ 047   ----------------------------------------
	.byte	W07
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Fs1 
	.byte		N01   , Bn1 
	.byte	W12
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+5
	.byte		        c_v-3
	.byte		N01   , Cs1 
	.byte		N01   , En1 
	.byte		N02   , Gn3 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N03   , Gs3 
	.byte	W06
	.byte		N03   
	.byte	W11
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N06   , Fs0 
	.byte		N01   , Gs3 
	.byte		N01   , As3 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W23
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W20
@ 048   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N05   , As0 
	.byte	W40
	.byte		BEND  , c_v-1
	.byte		        c_v-50
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Bn0 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N06   , An0 
	.byte	W12
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W22
	.byte		N06   
	.byte	W12
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Fs1 
	.byte		N01   , Bn1 
	.byte	W01
@ 049   ----------------------------------------
	.byte	W11
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+5
	.byte		        c_v-3
	.byte		N01   , Cs1 
	.byte		N01   , En1 
	.byte		N03   , Gn3 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		N03   
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N03   , Gs3 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Gs3 
	.byte		N01   , As3 
	.byte	W05
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W24
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-10
	.byte		        c_v-2
	.byte		N01   
	.byte		N23   , Fn3 
	.byte	W23
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , Fn3 
	.byte		N01   , An5 
	.byte	W04
@ 050   ----------------------------------------
	.byte	W07
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-38
	.byte		        c_v-3
	.byte		N01   , Bn0 
	.byte		N05   , Dn4 
	.byte	W06
	.byte		BEND  , c_v+28
	.byte		N03   
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		N03   , Ds4 
	.byte	W06
	.byte		N03   
	.byte	W12
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , As3 
	.byte		N01   , Ds4 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W11
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W23
	.byte		N05   
	.byte	W12
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Fs1 
	.byte		N01   , Bn1 
	.byte	W08
@ 051   ----------------------------------------
	.byte	W04
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-53
	.byte		        c_v-4
	.byte		N01   , En1 
	.byte		N05   , Ds4 
	.byte	W05
	.byte		BEND  , c_v+28
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v-4
	.byte		N03   , En4 
	.byte	W05
	.byte		N03   
	.byte	W12
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N06   , Fs0 
	.byte		N01   , As3 
	.byte		N01   , En4 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W23
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W23
	.byte		BEND  , c_v-1
	.byte		        c_v-37
	.byte		        c_v-1
	.byte		N01   , As0 
	.byte		N05   , Cs1 
	.byte	W11
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+43
	.byte		        c_v-4
	.byte		N01   
	.byte		N06   , Ds4 
	.byte	W01
@ 052   ----------------------------------------
	.byte	W06
	.byte		BEND  , c_v+28
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		N02   , En4 
	.byte	W06
	.byte		N02   
	.byte	W11
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , As3 
	.byte		N01   , En4 
	.byte	W06
	.byte		BEND  , c_v+14
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N06   , As0 
	.byte	W12
	.byte		BEND  , c_v-46
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W22
	.byte		N06   
	.byte	W12
	.byte		BEND  , c_v+8
	.byte		        c_v-1
	.byte		N05   , Ds1 
	.byte		N01   , Fs1 
	.byte		N01   , An1 
	.byte	W12
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-25
	.byte		        c_v-3
	.byte		N01   , Ds1 
	.byte		N05   , Dn4 
	.byte	W04
@ 053   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v+28
	.byte		N03   
	.byte	W06
	.byte		BEND  , c_v-4
	.byte		N03   , Ds4 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , As3 
	.byte		N01   , Ds4 
	.byte	W05
	.byte		BEND  , c_v-39
	.byte		        c_v+0
	.byte		N01   , Fs0 
	.byte		N05   , Gs0 
	.byte	W23
	.byte		BEND  , c_v+63
	.byte		N05   
	.byte	W24
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N05   , As0 
	.byte	W11
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		        c_v-38
	.byte		        c_v-3
	.byte		N01   , Bn0 
	.byte		N05   , Dn4 
	.byte	W06
	.byte		BEND  , c_v+28
	.byte		N03   
	.byte	W02
@ 054   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v-4
	.byte		N03   , Ds4 
	.byte	W06
	.byte		N03   
	.byte	W12
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , As3 
	.byte		N01   , Ds4 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W11
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W23
	.byte		N05   
	.byte	W11
	.byte		BEND  , c_v-9
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Fs1 
	.byte		N01   , Bn1 
	.byte	W12
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-53
	.byte		        c_v-4
	.byte		N01   , En1 
	.byte		N05   , Ds4 
	.byte	W06
	.byte		BEND  , c_v+28
	.byte		N02   
	.byte	W06
@ 055   ----------------------------------------
	.byte		BEND  , c_v-4
	.byte		N03   , En4 
	.byte	W05
	.byte		N03   
	.byte	W12
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-4
	.byte		        c_v+0
	.byte		N06   , Gs0 
	.byte		N01   , Cs3 
	.byte		N01   , En4 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N01   , Gs0 
	.byte		N05   , Bn0 
	.byte	W23
	.byte		BEND  , c_v+5
	.byte		        c_v+0
	.byte		N01   
	.byte		N05   , En1 
	.byte	W23
	.byte		N05   
	.byte	W11
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-53
	.byte		        c_v-4
	.byte		N01   
	.byte		N06   , Ds4 
	.byte	W07
	.byte		BEND  , c_v+28
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		N02   , En4 
	.byte	W04
@ 056   ----------------------------------------
	.byte	W02
	.byte		N02   
	.byte	W11
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		        c_v-1
	.byte		N05   , Cs1 
	.byte		N01   , Fs3 
	.byte		N01   , En4 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Cs1 
	.byte		N06   , Fs1 
	.byte	W12
	.byte		BEND  , c_v-1
	.byte		N01   
	.byte		N05   , As1 
	.byte	W22
	.byte		N06   
	.byte	W12
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W12
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		        c_v+6
	.byte		        c_v-3
	.byte		N01   , Gs1 
	.byte		N01   , Bn1 
	.byte		N05   , Dn4 
	.byte	W05
	.byte		BEND  , c_v+28
	.byte		N03   
	.byte	W06
	.byte		BEND  , c_v-4
	.byte		N03   , Ds4 
	.byte	W06
	.byte		N02   
	.byte	W02
@ 057   ----------------------------------------
	.byte	W09
	.byte		N03   
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , Ds4 
	.byte		N01   , An5 
	.byte	W06
	.byte		BEND  , c_v-35
	.byte		        c_v-4
	.byte		N01   , Bn0 
	.byte		N03   , Ds4 
	.byte	W12
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W11
	.byte		N03   
	.byte	W11
	.byte		N03   
	.byte	W07
	.byte		BEND  , c_v-14
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Ds4 
	.byte		N01   , Ds6 
	.byte	W22
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-39
	.byte		        c_v-3
	.byte		N01   , En1 
	.byte		N05   , Gn4 
	.byte	W06
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		N03   
	.byte	W06
@ 058   ----------------------------------------
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		        c_v-14
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Gs4 
	.byte		N01   , Ds6 
	.byte	W11
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , En1 
	.byte	W11
	.byte		BEND  , c_v-64
	.byte		        c_v-1
	.byte		N01   , Bn0 
	.byte		N06   , Ds2 
	.byte	W07
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		        c_v-4
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , En2 
	.byte		N01   , As2 
	.byte	W06
	.byte		BEND  , c_v-11
	.byte		        c_v-1
	.byte		N01   , Dn1 
	.byte		N01   , En1 
	.byte		N05   , En2 
	.byte	W05
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N05   , Ds1 
	.byte		N01   , En2 
	.byte		N01   , Gn2 
	.byte	W24
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-13
	.byte		        c_v-2
	.byte		N01   , Ds1 
	.byte		N05   , Fn4 
	.byte	W05
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+29
	.byte		N03   
	.byte	W10
@ 059   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v-3
	.byte		        c_v-4
	.byte		        c_v-1
	.byte		N06   , Ds1 
	.byte		N01   , Fs4 
	.byte		N01   , An4 
	.byte	W13
	.byte		BEND  , c_v-3
	.byte		        c_v+0
	.byte		N05   , Gs0 
	.byte		N01   , Cn1 
	.byte		N01   , Ds1 
	.byte	W11
	.byte		BEND  , c_v+21
	.byte		        c_v-1
	.byte		N01   , Gs0 
	.byte		N05   , Dn2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W12
	.byte		BEND  , c_v-1
	.byte		        c_v+5
	.byte		        c_v-1
	.byte		N05   , Ds1 
	.byte		N01   , Ds2 
	.byte		N01   , Gn2 
	.byte	W06
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N01   , Ds1 
	.byte		N05   , Ds2 
	.byte	W06
	.byte		BEND  , c_v-17
	.byte		        c_v-1
	.byte		N05   , Cs1 
	.byte		N01   , Ds2 
	.byte	W23
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+43
	.byte		        c_v-4
	.byte		N01   , Cs1 
	.byte		N05   , Ds4 
	.byte	W06
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+28
	.byte		N02   
	.byte	W11
	.byte		BEND  , c_v-4
	.byte		        c_v-3
	.byte		        c_v-1
	.byte		N05   , Cs1 
	.byte		N01   , Fs3 
	.byte		N01   , En4 
	.byte	W02
@ 060   ----------------------------------------
	.byte	W10
	.byte		BEND  , c_v+24
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Cs1 
	.byte	W11
	.byte		BEND  , c_v-41
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , Cn2 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		        c_v+23
	.byte		        c_v-1
	.byte		N06   , Fs1 
	.byte		N01   , Cs2 
	.byte	W06
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N01   , Fs1 
	.byte		N05   , Cs2 
	.byte	W06
	.byte		BEND  , c_v+7
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , Cs2 
	.byte		N01   , An2 
	.byte	W23
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-38
	.byte		        c_v-3
	.byte		N01   , Bn0 
	.byte		N06   , Dn4 
	.byte	W06
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+28
	.byte		N02   
	.byte	W11
	.byte		BEND  , c_v-4
	.byte		        c_v-12
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , Ds4 
	.byte		N01   , An5 
	.byte	W06
@ 061   ----------------------------------------
	.byte	W06
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   , An0 
	.byte		N01   , Bn0 
	.byte		N05   , Fs1 
	.byte	W12
	.byte		N05   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N01   
	.byte		N05   , An1 
	.byte	W12
	.byte		BEND  , c_v-1
	.byte		N05   , Fs1 
	.byte		N01   , An1 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N01   , Fs1 
	.byte		N06   , An1 
	.byte	W07
	.byte		BEND  , c_v+55
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , An1 
	.byte	W22
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-39
	.byte		        c_v-3
	.byte		N01   , En1 
	.byte		N05   , Gn4 
	.byte	W06
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		N03   
	.byte	W12
	.byte		BEND  , c_v-1
	.byte		        c_v-14
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Gs4 
	.byte		N01   , Ds6 
	.byte	W09
@ 062   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , En1 
	.byte	W11
	.byte		BEND  , c_v-64
	.byte		        c_v-1
	.byte		N01   , Bn0 
	.byte		N06   , Ds2 
	.byte	W07
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		        c_v-4
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , En2 
	.byte		N01   , As2 
	.byte	W06
	.byte		BEND  , c_v-11
	.byte		        c_v-1
	.byte		N01   , Dn1 
	.byte		N01   , En1 
	.byte		N05   , En2 
	.byte	W05
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N05   , Ds1 
	.byte		N01   , En2 
	.byte		N01   , Gn2 
	.byte	W23
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-13
	.byte		        c_v-2
	.byte		N01   , Ds1 
	.byte		N05   , Fn4 
	.byte	W06
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+29
	.byte		N03   
	.byte	W11
	.byte		BEND  , c_v-3
	.byte		        c_v-4
	.byte		        c_v-1
	.byte		N06   , Ds1 
	.byte		N01   , Fs4 
	.byte		N01   , An4 
	.byte	W12
	.byte		BEND  , c_v-3
	.byte		        c_v+0
	.byte		N05   , Gs0 
	.byte		N01   , Cn1 
	.byte		N01   , Ds1 
	.byte	W02
@ 063   ----------------------------------------
	.byte	W10
	.byte		BEND  , c_v+21
	.byte		        c_v-1
	.byte		N01   , Gs0 
	.byte		N05   , Dn2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W12
	.byte		BEND  , c_v-1
	.byte		        c_v+5
	.byte		        c_v-1
	.byte		N05   , Ds1 
	.byte		N01   , Ds2 
	.byte		N01   , Gn2 
	.byte	W06
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N01   , Ds1 
	.byte		N05   , Ds2 
	.byte	W06
	.byte		BEND  , c_v-17
	.byte		        c_v-1
	.byte		N05   , Cs1 
	.byte		N01   , Ds2 
	.byte	W23
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+43
	.byte		        c_v-4
	.byte		N01   , Cs1 
	.byte		N05   , Ds4 
	.byte	W06
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+28
	.byte		N02   
	.byte	W11
	.byte		BEND  , c_v-4
	.byte		        c_v-3
	.byte		        c_v-1
	.byte		N05   , Cs1 
	.byte		N01   , Fs3 
	.byte		N01   , En4 
	.byte	W12
	.byte		BEND  , c_v+24
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Cs1 
	.byte	W05
@ 064   ----------------------------------------
	.byte	W06
	.byte		BEND  , c_v-41
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , Cn2 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		        c_v+23
	.byte		        c_v-1
	.byte		N06   , Fs1 
	.byte		N01   , Cs2 
	.byte	W06
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N01   , Fs1 
	.byte		N05   , Cs2 
	.byte	W06
	.byte		BEND  , c_v+7
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , Cs2 
	.byte		N01   , An2 
	.byte	W23
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-38
	.byte		        c_v-3
	.byte		N01   , Bn0 
	.byte		N06   , Dn4 
	.byte	W06
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+28
	.byte		N02   
	.byte	W11
	.byte		BEND  , c_v-4
	.byte		        c_v-12
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , Ds4 
	.byte		N01   , An5 
	.byte	W11
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   , An0 
	.byte		N01   , Bn0 
	.byte		N05   , Fs1 
	.byte	W10
@ 065   ----------------------------------------
	.byte	W03
	.byte		N05   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N01   
	.byte		N05   , An1 
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		N05   , Fs1 
	.byte		N01   , An1 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N01   , Fs1 
	.byte		N06   , An1 
	.byte	W06
	.byte		VOL   , 45*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+55
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , An1 
	.byte	W23
	.byte		BEND  , c_v-39
	.byte		        c_v-3
	.byte		N01   , En1 
	.byte		N05   , Gn4 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		N03   
	.byte	W12
	.byte		BEND  , c_v-1
	.byte		        c_v-14
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , Gs4 
	.byte		N01   , Ds6 
	.byte	W11
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , En1 
	.byte	W11
	.byte		BEND  , c_v-64
	.byte		        c_v-1
	.byte		N01   , Bn0 
	.byte		N06   , Ds2 
	.byte	W02
@ 066   ----------------------------------------
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		        c_v-4
	.byte		        c_v+0
	.byte		N05   , En1 
	.byte		N01   , En2 
	.byte		N01   , As2 
	.byte	W05
	.byte		BEND  , c_v-11
	.byte		        c_v-1
	.byte		N01   , Dn1 
	.byte		N01   , En1 
	.byte		N05   , En2 
	.byte	W06
	.byte		BEND  , c_v+5
	.byte		        c_v-1
	.byte		N05   , Ds1 
	.byte		N01   , En2 
	.byte		N01   , Gn2 
	.byte	W23
	.byte		BEND  , c_v-13
	.byte		        c_v-2
	.byte		N01   , Ds1 
	.byte		N05   , Fn4 
	.byte	W06
	.byte		BEND  , c_v+29
	.byte		N03   
	.byte	W11
	.byte		BEND  , c_v-3
	.byte		        c_v-4
	.byte		        c_v-1
	.byte		N06   , Ds1 
	.byte		N01   , Fs4 
	.byte		N01   , An4 
	.byte	W12
	.byte		BEND  , c_v-3
	.byte		        c_v+0
	.byte		N05   , Gs0 
	.byte		N01   , Cn1 
	.byte		N01   , Ds1 
	.byte	W12
	.byte		BEND  , c_v+21
	.byte		        c_v-1
	.byte		N01   , Gs0 
	.byte		N05   , Dn2 
	.byte	W05
@ 067   ----------------------------------------
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W12
	.byte		BEND  , c_v-1
	.byte		        c_v+5
	.byte		        c_v-1
	.byte		N05   , Ds1 
	.byte		N01   , Ds2 
	.byte		N01   , Gn2 
	.byte	W06
	.byte		BEND  , c_v-58
	.byte		        c_v-1
	.byte		N01   , Ds1 
	.byte		N05   , Ds2 
	.byte	W05
	.byte		BEND  , c_v-17
	.byte		        c_v-1
	.byte		N05   , Cs1 
	.byte		N01   , Ds2 
	.byte	W24
	.byte		BEND  , c_v+43
	.byte		        c_v-4
	.byte		N01   , Cs1 
	.byte		N05   , Ds4 
	.byte	W05
	.byte		BEND  , c_v+28
	.byte		N02   
	.byte	W12
	.byte		BEND  , c_v-4
	.byte		        c_v-3
	.byte		        c_v-1
	.byte		N05   , Cs1 
	.byte		N01   , Fs3 
	.byte		N01   , En4 
	.byte	W12
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Cs1 
	.byte		N05   , Fs1 
	.byte	W11
	.byte		BEND  , c_v-37
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Cn2 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		N05   
	.byte	W03
@ 068   ----------------------------------------
	.byte	W08
	.byte		BEND  , c_v-1
	.byte		        c_v+23
	.byte		        c_v-1
	.byte		N06   , Fs1 
	.byte		N01   , Cs2 
	.byte	W06
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N01   , Fs1 
	.byte		N05   , Cs2 
	.byte	W06
	.byte		BEND  , c_v+63
	.byte		N02   
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		N03   , Ds2 
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		N06   , Cn2 
	.byte		N01   , Ds2 
	.byte	W07
	.byte		BEND  , c_v+31
	.byte		N02   , Cn2 
	.byte	W11
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N03   , Cs2 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		        c_v+31
	.byte		N03   , Dn2 
	.byte	W23
	.byte		BEND  , c_v-1
	.byte		        c_v+32
	.byte		        c_v-2
	.byte		N01   , Ds2 
	.byte		N02   , As3 
	.byte	W02
	.byte		BEND  , c_v-3
	.byte		N03   , Fs3 
	.byte		N01   , As3 
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		N03   , En3 
	.byte		N01   , Fs3 
	.byte	W01
@ 069   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-2
	.byte		N02   , Cs3 
	.byte		N01   , En3 
	.byte	W02
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N03   , As2 
	.byte		N01   , Cs3 
	.byte		N01   , Ds6 
	.byte	W03
	.byte		BEND  , c_v-2
	.byte		N02   , Fs2 
	.byte		N01   , As2 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N03   , En2 
	.byte		N01   , Fs2 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N03   , Cs2 
	.byte		N01   , En2 
	.byte	W03
	.byte		VOL   , 64*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+7
	.byte		        c_v-1
	.byte		N05   , Bn0 
	.byte		N01   , Cs2 
	.byte		N01   , An2 
	.byte	W40
	.byte		BEND  , c_v-50
	.byte		        c_v+0
	.byte		N05   , Fs0 
	.byte		N01   , Bn0 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N01   , Fs0 
	.byte		N05   , An0 
	.byte	W11
	.byte		BEND  , c_v-14
	.byte		        c_v-1
	.byte		N01   
	.byte		N05   , Fs1 
	.byte	W23
@ 070   ----------------------------------------
	.byte	W01
	.byte		N05   
	.byte	W11
	.byte	FINE

@**************** Track 2 (Midi-Chn.3) ****************@

mus_casino_plus_9_2:
	.byte	KEYSH , mus_casino_plus_9_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 12
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		BEND  , c_v-13
	.byte		N01   , Cn1 , v127
	.byte		N90   , Cn1 , v127, gtp1
	.byte	W92
mus_casino_plus_9_2_B1:
	.byte		N12   , Cn1 , v127
	.byte	W04
@ 001   ----------------------------------------
	.byte	W08
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		        c_v+1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W04
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N02   , En4 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , En4 , v127, gtp1
	.byte	W44
	.byte	W02
	.byte		N14   
	.byte	W14
	.byte		N92   
	.byte	W08
@ 002   ----------------------------------------
	.byte	W84
	.byte	W01
	.byte		N11   
	.byte	W11
@ 003   ----------------------------------------
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-31
	.byte		        c_v+1
	.byte		N03   , Ds4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N03   , En4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N08   
	.byte	W09
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , En4 , v127, gtp1
	.byte	W44
	.byte	W02
	.byte		N03   
	.byte	W03
	.byte		N90   , En4 , v127, gtp1
	.byte	W15
@ 004   ----------------------------------------
	.byte	W76
	.byte	W01
	.byte		N92   
	.byte	W19
@ 005   ----------------------------------------
	.byte	W72
	.byte	W01
	.byte		N92   
	.byte	W23
@ 006   ----------------------------------------
	.byte	W68
	.byte	W02
	.byte		N92   
	.byte	W24
	.byte	W02
@ 007   ----------------------------------------
	.byte	W66
	.byte		N90   , En4 , v127, gtp1
	.byte	W30
@ 008   ----------------------------------------
	.byte	W60
	.byte	W02
	.byte		N92   
	.byte	W32
	.byte	W02
@ 009   ----------------------------------------
	.byte	W56
	.byte	W02
	.byte		N92   
	.byte	W36
	.byte	W02
@ 010   ----------------------------------------
	.byte	W54
	.byte	W01
	.byte		N92   
	.byte	W40
	.byte	W01
@ 011   ----------------------------------------
	.byte	W48
	.byte	W03
	.byte		N90   , En4 , v127, gtp1
	.byte	W44
	.byte	W01
@ 012   ----------------------------------------
	.byte	W44
	.byte	W03
	.byte		N12   
	.byte	W12
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-31
	.byte		        c_v+1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N02   , En4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , En4 , v127, gtp1
	.byte	W17
@ 013   ----------------------------------------
	.byte	W28
	.byte	W01
	.byte		N14   
	.byte	W14
	.byte		N92   
	.byte	W52
	.byte	W01
@ 014   ----------------------------------------
	.byte	W36
	.byte	W03
	.byte		N11   
	.byte	W12
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-31
	.byte		        c_v+1
	.byte		N03   , Ds4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N03   , En4 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N08   
	.byte	W09
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , En4 , v127, gtp1
	.byte	W13
@ 015   ----------------------------------------
	.byte	W32
	.byte	W01
	.byte		N03   
	.byte	W03
	.byte		VOICE , 73
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N05   , Bn3 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , Fs3 
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W03
@ 016   ----------------------------------------
	.byte	W03
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , Bn3 
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+1
	.byte		N05   , Gs3 
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , En3 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W01
@ 017   ----------------------------------------
	.byte	W05
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , Bn3 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , Bn3 , v127, gtp2
	.byte	W22
@ 018   ----------------------------------------
	.byte	W24
	.byte		        Bn3 , v127, gtp1
	.byte	W44
	.byte	W02
	.byte		        Bn3 , v127, gtp2
	.byte	W24
	.byte	W02
@ 019   ----------------------------------------
	.byte	W21
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , Fs3 
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
@ 020   ----------------------------------------
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , Bn3 
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-10
	.byte		        c_v+2
	.byte		N05   , En4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+1
	.byte		        c_v+1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W05
@ 021   ----------------------------------------
	.byte		VOICE , 12
	.byte	W02
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N92   
	.byte	W80
	.byte	W03
@ 022   ----------------------------------------
	.byte	W09
	.byte		N48   , Gs3 , v127, gtp3
	.byte	W52
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v+0
	.byte		N03   , Fs2 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-32
	.byte		        c_v+0
	.byte		N03   , Fn2 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N02   , Fs2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+15
	.byte		        c_v+0
	.byte		N02   , Fs4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		N03   , Bn4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+1
	.byte		N03   , Ds5 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 114*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+3
	.byte		N06   , Fs5 
	.byte	W01
@ 023   ----------------------------------------
	.byte		VOICE , 1
	.byte	W06
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N22   
	.byte	W22
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		N05   , As4 
	.byte	W06
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N17   , Bn4 
	.byte	W17
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , Bn4 , v127, gtp1
	.byte	W44
	.byte	W01
@ 024   ----------------------------------------
	.byte	W01
	.byte		N23   
	.byte	W24
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-61
	.byte		        c_v+3
	.byte		N05   , An4 
	.byte	W05
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N17   , As4 
	.byte	W18
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , As4 , v127, gtp1
	.byte	W44
	.byte	W02
	.byte		N23   
	.byte	W02
@ 025   ----------------------------------------
	.byte	W21
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , Gn4 
	.byte	W06
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N16   , Gs4 
	.byte	W17
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , Gs4 , v127, gtp2
	.byte	W44
	.byte	W02
	.byte		N22   
	.byte	W06
@ 026   ----------------------------------------
	.byte	W17
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+1
	.byte		N06   , Fn4 
	.byte	W06
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N16   , Fs4 
	.byte	W17
	.byte		BEND  , c_v+2
	.byte		N05   , Bn4 
	.byte	W06
	.byte		BEND  , c_v+33
	.byte		        c_v+1
	.byte		N12   , Cn5 
	.byte	W12
	.byte		N11   
	.byte	W11
	.byte		BEND  , c_v+3
	.byte		N11   , Fs5 
	.byte	W11
	.byte		N06   
	.byte	W07
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N22   
	.byte	W09
@ 027   ----------------------------------------
	.byte	W13
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		N05   , As4 
	.byte	W06
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N17   , Bn4 
	.byte	W17
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , Bn4 , v127, gtp1
	.byte	W44
	.byte	W02
	.byte		N23   
	.byte	W14
@ 028   ----------------------------------------
	.byte	W09
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-61
	.byte		        c_v+3
	.byte		N05   , An4 
	.byte	W06
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N17   , As4 
	.byte	W18
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , As4 , v127, gtp1
	.byte	W44
	.byte	W02
	.byte		N23   
	.byte	W17
@ 029   ----------------------------------------
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , Gn4 
	.byte	W06
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N16   , Gs4 
	.byte	W16
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , Gs4 , v127, gtp2
	.byte	W44
	.byte	W03
	.byte		N22   
	.byte	W21
@ 030   ----------------------------------------
	.byte	W02
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+1
	.byte		N06   , Fn4 
	.byte	W06
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N44   , Fs4 , v127, gtp1
	.byte	W44
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+39
	.byte		        c_v+0
	.byte		N05   , Ds3 
	.byte	W06
	.byte		BEND  , c_v+1
	.byte		N06   , Cn3 
	.byte	W06
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N22   
	.byte	W01
	.byte		VOICE , 12
	.byte	W22
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		        c_v+2
	.byte		N05   , As4 
	.byte	W02
@ 031   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N17   , Bn4 
	.byte	W17
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , Bn4 , v127, gtp1
	.byte	W44
	.byte	W02
	.byte		N23   
	.byte	W23
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-61
	.byte		        c_v+3
	.byte		N05   , An4 
	.byte	W06
@ 032   ----------------------------------------
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N17   , As4 
	.byte	W18
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , As4 , v127, gtp1
	.byte	W44
	.byte	W01
	.byte		N23   
	.byte	W24
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , Gn4 
	.byte	W05
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N16   , Gs4 
	.byte	W04
@ 033   ----------------------------------------
	.byte	W13
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , Gs4 , v127, gtp2
	.byte	W44
	.byte	W03
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+3
	.byte		        c_v+0
	.byte		N02   , Bn1 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N08   
	.byte	W09
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N08   
	.byte	W08
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N06   , Gs1 
	.byte	W07
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N02   , An1 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N08   
	.byte	W05
@ 034   ----------------------------------------
	.byte	W04
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N03   , As1 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N03   , Bn1 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N42   , Bn1 , v127, gtp1
	.byte	W42
	.byte	W01
	.byte		N90   , Bn1 , v127, gtp1
	.byte	W40
@ 035   ----------------------------------------
	.byte	W52
	.byte	GOTO
	 .word	mus_casino_plus_9_2_B1
mus_casino_plus_9_2_B2:
	.byte		N12   , Bn1 , v127
	.byte	W12
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+12
	.byte		        c_v+1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W04
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N02   , En4 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , En4 , v127, gtp1
	.byte	W12
@ 036   ----------------------------------------
	.byte	W32
	.byte	W02
	.byte		N14   
	.byte	W14
	.byte		N92   
	.byte	W48
@ 037   ----------------------------------------
	.byte	W44
	.byte	W01
	.byte		N11   
	.byte	W11
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-31
	.byte		        c_v+1
	.byte		N03   , Ds4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N03   , En4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W04
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N08   
	.byte	W09
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , En4 , v127, gtp1
	.byte	W08
@ 038   ----------------------------------------
	.byte	W36
	.byte	W02
	.byte		N03   
	.byte	W03
	.byte		N90   , En4 , v127, gtp1
	.byte	W54
	.byte	W01
@ 039   ----------------------------------------
	.byte	W36
	.byte	W01
	.byte		N92   
	.byte	W56
	.byte	W03
@ 040   ----------------------------------------
	.byte	W32
	.byte	W01
	.byte		N92   
	.byte	W60
	.byte	W03
@ 041   ----------------------------------------
	.byte	W30
	.byte		N92   
	.byte	W66
@ 042   ----------------------------------------
	.byte	W24
	.byte	W02
	.byte		N90   , En4 , v127, gtp1
	.byte	W68
	.byte	W02
@ 043   ----------------------------------------
	.byte	W22
	.byte		N92   
	.byte	W72
	.byte	W02
@ 044   ----------------------------------------
	.byte	W18
	.byte		N92   
	.byte	W78
@ 045   ----------------------------------------
	.byte	W15
	.byte		N92   
	.byte	W80
	.byte	W01
@ 046   ----------------------------------------
	.byte	W11
	.byte		N90   , En4 , v127, gtp1
	.byte	W84
	.byte	W01
@ 047   ----------------------------------------
	.byte	W07
	.byte		N12   
	.byte	W12
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-31
	.byte		        c_v+1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N02   , En4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , En4 , v127, gtp1
	.byte	W44
	.byte	W02
	.byte		N14   
	.byte	W11
@ 048   ----------------------------------------
	.byte	W03
	.byte		N92   
	.byte	W92
	.byte		N11   
	.byte	W01
@ 049   ----------------------------------------
	.byte	W11
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-31
	.byte		        c_v+1
	.byte		N03   , Ds4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N03   , En4 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N08   
	.byte	W09
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , En4 , v127, gtp1
	.byte	W44
	.byte	W02
	.byte		N03   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N05   , Bn3 
	.byte	W04
@ 050   ----------------------------------------
	.byte	W01
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , Fs3 
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , Bn3 
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+1
	.byte		N05   , Gs3 
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W03
@ 051   ----------------------------------------
	.byte	W04
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , En3 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , Bn3 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W01
@ 052   ----------------------------------------
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , Bn3 , v127, gtp2
	.byte	W44
	.byte	W02
	.byte		        Bn3 , v127, gtp1
	.byte	W16
@ 053   ----------------------------------------
	.byte	W30
	.byte		        Bn3 , v127, gtp2
	.byte	W44
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W02
@ 054   ----------------------------------------
	.byte	W03
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , Fs3 
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , Bn3 
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-10
	.byte		        c_v+2
	.byte		N05   , En4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
@ 055   ----------------------------------------
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+1
	.byte		        c_v+1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N92   
	.byte	W24
	.byte	W03
@ 056   ----------------------------------------
	.byte	W64
	.byte	W01
	.byte		N48   , Gs3 , v127, gtp3
	.byte	W30
	.byte	W01
@ 057   ----------------------------------------
	.byte	W21
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-7
	.byte		        c_v+0
	.byte		N03   , Fs2 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-32
	.byte		        c_v+0
	.byte		N03   , Fn2 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W04
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N02   , Fs2 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+15
	.byte		        c_v+0
	.byte		N02   , Fs4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		N03   , Bn4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+1
	.byte		N03   , Ds5 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 114*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+3
	.byte		N06   , Fs5 
	.byte	W07
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N22   
	.byte	W22
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		N05   , As4 
	.byte	W06
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N17   , Bn4 
	.byte	W06
@ 058   ----------------------------------------
	.byte	W11
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , Bn4 , v127, gtp1
	.byte	W44
	.byte	W02
	.byte		N23   
	.byte	W24
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-61
	.byte		        c_v+3
	.byte		N05   , An4 
	.byte	W05
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N17   , As4 
	.byte	W10
@ 059   ----------------------------------------
	.byte	W08
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , As4 , v127, gtp1
	.byte	W44
	.byte	W02
	.byte		N23   
	.byte	W23
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , Gn4 
	.byte	W06
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N16   , Gs4 
	.byte	W13
@ 060   ----------------------------------------
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , Gs4 , v127, gtp2
	.byte	W44
	.byte	W03
	.byte		N22   
	.byte	W23
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+1
	.byte		N06   , Fn4 
	.byte	W06
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N16   , Fs4 
	.byte	W17
@ 061   ----------------------------------------
	.byte		BEND  , c_v+2
	.byte		N05   , Bn4 
	.byte	W06
	.byte		BEND  , c_v+33
	.byte		        c_v+1
	.byte		N12   , Cn5 
	.byte	W12
	.byte		N11   
	.byte	W11
	.byte		BEND  , c_v+3
	.byte		N11   , Fs5 
	.byte	W11
	.byte		N06   
	.byte	W07
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N22   
	.byte	W22
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		N05   , As4 
	.byte	W06
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N17   , Bn4 
	.byte	W17
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , Bn4 , v127, gtp1
	.byte	W04
@ 062   ----------------------------------------
	.byte	W42
	.byte		N23   
	.byte	W23
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-61
	.byte		        c_v+3
	.byte		N05   , An4 
	.byte	W06
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N17   , As4 
	.byte	W18
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , As4 , v127, gtp1
	.byte	W07
@ 063   ----------------------------------------
	.byte	W36
	.byte	W03
	.byte		N23   
	.byte	W23
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , Gn4 
	.byte	W06
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N16   , Gs4 
	.byte	W16
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , Gs4 , v127, gtp2
	.byte	W12
@ 064   ----------------------------------------
	.byte	W32
	.byte	W03
	.byte		N22   
	.byte	W22
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+1
	.byte		N06   , Fn4 
	.byte	W07
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N44   , Fs4 , v127, gtp1
	.byte	W32
@ 065   ----------------------------------------
	.byte	W14
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+39
	.byte		        c_v+0
	.byte		N05   , Ds3 
	.byte	W06
	.byte		BEND  , c_v+1
	.byte		N06   , Cn3 
	.byte	W06
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N22   
	.byte	W23
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		        c_v+2
	.byte		N05   , As4 
	.byte	W06
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N17   , Bn4 
	.byte	W17
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , Bn4 , v127, gtp1
	.byte	W19
@ 066   ----------------------------------------
	.byte	W24
	.byte	W03
	.byte		N23   
	.byte	W23
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-61
	.byte		        c_v+3
	.byte		N05   , An4 
	.byte	W06
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N17   , As4 
	.byte	W18
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , As4 , v127, gtp1
	.byte	W22
@ 067   ----------------------------------------
	.byte	W23
	.byte		N23   
	.byte	W24
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , Gn4 
	.byte	W05
	.byte		BEND  , c_v+34
	.byte		        c_v+2
	.byte		N16   , Gs4 
	.byte	W17
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N44   , Gs4 , v127, gtp2
	.byte	W24
	.byte	W03
@ 068   ----------------------------------------
	.byte	W20
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+3
	.byte		        c_v+0
	.byte		N02   , Bn1 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N08   
	.byte	W09
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N08   
	.byte	W08
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N06   , Gs1 
	.byte	W07
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N02   , An1 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N08   
	.byte	W09
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N03   , As1 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+32
	.byte		        c_v+0
	.byte		N03   , Bn1 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N42   , Bn1 , v127, gtp1
	.byte	W24
	.byte	W03
@ 069   ----------------------------------------
	.byte	W16
	.byte		N90   , Bn1 , v127, gtp1
	.byte	W80
@ 070   ----------------------------------------
	.byte	W12
	.byte	FINE

@**************** Track 3 (Midi-Chn.4) ****************@

mus_casino_plus_9_3:
	.byte	KEYSH , mus_casino_plus_9_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 12
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		        104*mus_casino_plus_9_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		BEND  , c_v-13
	.byte		        c_v+56
	.byte		        c_v-1
	.byte		N01   , Cn1 , v127
	.byte		N05   , Bn2 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Fs2 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , As2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N42   , Bn2 , v127, gtp1
	.byte	W42
	.byte	W01
	.byte		N03   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-14
	.byte		        c_v-2
	.byte		N05   , Fs3 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Ds3 
	.byte	W06
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N05   , Dn3 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Ds3 
	.byte	W06
mus_casino_plus_9_3_B1:
	.byte		BEND  , c_v-2
	.byte		N05   , Bn3 , v127
	.byte	W04
@ 001   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N06   , Gs3 
	.byte	W06
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , Gn3 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N42   , Gs3 , v127, gtp1
	.byte	W44
	.byte		N24   , Gs3 , v127, gtp1
	.byte	W24
	.byte	W01
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Fs2 
	.byte	W02
@ 002   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v-1
	.byte		N06   , As2 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N42   
	.byte	W42
	.byte		N03   
	.byte	W04
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-14
	.byte		        c_v-2
	.byte		N05   , Fs3 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N05   , Ds3 
	.byte	W06
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N06   , Dn3 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Ds3 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N05   , Gs3 
	.byte	W06
@ 003   ----------------------------------------
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , Gn3 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N17   
	.byte	W18
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+9
	.byte		        c_v-1
	.byte		N03   , Gs4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N42   
	.byte	W42
	.byte	W01
	.byte		N06   
	.byte	W03
	.byte		VOICE , 11
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W04
@ 004   ----------------------------------------
	.byte	W02
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Ds4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W01
@ 005   ----------------------------------------
	.byte	W04
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Cs4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
@ 006   ----------------------------------------
	.byte	W01
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , Cn3 
	.byte	W01
	.byte		VOICE , 12
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N06   , Cs3 
	.byte	W07
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N05   , Gs2 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+54
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Cs3 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N05   , Cn3 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Cs3 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N06   , En3 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Cs3 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , Fs3 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+15
	.byte		        c_v-1
	.byte		N05   , As2 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N05   , As2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N06   , Bn2 
	.byte	W04
@ 007   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N05   , As2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N05   , Cs3 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N05   , Ds3 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-41
	.byte		        c_v-1
	.byte		N05   , Fs2 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		N06   , Gs2 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Fs2 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		N05   , Gs2 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N05   , Fs2 
	.byte	W06
	.byte		VOL   , 93*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , Gs2 
	.byte	W06
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N06   , As2 
	.byte	W06
	.byte		VOICE , 11
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W02
@ 008   ----------------------------------------
	.byte	W05
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Ds4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N05   , Gs4 
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
@ 009   ----------------------------------------
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		        c_v-2
	.byte		N05   , Gn3 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W02
	.byte		VOICE , 12
	.byte	W03
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N06   , En3 
	.byte	W07
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W05
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N05   , Cs3 
	.byte	W06
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , En3 
	.byte	W03
@ 010   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N06   , Fs3 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En3 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-1
	.byte		N05   , Fs2 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N05   , As2 
	.byte	W06
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N05   , Cs3 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N06   , Fs3 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , As3 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N05   , Bn3 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Cs3 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , En3 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N06   , Cn3 
	.byte	W07
	.byte		BEND  , c_v-1
	.byte		N05   , En3 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N05   , Gn3 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , As3 
	.byte	W01
@ 011   ----------------------------------------
	.byte	W04
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N05   , Bn3 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Fs3 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N06   , Ds3 
	.byte	W06
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N05   , Ds3 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N05   , As2 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N06   , Bn2 
	.byte	W06
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Fs2 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N05   , As2 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N42   , Bn2 , v127, gtp1
	.byte	W22
@ 012   ----------------------------------------
	.byte	W21
	.byte		N03   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-14
	.byte		        c_v-2
	.byte		N05   , Fs3 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Ds3 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N05   , Dn3 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Ds3 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N06   , Gs3 
	.byte	W07
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , Gn3 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N42   , Gs3 , v127, gtp1
	.byte	W24
	.byte	W02
@ 013   ----------------------------------------
	.byte	W17
	.byte		N24   , Gs3 , v127, gtp1
	.byte	W24
	.byte	W02
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Fs2 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N06   , As2 
	.byte	W07
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N42   
	.byte	W30
@ 014   ----------------------------------------
	.byte	W13
	.byte		N03   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-14
	.byte		        c_v-2
	.byte		N05   , Fs3 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Ds3 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N06   , Dn3 
	.byte	W07
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Ds3 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N05   , Bn3 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , Gn3 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N17   
	.byte	W18
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+9
	.byte		        c_v-1
	.byte		N03   , Gs4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N42   
	.byte	W13
@ 015   ----------------------------------------
	.byte	W28
	.byte	W01
	.byte		N06   
	.byte	W01
	.byte		VOICE , 11
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Ds4 
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W03
@ 016   ----------------------------------------
	.byte	W03
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Cs4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W01
@ 017   ----------------------------------------
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W03
	.byte		VOICE , 12
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N01   , Cn4 
	.byte		N05   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N06   , Cs4 
	.byte	W06
	.byte		BEND  , c_v-9
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+9
	.byte		        c_v-1
	.byte		N05   , Gs4 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Cs4 
	.byte	W05
@ 018   ----------------------------------------
	.byte	W01
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , Cn4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N05   , Cs4 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N06   , En4 
	.byte	W07
	.byte		BEND  , c_v-2
	.byte		N05   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N05   , As3 
	.byte	W06
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N05   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , As3 
	.byte	W06
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N06   , Bn3 
	.byte	W06
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , As3 
	.byte	W06
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N05   , Bn3 
	.byte	W06
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N05   , Cs4 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N05   , Ds4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		        c_v-2
	.byte		N05   , Fs3 
	.byte	W05
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N06   , Gs3 
	.byte	W07
	.byte		BEND  , c_v-2
	.byte		N05   , Fs3 
	.byte	W05
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W03
@ 019   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v-2
	.byte		N05   , Fs3 
	.byte	W06
	.byte		VOL   , 93*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+62
	.byte		        c_v-2
	.byte		N06   , As3 
	.byte	W07
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+15
	.byte		        c_v-3
	.byte		N05   , Fs4 
	.byte	W03
	.byte		VOICE , 11
	.byte	W02
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Ds4 
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
@ 020   ----------------------------------------
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N05   , Gs4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W05
@ 021   ----------------------------------------
	.byte		VOICE , 12
	.byte	W02
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-2
	.byte		N05   , Gn3 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+9
	.byte		        c_v-1
	.byte		N05   , Gs4 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N05   , Bn3 
	.byte	W06
	.byte		BEND  , c_v-11
	.byte		        c_v-1
	.byte		N06   , En4 
	.byte	W07
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N05   , Bn3 
	.byte	W05
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N05   , Cs4 
	.byte	W06
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N05   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-11
	.byte		        c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Gs4 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N06   , Fs4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Gs4 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		        c_v-2
	.byte		N05   , Fs3 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , As3 
	.byte	W06
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N05   , Cs4 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N06   , Fs4 
	.byte	W03
@ 022   ----------------------------------------
	.byte	W04
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , As4 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N05   , Bn4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Gs4 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N06   , Cn4 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		BEND  , c_v-3
	.byte		N05   , Gn4 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N05   , As4 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N05   , Bn4 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N03   , Bn2 
	.byte	W03
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N03   , As2 
	.byte	W04
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , Bn2 
	.byte	W02
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-12
	.byte		        c_v-2
	.byte		N02   , Bn4 
	.byte	W03
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-4
	.byte		N03   , Ds5 
	.byte	W03
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N03   , Fs5 
	.byte	W03
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-6
	.byte		N06   , Bn5 
	.byte	W01
@ 023   ----------------------------------------
	.byte	W06
	.byte		VOICE , 1
	.byte		BEND  , c_v-4
	.byte		N05   , Cs5 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Gs4 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Bn4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N17   , En4 
	.byte	W17
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Gs4 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N28   
	.byte	W28
	.byte	W01
	.byte		VOL   , 93*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-35
	.byte		        c_v-3
	.byte		N05   , Gn4 
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N11   , Gs4 
	.byte	W10
@ 024   ----------------------------------------
	.byte	W01
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N06   , Cs4 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Fn4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N16   , As3 
	.byte	W17
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+15
	.byte		        c_v-3
	.byte		N05   , Fs4 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N06   , Bn4 
	.byte	W07
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N28   
	.byte	W28
	.byte		VOL   , 93*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N06   , As4 
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N11   , Bn4 
	.byte	W12
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , As4 
	.byte	W02
@ 025   ----------------------------------------
	.byte	W03
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N06   , Gs4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N16   , Cs4 
	.byte	W17
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , As4 
	.byte	W06
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N28   
	.byte	W28
	.byte		VOL   , 93*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N05   , An4 
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N12   , As4 
	.byte	W12
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N05   , Bn4 
	.byte	W06
@ 026   ----------------------------------------
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , As4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N17   , Ds4 
	.byte	W18
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Bn4 
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		N05   , Ds5 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+63
	.byte		        c_v-2
	.byte		N05   , Fn5 
	.byte	W06
	.byte		BEND  , c_v+29
	.byte		        c_v-3
	.byte		N12   , Fs5 
	.byte	W12
	.byte		N11   
	.byte	W11
	.byte		VOL   , 93*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , As4 
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N12   , Bn4 
	.byte	W12
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N05   , Cs5 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Gs4 
	.byte	W04
@ 027   ----------------------------------------
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Bn4 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N17   , En4 
	.byte	W18
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Gs4 
	.byte	W05
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N05   , As3 
	.byte	W06
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N05   , Cs4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N05   , As3 
	.byte	W05
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N06   , Cs4 
	.byte	W07
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Gn4 
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N11   , Gs4 
	.byte	W11
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N06   , Cs4 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Fn4 
	.byte	W02
@ 028   ----------------------------------------
	.byte	W04
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N16   , As3 
	.byte	W17
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+15
	.byte		        c_v-3
	.byte		N05   , Fs4 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N06   , Bn4 
	.byte	W07
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W05
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Bn3 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Bn3 
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+15
	.byte		        c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N06   , As4 
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N11   , Bn4 
	.byte	W12
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , As4 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N06   , Gs4 
	.byte	W06
@ 029   ----------------------------------------
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N16   , Cs4 
	.byte	W17
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , As4 
	.byte	W05
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		        c_v-2
	.byte		N06   , Fs3 
	.byte	W07
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , As3 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Fs3 
	.byte	W06
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , As3 
	.byte	W06
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N05   , Cs4 
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , An4 
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N12   , As4 
	.byte	W12
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N05   , Bn4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , As4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N17   , Ds4 
	.byte	W04
@ 030   ----------------------------------------
	.byte	W14
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Bn4 
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		N05   , Ds5 
	.byte	W06
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , An4 
	.byte	W05
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N06   , Ds4 
	.byte	W07
	.byte		BEND  , c_v-2
	.byte		N05   , Cn4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		        c_v-1
	.byte		N05   , An3 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , Fs3 
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-52
	.byte		        c_v-2
	.byte		N12   , Bn4 
	.byte	W12
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N05   , Cs5 
	.byte	W01
	.byte		VOICE , 11
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N05   , Gs4 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , Bn4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N17   , En4 
	.byte	W08
@ 031   ----------------------------------------
	.byte	W10
	.byte		N05   
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Gs4 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N28   
	.byte	W28
	.byte	W01
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-35
	.byte		        c_v-3
	.byte		N05   , Gn4 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N11   , Gs4 
	.byte	W11
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N06   , Cs4 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , Fn4 
	.byte	W06
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N16   , As3 
	.byte	W11
@ 032   ----------------------------------------
	.byte	W06
	.byte		BEND  , c_v+15
	.byte		        c_v-3
	.byte		N05   , Fs4 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N06   , Bn4 
	.byte	W07
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N28   
	.byte	W28
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N06   , As4 
	.byte	W06
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N11   , Bn4 
	.byte	W11
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , As4 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N06   , Gs4 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N16   , Cs4 
	.byte	W15
@ 033   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , As4 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N28   
	.byte	W28
	.byte	W01
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N05   , An4 
	.byte	W06
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N12   , As4 
	.byte	W12
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N02   , Bn4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N03   , Ds4 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N03   , Bn4 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N02   , Ds4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N06   , Gs4 
	.byte	W07
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , An4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N03   , Cs4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W02
@ 034   ----------------------------------------
	.byte	W04
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N03   , As4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N02   , Dn4 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N03   , Bn4 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N17   
	.byte	W18
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N02   , Fs5 
	.byte	W02
	.byte		BEND  , c_v-4
	.byte		N03   , En5 
	.byte	W04
	.byte		BEND  , c_v-4
	.byte		N03   , Cs5 
	.byte	W03
	.byte		BEND  , c_v-2
	.byte		N02   , As4 
	.byte	W02
	.byte		BEND  , c_v-3
	.byte		N03   , Fs4 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W03
	.byte		BEND  , c_v-2
	.byte		N03   , Cs4 
	.byte	W03
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N03   , As3 
	.byte	W01
	.byte		VOICE , 12
	.byte	W02
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Fs2 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , As2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N42   , Bn2 , v127, gtp1
	.byte	W17
@ 035   ----------------------------------------
	.byte	W24
	.byte	W02
	.byte		N03   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-14
	.byte		        c_v-2
	.byte		N05   , Fs3 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Ds3 
	.byte	W06
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N05   , Dn3 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Ds3 
	.byte	W06
	.byte	GOTO
	 .word	mus_casino_plus_9_3_B1
mus_casino_plus_9_3_B2:
	.byte		BEND  , c_v-2
	.byte		N05   , Bn3 , v127
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N06   , Gs3 
	.byte	W06
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , Gn3 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N42   , Gs3 , v127, gtp1
	.byte	W21
@ 036   ----------------------------------------
	.byte	W23
	.byte		N24   , Gs3 , v127, gtp1
	.byte	W24
	.byte	W01
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Fs2 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N06   , As2 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N42   
	.byte	W24
@ 037   ----------------------------------------
	.byte	W18
	.byte		N03   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-14
	.byte		        c_v-2
	.byte		N05   , Fs3 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Ds3 
	.byte	W06
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N06   , Dn3 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Ds3 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , Gn3 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N17   
	.byte	W18
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+9
	.byte		        c_v-1
	.byte		N03   , Gs4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N42   
	.byte	W08
@ 038   ----------------------------------------
	.byte	W32
	.byte	W03
	.byte		N06   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Ds4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W03
@ 039   ----------------------------------------
	.byte	W02
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Cs4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W01
@ 040   ----------------------------------------
	.byte	W04
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , Cn3 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N06   , Cs3 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		N05   , Gs2 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+54
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W05
@ 041   ----------------------------------------
	.byte	W01
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Cs3 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N05   , Cn3 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Cs3 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N06   , En3 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Cs3 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , Fs3 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+15
	.byte		        c_v-1
	.byte		N05   , As2 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N05   , As2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N06   , Bn2 
	.byte	W07
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N05   , As2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N05   , Cs3 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N05   , Ds3 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-41
	.byte		        c_v-1
	.byte		N05   , Fs2 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		N06   , Gs2 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Fs2 
	.byte	W03
@ 042   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v+0
	.byte		N05   , Gs2 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N05   , Fs2 
	.byte	W06
	.byte		VOL   , 93*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+0
	.byte		N05   , Gs2 
	.byte	W06
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N06   , As2 
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+14
	.byte		        c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Ds4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W01
@ 043   ----------------------------------------
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N05   , Gs4 
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
@ 044   ----------------------------------------
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		        c_v-2
	.byte		N05   , Gn3 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N06   , En3 
	.byte	W07
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W05
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N05   , Cs3 
	.byte	W06
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , En3 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N06   , Fs3 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En3 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-1
	.byte		N05   , Fs2 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N05   , As2 
	.byte	W06
	.byte		BEND  , c_v-16
	.byte		        c_v-1
	.byte		N05   , Cs3 
	.byte	W03
@ 045   ----------------------------------------
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N06   , Fs3 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , As3 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N05   , Bn3 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Cs3 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , En3 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N06   , Cn3 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , En3 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , Gn3 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , As3 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N05   , Bn3 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Fs3 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N06   , Ds3 
	.byte	W06
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		BEND  , c_v-8
	.byte		        c_v-1
	.byte		N05   , Ds3 
	.byte	W05
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N05   , As2 
	.byte	W01
@ 046   ----------------------------------------
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N06   , Bn2 
	.byte	W06
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Fs2 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N05   , As2 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N42   , Bn2 , v127, gtp1
	.byte	W44
	.byte		N03   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-14
	.byte		        c_v-2
	.byte		N05   , Fs3 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Ds3 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N05   , Dn3 
	.byte	W05
@ 047   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Ds3 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N06   , Gs3 
	.byte	W07
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , Gn3 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N42   , Gs3 , v127, gtp1
	.byte	W42
	.byte	W01
	.byte		N24   , Gs3 , v127, gtp1
	.byte	W23
@ 048   ----------------------------------------
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Fs2 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N06   , As2 
	.byte	W07
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N42   
	.byte	W42
	.byte	W01
	.byte		N03   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-14
	.byte		        c_v-2
	.byte		N05   , Fs3 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Ds3 
	.byte	W05
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N06   , Dn3 
	.byte	W07
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Ds3 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N05   , Bn3 
	.byte	W01
@ 049   ----------------------------------------
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , Gn3 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N17   
	.byte	W18
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+9
	.byte		        c_v-1
	.byte		N03   , Gs4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N42   
	.byte	W42
	.byte		N06   
	.byte	W07
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W04
@ 050   ----------------------------------------
	.byte	W02
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Ds4 
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W03
@ 051   ----------------------------------------
	.byte	W04
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Cs4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W01
@ 052   ----------------------------------------
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Cn4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N06   , Cs4 
	.byte	W06
	.byte		BEND  , c_v-9
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+9
	.byte		        c_v-1
	.byte		N05   , Gs4 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Cs4 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , Cn4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N05   , Cs4 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N06   , En4 
	.byte	W07
	.byte		BEND  , c_v-2
	.byte		N05   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N05   , As3 
	.byte	W06
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N05   , Bn3 
	.byte	W04
@ 053   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , As3 
	.byte	W06
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N06   , Bn3 
	.byte	W06
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , As3 
	.byte	W06
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N05   , Bn3 
	.byte	W06
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N05   , Cs4 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N05   , Ds4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		        c_v-2
	.byte		N05   , Fs3 
	.byte	W05
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N06   , Gs3 
	.byte	W07
	.byte		BEND  , c_v-2
	.byte		N05   , Fs3 
	.byte	W05
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , Fs3 
	.byte	W06
	.byte		VOL   , 93*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+62
	.byte		        c_v-2
	.byte		N06   , As3 
	.byte	W07
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+15
	.byte		        c_v-3
	.byte		N05   , Fs4 
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W02
@ 054   ----------------------------------------
	.byte	W03
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Ds4 
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+63
	.byte		        c_v-1
	.byte		N05   , Gs4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
@ 055   ----------------------------------------
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 47*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N06   
	.byte	W07
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		        c_v-2
	.byte		N05   , Gn3 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+9
	.byte		        c_v-1
	.byte		N05   , Gs4 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N05   , Bn3 
	.byte	W06
	.byte		BEND  , c_v-11
	.byte		        c_v-1
	.byte		N06   , En4 
	.byte	W06
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N05   , Bn3 
	.byte	W06
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N05   , Cs4 
	.byte	W04
@ 056   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-8
	.byte		        c_v-2
	.byte		N05   , Bn3 
	.byte	W05
	.byte		BEND  , c_v-11
	.byte		        c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Gs4 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N06   , Fs4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Gs4 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		        c_v-2
	.byte		N05   , Fs3 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , As3 
	.byte	W06
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N05   , Cs4 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N06   , Fs4 
	.byte	W07
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , As4 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N05   , Bn4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Cs4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Gs4 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N06   , Cn4 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W02
@ 057   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v-3
	.byte		N05   , Gn4 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N05   , As4 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N05   , Bn4 
	.byte	W06
	.byte		BEND  , c_v-12
	.byte		        c_v-1
	.byte		N03   , Bn2 
	.byte	W03
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N03   , As2 
	.byte	W04
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , Bn2 
	.byte	W02
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-12
	.byte		        c_v-2
	.byte		N02   , Bn4 
	.byte	W03
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N03   
	.byte	W03
	.byte		VOL   , 93*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-4
	.byte		N03   , Ds5 
	.byte	W03
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W03
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N03   , Fs5 
	.byte	W03
	.byte		VOL   , 33*mus_casino_plus_9_mvl/mxv
	.byte		N02   
	.byte	W02
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-6
	.byte		N06   , Bn5 
	.byte	W07
	.byte		BEND  , c_v-4
	.byte		N05   , Cs5 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Gs4 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N01   , Bn4 
	.byte		N05   
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N17   , En4 
	.byte	W17
@ 058   ----------------------------------------
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Gs4 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N28   
	.byte	W28
	.byte	W01
	.byte		VOL   , 93*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-35
	.byte		        c_v-3
	.byte		N05   , Gn4 
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N11   , Gs4 
	.byte	W11
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N06   , Cs4 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Fn4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N16   , As3 
	.byte	W17
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+15
	.byte		        c_v-3
	.byte		N05   , Fs4 
	.byte	W04
@ 059   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v-2
	.byte		N06   , Bn4 
	.byte	W07
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N28   
	.byte	W28
	.byte		VOL   , 93*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N06   , As4 
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N11   , Bn4 
	.byte	W12
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , As4 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N06   , Gs4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N16   , Cs4 
	.byte	W17
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , As4 
	.byte	W02
@ 060   ----------------------------------------
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N28   
	.byte	W28
	.byte		VOL   , 93*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N05   , An4 
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N12   , As4 
	.byte	W12
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N05   , Bn4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , As4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N17   , Ds4 
	.byte	W18
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Bn4 
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		N05   , Ds5 
	.byte	W06
@ 061   ----------------------------------------
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+63
	.byte		        c_v-2
	.byte		N05   , Fn5 
	.byte	W06
	.byte		BEND  , c_v+29
	.byte		        c_v-3
	.byte		N12   , Fs5 
	.byte	W12
	.byte		N11   
	.byte	W11
	.byte		VOL   , 93*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , As4 
	.byte	W05
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N12   , Bn4 
	.byte	W13
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N05   , Cs5 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Gs4 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Bn4 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N17   , En4 
	.byte	W18
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Gs4 
	.byte	W05
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N05   , As3 
	.byte	W04
@ 062   ----------------------------------------
	.byte	W02
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N05   , Cs4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N05   , As3 
	.byte	W05
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N06   , Cs4 
	.byte	W07
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Gn4 
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N11   , Gs4 
	.byte	W11
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N06   , Cs4 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Fn4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N16   , As3 
	.byte	W17
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+15
	.byte		        c_v-3
	.byte		N05   , Fs4 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N06   , Bn4 
	.byte	W07
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-9
	.byte		        c_v-1
	.byte		N05   , Gs3 
	.byte	W05
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Bn3 
	.byte	W02
@ 063   ----------------------------------------
	.byte	W04
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , Gs3 
	.byte	W06
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Bn3 
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+15
	.byte		        c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N06   , As4 
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N11   , Bn4 
	.byte	W12
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , As4 
	.byte	W05
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N06   , Gs4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N16   , Cs4 
	.byte	W17
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , As4 
	.byte	W05
	.byte		VOL   , 57*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+2
	.byte		        c_v-2
	.byte		N06   , Fs3 
	.byte	W07
	.byte		VOL   , 66*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , As3 
	.byte	W05
@ 064   ----------------------------------------
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Fs3 
	.byte	W06
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , As3 
	.byte	W06
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+8
	.byte		        c_v-2
	.byte		N05   , Cs4 
	.byte	W05
	.byte		VOL   , 98*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , An4 
	.byte	W06
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N12   , As4 
	.byte	W12
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N05   , Bn4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , As4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N17   , Ds4 
	.byte	W18
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N05   , Bn4 
	.byte	W05
	.byte		BEND  , c_v-4
	.byte		N05   , Ds5 
	.byte	W06
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N05   , An4 
	.byte	W05
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		VOL   , 73*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N06   , Ds4 
	.byte	W04
@ 065   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-2
	.byte		N05   , Cn4 
	.byte	W06
	.byte		BEND  , c_v-3
	.byte		        c_v-1
	.byte		N05   , An3 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , Fs3 
	.byte	W05
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-52
	.byte		        c_v-2
	.byte		N12   , Bn4 
	.byte	W12
	.byte		BEND  , c_v+60
	.byte		        c_v-4
	.byte		N05   , Cs5 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Gs4 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , Bn4 
	.byte	W05
	.byte		BEND  , c_v-1
	.byte		N17   , En4 
	.byte	W18
	.byte		N05   
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Gs4 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N28   
	.byte	W19
@ 066   ----------------------------------------
	.byte	W10
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-35
	.byte		        c_v-3
	.byte		N05   , Gn4 
	.byte	W06
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N11   , Gs4 
	.byte	W11
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N06   , Cs4 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , Fn4 
	.byte	W06
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N16   , As3 
	.byte	W17
	.byte		BEND  , c_v+15
	.byte		        c_v-3
	.byte		N05   , Fs4 
	.byte	W05
	.byte		BEND  , c_v-2
	.byte		N06   , Bn4 
	.byte	W07
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N28   
	.byte	W22
@ 067   ----------------------------------------
	.byte	W06
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N06   , As4 
	.byte	W06
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N11   , Bn4 
	.byte	W11
	.byte		BEND  , c_v-34
	.byte		        c_v-2
	.byte		N05   , As4 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , En4 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N06   , Gs4 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N16   , Cs4 
	.byte	W17
	.byte		BEND  , c_v-3
	.byte		N05   , Fs4 
	.byte	W06
	.byte		BEND  , c_v-2
	.byte		N05   , As4 
	.byte	W05
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N28   
	.byte	W24
	.byte	W03
@ 068   ----------------------------------------
	.byte	W02
	.byte		VOL   , 87*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N05   , An4 
	.byte	W06
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N12   , As4 
	.byte	W12
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+30
	.byte		        c_v-2
	.byte		N02   , Bn4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N03   , Ds4 
	.byte	W04
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N03   , Bn4 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N02   , Ds4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W05
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-1
	.byte		N06   , Gs4 
	.byte	W07
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N02   , An4 
	.byte	W02
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N03   , Cs4 
	.byte	W03
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N05   
	.byte	W06
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N03   , As4 
	.byte	W03
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N02   , Dn4 
	.byte	W03
	.byte		VOL   , 109*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-2
	.byte		N03   , Bn4 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N02   , Ds4 
	.byte	W02
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N17   
	.byte	W18
	.byte		VOL   , 80*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-3
	.byte		N02   , Fs5 
	.byte	W02
	.byte		BEND  , c_v-4
	.byte		N03   , En5 
	.byte	W04
	.byte		BEND  , c_v-4
	.byte		N03   , Cs5 
	.byte	W01
@ 069   ----------------------------------------
	.byte	W02
	.byte		BEND  , c_v-2
	.byte		N02   , As4 
	.byte	W02
	.byte		BEND  , c_v-3
	.byte		N03   , Fs4 
	.byte	W03
	.byte		BEND  , c_v-1
	.byte		N02   , En4 
	.byte	W03
	.byte		BEND  , c_v-2
	.byte		N03   , Cs4 
	.byte	W03
	.byte		BEND  , c_v+6
	.byte		        c_v-2
	.byte		N03   , As3 
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v+12
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Fs2 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , As2 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte		N05   , Bn2 
	.byte	W06
	.byte		VOL   , 0*mus_casino_plus_9_mvl/mxv
	.byte		N42   , Bn2 , v127, gtp1
	.byte	W42
	.byte	W01
	.byte		N03   
	.byte	W03
	.byte		VOL   , 104*mus_casino_plus_9_mvl/mxv
	.byte		BEND  , c_v-14
	.byte		        c_v-2
	.byte		N05   , Fs3 
	.byte	W06
	.byte		BEND  , c_v-1
	.byte		N05   , Ds3 
	.byte	W05
@ 070   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v-33
	.byte		        c_v-1
	.byte		N05   , Dn3 
	.byte	W05
	.byte		BEND  , c_v+31
	.byte		        c_v-1
	.byte	W06
	.byte	FINE

@**************** Track 4 (Midi-Chn.10) ****************@

mus_casino_plus_9_4:
	.byte	KEYSH , mus_casino_plus_9_key+0
@ 000   ----------------------------------------
	.byte		VOICE , 0
	.byte		VOL   , 69*mus_casino_plus_9_mvl/mxv
	.byte		        69*mus_casino_plus_9_mvl/mxv
	.byte		PAN   , c_v+0
	.byte		        c_v+0
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N02   , Cn1 , v127
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W18
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W11
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
mus_casino_plus_9_4_B1:
	.byte		N02   , Cn1 , v127
	.byte	W04
@ 001   ----------------------------------------
	.byte	W08
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W24
	.byte		N02   , Cn1 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N11   , En1 
	.byte	W11
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W06
	.byte		N05   , En1 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N02   , Cn1 
	.byte	W08
@ 002   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W12
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W12
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W11
@ 003   ----------------------------------------
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W24
	.byte		N02   , Cn1 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N12   , En1 
	.byte	W12
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W05
	.byte		N05   , En1 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N02   , Cn1 
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W03
@ 004   ----------------------------------------
	.byte	W08
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W11
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W07
@ 005   ----------------------------------------
	.byte	W04
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W24
	.byte		N02   , Cn1 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N11   , En1 
	.byte	W11
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W06
	.byte		N05   , En1 
	.byte	W06
	.byte		N05   
	.byte	W05
	.byte		N02   , Cn1 
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
@ 006   ----------------------------------------
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W12
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W18
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W04
@ 007   ----------------------------------------
	.byte	W20
	.byte		N02   , Cn1 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N12   , En1 
	.byte	W12
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W06
	.byte		N05   , En1 
	.byte	W06
	.byte		N06   
	.byte	W06
	.byte		N02   , Cn1 
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W12
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W07
@ 008   ----------------------------------------
	.byte	W10
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W11
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W11
@ 009   ----------------------------------------
	.byte	W12
	.byte		N02   , Cn1 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N11   , En1 
	.byte	W11
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W06
	.byte		N05   , En1 
	.byte	W06
	.byte		N05   
	.byte	W05
	.byte		N02   , Cn1 
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W12
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W15
@ 010   ----------------------------------------
	.byte	W02
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W18
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W19
@ 011   ----------------------------------------
	.byte	W04
	.byte		N02   , Cn1 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N12   , En1 
	.byte	W12
	.byte		N05   
	.byte	W05
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N05   , En1 
	.byte	W06
	.byte		N06   
	.byte	W06
	.byte		N02   , Cn1 
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W12
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W05
@ 012   ----------------------------------------
	.byte	W01
	.byte		N02   
	.byte	W11
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W23
	.byte		N02   , Cn1 
	.byte	W03
@ 013   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N11   , En1 
	.byte	W11
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W07
	.byte		N05   , En1 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N02   , Cn1 
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W12
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W07
@ 014   ----------------------------------------
	.byte	W05
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W18
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W23
	.byte		N02   , Cn1 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W05
@ 015   ----------------------------------------
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N12   , En1 
	.byte	W12
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W06
	.byte		N05   , En1 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W07
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N02   , Cn1 
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W18
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W11
	.byte		N02   
	.byte	W03
@ 016   ----------------------------------------
	.byte	W03
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W23
	.byte		N02   , Cn1 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N11   , En1 
	.byte	W07
@ 017   ----------------------------------------
	.byte	W05
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W07
	.byte		N05   , En1 
	.byte	W05
	.byte		N05   
	.byte	W06
	.byte		N02   , Cn1 
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W12
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W05
@ 018   ----------------------------------------
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W18
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W23
	.byte		N02   , Cn1 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N12   , En1 
	.byte	W13
	.byte		N02   , Cn1 
	.byte	W02
@ 019   ----------------------------------------
	.byte	W03
	.byte		N02   
	.byte	W06
	.byte		N05   , En1 
	.byte	W05
	.byte		N06   
	.byte	W07
	.byte		N02   , Cn1 
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W18
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W11
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W06
@ 020   ----------------------------------------
	.byte	W11
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W23
	.byte		N02   , Cn1 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N11   , En1 
	.byte	W12
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W05
@ 021   ----------------------------------------
	.byte	W02
	.byte		N05   , En1 
	.byte	W05
	.byte		N05   
	.byte	W06
	.byte		N02   , Cn1 
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W12
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W14
@ 022   ----------------------------------------
	.byte	W04
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W23
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W07
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   , En1 
	.byte	W05
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N05   , En1 
	.byte	W06
	.byte		N05   
	.byte	W05
	.byte		N06   
	.byte	W01
@ 023   ----------------------------------------
	.byte	W10
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W13
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W10
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W24
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W08
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W02
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
@ 024   ----------------------------------------
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W02
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W14
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W09
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W24
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W07
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W06
	.byte		N06   
	.byte	W10
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W08
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W02
@ 025   ----------------------------------------
	.byte	W02
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W14
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W10
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W24
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W07
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W03
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W02
@ 026   ----------------------------------------
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W13
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N06   
	.byte	W10
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W24
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W08
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W05
	.byte		N06   
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
@ 027   ----------------------------------------
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W13
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W10
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W24
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W08
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W02
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W02
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W04
@ 028   ----------------------------------------
	.byte	W10
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W09
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W24
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W07
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W06
	.byte		N06   
	.byte	W10
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W08
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W08
@ 029   ----------------------------------------
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W10
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W24
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W08
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W02
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W02
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W02
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W11
@ 030   ----------------------------------------
	.byte	W02
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N06   
	.byte	W10
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W24
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W08
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W06
	.byte		N05   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N06   
	.byte	W30
	.byte	W01
@ 031   ----------------------------------------
	.byte	W96
@ 032   ----------------------------------------
	.byte	W96
@ 033   ----------------------------------------
	.byte	W60
	.byte		N11   
	.byte	W11
	.byte		N11   
	.byte	W11
	.byte		N02   , Cn1 
	.byte	W07
	.byte		N11   , En1 
	.byte	W07
@ 034   ----------------------------------------
	.byte	W04
	.byte		N05   
	.byte	W06
	.byte		N23   
	.byte	W23
	.byte		N02   , Cn1 
	.byte	W11
	.byte		N02   
	.byte	W06
	.byte		N06   , En1 
	.byte	W06
	.byte		N02   , Cn1 
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W17
@ 035   ----------------------------------------
	.byte	W01
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W11
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
	.byte	GOTO
	 .word	mus_casino_plus_9_4_B1
mus_casino_plus_9_4_B2:
	.byte		N02   , Cn1 , v127
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W21
@ 036   ----------------------------------------
	.byte	W03
	.byte		N02   , Cn1 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N11   , En1 
	.byte	W11
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W06
	.byte		N05   , En1 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N02   , Cn1 
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W12
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W02
@ 037   ----------------------------------------
	.byte	W10
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W24
	.byte		N02   , Cn1 
	.byte	W05
@ 038   ----------------------------------------
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N12   , En1 
	.byte	W12
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W05
	.byte		N05   , En1 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N02   , Cn1 
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W12
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W09
@ 039   ----------------------------------------
	.byte	W02
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W24
	.byte		N02   , Cn1 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N11   , En1 
	.byte	W01
@ 040   ----------------------------------------
	.byte	W10
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W06
	.byte		N05   , En1 
	.byte	W06
	.byte		N05   
	.byte	W05
	.byte		N02   , Cn1 
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W12
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W16
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		N02   
	.byte	W05
@ 041   ----------------------------------------
	.byte	W01
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W18
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W24
	.byte		N02   , Cn1 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N12   , En1 
	.byte	W09
@ 042   ----------------------------------------
	.byte	W03
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W06
	.byte		N05   , En1 
	.byte	W06
	.byte		N06   
	.byte	W06
	.byte		N02   , Cn1 
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W12
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W11
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W01
@ 043   ----------------------------------------
	.byte	W16
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W23
	.byte		N02   , Cn1 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N11   , En1 
	.byte	W11
	.byte		N02   , Cn1 
	.byte	W05
@ 044   ----------------------------------------
	.byte		N02   
	.byte	W07
	.byte		N05   , En1 
	.byte	W06
	.byte		N05   
	.byte	W05
	.byte		N02   , Cn1 
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W12
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W09
@ 045   ----------------------------------------
	.byte	W09
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W23
	.byte		N02   , Cn1 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N12   , En1 
	.byte	W12
	.byte		N05   
	.byte	W05
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N05   , En1 
	.byte	W01
@ 046   ----------------------------------------
	.byte	W05
	.byte		N06   
	.byte	W06
	.byte		N02   , Cn1 
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W12
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W11
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W16
@ 047   ----------------------------------------
	.byte	W01
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W23
	.byte		N02   , Cn1 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N11   , En1 
	.byte	W12
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W07
	.byte		N05   , En1 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W03
@ 048   ----------------------------------------
	.byte	W03
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N02   , Cn1 
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W12
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W18
	.byte		N02   , Cn1 
	.byte	W06
@ 049   ----------------------------------------
	.byte		N02   
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W23
	.byte		N02   , Cn1 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N12   , En1 
	.byte	W12
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W06
	.byte		N05   , En1 
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W07
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N02   , Cn1 
	.byte	W04
@ 050   ----------------------------------------
	.byte	W07
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W18
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W11
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W08
@ 051   ----------------------------------------
	.byte	W04
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W23
	.byte		N02   , Cn1 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N11   , En1 
	.byte	W12
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W07
	.byte		N05   , En1 
	.byte	W05
	.byte		N05   
	.byte	W06
	.byte		N02   , Cn1 
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W01
@ 052   ----------------------------------------
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W18
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W04
@ 053   ----------------------------------------
	.byte	W07
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W23
	.byte		N02   , Cn1 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N12   , En1 
	.byte	W12
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W06
	.byte		N05   , En1 
	.byte	W05
	.byte		N06   
	.byte	W07
	.byte		N02   , Cn1 
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W08
@ 054   ----------------------------------------
	.byte	W03
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W18
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W11
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W07
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W17
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W12
@ 055   ----------------------------------------
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W23
	.byte		N02   , Cn1 
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W05
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N11   , En1 
	.byte	W12
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W07
	.byte		N05   , En1 
	.byte	W05
	.byte		N05   
	.byte	W06
	.byte		N02   , Cn1 
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W12
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W04
@ 056   ----------------------------------------
	.byte	W13
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W12
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W18
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N23   , En1 
	.byte	W08
@ 057   ----------------------------------------
	.byte	W15
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N02   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W07
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   , En1 
	.byte	W05
	.byte		N02   , Cn1 
	.byte	W06
	.byte		N05   , En1 
	.byte	W06
	.byte		N05   
	.byte	W05
	.byte		N06   
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W13
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W10
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W02
@ 058   ----------------------------------------
	.byte	W23
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W08
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W02
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W02
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W14
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W09
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
@ 059   ----------------------------------------
	.byte	W19
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W07
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W06
	.byte		N06   
	.byte	W10
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W08
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W14
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W10
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W09
@ 060   ----------------------------------------
	.byte	W16
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W07
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W03
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W02
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W13
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N06   
	.byte	W10
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W13
@ 061   ----------------------------------------
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W08
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W05
	.byte		N06   
	.byte	W11
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W13
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W10
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W17
@ 062   ----------------------------------------
	.byte	W08
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W08
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W02
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W02
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W14
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W09
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W21
@ 063   ----------------------------------------
	.byte	W04
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W07
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W06
	.byte		N06   
	.byte	W10
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W08
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W01
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W14
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W10
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W24
@ 064   ----------------------------------------
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W08
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W02
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W02
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W02
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W13
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N06   
	.byte	W10
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W24
	.byte		        c_v-13
	.byte		        c_v-13
	.byte	W04
@ 065   ----------------------------------------
	.byte		        c_v+0
	.byte		        c_v+0
	.byte	W08
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N05   
	.byte	W06
	.byte		N05   
	.byte	W05
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N06   
	.byte	W68
	.byte	W03
@ 066   ----------------------------------------
	.byte	W96
@ 067   ----------------------------------------
	.byte	W96
@ 068   ----------------------------------------
	.byte	W20
	.byte		N11   
	.byte	W11
	.byte		N11   
	.byte	W11
	.byte		N02   , Cn1 
	.byte	W07
	.byte		N11   , En1 
	.byte	W11
	.byte		N05   
	.byte	W06
	.byte		N23   
	.byte	W23
	.byte		N02   , Cn1 
	.byte	W07
@ 069   ----------------------------------------
	.byte	W04
	.byte		N02   
	.byte	W06
	.byte		N06   , En1 
	.byte	W06
	.byte		N02   , Cn1 
	.byte	W12
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W11
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N17   , En1 
	.byte	W18
	.byte		N02   , Cn1 
	.byte	W05
	.byte		N02   
	.byte	W11
	.byte		N02   
	.byte	W06
	.byte		BEND  , c_v+0
	.byte		        c_v+0
	.byte	W06
	.byte		        c_v-13
	.byte		        c_v-13
	.byte		N16   , En1 
	.byte	W11
@ 070   ----------------------------------------
	.byte	W06
	.byte		N02   , Cn1 
	.byte	W06
	.byte	FINE

@******************************************************@
	.align	2

mus_casino_plus_9:
	.byte	4	@ NumTrks
	.byte	0	@ NumBlks
	.byte	mus_casino_plus_9_pri	@ Priority
	.byte	mus_casino_plus_9_rev	@ Reverb.

	.word	mus_casino_plus_9_grp

	.word	mus_casino_plus_9_1
	.word	mus_casino_plus_9_2
	.word	mus_casino_plus_9_3
	.word	mus_casino_plus_9_4

	.end
