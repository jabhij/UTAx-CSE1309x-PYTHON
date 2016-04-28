"""
Write a function that accepts a positive integer n as function parameter and returns True if n is a prime number, False otherwise. 
Note that zero and one are not prime numbers and two is the only prime number that is even. 
"""

# Function Declaration
def check_prime(number):
    # Conditional Checks
    if number == 2:
        return True
    if number <= 1:
        return False
    # Accessing numbers in the range
    for i in range(2, number):
        # Logic
        if number % i == 0:
            return False
    return True
