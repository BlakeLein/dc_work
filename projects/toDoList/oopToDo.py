### To-Do List App ###
### Developed Summer 2022 by Blake Lein ###
import json

class ToDo:
    def __init__(self):
        self.toDoList = []
        self.userName = ""

    def welcomeMessage(self):
        print('''
    Good for you for staying organized and setting goals!
        ''')

    def getAndStoreUsername(self):
        self.userName = input("Please enter your username: ").lower()
        
    def loadList(self):

            load = input("Would you like to load a previous list? (Y/N) ").lower()
            while load != 'y' and load != 'n': # While loop to prevent any other kind of input
                load = input("I'm sorry, that is not an option. Please select Y or N. ").lower() 
            if load == 'y': #If yes, load the list that is attached to that username.
                filename = f'{self.userName}.json'
                with open(filename) as f:
                    file = json.load(f)
                    self.toDoList = file
            elif load == 'n':
                return

    def showList(self):
        print("\n***********************")   
        print("Here is your To-Do List")
        print("***********************\n")   

        if self.toDoList:
            count = 1
            for i in self.toDoList:
                for k, v in i.items():
                    print(f"{count}. {k}: {v}")
                    count += 1

            print("\n***********************")   
        else:
            print("You currently have no items on your To-Do List.")

    def getOption(self):
        choice = input('''
What would you like to do?\n
1. Add a task\t
2. Delete a task\t
3. Save and quit the program\n
>>>  ''')
        if choice == '1':
            self.addTask()
        elif choice == '2':
            self.delTask()
        elif choice == '3':
            self.saveAndQuit()


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

    def saveAndQuit(self):
        q = input("Are you sure you want to quit? Y/N ").lower()
        if q == 'y':
            save = input("Would you like to save your progress? Y/N ").lower()
            if save == 'y':
                print("Saving your progress.....")
                filename = f'{self.userName}.json'
                with open(filename, 'w') as f:
                    json.dump(self.toDoList, f)
                print("Your preogress has been saved!")
                print("See you next time!")
                return 'q'
        print("See you next time!")
        return 'q'
            

# Main Loop
toDo = ToDo()

toDo.welcomeMessage()
toDo.getAndStoreUsername()
toDo.loadList()


choice = ''
while choice != 'q':
    toDo.showList()
    toDo.getOption()
    
