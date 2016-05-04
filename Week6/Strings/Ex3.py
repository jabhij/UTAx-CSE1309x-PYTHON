"""
Write a program using while loops that asks the user for a positive integer 'n' and prints a triangle using numbers from 1 to 'n'. 
For example if the user enters 6 then the output should be like this :

(There should be no spaces between the numbers)

1
22
333
4444
55555
666666
"""

# Getting User Input
n = int(input('Enter a Number: '))
i = 1
# Condition
while i <= n:
    # Logic for Pattern
    print (i * str(i))
    i += 1
