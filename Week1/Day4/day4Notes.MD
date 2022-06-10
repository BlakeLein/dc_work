# Class Notes Thursday, 6/9/2022

## --Pre-class reading: Dictionaries/File Manipulation--

- "Key" and "Values" make up a dictionary.
- Keys are always an immutable value (strings, numbers, etc); values can be any python value.

#### Ways to retrieve values in a dictionary:

1. [< key name >] retrieves the value for the key using the index syntax or name of key (similar to lists)

- Ex: heroName = dictionary['key']; heroName would be the value of that key.

2. .get(< key name >) retrieves the value for the key using the index syntax or name of key. .get() can take a second argument that represents the default return value if an item doesn't exist (if you don't want it to just return "None")

- Ex: heroName = dictionary.get('key')

3. .values() returns all values of a dictionary.

- Ex: values = dictionary.values()

4. .items() iterates through all the key/value pairs in a dictionary.

- For loop to iterate through a dictionary using .items():

```
for key, value in superhero.items():
    print(f"Superhero's {key} is {value"})
```

#### Working with Dictionaries

- You can use the 'in' or 'not in' keywords in conditional statements to find items in a dictionary.
- You can update an item in a dictionary by using the brackets. variable = dictionary['key'] = new_value
- Order of key/value pairs in dictionaries can change.
- Deleting a dictionary item is done with 'del'. Ex: del dictionary['key'] removes that key and value.

#### Nested Dictionaries

- Sometimes lists or other dictionaries will be nested in a dictionary.
- If a value is a list or other dictionary, you just stack your indeces. dictionary['key'][0] <-- Index of list value you want.

#### Opening a File in Python:

```
file_name = "to-do-list.txt"
with open(file_name, "r") as file_handle:
    contents = file_handle.read()
    print(contents)
```

- Here we have a text file saved to a variable "file_name".
- open() is the built-in function that performs the work.
- open() takes two arguments: the file and a mode of what you intend to do (in this case 'r' for 'read' the file).
- We are opening this file as a new name - "file_handle"
- We now want to actually read the file we opened with 'file_handle.read()'. We save this action to a new variable. The variable 'contents' contains the python code for the text file. Now we just need to print it.
- "with-as" are syntax tools that python needs to run the code.

#### The Pickle Module

- You can import the pickle module to your file.
- The pickle module can encode your Python variables so that they can be stored to a file. Pickle can also decode the data and convert it back into Python values.
- Pickle is a variable. You can use it like this:

  - pickle.dump() serializes
  - pickle.load() deserializes

(Formatting or encoding data for saving to a file or transmitting over a network is also known as SERIALIZATION.)

(The act of decoding data that has been saved to a file or transmitted over a network is known as DESERIALIZATION.)

#### Using pickle.dump()

```
import pickle

# Ending the file in ".pickle" as a reminder to use pickle module.
file_name = "to-do-list.pickle"

# Todos as a list of dictionaries
todos = [
    {
        "title": "Sand the floor",
        "priority": 1,
        "completed": True,
    },
    {
        "title": "Wax on, wax off",
        "priority": 2,
        "completed": False,
    },
    {
        "title": "Paint the fence",
        "priority": 3,
        "completed": False,
    },
]

with open(file_name, "wb") as file_handle:
    pickle.dump(todos, file_handle)
```

- Here we are passing the dump function to arguments:
  - The data to serialize ('todos' list)
  - A file handle to write to
- 'wb' stands for 'write binary'

#### Using pickle.load()

```
import pickle

# Ending the file in ".pickle" as a reminder to use pickle module.
file_name = "to-do-list.pickle"

with open(file_name, "rb") as file_handle:
    todos = pickle.load(file_handle)

    for todo in todos:
        print("------------")
        if todo["completed"]:
            print("Done:", todo["title"])
        else:
            print("Todo:", todo["title"])
```

- pickle.load() only expects one argument - The file handle where it can find the pickle data; in this case - file_handle
- "rb" stands for "read binary"

#### JSON

- You can import the JSON module to read and right the same way as an alternative to pickle. JSON does not convert to binary.

## --Class Notes--

# Functions and Why We Use Them

- Functions are things we create to do the same process over-and-over again.
- You can write the code once and just throw different variables at it.
- Parameters/arguments are totally up to you but should be meaningful.

#### Calling, Referencing, and Defining a Function

- Defining is making it.
- Calling is using it.
  - You can save a function call to a variable to store whatever that function returns. This is
    very helpful when facing issues with scope.
- Referencing a function shows you where the memory address is for that function. You can print the name
  of the function without calling it to see where it is. - You can assignt he location of the function to a variable. - You can then invoke the power of that function with that variable! - ` functionName() variable = functionName variable() # Using the power of the function in a different variable.

  #### Recursion

- Calling a function within a function.
- You use recursion when you need to iterate over something and you can't use a loop!
- The downside is that calling a function within a function can slow down a machine. A loop is always less data.
