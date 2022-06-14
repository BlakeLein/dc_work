# class User:
#     def __init__(self, firstName, lastName, addresses=[]):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.addresses = addressesd

#     def addAddress(self, address):
#         self.addresses.append(address)

#     def displayAddresses(self):
#         for address in self.addresses:
#             print(address)



# class Address:
#     def __init__(self, street, city, state, zipCode):
#         self.street = street
#         self.city = city
#         self.state = state
#         self.zipCode = zipCode


# blake = User("Blake", "Lein")
# pearland = Address("Ivy Arbor", "Pearland", "Texas", 77581)
# blake.addresses.append(pearland)
# print(blake.addresses[0])


# Create a relationship between User and Address in a way a single user can have multiple addresses.
# Add a new method/function to User class called add_address(self, address) which would take an address as an argument and add it to a list/array of addresses.
# Add another method to the User class called display_addresses(self) which would display all the address of that user.

class BankAccount:
    def __init__(self, balance, accountNumber):
        self.balance = balance
        self.accountNumber = accountNumber

    def depositFunds(self, funds):
        self.balance += funds
        print(f"You deposited {funds} dollars into your bank account.")

    def withdrawFunds(self, funds):
        self.balance -= funds
        print(f"You withdrew {funds} dollars from your bank account.")

    def transferFunds(self, account, funds):
        self.balance -= funds
        account.depositFunds(funds)
        
       
blakeChecking = BankAccount(10_000, 1112223344)
print(blakeChecking.balance)

blakeChecking.depositFunds(1300)
print(blakeChecking.balance)

blakeChecking.withdrawFunds(5000)
print(blakeChecking.balance)

blakeSavings = BankAccount(20_000, 9998887766)
blakeChecking.transferFunds(blakeSavings, 1000)
print(blakeChecking.balance)
print(blakeSavings.balance)
    
