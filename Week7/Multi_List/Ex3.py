"""
Write a function that accepts a 2D list of integers and returns the maximum EVEN value for the entire list. You can assume that the number
of columns in each row is the same. Your function should return None if the list is empty or all the numbers in the 2D list are odd. 
Do NOT use python's built in max() function.

"""

# Type your code here
def even_val(L):
    if not L:
        return None
    new_list = []
    for row in range(len(L)):
        for col in range(len(L[0])):
            if L[row][col] % 2 == 0:
                new_list.append(L[row][col])
    return new_list

def max_even_val(new_list):
    max_even = new_list[0]
    for i in new_list:
        if i > max_even:
            max_even = i
    return max_even
