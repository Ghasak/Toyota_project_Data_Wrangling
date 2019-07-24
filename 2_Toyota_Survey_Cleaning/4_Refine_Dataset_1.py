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
    minimum_width_physcial_median.append(physical_median_width_df.iloc[index,:].min())
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
    min_width_central_strip.append(width_central_strip_df.iloc[index,:].min())


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
