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

# class BankAccount:
#     def __init__(self, balance, accountNumber):
#         self.balance = balance
#         self.accountNumber = accountNumber

#     def depositFunds(self, funds):
#         self.balance += funds
#         print(f"You deposited {funds} dollars into your bank account.")

#     def withdrawFunds(self, funds):
#         self.balance -= funds
#         print(f"You withdrew {funds} dollars from your bank account.")

#     def transferFunds(self, account, funds):
#         self.balance -= funds
#         account.depositFunds(funds)
        
       
# blakeChecking = BankAccount(10_000, 1112223344)
# print(blakeChecking.balance)

# blakeChecking.depositFunds(1300)
# print(blakeChecking.balance)

# blakeChecking.withdrawFunds(5000)
# print(blakeChecking.balance)

# blakeSavings = BankAccount(20_000, 9998887766)
# blakeChecking.transferFunds(blakeSavings, 1000)
# print(blakeChecking.balance)
# print(blakeSavings.balance)

################################### To-Do List ###################################

class ToDo:
    def __init__(self):
        self.toDoList = []

    def welcomeMessage(self):
        print('''
Good for you for staying organized and setting goals!
    ''')


    def showList(self):
        print("\n***********************")   
        print("Here is your To-Do List")
        print("***********************\n")   

        if self.toDoList:
            count = 1
            for i in self.toDoList: # Looping through a Dictionary
                for k, v in i.items():
                    print(f"{count}. {k}: {v}")
                    count += 1

            print("\n***********************")   
        else:
            print("You currently have no items on your To-Do List.")

    def getOption(self):
        option = input('''
What would you like to do?\n
1. Add a task\t
2. Delete a task\t
3. Save and quit the program\n
>>>  ''')
        if option == '1':
            self.addTask()
        elif option == '2':
            self.delTask()
        elif option == '3':
            return self.quit()


    def addTask(self):
    # Adding an item
        toDoDict = {}
        item = input("What would you like to add? ")
        priority = input('What priority level should I set this task to? '
            '(1. High, 2. Normal, 3. Low) ')
        if priority == '1':
            priority = "high"
        elif priority == '2':
            priority = "normal"
        elif priority == '3':
            priority = "low"

        toDoDict[item.title()] = priority.title()   
        # Add the input to the dictionary
        self.toDoList.append(toDoDict)

    def delTask(self):
        delete = int(input("Which number would you like to delete? "))
        delIndex = delete - 1
        taskToDelete = self.toDoList[delIndex]
        del self.toDoList[delIndex]
        print(f"I just deleted {taskToDelete}.")

    def quit(self):
        q = input("Are you sure you want to quit? Y/N ").lower()
        if q == 'y':
            print("See you next time!")
            return 'q'
        else:
            print("Let's keep working!")

# Create instance of ToDo Class
toDo = ToDo()

# Opening Greeting
toDo.welcomeMessage()

# Main Loop
choice = ''
while choice != 'q':
    toDo.showList()
    choice = toDo.getOption()
    
