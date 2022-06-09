# Day 3 Notes - 6/8/2022

# Using the range(len(list))!

## Lists

- You access things inside of lists using an index.
- You can store any kind of data type in a list.

#### Storage Considerations and Other Cons

- Lists have the capability of taking our best computers to the highest capacity.
- When lists are stored, they have to be stored somewhere where all items in the list can be stored TOGETHER.
- As the list gets bigger, so does the requirement for storage.
- You can only traverse a list by looking at every item in a row. You can access one-at-a-time or in a certain range, but you still have to cylce through each item in that range - no skipping over.

##Big - O Notation Concepts

- Computers look at TIME (how long) and SPACE (how much room). They don't track speed, they track the worst-case possible situation, because if we can accept the worst possible scenario, we are good.
- BIG O Notation is about Time and Space complexity in providing the worst-case scenario. These are all formulas for worst-case scenario.

  - O(i) is considered an instant, super easy task for a computer. This includes things like:

    1. Reading code
    2. Assigning variables
    3. Simple operations

  - O(n) is as difficult as 'n', where n is the size of what you're doing. A small item is less, a big item takes more work.

### Big-O Notation Examples for Lists:

- Creating a list takes o(n) compl

## More Lists!

- .append() is a built-in function that adds an item to the end of a list. The argument is what you want to add to the list.
- .extend() can be used to combine two lists.
- You can also concatenate two lists by simply adding them together.
- You can use a for loop to loop through the list and individually add items to a new list.
- List Comprehension is a shorthand way to create new list with a for loop in one line of code.

You can iterate over a list; you can also iterate over:

- A string
- A dictionary

# Reading Review of Sequences, Tuples, Lists

### Lists

- Lists are mutable (modifiable) sequences - versatile, general-purpose collection
- Tuples are immutable sequences - best for representing a something with a fixed size
- You can access an item in the list with it's index. If you try to access an item that isn't there, it throws an IndexError.
- A negative index number will work backward from the end of the list.

### Sequences

- Sequence = word to describe a functional superset
- There are six sequence types: strings, Unicode strings, lists, tuples, buffers, and xrange objects.
- A list is a sequence, but a sequence isn't always a list.
- Sequences are index-able, slice-able, length-able, and iterable!

### Slicing a list

- You can access certain parts of a list by slicing. [0:0:0]
- The first number is where the you want to start (including that index)
- The second number is where you want to end (NOT INCLUDING THAT INDEX!)
- The third number is how you want to move through. -1 is from the end. 2 is every other. 3 is every 3rd and so forth.

### Looping (Iterating) through a list

- While Loop

```
todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

index = 0 # Begin with index 0

while index < len(todos):

    todo = todos[index]

    print("%d: %s" % (index + 1, todo))

    index += 1
```

- Notice:

  - Counter variable
  - Use len(list)

- For Loop

```
todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

count = 1

for todo in todos:

    print("%d: %s" % (count, todo))

    count += 1
```

- Notice
  - There is a counter variable so we can still number our items in the list for the user.

### Modifying a List

- .append() adds an item to the end of a list
- .extend() uses elements from another list
- Concactenate two lists together
- del list[] to delete items(s) in a list
- list() converts a string to a list

Note:

- You can not change the index of a string.
- To make a list a string use: ''.join(list) - Must start with an empty string!

### Tuples

- Like a list, but immutable. They cannot be altered.
- Notated with parentheses instead of brackets.
- You cannot remove items in a tuple, but you can reassign items.

# Sequences
