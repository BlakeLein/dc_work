# Ex 1:

# bill = float(input("Total bill amount? "))
# service = input("Level of service? "
# "(Enter good, fair, or bad) ")

# def getTip(bill, service):
#     if service == 'good':
#         tip = bill * 0.20
#         total = bill + tip
        
#     elif service == 'fair':
#         tip = bill * 0.15
#         total = bill + tip

#     elif service == 'bad':
#         tip = bill * 0.10
#         total = bill + tip
    
#     fTip = "${:,.2f}".format(tip)
#     fTotal = "${:,.2f}".format(total)
#     print(f"Tip amount: {fTip}")
#     print(f"Total amount: {fTotal}")

# getTip(bill, service)

# Ex 2:
# bill = float(input("Total bill amount? "))
# service = input("Level of service? "
# "(Enter good, fair, or bad) ")
# people = int(input("Split how many ways? "))

# def getTip(bill, service, people):
#     if service == 'good':
#         tip = bill * 0.20
#         total = bill + tip
#         individual = total / people
        
#     elif service == 'fair':
#         tip = bill * 0.15
#         total = bill + tip
#         individual = total / people

#     elif service == 'bad':
#         tip = bill * 0.10
#         total = bill + tip
#         individual = total / people
    
#     fIndividual = "${:,.2f}".format(individual)
#     fTip = "${:,.2f}".format(tip)
#     fTotal = "${:,.2f}".format(total)
#     print(f"Tip amount: {fTip}")
#     print(f"Total amount: {fTotal}")
#     print(f"Price per person: {fIndividual}")

# getTip(bill, service, people)

# Ex 3:
# coins = 0
# while True:
#     print(f"You have {coins} coins.")
#     another = input("Would you like another? (y or n) ")
    
#     if another == 'y':
#         coins += 1
#     elif another == 'n':
#         print("Okay, bye.")
#         break

# #Ex 4:
# width = int(input("Enter the width of the box: ")) # Get the size of the box.
# height = int(input("Enter the height of the box: "))

# for i in range(height): # Outer loop to put the rows together.
#     for j in range(width): # Inner loop to create each individual row.
#         if(i == 0 or i == height - 1 or j == 0 or j == width - 1):
#             print('*', end = ' ') # (i == 0 prints first row), (i == length - 1 prints last row), (j == 0 prints first column), (j == length - 1 prints last column)
#         else:
#             print(' ', end = ' ') # Every other row and column is a space.
#     print() # Brings the next row to a new column - WHY IS THIS NOT AUTOMATIC?

# end = ' ' # Tells python to not start a new line, but to keep it on the same line.

# Ex 5:
rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()

# # Ex 6:
# for i in range(1, 11):
#     print("----------\n")
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i*j}\n")