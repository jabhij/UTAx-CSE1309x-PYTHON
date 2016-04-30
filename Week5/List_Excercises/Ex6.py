"""
Write a function that accepts a list and return a new list which contains all but the first and last elements of the original list.
"""

# Function Dec.
def extract(L):
    # Logic- List Slicing
    new_list = L[1: -1]
    return new_list
