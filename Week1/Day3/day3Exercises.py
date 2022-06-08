# listOfStudents = ["Amanda", "Andrea", "Blake", "Carlos", 
# "Ethan", "Jason", "Olivia", "Rahmin", "Stacy", "West"]

# listOfStudents.append("Bob")
# print(listOfStudents)

# Square the numbers in this list
numbers = [1, 2, 3, 4, 5, 6, 7]
# Output [1, 4, 9, 16, 25, 36, 49]

squareList = [number**2 for number in numbers]
print(squareList)
    

# Remove all empty strings in this list
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# output ["Mike", "Emma", "Kelly", "Brad"]
for i in list1:
    if i == '':
        list1.remove(i)
print(list1)

# Add new item to list after a specified item
list2 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# output [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

list2[2][2].append(7000)
print(list2)

# Replace list's item with new value if found
list3 = [5, 10, 15, 20, 25, 50, 20]
output = [5, 10, 15, 200, 25, 50, 20]

# list3[3] = 200
# print(list3)

for i in range(len(list3)):
    if list3[i] == 20:
        list3[i] = 200
        break
print(list3)

# Remove all occurrences of a specific item from a list.
list4 = [5, 20, 15, 20, 25, 50, 20]
# output [5, 15, 25, 50]
for i in list4:
    if i == 20:
        list4.remove(i)
print(list4)