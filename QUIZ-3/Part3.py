"""
Write a program that asks the user for a positive number 'n' as input. Assume that the user enters a number greater than or equal to 3 and print a triangle as described below. For example if the user enters 6 then the output should be:
*
**
***
****
*****
******
*****
****
***
**
*
"""

# User Input
n = int(input('Enter any Number: '))
# Logic - Upper Pattern
for i in range(n+1):
    print '*' * i
# Logic - Lower Pattern
for j in range(n-1, 0, -1):
    print '*' * j
