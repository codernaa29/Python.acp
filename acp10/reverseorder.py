# take input from the user
num = int(input("Enter a number: "))

# initialize count
count = 0

# copy the number
temp = num

# count total digits using while loop
while temp > 0:
    count = count + 1
    temp = temp // 10

# display the result
print("Total digits =", count)
