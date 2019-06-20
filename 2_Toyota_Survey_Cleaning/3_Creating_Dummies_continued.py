"""
=========================================================
          Creating Dummies for and
            arrange your dataset
            Tue Jun. 19th 2019
                 17:03:00
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
import os
Current_Path = os.getcwd()


# print(Current_Path)
# print(f"This is the relative path {os.path.abspath(os.getcwd())}")
# print(f"This is the full path {os.path.dirname(os.path.abspath(__file__))}")

inner_joint_Int = pd.read_excel(Current_Path +
                                "/Toyota_Survey_Sheetfiles/1_Cleaning_Data_set/Results/inner_joint_Int.xlsx",
                                sheet_name="inner_joint_Int")
"""
=========================================================
        Prepare the Intersection Survey
            Columns/variables
                 14:32:00
=========================================================
    - We would like combine the Arm5 and Arm6 into a new
        set which will be our baseline set later in modeling
    - The new variables called Larger than 4 or more, and its
        every variable is sum of variable of arm5 and arm6
"""
inner_joint_Int["Road_type_larger_than_four_arms"] = inner_joint_Int['Road_type_for_fifth_arm'] + inner_joint_Int['Road_type_for_sixth_arm']
# To know which column index number in your dataset use:
inner_joint_Int.columns.get_loc("Road_type_larger_than_four_arms")
# Answer is: 144
# list_Col_Names = inner_joint_Int.columns
# shift = 13  # There are 26 columns that we wish to combine in our dataset, we start with half of them.
# Selected_Column = inner_joint_Int.columns.get_loc("Road_type_for_fifth_arm")
# for i in range(1, 13):
#     inner_joint_Int[list_Col_Names[Selected_Column + i]] = inner_joint_Int[list_Col_Names[Selected_Column + i]] + inner_joint_Int[list_Col_Names[Selected_Column + i + shift]]
#     # print(column)

# This above is working very good, but we will do it manually in Excel for better control.

inner_joint_Int["Road_type_larger_than_four"] = inner_joint_Int["Road_type_for_fifth_arm"] + inner_joint_Int["Road_type_for_sixth_arm"]

inner_joint_Int["Numer_of_lanes_larger_than_four"] = inner_joint_Int["Number_of_lanes_for_fifth_arm"] + inner_joint_Int["Number_of_lanes_for_sixth_arm"]

inner_joint_Int["No_of_lanes_changed_larger_than_four"] = inner_joint_Int["No._of_lanes_changed_at_the_approach.4"] + inner_joint_Int["No._of_lanes_changed_at_the_approach.5"]

inner_joint_Int["Left_turn_only_lane_larger_than_four"] = inner_joint_Int["Left_turn_only_lane_for_fifth_arm"] + inner_joint_Int["Left_turn_only_lane_for_sixth_arm"]

inner_joint_Int["Right_turn_only_lane_larger_than_four"] = inner_joint_Int["Right_turn_only_lane_for_fifth_arm"] + inner_joint_Int["Right_turn_only_lane_for_sixth_arm"]

inner_joint_Int["Width_of_Physical_Median_larger_than_four"] = inner_joint_Int["Width_of_Pysical_Median_of_fifth_arm_if_exist"] + inner_joint_Int["Width_of_Pysical_Median_of_sixth_arm_if_exist"]

inner_joint_Int["Width_of_centeral_strip_larger_than_four"] = inner_joint_Int["Width_of_central_strip_of_fifth_arm_if_exist"] + inner_joint_Int["Width_of_central_strip_of_sixth_arm_if_exist"]

inner_joint_Int["Pedestrain_and_bicycle__larger_than_four"] = inner_joint_Int["Pedestrian_and_bicycle_crossing_roadway_type.4"] + inner_joint_Int["Pedestrian_and_bicycle_crossing_roadway_type.5"]

inner_joint_Int["Skewness_level_larger_than_four"] = inner_joint_Int["Skewness_level_of_fifth_arm_to_the_next_arm"] + inner_joint_Int["Skewness_level_of_sixth_arm_to_the_next_arm"]

inner_joint_Int["Sidewalk_type_First_Side_larger_than_four"] = inner_joint_Int["Sidewalk_type_First_Side.4"] + inner_joint_Int["Sidewalk_type_First_Side.5"]

inner_joint_Int["Sidewalk_type_Second_Side_larger_than_four"] = inner_joint_Int["Sidewalk_type_Second_Side.4"] + inner_joint_Int["Sidewalk_type_Second_Side.5"]

inner_joint_Int["Traffic_signal_contral_type_larger_than_four"] = inner_joint_Int["Traffic_signal_contral_type.4"] + inner_joint_Int["Traffic_signal_contral_type.5"]

inner_joint_Int["Presence_of_pedestrian_traffic_signal_larger_than_four"] = inner_joint_Int["Presence_of_pedestrian_traffic_signal.4"] + inner_joint_Int["Presence_of_pedestrian_traffic_signal"]


inner_joint_Int = inner_joint_Int.drop(['Road_type_for_fifth_arm',
                                        'Road_type_for_sixth_arm',
                                        'Number_of_lanes_for_fifth_arm',
                                        'Number_of_lanes_for_sixth_arm',
                                        'No._of_lanes_changed_at_the_approach.4',
                                        'No._of_lanes_changed_at_the_approach.5',
                                        'Left_turn_only_lane_for_fifth_arm',
                                        'Left_turn_only_lane_for_sixth_arm',
                                        'Right_turn_only_lane_for_fifth_arm',
                                        'Right_turn_only_lane_for_sixth_arm',
                                        'Width_of_Pysical_Median_of_fifth_arm_if_exist',
                                        'Width_of_Pysical_Median_of_sixth_arm_if_exist',
                                        'Width_of_central_strip_of_fifth_arm_if_exist',
                                        'Width_of_central_strip_of_sixth_arm_if_exist',
                                        'Pedestrian_and_bicycle_crossing_roadway_type.4',
                                        'Pedestrian_and_bicycle_crossing_roadway_type.5',
                                        'Skewness_level_of_fifth_arm_to_the_next_arm',
                                        'Skewness_level_of_sixth_arm_to_the_next_arm',
                                        'Sidewalk_type_First_Side.4',
                                        'Sidewalk_type_First_Side.5',
                                        'Traffic_signal_contral_type.4',
                                        'Traffic_signal_contral_type.5',
                                        'Presence_of_pedestrian_traffic_signal.4',
                                        ], 1)

# We will set the intersection ID as an idex to our DataFrame:
inner_joint_Int.set_index(['FilterLess35'], inplace=True)
# Change the Name of this column as it has (. or - or space ---> '_')
inner_joint_Int.columns = inner_joint_Int.columns.str.replace(' |-', '_')
inner_joint_Int.columns = inner_joint_Int.columns.str.replace('\.', '')
# Remove the (degree-sign) after each value you have so you can use later in Google-Earth.
inner_joint_Int["Altitude"] = inner_joint_Int["Altitude"].str.replace('°', '')
inner_joint_Int["Longitute"] = inner_joint_Int["Longitute"].str.replace('°', '')

"""
=========================================================
            Creating the Dummies Variables
                [Using Pandas Function]
=========================================================
    - There are Several steps we can do:
        [1] replace method e.g."df[Column].replace(dictionary)"
            This will allow us to converate any column with text (categoraical)
            to a different name or numbers or anything, using the dictionary.
        [same]    df[newcolumn] = df[column].map(dictionary)
            this method is same functionality to the replace method
        [2] np.where(df[column name] Condition,1,0)
            Condition can be (>0) or any logical condition.
        [same] you can also use the creative method
                1 * (df[column]=="value") which works for the binary cateogrical variables such as (Yes/No)
                converated to (1/0), see V10
            This method is to converate the dummy variable(text) to (1/0) values
        [3] List_of_Dummies = pd.get_dummies(df[column])
            This method will take the "column" converate it to dummies which are same as
            the categories of columns and store them in a mini pandas table "List_of_Dummies"
        [4] df = df.join(List_of_Dummies)
            this has to accombine the get_dummies method in pandas to append the list of new
            dummies (columns) to our existed dataframe (df)
        [5]
"""
# ==================================================#
#       Change Categorical Variables to Dummies
# ==================================================#
# ###################################################
#        Variables For All intersection Geometry
# ###################################################
# ===================================================
# ============== Intersection_type ==========V1======
# ===================================================
# Check the missing values in your column
inner_joint_Int["Intersection_type"].isnull().sum()
inner_joint_Int["Intersection_type"].isnull().values.any()
# Replace the Missing values using: df[1].fillna(0, inplace=True)
# Start with the intersection Type cateogrical variable
Inters_type_Table = pd.get_dummies(inner_joint_Int["Intersection_type"])
# We will clean the column names to not have spaces
Inters_type_Table.columns = Inters_type_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
Inters_type_Table.columns = Inters_type_Table.columns.str.replace(' |-', '_')
# Remove the (+) from Cross_intersection column name:
Inters_type_Table.rename(columns={'Cross_intersection(十)': 'Cross_intersection'}, inplace=True)
# Verify the Table output in two ways:
Inters_type_Table.describe().T
Inters_type_Table["Cross_intersection"].value_counts(normalize=True)
# ===================================================
# ============== Number_of_driverways ==========V2===
# =======================================================
# Check the missing values in your column
inner_joint_Int["Number_of_driverways"].isnull().sum()
inner_joint_Int["Number_of_driverways"].isnull().values.any()
# We captured only one
# Replace the Missing values using: df[1].fillna(0, inplace=True)
inner_joint_Int["Number_of_driverways"].fillna(0, inplace=True)
# =======================================================
# =Distance_to_adjacent_intersection_within_500_meter ==V3==
# =======================================================
inner_joint_Int["Distance_to_adjacent_intersection_within_500_meter"].isnull().sum()
# This variable has no problem
# =======================================================
# ============== Longest_Width_of_intersection ===V4=====
# =======================================================
inner_joint_Int["Longest_Width_of_intersection"].isnull().sum()
# This variable has no problem
# =======================================================
# ============== Shortest_Width_of_intersection ===V5====
# =======================================================
inner_joint_Int["Shortest_Width_of_intersection"].isnull().sum()
# There are three missing values for this variable
inner_joint_Int["Shortest_Width_of_intersection"].fillna(0, inplace=True)
# =======================================================
# ============== Intersection Radius =============V6=====
# =======================================================
List_Radius = ["Radius_of_arm_1_and_arm_2_", "Radius_of_arm_2_and_arm_3_", "Radius_of_arm_3_and_arm_4_", "Radius_of_arm_4_and_arm_5_", "Radius_of_arm_5_and_arm_6_", "Radius_of_arm_6_and_arm_7_"]

for i in range(len(List_Radius)):
    print(List_Radius[i])
    if inner_joint_Int[List_Radius[i]].isnull().values.any():
        inner_joint_Int[List_Radius[i]].fillna(0, inplace=True)
# =======================================================
# ================ Number_of_arms =================V7====
# =======================================================
# Check the missing values in your column
inner_joint_Int["Number_of_arms"].isnull().sum()
inner_joint_Int["Number_of_arms"].isnull().values.any()
# Replace the Missing values using: df[1].fillna(0, inplace=True)
# Start with the intersection Type cateogrical variable
Number_of_arms_Table = pd.get_dummies(inner_joint_Int["Number_of_arms"])
# We will clean the column names to not have spaces
Number_of_arms_Table.columns = Number_of_arms_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
Number_of_arms_Table.columns = Number_of_arms_Table.columns.str.replace(' |-', '_')
# =======================================================
# =======================================================
# ###################################################
#        Variables For Each Arm
# ###################################################
# ###################################################
#        First Arm
# ###################################################
# =======================================================
# ================ Road_type_for_first_arm ========V8====
# =======================================================
# Check the missing values in your column
inner_joint_Int["Road_type_for_first_arm"].isnull().sum()
inner_joint_Int["Road_type_for_first_arm"].isnull().values.any()
# Replace the Missing values using: df[1].fillna(0, inplace=True)
# Start with the intersection Type categorical variable
Road_type_for_first_arm_Table = pd.get_dummies(inner_joint_Int["Road_type_for_first_arm"], prefix="Arm1_RoadType")
# We will clean the column names to not have spaces
Road_type_for_first_arm_Table.columns = Road_type_for_first_arm_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
Road_type_for_first_arm_Table.columns = Road_type_for_first_arm_Table.columns.str.replace(' |-', '_')
# =======================================================
# ================ Number_of_lanes_for_first_arm ==V9====
# =======================================================
# Check the missing values in your column
inner_joint_Int["Number_of_lanes_for_first_arm"].isnull().sum()
inner_joint_Int["Number_of_lanes_for_first_arm"].isnull().values.any()
# This variable is should nominal (integer) but there is text in the colum that I will remove
# The text is "6 or more" will be replaced by 6 arms to reflect high numers.
list1 = []
#inner_joint_Int["Number_of_lanes_for_first_arm"] = inner_joint_Int["Number_of_lanes_for_first_arm"].str.strip()
for i in inner_joint_Int["Number_of_lanes_for_first_arm"]:
    # print(i)
    if i != "6 or more":
        list1.append(i)
    if i == "6 or more":
        list1.append(6)
inner_joint_Int["Number_of_lanes_for_first_arm"] = list1
# Check the affected intersections
a1 = "23-K11790-000"  # ; inner_joint_Int.loc["23-K11790-000","Number_of_lanes_for_first_arm"]
a2 = "23-K11893-000"  # ; inner_joint_Int.loc["23-K11893-000","Number_of_lanes_for_first_arm"]
a3 = "23-K11928-000"  # ; inner_joint_Int.loc["23-K11928-000","Number_of_lanes_for_first_arm"]
print(f"The affected intersections \n\t For the variable Number_of_lanes_for_first_arm are:  {a1}, {a2} and {a3}")
# =======================================================
# ======== No._of_lanes_changed_at_the_approach ===V10===
# =======================================================
# As we can see No. has already been replaced above to No_ using reqular expression
inner_joint_Int["No_of_lanes_changed_at_the_approach"].isnull().sum()
# Converte a Dummy binary (text) -----> to (1/0)
inner_joint_Int["No_of_lanes_changed_at_the_approach"] = 1 * (inner_joint_Int["No_of_lanes_changed_at_the_approach"] == "Yes (it has changed)")
inner_joint_Int["Arm1_No_of_lanes_changed_at_the_approach"] = inner_joint_Int["No_of_lanes_changed_at_the_approach"]
inner_joint_Int.drop("No_of_lanes_changed_at_the_approach", inplace=True, axis=1)
# =======================================================
# ===== Left_turn_only_lane_for_first_arm ========V11====
# =======================================================
inner_joint_Int["Left_turn_only_lane_for_first_arm"].isnull().sum()
# Converte a Dummy binary (text) -----> to (1/0)
inner_joint_Int["Left_turn_only_lane_for_first_arm"] = 1 * (inner_joint_Int["Left_turn_only_lane_for_first_arm"] == "Exist")
# =======================================================
# ========= Right_turn_only_lane_for_first_arm ===V12====
# =======================================================
inner_joint_Int["Right_turn_only_lane_for_first_arm"].isnull().sum()
# Converte a Dummy binary (text) -----> to (1/0)
inner_joint_Int["Right_turn_only_lane_for_first_arm"] = 1 * (inner_joint_Int["Right_turn_only_lane_for_first_arm"] == "Exist")
# === Width_of_Pysical_Median_of_first_arm_if_exist ====V13====
# =======================================================
inner_joint_Int["Width_of_Pysical_Median_of_first_arm_if_exist"].isnull().sum()
inner_joint_Int["Width_of_Pysical_Median_of_first_arm_if_exist"].fillna(0, inplace=True)
# We will create a variable for the physical median using np.where and converate it to a pandas-Series which
# we will use join later to add it to our exited DataFrame (inner_joint_Int), notice I added also the index for matching.
Is_there_Physical_Median_first_arm = pd.Series(np.where(inner_joint_Int["Width_of_Pysical_Median_of_first_arm_if_exist"] != 0, 1, 0), index=inner_joint_Int.index)
# =======================================================
# === Width_of_central_strip_of_first_arm_if_exist ======V14====
# =======================================================
# It seems this variable from the survey has a problem
# the cell number 7 has a text lets remove it first
list2 = []
#inner_joint_Int["Number_of_lanes_for_first_arm"] = inner_joint_Int["Number_of_lanes_for_first_arm"].str.strip()
for i in inner_joint_Int["Width_of_central_strip_of_first_arm_if_exist"]:
    # print(i)
    if i != "Width_of_Pysical_Median_of_first_arm_if_exist":
        list2.append(i)
    if i == "Width_of_Pysical_Median_of_first_arm_if_exist":
        list2.append(0)
inner_joint_Int["Width_of_central_strip_of_first_arm_if_exist"] = list2
# Check the missing values in your column
inner_joint_Int["Width_of_central_strip_of_first_arm_if_exist"].isnull().sum()
inner_joint_Int["Width_of_central_strip_of_first_arm_if_exist"].isnull().values.any()
inner_joint_Int["Width_of_central_strip_of_first_arm_if_exist"].fillna(0, inplace=True)
# Simliar to above lets create a dummy variable for all roads that have a central strip
Is_there_centeral_strip_first_arm = pd.Series(np.where(inner_joint_Int["Width_of_central_strip_of_first_arm_if_exist"] != 0, 1, 0), index=inner_joint_Int.index)
# =======================================================
# = Pedestrian_and_bicycle_crossing_roadway_type ==V15===
# =======================================================
# This variable is categorical and has a problem, missing entry at 23-K06472-000
list3 = []
#inner_joint_Int["Number_of_lanes_for_first_arm"] = inner_joint_Int["Number_of_lanes_for_first_arm"].str.strip()

# Python non-unique NaN: float('nan')
# numpy unique NaN (singleton) : np.nan
# any other objects: string or whatever (does not raise exceptions if encountered)
# https://stackoverflow.com/questions/944700/how-can-i-check-for-nan-values


def is_nan(x):
    return (x is np.nan or x != x)


# ========================================================================
for i in inner_joint_Int["Pedestrian_and_bicycle_crossing_roadway_type"]:
    # print(i)
    if not is_nan(i):
        # print(i)
        list3.append(i)
    else:
        list3.append("Crosswalk existed within 50m")
print(f"Variable Pedestrian_and_bicycle_crossing_roadway_type of first arm")
print("===================================================================")
a4 = inner_joint_Int.loc["23-K06472-000", "Pedestrian_and_bicycle_crossing_roadway_type"]
print(f"It was like this {a4} at 23-K06472-000")
inner_joint_Int["Pedestrian_and_bicycle_crossing_roadway_type"] = list3
a4 = inner_joint_Int.loc["23-K06472-000", "Pedestrian_and_bicycle_crossing_roadway_type"]
print(f"Now it becomes '{a4}' at 23-K06472-000")
print("===================================================================")
# Changing the Categorical Variable to the following:
Pedestrian_and_bicycle_first_arm_Table = pd.get_dummies(inner_joint_Int["Pedestrian_and_bicycle_crossing_roadway_type"], prefix="Arm1")
# We will clean the column names to not have spaces
Pedestrian_and_bicycle_first_arm_Table.columns = Pedestrian_and_bicycle_first_arm_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
Pedestrian_and_bicycle_first_arm_Table.columns = Pedestrian_and_bicycle_first_arm_Table.columns.str.replace(' |-', '_')
# ========================================================================
# === Skewness_level_of_first_arm_to_the_next_arm ==V16==
# =======================================================
inner_joint_Int["Skewness_level_of_first_arm_to_the_next_arm"].isnull().sum()
# Simliar to above lets create a dummy variable for all roads that have a central strip
Is_there_centeral_Skewness_arm_one_two = 1 * (inner_joint_Int["Skewness_level_of_first_arm_to_the_next_arm"] == "Yes (it is skewed)")
# =======================================================
# =============== Sidewalk_type_First_Side =======V17====
# =======================================================
inner_joint_Int["Sidewalk_type_First_Side"].isnull().sum()  # There is a missing value at 23-K06475-000
inner_joint_Int["Sidewalk_type_First_Side"].fillna("No sidewalk", inplace=True)
# Changing the Categorical Variable to the following:
Sidewalk_type_First_Side_first_arm_Table = pd.get_dummies(inner_joint_Int["Sidewalk_type_First_Side"], prefix="Arm1_1stSide")
# We will clean the column names to not have spaces
Sidewalk_type_First_Side_first_arm_Table.columns = Sidewalk_type_First_Side_first_arm_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
Sidewalk_type_First_Side_first_arm_Table.columns = Sidewalk_type_First_Side_first_arm_Table.columns.str.replace(' |-', '_')
# =======================================================
# =============== Sidewalk_type_Second_Side ======V18====
# =======================================================
inner_joint_Int["Sidewalk_type_Second_Side"].isnull().sum()
# Changing the Categorical Variable to the following:
Sidewalk_type_Second_Side_first_arm_Table = pd.get_dummies(inner_joint_Int["Sidewalk_type_Second_Side"], prefix="Arm1_2ndSide")
# We will clean the column names to not have spaces
Sidewalk_type_Second_Side_first_arm_Table.columns = Sidewalk_type_Second_Side_first_arm_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
Sidewalk_type_Second_Side_first_arm_Table.columns = Sidewalk_type_Second_Side_first_arm_Table.columns.str.replace(' |-', '_')
# =============== Traffic_signal_contral_type ====V19====
# =======================================================
inner_joint_Int["Traffic_signal_contral_type"].isnull().sum()
# Changing the Categorical Variable to the following:
Traffic_signal_contral_type_first_arm_Table = pd.get_dummies(inner_joint_Int["Traffic_signal_contral_type"], prefix="Arm1")
# We will clean the column names to not have spaces
Traffic_signal_contral_type_first_arm_Table.columns = Traffic_signal_contral_type_first_arm_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
Traffic_signal_contral_type_first_arm_Table.columns = Traffic_signal_contral_type_first_arm_Table.columns.str.replace(' |-', '_')

# =============== Traffic_signal_contral_type ====V20====
# =======================================================

inner_joint_Int['Presence_of_pedestrian_traffic_signal'].isnull().sum()
# Chaging the Categorical Variable to the following:
inner_joint_Int['Presence_of_pedestrian_traffic_signal'] = 1 * (inner_joint_Int["Presence_of_pedestrian_traffic_signal"] == "Exist")

# =======================================================
# ###################################################
#        Second Arm
# ###################################################
# =============== Road_type_for_second_arm ====V21=======
inner_joint_Int["Road_type_for_second_arm"].isnull().sum()
# Changing the Categorical Variable to the following:
Road_type_for_second_arm_Table = pd.get_dummies(inner_joint_Int["Road_type_for_second_arm"], prefix="Arm2")
# We will clean the column names to not have spaces
Road_type_for_second_arm_Table.columns = Road_type_for_second_arm_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
Road_type_for_second_arm_Table.columns = Road_type_for_second_arm_Table.columns.str.replace(' |-', '_')
# ================ Number_of_lanes_for_second_arm =================V22====
# =======================================================
# Check the missing values in your column
inner_joint_Int["Number_of_lanes_for_second_arm"].isnull().sum()
inner_joint_Int["Number_of_lanes_for_second_arm"].isnull().values.any()
##############################################################################
'''
    - I have created two algorithm to bring you the value in a pattern inside the column
    - Output will retrun the intersection ID that has this pattern.
'''
##############################################################################
# [METHOD A]
listx = ["6 or more"]
pattern = '|'.join(listx)
IScritical = inner_joint_Int["Number_of_lanes_for_second_arm"].str.contains(pattern)
len(inner_joint_Int) - IScritical.isnull().sum()
##############################################################################
# [METHOD B]
listy = []

for row in range(len(inner_joint_Int["Number_of_lanes_for_second_arm"])):
    if inner_joint_Int["Number_of_lanes_for_second_arm"].iloc[row] == pattern:
        listy.append(inner_joint_Int.index[row])
##############################################################################
# This variable is should nominal (integer) but there is text in the colum that I will remove
# The text is "6 or more" will be replaced by 6 arms to reflect high numbers.
list1 = []
#inner_joint_Int["Number_of_lanes_for_second_arm"] = inner_joint_Int["Number_of_lanes_for_second_arm"].str.strip()
for i in inner_joint_Int["Number_of_lanes_for_second_arm"]:
    # print(i)
    if i != "6 or more":
        list1.append(i)
    if i == "6 or more":
        list1.append(6)
inner_joint_Int["Number_of_lanes_for_second_arm"] = list1
# Check the affected intersections, Or Use either METHOD A or METHOD B
List_affected = []
List_affected.append('23-K11827-000')
List_affected.append('23-K11829-000')
List_affected.append('23-K11834-000')
List_affected.append('23-K11835-000')
List_affected.append('23-K11887-000')
List_affected.append('23-K11900-000')
List_affected.append('23-K11912-000')
List_affected.append('23-K11913-000')
print(f"The affected intesections \n\t For the variable Number_of_lanes_for_second_arm are:  {List_affected}")

# ================ No_of_lanes_changed_at_the_approach1 =================V23====

# As we can see No. has already been replaced above to No_ using reqular expression
inner_joint_Int["No_of_lanes_changed_at_the_approach1"].isnull().sum()
# Converte a Dummy binary (text) -----> to (1/0)
inner_joint_Int["No_of_lanes_changed_at_the_approach1"] = 1 * (inner_joint_Int["No_of_lanes_changed_at_the_approach1"] == "Yes (it has changed)")
# =======================================================
# ===== Left_turn_only_lane_for_second_arm ========V24====
inner_joint_Int["Left_turn_only_lane_for_second_arm"].isnull().sum()
# Converte a Dummy binary (text) -----> to (1/0)
inner_joint_Int["Left_turn_only_lane_for_second_arm"] = 1 * (inner_joint_Int["Left_turn_only_lane_for_second_arm"] == "Exist")
# =======================================================
# ========= Right_turn_only_lane_for_second_arm ===V25====
# =======================================================
inner_joint_Int["Right_turn_only_lane_for_second_arm"].isnull().sum()
# Converte a Dummy binary (text) -----> to (1/0)
inner_joint_Int["Right_turn_only_lane_for_second_arm"] = 1 * (inner_joint_Int["Right_turn_only_lane_for_second_arm"] == "Exist")
# === Width_of_Pysical_Median_of_second_arm_if_exist ====V26====
# =======================================================
inner_joint_Int["Width_of_Pysical_Median_of_second_arm_if_exist"].isnull().sum()
inner_joint_Int["Width_of_Pysical_Median_of_second_arm_if_exist"].fillna(0, inplace=True)
# We will create a variable for the physical median using np.where and converate it to a pandas-Series which
# we will use join later to add it to our exited DataFrame (inner_joint_Int), notice I added also the index for matching.
Is_there_Physical_Median_first_arm = pd.Series(np.where(inner_joint_Int["Width_of_Pysical_Median_of_second_arm_if_exist"] != 0, 1, 0), index=inner_joint_Int.index)
# =======================================================
# === Width_of_central_strip_of_second_arm_if_exist ======V27====
# =======================================================
# It seems this variable from the survey has a problem
# the cell number 7 has a text lets remove it first
list2 = []
#inner_joint_Int["Number_of_lanes_for_first_arm"] = inner_joint_Int["Number_of_lanes_for_first_arm"].str.strip()
for i in inner_joint_Int["Width_of_central_strip_of_second_arm_if_exist"]:
    # print(i)
    if i != "Width_of_Pysical_Median_of_first_arm_if_exist":
        list2.append(i)
    if i == "Width_of_Pysical_Median_of_first_arm_if_exist":
        list2.append(0)
inner_joint_Int["Width_of_central_strip_of_second_arm_if_exist"] = list2
# Check the missing values in your column
inner_joint_Int["Width_of_central_strip_of_second_arm_if_exist"].isnull().sum()
inner_joint_Int["Width_of_central_strip_of_second_arm_if_exist"].isnull().values.any()
inner_joint_Int["Width_of_central_strip_of_second_arm_if_exist"].fillna(0, inplace=True)
# Simliar to above lets create a dummy variable for all roads that have a central strip
Is_there_centeral_strip_first_arm = pd.Series(np.where(inner_joint_Int["Width_of_central_strip_of_second_arm_if_exist"] != 0, 1, 0), index=inner_joint_Int.index)
# =======================================================
# = Pedestrian_and_bicycle_crossing_roadway_type1 ==V28===
# =======================================================
# This variable is categorical and has a problem, missing entry at 23-K06472-000
inner_joint_Int["Pedestrian_and_bicycle_crossing_roadway_type1"].isnull().sum()
print("Variable Pedestrian_and_bicycle_crossing_roadway_type1 of the second arm has no probme")
print("Notice that the number (1) added in the end indicating the second arm")
print("===================================================================")
# Changing the Categorical Variable to the following:
Pedestrian_and_bicycle_second_arm_Table = pd.get_dummies(inner_joint_Int["Pedestrian_and_bicycle_crossing_roadway_type1"], prefix="Arm2")
# We will clean the column names to not have spaces
Pedestrian_and_bicycle_second_arm_Table.columns = Pedestrian_and_bicycle_second_arm_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
Pedestrian_and_bicycle_second_arm_Table.columns = Pedestrian_and_bicycle_second_arm_Table.columns.str.replace(' |-', '_')
print(f"Check the Sum of Dummies equal to 1 using {Pedestrian_and_bicycle_second_arm_Table.describe().T.iloc[:,1].sum()}")
print("===================================================================")
k = inner_joint_Int["Pedestrian_and_bicycle_crossing_roadway_type1"].value_counts(normalize=True).sum()
print(f"also for our main categorical variable before trasfered to dummies {k}")
# ========================================================================
# === Skewness_level_of_second_arm_to_the_next_arm ==V29==
# =======================================================
inner_joint_Int["Skewness_level_of_second_arm_to_the_next_arm"].isnull().sum()
# There is a missing input at: 23-K06501-000
list3 = []
#inner_joint_Int["Number_of_lanes_for_first_arm"] = inner_joint_Int["Number_of_lanes_for_first_arm"].str.strip()

# Python non-unique NaN: float('nan')
# numpy unique NaN (singleton) : np.nan
# any other objects: string or whatever (does not raise exceptions if encountered)
# https://stackoverflow.com/questions/944700/how-can-i-check-for-nan-values


def is_nan(x):
    return (x is np.nan or x != x)


# ========================================================================
for i in inner_joint_Int["Skewness_level_of_second_arm_to_the_next_arm"]:
    # print(i)
    if not is_nan(i):
        # print(i)
        list3.append(i)
    else:
        list3.append("No (it is not skewed)")
inner_joint_Int["Skewness_level_of_second_arm_to_the_next_arm"] = list3
# Simliar to above lets create a dummy variable for all roads that have a central strip
Is_there_centeral_Skewness_arm_two_three = 1 * (inner_joint_Int["Skewness_level_of_second_arm_to_the_next_arm"] == "Yes (it is skewed)")
# =======================================================
# =============== Sidewalk_type_First_Side1 =======V30====
# =======================================================
inner_joint_Int["Sidewalk_type_First_Side1"].isnull().sum()  # There is a missing value at 23-K06475-000
inner_joint_Int["Sidewalk_type_First_Side1"].fillna("No sidewalk", inplace=True)
# Changing the Categorical Variable to the following:
Sidewalk_type_First_Side_second_arm_Table = pd.get_dummies(inner_joint_Int["Sidewalk_type_First_Side1"], prefix="Arm2_1stSide")
# We will clean the column names to not have spaces
Sidewalk_type_First_Side_second_arm_Table.columns = Sidewalk_type_First_Side_second_arm_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
Sidewalk_type_First_Side_second_arm_Table.columns = Sidewalk_type_First_Side_second_arm_Table.columns.str.replace(' |-', '_')
# =======================================================
# =============== Sidewalk_type_Second_Side1 ======V31====
# =======================================================
inner_joint_Int["Sidewalk_type_Second_Side1"].isnull().sum()
# Changing the Categorical Variable to the following:
Sidewalk_type_Second_Side_second_arm_Table = pd.get_dummies(inner_joint_Int["Sidewalk_type_Second_Side1"], prefix="Arm2_2ndSide")
# We will clean the column names to not have spaces
Sidewalk_type_Second_Side_second_arm_Table.columns = Sidewalk_type_Second_Side_second_arm_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
Sidewalk_type_Second_Side_second_arm_Table.columns = Sidewalk_type_Second_Side_second_arm_Table.columns.str.replace(' |-', '_')
# # =============== Traffic_signal_contral_type1 ====V32====
# # =======================================================
inner_joint_Int["Traffic_signal_contral_type1"].isnull().sum()
# Changing the Categorical Variable to the following:
Traffic_signal_contral_type_second_arm_Table = pd.get_dummies(inner_joint_Int["Traffic_signal_contral_type1"], prefix="Arm2")
# We will clean the column names to not have spaces
Traffic_signal_contral_type_second_arm_Table.columns = Traffic_signal_contral_type_second_arm_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
Traffic_signal_contral_type_second_arm_Table.columns = Traffic_signal_contral_type_second_arm_Table.columns.str.replace(' |-', '_')
# # =============== Presence_of_pedestrian_traffic_signal1 ====V33====
# # =======================================================
inner_joint_Int["Presence_of_pedestrian_traffic_signal1"].isnull().sum()
# Chaging the Categorical Variable to the following:
inner_joint_Int['Presence_of_pedestrian_traffic_signal1'] = 1 * (inner_joint_Int["Presence_of_pedestrian_traffic_signal1"] == "Exist")

# ========================================================================
# ###################################################
#        Third Arm
# ###################################################
# Due to missing information of Intersection 23-K06472-000
# We suggest to remove this from our dataset
inner_joint_Int = inner_joint_Int.drop("23-K06472-000", axis=0)

# =============== Road_type_for_third_arm ====V34=======
inner_joint_Int["Road_type_for_third_arm"].isnull().sum()
Road_type_for_third_arm_Table = pd.get_dummies(inner_joint_Int["Road_type_for_third_arm"], prefix="Arm3")
# We will clean the column names to not have spaces
Road_type_for_third_arm_Table.columns = Road_type_for_third_arm_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
Road_type_for_third_arm_Table.columns = Road_type_for_third_arm_Table.columns.str.replace(' |-', '_')
# ================ Number_of_lanes_for_third_arm =================V35====
# =======================================================
# Check the missing values in your column
inner_joint_Int["Number_of_lanes_for_third_arm"].isnull().sum()
inner_joint_Int["Number_of_lanes_for_third_arm"].isnull().values.any()

listy = []
listz = []
for row in range(len(inner_joint_Int["Number_of_lanes_for_third_arm"])):
    if is_nan(inner_joint_Int["Number_of_lanes_for_third_arm"].iloc[row]):
        listy.append(inner_joint_Int.index[row])
print("========================================================")
print("The Third Arm-----> Number_of_lanes_for_third_arm")
print(f"There is a missing values at intersection {listy}")
print("========================================================")
print("Fixing Missing Values: Left_turn_only_lane_for_third_arm")
print("========================================================")
print(f'Missing values are at {listy}')
print("========================================================")
listy = []
listx = ["6 or more"]
pattern = '|'.join(listx)
# Adding for the empty celles
for row in range(len(inner_joint_Int["Number_of_lanes_for_third_arm"])):
    if is_nan(inner_joint_Int["Number_of_lanes_for_third_arm"].iloc[row]):
        listy.append(pattern)
    else:
        listy.append(inner_joint_Int["Number_of_lanes_for_third_arm"].iloc[row])

inner_joint_Int["Number_of_lanes_for_third_arm"] = listy
# Remove hte pattern in your column
for row in range(len(inner_joint_Int["Number_of_lanes_for_third_arm"])):
    if inner_joint_Int["Number_of_lanes_for_third_arm"].iloc[row] != pattern:
        listz.append(inner_joint_Int["Number_of_lanes_for_third_arm"].iloc[row])
    if inner_joint_Int["Number_of_lanes_for_third_arm"].iloc[row] == pattern:
        listz.append(6)

inner_joint_Int["Number_of_lanes_for_third_arm"] = listz
# ================ No_of_lanes_changed_at_the_approach2 =================V36====

inner_joint_Int["No_of_lanes_changed_at_the_approach2"].isnull().sum()
# Converte a Dummy binary (text) -----> to (1/0)
inner_joint_Int["No_of_lanes_changed_at_the_approach2"] = 1 * (inner_joint_Int["No_of_lanes_changed_at_the_approach2"] == "Yes (it has changed)")
# # =======================================================
# ===== Left_turn_only_lane_for_third_arm ========V37====
inner_joint_Int["Left_turn_only_lane_for_third_arm"].isnull().sum()
# Converte a Dummy binary (text) -----> to (1/0)
inner_joint_Int["Left_turn_only_lane_for_third_arm"] = 1 * (inner_joint_Int["Left_turn_only_lane_for_third_arm"] == "Exist")
# # =======================================================
# # ========= Right_turn_only_lane_for_third_arm ===V38====
# # =======================================================
inner_joint_Int["Right_turn_only_lane_for_third_arm"].isnull().sum()
# Converte a Dummy binary (text) -----> to (1/0)
inner_joint_Int["Right_turn_only_lane_for_third_arm"] = 1 * (inner_joint_Int["Right_turn_only_lane_for_third_arm"] == "Exist")
# # # === Width_of_Pysical_Median_of_third_arm_if_exist ====V39====
# # # =======================================================
inner_joint_Int["Width_of_Pysical_Median_of_third_arm_if_exist"].isnull().sum()
inner_joint_Int["Width_of_Pysical_Median_of_third_arm_if_exist"].fillna(0, inplace=True)
# We will create a variable for the physical median using np.where and converate it to a pandas-Series which
# we will use join later to add it to our exited DataFrame (inner_joint_Int), notice I added also the index for matching.
Is_there_Physical_Median_third_arm = pd.Series(np.where(inner_joint_Int["Width_of_Pysical_Median_of_third_arm_if_exist"] != 0, 1, 0), index=inner_joint_Int.index)
# =======================================================
# === Width_of_central_strip_of_third_arm_if_exist ======V40====
# =======================================================

# Check the missing values in your column
inner_joint_Int["Width_of_central_strip_of_third_arm_if_exist"].isnull().sum()
inner_joint_Int["Width_of_central_strip_of_third_arm_if_exist"].isnull().values.any()
inner_joint_Int["Width_of_central_strip_of_third_arm_if_exist"].fillna(0, inplace=True)
# Simliar to above lets create a dummy variable for all roads that have a central strip
Is_there_centeral_strip_third_arm = pd.Series(np.where(inner_joint_Int["Width_of_central_strip_of_third_arm_if_exist"] != 0, 1, 0), index=inner_joint_Int.index)
# =======================================================
# = Pedestrian_and_bicycle_crossing_roadway_type2 ==V41===
# =======================================================
# This variable is categorical and has a problem, missing entry at 23-K06472-000
inner_joint_Int["Pedestrian_and_bicycle_crossing_roadway_type2"].isnull().sum()
print("Variable Pedestrian_and_bicycle_crossing_roadway_type2 of the third arm has no problem")
print("Notice that the number (2) added in the end indicating the third arm")
print("===================================================================")
# Changing the Categorical Variable to the following:
Pedestrian_and_bicycle_third_arm_Table = pd.get_dummies(inner_joint_Int["Pedestrian_and_bicycle_crossing_roadway_type2"], prefix="Arm3")
# We will clean the column names to not have spaces
Pedestrian_and_bicycle_third_arm_Table.columns = Pedestrian_and_bicycle_third_arm_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
Pedestrian_and_bicycle_third_arm_Table.columns = Pedestrian_and_bicycle_third_arm_Table.columns.str.replace(' |-', '_')
print(f"Check the Sum of Dummies equal to 1 using {Pedestrian_and_bicycle_third_arm_Table.describe().T.iloc[:,1].sum()}")
print("===================================================================")
k = inner_joint_Int["Pedestrian_and_bicycle_crossing_roadway_type2"].value_counts(normalize=True).sum()
print(f"also for our main categorical variable before trasfered to dummies {k}")
# ========================================================================
# === Skewness_level_of_third_arm_to_the_next_arm ==V42==
# ========================================================================
inner_joint_Int["Skewness_level_of_third_arm_to_the_next_arm"].isnull().sum()
inner_joint_Int["Skewness_level_of_third_arm_to_the_next_arm"].fillna("No (it is not skewed)", inplace=True)
# Simliar to above lets create a dummy variable for all roads that have a central strip
Is_there_centeral_Skewness_arm_three_fourth = 1 * (inner_joint_Int["Skewness_level_of_third_arm_to_the_next_arm"] == "Yes (it is skewed)")
# =======================================================
# =============== Sidewalk_type_First_Side2 =======V43====
# =======================================================
inner_joint_Int["Sidewalk_type_First_Side2"].isnull().sum()  # There is a missing value at 23-K06475-000
inner_joint_Int["Sidewalk_type_First_Side2"].fillna("No sidewalk", inplace=True)
# Changing the Categorical Variable to the following:
Sidewalk_type_First_Side_third_arm_Table = pd.get_dummies(inner_joint_Int["Sidewalk_type_First_Side2"], prefix="Arm3_1stSide")
# We will clean the column names to not have spaces
Sidewalk_type_First_Side_third_arm_Table.columns = Sidewalk_type_First_Side_third_arm_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
Sidewalk_type_First_Side_third_arm_Table.columns = Sidewalk_type_First_Side_third_arm_Table.columns.str.replace(' |-', '_')
# =======================================================
# =============== Sidewalk_type_Second_Side2 ======V42====
# =======================================================
inner_joint_Int["Sidewalk_type_Second_Side2"].isnull().sum()
# Changing the Categorical Variable to the following:
Sidewalk_type_Second_Side_third_arm_Table = pd.get_dummies(inner_joint_Int["Sidewalk_type_Second_Side2"], prefix="Arm3_2ndSide")
# We will clean the column names to not have spaces
Sidewalk_type_Second_Side_third_arm_Table.columns = Sidewalk_type_Second_Side_second_arm_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
Sidewalk_type_Second_Side_third_arm_Table.columns = Sidewalk_type_Second_Side_second_arm_Table.columns.str.replace(' |-', '_')
# # =============== Traffic_signal_contral_type2 ====V43====
# # =======================================================
inner_joint_Int["Traffic_signal_contral_type2"].isnull().sum()
# Changing the Categorical Variable to the following:
Traffic_signal_contral_type_third_arm_Table = pd.get_dummies(inner_joint_Int["Traffic_signal_contral_type2"], prefix="Arm3")
# We will clean the column names to not have spaces
Traffic_signal_contral_type_third_arm_Table.columns = Traffic_signal_contral_type_third_arm_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
Traffic_signal_contral_type_third_arm_Table.columns = Traffic_signal_contral_type_third_arm_Table.columns.str.replace(' |-', '_')

# # =============== Presence_of_pedestrian_traffic_signal2 ====V44====
# # =======================================================
inner_joint_Int["Presence_of_pedestrian_traffic_signal2"].isnull().sum()
# Chaging the Categorical Variable to the following:
inner_joint_Int['Presence_of_pedestrian_traffic_signal2'] = 1 * (inner_joint_Int["Presence_of_pedestrian_traffic_signal2"] == "Exist")

# ========================================================================
# ###################################################
#        Fourth Arm
# ###################################################
# =============== Road_type_for_fourth_arm ====V45=======
inner_joint_Int["Road_type_for_fourth_arm"].isnull().sum()
inner_joint_Int["Road_type_for_fourth_arm"].fillna("Non_Existed", inplace=True)

Road_type_for_fourth_arm_Table = pd.get_dummies(inner_joint_Int["Road_type_for_fourth_arm"], prefix="Arm4")
# We will clean the column names to not have spaces
Road_type_for_fourth_arm_Table.columns = Road_type_for_fourth_arm_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
Road_type_for_fourth_arm_Table.columns = Road_type_for_fourth_arm_Table.columns.str.replace(' |-', '_')
# =======================================================
# ================ Number_of_lanes_for_fourth_arm =================V46====
# =======================================================
# Check the missing values in your column
inner_joint_Int["Number_of_lanes_for_fourth_arm"].isnull().sum()
inner_joint_Int["Number_of_lanes_for_fourth_arm"].isnull().values.any()
inner_joint_Int["Number_of_lanes_for_fourth_arm"].fillna(0, inplace=True)
print("========================================================")
listg = []
listz = []
listx = ["6 or more"]
pattern = '|'.join(listx)
# Remove hte pattern in your column
for row in range(len(inner_joint_Int["Number_of_lanes_for_fourth_arm"])):
    if inner_joint_Int["Number_of_lanes_for_fourth_arm"].iloc[row] != pattern:
        listz.append(inner_joint_Int["Number_of_lanes_for_fourth_arm"].iloc[row])
    if inner_joint_Int["Number_of_lanes_for_fourth_arm"].iloc[row] == pattern:
        listg.append(inner_joint_Int.index[row])
        listz.append(6)
print("========================================================")
print(f"Number_of_lanes_for_fourth_arm has 6 or more at intersections {listg}")
inner_joint_Int["Number_of_lanes_for_fourth_arm"] = listz
# ================ No_of_lanes_changed_at_the_approach3 =================V47====

inner_joint_Int["No_of_lanes_changed_at_the_approach3"].isnull().sum()
inner_joint_Int["No_of_lanes_changed_at_the_approach3"].fillna("Non_Existed", inplace=True)
# Converte a Dummy binary (text) -----> to (1/0)
No_of_lanes_changed_at_the_approach3_Table = pd.get_dummies(inner_joint_Int["No_of_lanes_changed_at_the_approach3"], prefix="Arm4")
# inner_joint_Int["No_of_lanes_changed_at_the_approach3"] = 1 * (inner_joint_Int["No_of_lanes_changed_at_the_approach3"] == "Yes (it has changed)")
# =======================================================
# ===== Left_turn_only_lane_for_fourth_arm ========V48====
inner_joint_Int["Left_turn_only_lane_for_fourth_arm"].isnull().sum()
# The Fourth Arm is missing means this intersection is either T or Y shape
inner_joint_Int["Left_turn_only_lane_for_fourth_arm"].fillna("fourth_arm_is_not_existed", inplace=True)
Left_turn_only_lane_for_fourth_arm_Table = pd.get_dummies(inner_joint_Int["Left_turn_only_lane_for_fourth_arm"], prefix="Arm4")
# We will clean the column names to not have spaces
Left_turn_only_lane_for_fourth_arm_Table.columns = Left_turn_only_lane_for_fourth_arm_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
Left_turn_only_lane_for_fourth_arm_Table.columns = Left_turn_only_lane_for_fourth_arm_Table.columns.str.replace(' |-', '_')
# Converte a Dummy binary (text) -----> to (1/0)
# inner_joint_Int["Left_turn_only_lane_for_fourth_arm"] = 1 * (inner_joint_Int["Left_turn_only_lane_for_fourth_arm"] == "Exist")
# # =======================================================
# # ========= Right_turn_only_lane_for_fourth_arm ===V49====
# # =======================================================
inner_joint_Int["Right_turn_only_lane_for_fourth_arm"].isnull().sum()
inner_joint_Int["Right_turn_only_lane_for_fourth_arm"].fillna("fourth_arm_is_not_existed", inplace=True)
right_turn_only_lane_for_fourth_arm_Table = pd.get_dummies(inner_joint_Int["Right_turn_only_lane_for_fourth_arm"], prefix="Arm4")
# We will clean the column names to not have spaces
right_turn_only_lane_for_fourth_arm_Table.columns = right_turn_only_lane_for_fourth_arm_Table.columns.str.strip()
# Create a column name underscored by removing any spaces or (-)
right_turn_only_lane_for_fourth_arm_Table.columns = right_turn_only_lane_for_fourth_arm_Table.columns.str.replace(' |-', '_')
# # Converte a Dummy binary (text) -----> to (1/0)
# inner_joint_Int["Right_turn_only_lane_for_fourth_arm"] = 1 * (inner_joint_Int["Right_turn_only_lane_for_fourth_arm"] == "Exist")
# # # # === Width_of_Pysical_Median_of_third_arm_if_exist ====V39====
# # # # =======================================================
# inner_joint_Int["Width_of_Pysical_Median_of_third_arm_if_exist"].isnull().sum()
# inner_joint_Int["Width_of_Pysical_Median_of_third_arm_if_exist"].fillna(0, inplace=True)
# # We will create a variable for the physical median using np.where and converate it to a pandas-Series which
# # we will use join later to add it to our exited DataFrame (inner_joint_Int), notice I added also the index for matching.
# Is_there_Physical_Median_third_arm = pd.Series(np.where(inner_joint_Int["Width_of_Pysical_Median_of_third_arm_if_exist"] != 0, 1, 0), index=inner_joint_Int.index)
# # =======================================================
# # === Width_of_central_strip_of_third_arm_if_exist ======V40====
# # =======================================================

# # Check the missing values in your column
# inner_joint_Int["Width_of_central_strip_of_third_arm_if_exist"].isnull().sum()
# inner_joint_Int["Width_of_central_strip_of_third_arm_if_exist"].isnull().values.any()
# inner_joint_Int["Width_of_central_strip_of_third_arm_if_exist"].fillna(0, inplace=True)
# # Simliar to above lets create a dummy variable for all roads that have a central strip
# Is_there_centeral_strip_third_arm = pd.Series(np.where(inner_joint_Int["Width_of_central_strip_of_third_arm_if_exist"] != 0, 1, 0), index=inner_joint_Int.index)
# # =======================================================
# # = Pedestrian_and_bicycle_crossing_roadway_type2 ==V41===
# # =======================================================
# # This variable is categorical and has a problem, missing entry at 23-K06472-000
# inner_joint_Int["Pedestrian_and_bicycle_crossing_roadway_type2"].isnull().sum()
# print("Variable Pedestrian_and_bicycle_crossing_roadway_type2 of the third arm has no problem")
# print("Notice that the number (2) added in the end indicating the third arm")
# print("===================================================================")
# # Changing the Categorical Variable to the following:
# Pedestrian_and_bicycle_third_arm_Table = pd.get_dummies(inner_joint_Int["Pedestrian_and_bicycle_crossing_roadway_type2"], prefix="Arm3")
# # We will clean the column names to not have spaces
# Pedestrian_and_bicycle_third_arm_Table.columns = Pedestrian_and_bicycle_third_arm_Table.columns.str.strip()
# # Create a column name underscored by removing any spaces or (-)
# Pedestrian_and_bicycle_third_arm_Table.columns = Pedestrian_and_bicycle_third_arm_Table.columns.str.replace(' |-', '_')
# print(f"Check the Sum of Dummies equal to 1 using {Pedestrian_and_bicycle_third_arm_Table.describe().T.iloc[:,1].sum()}")
# print("===================================================================")
# k = inner_joint_Int["Pedestrian_and_bicycle_crossing_roadway_type2"].value_counts(normalize=True).sum()
# print(f"also for our main categorical variable before trasfered to dummies {k}")
# # ========================================================================
# # === Skewness_level_of_third_arm_to_the_next_arm ==V42==
# # ========================================================================
# inner_joint_Int["Skewness_level_of_third_arm_to_the_next_arm"].isnull().sum()
# inner_joint_Int["Skewness_level_of_third_arm_to_the_next_arm"].fillna("No (it is not skewed)", inplace=True)
# # Simliar to above lets create a dummy variable for all roads that have a central strip
# Is_there_centeral_Skewness_arm_three_fourth = 1 * (inner_joint_Int["Skewness_level_of_third_arm_to_the_next_arm"] == "Yes (it is skewed)")
# # =======================================================
# # =============== Sidewalk_type_First_Side2 =======V43====
# # =======================================================
# inner_joint_Int["Sidewalk_type_First_Side2"].isnull().sum()  # There is a missing value at 23-K06475-000
# inner_joint_Int["Sidewalk_type_First_Side2"].fillna("No sidewalk", inplace=True)
# # Changing the Categorical Variable to the following:
# Sidewalk_type_First_Side_third_arm_Table = pd.get_dummies(inner_joint_Int["Sidewalk_type_First_Side2"], prefix="Arm3_1stSide")
# # We will clean the column names to not have spaces
# Sidewalk_type_First_Side_third_arm_Table.columns = Sidewalk_type_First_Side_third_arm_Table.columns.str.strip()
# # Create a column name underscored by removing any spaces or (-)
# Sidewalk_type_First_Side_third_arm_Table.columns = Sidewalk_type_First_Side_third_arm_Table.columns.str.replace(' |-', '_')
# # =======================================================
# # =============== Sidewalk_type_Second_Side2 ======V42====
# # =======================================================
# inner_joint_Int["Sidewalk_type_Second_Side2"].isnull().sum()
# # Changing the Categorical Variable to the following:
# Sidewalk_type_Second_Side_third_arm_Table = pd.get_dummies(inner_joint_Int["Sidewalk_type_Second_Side2"], prefix="Arm3_2ndSide")
# # We will clean the column names to not have spaces
# Sidewalk_type_Second_Side_third_arm_Table.columns = Sidewalk_type_Second_Side_second_arm_Table.columns.str.strip()
# # Create a column name underscored by removing any spaces or (-)
# Sidewalk_type_Second_Side_third_arm_Table.columns = Sidewalk_type_Second_Side_second_arm_Table.columns.str.replace(' |-', '_')
# # # =============== Traffic_signal_contral_type2 ====V43====
# # # =======================================================
# inner_joint_Int["Traffic_signal_contral_type2"].isnull().sum()
# # Changing the Categorical Variable to the following:
# Traffic_signal_contral_type_third_arm_Table = pd.get_dummies(inner_joint_Int["Traffic_signal_contral_type2"], prefix="Arm3")
# # We will clean the column names to not have spaces
# Traffic_signal_contral_type_third_arm_Table.columns = Traffic_signal_contral_type_third_arm_Table.columns.str.strip()
# # Create a column name underscored by removing any spaces or (-)
# Traffic_signal_contral_type_third_arm_Table.columns = Traffic_signal_contral_type_third_arm_Table.columns.str.replace(' |-', '_')

# # # =============== Presence_of_pedestrian_traffic_signal2 ====V44====
# # # =======================================================
# inner_joint_Int["Presence_of_pedestrian_traffic_signal2"].isnull().sum()
# # Changing the Categorical Variable to the following:
# inner_joint_Int['Presence_of_pedestrian_traffic_signal2'] = 1 * (inner_joint_Int["Presence_of_pedestrian_traffic_signal2"] == "Exist")

# # ================ Template =================V0==========
# # =======================================================
# # Things to do: you need to drop the columns that you don't use.
# # inner_joint_Int.join(Sidewalk_type_First_Side_first_arm_Table)
# # You need to add a prefix to each arm variable to clarify.
# ==================================================#
#          Preparation to exprot the results
# ==================================================#

# Append all our finding so far in our final dataset
# Crash total count and age based Data
# ==============================================================================
'''
    df is the original dataset that we have from our firs survey with -U sensei,
        which contian all information regrading the crash drivers,speed,..etc.
        which started after the column number 42
'''
# ==============================================================================
# That was my mistake which copy only a reference to the original dataframe df = inner_joint_Int
df = inner_joint_Int.copy(deep = True)
df.drop(df.columns[42:len(df.columns)],axis=1, inplace =True)
# ==============================================================================
'''
    Step -1- Adding the Intersection Type Dummy variables. and remove the
                categorical variable "Intersection_type"
'''
df = df.join(Inters_type_Table)
#df.drop(["Intersection_type"], axis=1)
# ==============================================================================
'''
    Step -2- Number of driveways
'''
df = df.join(inner_joint_Int["Number_of_driverways"])
# ==============================================================================
'''
    Step -3- Distance to adjacent intersection within 500 meter.
'''
df = df.join(inner_joint_Int["Distance_to_adjacent_intersection_within_500_meter"])
# ==============================================================================
'''
    Step -4- Longest width of intersection
'''
df = df.join(inner_joint_Int["Longest_Width_of_intersection"])
# ==============================================================================
'''
    Step -5- Shortest width of intersection
'''
df = df.join(inner_joint_Int["Shortest_Width_of_intersection"])
# ==============================================================================
'''
    Step -6- Radius of between arms
'''
# There are 6 radiuses available in the dataframe whichare:
for column in range(len(List_Radius)):
    print(List_Radius)
    df = df.join(inner_joint_Int[List_Radius[column]])
# ==============================================================================
'''
    Step -7- Number of arms of the selected intersection
'''
# There are 6 radiuses available in the dataframe whichare:
df = df.join(Number_of_arms_Table)
# ==============================================================================
# ###################################################
# ###################################################
'''
    Variables for each arm - first arm
    Step -8- Road type for first arm - first arm.
'''
# There are 6 radiuses available in the dataframe whichare:
df = df.join(Road_type_for_first_arm_Table)
# ==============================================================================
'''
    Step -9- Number of lanes for first arm
'''
# There are 6 radiuses available in the dataframe whichare:
df = df.join(inner_joint_Int["Number_of_lanes_for_first_arm"])
# ==============================================================================
'''
    Step -10- No. of lanes changed at the approach - dummy
'''
# There are 6 radiuses available in the dataframe whichare:
df = df.join(inner_joint_Int["Arm1_No_of_lanes_changed_at_the_approach"])
# ==============================================================================
'''
    Step -11- Left turn only lane for first arm
'''
# There are 6 radiuses available in the dataframe whichare:
df = df.join(inner_joint_Int["Left_turn_only_lane_for_first_arm"])
# ==============================================================================
'''
    Step -12- Right turn only lane for first arm
'''
# There are 6 radiuses available in the dataframe whichare:
df = df.join(inner_joint_Int["Right_turn_only_lane_for_first_arm"])
# ==============================================================================
'''
    Step -13- Width of physical median of first arm
'''
# There are 6 radiuses available in the dataframe whichare:
# df = df.merge(Is_there_Physical_Median_first_arm.to_frame(), left_index=True, right_index=True)
# df = df.join(Is_there_Physical_Median_first_arm) This one is not working to join panda series with pandas dataframe. The above solution works only with V0.24.0 onwards, check using print(pd.__version__)
# Update it is working but not give a name for the column, so I need to coverate the series to a
# DataFrame object in panda.
df1 = pd.DataFrame(Is_there_Physical_Median_first_arm.rename("Is_there_Physical_Median_first_arm"))
df = df.join(df1)
# ==============================================================================
'''
    Step -14- Width of central strip of first arm dummy
'''
df2 = pd.DataFrame(Is_there_centeral_strip_first_arm.rename("Is_there_centeral_strip_first_arm"))
df = df.join(df2)
# ==============================================================================











# ==================================================#
#           Export the Final Results
# ==================================================#
Final_DataSet = df
# ---- Export as a xlsx file --------
# Final_DataSet.to_excel(Current_Path + "/Toyota_Survey_Sheetfiles/3_Results_Creating_dummies_cont/Final_DataSet.xlsx", sheet_name="Final_Dataset")
# ---- Export as a csv file --------
# Final_DataSet.to_csv(Current_Path + "/Toyota_Survey_Sheetfiles/3_Results_Creating_dummies_cont/Final_DataSet.csv", index = True)
# ===================================================
#       Functions that I used with my analysis
# ===================================================

def check_df(df,option = None):
    if option == 1:
        for index,column in enumerate(df.columns):
            print(index,column)
    elif option==2:
        print(df.describe().T)
    else:
        for index,column in enumerate(df.columns):
            print(index,column)
        print(50*'-')
        print(df.describe().T)
