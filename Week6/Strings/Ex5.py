"""
Write a program that asks the user for an input 'n' (assume that the user enters a positive integer) and prints only the boundaries of the
triangle using asterisks "*" of height 'n'. For example if the user enters 6 then the height of the triangle should be 6 as shown below and
there should be no spaces between the asterisks on the top line:

******
*   *
*  *
* *
**
*

"""

# Getting User Input
n = int(input('Enter a Number: '))
# Printing the first line
if n > 1:
    print n * '*'
    # Accessing range
    # Logic for the rest of the pattern
    for i in range(n-1, 1, -1):
        print '*' + (i - 2)*' ' + '*'
    print '*'
