"""
Write a function that accepts a 2-dimensional list of integers, and sorts (descending order) all the elements inside each row and returns 
the sorted 2-dimensional list.

"""

# Function Dec.
def sort_rows(L):
    # Accessing every row
    for i in L:
        # Sorting
        i.sort(reverse = True)
    return L
