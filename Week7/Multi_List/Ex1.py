"""
Write a function which accepts a 2D list of numbers and returns the sum of all the number in the list You can assume that the number of 
columns in each row is the same. (Do not use python's built-in sum() function).

"""

# Function Dec.
def add_list(L):
    add = 0
    # Accessing all elements
    # Adding them
    for i in L:
        add += i
    return add
