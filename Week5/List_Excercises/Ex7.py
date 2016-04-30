"""
Write a function that accepts a list that contains positive integers and returns a new list which contains all the elements from original 
list but adds 1 to those elements which are odd. For example if :

input_list = [12, 3, 4, 5, 6]
Then your function should return a list such as:
[12, 4, 4, 6, 6]
"""

# Function Dec.
def mod_list(L):
    # New list -- Slcing on the L
    new_list = L[:]
    # Accessing elements of new list
    for i in range(0, len(new_list)):
        # Logic
        if new_list[i] % 2 != 0:
            new_list[i] += 1
    return new_list
