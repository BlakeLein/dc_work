# # // Write a function that takes in a string of lowercase letters
# # // and returns the index of the string's first non-repeating character.
# # // If the input string does not have any non-repeating characters,
# # // your function should return -1.
# string = "abcjja"

# def nonRepeating(string):
#     # stringList = list(string)
#     count = dict()
#     for s in string:
#         if s not in count:
#             count[s] = 1
#         else:
#             count[s] += 1
#     for s in string:
#         if count[s] == 1:
#             return f"{s}, {string.index(s)}"
#     return "-1"

# print(nonRepeating(string))

# # Tandem Bicycle: ---- #You can compare t
# redShirtSpeeds = [10, 6, 4, 11, 2]
# blueShirtSpeeds = [6, 7, 3, 14, 5]
# fastest = False

# def tandemBicycle(red, blue, fastest):
#     red.sort() # Sort both lists low to high
#     blue.sort()
#     combined = [] # Make a new list to add the desired values to.
#     if fastest == True: # If we want the fastest, reverse one of the lists.
#         blue.reverse()
#     for i in range(len(red)): #Loop through the number of items in a list.
#         if red[i] > blue[i]: # If the red index is more than the matching blue, add red to the list.
#             combined.append(red[i])
#         if blue[i] > red[i]: # If the blue index is more than the matching red, add blue to the list.
#             combined.append(blue[i])
#         if blue[i] == red[i]: #If the are equal, add blue (red is also fine; they are equal so it doesn't matter)
#             combined.append(blue[i])
    
#     return(sum(combined)) #Return the sum of the new list. It either returns the fastest or slowest possible speeds.

# print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest))

# # This function starts by taking 2 lists. We want to compare each value in the list to each other and get the fastest possible speed or the lowest possible speed.

# # Using a for loop with the range of the list, we can compare each index in the lists to each other and pluck out the higher number.

# # By reversing one of the lists, we are able to compare one lowest-to-highest to another highest-to-lowest list. The highest number always gets picked.

# # When the lists are not reversed and compared, You are comparing the lowest number of each list with the corresponding indexed value on the other list. We have to take the fastest still --
#     # so we pluck out the fastest.