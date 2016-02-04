# Type your code here
val = input('Enter:')

n = int(val)
if (n%2 == 0) and (n%3==0):
    print ("BOTH")
elif (n%2 == 0) or (n%3 == 0):
    print ("ONE")
elif (n%2 != 0) and (n%3 != 0):
    print ("NEITHER")
