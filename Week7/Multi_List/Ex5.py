"""
Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns a list which includes the sum of 
each column. Assume that the number of columns in each row is the same.

"""

# Function Dec.
def cols_sum(L):
    new_list = []
    # Starting from first Col
    for i in range(len(L[0])):
        get_sum = 0
        # Iterating through rows (top -> bottom)
        for j in L:
            # Add and Append
            get_sum += j[i]
        new_list.append(get_sum)
    return new_list
