# Take input from user
radius = int(input("Enter the radius of the circle: "))

# create function to calculate circumference
def circumference(r):
    result = 2 * 3.14 * r
    print("Circumference of the circle is =", result)

# call the function
circumference(radius)
