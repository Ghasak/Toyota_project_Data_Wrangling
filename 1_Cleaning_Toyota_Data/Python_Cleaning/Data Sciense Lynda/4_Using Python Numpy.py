# ==================================================#
# 			Import Libraries				
# ==================================================#
# its the fundamental pacakge for math and sicentific 
# Orginize the data in memory of NumPy Array
# NumPy need to be very precise of Data Type
"""
	- Integers: numpy.int8, numpy.int16, numpy.int32, numpy.int64. 
		Unsigned: numpy.uint8, etc.
	- Floating-point numbers: numpy.float32, numpy.float64, numpy.float128. 
		Complex: numpy.complex64, etc.

"""
"""
	- Applying mathematical operations to and between arrays
	- Plotting one-dimensional arrays with matplotlib
	- Performing linear-algebra computations with arrays

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,40)

sinx = np.sin(x)
cosx = np.cos(x)
plt.plot(x,sinx)	# you can add (x,sinx,'x')
plt.plot(x,cosx) 	# you can add (x,cos,'o')
plt.show()


# ---------------------------------

y = sinx * cosx
z = cosx**2 - sinx**2
plt.plot(x,y)
plt.plot(x,z)
plt.legend(['sinc(x) cos(x)', 'cos(x)^2 - sin(x)^2'])
plt.show()

# ---------------------------------
"""
Linear Algebra
"""
print(np.dot(sinx,cosx))
print(np.outer(sinx,cosx))

"""
Create Vector as an array

"""
v1 = np.linspace(0,10,5)
v2 = v1+1

print(v1,v2)

vv = np.outer(v, v)
vv+v1

np.transpose(vv)



x = np.linspace(, stop)



"""
	- How to indexing and slicing numpy array
	- Indexing array eleemnts
	- Slicing arrays
	- Advanced indexing
	- NumPy vs. Python -list indexing and slicing

"""

v = np.linspace(0, 10,5)
v[1]
v[-1]
v[5]


vv = np.random.random([5,4])
vv[0,0]
# or 
vv[0][0]

# if you want to use the python list you can use a list of list

LL = [[1,2,3],[4,5,6],[7,8,9]]
LL[0]
LL[0][1] # you cant use the LL(0,1)

# Slicing similar to the Python list
vv[2:4]
vv[2:5,1]

"""
	Usually NumPy if you apply a change to a sublist then the orginal
	list also will change (you can use explicit .copy() to fix this problem)
	[Later I discover that new Python have fixed this feature]
""" 
list1 = [1,2,3,4,5]
print(list1)
list2 = list1[2:4]
print(list2)
list2[0] = "I applied a change"
print(list2)
# but the original also has been changed
print(list1)



"""
	Records and Dates in Numpy
	- Creating and manipulating NumPy record arrays.
	- Working with Numpy datetime64 objects.
""" 

# Create a mixed of list and dictionary in numpy

reca = np.array([(1,(2.0,3.0),'Hey'),(2,(3.5,4.0),'n')], 
	dtype=[('x',np.int32),('y',np.float64,2),('z',np.str,4)])  # Str length is 4 



# if you want to access the first element we use
reca[0]
reca['x'] 
reca['x'][0]
reca[0]['x']

# record arraies are similar to DataFrame in Pandas as we will see later
# it is to represent a non-homogenous tabular data.


# Now we will see the date 

np.datetime64('2015')
np.datetime64('2015-01')
np.datetime64('2015-02-03 12:00:00')
np.datetime64('2015-02-03 12:00:00+0700')


# You can add some logic to the time

np.datetime64('2015-01-01') < np.datetime64('2015-04-03')
# Time delta object we can get it as:
np.datetime64('2015-04-03')- np.datetime64('2015-01-01') 

np.datetime64('2015-01-01') + np.timedelta64(5,'D') # Adding 5 days

np.datetime64('2015-01-01') + np.timedelta64(5,'h') # Adding 5 hours


# You also can converte the date or time into float type
 np.datetime64('2015-01-01').astype(float) # this will give you number of days since 1970 (the standard date)
# Check on finding the standard date

np.datetime64('1970-01-01').astype(float)


# this is so helpful to create a date in numpy as

r = np.arange(np.datetime64('2016-02-01'),np.datetime64('2016-03-01'))
























































