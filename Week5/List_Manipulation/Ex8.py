"""
Write a function that accepts two positive integers a and b and returns a list of all the even numbers between a and b (including a and 
not including b).
"""

# Function Dec.
def even_num(a, b):
    # A blank list
    L = []
    # Accessing the range
    for num in range(a, b):
        # Logic and adding Even
        if num % 2 == 0:
            L.append(num)
    return L
