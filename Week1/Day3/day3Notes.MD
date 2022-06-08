# Day 3 Notes - 6/8/2022

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

```
name = "Blake Lein"
print(name[0])
```

Output is

```
B
```

```
dictionary = "key": "value"
```
