# ==================================================#
# 			Import Libraries				
# ==================================================#
"""
In python you want to iterate over each element in your 
list or dict then perform some math or data wrangling
then store them in a list of dict again
this is so powerful and you will need several for loops
but python allow you to perform this using comprehensions
	- Write a loop as a comprehensiions
	- Filter items by applying these comprehensions
	- Create a dict and list from a comprehension
"""

# lets say we are bulding a list of square

squares = []

for i in range(10):
	squares.append(i**2)


# We will apply our comprehensions to achieve same thing


squares = [i**2 for i in range(10)]

# You can also filter your loop as
# Lets say that we want to get only the square of
# Divisable by (3)

squares_div_3 = [i**2 for i in range(30) if (i%3 ==0)]

# We can achieve samething using dictionary 
squares_div_4 = {i:i**2 for i in range(30) if (i%3 == 0)}

# -----------------------------------------
"""
Lets pracitse of our last looping techniques from dictionary
"""
squares_div_5 = {i:i**2 for i in range(10)}

for value, key in squares_div_5.items():
	print(value,key)

for value in squares_div_5.values():
	print(value)	

for key in squares_div_5.keys():
	print(key)

for key in squares_div_5:
	print(key, squares_div_5[key])


"""
Lets try to traspot our dictionary 
values instead keys 

"""
capitals = {'United States': 'Washington', 'Franc':'Paris', 
			'Italy': 'Rome','Germany': 'Berlin', 'United Kingdom': 'London'}

capitals_by_capitals = { capitals[value]:value for value in capitals} # we have switeched between the keys and values

"""
Generated Squence (Naked Comprehensions)
"""
print("The sum of 10 powered elements")
sum([i**2 for i in range(10)])
# if you remove the [] then you will get the naked comprehensions, which is not saved as list

sum(i**2 for i in range(10))


"""
	- Comprehensions are a concise and expressive way to write a data transformation.
	- They are quick to write, easy to parse, and surprisingly powerful.
"""




