# define a function to check for shutdown
def shutdown(command):

    if command == "yes":
        return "Shutting down"

    elif command == "no":
        return "Shutdown aborted"

    else:
        return "Sorry"

# display result
print(shutdown("yes"))
print(shutdown("no"))
print(shutdown("xyz"))
