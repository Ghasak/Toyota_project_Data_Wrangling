# ==================================================#
# 			Import Libraries				
# ==================================================#
"""
	We will learn here the pandas pacakge
	- It is bulit over Numpy and its a pacakge can deal
		with data numbers and names.
	- It also enhanced numpy and more robust for 
	- 

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
	We will learn now about pandas Series
	- Making series objects from python lists and dicts.
	- Extracting indexes and values
	- How we will do indexing series objects implicitly and explicitly.
	- its for one dimensional array (as a vector)
"""
# To create a series (one-dimensional array) of square numbers
# with a name as squares.
s = pd.Series([0,1,4,9,16,25],name='squares') 
# You can get also the power of NumPy array and add it to Pandas Series
s1 = pd.Series(np.random.random(10)) 

# To obtain the values
s.values
s.count()

# To obtain  of a specific value
s.values[3]
s[3]

# We can use a standard slicing same as Python list
s[0]
s[1:4]

"""
	Lets formulate our Dataset and get the items in it
	- We will learn how to formulate a data-frame.
	- Call or refer to any item in the dataframe.
	- loop over a specific value in the dataframe.
	- perform any acrobatic.
"""

pop2014 = pd.Series([100,99.3,95.5,93.5,92.4,84.8,84.5,78.9,74.3,72.8],
			index=['Java','C','C++','Python','C#','PHP','JavaScript','Ruby','R','Matlab'])
pop2015 = pd.Series({'Java':100,'C':99.9,'C++':99.4,'Python':96.5,'C#':91.3,'R':84.8,'PHP'
			:84.5,'JavaScript':83.0,'Ruby':76.2,'Matlab': 72.4})
twoyears = pd.DataFrame({'2014':pop2014,'2015':pop2015})

"""
	To refer to any column in the dataframe (dataframe is like excel-sheet file 
	(there is a key which)) and to loop over a specific value in the dataframe
	
"""
#------------------------------------------------------------
DataSheet1 = pd.DataFrame({'Year2014':pop2014,'Year2015':pop2015}) 
DataSheet1['Year2015'] # You can achieve the same thing by typing
DataSheet1.Year2014
DataSheet1['Year2015'][1] # bring the cell number 2 from the Columns labled as Year2015

for i in range(len(DataSheet1['Year2015'])):  # Notice here we loop over the len of the colum as i=1,2,3,...
	print(DataSheet1['Year2015'][i])
# Same thing you can achieve by refere using the .object	
# for i in range(len(DataSheet1)): 
#          print(DataSheet1.Year2015[i]) 	
# you can achieve the samething as following:
for item in DataSheet1['Year2015']:
	print(item)
#------------------------------------------------------------	
"""
	To loop and compare each value specific column
		- using the if statment
		- It seems that the loop in the i better than item-loop as I can know the index of the value
			of each row.
"""
for i in range(len(DataSheet1['Year2015'])):
	if DataSheet1['Year2015'][i] == 84.8: # any value that you want to compare
		print("Yes we are having an item 84.8 located at {}".format(i))
	else:
		print(DataSheet1['Year2015'][i])

# Notice here as for now I cant get the idex of the loop
for item in DataSheet1['Year2015']:
	if item == 84.8: # any value that you want to compare
		print("Yes we are having an item 84.8 = {}".format(item))
	else:
		print(item)
#------------------------------------------------------------
"""
	Change data type of columns in Pandas
	- This topic is the most important for the DataSheet
	- You will investigate the Datatype in your DataFrame and 
		try to understand all the fields of your dataset (feilds=cell)
		https://stackoverflow.com/questions/15891038/change-data-type-of-columns-in-pandas	
"""

# To see what kind of Data type I have you can use
DataSheet1.info()


#------------------------------------------------------------
"""
	How to Create a new Column in our DataSheet
	- Create a zero value column named (Year_Dummy) and assign the value of zero
"""
# How to Create a new Column in our DataSheet
# Create a zero value column named (Year_Dummy) and assign the value of zero
DataSheet1['Year_Dummy']=pd.Series(0,index = DataSheet1.index) 

for i in range(len(DataSheet1['Year2015'])):
	if DataSheet1['Year2015'][i] == 84.8: # any value that you want to compare
		#print("Yes",DataSheet1['Year2015'][i])
		DataSheet1['Year_Dummy'][i] = 1
	else:
		#print(DataSheet1['Year2015'][i])
		DataSheet1['Year_Dummy'][i] = 0
# Same like before but as you can see we dont know the index number so this will not work
for item in DataSheet1['Year2015']:
	if item == 84.8: # any value that you want to compare
		#print("Yes",DataSheet1['Year2015'][i])
		DataSheet1['Year_Dummy'][item] = item
	else:
		#print(DataSheet1['Year2015'][i])
		DataSheet1['Year_Dummy'][item] = 0
#------------------------------------------------------------
"""
	How to Remove a column from your dataset
	- if you drop a column it will not be drop from the original, thats why you need to create a copy
	- if you want to change the orginal DataSheet then you can use (inplace=True) add it in the drop
		or any function that you want to perform a change to your original DataSheet.
"""

DataSheet2 = DataSheet1.drop('Year_Dummy',axis=1)
#------------------------------------------------------------
"""
	How to understand iloc and lock
	- These two fucntions are used with the DataFrame (DataSheet) or a column-vectors.
	- It will get you the Number of the row of your DataFrame and all the attached Column (Value) to this row
	- the loc usually works with names and it needs the index name (I usually can control this when
		I will create a DataFrame and assign which index i want to do.)
	- iloc need the row number (index number which is very good for looping over all columns for this specified row).
"""
print(DataSheet1)
print(DataSheet1.iloc[1])	# bring me the row number one, remeber it is count from 0 so this means row number two.
print(DataSheet1.loc['C#'])	# as you can see here you have to give the name of the row if it is name-indexed-based.
#------------------------------------------------------------
"""
	Applying a Boolian Mask
	- This tech is so useful to work with the Columns and apply filters
	- it can be used for Series only (Column Vector) (DataFrame I havent discvoered yet)
"""
pop2014[pop2014>90]
DataSheet1['Year2015'][DataSheet1['Year2015']>90]  
#------------------------------------------------------------
"""
	How to Look into specific values (rows) in your DataSheet, it can be also used for colum
	- Using the iloc and loc functions.
	- You will also after trunction will create two series (two columns) of these truncated from DataSheet1
	- at assign these two values to a new DataSheet3 
"""
print(DataSheet1.iloc[0:3])
print(DataSheet1['Year2015'].iloc[0:3])
# Lets create two series (two columns) truncated with three values using iloc
Series1 = pd.Series(DataSheet1['Year2014'].iloc[0:3]) #,index=DataSheet1.index)
Series2 = pd.Series(DataSheet1['Year2015'].iloc[0:3]) #,index=DataSheet1.index)
# lets create a Sheet using DataFrame function combine the two using Dictionary.
DataSheet3 = pd.DataFrame({'Series1':Series1,'Series2':Series2})
#------------------------------------------------------------
"""
	Filtering Columns in Pandas based on a criteria.
	- We will use something called Boolian indexing.
	- https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
	- To add more criteria for our DataSheet we can use the following.
	- https://stackoverflow.com/questions/13611065/efficient-way-to-apply-multiple-filters-to-pandas-dataframe-or-series
	- The DataFrame now can be filtered based on each column in the datasheet.
"""
# Show the DataSheet1 first
DataSheet1
Filter1 = DataSheet1['Year2014'] == 92.4		# Apply the first filter to a value like 92.4
Filter2 = DataSheet1['Year2015'] == 100.0		# Apply the Second filter to a value like 100.0
DataSheet1[Filter1 | Filter2]	#   You can use & (and) | (or) to join two filters or more
# Similary you can also apply the following with .loc or without it.
# The () are so important wihtout them you will get an error.
DataSheet1.loc[(DataSheet1['Year2015']==100.0) | (DataSheet1['Year2014']==92.4)]
# There is another way to filter using group as
# DataSheet1.groupby('Year2014') # This is useful but has to be used with list and dic
# IID = pd.Series(DataSheet1.groupby('Year2015'))
#------------------------------------------------------------
"""
	Adding a caculation for a specific column.
	- We will use something called Boolian indexing.
	- https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
	- To add more criteria for our DataSheet we can use the following.
	- https://stackoverflow.com/questions/13611065/efficient-way-to-apply-multiple-filters-to-pandas-dataframe-or-series
	- The DataFrame now can be filtered based on each column in the datasheet.
"""
# Calculating the Average and create a coulmn called Average
DataSheet1['Average']= 0.5*(DataSheet1['Year2014']+DataSheet1['Year2015'])
DataSheet1['Sum'] = DataSheet1['Year2014']+DataSheet1['Year2015']
DataSheet1['X'] = DataSheet1['Year2015']-DataSheet1['Year2014'][0]

#------------------------------------------------------------
"""
	How to Change a column name in you DataSheet.
	- The best way is to follow: 
		https://cmdlinetips.com/2018/03/how-to-change-column-names-and-row-indexes-in-pandas/
	- You can call first all the columns in your dataset and apply the function (rename)
"""
DataSheet1.columns
DataSheet4 = DataSheet1.rename(columns={'Year2014':'Year2014_New','Year2015':'Year2015_New'})
# Now you will see DataSheet4 has been changed to the new columns name., 
# You dont need to change ever column just the one you dont like.
#------------------------------------------------------------
"""
	Change data type of columns in Pandas
	- This topic is the most important for the DataSheet
	- You will investigate the Datatype in your DataFrame and 
		try to understand all the fields of your dataset (feilds=cell)
"""

# To see what kind of Data type I have you can use
DataSheet1.info()
#------------------------------------------------------------







# I have changed sort to sort_values with the new pandas
twoyears = twoyears.sort_values('2015',ascending=False) 
# Access the values of the data
twoyears.values
# Access the names of each row
twoyears.index
# Access the names of each column
twoyears.columns
# iloc and loc for get a specific value
twoyears.iloc[1:4]
twoyears.loc['C':'PHP']
# To access your dataframe of a certian column
print(twoyears['2014'])
# To access your dataframe ofa certain value in a column
print(twoyears['2014'].get('Python'))
# Calculating the Average and create a coulmn called Average
twoyears['Average']= 0.5*(twoyears['2014']+twoyears['2015'])
























#------------------------------------------------------------
presidents = pd.DataFrame([{'name': 'Barack Obama', 'inauguration': 2009, 'birthyear': 1961},
						  {'name': 'George W.Bush', 'inauguration': 2001, 'birthyear': 1946},
						  {'name': 'Bill Clinton', 'inauguration': 1993, 'birthyear': 1946},
						  {'name': 'George H. W. Bush', 'inauguration': 1989, 'birthyear': 1924}])

# Indexing the data based on the name variable (name is a column)
presidents_indexes = presidents.set_index('name')
# Lets get the entir record for Bill Clinton
presidents_indexes.loc['Bill Clinton']
# Lets get the entir record for Bill Clinto with the a specific column (inauguration)
presidents_indexes.loc['Bill Clinton']['inauguration'] # same you can use presidents_indexes.loc['inauguration']['Bill Clinton']
# Using the Join betweent two dataframes in Pandas

presidents_fathers = pd.DataFrame([{'son': 'Barack Obama', 'father': 'Barack Obama Sr.'}
								  ,{'son': 'George W.Bush', 'father': 'George H. W. Bush'}
								  ,{'son': 'George H. W. Bush', 'father': 'prescott Bush'}])
pd.merge(presidents,presidents_fathers,left_on='name',right_on='son')

# How about dropping some specific column 
pd.merge(presidents,presidents_fathers,left_on='name',right_on='son').drop('son',axis = 1)

# For not matched DataFrames we can include in the joint method called left-joint
pd.merge(presidents,presidents_fathers,left_on='name',right_on='son', how = 'left').drop('son',axis = 1)

# Lets now Use the Data from teh seaborn
flights = seaborn.load_dataset('flights')
flights_indexed = flights.set_index(['year','month'])
# Lets Slice based on the indcies
flights_indexed.loc[1949,'January']
flights_indexed.loc[1949].loc['January':'June']

# Lets now using the information of stack() method
# This method used to flib between index and columns
flights_unstacked = flights_indexed.unstack()
# now we can perform over the values 
flights_unstacked.sum(axis=1)

flights_unstacked['passengers','total'] = flights_unstacked.sum(axis=1)




































