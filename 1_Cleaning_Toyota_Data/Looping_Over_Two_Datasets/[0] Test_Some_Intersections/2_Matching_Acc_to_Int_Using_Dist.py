# ==================================================#
# 			Import Libraries				
# ==================================================#
# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import numpy as np 

# ==================================================#
# 			Import Toyota Data Using Panda					
# ==================================================#
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
Acc_ID_Data = pd.read_csv("Accidents_Database.csv") 
Int_ID_Data = pd.read_csv("Intersection_ID.csv")   
# You need to set the directory to (/Users/ghasak/Desktop/1_Cleaning_Toyota_Data/Python_Cleaning/)
# if you open your ipython not inside your folder where you can get the .csv file (working Direcotry)
# Preview the first 5 lines of the loaded data 
Int_ID_Data.head()
# ==================================================#
# 			Descriptive Statistic in Panda					
# ==================================================#
# If you want to print a specific Column
# print (data['ITARDA_crossing_ID'])

# Data Description 
Acc_ID_Data.describe()
Int_ID_Data.describe()
# You can use the 
Acc_ID_Data.transpose() # to change columns to rows
# ==================================================#
# 	Distance Function (considering Curvtuer of earth)					
# ==================================================#

def measure(lat1,lon1,lat2,lon2):
    # Website :https://stackoverflow.com/questions/639695/how-to-convert-latitude-or-longitude-to-meters
    # Formula :https://en.wikipedia.org/wiki/Haversine_formula
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

# ==================================================#
# 			Accessing Data in Panda						
# ==================================================#

Acc_ID_Data_indexed = Acc_ID_Data.set_index(['ITARDA_crossing_ID'])
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
Acc_ID_Data_indexed.rename(columns = {'Latitude_base-10_':'Latitudex','Longitude_base-10_':'Longitudex'}, inplace =True) 
# Now we can call the columns that we want
Acc_ID_Data_indexed.Longitudex[0]
Acc_ID_Data_indexed.Latitudex[0]
# --------------------------------------------------
"""
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

for q in range(len(Int_ID_Data_indexed.LATITUDE)):
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
                [Working So far distane of two intesections or Q intersections]
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
# This Block is working for only two intersections. 
Intersection_ID_Assigned_to_Acc = pd.Series(0,index=Acc_ID_Data_indexed.index)
Distance = pd.DataFrame({'Intersection1':0*len(Acc_ID_Data_indexed.index),
                        'Intersection2':0*len(Acc_ID_Data_indexed.index)},
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

















  

