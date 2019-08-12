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
CURRENT_PATH = os.getcwd()

print(CURRENT_PATH)
os.chdir(CURRENT_PATH)
CURRENT_PATH = os.getcwd()
# print(f"This is the relative path {os.path.abspath(os.getcwd())}")
# print(f"This is the full path {os.path.dirname(os.path.abspath(__file__))}")

df = pd.read_excel(CURRENT_PATH + "/inner_joint_Int.xlsx",
                                 sheet_name="inner_joint_Int" , index = "Unnamed: 0")



df['Altitude'] = df['Altitude'].astype(float)
df['Longitute'] = df['Longitute'].astype(float)
plt.show(df.plot(kind="scatter",
                                 x="Altitude",
                                 y="Longitute",
                                 s=df['Crash_count']*10, label ="Crash Count",figsize = (10,7),
                                 c="Crash_count", cmap=plt.get_cmap("jet"), colorbar=True,
                                 sharex=True,
                                 alpha=0.3))



