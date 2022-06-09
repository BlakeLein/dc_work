#Ex 1: Multiply Vectors
list1 = [2, 4, 5]
list2 = [2, 3, 6]
ansList = []

i = 0
while i < len(list1):
    ansList.append(list1[i] * list2[i])
    i += 1

print(ansList)

# target = 5
# def twoSum(list1, list2, target):
#       for i in list1:
#         for j in range(i, len(list2)):
#             if i + j == target:
#                 return [i, j]


# print(twoSum(list1, list2, target))
# #Ex 2: 