"""
Write a function that takes a list of words as an input argument and returns True if the list is sorted and returns False otherwise.
"""

# Function Dec.
def sort_list(L):
    # Making a copy of list
    # Using list slicing
    copy_L = L[:]
    # List Sorting
    L.sort()
    # Checking if both lists are equal
    if copy_L == L:
        return True
    else:
        return False
