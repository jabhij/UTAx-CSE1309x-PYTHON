"""
Write a function that accepts two positive integers a and b (a is smaller than b)and returns a list that contains all the odd numbers 
between a and b (including a and including b if applicable) in descending order.
"""

# Function Decl.
def odd_num(a, b):
    num = b
    # An empty list
    l = []
    # Logicc and adding odds
    while num >= a:
        if num % 2 != 0:
            l.append(num)
        num -= 1
    return l
