from google_polyline import *

polylines = [
    "}}|uFbkyfNyCIa@E[C{A?gDMqAIcAIk@GYfAc@lBoAvEm@zBS~@c@jBEXE`@i@vBmClK]tAUZo@jC_CnKA|A^|OF`EDjDk@zIiB`X}@vLoBbXCr@BhBd@fFj@rFnB|S",
    "mj~uFfx_gNo@p@Y`@gCfDq@|@y@bAoBpCq@x@{@lAuAlBoAzA",
    "o`_vFhs`gNqAkB_@g@g@w@}@gAoA{@MGeAm@gDqBgC_BeCaBcCcB_BgAECc@WQK_@E_DG{ACa@A_@@OCKA]QwAgAy@m@oDiDsAqAaLsF}@k@o@a@s@c@KEOMAAGGACa@u@kBcEmC_GoB_Ec@}@cA{C{@iCc@mAc@uAc@mAoA{D{CqLsBiISw@kEsP{AiGQq@U_AUs@EOKi@e@cBg@sBS_AMe@GWEQCMAKAI?I?e@?e@@sA?eBB}B@qA?c@AOAOAQCUO}@CWk@sDE_@Ea@AQASNePFu@b@_Dj@}Dh@uDLw@l@gEjAkIbAgHFe@Hg@",
    "kwbvF|hxfNsHth@k@tEMxPFr@p@rEX|BB^AtBE|IBdA`CtJ",
    "c|bvFxt{fNINEHMV",
    "a}bvFjv{fNg@HMBq@N_AP_APaAP{EfAiCj@cAT]DQDUFsDx@aATMBIB]Jk@Pc@LcAb@m@XKF]R]PIBMF{@b@IB]N_AX_@Ja@HQDe@JaAN]HaBXmB\\M@UDQFOFQFQFo@XQHm@X?@cAn@{BzAy@n@kAlAi@x@Yd@[r@Q^Wx@K\\AJa@rB[~BETGj@K|@I^Ux@GNGPGPEJEDEJINMXW`@GHIFGFIDMHSJQDU?",
    "ozevFvu}fNT?PE`@Ub@_@t@wAZu@\\iAT}ALaA|@sFLi@h@yAt@yAh@y@jAmAtDkCbAq@`CeAhA]zB_@~Bc@xBa@`AU|Ai@rAo@f@U\\Sx@a@fBq@`Be@|G}A`B[dJsBrFeApASLA@D",
    "u{bvFhv{fN{AgGo@oCGm@@eGBcGWuB{@mGCe@NePFu@nA}Iv@mFdEaZp@_ERmAJyA\\{Cl@yDrCgQvDoUReA^uA\\aA\\q@\\e@RQN?F?bAc@r@MJANGp@Ft@H|AJrA?dAE|CW~BK|CAjBD`Uz@nERlBFzGTxGXVH",
    "uo_vFlcvfNHFB?xCH?bA@\\D\\FTJ^JTPVj@p@r@v@p@x@LRJPl@`Ap@~A^hA`@jA\\lA^hAj@fBRp@f@xAHb@Rp@VnALx@\\vB@R?@\\hCJx@BPJt@PbA`@|Af@jBPb@HVJNTTPNpCzAVNk@|B]lAi@zBGZKb@EREXERAXCPK~@KfAGr@CNIZe@~Bs@pCYhAi@rBYhA_ArDcAzDvBjArAp@dExB~EfCvAr@lAj@XP_@xA]zAEf@Kj@c@~A}A|G[|ACHAHAJ?N?f@?VBb@LhGFnCD`BBfABxBDfC?b@CXIrA[|EANi@hIYzDG~@]zEWhDIfAKrAOnBAPOnBi@fHs@zJAVAZ?p@Bv@H`ADXH~@JjAFd@LtAJbAHr@TpBNlB^xDl@`GV`DHx@b@`EHr@PxBRrB`@lEPrBHl@RzBH|@fAQhDvF`DbFFFDHDDHNV`@RVDDDBP@d@MHCNELEPGf@QbA[j@YxAg@pAg@NILEDEJGLGLG\\QVMn@UFGHCDGBEBIBG?I?G?F?HCFCHCDEFIBGFo@TWL]PMFMFKFEDMDOHqAf@yAf@k@XcAZg@PQFMDODIBe@LQAECEESWWa@IOEEEIGGu@`AMRk@n@EGe@M_BkAyBqAECc@WgAu@gDwBo@a@sBkAcAo@}@m@MIg@]MKiAu@gCiD}AwBsAmB_@e@g@w@}@gAoA{@MGcAm@iDqBgC_BeCaBcCeB_BgACAe@WQK_@E}CI}AAa@A_@@OEK?]QwAgAy@m@oDiDqAqAcLsF}@k@o@a@s@c@KEOMACEECC_@u@mBcEmC_GoB_Ec@}@cA{C{@kCc@kAc@uAc@oAoA{D{CoLsBiISw@kEsP{AiGQq@UaAUq@COMi@e@cBg@sBS_AMe@GWEQCOAIAI?I?e@?e@@sA?gBB}B@oA?c@AQAMAQAUQ}@LM?{@FI?W@wB?q@@{@?a@Dk@Dq@f@uGLqAJw@dAeHD[BG?GFOGN?FCFEZeAdHKv@MpAg@tGEp@Ej@?`@Az@?p@AvB?V?\\?P?F?D@B?F@NDRD^BP@H@D?DBD?F?JCZAtAA\\AVCj@?B?FCB?D??CFGH?fBArA?d@?d@?H@H@HBNDPFVLd@R~@f@rBd@bBGNGHMVg@HMBq@N_AP_AP_AP}EfAiCj@cAR]FQDUFqDx@cATMBGB_@Jk@Pc@JcAb@k@XMH]P]RIBMFy@b@KB]N_AX_@Ha@HQFe@HaAP]FaBZmB\\M@UDQDMHQFQFq@XQHk@X?@eAn@{BzAy@n@kAlAi@v@Wf@]p@Q`@Wx@K\\AJa@rB[|BCVIj@K|@I\\Uz@GNGPEPGJEDCJKNMXW^GJIDGFIFMHSHQFa@AUAKCGAICIESOQMOOSMOQe@We@YSKSISISISGa@KMBa@GQCQEQAQA[C]AeDGyBAxB@dDF\\@ZBP@P@PDPB`@FPVD@PFTFPHPHRHRJPJPJd@XNLPLZ\\XLLFXHJ?~@Fl@[JEHIFCJMNSFOT[f@iAN_@FQLe@FABCFIHQHQj@iALD`@H@YDg@@[BSDQDOFMT]RSRWNIVQd@SDAx@[HEFADCD?H?L?Z?vFAzEHfADzBHJ@J?BBD@JBDDJHFF`@j@`@l@lAxAh@l@l@r@|AlB`BjBdD|GeAzAA\\?HAH?HAT?\\Cj@Cl@?R?PBLBHBLBJHPXj@HJDTBTJl@F|@DXBTBLFj@?NDT?N@VA^?F@NAN@TBPBLBJDHBFFHFJBBLDRb@HLFJ@F@D@F~@rC`BhFb@`AXt@~BbGxBjCz@`Ah@n@x@fAlAbBl@x@n@|@b@n@b@z@Zz@n@lBPb@b@nAh@fBb@dBd@fBb@xAFNNb@Td@Nd@J^Nf@RjApA~FJ\\Vz@^tA\\tAZ|A^pB?RBJ?L@d@?|B`@`EJzALjB"
]

def concat_polylines(polylines):
    line_coords = []
    for line in polylines:
        if(line_coords == []):
            line_coords += decode(line)
        else:
            line_coords += decode(line)[1:]

    return encode_coords(line_coords)

print(concat_polylines(polylines))
