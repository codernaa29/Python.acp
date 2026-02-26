# define a function to calculate due amount
def due_amount(bill, paid):

    if paid >= bill:
        return 0
    else:
        return bill - paid


# take user input
bill = int(input("Enter the bill amount: "))
paid = int(input("Enter the paid amount: "))

# display result
print("Customer due amount is =", due_amount(bill, paid))