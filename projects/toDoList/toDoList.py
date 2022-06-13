### To-Do List App ###
### Developed Summer 2022 by Blake Lein ###
import json

toDoList = []


def welcomeMessage():
    print('''
Good for you for staying organized and setting goals!
    ''')

def getAndStoreUsername():
    username = input("Please enter your username: ").lower()
    return username
    

def loadList(username):

        load = input("Would you like to load a previous list? (Y/N) ").lower()
        while load != 'y' and load != 'n': # While loop to prevent any other kind of input
            load = input("I'm sorry, that is not an option. Please select Y or N. ").lower() 
        if load == 'y': #If yes, load the list that is attached to that username.
            filename = f'{username}.json'
            with open(filename) as f:
                file = json.load(f)
                toDoList = file
                return toDoList
        elif load == 'n':
            return

def showList(toDoList):
    print("\n***********************")   
    print("Here is your To-Do List")
    print("***********************\n")   

    if toDoList:
        count = 1
        for i in toDoList:
            for k, v in i.items():
                print(f"{count}. {k}: {v}")
                count += 1

        print("\n***********************")   
    else:
        print("You currently have no items on your To-Do List.")

def getOption(option):
    if option == '1':
        addTask()
    elif option == '2':
        delTask()
    elif option == '3':
        return saveAndQuit()


def addTask():
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
    toDoList.append(toDoDict)

def delTask():
    delete = int(input("Which number would you like to delete? "))
    delIndex = delete - 1
    taskToDelete = toDoList[delIndex]
    del toDoList[delIndex]
    print(f"I just deleted {taskToDelete}.")

def saveAndQuit():
    q = input("Are you sure you want to quit? Y/N ").lower()
    if q == 'y':
        save = input("Would you like to save your progress? Y/N ").lower()
        if save == 'y':
            print("Saving your progress.....")
            filename = f'{username}.json'
            with open(filename, 'w') as f:
                json.dump(toDoList, f)
            print("Your preogress has been saved!")
            print("See you next time!")
            return 'q'
    print("See you next time!")
    return 'q'
        

# Main Loop
choice = ""
welcomeMessage()
username = getAndStoreUsername()
loadedList = loadList(username)
showList(loadedList)

while choice != 'q':
    showList(toDoList)
    choice = input('''
What would you like to do?\n
1. Add a task\t
2. Delete a task\t
3. Save and quit the program\n
>>>  ''')
    outcome = getOption(choice)
    choice = outcome
