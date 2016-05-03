"""
Write a function named crazy_list that accepts a list as parameter and returns a boolean (either True or False) based on whether or not the
list is the same forward and backwards. You may NOT use list.reverse() method. 

For example, if the list received by the function is:

[5, 6, 8, 9, 'PYTHON', 9, 8, 6, 5] 
(Notice how the list is exactly the same whethere you read it from left to right, or from right to left) Then your function should return 
the Boolean
True 
however, if the list recieved by the function is something like this:
[4, 5, 6, 7, 8, 4, 5, 2] 
(Notice how the list is NOT the same when reading from left to right vs right to left) In this case, your function should return the Boolean
False 
"""

# Function Dec.
def crazy_list(L):
    length = len(L)
    # For EVEN Length
    if length % 2 == 0:
        mid = int(length / 2)
        # List Slicing for Comparison
        sec1 = L[0: mid]
        sec2 = L[-1: mid+1]
    # If ODD
    else:
        mid = int(length / 2)
        # List Slicing for Comparison
        sec1 = L[0: mid]
        sec2 = L[mid+1::][::-1]

    if sec1 == sec2:
        return True
    else:
        return False
