"""
=========================================================
         This is cleaning program for the
            Toyota Survey Dataset.
=========================================================
    - We have deployed a survey for the ITARDA intersections
        located in Toyota City - the dataset is created through
        multiple Datasheet data collecation conducted by a sruvey
        group in our lab
    - Starting on Cleaning the Survey data, as there are about 7 files
        these files are Excell-Sheet files which we will use to join them to our
        current dataset survey that we have from the ITARDA DataSet.
    - Starting Date: Sat Apr. 6th 2019 17:30 at the Cafe Blanc.
"""

# ==================================================#
#           Import Libraries
# ==================================================#
# Load the Pandas libraries with alias 'pd'
import pandas as pd
import numpy as np
import os
Current_Path = os.getcwd()
# ==================================================#
#           Import Toyota Data Using Panda
# ==================================================#
# This time we will use the Excel Import Data where we can get all information in Japanese to clean them later.
# [1] Survey Plan [1-80]
# ExcelFiles = ["[1] Survey Plan [1-80]",
#               "[2] Survey Plan [81-160]",
#               "[3] Survey Plan [161-203]",
#               "[3] Survey Plan [203-240]",
#               "[4] Survey Plan [241-320]",
#               "[5] Survey Plan [321-400]",
#               "[6] Survey Plan [400-430]",
#               "[7] Survey Plan [431-482]"]

# Name = "SurveySheet"
# Survey_File_Names = []
# Survey_Files = [0] * len(ExcelFiles)
# for i in range(len(ExcelFiles)):
#   print(ExcelFiles[i])
#   Survey_File_Names.append(Name + f"{i}")
#   Survey_Files[i] = pd.read_excel(Current_Path
#                                   + f"/Toyota_Survey_Sheetfiles/{ExcelFiles[i]}.xlsx", sheet_name=0)
# ==================================================#
#               Example on Printing                 #
# ==================================================#
# df_row = pd.concat([Survey_Files[0], Survey_Files[3]])
# import random

# namecount = 5
# namelist=[]
# for i in range(0, namecount):
#   namelist.append(input("Please enter name %s:" % (i+1))) #Stored in namelist[i]

# nameindex = random.randint(0, namecount)
# print('Well done {}. You are the winner!'.format(namelist[nameindex]))
# ==================================================#

ExcelFiles = ["[1] Survey Plan [1-80]",
              "[2] Survey Plan [81-160]",
              "[3] Survey Plan [161-240]",
              "[4] Survey Plan [241-320]",
              "[5] Survey Plan [321-400]",
              "[6] Survey Plan [400-430]",
              "[7] Survey Plan [431-482]"]

# [1] Survey Plan [1-80]
SurveySheet_IntID_1 = pd.read_excel(Current_Path
                                    + f"/Toyota_Survey_Sheetfiles/1_Cleaning_Data_set/Survey_Data/{ExcelFiles[0]}.xlsx",
                                    sheet_name="Survey_Plan_1_81_Int")
# [2] Survey Plan [81-160]
SurveySheet_IntID_2 = pd.read_excel(Current_Path
                                    + f"/Toyota_Survey_Sheetfiles/1_Cleaning_Data_set/Survey_Data/{ExcelFiles[1]}.xlsx",
                                    sheet_name="Survey_Plan_81_160_Int")
# [3] Survey Plan [161-203]
SurveySheet_IntID_3 = pd.read_excel(Current_Path
                                    + f"/Toyota_Survey_Sheetfiles/1_Cleaning_Data_set/Survey_Data/{ExcelFiles[2]}.xlsx",
                                    sheet_name="Survey_Plan_161_240_Int")
# [4] Survey Plan [241-320]
SurveySheet_IntID_4 = pd.read_excel(Current_Path
                                    + f"/Toyota_Survey_Sheetfiles/1_Cleaning_Data_set/Survey_Data/{ExcelFiles[3]}.xlsx",
                                    sheet_name="Survey_Plan_241_320_Int")
# [5] Survey Plan [321-400]
SurveySheet_IntID_5 = pd.read_excel(Current_Path
                                    + f"/Toyota_Survey_Sheetfiles/1_Cleaning_Data_set/Survey_Data/{ExcelFiles[4]}.xlsx",
                                    sheet_name="Survey_Plan_321_400_Int")
# [6] Survey Plan [400-430]
SurveySheet_IntID_6 = pd.read_excel(Current_Path
                                    + f"/Toyota_Survey_Sheetfiles/1_Cleaning_Data_set/Survey_Data/{ExcelFiles[5]}.xlsx",
                                    sheet_name="Survey_Plan_400_430_Int")
# [7]Survey Plan [431-482]
SurveySheet_IntID_7 = pd.read_excel(Current_Path
                                    + f"/Toyota_Survey_Sheetfiles/1_Cleaning_Data_set/Survey_Data/{ExcelFiles[6]}.xlsx",
                                    sheet_name="Survey_Plan_431_482_Int")


frames = [SurveySheet_IntID_1, SurveySheet_IntID_2, SurveySheet_IntID_3, SurveySheet_IntID_4, SurveySheet_IntID_5, SurveySheet_IntID_6, SurveySheet_IntID_7]

Int_Survey_DataSet = pd.concat(frames)
Int_Survey_DataSet['Pedestrian_and_bicycle_crossing_roadway_type'].value_counts(normalize=True)

"""
=========================================================
        Printing the Percentage of each
      Cateogrical Variable in our dataset
=========================================================
    - Since we cant see the variables we are interested in
      if they are categorical using the method
        describe().T then we can use instead
        the method value_counts(normalize =True)
    - Here we will do the best option in our work.
"""
#Categorical_Columns = Int_Survey_DataSet.select_dtypes(exclude=["number", "bool_", "object_"])
#num_cols = Int_Survey_DataSet._get_numeric_data().columns
#num_cols = Int_Survey_DataSet.select_dtypes(include=['category'])
# Int_Survey_DataSet.select_dtypes(exclude=['int', 'float']).columns
cat_col = [c for i, c in enumerate(Int_Survey_DataSet.columns) if Int_Survey_DataSet.dtypes[i] in [np.object]]

num_cols = [key for key in dict(Int_Survey_DataSet.dtypes)
            if dict(Int_Survey_DataSet.dtypes)[key] in ['object']]  # Categorical Varible

for colum in range(len(num_cols)):
  print(Int_Survey_DataSet[f"{num_cols[colum]}"].value_counts(normalize=True))
# print(colum)
# ==================================================#
#           Descriptive Statistic in Panda
# ==================================================#
# If you want to print a specific Column
# print (data['ITARDA_crossing_ID'])
# SampleSize_Acc = len(Acc_ID_Data)
# SampleSize_Int = len(Int_ID_Data)
# # Data Description
# Acc_ID_Data.describe()
# Int_ID_Data.describe()
# # You can use the
# Acc_ID_Data.transpose()  # to change columns to rows
# # To see all columns in our Dataset
# Acc_ID_Data.columns
# # To see all rows in your dataset
# Acc_ID_Data.index
"""

=========================================================
        Join the Crash Dataset Combined together
            Old Dataset with new Survey Data
=========================================================
    - We will try to use the orginal dataset and combine
       the results with our current dataset.
    - The result will show a potential of speed, traffic
       volume and other dataset increbited for our current
       dataset including the geometry of all ITRDA observed
       Intersections.
    - We will use the method of Join in pandas
"""
# We will try to remove the white spaces in the end of each column
# Find a note here: https://stackoverflow.com/questions/41476150/removing-space-from-dataframe-columns-in-pandas
# result[result.isnull().any(axis=1)][0:]
# Remove white spaces from both ending of the string.

# for column_name in (result.columns):
#   print(column_name)
# # You can unzip all elements of your list using (*)
# print(*results.columns)

"""
=========================================================
        What Kind of Joint We are Looking For
=========================================================
    - Joint[1]:[LEFT] Here we will joint the two dataset based on
                the attribute "Left" which is the original
                dataset by Usui sensei.
    - Joint[2]:[INNER] This is the inner joint which means bring all
                intersections that intersect between our original
                dataset and the survey dataset.
    - Joint[3]:[OUTER] This is the outer join which means bring all
                intersections that available in first dataset and
                in second database and the intersected together.
                [This will help us to see how big our dataset can be
                 if we can count all the missing values in our dataset]
"""
#  Joint[1]:[LEFT]

# First upload the Original Databased from our previous analysis

Original_IntID = pd.read_excel(Current_Path
                               + f"/Toyota_Survey_Sheetfiles/1_Cleaning_Data_set/Data_Fusion/Pivot_table1.xlsx",
                               sheet_name="Pivot_table1")
# key = FilterLess35
#results = pd.merge(Original_IntID, Int_Survey_DataSet, how='left', left_on='FilterLess35', right_on='Intersection_ID ')
left_joint_Int = Original_IntID.merge(Int_Survey_DataSet, how='left', left_on='FilterLess35', right_on='Intersection_ID ')
# Remove white spaces from both ending of the string.
left_joint_Int.columns = left_joint_Int.columns.str.strip()

# Joint[2]:[INNER]
inner_joint_Int = Original_IntID.merge(Int_Survey_DataSet,
                                       how='inner',
                                       left_on='FilterLess35',
                                       right_on='Intersection_ID ')
# Remove white spaces from both ending of the string.
inner_joint_Int.columns = inner_joint_Int.columns.str.strip()

# Joint[3]:[OUTER]
outer_joint_Int = Original_IntID.merge(Int_Survey_DataSet,
                                       how='outer',
                                       left_on='FilterLess35',
                                       right_on='Intersection_ID ')
# Remove white spaces from both ending of the string.
outer_joint_Int.columns = outer_joint_Int.columns.str.strip()
# ==================================================#
#                Printing left_joint_Ints
# ==================================================#
left_joint_Int.to_excel(Current_Path + "/Toyota_Survey_Sheetfiles/1_Cleaning_Data_set/Results/left_joint_Int.xlsx", sheet_name="left_joint_Int")
inner_joint_Int.to_excel(Current_Path + "/Toyota_Survey_Sheetfiles/1_Cleaning_Data_set/Results/inner_joint_Int.xlsx", sheet_name="inner_joint_Int")
outer_joint_Int.to_excel(Current_Path + "/Toyota_Survey_Sheetfiles/1_Cleaning_Data_set/Results/outer_joint_Int.xlsx", sheet_name="outer_joint_Int")

Int_Survey_DataSet.to_excel(Current_Path + "/Toyota_Survey_Sheetfiles/1_Cleaning_Data_set/Data_Fusion/Int_Survey_dataSet_Combined.xlsx", sheet_name="Int_Survey_dataSet_Combined")
