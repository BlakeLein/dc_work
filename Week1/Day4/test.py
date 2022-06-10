toDo = {
    "hi there": "normal",
    "contemp": "high",
}

def showList():
    print("\n**************")   
    print("Here is your updated To-Do List:")
    print("**************\n")   

    # Assign the task to an index and format neatly:
    for num, (k,v) in enumerate(toDo.items(), 1):
        print(f"{num}. {k.title()}: {v.title()}")

# Main Loop
while True:
    showList()
    
    option = int(input('''
    What would you like to do?\n
    1. Add a task\t
    2. Delete a task\t
    3. Save and quit the program
    >>>  '''))

    # Adding an item
    if option == 1:
        item = input('Okay, what would you like to add to the list? ')
        if item in toDo:
            print("\nThat's already on your To-Do List.")
        else:
            priority = input('What priority level should I set this task to? '
            '(1. High, 2. Normal, 3. Low) ')
        if priority == '1':
            priority = "high"
        elif priority == '2':
            priority = "normal"
        elif priority == '3':
            priority = "low"
        # Add the input to the dictionary
        toDo[item] = priority
 
    showList()
        
    # Delete an item
    if option == 2:
         # Get item to del and delete.
        delete = int((input("Which number would you like to delete? ")))
        for num, (k,v) in enumerate(toDo.items(), 1):
            if delete == num:
                del toDo[k]
            else:
                print(f"There is no number {delete}.")
        
        
    