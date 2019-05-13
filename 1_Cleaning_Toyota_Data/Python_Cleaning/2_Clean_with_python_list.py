# ==================================================#
# 			Import Libraries				
# ==================================================#
# Load the Pandas libraries with alias 'pd' 
import numpy as np 
import csv
# ==================================================#
# 			Import Toyota Data Using Panda					
# ==================================================#

# define the location of importing data
infile=open(r"/Users/Ghasak/Desktop/1_Cleaning_Toyota_Data/Python_Cleaning/3_Clean_Original_Python.csv","r")
infile.readline() # to skip the first row of the columns titles.
reader=csv.reader(infile)

# define the location of exporting data
outfile=open(r"/Users/Ghasak/Desktop/1_Cleaning_Toyota_Data/Python_Cleaning/","ab")
heads=['No', 'Year', 'Latitude_base-10_', 'Longitude_base-10_','ITARDA_crossing_ID']
writer=csv.writer(outfile)

list0=[]
for row in reader:
    print (row)
    if row[1] in list0:
        print("ok")
    else:
        list0.append(row[1])
print(len(list0))

for item in list0:
     writer.writerow([item])

# ==================================================#
# 			Descriptive Statistic in Panda					
# ==================================================#
# If you want to print a specific Column
# print (data['ITARDA_crossing_ID'])

# Data Description 
data.describe()
# ==================================================#
# 				Clean Data with Panda						
# ==================================================#
# Detecting numbers 
New_Data = []

for row in data['ITARDA_crossing_ID',]:
	if row not in ITARDA_crossing_ID2:
		New_Data.append(row)
	else:
		continue







# ==================================================#
# 				Import DataSet						
# ==================================================#

    