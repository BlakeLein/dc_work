########################################################### To Do List ###########################################################
import json

toDo = {}
count = 1

def getInput(count):
    option = int(input('''
    What would you like to do?\n
    1. Add a task\t
    2. Delete a task\t
    3. Save and quit the program
    >>>  '''))

    if option == 1:
        action = addTask(count)
        return action
    if option == 2:
        action = deleteTask(count)
        return action
    if option == 3:
        action = saveAndQuit()
        return action

def addTask(count):
    name = input("What is the name of the task? ") # Take in the name
    priority = input("What is the priority for this task? (high, normal, low) ") # Take in the priority
    toDo[str(count)] = f"{name.title()}: {priority.title()}" # Add to the dictionary in a format
    count += 1

    

def deleteTask(count):
    getTaskFormat(count)
    task = input("Select the number of the task you want to delete: ")
    if task in toDo:
        del task
        print("Task deleted.")
    

    
def viewTasks():
    print("Here is your list of tasks and their priority: \n")
    
    if toDo == None:
        print("You don't have any items in your To-Do list.")
    else:  
        getTaskFormat()
        
        

def getTaskFormat():
    for key, value in toDo.items():
            print(f"{key}. {value}")
            

def saveAndQuit():

    return 'quit'
    
# def loadAndReadList():
#     filename = 'toDoList.txt'
#     with open(filename) as f:
        



    # loadList()

viewTasks()

while True:
    if getInput(count) == 'quit':
        break
    viewTasks()
