"""
Write a function that accepts two positive integers as function parameters and returns their least common multiple (LCM).
The LCM of two integers a and b is the smallest (non zero) positive integer that is divisible by both a and b.
For example, the LCM of 4 and 6 is 12, the LCM of 10 and 5 is 10. 
"""

# Function Declaration
def get_lcm(a, b):
    # A copy of a
    temp = a
    # Condition and Logic
    while temp % b != 0:
        temp += a
    return temp
