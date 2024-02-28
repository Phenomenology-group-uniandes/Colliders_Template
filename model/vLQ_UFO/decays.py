# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Microsoft Windows (64-bit) (December 13, 2023)
# Date: Wed 28 Feb 2024 04:32:53


from object_library import all_decays, Decay
import particles as P


Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.VLQ,P.vm):'((MT**2 - MVLQ**2)*((3*gU**2*I5a23*MT**2*complexconjugate(I5a23))/2. + (3*gU**2*I5a23*MT**4*complexconjugate(I5a23))/(2.*MVLQ**2) - 3*gU**2*I5a23*MVLQ**2*complexconjugate(I5a23)))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.VLQ,P.vt):'((MT**2 - MVLQ**2)*((3*gU**2*I5a33*MT**2*complexconjugate(I5a33))/2. + (3*gU**2*I5a33*MT**4*complexconjugate(I5a33))/(2.*MVLQ**2) - 3*gU**2*I5a33*MVLQ**2*complexconjugate(I5a33)))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.W__plus__,P.b):'((MT**2 - MW**2)*((3*CKM3x3*ee**2*MT**2*complexconjugate(CKM3x3))/(2.*sw**2) + (3*CKM3x3*ee**2*MT**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) - (3*CKM3x3*ee**2*MW**2*complexconjugate(CKM3x3))/sw**2))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.W__plus__,P.d):'((MT**2 - MW**2)*((3*CKM3x1*ee**2*MT**2*complexconjugate(CKM3x1))/(2.*sw**2) + (3*CKM3x1*ee**2*MT**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) - (3*CKM3x1*ee**2*MW**2*complexconjugate(CKM3x1))/sw**2))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.W__plus__,P.s):'((MT**2 - MW**2)*((3*CKM3x2*ee**2*MT**2*complexconjugate(CKM3x2))/(2.*sw**2) + (3*CKM3x2*ee**2*MT**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) - (3*CKM3x2*ee**2*MW**2*complexconjugate(CKM3x2))/sw**2))/(96.*cmath.pi*abs(MT)**3)'})

Decay_VLQ = Decay(name = 'Decay_VLQ',
                  particle = P.VLQ,
                  partial_widths = {(P.b,P.mu__plus__):'(betaL3x2**2*gU**2*MVLQ**4)/(48.*cmath.pi*abs(MVLQ)**3)',
                                    (P.b,P.ta__plus__):'(MVLQ**2*(3*betaL3x3**2*gU**2*MVLQ**2 + 3*betaRd3x3**2*gU**2*MVLQ**2))/(144.*cmath.pi*abs(MVLQ)**3)',
                                    (P.c,P.vm__tilde__):'(gU**2*I6a22*MVLQ**4*complexconjugate(I6a22))/(48.*cmath.pi*abs(MVLQ)**3)',
                                    (P.c,P.vt__tilde__):'(gU**2*I6a23*MVLQ**4*complexconjugate(I6a23))/(48.*cmath.pi*abs(MVLQ)**3)',
                                    (P.d,P.ta__plus__):'(betaL1x3**2*gU**2*MVLQ**4)/(48.*cmath.pi*abs(MVLQ)**3)',
                                    (P.s,P.ta__plus__):'(betaL2x3**2*gU**2*MVLQ**4)/(48.*cmath.pi*abs(MVLQ)**3)',
                                    (P.t,P.vm__tilde__):'((-MT**2 + MVLQ**2)*((-3*gU**2*I6a32*MT**2*complexconjugate(I6a32))/2. - (3*gU**2*I6a32*MT**4*complexconjugate(I6a32))/(2.*MVLQ**2) + 3*gU**2*I6a32*MVLQ**2*complexconjugate(I6a32)))/(144.*cmath.pi*abs(MVLQ)**3)',
                                    (P.t,P.vt__tilde__):'((-MT**2 + MVLQ**2)*((-3*gU**2*I6a33*MT**2*complexconjugate(I6a33))/2. - (3*gU**2*I6a33*MT**4*complexconjugate(I6a33))/(2.*MVLQ**2) + 3*gU**2*I6a33*MVLQ**2*complexconjugate(I6a33)))/(144.*cmath.pi*abs(MVLQ)**3)',
                                    (P.u,P.vm__tilde__):'(gU**2*I6a12*MVLQ**4*complexconjugate(I6a12))/(48.*cmath.pi*abs(MVLQ)**3)',
                                    (P.u,P.vt__tilde__):'(gU**2*I6a13*MVLQ**4*complexconjugate(I6a13))/(48.*cmath.pi*abs(MVLQ)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.b__tilde__):'(CKM2x3*ee**2*MW**4*complexconjugate(CKM2x3))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.c,P.d__tilde__):'(CKM2x1*ee**2*MW**4*complexconjugate(CKM2x1))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.c,P.s__tilde__):'(CKM2x2*ee**2*MW**4*complexconjugate(CKM2x2))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'((-MT**2 + MW**2)*((-3*CKM3x3*ee**2*MT**2*complexconjugate(CKM3x3))/(2.*sw**2) - (3*CKM3x3*ee**2*MT**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) + (3*CKM3x3*ee**2*MW**2*complexconjugate(CKM3x3))/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.d__tilde__):'((-MT**2 + MW**2)*((-3*CKM3x1*ee**2*MT**2*complexconjugate(CKM3x1))/(2.*sw**2) - (3*CKM3x1*ee**2*MT**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) + (3*CKM3x1*ee**2*MW**2*complexconjugate(CKM3x1))/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.s__tilde__):'((-MT**2 + MW**2)*((-3*CKM3x2*ee**2*MT**2*complexconjugate(CKM3x2))/(2.*sw**2) - (3*CKM3x2*ee**2*MT**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) + (3*CKM3x2*ee**2*MW**2*complexconjugate(CKM3x2))/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.b__tilde__):'(CKM1x3*ee**2*MW**4*complexconjugate(CKM1x3))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(CKM1x1*ee**2*MW**4*complexconjugate(CKM1x1))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.u,P.s__tilde__):'(CKM1x2*ee**2*MW**4*complexconjugate(CKM1x2))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.VLQ__tilde__,P.VLQ):'(((-16*ee**2*MVLQ**2*sw**2)/cw**2 - (68*ee**2*MZ**2*sw**2)/(3.*cw**2) + (80*ee**2*kappaUtilde*MZ**2*sw**2)/(3.*cw**2) - (16*ee**2*kappaUtilde**2*MZ**2*sw**2)/(3.*cw**2) + (16*ee**2*MZ**4*sw**2)/(3.*cw**2*MVLQ**2) - (4*ee**2*kappaUtilde*MZ**4*sw**2)/(cw**2*MVLQ**2) + (ee**2*MZ**6*sw**2)/(3.*cw**2*MVLQ**4) - (2*ee**2*kappaUtilde*MZ**6*sw**2)/(3.*cw**2*MVLQ**4) + (ee**2*kappaUtilde**2*MZ**6*sw**2)/(3.*cw**2*MVLQ**4))*cmath.sqrt(-4*MVLQ**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

