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
#       Road Type of each arm combination
# ==================================================#
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
DIVIDED_NO_CENTERAL_DIVISION.name = 'DIVIDED_NO_CENTERAL_DIVISION'
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
DIVIDED_WITH_CENTRAL_DIVISION.name = 'DIVIDED_WITH_CENTRAL_DIVISION'
# --------------------------------------------------
#     Road Type 2 Divided but with Central Division
#           - based on physical median existence
# --------------------------------------------------
DIVIDED_NO_PHYSICAL_DIVISION = ((df['Arm1_RoadType_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip']==1) |
                              (df['Arm2_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip']==1)|
                              (df['Arm3_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip']==1)|
                              (df['Arm4_Road_type_Divided_roadway_with_No_Physical_Median_and_with_Central_Strip']==1)).astype(int)
DIVIDED_NO_PHYSICAL_DIVISION.name = 'DIVIDED_NO_PHYSICAL_DIVISION'
# --------------------------------------------------
x1 = (df['Arm1_RoadType_Divided_roadway_with_Physical_Median_and_with_Central_Strip'] ==1 ) | (df['Arm1_RoadType_Divided_roadway_with_Physical_Median_and_with_Central_Strip'] ==1 )
x2 = ((df['Arm2_Divided_roadway_with_Physical_Median_and_No_Central_Strip'] ==1 ) | (df['Arm2_Divided_roadway_with_Physical_Median_and_with_Central_Strip'] ==1 ))
x3 = ((df['Arm3_Divided_roadway_with_Physical_Median_and_No_Central_Strip'] ==1 ) | (df['Arm3_Divided_roadway_with_Physical_Median_and_with_Central_Strip'] ==1 ))
x4 = ((df['Arm4_Road_type_Divided_roadway_with_Physical_Median_and_No_Central_Strip'] ==1 ) | (df['Arm4_Road_type_Divided_roadway_with_Physical_Median_and_with_Central_Strip'] ==1 ))
# --------------------------------------------------
DIVIDED_WITH_PHYSICAL_DIVISION = ((x1)|(x2)|(x3)|(x4)).astype(int)
DIVIDED_WITH_PHYSICAL_DIVISION.name = 'DIVIDED_WITH_PHYSICAL_DIVISION'
# --------------------------------------------------
#     Road Type 3 Combination of minor roads
# --------------------------------------------------

x1 = (df['Arm1_RoadType_One_way_street'] ==1)|(df['Arm1_RoadType_Single_roadway_without_central_strip']==1)
x2 = (df['Arm2_One_way_street']==1)|(df['Arm2_Single_roadway_without_central_strip']==1)
x3 = (df['Arm3_One_way_street']==1)|(df['Arm3_Single_roadway_without_central_strip']==1)
x4 = (df['Arm4_Road_type_One_way_street']==1) | (df['Arm4_Road_type_Single_roadway_without_central_strip']==1)
NON_DIVIDED_SINGLE_ROADWAY = ((x1)|(x2)|(x3)|(x4)).astype(int)
NON_DIVIDED_SINGLE_ROADWAY.name = 'NON_DIVIDED_SINGLE_ROADWAY'

# ==================================================#
#       Number of lanes combined all arms
# ==================================================#
NUMBER_OF_LANES = ((df['Arm1_Number_of_lanes_for_first_arm'])
                  +(df['Arm2_Number_of_lanes_for_second_arm'])
                  +(df['Arm3_Number_of_lanes_for_third_arm'])
                  +(df['Arm4_Number_of_lanes_for_fourth_arm'])
                  +(df['Arm5_6_Numer_of_lanes_larger_than_four'])).astype(int)
NUMBER_OF_LANES.name = 'NUMBER_OF_LANES'
# ==================================================#
#       Lane changing
# ==================================================#
# at least one of the lanes has changed at the approach
NO_OF_LANES_CHANGED = ((df['Arm1_No_of_lanes_changed_at_the_approach']==1)|
                       (df['Arm2_No_of_lanes_changed_at_the_approach1']==1)|
                       (df['Arm3_No_of_lanes_changed_at_the_approach2']==1)|
                       (df['Arm4_No_of_lanes_changed_at_the_approach3']==1)|
                       (df['Arm5_6_No_of_lanes_changed_larger_than_four']==1)).astype(int)
NO_OF_LANES_CHANGED.name = 'NO_OF_LANES_CHANGED'

# ==================================================#
#       Left Turn Exclusive lane
# ==================================================#
LEFT_TURN_EXCLUSIVE_LANE = ((df['Left_turn_only_lane_for_first_arm']==1)|
                           (df['Left_turn_only_lane_for_second_arm']==1)|
                           (df['Left_turn_only_lane_for_third_arm']==1)|
                           (df['Left_turn_only_lane_for_fourth_arm']==1)|
                           (df['Left_turn_only_lane_larger_than_four']==1)).astype(int)

LEFT_TURN_EXCLUSIVE_LANE.name = 'LEFT_TURN_EXCLUSIVE_LANE'

# ==================================================#
#       Right Turn Exclusive lane
# ==================================================#
RIGHT_TURN_EXCLUSIVE_LANE = ((df['Right_turn_only_lane_for_first_arm']==1)|
                             (df['Right_turn_only_lane_for_second_arm']==1)|
                             (df['Right_turn_only_lane_for_third_arm']==1)|
                             (df['Right_turn_only_lane_for_fourth_arm']==1)|
                             (df['Right_turn_only_lane_larger_than_four']==1)).astype(int)

RIGHT_TURN_EXCLUSIVE_LANE.name = 'RIGHT_TURN_EXCLUSIVE_LANE'

# ==================================================#
#       Width of central strip
# ==================================================#
# Here we have two variables one is the measure itself and
# one is the dummy of existence of the central strip itself.
# Arm1
AVERAGE_WIDTH_PHYSICAL_MEDIAN =()
MIN_WIDTH_PHYSICAL_MEDIAN
MAX_WIDTH_PHYSICAL_MEDIAN
Width_of_Pysical_Median_of_first_arm_if_exist
Is_there_Physical_Median_first_arm
# Arm2
Width_of_Pysical_Median_of_second_arm_if_exist
Is_there_Physical_Median_second_arm
# Arm3
Width_of_Pysical_Median_of_third_arm_if_exist
Is_there_Physical_Median_third_arm
# Arm4
Width_of_Pysical_Median_of_fourth_arm_if_exist
Is_there_Physical_Median_fourth_arm
# Larger than 4 arms
Width_of_Physical_Median_larger_than_four
Is_there_Physical_Median_five_arm


# ==================================================#
#           Constructing Our DATASET
# ==================================================#
# Adding Road types
df = df.join(DIVIDED_NO_CENTERAL_DIVISION).join(DIVIDED_WITH_CENTRAL_DIVISION).join(DIVIDED_NO_PHYSICAL_DIVISION).join(DIVIDED_WITH_PHYSICAL_DIVISION).join(NON_DIVIDED_SINGLE_ROADWAY)
# Adding Number of lanes
df = df.join(NUMBER_OF_LANES)
# Adding Lanes changing
df = df.join(NO_OF_LANES_CHANGED)
# Adding the left turn exclusive lane
df = df.join(LEFT_TURN_EXCLUSIVE_LANE)
# Adding the right turn exclusive lane
df = df.joint(RIGHT_TURN_EXCLUSIVE_LANE)








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
