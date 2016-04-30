"""
Write a function that accepts two input lists and returns a new list which contains only the unique elements from both lists.
"""

# Function Dec.
def get_unique(L1, L2):
    L1.append(L2)
    new_list = []
    # Accessing the List
    for i in L1:
        # Logic
        if i not in new_list:
            new_list.append(i)
    return new_list
