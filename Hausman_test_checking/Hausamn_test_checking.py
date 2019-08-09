'''
        Conducting Hausamn's Test:

        b = consistent under Ho and Ha; obtained from nbreg
        B = inconsistent under Ha, efficient under Ho; obtained from poisson

        Test:  Ho:  difference in coefficients not systematic

            chi2(19) = (b-B)'[(V_b-V_B)^(-1)](b-B)

'''


import pandas as pd
import numpy as np
import os
Current_Path = os.getcwd()

'''
        Input the Base Model here - Poisson model
            no-constants:

'''
Poisson_Matrix = pd.read_excel(Current_Path +
                                "/Hausman_test_checking.xlsx",
                                sheet_name="Poisson_Matrix")
Poisson_Matrix.index  = Poisson_Matrix['index']
Poisson_Matrix.drop(['index'], axis = 1,inplace = True)


'''
        Input the Variance-Covariance of the suggested model
            the suggested model here is : NBII
            no-constant and no dispersion parameter
'''
NBII_Matrix = pd.read_excel(Current_Path +
                                "/Hausman_test_checking.xlsx",
                                sheet_name="NBII_Matrix")

NBII_Matrix.index  = NBII_Matrix['index']
NBII_Matrix.drop(['index'], axis = 1,inplace = True)


'''
    Input the parameters of estimate assume
    b: is the vector of the suggested model (NBII)
    B: is the vector of the base model (poisson)
'''

Vectors = pd.read_excel(Current_Path +
                                "/Hausman_test_checking.xlsx",
                                sheet_name="Vectors")

# chi2(19) = (b-B)'[(V_b-V_B)^(-1)](b-B)

C = (Vectors['b']-Vectors['B'])

B = Poisson_Matrix.to_numpy()
A = NBII_Matrix.to_numpy()

M = np.linalg.inv(A-B)

R = ((C.T).dot(M)).dot(C)

S = (C.T).dot(M)

print("-------------+-----------------------")
print(f"The value of Hausman's test is = {R}")
print("-------------+-----------------------")
# The results is : 3.6273073810583787 which is same as STATA

'''
Example= Total Number of crashes: Toyota City
---- Coefficients ----
|      (b)          (B)            (b-B)     sqrt(diag(V_b-V_B))
|  nbII_final~l poisson_fi~l    Difference          S.E.
-------------+----------------------------------------------------------------
Minor_pref~d |    .1826186     .1722504        .0103682        .0256661
Narrow_road |    .5042419     .5272689       -.0230269        .0397776
conf1_30km~s |    .3911569     .3891669          .00199        .0348945
conf1_40km~s |    .5937907     .5944551       -.0006644        .0287893
conf1_50km~s |    .5929481     .6037543       -.0108062        .0297459
conf1_60km~s |     .325024     .3289966       -.0039726        .0267186
conf1_No_r~n |    .4006754     .4026645       -.0019891        .0243691
log_traffi~e |    .0984464     .1040154        -.005569        .0085993
IS_IT_THRE~S |   -.1996484    -.2162154        .0165671        .0371965
LOG_SHORTE~R |     .098151     .1030792       -.0049282        .0267523
LOG_NO_DRI~S |   -.0690657     -.070487        .0014212        .0161586
LOG_NUMBER~S |    .5383384      .582053       -.0437146        .0625468
NO_OF_LANE~D |   -.1755754    -.1921777        .0166022        .0422676
IS_THERE_S~S |    .0437858     .0516953       -.0079094        .0231352
NON_DIVIDE~Y |   -.1400987    -.1502704        .0101718        .0293216
LOG_AVERAG~A |    .1191682     .1194617       -.0002935        .0290461
IS_THERE_C~P |   -.1811507     -.196414        .0152633        .0361446
SIG~L_SIGNAL |    .1541095     .1501088        .0040007        .0297957
FLASHING_G~D |    .1102788     .1179784       -.0076996        .0294894
------------------------------------------------------------------------------
              b = consistent under Ho and Ha; obtained from nbreg
B = inconsistent under Ha, efficient under Ho; obtained from poisson

Test:  Ho:  difference in coefficients not systematic

    chi2(19) = (b-B)'[(V_b-V_B)^(-1)](b-B)
             =        3.63
   Prob>chi2 =      1.0000'''
