# take input from the user
num = int(input("Enter a decimal number: "))

# copy the number
temp = num

# initialize binary result
binary = ""

# convert decimal to binary using while loop
while temp > 0:
    rem = temp % 2
    binary = str(rem) + binary
    temp = temp // 2

# display the result
print("Binary of", num, "is =", binary)
