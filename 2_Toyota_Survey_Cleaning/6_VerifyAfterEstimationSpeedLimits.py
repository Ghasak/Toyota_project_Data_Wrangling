"""
=========================================================
       Verifying the Speed Limit Configuration
            Wed Sep. 18th 2019
                 17:00:00,
=========================================================
    To Run Independently use:
    -------------------------
    python 2_Toyota_Survey_Cleaning/6_VerifyAfterEstimationSpeedLimits.py
    Or using IPython:
    %run 2_Toyota_Survey_Cleaning/6_VerifyAfterEstimationSpeedLimits.py

    Working Plan:
    -------------
    - We would like to know the speed limit crash sum by
        driver's age and verify it with the univariate
        and the multivariate model results.
    [Steps]
    A- Locate and load last crash (accidents) data before
        combined with the Survey crashes dataset (U-sensei)
        plus the one you used with the 35 meter configuration.

    B- Check your current dataset (after pivoting and clearning)
        and applying the dummies.

    C- Then you can get only the intersections that has been
        removed from your last dataset.

    D- The final results should show the sum of crashes per driver's
        age and how they are refactored to our current dataframe.

    To-Do List:
    -----------
    1- You want to create a dataset with only the accidents available
        after applying 35-rule, dummies, refined --> the Modeling Dataset
        as it called (refined.xls). This will be a dataset for both
        drawing the crash density over all places in Toyota City
    2- Verify the speed limit using the new dataset usign pivot table.


"""
# ==================================================#
#           Import Libraries
# ==================================================#
# Load the Pandas libraries with alias 'pd'
import pandas as pd
import numpy as np
import re
import os
import sys
from Cleaning_tools_G import *
sys.path.append(os.getcwd()+"/")
CURRENTPATH = os.getcwd()
CRASHDATAPATH = os.path.join(CURRENTPATH+"/2_Toyota_Survey_Cleaning/SpeedLimitVerficiationData/3_Acc_ID_Final.xlsx")
# print(CRASHDATAPATH)
INTERSECTIONDATAPATH = CURRENTPATH + "/2_Toyota_Survey_Cleaning/Toyota_Survey_Sheetfiles/4_Refine_Dataframe/refined_df.xlsx"
# ==================================================#
#           Step A Load your dataset
# ==================================================#
Acc_ID_Final = pd.read_excel(CRASHDATAPATH , sheet_name=0)
print(Acc_ID_Final.head())

# ==================================================#
#              Import Dataset from Script
#           3_Creating_Dummies_continued.py
# ==================================================#
df = pd.read_excel(INTERSECTIONDATAPATH,sheet_name='DataSet')
print(df.head())

