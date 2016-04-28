"""
Write a function that accepts a list of integers as parameter. Your function should return the sum of all the odd numbers in the list. If there are no odd numbers in the list, your function should return 0 as the sum. 
"""

# Function Declaration
def parameter_list(L):
    get_sum = 0
    # Accessing List Elements
    for number in L:
        # Logic
        if number%2 != 0:
            get_sum += number
    return get_sum
