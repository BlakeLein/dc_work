#Ex 1: Multiply Vectors
list1 = [2, 4, 5]
list2 = [2, 3, 6]
ansList = []

i = 0
while i < len(list1):
    ansList.append(list1[i] * list2[i])
    i += 1

print(ansList)