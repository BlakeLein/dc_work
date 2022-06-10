# Function practice

# def studentNameBlake(listOfResponsibilities = [], arg2 = "string", arg3=''):
#     dateOfBirth = '1992'

#     for item in listOfResponsibilities:
#         print(item)
#         print(dateOfBirth)

#     return True

# list = ["go to work"]
# studentNameBlake(list, "hi", "lol")
# info = studentNameBlake()

# print(studentNameBlake)

# dicitonary = {
#     "First Name": "Blake",
#     "Last Name": "Lein",
#     "City": "Pearland",
#     "Favorite Food": "Steak",
#     "Hobbies": "Reading and Video Games",
# }

# def getInfo(dictionary):
#     for key, value in dictionary.items():
#         print(f"Your {key}: {value}")

# getInfo(dicitonary)

# def getInfo2(first="", last="", city="", food="",hobbies=""):
#     print(f'''
#     {first}
#     {last}
#     {city}
#     {food}
#     {hobbies}
#     ''')

# getInfo2("Blake", "Lein", "Pearland", "Steak", "Reading")

# first = input("What is your first name? ")
# last = input("What is your last name? ")
# city = input("Where do you live? ")
# food = input("What is your fav food? ")
# hobby = input("What is your hobby? ")

# def getUserInfo(first="", last="", city="", food="",hobbies=""):
#     print(f'''
#     {first}
#     {last}
#     {city}
#     {food}
#     {hobbies}
#     ''')

# getUserInfo(first, last, city, food, hobby)

################## Dictionaries ##################

# #Ex 1:
# dict = { 'Alice': '703-493-1834', 'Bob': '857-384-1234', 'Elizabeth': '484-584-2923' }

# # Print Elizabeth's phone number.
# print(f"Elizabeth's phone number is {dict['Elizabeth']}.")

# # Add an entry to the dictionary: Kareem's number is 938-489-1234.
# dict["Kareem"] = "938-489-1234"
# print(dict)

# # Delete Alice's phone entry.
# del dict['Alice']
# print(dict)

# # Change Bob's phone number to '968-345-2345'.
# dict['Bob'] = '968-345-2345'
# print(dict)

# # Print all the phone entries.
# print(dict)

# #OR

# for key, value in dict.items():
#     print(f"{key}: {value}")

# # In this exercise, are you using dynamic keys or fixed keys?

# #Ex 2:
# ramit = { 
#     'name': 'Ramit', 
#     'email': 'ramit@gmail.com', 
#     'interests': ['movies', 'tennis'], 
#     'friends': [ 
#         { 'name': 'Jasmine', 
#         'email': 'jasmine@yahoo.com', 
#         'interests': ['photography', 'tennis'] }, 
#         { 'name': 'Jan', 
#         'email': 'jan@hotmail.com', 
#         'interests': ['movies', 'tv'] } 
#         ] 
#         }
# # Write a python expression that gets the email address of Ramit.
# print(ramit['email'])

# # Write a python expression that gets the first of Ramit's interests.
# print(ramit['interests'][0])

# # Write a python expression that gets the email address of Jasmine.
# print(ramit['friends'][0]['email'])

# # Write a python expression that gets the second of Jan's two interests.
# print(ramit['friends'][1]['interests'][1])

# # In this exercise, are you using dynamic keys or fixed keys?

# Letter Summary:
# Letter Summary: Write a letter_histogram program that asks the user for input, 
# and prints a dictionary containing the tally of how many times each letter in the alphabet was used in the word. For example:

# $ python letter_histogram.py 
# Please enter a word: banana {'a': 3, 'b': 1, 'n': 2} 
# In this exercise, are you using dynamic keys or fixed keys


# def letter_histogram(word):
#     d = dict() # Create an empty dictionary
#     for w in word: # Loop through each letter in the passed string
#         if w not in d: # Conditional: If the letter is not already in the dictionary, add it as a key and set the start value to 1
#             d[w] = 1
#         else:
#             d[w] += 1 # Conditional: If the letter is already in the new dictionary, increase the value by 1 (counting up)
#     return d #Return the new dictionary

# print(letter_histogram('apple'))

# # Word Summary: 
# def word_histogram(sentence):
#     d = dict() #Start with an empty dictionary because this is what you want to return
#     words = sentence.split() # Split the sentence into words.
#     for w in words: #Loop through each word.
#         if w not in d: 
#             d[w] = 1 # If the word is not in the dictionary, add it to the dictionary.
#         else:
#             d[w] += 1 # If the word is already in the dictionary, increase the occurance by 1.
#     return d # Return the empty dictionary.

# print(word_histogram("I love to love the love to"))