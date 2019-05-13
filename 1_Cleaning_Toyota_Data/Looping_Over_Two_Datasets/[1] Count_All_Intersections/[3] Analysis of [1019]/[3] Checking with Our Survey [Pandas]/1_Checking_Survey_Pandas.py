"""
    The work here is to verify the number of intersections that we obtained from new calculation
    wiht the one we are doing by conducting the Survey to obtain what is missing and what is
    doing as extra.
    - Files are in Excel format,
    - The results of this has shown that there are 185 intersections not included in our current dataset
    - and Our Survey Unit now are Conducting Data Collection of  intersections only.
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

ITARDA = pd.read_excel("All_1018_Intersections.xls", sheet_name=0)
Survey_554 = pd.read_excel("Our_554_Intersections.xls", sheet_name=0)
Survey_482 = pd.read_excel("Our_482_Intersections.xlsx", sheet_name=0)

# ==================================================#
#      Missing Intersection ID in Our Survey Unit
# ==================================================#
"""
There are several ways to put two or more dataframe side by side we will use.
    <1> - Merage Method [Merge To Dataset in Column ], with and without setting index.
            The purpose here is to get a dataset with information about longitude and latitude
            and node from the original dataset of all intesections in Toyota.
            (this is after we found these 554 intersections)
    <2> - You can use also merge instead of join (and add how ='left','right','inner', 'outer'), the
            results should be same,
"""
# <1> -

# Joint them based on Column names
Merge1 = pd.merge(ITARDA, Survey_554, left_on='ITARDA', right_on='Intersection ID')
# if you want to join them based on index then

ITARDA = ITARDA.set_index(['ITARDA'])
Survey_554 = Survey_554.set_index(['Intersection ID'])
Merge2 = pd.merge(ITARDA, Survey_554, left_index=True, right_index=True)

# Now we will check that these intersections of Survey_554 are included in Survey_482
# We will use the indexed Merge (Merge2)
#
# Merge_554_482 = pd.merge(Merge2, Survey_482, left_index = True, right_index = True)

# Now we will look into the Intersections which are located in both sets (554 and 482)
# I selected (left) because we need to find a table same length to the 554 (left table) that
# some of its intersections are missing in the 482 (right table).
Survey_482 = Survey_482.set_index(['ITARDA'])
test1 = Merge2.join(Survey_482, lsuffix='_caller', rsuffix='_other', how='left')

# The Values that are not available means these intersections are not included in the 482 Survey set.
Missing_From_482 = test1[test1.isnull().any(axis=1)][0:]

"""
        Exporting Our Results [- Output of our Cleaned Data]
        The output for both the Distances and for the Accident final Dataset.
            - Calling the main directory and attach it to a subfolder for transformability folders.
"""
import os
Current_Path = os.getcwd()
Missing_From_482.to_excel(Current_Path + "/Results2/Missing_From_482.xlsx", sheet_name="Missing_From_482")


# ==================================================#
#     What Our Survey Unit are conducting Extra
# ==================================================#
"""
It is clearly the
    <1> - We will do the same and obtain the Extra intersections that available in the 482 data set
            [left table] and not available in the 554 right table, which means we dont need them and
            they are extra.
"""

Extra_Inters = Survey_482.join(Merge2, lsuffix='_caller', rsuffix='_other', how='left')
Extra_in_482 = Extra_Inters[Extra_Inters.isnull().any(axis=1)][0:]
Extra_in_482.to_excel(Current_Path + "/Results2/Extra_in_482.xlsx", sheet_name="Extra_in_482")
