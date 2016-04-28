"""
Write a function that receives a positive integer as function parameter and returns True if the integer is a perfect number, False otherwise.
A perfect number is a number whose sum of the all the divisors (excluding itself) is equal to itself. 
For example: divisors of 6 (excluding 6 are) : 1, 2, 3 and their sum is 1+2+3 = 6. Therefore, 6 is a perfect number. 
"""

# Function Declaration
def check_number(number):
    get_sum = 0
    # Getting the range of divisors
    for i in range(1, number-1):
        if number % i == 0:
            # Sum of Divisors
            get_sum += i
    # Check
    if get_sum == number:
        return True
    else:
        return False
