class ToDo:
    """A Class for our To-Do List App"""
    def __init__(self):
        """Initialize the empty to-do list we are starting with."""
        self.toDoList = []

    def welcomeMessage(self):
        """Greet the user."""
        print('''
Good for you for staying organized and setting goals!
    ''')


    def showList(self):
        """Returns formatted To-Do List. Assigns task to 
        number."""
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
        """Get user option and direct to necessary action."""
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
        """Receives user task and adds to master To-Do list."""
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
        """Delete task based on position in list."""
        delete = int(input("Which number would you like to delete? "))
        delIndex = delete - 1
        taskToDelete = self.toDoList[delIndex]
        del self.toDoList[delIndex]
        print(f"I just deleted {taskToDelete}.")

    def quit(self):
        """Exits program after double-checking."""
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