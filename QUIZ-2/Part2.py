# Type your code here
val = input('Enter a int:')

age = int(val)
if (age <= 0):
   print ("UNBORN")
elif (age > 0) and (age <= 150):
   print ("ALIVE")
elif (age>150):
   print ("VAMPIRE")
