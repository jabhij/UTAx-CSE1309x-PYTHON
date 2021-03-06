"""
Write a function that accepts two (matrices) 2 dimensional lists a and b of unknown lengths and returns True if they can be multiplied 
together False otherwise. Hint: Two matrices a and b can be multiplied together only if the number of columns of the first matrix(a) is 
the same as the number of rows of the second matrix(b). The input for this function will be two 2 Dimensional lists. 
For example if the input lists are:

a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]
     
Then your function should return a boolean value:
 True
 
"""

def multiplication_check(mat1, mat2):
    # Counting rows and columns
    columns_count = len(mat1[0])
    rows_count = len(mat2)
    # Checking 
    if columns_count == rows_count:
        return True
    else:
        return False
