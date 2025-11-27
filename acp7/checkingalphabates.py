# Take input from the user
character = input("Enter a character: ")

# Check if the character is an alphabet
if ('a' <= character <= 'z') or ('A' <= character <= 'Z'):
    print(character, "is an alphabet.")
else:
    print(character, "is not an alphabet.")
