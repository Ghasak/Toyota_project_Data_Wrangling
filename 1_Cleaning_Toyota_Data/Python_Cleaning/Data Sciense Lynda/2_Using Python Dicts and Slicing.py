# ==================================================#
# 			Import Libraries				
# ==================================================#

capitals = {'United States': 'Washington', 'Franc':'Paris', 'Italy': 'Rome'}

capitals['Italy']

# To add an element to our dictionary
capitals['Spain'] = 'Madrid'

# To check an element in our dictionary using (in)

'Germany' in capitals
'Italy' in capitals

# Combine two dictionary maybe is not conveient like in list (concatination)
# because we are having a collision among items

morecapitals = {'Germany': 'Berlin', 'United Kingdom': 'London'}

capitals.update(morecapitals)

# To delete an item in a dictionary we can use the item (del)

del capitals['United States']
del capitals[3]


# Looping over dictionary similar to the List but there are three types of loop
# Loop type 1
# ------------------
# Straight forward loop
for key in capitals:
	print(key,capitals[key])

# Loop type 2
# ------------------
# loop over keys only
for key in capitals.keys():
	print(key)

# Loop type 3
# ------------------
for key in capitals.values():
	print(key)

# Loop type 4
# ------------------
for key, value in capitals.items():
	print(key,value)

# Python dicts are useful and Ubiquitous
# - Flexibel and efficient containers to associate labesl with heterogneous data
# - Use where data  items have, can be, given lables
# - Most appropriate for collecting data items of different kinds



# --------------------------------
# How to work with Dictionaries as a table
Dic = {'Key1':[1,2,3], 'Key2':[0.2,0.4,0.5],'Key3': ['male','female','male']} 

Dic['Key1'][1]   

# To access the values of each column we can write
for value in Dic.values(): 
    for item in value: 
    	print(item) 

 # How to loop over each dic key (column name) to get first value in the list
 print(Dic['Key1'][0],Dic['Key2'][0],Dic['Key3'][0])


 for key in Dic.values():
 	# print(key)
 	for value in key:
 		print(key,value)
 	 #print(Dic[key][value],Dic[key][value],Dic[key][value])

for value in Dic.values():
	for key in Dic.keys():
		print(key,value)














