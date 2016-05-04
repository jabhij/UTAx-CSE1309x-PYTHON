"""
Write a program that asks the user for an input 'n' and prints a square of n by n asterisks "*". For example if the user enters 5 then the
output should look like the following: Note that there should be no spaces between the asterisks

*****
*****
*****
*****
*****

"""

# Getting User Input
n = int(input('Enter a Number: '))
i = 1
# Condition
while i <= n:
    # Logic for Pattern
    print (n * '*')
    i += 1
