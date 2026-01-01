#Take input
rows = int(input("Enter the number of rows: "))

print("Mirrored Right Angled Triangle")

#outer loop to handle number of rows
for i in range(1, rows + 1):

    #inner loop to print spaces
    for j in range(1, rows - i + 1):
        print(" ", end=" ")

    #inner loop to print stars
    for k in range(1, i + 1):
        print("*", end=" ")

    print()   #move to next line
