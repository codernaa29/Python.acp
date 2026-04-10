import math #importing math module

# take input from user
angle = int(input("Enter the angle in degrees: "))

# convert degree to radian
radian = angle * (3.14/180)

# display result
print("sin value is: " + str(math.sin(radian)))
print("cos value is: " + str(math.cos(radian)))
print("tan value is: " + str(math.tan(radian)))