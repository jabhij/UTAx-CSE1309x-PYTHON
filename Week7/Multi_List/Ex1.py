"""
Write a function which accepts a 2D list of numbers and returns the sum of all the number in the list You can assume that the number of 
columns in each row is the same. (Do not use python's built-in sum() function).

"""

# Function Dec.
def add_list(L):
    total_sum = 0
    # Accessing every row 
    for row in range(len(L)):
        # Accessing every column
        for col in range(len(L[0])):
            # Sum
            total_sum += L[row][col]
    return total_sum
