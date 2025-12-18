# Input the base number
base = int(input("Enter the base number: "))

# Input the power (n)
n = int(input("Enter the value of n: "))

# Initialize result
result = 1

# Loop to calculate power
for i in range(1, n + 1):
    result = result * base

# Print the result
print(base, "raised to the power of", n, "is:", result)
