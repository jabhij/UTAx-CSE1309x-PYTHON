# Importing math 
import math
def mag(vector):
    x = vector[0]
    y = vector[1]
    z = vector[2]
    # Rest 
    mag = math.sqrt(x**2 + y**2 + z**2)
    return (mag)
