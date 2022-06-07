#Ex 1:

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

#Ex 2:
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

#Ex 3:
# coins = 0
# while True:
#     print(f"You have {coins} coins.")
#     another = input("Would you like another? (y or n) ")
    
#     if another == 'y':
#         coins += 1
#     elif another == 'n':
#         print("Okay, bye.")
#         break

#Ex 4:
