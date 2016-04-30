"""
Write a function that accepts two lists both of which consists of integers and returns the total sum of all the odd integers from both 
lists.
"""

# Function Dec.
def add_odd(L1, L2):
    L1.extend(L2)
    new_list = []
    # Accessing elements of new list
    for i in L1:
        # Logic
        if i%2 != 0:
            new_list.append(i)
        total_sum = sum(new_list)
    return total_sum
