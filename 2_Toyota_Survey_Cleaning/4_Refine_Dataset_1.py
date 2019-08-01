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
DIVIDED_NO_CENTRAL_DIVISION = dfnroadtype1.astype(int)
DIVIDED_NO_CENTRAL_DIVISION.name = 'DIVIDED_NO_CENTRAL_DIVISION'
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
physical_median_width_df = df[['Width_of_Pysical_Median_of_first_arm_if_exist',
                               'Width_of_Pysical_Median_of_second_arm_if_exist',
                               'Width_of_Pysical_Median_of_third_arm_if_exist',
                               'Width_of_Pysical_Median_of_fourth_arm_if_exist',
                               'Width_of_Physical_Median_larger_than_four']]
checking_intersection_type = df[['Three_arms','Four_arms','Five_arms','Six_arms']]

sum_width_physical_median = []
maximum_width_physical_median = []
minimum_width_physcial_median = []
for index in range(len(physical_median_width_df)):
    sum_width_physical_median.append(physical_median_width_df.iloc[index,:].sum())
    maximum_width_physical_median.append(physical_median_width_df.iloc[index,:].max())
    minimum_width_physcial_median.append(physical_median_width_df[physical_median_width_df > 0].iloc[index,:].min())
# Now we will construct our Pandas Series from the list we created
sum_width_physical_median     = pd.Series(sum_width_physical_median,index = df.index, name = 'SUM_OF_PHYSICAL_MEDIAN')
maximum_width_physical_median = pd.Series(maximum_width_physical_median,index = df.index, name = 'MAXIMUM_WIDTH_PHYSICAL_MEDIAN')
minimum_width_physcial_median = pd.Series(minimum_width_physcial_median, index = df.index,name = 'MINIMUM_WIDTH_PHYSICAL_MEIDAN')
# Now we will convert it to a dataframe as
sum_width_physical_median     = pd.DataFrame(sum_width_physical_median)
maximum_width_physical_median = pd.DataFrame(maximum_width_physical_median)
minimum_width_physcial_median = pd.DataFrame(minimum_width_physcial_median)
# Now we will divide the sum based on number of arms for each intersection
average_width_physical_median = []

for index in range(len(df)):

    if  checking_intersection_type['Three_arms'].iloc[index]==1 :
        print(f"the intersection of three arms is = {sum_width_physical_median.index[index]}")
        average_width_physical_median.append(sum_width_physical_median['SUM_OF_PHYSICAL_MEDIAN'][index]/3.0)

    elif checking_intersection_type['Four_arms'].iloc[index] ==1 :
        print(f"the intersection of four arms is = {sum_width_physical_median.index[index]}")
        average_width_physical_median.append(sum_width_physical_median['SUM_OF_PHYSICAL_MEDIAN'][index]/4.0)

    elif checking_intersection_type['Five_arms'].iloc[index]==1 :
        print(f"the intersection of five arms is = {sum_width_physical_median.index[index]}")
        average_width_physical_median.append(sum_width_physical_median['SUM_OF_PHYSICAL_MEDIAN'][index]/5.0)

    elif checking_intersection_type['Six_arms'].iloc[index] == 1:
        print(f"the intersection of six arms is = {sum_width_physical_median.index[index]}")
        average_width_physical_median.append(sum_width_physical_median['SUM_OF_PHYSICAL_MEDIAN'][index]/6.0)

average_width_physical_median = pd.Series(average_width_physical_median, index = df.index, name = "AVERAGE_WIDTH_PHYSICAL_MEDIAN")
average_width_physical_median = pd.DataFrame(average_width_physical_median)

SUM_MAX_MIN_AVERAGE_WIDTH_PHYSICAL_MEDIAN = sum_width_physical_median.join(maximum_width_physical_median).join(minimum_width_physcial_median).join(average_width_physical_median)
SUM_MAX_MIN_AVERAGE_WIDTH_PHYSICAL_MEDIAN.fillna(0,inplace = True)
# --------------------------------------------------
#     Now we add the dummy of physical median
# --------------------------------------------------
IS_THERE_PHYSICAL_MEDIAN = ((df['Is_there_Physical_Median_first_arm']==1)|
                            (df['Is_there_Physical_Median_second_arm']==1)|
                            (df['Is_there_Physical_Median_third_arm']==1)|
                            (df['Is_there_Physical_Median_fourth_arm']==1)|
                            (df['Is_there_Physical_Median_five_arm']==1)).astype(int)

IS_THERE_PHYSICAL_MEDIAN.name = 'IS_THERE_PHYSICAL_MEDIAN'
# ==================================================#
#              Width of Central Strip:
# ==================================================#

width_central_strip_df = df[['Width_of_central_strip_of_first_arm_if_exist',
                             'Width_of_central_strip_of_second_arm_if_exist',
                             'Width_of_central_strip_of_third_arm_if_exist',
                             'Width_of_central_strip_of_fourth_arm_if_exist',
                             ]]

'''
    - [2019 Wed. Jul 24], I have found that there is a typo in the
        (width_central_strip_df),could not convert string to float: '2,.99'
        this typo comes when i tried to go into the loop down
        I found the typo by trying to convert the (width_central_strip_df)
        to an (float) using the command (width_central_strip_df.astype(float))
    - Quick solution, I have changed '2,.99' in the original dataframe
'''
# -----------------------------------------------------------------
# Starting checking column-by-column in our df related to width of central strip
# First detect our column with the problem
for index,item in enumerate(width_central_strip_df['Width_of_central_strip_of_first_arm_if_exist']):
    if item == '2,.99':
        print(width_central_strip_df.index[index])
# Second-create function to correct the error
def is_string(x):
    if x == '2,.99':
        x = 2.99
    return(x)
# Correct Master Dataframe
df['Width_of_central_strip_of_first_arm_if_exist'] = df['Width_of_central_strip_of_first_arm_if_exist'].apply(is_string)
# Assign the new value using apply()
width_central_strip_df['Width_of_central_strip_of_first_arm_if_exist'] = width_central_strip_df['Width_of_central_strip_of_first_arm_if_exist'].apply(is_string)

# -----------------------------------------------------------------

sum_width_central_strip = []
max_width_central_strip = []
min_width_central_strip = []

for index in range(len(width_central_strip_df)):
    sum_width_central_strip.append(width_central_strip_df.iloc[index,:].sum())
    max_width_central_strip.append(width_central_strip_df.iloc[index,:].max())
    min_width_central_strip.append(width_central_strip_df[width_central_strip_df > 0].iloc[index,:].min())


# Now we will construct our Pandas Series from the lists we created
sum_width_central_strip = pd.Series(sum_width_central_strip,index = df.index, name = 'SUM_WIDTH_CENTRAL_STRIP')
max_width_central_strip = pd.Series(max_width_central_strip,index = df.index, name = 'MAX_WIDTH_CENTRAL_STRIP')
min_width_central_strip = pd.Series(min_width_central_strip,index = df.index, name = 'MIN_WIDTH_CENTRAL_STRIP')

# Now we will convert it to a dataframe as
sum_width_central_strip = pd.DataFrame(sum_width_central_strip)
max_width_central_strip = pd.DataFrame(max_width_central_strip)
min_width_central_strip = pd.DataFrame(min_width_central_strip)


# Now we will divide the sum based on number of arms for each intersection
average_width_central_strip = []

for index in range(len(df)):

    if  checking_intersection_type['Three_arms'].iloc[index]==1 :
        print(f"the intersection of three arms is = {sum_width_central_strip.index[index]}")
        average_width_central_strip.append(sum_width_central_strip['SUM_WIDTH_CENTRAL_STRIP'][index]/3.0)

    elif checking_intersection_type['Four_arms'].iloc[index] ==1 :
        print(f"the intersection of four arms is = {sum_width_central_strip.index[index]}")
        average_width_central_strip.append(sum_width_central_strip['SUM_WIDTH_CENTRAL_STRIP'][index]/4.0)

    elif checking_intersection_type['Five_arms'].iloc[index]==1 :
        print(f"the intersection of five arms is = {sum_width_central_strip.index[index]}")
        average_width_central_strip.append(sum_width_central_strip['SUM_WIDTH_CENTRAL_STRIP'][index]/5.0)

    elif checking_intersection_type['Six_arms'].iloc[index] == 1:
        print(f"the intersection of six arms is = {sum_width_central_strip.index[index]}")
        average_width_central_strip.append(sum_width_central_strip['SUM_WIDTH_CENTRAL_STRIP'][index]/6.0)

average_width_central_strip = pd.Series(average_width_central_strip, index = df.index, name = "AVERAGE_WIDTH_CENTRAL_STRIP")
average_width_central_strip = pd.DataFrame(average_width_central_strip)

SUM_MAX_MIN_AVERAGE_WIDTH_CENTRAL_STRIP = sum_width_central_strip.join(max_width_central_strip).join(min_width_central_strip).join(average_width_central_strip)
SUM_MAX_MIN_AVERAGE_WIDTH_CENTRAL_STRIP.fillna(0, inplace = True)
# --------------------------------------------------
#  Now we add the dummy of central strip existence
# --------------------------------------------------
IS_THERE_CENTRAL_STRIP = ((df['Is_there_centeral_strip_first_arm']==1) |
                          (df['Is_there_centeral_strip_second_arm']==1)|
                          (df['Is_there_centeral_strip_third_arm']==1) |
                          (df['Is_there_centeral_strip_fourth_arm']==1)|
                          (df['Is_there_centeral_strip_five_arm']==1)).astype(int)

IS_THERE_CENTRAL_STRIP.name = 'IS_THERE_CENTRAL_STRIP'

# ==================================================#
#                 Skewness_level
# ==================================================#
IS_THERE_SKEWNESS = ((df['Skewness_level_of_first_arm_to_the_next_arm']  == 1) |
                     (df['Skewness_level_of_second_arm_to_the_next_arm'] == 1) |
                     (df['Skewness_level_of_third_arm_to_the_next_arm']  == 1) |
                     (df['Skewness_level_of_fourth_arm_to_the_next_arm'] == 1) |
                     (df['Skewness_level_larger_than_four']) == 1).astype(int)
IS_THERE_SKEWNESS.name = 'IS_THERE_SKEWNESS'

# ==================================================#
#                 Traffic Signal Variable
# ==================================================#
# create a min-df for each variable

# Flashing red/yellow variable
red_yellow_flashing_signal = df[['Arm1_Red/Yellow_flashing_signal',
                                 'Arm2_Red/Yellow_flashing_signal',
                                 'Arm3_Red/Yellow_flashing_signal',
                                 'Arm4_TrafSig_Red/Yellow_flashing_signal']]

# Stop sign of controlled intersection
stop_sign = df[['Arm1_Stop_sign',
                'Arm2_Stop_sign',
                'Arm3_Stop_sign',
                'Arm4_TrafSig_Stop_sign']]

# Signal types - high level means right/left exclusive is available
high_level_signal = df[['Arm1_Traffic_signal_with_left_or_right_turn_only',
                        'Arm2_Traffic_signal_with_left_or_right_turn_only',
                        'Arm3_Traffic_signal_with_left_or_right_turn_only',
                        'Arm4_TrafSig_Traffic_signal_with_left_or_right_turn_only']]

# Single types - regular type red-yellow-green
regular_signal = df[['Arm1_Traffic_signal_without_left_or_right_turn_only',
                     'Arm2_Traffic_signal_without_left_or_right_turn_only',
                     'Arm3_Traffic_signal_without_left_or_right_turn_only',
                     'Arm4_TrafSig_Traffic_signal_without_left_or_right_turn_only']]

# Uncontrolled intersection - Non Signalized intersection
uncontrolled_intersection = df[['Arm1_Uncontroled',
                                'Arm2_Uncontroled',
                                'Arm3_Uncontroled',
                                'Arm4_TrafSig_Uncontroled',
                                'Arm5_6_TrafSig_UncontroledStop_sign']]

# Intersection with pedestrain flashing green signal

flashing_green_pedestrain = df[['Arm1_Presence_of_pedestrian_traffic_signal',
                                'Arm2_Presence_of_pedestrian_traffic_signal1',
                                'Arm3_Presence_of_pedestrian_traffic_signal2',
                                'Arm4_Presence_of_pedestrian_traffic_signal3',
                                'Arm5_6_Presence_of_pedestrian_traffic_signal_larger_than_four']]
# -------------------------------------------------------
# Uncontrolled intersection - Non Signalized intersection
# -------------------------------------------------------
# At least one of the approaches has uncotrolled feature
IT_UNCONTROLLED_INT =  ((uncontrolled_intersection['Arm1_Uncontroled'] == 1) |
                        (uncontrolled_intersection['Arm1_Uncontroled'] == 1) |
                        (uncontrolled_intersection['Arm2_Uncontroled'] == 1) |
                        (uncontrolled_intersection['Arm3_Uncontroled'] == 1) |
                        (uncontrolled_intersection['Arm4_TrafSig_Uncontroled'] == 1)|
                        (uncontrolled_intersection['Arm5_6_TrafSig_UncontroledStop_sign'] == 1)).astype(int)
IT_UNCONTROLLED_INT.name = 'IT_UNCONTROLLED_INT'

a = uncontrolled_intersection['Arm1_Uncontroled']
b = uncontrolled_intersection['Arm1_Uncontroled']
c = uncontrolled_intersection['Arm2_Uncontroled']
d = uncontrolled_intersection['Arm3_Uncontroled']
e = uncontrolled_intersection['Arm4_TrafSig_Uncontroled']
f = uncontrolled_intersection['Arm5_6_TrafSig_UncontroledStop_sign']

# from from itertools import combinations  ;list(combinations(['a','b','c','d','e','f'],2))
# if there are at least two approaches with uncontrolled feature
IT_IS_UNCONTROLLED_TWO_AT_LEAST =   ((a & b) |
                                     (a & c) |
                                     (a & d) |
                                     (a & e) |
                                     (a & f) |
                                     (b & c) |
                                     (b & d) |
                                     (b & e) |
                                     (b & f) |
                                     (c & d) |
                                     (c & e) |
                                     (c & f) |
                                     (d & e) |
                                     (d & f) |
                                     (e & f)).astype(int)
IT_IS_UNCONTROLLED_TWO_AT_LEAST.name = 'IT_IS_UNCONTROLLED_TWO_AT_LEAST'
# -------------------------------------------------------
#           Stop sign of controlled intersection
# -------------------------------------------------------
STOP_SIGN = ((df['Arm1_Stop_sign'] ==1) |
             (df['Arm2_Stop_sign'] ==1) |
             (df['Arm3_Stop_sign'] ==1) |
             (df['Arm4_TrafSig_Stop_sign'] ==1) ).astype(int)

STOP_SIGN.name = 'STOP_SIGN'
# -------------------------------------------------------
#       Does the intersection is signalized or not
# -------------------------------------------------------

IT_IS_NON_SIGNALIZED = ((IT_IS_UNCONTROLLED_TWO_AT_LEAST == 1) | (STOP_SIGN ==1)).astype(int)

IT_IS_NON_SIGNALIZED.name = 'IT_IS_NON_SIGNALIZED'
# -------------------------------------------------------
#                   Signal types
# -------------------------------------------------------
# - Signal types - high level means right/left exclusive is available
# It will be considered a signalized with high-level if there two and
# only two approaches labeled with right/left exclusive signal.
a = df['Arm1_Traffic_signal_with_left_or_right_turn_only']
b = df['Arm2_Traffic_signal_with_left_or_right_turn_only']
c = df['Arm3_Traffic_signal_with_left_or_right_turn_only']
d = df['Arm4_TrafSig_Traffic_signal_with_left_or_right_turn_only']

SIGNALIZED_HIGH_LEVEL_SIGNAL = ((a & b) |
                                (a & c) |
                                (a & d) |
                                (b & c) |
                                (b & d) |
                                (c & d) ).astype(int)

SIGNALIZED_HIGH_LEVEL_SIGNAL.name = 'SIGNALIZED_HIGH_LEVEL_SIGNAL'
# ------------------------------------------------------------------
# -Single types - regular type red-yellow-green
a = df['Arm1_Traffic_signal_without_left_or_right_turn_only']
b = df['Arm2_Traffic_signal_without_left_or_right_turn_only']
c = df['Arm3_Traffic_signal_without_left_or_right_turn_only']
d = df['Arm4_TrafSig_Traffic_signal_without_left_or_right_turn_only']


SIGNALIZED_REGULAR_SIGNAL=((a & b & c) |
                           (a & b & d) |
                           (a & c & d) |
                           (b & c & d)).astype(int)
SIGNALIZED_REGULAR_SIGNAL.name = 'SIGNALIZED_REGULAR_SIGNAL'
# Maybe can be optimized later - suggestion is to consider number of arms and use (&)
# is_it_sigalized_regular = []
SIGNALIZED_REGULAR_SIGNAL_2 = pd.Series(np.zeros(len(df)), name = "SIGNALIZED_REGULAR_SIGNAL_2",index = df.index)
for index in range(len(df)):
    if  checking_intersection_type['Three_arms'].iloc[index]==1 :
        #print(f"the intersection of three arms is = {sum_width_central_strip.index[index]}")
        if (a[index]  & b[index] & c[index]).astype(int):
            SIGNALIZED_REGULAR_SIGNAL_2[index] = ((a[index]  & b[index] & c[index]).astype(int))

    elif checking_intersection_type['Four_arms'].iloc[index] ==1 :
        #print(f"the intersection of four arms is = {sum_width_central_strip.index[index]}")
        if (a[index]  & b[index] & c[index] & d[index]).astype(int):
            SIGNALIZED_REGULAR_SIGNAL_2[index] = ((a[index]  & b[index] & c[index] & d[index]).astype(int))

    elif checking_intersection_type['Five_arms'].iloc[index]==1 :
        #print(f"the intersection of five arms is = {sum_width_central_strip.index[index]}")
        if (a[index]  & b[index] & c[index] & d[index] ).astype(int):
            SIGNALIZED_REGULAR_SIGNAL_2[index] = (a[index]  & b[index] & c[index] ).astype(int)

    elif checking_intersection_type['Six_arms'].iloc[index] == 1:
        #print(f"the intersection of six arms is = {sum_width_central_strip.index[index]}")
        if (a[index]  & b[index] & c[index] & d[index]).astype(int):
            SIGNALIZED_REGULAR_SIGNAL_2[index] = (a[index]  & b[index] & c[index] ).astype(int)

SIGNALIZED_REGULAR_SIGNAL_2 = SIGNALIZED_REGULAR_SIGNAL_2.to_frame()
SIGNALIZED_REGULAR_SIGNAL_2.name = 'SIGNALIZED_REGULAR_SIGNAL_2'

# -------------------------------------------------------
#          Other Traffic Signales Configurations
# -------------------------------------------------------
'''
    - After a quick discussion over the best way to find best
        configuration to the model set I have set the signalized
        variable. Now we have: signalized with regular, high-level
        and others
'''

OTHERS1 =((df['Arm1_Red/Yellow_flashing_signal'] == 1) |
          (df['Arm2_Red/Yellow_flashing_signal'] == 1) |
          (df['Arm3_Red/Yellow_flashing_signal'] == 1) |
          (df['Arm4_TrafSig_Red/Yellow_flashing_signal'] == 1))

OTHERS2 =((df['Arm1_Stop_sign'] == 1) |
          (df['Arm2_Stop_sign'] == 1) |
          (df['Arm3_Stop_sign'] == 1) |
          (df['Arm4_TrafSig_Stop_sign'] == 1))

OTHERS3 = ((df['Arm1_Uncontroled'] == 1) |
           (df['Arm2_Uncontroled'] ==1) |
           (df['Arm3_Uncontroled'] ==1) |
           (df['Arm4_TrafSig_Uncontroled'] ==1) |
           (df['Arm5_6_TrafSig_UncontroledStop_sign'] ==1) )

OTHERS = (OTHERS1 | OTHERS2 | OTHERS3).astype(int)
OTHERS.name = 'OTHERS_SIGNALS'

# -------------------------------------------------------
#                Flashing Green Signales
# -------------------------------------------------------
FLASHING_GREEN_PED = ((df['Arm1_Presence_of_pedestrian_traffic_signal']  == 1) |
                      (df['Arm2_Presence_of_pedestrian_traffic_signal1'] == 1) |
                      (df['Arm3_Presence_of_pedestrian_traffic_signal2'] == 1) |
                      (df['Arm4_Presence_of_pedestrian_traffic_signal3'] == 1) |
                      (df['Arm5_6_Presence_of_pedestrian_traffic_signal_larger_than_four'] == 1)).astype(int)
FLASHING_GREEN_PED.name = 'FLASHING_GREEN_PED'

# ==================================================#
#          Intersection Radius in (meter)
# ==================================================#
radius_intersection_df = df[['Radius_of_arm_1_and_arm_2_',
                             'Radius_of_arm_2_and_arm_3_',
                             'Radius_of_arm_3_and_arm_4_',
                             'Radius_of_arm_4_and_arm_5_',
                             'Radius_of_arm_5_and_arm_6_',
                             'Radius_of_arm_6_and_arm_7_']]
# -----------------------------------------------------
# found a problem with one of the records of our dataframe:
# it seems one of the records has a string not a number
# -----------------------------------------------------
for index, item in enumerate(radius_intersection_df['Radius_of_arm_3_and_arm_4_']):
    if item == '３１，３１':
        print(radius_intersection_df.index[index])
# The problem is located with intersection "23-K06576-000"
# Now we will use the following idea:
        # change  the master dataframe
        #df['Radius_of_arm_3_and_arm_4_'].iloc[index] = 31.31
        radius_intersection_df['Radius_of_arm_3_and_arm_4_'].iloc[index] = 31.31
        df['Radius_of_arm_3_and_arm_4_'].iloc[index] = 31.31

radius_intersection_df['Radius_of_arm_3_and_arm_4_'] = radius_intersection_df['Radius_of_arm_3_and_arm_4_'].astype(float)
df['Radius_of_arm_3_and_arm_4_'] = df['Radius_of_arm_3_and_arm_4_'].astype(float)
# # You can also use the following idea:
# # Second-create function to correct the error
# def is_string2(x):
#     if x == '３１，３１':
#         x = 2.99
#     return(x)
# # Correct Master Dataframe
# df['Radius_of_arm_3_and_arm_4_'] = df['Radius_of_arm_3_and_arm_4_'].apply(is_string2)
# # Assign the new value using apply()
# radius_intersection_df['Radius_of_arm_3_and_arm_4_'] = radius_intersection_df['Width_of_central_strip_of_first_arm_if_exist'].apply(is_string2)
# -----------------------------------------------------

# One of the records is so big in the maximum radius which is (141.63)
# The real radius is (14.63 m) - We will adjust this one here:
for index, item in enumerate(df['Radius_of_arm_3_and_arm_4_']):
    if item == 141.63:
        df['Radius_of_arm_3_and_arm_4_'].iloc[index] = 14.63
        radius_intersection_df['Radius_of_arm_3_and_arm_4_'].iloc[index] = 14.63
#
# Radius_of_arm_2_and_arm_3_ = 141.63 ----> 14.63 m instead
for index, item in enumerate(df['Radius_of_arm_2_and_arm_3_']):
    if item == 141.63:
        df['Radius_of_arm_2_and_arm_3_'].iloc[index] = 14.63
        radius_intersection_df['Radius_of_arm_2_and_arm_3_'].iloc[index] = 14.63
    elif item == 104.52:
        df['Radius_of_arm_2_and_arm_3_'].iloc[index] = 14.52
        radius_intersection_df['Radius_of_arm_2_and_arm_3_'].iloc[index] = 14.63

# -----------------------------------------------------
sum_radius = []
max_radius = []
min_radius = []

for index in range(len(radius_intersection_df)):
    sum_radius.append(radius_intersection_df.iloc[index,:].sum())
    max_radius.append(radius_intersection_df.iloc[index,:].max())
    # We will get the smallest radius but not zero
    min_radius.append(radius_intersection_df[radius_intersection_df > 0].iloc[index,:].min())

# To check the smallest radius but not zero simply use:
for row in radius_intersection_df.iloc[0,:]:
    print(row)

sum_radius = pd.Series(sum_radius,index = df.index, name = 'SUM_RADIUS')
max_radius = pd.Series(max_radius,index = df.index, name = 'MAX_RADIUS')
min_radius = pd.Series(min_radius,index = df.index, name = 'MIN_RADIUS')

# Now we will convert it to a dataframe as
sum_radius = pd.DataFrame(sum_radius)
max_radius = pd.DataFrame(max_radius)
min_radius = pd.DataFrame(min_radius)
# Now we will divide the sum based on number of arms for each intersection
average_radius = []

for index in range(len(df)):

    if  checking_intersection_type['Three_arms'].iloc[index]==1 :
        print(f"the intersection of three arms is = {sum_radius.index[index]}")
        average_radius.append(sum_radius['SUM_RADIUS'][index]/3.0)

    elif checking_intersection_type['Four_arms'].iloc[index] ==1 :
        print(f"the intersection of four arms is = {sum_radius.index[index]}")
        average_radius.append(sum_radius['SUM_RADIUS'][index]/4.0)

    elif checking_intersection_type['Five_arms'].iloc[index]==1 :
        print(f"the intersection of five arms is = {sum_radius.index[index]}")
        average_radius.append(sum_radius['SUM_RADIUS'][index]/5.0)

    elif checking_intersection_type['Six_arms'].iloc[index] == 1:
        print(f"the intersection of six arms is = {sum_radius.index[index]}")
        average_radius.append(sum_radius['SUM_RADIUS'][index]/6.0)

average_radius = pd.Series(average_radius, index = df.index, name = "AVERAGE_RADIUS")
average_radius = pd.DataFrame(average_radius)

SUM_MAX_MIN_AVERAGE_RADIUS = sum_radius.join(max_radius).join(min_radius).join(average_radius)
# ==================================================#
#          Intersection Type Variables
# ==================================================#
intersection_type = df[['Cross_intersection',
                        'Intersection_with_more_than_four_arms',
                        'Other_shapes',
                        'T_or_staggered_intersection',
                        'Y_shape_intersection']]

intersection_type['Other_shapes2'] = ((intersection_type['Other_shapes'] ==1) | (intersection_type['Intersection_with_more_than_four_arms'] ==1)).astype(int)
INTERSECTION_TYPE_OTHERS = intersection_type['Other_shapes2']
INTERSECTION_TYPE_OTHERS.name = 'INTERSECTION_TYPE_OTHERS'

# ==================================================#
#     Take Log and Adjust some Exposure Variables
# ==================================================#
# ------------------------------------------------------
#               No of driveways -cardinal no.
# ------------------------------------------------------
LOG_NO_DRIVE_WAYS        = np.log(df['Number_of_driverways'].mask(df['Number_of_driverways'] <=0)).fillna(0)
LOG_NO_DRIVE_WAYS.name   = 'LOG_NO_DRIVE_WAYS'
# ------------------------------------------------------
#               Distance to adjacent intersection
# ------------------------------------------------------
LOG_DISTANCE_TO_ADJUST      = np.log(df['Distance_to_adjacent_intersection_within_500_meter'].mask(df['Distance_to_adjacent_intersection_within_500_meter'] <=0)).fillna(0)

LOG_DISTANCE_TO_ADJUST.name = 'LOG_DISTANCE_TO_ADJUST'
# ------------------------------------------------------
#               Longest width of intersection
# ------------------------------------------------------
LOG_LONGEST_WIDTH_INTER      = np.log(df['Longest_Width_of_intersection'].mask(df['Longest_Width_of_intersection'] <=0)).fillna(0)
LOG_LONGEST_WIDTH_INTER.name = 'LOG_LONGEST_WIDTH_INTER'
# ------------------------------------------------------
#               Shortest width of intersection
# ------------------------------------------------------
LOG_SHORTEST_WIDTH_INTER      = np.log(df['Shortest_Width_of_intersection'].mask(df['Shortest_Width_of_intersection'] <=0)).fillna(0)
LOG_SHORTEST_WIDTH_INTER.name = 'LOG_SHORTEST_WIDTH_INTER'
# ------------------------------------------------------
#               Radius of intersection
# ------------------------------------------------------
LOG_MAX_RADIUS = np.log(SUM_MAX_MIN_AVERAGE_RADIUS['MAX_RADIUS'].mask(SUM_MAX_MIN_AVERAGE_RADIUS['MAX_RADIUS'] <=0)).fillna(0)
LOG_MAX_RADIUS.name ='LOG_MAX_RADIUS'

LOG_MIN_RADIUS = np.log(SUM_MAX_MIN_AVERAGE_RADIUS['MIN_RADIUS'].mask(SUM_MAX_MIN_AVERAGE_RADIUS['MIN_RADIUS'] <=0)).fillna(0)
LOG_MIN_RADIUS.name = 'LOG_MIN_RADIUS'
LOG_MIN_RADIUS = LOG_MIN_RADIUS.mask(LOG_MIN_RADIUS <= 0).fillna(0)

LOG_AVERAGE_RADIUS = np.log(SUM_MAX_MIN_AVERAGE_RADIUS['AVERAGE_RADIUS'].mask(SUM_MAX_MIN_AVERAGE_RADIUS['AVERAGE_RADIUS'] <=0)).fillna(0)

LOG_AVERAGE_RADIUS.name = 'LOG_AVERAGE_RADIUS'
# ------------------------------------------------------
#                   Number of lanes
# ------------------------------------------------------
LOG_NUMBER_OF_LANES = np.log(NUMBER_OF_LANES.mask(NUMBER_OF_LANES <=0)).fillna(0)
LOG_NUMBER_OF_LANES.name = 'LOG_NUMBER_OF_LANES'
# ------------------------------------------------------
#           Physical width in (meter) - log
# ------------------------------------------------------
LOG_MAX_WIDTH_PHYSICAL_MEDIAN = np.log(SUM_MAX_MIN_AVERAGE_WIDTH_PHYSICAL_MEDIAN['MAXIMUM_WIDTH_PHYSICAL_MEDIAN'].mask(SUM_MAX_MIN_AVERAGE_WIDTH_PHYSICAL_MEDIAN['MAXIMUM_WIDTH_PHYSICAL_MEDIAN'] <=0)).fillna(0)
LOG_MAX_WIDTH_PHYSICAL_MEDIAN.name = 'LOG_MAX_WIDTH_PHYSICAL_MEDIAN'
LOG_MAX_WIDTH_PHYSICAL_MEDIAN = LOG_MAX_WIDTH_PHYSICAL_MEDIAN.mask(LOG_MAX_WIDTH_PHYSICAL_MEDIAN <= 0).fillna(0)   # To get rid of the small values of log(0.0000e)
# ------------------------------------------------------
LOG_MIN_WIDTH_PHYSICAL_MEDIAN = np.log(SUM_MAX_MIN_AVERAGE_WIDTH_PHYSICAL_MEDIAN['MINIMUM_WIDTH_PHYSICAL_MEIDAN'].mask(SUM_MAX_MIN_AVERAGE_WIDTH_PHYSICAL_MEDIAN['MINIMUM_WIDTH_PHYSICAL_MEIDAN'] <=0)).fillna(0)
LOG_MIN_WIDTH_PHYSICAL_MEDIAN.name = 'LOG_MIN_WIDTH_PHYSICAL_MEDIAN'
LOG_MIN_WIDTH_PHYSICAL_MEDIAN = LOG_MIN_WIDTH_PHYSICAL_MEDIAN.mask(LOG_MIN_WIDTH_PHYSICAL_MEDIAN <= 0).fillna(0)   # To get rid of the small values of log(0.0000e)
# ------------------------------------------------------
LOG_AVERAGE_WIDTH_PHYSICAL_MEDIAN = np.log(SUM_MAX_MIN_AVERAGE_WIDTH_PHYSICAL_MEDIAN['AVERAGE_WIDTH_PHYSICAL_MEDIAN'].mask(SUM_MAX_MIN_AVERAGE_WIDTH_PHYSICAL_MEDIAN['AVERAGE_WIDTH_PHYSICAL_MEDIAN'] <=0)).fillna(0)
LOG_AVERAGE_WIDTH_PHYSICAL_MEDIAN.name = 'LOG_AVERAGE_WIDTH_PHYSICAL_MEDIAN'
LOG_AVERAGE_WIDTH_PHYSICAL_MEDIAN = LOG_AVERAGE_WIDTH_PHYSICAL_MEDIAN.mask(LOG_AVERAGE_WIDTH_PHYSICAL_MEDIAN <= 0).fillna(0)   # To get rid of the small values of log(0.0000e)
# ------------------------------------------------------
#           Central Strip width in (meter) - log
# ------------------------------------------------------
LOG_MAX_WIDTH_CENTRAL_STRIP = np.log(SUM_MAX_MIN_AVERAGE_WIDTH_CENTRAL_STRIP['MAX_WIDTH_CENTRAL_STRIP'].mask(SUM_MAX_MIN_AVERAGE_WIDTH_CENTRAL_STRIP['MAX_WIDTH_CENTRAL_STRIP'] <=0)).fillna(0)
LOG_MAX_WIDTH_CENTRAL_STRIP.name = 'LOG_MAX_WIDTH_CENTRAL_STRIP'
LOG_MAX_WIDTH_CENTRAL_STRIP = LOG_MAX_WIDTH_CENTRAL_STRIP.mask(LOG_MAX_WIDTH_CENTRAL_STRIP<=0).fillna(0)
# ------------------------------------------------------
LOG_MIN_WIDTH_CENTRAL_STRIP = np.log(SUM_MAX_MIN_AVERAGE_WIDTH_CENTRAL_STRIP['MIN_WIDTH_CENTRAL_STRIP'].mask(SUM_MAX_MIN_AVERAGE_WIDTH_CENTRAL_STRIP['MIN_WIDTH_CENTRAL_STRIP'] <=0)).fillna(0)
LOG_MIN_WIDTH_CENTRAL_STRIP.name = 'LOG_MIN_WIDTH_CENTRAL_STRIP'
LOG_MIN_WIDTH_CENTRAL_STRIP = LOG_MIN_WIDTH_CENTRAL_STRIP.mask(LOG_MIN_WIDTH_CENTRAL_STRIP<=0).fillna(0)
# ------------------------------------------------------
LOG_AVERAGE_WIDTH_CENTRAL_STRIP = np.log(SUM_MAX_MIN_AVERAGE_WIDTH_CENTRAL_STRIP['AVERAGE_WIDTH_CENTRAL_STRIP'].mask(SUM_MAX_MIN_AVERAGE_WIDTH_CENTRAL_STRIP['AVERAGE_WIDTH_CENTRAL_STRIP'] <=0)).fillna(0)
LOG_AVERAGE_WIDTH_CENTRAL_STRIP.name = 'LOG_AVERAGE_WIDTH_CENTRAL_STRIP'
LOG_AVERAGE_WIDTH_CENTRAL_STRIP = LOG_AVERAGE_WIDTH_CENTRAL_STRIP.mask(LOG_AVERAGE_WIDTH_CENTRAL_STRIP<=0).fillna(0)

# ==================================================#
#           Constructing Our DATASET
# ==================================================#
# Adding Road types
df = df.join(DIVIDED_NO_CENTRAL_DIVISION).join(DIVIDED_WITH_CENTRAL_DIVISION).join(DIVIDED_NO_PHYSICAL_DIVISION).join(DIVIDED_WITH_PHYSICAL_DIVISION).join(NON_DIVIDED_SINGLE_ROADWAY)
# Adding Number of lanes
df = df.join(NUMBER_OF_LANES)
# Adding Lanes changing
df = df.join(NO_OF_LANES_CHANGED)
# Adding the left turn exclusive lane
df = df.join(LEFT_TURN_EXCLUSIVE_LANE)
# Adding the right turn exclusive lane
df = df.join(RIGHT_TURN_EXCLUSIVE_LANE)
# Adding the physical medium width (two variables)
df = df.join(SUM_MAX_MIN_AVERAGE_WIDTH_PHYSICAL_MEDIAN).join(IS_THERE_PHYSICAL_MEDIAN)
# Adding the central strip width (two variables)
df = df.join(SUM_MAX_MIN_AVERAGE_WIDTH_CENTRAL_STRIP).join(IS_THERE_CENTRAL_STRIP)
# Adding the skewness level
df = df.join(IS_THERE_SKEWNESS)
# Adding the traffic signal variables
#df = df.join(IT_UNCONTROLLED_INT).join(IT_IS_UNCONTROLLED_TWO_AT_LEAST).join(STOP_SIGN).join(IT_IS_NON_SIGNALIZED).join(SIGNALIZED_HIGH_LEVEL_SIGNAL).join(SIGNALIZED_REGULAR_SIGNAL).join(SIGNALIZED_REGULAR_SIGNAL_2)
df = df.join(SIGNALIZED_HIGH_LEVEL_SIGNAL).join(SIGNALIZED_REGULAR_SIGNAL).join(OTHERS).join(FLASHING_GREEN_PED)
# Radius of intersection
df = df.join(SUM_MAX_MIN_AVERAGE_RADIUS)
# ------------------------------------------------------
# Combined both the othershapes and more than 5 arms intersection type
df = df.join(INTERSECTION_TYPE_OTHERS)
# ------------------------------------------------------
# Adding Log variables
df = df.join(LOG_NO_DRIVE_WAYS.to_frame())
df = df.join(LOG_DISTANCE_TO_ADJUST.to_frame())
df = df.join(LOG_LONGEST_WIDTH_INTER.to_frame())
df = df.join(LOG_SHORTEST_WIDTH_INTER.to_frame())
df = df.join(LOG_MAX_RADIUS.to_frame())
df = df.join(LOG_MIN_RADIUS.to_frame())
df = df.join(LOG_AVERAGE_RADIUS.to_frame())
df = df.join(LOG_NUMBER_OF_LANES.to_frame())
df = df.join(LOG_MAX_WIDTH_PHYSICAL_MEDIAN.to_frame())
df = df.join(LOG_MIN_WIDTH_PHYSICAL_MEDIAN.to_frame())
df = df.join(LOG_AVERAGE_WIDTH_PHYSICAL_MEDIAN.to_frame())
df = df.join(LOG_MAX_WIDTH_CENTRAL_STRIP.to_frame())
df = df.join(LOG_MIN_WIDTH_CENTRAL_STRIP.to_frame())
df = df.join(LOG_AVERAGE_WIDTH_CENTRAL_STRIP.to_frame())
# ------------------------------------------------------
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
