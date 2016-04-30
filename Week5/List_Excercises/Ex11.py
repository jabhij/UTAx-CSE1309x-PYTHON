"""
Write a function that accepts a list and returns a new list such that the new list contains all the items of the old list in reverse order. 
Note that this is NOT a sorting problem. Do NOT use the built in reverse() method for this problem. For example if:

input_list = ['apples', 'eat', "don't", 'I', 'but', 'Grapes', 'Love', 'I']
then your function should return a list such as:
['I', 'Love', 'Grapes', 'but', 'I', "don't", 'eat', 'apples']
"""

# Function Dec.
def traverse(L):
    new_list = []
    i = -1
    # Accessing Values and Logic
    while i > -len(L)-1:
        new_list.append(L[i])
        i -= 1
    return new_list
