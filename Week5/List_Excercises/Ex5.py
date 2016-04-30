"""
Write a function that accepts a list and a value of an element and returns the count of how many times that element appears in the list. 
The behaviour of this function should be exactly like the list.count() method. You may NOT use any built in list methods for this problem.
"""

# Function Dec.
def get_count(L, element):
    count = 0
    # Accessing range & Logic
    for i in L:
        if i == element:
            count += 1
    return count
