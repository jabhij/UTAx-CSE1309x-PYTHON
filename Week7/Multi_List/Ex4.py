"""
Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns a list which includes the sum of each
row. You can assume that the number of columns in each row is the same.

"""

# Function Dec.
def rows_sum(L):
    new_list = []
    # Iterating through rows
    for i in L:
        # Add and Append
        new_list.append(sum(i))
    return new_list
