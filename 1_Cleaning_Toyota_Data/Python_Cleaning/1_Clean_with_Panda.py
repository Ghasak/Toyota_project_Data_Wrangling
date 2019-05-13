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
data = pd.read_csv("3_Clean_Original_Python.csv")  
# You need to set the directory to (/Users/ghasak/Desktop/1_Cleaning_Toyota_Data/Python_Cleaning/)
# if you open your ipython not inside your folder where you can get the .csv file (working Direcotry)
# Preview the first 5 lines of the loaded data 
data.head()
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

for row in data['ITARDA_crossing_ID']:
	if row not in New_Data:
		New_Data.append(row)
		
	else:
		continue

# ==================================================#
# 			Accessing Data in Panda						
# ==================================================#

# --------------------------------------------------
# 		Observing all intersection gropued
# --------------------------------------------------
for name, group in data.groupby('ITARDA_crossing_ID'):
	pass
	# print(name)
	# print(group)
# --------------------------------------------------
# 		Inetrsection groupby Intersection ID 		
# 		and how many crashes occured
# --------------------------------------------------
IID = dict(list(data.groupby('ITARDA_crossing_ID'))) # Intersection ID
# Print Each Intersection ID as following
for id in IID:
	print(id,len(IID[id]))

# You also can try
for line in IID.keys():
	print(line,len(IID[line]))

# --------------------------------------------------#
# Testing Individual Intersection ID
# --------------------------------------------------#
print(IID['23-K05165-000'])
IID['23-K05165-000'].get('Hour') 
IID['23-K05165-000'].get(['Year','Hour']) 

for item in IID['23-K05165-000'].get('Hour'):
	print(item) 
# --------------------------------------------------
IID['23-K05165-000'].iloc[0:1] # Disply Horizontally 
IID['23-K05165-000'].iloc[0]   # Disply Vertically
IID_23_K05165_000_indexes = IID['23-K05165-000'].set_index('No')

IID_23_K05165_000_indexes_DF = pd.DataFrame(IID_23_K05165_000_indexes)
IID_23_K05165_000_indexes_DF.loc['Hour':'Year']
# Converate to a Series to work with the data
K = pd.Series(IID['23-K05165-000'].iloc[0]) 
# Now you can do anything to K like
K[0:5]
K[1]
K[3]
# Up to hear I couldnt access the values of K
# --------------------------------------------------# 
# --------------------------------------------------#
# 			Working with Data Indexing
#		[Based on Using multilevel indices]
# --------------------------------------------------#
Datanew = data.set_index(['ITARDA_crossing_ID'])
Datanew.loc[('23-K05165-000')]
Datanew.iloc[0:3]
# We can specify a value with the ID
Datanew.loc['23-K05165-000','Year']
Datanew.loc['23-K05165-000','Year']

# Lets see the Stuck() method
Datanew_unstacked = Datanew.loc[('23-K05165-000')].unstack()




















for lines in IID['23-K05165-000'].keys(): 
	print(lines)
	l =lines.strip().split("\t") 
 # --------------------------------------------------#   




# Printing All Intersection in our Dataset
len(IID.keys())
# Printing All Crashes in our dataset
sum(len(v)for v in IID.values())
# Printing count each intersection hommany accidents
sum(len(v) for v in IID['23-K05165-000'])
# To see what kind of columns I have for this Intersection ID
IID['23-K05165-000'].columns


cnt = 0
for item in IID['23-K05165-000']:
	cnt += 1
print(cnt)

 
name = []
count = []
for name, group in data.groupby('ITARDA_crossing_ID'):
	name.append(name)
	# print(name)
	# print(group)


data.groupby(len).sum()
# ==================================================#
# 				Import DataSet						
# ==================================================#

    