"""
Write a function that accepts a 2-dimensional list of integers, and returns a sorted (ascending order) 1-Dimensional list containing all 
the integers from the original 2-dimensional list.

"""

# Function Dec.
def _2D_to_1D_ (L):
    new_list = []
    # Accessing Rows
    for i in L:
        # Accessing every row's element
        for elements in i:
            new_list.append(elements)
            new_list.sort()
    return new_list
