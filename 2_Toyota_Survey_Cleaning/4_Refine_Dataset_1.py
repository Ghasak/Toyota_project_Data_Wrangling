"""
=========================================================
          Refine the dataset- with configurations
            Tue Jun. 16th 2019
                 11:00:00,
=========================================================
    - The configurations of our Toyota City intersections
        Dataset is provided through finding the best way
        to combine all variables in our dataset
"""
# ==================================================#
#           Import Libraries
# ==================================================#
# Load the Pandas libraries with alias 'pd'
import pandas as pd
import numpy as np
import os
from Cleaning_tools_G import *
Current_Path = os.getcwd()
# ==================================================#
#              Import Dataset from Script
#           3_Creating_Dummies_continued.py
# ==================================================#
df = pd.read_excel(Current_Path + "/Toyota_Survey_Sheetfiles/3_Results_Creating_dummies_cont/Final_DataSet.xlsx",sheet_name="DataSet")

df.set_index(df['Unnamed: 0'], inplace = True)
#df.drop(df['Unnamed: 0'], inplace = True)
# ==================================================#
#       Remove intersections with duplicates
# ==================================================#
affected_intersection = []
'''
23-K05635-0001
23-K11839-0001
23-K15094-0001
23-K50523-0001
'''
for id, intersection in enumerate(df.index):
    #print(intersection)
    if len(intersection) > 13:
        print(intersection)
        affected_intersection.append(intersection)
print(10*"-","check the ss dataframe", 10*"-")
df.drop(index = affected_intersection,inplace = True)
# ==================================================#
#       Remove some repeated columns in your df
# ==================================================#
df.drop(columns = ['Unnamed: 0','Unnamed:_0'],inplace = True)
df.index.name = 'Intersection_ID'

# ==================================================#
#       Working on the combine variables at
#           each arms   -
# ==================================================#

# --------------------------------------------------
#         Road Type of each arm combination
# --------------------------------------------------

# Divided roadway with no physical median and no central strip
# Divied roadway with no physical median and with central strip
# Divided roadway with physical median and no central strip
# Divided roadway with physical median and with central strip
# One way street
# Single roadway without central strip
roadtype_list = [
'Arm1_RoadType_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip',
'Arm1_RoadType_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip',
'Arm1_RoadType_Divided_roadway_with_Physical_Median_and_No_Central_Strip',
'Arm1_RoadType_Divided_roadway_with_Physical_Median_and_with_Central_Strip',
'Arm1_RoadType_One_way_street',
'Arm1_RoadType_Single_roadway_without_central_strip',
# Second-arm
'Arm2_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip',
'Arm2_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip',
'Arm2_Divided_roadway_with_Physical_Median_and_No_Central_Strip',
'Arm2_Divided_roadway_with_Physical_Median_and_with_Central_Strip',
'Arm2_One_way_street',
'Arm2_Single_roadway_without_central_strip',
# Third-arm
'Arm3_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip',
'Arm3_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip',
'Arm3_Divided_roadway_with_Physical_Median_and_No_Central_Strip',
'Arm3_Divided_roadway_with_Physical_Median_and_with_Central_Strip',
'Arm3_One_way_street',
'Arm3_Single_roadway_without_central_strip',
# Fourth-arm
'Arm4_Road_type_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip',
'Arm4_Road_type_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip',
'Arm4_Road_type_Divided_roadway_with_Physical_Median_and_No_Central_Strip',
'Arm4_Road_type_Divided_roadway_with_Physical_Median_and_with_Central_Strip',
'Arm4_Road_type_Non_Existed',
'Arm4_Road_type_One_way_street',
'Arm4_Road_type_Single_roadway_without_central_strip',
# Fifth-arm
'Arm5_6_Road_type_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip_Single_roadway_without_central_strip',
'Arm5_6_Road_type_Non_Existed'
]
# Create a dictionary with len n-zeros
Road_type={}
for s in range(len(roadtype_list)):
     Road_type[roadtype_list[s]] = np.zeros(len(df.index))
# Create from the dictionary a dataframe in pandas
for index,item in enumerate((roadtype_list)):
    dfn = pd.DataFrame(Road_type,index = df.index)
# populate the dataframe with the columns you want from your original dataframe
for index,item in enumerate(dfn):
    dfn[item] = df[item]

# Now we will create a variables out of these set- using both regular method and query
# Regular method
mask0 = dfn[(df['Arm1_RoadType_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip'] ==1) | (dfn['Arm1_RoadType_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip']==1)]
# Query method
mask1 = dfn.query("(Arm1_RoadType_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip == 1) or (Arm1_RoadType_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip ==1 )")

# This method will git us same but through booleans variables same size to the dfn
mask_original = (dfn['Arm1_RoadType_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip']==1) | (dfn['Arm2_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip'] == 1) | (dfn['Arm3_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip']) | (dfn['Arm4_Road_type_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip'])
# Coverate the variable from boolean to binary
mask_original.astype(int)
# ==================================================#
#  Classify- Based on Divided or not Divided with
#               Central Division
# ==================================================#
# --------------------------------------------------
#     Road Type 1 Divided but no Central Division
# --------------------------------------------------
# Road type Divided but no Central Division
dfnroadtype1 = df[['Arm1_RoadType_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip','Arm2_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip','Arm3_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip','Arm4_Road_type_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip','Arm5_6_Road_type_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip_Single_roadway_without_central_strip']]
# Comprise the road type -Divided but no central division into one single variable
dfnroadtype1 =(df['Arm1_RoadType_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip'] == 1)|(df['Arm2_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip'] == 1) |(df['Arm3_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip'] == 1) |(df['Arm4_Road_type_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip'] ==1) |(df['Arm5_6_Road_type_Divided_roadway_with_No_Physical_Median_and_No_Central_Strip_Single_roadway_without_central_strip'] ==1)
DIVIDED_NO_CENTERAL_DIVISION = dfnroadtype1.astype(int)
# --------------------------------------------------
#     Road Type 2 Divided but with Central Division
# --------------------------------------------------
# Road type Divided with Central Division
# Arm1 -
dfnroadtype2_arm1 = df[['Arm1_RoadType_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip',
'Arm1_RoadType_Divided_roadway_with_Physical_Median_and_No_Central_Strip',
'Arm1_RoadType_Divided_roadway_with_Physical_Median_and_with_Central_Strip']]
# Arm2 -
dfnroadtype2_arm2 = df[['Arm2_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip',
'Arm2_Divided_roadway_with_Physical_Median_and_No_Central_Strip',
'Arm2_Divided_roadway_with_Physical_Median_and_with_Central_Strip']]
# Arm3 -
dfnroadtype2_arm3 = df[['Arm3_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip',
'Arm3_Divided_roadway_with_Physical_Median_and_No_Central_Strip',
'Arm3_Divided_roadway_with_Physical_Median_and_with_Central_Strip']]
# Arm4 -
dfnroadtype2_arm4 = df[['Arm4_Road_type_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip',
'Arm4_Road_type_Divided_roadway_with_Physical_Median_and_No_Central_Strip',
'Arm4_Road_type_Divided_roadway_with_Physical_Median_and_with_Central_Strip']]

# Comprise Road type 2 Divided with central division
# Arm1
dfnroadtype2_arm1 = (df['Arm1_RoadType_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip'] ==1)| (df['Arm1_RoadType_Divided_roadway_with_Physical_Median_and_No_Central_Strip']==1) |(df['Arm1_RoadType_Divided_roadway_with_Physical_Median_and_with_Central_Strip']==1)
dfnroadtype2_arm1 = dfnroadtype2_arm1.astype(int)
# Arm2
dfnroadtype2_arm2 = (df['Arm2_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip']) | (df['Arm2_Divided_roadway_with_Physical_Median_and_No_Central_Strip']) | (df['Arm2_Divided_roadway_with_Physical_Median_and_with_Central_Strip'])
dfnroadtype2_arm2 = dfnroadtype2_arm2.astype(int)
# Arm3
dfnroadtype2_arm3 = (df['Arm3_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip']) | (df['Arm3_Divided_roadway_with_Physical_Median_and_No_Central_Strip']) | (df['Arm3_Divided_roadway_with_Physical_Median_and_with_Central_Strip'])
dfnroadtype2_arm3 = dfnroadtype2_arm3.astype(int)
# Arm4
dfnroadtype2_arm4 = (df['Arm4_Road_type_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip']) | (df['Arm4_Road_type_Divided_roadway_with_Physical_Median_and_No_Central_Strip']) | (df['Arm4_Road_type_Divided_roadway_with_Physical_Median_and_with_Central_Strip'])
dfnroadtype2_arm4 = dfnroadtype2_arm4.astype(int)

# Now put them all in one virtual arm
dfnroadtype2 = (dfnroadtype2_arm1 == 1) | (dfnroadtype2_arm2 ==1) | (dfnroadtype2_arm3 ==1) | (dfnroadtype2_arm4 ==1)
DIVIDED_WITH_CENTRAL_DIVISION = dfnroadtype2.astype(int)
# --------------------------------------------------
#     Road Type 2 Divided but with Central Division
#           - based on physical median existence
# --------------------------------------------------
DIVIDED_NO_PHYSICAL_DIVISION = ((df['Arm1_RoadType_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip']==1) |
                              (df['Arm2_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip']==1)|
                              (df['Arm3_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip']==1)|
                              (df['Arm4_Road_type_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip']==1)).astype(int)
# --------------------------------------------------
x1 = (df['Arm1_RoadType_Divided_roadway_with_Physical_Median_and_with_Central_Strip'] ==1 ) | (df['Arm1_RoadType_Divided_roadway_with_Physical_Median_and_with_Central_Strip'] ==1 )
x2 = ((df['Arm2_Divided_roadway_with_Physical_Median_and_No_Central_Strip'] ==1 ) | (df['Arm2_Divided_roadway_with_Physical_Median_and_with_Central_Strip'] ==1 ))
x3 = ((df['Arm3_Divided_roadway_with_Physical_Median_and_No_Central_Strip'] ==1 ) | (df['Arm3_Divided_roadway_with_Physical_Median_and_with_Central_Strip'] ==1 ))
x4 = ((df['Arm4_Road_type_Divided_roadway_with_Physical_Median_and_No_Central_Strip'] ==1 ) | (df['Arm4_Road_type_Divided_roadway_with_Physical_Median_and_with_Central_Strip'] ==1 ))
# --------------------------------------------------
DIVIDED_WITH_PHYSICAL_DIVISION = ((x1)|(x2)|(x3)|(x4)).astype(int)
# --------------------------------------------------


# # Arm1
# x1 = df['Arm1_RoadType_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip']
# x2 =
# x2.name = "Arm1_divided_physical_median_existed"
# x2 = x2.astype(int)
# x1 = x1.to_frame()
# x2 = x2.to_frame()
# dfnroadtype2_arm1_2ndconf = x1.join(x2)

# # Arm2
# x1 = df['Arm2_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip']
# x2 =
# x2.name = "Arm2_divided_physical_median_existed"
# x2 = x2.astype(int)
# x1 = x1.to_frame()
# x2 = x2.to_frame()
# dfnroadtype2_arm2_2ndconf = x1.join(x2)
# # Arm3
# x1 = df['Arm3_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip']
# x2 =
# x2.name = "Arm3_divided_physical_median_existed"
# x2 = x2.astype(int)
# x1 = x1.to_frame()
# x2 = x2.to_frame()
# dfnroadtype2_arm3_2ndconf = x1.join(x2)
# # Arm4
# x1 = df['Arm4_Road_type_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip']
# x2 =
# x2.name = "Arm4_divided_physical_median_existed"
# x2 = x2.astype(int)
# x1 = x1.to_frame()
# x2 = x2.to_frame()
# dfnroadtype2_arm4_2ndconf = x1.join(x2)
# # ------------------------------------------------------------------
# dfnroadtype2_2ndconf = dfnroadtype2_arm1_2ndconf.join(dfnroadtype2_arm2_2ndconf).join(dfnroadtype2_arm3_2ndconf).join(dfnroadtype2_arm4_2ndconf)
# # Put variables all in one Virtual Arm
# dfnroadtype2_2ndconf_no_physical_median = (dfnroadtype2_2ndconf['Arm1_RoadType_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip']==1 ) |(dfnroadtype2_2ndconf['Arm2_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip']==1 ) |(dfnroadtype2_2ndconf['Arm3_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip']==1 ) |(dfnroadtype2_2ndconf['Arm4_Road_type_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip']==1 )
# dfnroadtype2_2ndconf_no_physical_median = x1.astype(int)
# # Comprise all physical Median
# dfnroadtype2_2ndconf_with_physical_median = (dfnroadtype2_2ndconf['']) | () | () | ()
# --------------------------------------------------
#     Road Type 2 Divided but with Central Division
# --------------------------------------------------




























# ==================================================#
#           Export the Final Results
# ==================================================#
printing = True
if printing == True:
    Final_DataSet = df.copy(deep = True)

    writer = pd.ExcelWriter(Current_Path + "/Toyota_Survey_Sheetfiles/4_Refine_Dataframe/refined_df.xlsx", engine='xlsxwriter')
    #store your dataframes in a  dict, where the key is the sheet name you want

    frames = {'DataSet': Final_DataSet, 'Descriptive': Final_DataSet.describe().T}
    #now loop thru and put each on a specific sheet
    for sheet, frame in  frames.items(): # .use .items for python 3.X, and .iteritems() fro 2.X
        frame.to_excel(writer, sheet_name = sheet)

    #critical last step
    writer.save()
