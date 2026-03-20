# using try and except

try:
    age = int(input("Enter your age: "))

    # check even or odd
    if age % 2 == 0:
        print("Age is even")
    else:
        print("Age is odd")

# handle error
except ValueError as ex:
    print("Exception:", ex)

else:
    print("No exceptions")

finally:
    print("Program finished")