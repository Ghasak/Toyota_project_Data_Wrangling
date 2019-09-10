"""
    We will Run now the program again this time we would do:
        - Assume intersection with more than one node (up to 6 nodes) will be assigned to one intersection (dictionary name)
        - This will be referected to count the crashes per intersections (the exact number of intersections)
        - Later when be aggregated in using Pivot-table will be more efficient way to represent these numbers.
        - The Number of intersections which are missing in our Survey and the one is being done extra will be exact.
    What we will need is a dataset of ITARDA intersections without Nodes renumbering,
    Also we need the to check the distance if its performed over all intersections and checked later with the one with nodes.
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

Acc_ID_Data = pd.read_excel("1_Accident_1019_zeroITARDA_Not_Removed.xlsx", sheet_name=0)
Int_ID_Data = pd.read_excel("2_Intersection_ID_No_Nodes.xlsx", sheet_name=0)
# ==================================================#
#           Descriptive Statistic in Panda
# ==================================================#
# If you want to print a specific Column
# print (data['ITARDA_crossing_ID'])
SampleSize_Acc = len(Acc_ID_Data)
SampleSize_Int = len(Int_ID_Data)
# Data Description
Acc_ID_Data.describe()
Int_ID_Data.describe()
# You can use the
Acc_ID_Data.transpose()  # to change columns to rows
# To see all columns in our Dataset
Acc_ID_Data.columns
# To see all rows in your dataset
Acc_ID_Data.index


# ==================================================#
#   Distance Function (considering Curvature of earth)
# ==================================================#

def measure(lat1, lon1, lat2, lon2):
    """
        This function calculate the distance between to points on the Earth Surface considering
            the curvture of the earth.
            - the Latitude and Longitude should be measured in DD (Degree-Decimal).
            - Website :
                https://stackoverflow.com/questions/639695/how-to-convert-latitude-or-longitude-to-meters
                Formula :https://en.wikipedia.org/wiki/Haversine_formula
    """
    R = 6378.137        # Radius of Earth in Km
    dlat = (lat2 - lat1) * (np.pi / 180)
    dlon = (lon2 - lon1) * (np.pi / 180)
    a = (np.sin(dlat / 2) * np.sin(dlat / 2)) + (np.cos(lat1 * np.pi / 180) * np.cos(lat2 * np.pi / 180)) * (np.sin(dlon / 2) * np.sin(dlon / 2))
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    d = R * c
    return (d * 1000)     # distance in meter
    # Tested with
    # measure(35.07121056, 137.1518367,35.07110167, 137.147385)
    # measure(x[13][0],x[13][1],x[12][0],x[12][1]) = 12.844 meter
# =======================================================#
#   Distance Function (Not considering Curvtuer of earth)
# =======================================================#


def ecluidianDist(lat1, lon1, lat2, lon2):
    """
        This function calculate the distance between to points on the Earth Surface not considering
            the curvature of the earth.
            - the Latitude and Longitude should be measured in DD (Degree-Decimal).
            - The approximation of the Long and lat factors are obtained from :
                https://s-giken.info/distance/distance.php
    """
    deltalat = (np.float(lat2) - np.float(lat1)) * 110.9463
    deltalong = (np.float(lon2) - np.float(lon1)) * 90.4219
    dist1 = np.sqrt(np.power(lon2 - lon1, 2) + np.power(lat2 - lat1, 2))
    dist2 = np.float(np.linalg.norm([deltalat, deltalong]))
    return np.float(dist2 * 1000)    # return a tuple(('Using np.qrt =',dist1,'Using np.linalg =',dist2))


# --------------------------------------------------
# Test of the two formula
measure(35.07110167, 137.147385, 35.07231811, 137.1519749)
ecluidianDist(35.07110167, 137.147385, 35.07231811, 137.1519749)

# ==================================================#
#           Accessing Data in Panda
# ==================================================#

Acc_ID_Data_indexed = Acc_ID_Data.set_index(['Acc_ID'])
Int_ID_Data_indexed = Int_ID_Data  # .set_index(['ITARDA'], verify_integrity=False)

"""
    First Navigate the Variables of Intereset Location
        - You will call the Columns LONGITUDE and LATITUDE in the (Int_ID_Data_indexed)
        - You will call the Columns Longitude_base-10_ and Latitude_base-10_ in the (Acc_ID_Data_indexed)

"""
Acc_ID_Data_indexed.rename(columns={'Latitude（base-10）': 'Latitudex', 'Longitude（base-10）': 'Longitudex'}, inplace=True)

# --------------------------------------------------
"""
        [- Continue working Wed March 6th 13:36:36]
        Here will add three filters to identify the distance range (35 meter, 50 meter,75 meter,100 meter)
            - There filters will be measure from the Intersection longitude and latitude to each accident
            -
"""
Intersection_Dict = {}
# n = 1019 # How many Intersections n < 1019 intersection of your intersection database.
for s in range(len(Int_ID_Data_indexed)):
    Intersection_Dict[Int_ID_Data_indexed.index[s]] = np.zeros(len(Acc_ID_Data.index))

# Declare my dictionary (later it will have 1000 Intersection)
Distance = pd.DataFrame(Intersection_Dict, index=(Acc_ID_Data_indexed.index), columns=Int_ID_Data_indexed.iloc[:, 1])
Distance.fillna(0, inplace=True)
Filter10 = pd.Series(0, index=Acc_ID_Data_indexed.index)
Filter20 = pd.Series(0, index=Acc_ID_Data_indexed.index)
Filter30 = pd.Series(0, index=Acc_ID_Data_indexed.index)
Filter50 = pd.Series(0, index=Acc_ID_Data_indexed.index)
Filter75 = pd.Series(0, index=Acc_ID_Data_indexed.index)
Filter100 = pd.Series(0, index=Acc_ID_Data_indexed.index)
for q in range(len(Int_ID_Data_indexed.LATITUDE)):
    ##!clear
    print(" Intersection No. {}".format(q))
    for i in range(len(Acc_ID_Data_indexed.Latitudex)):
        Distance.iloc[i][q] = measure(Int_ID_Data_indexed.LATITUDE[q],
                                      Int_ID_Data_indexed.LONGITUDE[q],
                                      Acc_ID_Data_indexed.Latitudex.iloc[i],
                                      Acc_ID_Data_indexed.Longitudex.iloc[i])
        if Distance.iloc[i][q] < int(10):
            Filter10.iloc[i] = Int_ID_Data_indexed.index[q]
        elif Distance.iloc[i][q] < int(20):
            Filter20.iloc[i] = Int_ID_Data_indexed.index[q]
        elif Distance.iloc[i][q] < int(35):
            Filter30.iloc[i] = Int_ID_Data_indexed.index[q]
        elif Distance.iloc[i][q] < int(50):
            Filter50.iloc[i] = Int_ID_Data_indexed.index[q]
        elif Distance.iloc[i][q] < int(75):
            Filter75.iloc[i] = Int_ID_Data_indexed.index[q]
        elif Distance.iloc[i][q] < int(100):
            Filter100.iloc[i] = Int_ID_Data_indexed.index[q]
        else:
            continue
# --------------------------------------------------
"""
        [- How to Sort the rows of your distance from smaller to bigger distances]
        This algorithm is to find the closest distance to each intersection
            - There filters will be measure from the Intersection longitude and latitude to each accident.
"""
Filtered_Data = pd.DataFrame({'Filter10': Filter10,
                              'Filter20': Filter20,
                              'Filter30': Filter30,
                              'Filter50': Filter50,
                              'Filter75': Filter75,
                              'Filter100': Filter100})
# Is it possible to add a DataFrame to another DataFrame [as Column], as Row I found (concat method)
# https://stackoverflow.com/questions/19866377/is-it-possible-to-add-several-columns-at-once-to-a-pandas-dataframe
Acc_ID_Final = Acc_ID_Data_indexed.assign(**Filtered_Data)


# Suspicious Intersections
# Here we will use the query to do that,
Acc_ID_Final.query("Filter10 != 0 and Filter20 != 0")

# Lets see how many intersections we have now in our current data Frame
# Assume up to Filter30,
Filtered_Data.query("Filter30 != 0")
# https://stackoverflow.com/questions/31306741/unmelt-pandas-dataframe
# http://wesmckinney.com/blog/fast-and-easy-pivot-tables-in-pandas-0-5-0/

# --------------------------------------------------
"""
        [- How to count the intersections based on Distance not Using Filters]
        The output for both the Distances and for the Accident final Dataset.
            - I have created a DataFrame Called [TopFive], based on Pandas, this would give us
                as many as columns you want to filter your distance based on nearest intersection.
            - This Algorithm takes some times, we would like to confirm later with larger dataset.
"""

# Suspicious Intersections
Distance['23-K05617-000'][Distance['23-K05617-000'] < 30]
# How to sort the values in maximum order using the rows up to 2 intersections.
Distance.iloc[0][:].sort_values(ascending=True)[:2]
# ==================================================#
#          Filtering based on Distance
# ==================================================#

List_Int_Name = []
# How many Columns You want to Filter
F = 5
for k in range(2 * F):
    if k < F:
        List_Int_Name.append('Intersection{}'.format(k + 1))
    else:
        List_Int_Name.append('Distance{}'.format(k - F + 1))

Distance_Dict = {}
for s in range(2 * F):
    Distance_Dict[List_Int_Name[s]] = 0 * len(Acc_ID_Data_indexed.index)
# Lets create a DataFrame with keys are Intersection[1:5] and Distances[1:5]
# this is from Pandas Frame, which gives us a zero value of 2870 [len(TopFive)],
# and give you: len(TopFive.columns) 10 columns.
TopFive = pd.DataFrame(Distance_Dict, index=(Acc_ID_Data_indexed.index))
# populate the DataFrame with our results from the Distance measured.
for acc in range(len(TopFive)):
    #!clear
    print(" Accident No. {}".format(acc))
    TopFive.iloc[acc, 0:F] = Distance.iloc[acc, 0:].sort_values(ascending=True)[:F].keys()
    TopFive.iloc[acc, F:] = Distance.iloc[acc, 0:].sort_values(ascending=True)[:F].values[:]
# Lets add our results of TopFive to our Final Crash Dataset output
Acc_ID_Final = Acc_ID_Final.assign(**TopFive)
# ==================================================#
#          Queries for our TopFive Dataset
# ==================================================#
# Now we will perform the query to obtain the Toptwo distances with less than 30 meter
TopFive.query("(Intersection1 == '23-K11902-000')")  # Example of clustering correctly.
TopFive.query("(Distance1 < 30) and (Distance2 <30)")
TopFive.query("(Intersection1 == '23-K51139-100') and (Intersection2 =='23-K52413-200')")
TopFive.query("(Intersection1 == '23-K51139-100') or (Intersection2 =='23-K51139-100')")
# Get a specific Crash based on Crash ID using Fancy Indexing
TopFive.iloc[TopFive.index[:] == 22]


# ==================================================#
#          Refine the Accidents for Matching
# ==================================================#
# --------------------------------------------------
"""
        We will use two criteria to allocate the intersection label to the specific accident
        in our dataset, these criterias are shown as:
            - Select the nearest distance among the distance 1 and distance 2.
            - Select the distance of less than 35 meter
            - Select teh distance between 35 and 50 meters.
            - We will first trying to make an example for 5 elements
"""
# - < Example >
# From this example you will notice that its working but gives NaN to the missing criteria rows
X = TopFive.iloc[0:5, 0:]
Y = X.query("Distance1 < 100")
Xnew = X.assign(**Y)

# the above example cannot work if we want to add more criterias.
# the solution is to loop over all accidents


Acc_Dict1 = {}
Acc_Dict2 = {}
Acc_Dict1["Selected_Intersection_Less35"] = np.zeros(len(Acc_ID_Data_indexed.index))
Acc_Dict2["Selected_Intersection_Less50"] = np.zeros(len(Acc_ID_Data_indexed.index))
# You can create pd.Series too but I prefer to make DataFrame (SpreadSheet) as it gives you the dictionary name as column.
Desginated_Intersection_Less35 = pd.DataFrame(Acc_Dict1, index=(Acc_ID_Data_indexed.index))
Desginated_Intersection_less50 = pd.DataFrame(Acc_Dict2, index=(Acc_ID_Data_indexed.index))
count_cases = 0
for acc in range(len(TopFive)):       # For debugging TopFive.iloc[0:5,0:]
    if TopFive.iloc[acc].loc["Distance1"] < 35:
        Desginated_Intersection_Less35.iloc[acc] = TopFive.iloc[acc].loc["Intersection1"]
    elif (TopFive.iloc[acc].loc["Distance1"] < 50):   # (TopFive.iloc[acc].loc["Distance1"] > 35) and
        Desginated_Intersection_less50.iloc[acc] = TopFive.iloc[acc].loc["Intersection1"]
    else:
        ##!clear
        count_cases = count_cases + 1
        print("Accidents not meeting our Criteria {}".format(count_cases))
        print("=================================")
        continue

FinalSelection = pd.DataFrame({'FilterLess35': Desginated_Intersection_Less35.Selected_Intersection_Less35,
                               'FilterLess50': Desginated_Intersection_less50.Selected_Intersection_Less50})
print(" Accidents with Number of crashes located less than 35 meter is ={} out of {}".format(len(TopFive) - len(FinalSelection.query("FilterLess35 != 0")), len(TopFive)))
print("=================================")
print(" Accidents with Number of crashes located less than 50 meter is ={} out of {}".format(len(TopFive) - len(FinalSelection.query("FilterLess50 != 0")), len(TopFive)))
Acc_ID_Final = Acc_ID_Final.assign(**FinalSelection)


# print(acc)
# TopFive.iloc[0:5,5:].min(axis = 1)


"""
        Exporting Our Results [- Output of our Cleaned Data]
        The output for both the Distances and for the Accident final Dataset.
            - Calling the main directory and attach it to a subfolder for transformability folders.
"""
import os
Current_Path = os.getcwd()
Distance.to_csv(Current_Path + "/Results3/Distance.csv", sep='\t')
TopFive.to_csv(Current_Path + "/Results3/TopFive.csv", sep='\t')
Acc_ID_Final.to_csv(Current_Path + "/Results3/Acc_ID_Final.csv", sep='\t')


# Export to Check,
Table56 = TopFive.query("(Distance1 < 35) and (Distance2 <35)")
Table56.to_csv(Current_Path + "/Results3/Table56.csv", sep='\t')


# Export as an Excel Sheet File
Acc_ID_Final.to_excel(Current_Path + "/Results3/Acc_ID_Final.xlsx", sheet_name="Acc_ID_Final")
Distance.to_excel(Current_Path + "/Results3/Distance.xlsx", sheet_name="Distance")
TopFive.to_excel(Current_Path + "/Results3/TopFive.xlsx", sheet_name="TopFive")

# ==================================================#
#          Pivot Table Analysis of Final Data
# ==================================================#
# --------------------------------------------------
"""
        As we proced with the data analysis we will conduct an anaylsis using Pandas Pivot_table:
            - Construct here the Cross-sectional Dataset with considering the indexing
"""

# getting an overview of our data
print("Our data has {0} rows and {1} columns".format(Acc_ID_Final.shape[0], Acc_ID_Final.shape[1]))
# checking for missing values
print("Are there missing values? {}".format(Acc_ID_Final.isnull().any().any()))
Acc_ID_Final.describe()


# -------------Cross Sectional Analysis------------------

pd.pivot_table(Acc_ID_Final, index=["FilterLess35"])

Acc_ID_Final.rename(columns={'12h_traffic_volume（100台）': 'Traffic'}, inplace=True)

# How to apply columns to your data
pd.pivot_table(Acc_ID_Final, index=["FilterLess35"], columns=["Age_Group"],
               values=['Traffic'],
               aggfunc=[len, np.max], fill_value=0)

# How to apply a filter to your Data
pd.pivot_table(Acc_ID_Final[Acc_ID_Final['Age_Group'] == '一般'], index=["FilterLess35"],  # columns =["Age_Group"],
               values=['Traffic'],
               aggfunc=[len, np.max], fill_value=0)

# -------------Panel Sectional Analysis------------------
# I cant make the years show repreatly the same length, in Excel there is functiont to do so,

pd.pivot_table(Acc_ID_Final[Acc_ID_Final['Age_Group'] == '一般'], index=["FilterLess35", "Year"],  # columns =["Age_Group"],
               values=['Traffic'],
               aggfunc=[len, np.max],fill_value=0,)
               #dropna=False)

Panel_Data = pd.pivot_table(Acc_ID_Final[Acc_ID_Final['Age_Group'] == '一般'],
               index=["FilterLess35",pd.Grouper(key="Year")],  # columns =["Age_Group"],
               values=['Traffic'],
               aggfunc=[len, np.max],fill_value=0,)
               #dropna=False)


# Here is the working Method that I tried

Panel_Data = Panel_Data.unstack()

# Not sure this method is correct.
year_index = [2006+i for i in range(10)]
Panel_Data.reset_index(inplace = True)
years_index = pd.DataFrame({'Year_New_Index':year_index}, index = year_index)
Merge1 = pd.merge(Panel_Data, years_index, left_on='Year', right_on='Year_New_Index')
Merge1.to_excel(Current_Path + "/Results3/Merge1.xlsx", sheet_name="Merge1")


# This is a bit easier way to do same
Panel_Data=Panel_Data.unstack().T.stack()
# Or this method much better
Panel_Data = Panel_Data.unstack().T
# Then
Panel_Data.unstack().T.melt()
Panel_Data.to_excel(Current_Path + "/Results3/Panel_Data.xlsx", sheet_name="Panel_Data")
