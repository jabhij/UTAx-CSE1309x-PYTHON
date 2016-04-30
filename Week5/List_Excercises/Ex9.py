"""
Write a function that accepts an input list and returns a new list which contains only the unique elements(Elements should only appear one
time in the list and the order of the elements must be preserved as the original list. )
"""

# Function Dec.
def get_unique(L):
    new_list = []
    # Accessing the List
    for i in L:
        # Logic
        if i not in new_list:
            new_list.append(i)
    return new_list
