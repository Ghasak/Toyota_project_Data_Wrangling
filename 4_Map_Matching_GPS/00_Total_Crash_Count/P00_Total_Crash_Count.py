"""
=========================================================
          Creating Dummies for and
            arrange your dataset
            Tue Jun. 19th 2019
                 17:03:00,
=========================================================
    - We will create dummies using the pandas package to
        make all categorical variables dummies.
    - We will remove the non-necessary columns/variables
        from our Survey dataset as we don't need them
    -
"""
# ==================================================#
#           Import Libraries
# ==================================================#
# Load the Pandas libraries with alias 'pd'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import os
Current_Path = os.getcwd()

# print(Current_Path)
# print(f"This is the relative path {os.path.abspath(os.getcwd())}")
# print(f"This is the full path {os.path.dirname(os.path.abspath(__file__))}")

inner_joint_Int = pd.read_excel(Current_Path +
                                "/Toyota_Survey_Sheetfiles/1_Cleaning_Data_set/Results/inner_joint_Int.xlsx",
                                sheet_name="inner_joint_Int")



inner_joint_Int['Altitude'] = inner_joint_Int['Altitude'].astype(float)
inner_joint_Int['Longitute'] = inner_joint_Int['Longitute'].astype(float)
plt.show(inner_joint_Int.plot(kind="scatter",
                                 x="Longitute",
                                 y="Altitude",
                                 s=inner_joint_Int['Crash_count']*10, label ="Crash Count",figsize = (10,7),
                                 c="Crash_count", cmap=plt.get_cmap("jet"), colorbar=True,
                                 sharex=False,
                                 alpha=0.1))

