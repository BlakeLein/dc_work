toDoList = []

def showList():
    print("\n**************")   
    print("Here is your updated To-Do List:")
    print("**************\n")   

    if toDoList:
        count = 1
        for i in toDoList:
            for k, v in i.items():
                print(f"{count}. {k}: {v}")
                count += 1

    # Assign the task to an index and format neatly:

# Main Loop
while True:
    showList()
    
    option = int(input('''
    What would you like to do?\n
    1. Add a task\t
    2. Delete a task\t
    3. Save and quit the program
    >>>  '''))

    if option == 1:
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
 
    # showList()
        
    # Delete an item
    if option == 2:
         # Get item to del and delete.
        delete = int(input("Which number would you like to delete? "))
        delIndex = delete - 1
        taskToDelete = toDoList[delIndex]
        del toDoList[delIndex]
        print(f"I just deleted {taskToDelete}.")

    if option == 3:
        print("We have saved your to do list! See you next time!")        
        break
            
    



    