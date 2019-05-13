# ==================================================#
#           Import Libraries                
# ==================================================#
# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import numpy as np 

# ==================================================#
#           Import Toyota Data Using Panda                  
# ==================================================#
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
Acc_ID_Data = pd.read_csv("2_Accident_482_zeroITARDA_Removed.csv") 
Int_ID_Data = pd.read_csv("Intersection_482_Usui_Data.csv")   
# You need to set the directory to (/Users/ghasak/Desktop/1_Cleaning_Toyota_Data/Python_Cleaning/)
# if you open your ipython not inside your folder where you can get the .csv file (working Direcotry)
# Preview the first 5 lines of the loaded data 
Int_ID_Data.head()
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
Acc_ID_Data.transpose() # to change columns to rows
# To see all columns in our Dataset
Acc_ID_Data.columns
# To see all rows in your dataset
Acc_ID_Data.index

# ==================================================#
#   Distance Function (considering Curvtuer of earth)                   
# ==================================================#

def measure(lat1,lon1,lat2,lon2):
    """
        This function calculate the distance between to points on the Earth Surface considering
            the curvture of the earth. 
            - the Latitude and Longitude should be measured in DD (Degree-Decimal).
            - Website :
                https://stackoverflow.com/questions/639695/how-to-convert-latitude-or-longitude-to-meters
                Formula :https://en.wikipedia.org/wiki/Haversine_formula
    """ 
    R = 6378.137        # Radius of Earth in Km
    dlat = (lat2-lat1)*(np.pi/180)
    dlon = (lon2-lon1)*(np.pi/180)
    a = (np.sin(dlat/2)*np.sin(dlat/2))+(np.cos(lat1*np.pi/180)*np.cos(lat2*np.pi/180))*(np.sin(dlon/2)*np.sin(dlon/2))
    c = 2 * np.arctan2(np.sqrt(a),np.sqrt(1-a))
    d = R*c

    return (d*1000)     # distance in meter
    # Tested with 
    # measure(35.07121056, 137.1518367,35.07110167, 137.147385) 
    # measure(x[13][0],x[13][1],x[12][0],x[12][1]) = 12.844 meter
# =======================================================#
#   Distance Function (Not considering Curvtuer of earth)                   
# =======================================================#
def ecluidianDist(lat1,lon1,lat2,lon2):
    """
        This function calculate the distance between to points on the Earth Surface not considering
            the curvture of the earth. 
            - the Latitude and Longitude should be measured in DD (Degree-Decimal).
            - The approximation of the Long and lat factors are obtained from :
                https://s-giken.info/distance/distance.php
    """
    deltalat  = (np.float(lat2)-np.float(lat1))*110.9463
    deltalong = (np.float(lon2) -np.float(lon1))*90.4219
    dist1 = np.sqrt(np.power(lon2-lon1,2)+np.power(lat2-lat1,2)) 
    dist2 = np.float(np.linalg.norm([deltalat,deltalong]))
    return np.float(dist2*1000)    # return a tuple(('Using np.qrt =',dist1,'Using np.linalg =',dist2))
# --------------------------------------------------
# Test of the two formula
measure(35.07110167,137.147385,35.07231811,137.1519749) 
ecluidianDist(35.07110167,137.147385,35.07231811,137.1519749) 

# ==================================================#
#           Accessing Data in Panda                     
# ==================================================#

Acc_ID_Data_indexed = Acc_ID_Data.set_index(['Acc_ID'])
Int_ID_Data_indexed = Int_ID_Data.set_index(['ITARDA'])

"""
    First Navigate the Variables of Intereset Location
        - You will call the Columns LONGITUDE and LATITUDE in the (Int_ID_Data_indexed)
        - You will call the Columns Longitude_base-10_ and Latitude_base-10_ in the (Acc_ID_Data_indexed)

"""
# Lets try to call them first
Int_ID_Data_indexed.transpose() # it is better to see all the columns as rows so you can choose the name correctly
Int_ID_Data_indexed.LONGITUDE['23-K05867-000'] # this will bring you the LONGITUDE of Intersection loction [23-K05867-000]
# You can achieve the same thing as:
Int_ID_Data_indexed.LONGITUDE[0]     # indexed by 0 and 1 for our current database [0] ==>23-K05867-000 and [1] ==>23-K06431-000
# We will proceed to the other using the key much better

Int_ID_Data_indexed.LONGITUDE[0]
Int_ID_Data_indexed.LATITUDE[0]

# Acc_ID_Data_indexed.Longitude_base-10_[0]   # this kind of name is wrong Python doesnt accept (-) or (_ without attached word)
# Acc_ID_Data_indexed.Latitude_base-10_[0]
# --------------------------------------------------
"""
    This problem need to be solved
        - We will apply the function (rename) we dont need to change everything only the one we want to alter.
        - in our case they are the Longitude_base-10_ and Latitude_base-10_ these two names will be chagned into
            Latitudex and Longitudex.
        - Notice that we have used the function inplace = Ture which is to change the original database
            (Acc_ID_Data_indexed).

"""
# already named
Acc_ID_Data_indexed.rename(columns = {'Latitude':'Latitudex','Longitude':'Longitudex'}, inplace =True) 
# Now we can call the columns that we want
Acc_ID_Data_indexed.Latitudex[0]
Acc_ID_Data_indexed.Latitudex[0]
# --------------------------------------------------
"""
        [This problem Sometimes it occurs and sometimes not to my current dataset if its not working use .loc[]]
    TypeError: '<' not supported between instances of 'str' and 'int'
    - This error happen for the Acc_ID_Data_indexed because there are a letter in it (A) for
        actor type and (male/female) for sex column
    - The bulit in functions in Pandas cannot loop if one of the columns has name, this problem 
        was not occuring in the (Int_ID_Data_indexed) where all the data are numericals.
    - [Solution <1>] You can solve this problem by changin the column with names to another datatype [Pending]
    - [Solution <2>] Other solution is to use (iloc) to index this column
"""
# To see what kind of Data type I have for each column
Acc_ID_Data_indexed.dtypes
# We will apply now the [Solution <2>]
Acc_ID_Data_indexed.Longitudex.iloc[0]      # This is the longitude of first crash in the Acc_ID_Data_indexed.
Acc_ID_Data_indexed.Latitudex.iloc[0]       # This is the Latitudex of first crash in the Acc_ID_Data_indexed.

# You can achieve the same if you use the loc
# --------------------------------------------------

"""
    We will start Measuring the Distance between our inersection and each accident.
    - For start we will make a loop for all accidents without pay attention to their ID
    - The problem with this algorithm it will not stop and will measure all the distances
       even for the second intersection [See below]

"""
# Lets Calculate the Distance between the First intersection location and our first accident

Dist1 = measure(Int_ID_Data_indexed.LATITUDE[0], 
Int_ID_Data_indexed.LONGITUDE[0], Acc_ID_Data_indexed.Latitudex.iloc[0], Acc_ID_Data_indexed.Longitudex.iloc[0])
# --------------------------------------------------
# Lets loop now over all the crashes we are having in Acc
    
Distance = pd.Series(0,index=Acc_ID_Data_indexed.index)
for i in range(len(Acc_ID_Data_indexed.Latitudex)):
    Distance[i]=measure(Int_ID_Data_indexed.LATITUDE[0], 
                                Int_ID_Data_indexed.LONGITUDE[0], 
                                Acc_ID_Data_indexed.Latitudex.iloc[i], 
                                Acc_ID_Data_indexed.Longitudex.iloc[i])
# --------------------------------------------------
# Now if we want to get over each intersection we write [Also wrong check it]
# This loop takes around 30 mins to finish

for q in range(len(Int_ID_Data_indexed.LATITUDE)):
    !clear
    print(" Intersection No. {}".format(q))
    for i in range(len(Acc_ID_Data_indexed.Latitudex)):
        Distance[i]=measure(Int_ID_Data_indexed.LATITUDE[q], 
                                    Int_ID_Data_indexed.LONGITUDE[q], 
                                    Acc_ID_Data_indexed.Latitudex.iloc[i], 
                                    Acc_ID_Data_indexed.Longitudex.iloc[i])
  
# --------------------------------------------------
# To know the index that we will use for comparison later we can d
Int_ID_Data_indexed.index[0]    # Bring you the name of the intesection.
Acc_ID_Data_indexed.index[0]    # Bring you the name of the Accident.
# --------------------------------------------------
#                   [Working]
#       Lets put now the two loops 
# --------------------------------------------------

for q in range(len(Int_ID_Data_indexed.LATITUDE)):
        for i in range(len(Acc_ID_Data_indexed.Latitudex)):
            if (Int_ID_Data_indexed.index[q]==Acc_ID_Data_indexed.index[i]):
                Distance[i]=measure(Int_ID_Data_indexed.LATITUDE[q], 
                                            Int_ID_Data_indexed.LONGITUDE[q], 
                                            Acc_ID_Data_indexed.Latitudex.iloc[i], 
                                            Acc_ID_Data_indexed.Longitudex.iloc[i])

# --------------------------------------------------
#                   [Working]
#       How about create a new column and assign the intesection ID to the accident
#       if it meets the 35 meter criteria. 
# --------------------------------------------------

for q in range(len(Int_ID_Data_indexed.LATITUDE)):
    !clear
    print(" Intersection No. {}".format(q)) 
    for i in range(len(Acc_ID_Data_indexed.Latitudex)):
        if (Int_ID_Data_indexed.index[q]==Acc_ID_Data_indexed.index[i]):
            Distance[i]= measure(Int_ID_Data_indexed.LATITUDE[q], 
                                        Int_ID_Data_indexed.LONGITUDE[q], 
                                        Acc_ID_Data_indexed.Latitudex.iloc[i], 
                                        Acc_ID_Data_indexed.Longitudex.iloc[i])
            if ((Distance.iloc[i]) < int(35)): # As you can see Distance is a Pandas Series with two columns now so you 
                                                # have to loop over the values not the index thats why I use iloc
                print("Ok",i,Distance.iloc[i],Int_ID_Data_indexed.index[q])
            else:
                continue
# --------------------------------------------------
"""
                                    [Working Pefectly]
        We will Make here a new column and add it to our database (Acc_ID_Data_indexed)
            - This will be filtered later in Excel or we can use pivot in Pandas.
            - Now the accidents with matching id between the accident and intesection with 
                less than (35) meter distance assign the intesection name to this accidetn 
                and skip otherwise.
            - Assign the new Column you created to your original dataset of intesections.

"""
Intersection_ID_Assigned_to_Acc = pd.Series(0,index=Acc_ID_Data_indexed.index)
for q in range(len(Int_ID_Data_indexed.LATITUDE)):
    !clear
    print(" Intersection No. {}".format(q)) 
    for i in range(len(Acc_ID_Data_indexed.Latitudex)):
        if (Int_ID_Data_indexed.index[q]==Acc_ID_Data_indexed.index[i]):
            Distance[i]= measure(Int_ID_Data_indexed.LATITUDE[q], 
                                        Int_ID_Data_indexed.LONGITUDE[q], 
                                        Acc_ID_Data_indexed.Latitudex.iloc[i], 
                                        Acc_ID_Data_indexed.Longitudex.iloc[i])
            if ((Distance.iloc[i]) < int(35)): # As you can see Distance is a Pandas Series with two columns now so you 
                                                # have to loop over the values not the index thats why I use iloc
                print("Ok",i,Distance.iloc[i],Int_ID_Data_indexed.index[q])
                Intersection_ID_Assigned_to_Acc[i]=Int_ID_Data_indexed.index[q]
            else:
                continue


# Lets create now our final database
Acc_ID_Data_indexed['NewColumn'] =Intersection_ID_Assigned_to_Acc
# --------------------------------------------------
"""
                [Working So far distane of Three intesections or Q intersections]
        As Yamamoto sensei have informed me recently, Use this Algorithm
            - The above alogrithm will calculate the distance not across all the accidents in 
                the database rather than matched only [based on the Acc_ID_Data_indexed ID by 
                Usui sensei]. Now what I will do is:
            - Calcualte the distance between an intersection and every accident in the 
                the database of accident which means
            - Calculate the distance between an intersection q from the Int_ID_Data_indexed
                and every accident i in Acc_ID_Data_indexed [no need to match their indecies]
            - This procedure can be used for any crash dataset if you just know the long and lat
                of the intersection in your city and the location of each accident.
"""
# This Block is working for only Three intersections. 
Intersection_ID_Assigned_to_Acc = pd.Series(0,index=Acc_ID_Data_indexed.index)
Distance = pd.DataFrame({'Intersection1':0*len(Acc_ID_Data_indexed.index),
                         'Intersection2':0*len(Acc_ID_Data_indexed.index),
                         'Intersection3':0*len(Acc_ID_Data_indexed.index)},
                        index=(Acc_ID_Data_indexed.index))
for q in range(len(Int_ID_Data_indexed.LATITUDE)):
    for i in range(len(Acc_ID_Data_indexed.Latitudex)):
            Distance.iloc[i][q]= measure(Int_ID_Data_indexed.LATITUDE[q], 
                                        Int_ID_Data_indexed.LONGITUDE[q], 
                                        Acc_ID_Data_indexed.Latitudex.iloc[i], 
                                        Acc_ID_Data_indexed.Longitudex.iloc[i])
            
# If you want to increase to (Q) Intersection

# Here I will create a Dictionary with an (Q) intersections
Intersection_Dict={}
n = 5 # How many Intersections you need
for s in range(n): 
     Intersection_Dict['Intersection{}'.format(s)]=0*len(Acc_ID_Data_indexed.index)
# Declare my dictionary (later it will have 1000 Intersection)
Distance = pd.DataFrame(Intersection_Dict,index=(Acc_ID_Data_indexed.index))

for q in range(len(Int_ID_Data_indexed.LATITUDE)):
    for i in range(len(Acc_ID_Data_indexed.Latitudex)):
            Distance.iloc[i][q]= measure(Int_ID_Data_indexed.LATITUDE[q], 
                                        Int_ID_Data_indexed.LONGITUDE[q], 
                                        Acc_ID_Data_indexed.Latitudex.iloc[i], 
                                        Acc_ID_Data_indexed.Longitudex.iloc[i])
# --------------------------------------------------
"""
                [- Continue working Thu Feb 21 13:50]
        Now we will add some changing to our current code
            - We will add instead of intersection1 intersection2 ... the intesection ID.
            - Dont ever Create your Column inside the loop and specify the length always.
                This is super important and save alot of time try not to create a list or dict.
                inside a loop too, also dont create a Dataframe Column inside a loop. because 
                each value you create
            - 
            - 
"""

Intersection_Dict={}
n = 3 # How many Intersections you need Remember you have n < 1019 intersection.
for s in range(len(Int_ID_Data.index[0:n])): 
     Intersection_Dict[Int_ID_Data_indexed.index[s]]=0*len(Acc_ID_Data_indexed.index)

# Declare my dictionary (later it will have 1000 Intersection)
Distance = pd.DataFrame(Intersection_Dict,index=(Acc_ID_Data_indexed.index))
Intersection_ID_Assigned_to_Acc = pd.Series(0,index=Acc_ID_Data_indexed.index)
for q in range(len(Int_ID_Data_indexed.LATITUDE)):
    print(q)
    for i in range(len(Acc_ID_Data_indexed.Latitudex)):
            Distance.iloc[i][q]= measure(Int_ID_Data_indexed.LATITUDE[q], 
                                        Int_ID_Data_indexed.LONGITUDE[q], 
                                        Acc_ID_Data_indexed.Latitudex.iloc[i], 
                                        Acc_ID_Data_indexed.Longitudex.iloc[i])
            if Distance.iloc[i][q] < int(35):
                #print(Distance.iloc[i][q]) 
                Intersection_ID_Assigned_to_Acc.iloc[i]=Int_ID_Data_indexed.index[q]
                #if Acc_ID_Data_indexed['Col1'].iloc[i] != 0:
            else:
                #Intersection_ID_Assigned_to_Acc.iloc[i]=0 # this line will print over the existed column and it is wrong
                # 
                #  
                pass

print(Intersection_ID_Assigned_to_Acc)
Acc_ID_Data_indexed['Col1'] =Intersection_ID_Assigned_to_Acc

# Perform a query for a specific value in the Table
Acc_ID_Data_indexed.loc[Acc_ID_Data_indexed.Col1=='23-K05867-000']
# Same thing you can achieve using Query
Acc_ID_Data_indexed.query("Col1 == '23-K05867-000'") 
# if you want to perform more complicated Queries here the one will bring Ghasak Intersections
"""
    Bring to us any values located in Col1 not equal to the intersection [23-K05867-000] and not zero.
"""
Acc_ID_Data_indexed.query("Col1 != '23-K05867-000' and Col1 != 0") 

# --------------------------------------------------
"""
        [- Continue working Fri Feb 22nd 19:23:23]
        Here will add three filters to identify the distance range (35 meter, 50 meter,75 meter,100 meter)
            - There filters will be measure from the Intersection longitude and latitude to each accident
            - 
"""
Intersection_Dict={}
n = 482 # How many Intersections you need Remember you have n < 1019 intersection.
for s in range(len(Int_ID_Data.index[0:n])): 
     Intersection_Dict[Int_ID_Data_indexed.index[s]]=0*len(Acc_ID_Data_indexed.index)

# Declare my dictionary (later it will have 1000 Intersection)
Distance   = pd.DataFrame(Intersection_Dict,index=(Acc_ID_Data_indexed.index))
Filter10   = pd.Series(0,index=Acc_ID_Data_indexed.index)
Filter20   = pd.Series(0,index=Acc_ID_Data_indexed.index)
Filter30   = pd.Series(0,index=Acc_ID_Data_indexed.index)
Filter50   = pd.Series(0,index=Acc_ID_Data_indexed.index)
Filter75   = pd.Series(0,index=Acc_ID_Data_indexed.index)
Filter100  = pd.Series(0,index=Acc_ID_Data_indexed.index)
for q in range(len(Int_ID_Data_indexed.LATITUDE)):
    !clear
    print(" Intersection No. {}".format(q))    
    for i in range(len(Acc_ID_Data_indexed.Latitudex)):
            Distance.iloc[i][q]= measure(Int_ID_Data_indexed.LATITUDE[q], 
                                        Int_ID_Data_indexed.LONGITUDE[q], 
                                        Acc_ID_Data_indexed.Latitudex.iloc[i], 
                                        Acc_ID_Data_indexed.Longitudex.iloc[i])
            if Distance.iloc[i][q] < int(10):
                Filter10.iloc[i]=Int_ID_Data_indexed.index[q]
            elif Distance.iloc[i][q] < int(20):
                Filter20.iloc[i]=Int_ID_Data_indexed.index[q]
            elif Distance.iloc[i][q] < int(35):
                Filter30.iloc[i]=Int_ID_Data_indexed.index[q]
            elif Distance.iloc[i][q] < int(50):
                Filter50.iloc[i]=Int_ID_Data_indexed.index[q]
            elif Distance.iloc[i][q] < int(75):
                Filter75.iloc[i]=Int_ID_Data_indexed.index[q]
            elif Distance.iloc[i][q] < int(100):
                Filter100.iloc[i]=Int_ID_Data_indexed.index[q]        
            else:
                continue
# --------------------------------------------------
"""
        [- How to Sort the rows of your distance from smaller to bigger distances]
        This algorithm is to find the closest distance to each intersection
            - There filters will be measure from the Intersection longitude and latitude to each accident
            - 
"""
Filtered_Data = pd.DataFrame({'Filter10':Filter10,
                'Filter20': Filter20,
                'Filter30': Filter30,
                'Filter50': Filter50,
                'Filter75': Filter75,
                'Filter100':Filter100})
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
Distance['23-K05617-000'][Distance['23-K05617-000']<30]
# How to sort the values in maximum order using the rows up to 2 intersections.
Distance.iloc[0][:].sort_values(ascending =True)[:2]
# ==================================================#
#          Filtering based on Distance                 
# ==================================================# 

List_Int_Name = []
# How many Columns You want to Filter
F = 5
for k in range(2*F):
    if k < F:
        List_Int_Name.append('Intersection{}'.format(k+1))
    else:
        List_Int_Name.append('Distance{}'.format(k-F+1))    


Distance_Dict = {}  
for s in range(2*F):
    Distance_Dict[List_Int_Name[s]]=0*len(Acc_ID_Data_indexed.index)
# Lets create a DataFrame with keys are Intersection[1:5] and Distances[1:5]
# this is from Pandas Frame, which gives us a zero value of 2870 [len(TopFive)],
# and give you: len(TopFive.columns) 10 columns.
TopFive   = pd.DataFrame(Distance_Dict,index=(Acc_ID_Data_indexed.index))
# populate the DataFrame with our results from the Distance measured. 
for acc in range(len(TopFive)):
    !clear
    print(" Accident No. {}".format(acc))
    TopFive.iloc[acc,0:F]=Distance.iloc[acc,0:].sort_values(ascending =True)[:F].keys()
    TopFive.iloc[acc,F:]=Distance.iloc[acc,0:].sort_values(ascending =True)[:F].values[:]
# Lets add our results of TopFive to our Final Crash Dataset output
Acc_ID_Final = Acc_ID_Final.assign(**TopFive)
# ==================================================#
#          Queries for our TopFive Dataset                 
# ==================================================#    
# Now we will perform the query to obtain the Toptwo distances with less than 30 meter
TopFive.query("(Intersection1 == '23-K11902-000')") # Example of clustering correctly.
TopFive.query("(Intersection1 == '23-K05611-000' and Distance1 < 35)")
TopFive.query("(Distance1 < 30) and (Distance2 <30)")    
TopFive.query("(Intersection1 == '23-K51139-100') and (Intersection2 =='23-K52413-200')") 
TopFive.query("(Intersection1 == '23-K51139-100') or (Intersection2 =='23-K51139-100')")
# Get a specific Crash based on Crash ID using Fancy Indexing
TopFive.iloc[TopFive.index[:]==22]
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
X = TopFive.iloc[0:5,0:] 
Y = X.query("Distance1 < 100") 
Xnew =X.assign(**Y)

# the above example cannot work if we want to add more criterias.
# the solution is to loop over all accidents 


Acc_Dict1 = {} 
Acc_Dict2 = {}  
Acc_Dict1["Selected_Intersection_Less35"] = np.zeros(len(Acc_ID_Data_indexed.index))
Acc_Dict2["Selected_Intersection_Less50"] = np.zeros(len(Acc_ID_Data_indexed.index))  
# You can create pd.Series too but I prefer to make DataFrame (SpreadSheet) as it gives you the dictionary name as column.
Desginated_Intersection_Less35 = pd.DataFrame(Acc_Dict1,index=(Acc_ID_Data_indexed.index))
Desginated_Intersection_less50 = pd.DataFrame(Acc_Dict2,index=(Acc_ID_Data_indexed.index))
count_cases = 0
for acc in range(len(TopFive)):       # For debugging TopFive.iloc[0:5,0:]
    if TopFive.iloc[acc].loc["Distance1"] < 35:
        Desginated_Intersection_Less35.iloc[acc] =TopFive.iloc[acc].loc["Intersection1"]
    elif  (TopFive.iloc[acc].loc["Distance1"] < 50):   # (TopFive.iloc[acc].loc["Distance1"] > 35) and
        Desginated_Intersection_less50.iloc[acc] =TopFive.iloc[acc].loc["Intersection1"]
    else:
        !clear
        count_cases = count_cases +1
        print("Accidents not meeting our Criteria {}".format(count_cases))
        print("=================================") 
        continue         

FinalSelection = pd.DataFrame({'FilterLess35':Desginated_Intersection_Less35.Selected_Intersection_Less35,
                               'FilterLess50': Desginated_Intersection_less50.Selected_Intersection_Less50 })
print(" Accidents with Number of crashes located less than 35 meter is ={} out of {}".format(len(TopFive)-len(FinalSelection.query("FilterLess35 != 0")),len(TopFive)))
print("=================================")
print(" Accidents with Number of crashes located less than 50 meter is ={} out of {}".format(len(TopFive)-len(FinalSelection.query("FilterLess50 != 0")),len(TopFive)))
Acc_ID_Final = Acc_ID_Final.assign(**FinalSelection)
                                   

#print(acc)
# TopFive.iloc[0:5,5:].min(axis = 1)


"""
        Exporting Our Results [- Output of our Cleaned Data]
        The output for both the Distances and for the Accident final Dataset.
            - Calling the main directory and attach it to a subfolder for transformability folders.
"""
import os 
Current_Path = os.getcwd() 
Distance.to_csv(Current_Path+"/Results/Distance.csv", sep='\t')
TopFive.to_csv(Current_Path+"/Results/TopFive.csv",sep='\t')
Acc_ID_Final.to_csv(Current_Path+"/Results/Acc_ID_Final.csv", sep='\t')



# Export to Check, 
Table56 = TopFive.query("(Distance1 < 35) and (Distance2 <35)")
Table56.to_csv(Current_Path+"/Results/Table56.csv", sep = '\t')








