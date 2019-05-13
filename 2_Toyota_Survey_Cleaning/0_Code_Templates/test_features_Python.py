# # Lets test teh first critira
# # import only system from os

# from os import system, name

# # import sleep to show output for some time period
# from time import sleep

# # define our clear function


# def clear():

#     # for windows
#     if name == 'nt':
#         _ = system('cls')

#     # for mac and linux(here, os.name is 'posix')
#     else:
#         _ = system('clear')


# # print out some text
# print('hello geeks\n' * 1000000)

# # sleep for 2 seconds after printing output
# sleep(2)

# # now call function we defined above
# clear()


# import os


# def clear(): return os.system('clear')
# import os


# def clear():
#     os.system('cls' if os.name == 'nt' else 'clear')


# # now, to clear the screen
# # add something to clear the screen
# class cls(object):
#     def __repr__(self):
#         import os
#         os.system('cls' if os.name == 'nt' else 'clear')
#         return ''


# cls = cls()
import os; clear = lambda: os.system('clear');
# ==== end pythonstartup.py ====

#print("Please input the method of printing")
#x = int(input("Which method you want x ={1,2,3}? "))
# x = float(input("Write a number"))


for count in range(1000):
    print(f"The value that we are looking for is {count}")
    clear()

# if x == 2:
# for count in range(10000):
#     print(f"The value that we are looking for is {count}")
#     print('\n' * 1000)  # Activate this if you are running the program in Sublime Console


# for count in range(1000):
#     print(f"The value that we are looking for is {count}")
#     clear()           # Activate this if you are running the program in Terminal Console for calling your script as (python script_name.py)

    # if count % 100 == 0: # This to pring every specific step usually in R loop calcuation or even Python.
    #     print(count)
