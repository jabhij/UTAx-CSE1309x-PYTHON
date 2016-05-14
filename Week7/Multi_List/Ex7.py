"""
Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns a list which includes the maximum 
value of each row.

"""

# Function Dec.
def get_max(L):
    new_list = []
    # Iterating through rows
    for i in L:
        # Max and Append
        new_list.append(max(i))
    return new_list
