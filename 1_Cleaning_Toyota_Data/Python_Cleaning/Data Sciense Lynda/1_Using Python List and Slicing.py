# ==================================================#
# 			Import Libraries				
# ==================================================#

# Lists begin 

"""
We will learng first about python containers
"""

nephews = ['Huey','Dewey','Louie']
nephews[0]
len(nephews)

for item in range(len(nephews)):
	nephews[item] = nephews[item]+'Duck'

# We dont need to have homogenious datatype in our list: we can have numbers, string...etc

mix_it_up = [1,[1,2],'alpha']

print('Item','name')
for i in range(len(mix_it_up)):
	print(i,mix_it_up[i])

#----------------------------------------------
# To add a value to our list
nephews.append('April Duck')
# To concatinate to a list
nephews.extend(['May Duck', 'June Duck']) # you can use the extend method or
print(nephews)
newphews2 = nephews + ['Donald Duck','Daisy Duck']
# To iterate over each element in our list 
for i in range(len(newphews2)):
	print(i,newphews2[i])

# To insert an element at any position we can write
newphews2.insert(3,'I am Ghasak') # newphews2.insert(index, object)

# We can delete an element either by index or by value 
newphews2.remove('I am Ghasak')
# or
del newphews2[0]
#----------------------------------------------
newphews2.sort()  # Alphabetically sorting
print(newphews2)

# Lets using Slicing

square = [ 0,1,4,9,16,25,36,49]
square[0:2]
square[1:3]
square[:]
square[-1] # bring the last element

for i in range(len(square)):	# Print elements in reverse order
	print(square[-i-1])
#----------------------------------------------
# We can do assign 

square[2:4] = ['test1','test2']
print(square)

del square[2:4]

#----------------------------------------------
# Usually the Python list is used in loops
# Loop in this shape without in ragne(len(square)) is for both numerials and string
for value in square:
	print('Element',value)

for value in square:
	if value == 16:
		print('Found Element at = ',value)
		print('-----> Square of the value is = ',(value)**2)
	else:
		print('Element',value)

#-------------------------------------------------
 # Usually the list we can loop with index (called enumerate)

 for index, value in enumerate(square):
 	 print('Element','--->',index,'with',value)

# List also is good to store same data type in one place


# You can use List with names as 

List = ['Huey', 'Dewey', 'Louie']

for item in range(len(List)): 
 	print(List[item]) 

# Or

for item in List:
	print(item)




