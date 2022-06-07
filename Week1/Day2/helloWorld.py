from multiprocessing.sharedctypes import Value


print("Hello World")

def sayHi():
    print("Hi!")

sayHi()

name = "Joe"
true = True
number = 14

students = [
    "Jason", "Blake", "Carlos", "Stacy", "Amanda"
]

# How to access Blake:
print(students[1])

dictionary = {
    "key": "value",
    "key_1": true,
    "key_2": 14,
    "students": students
}

key = dictionary["key"]
print(dictionary["students"][0])

print(data["president"]["name"])
print(data["president"]["location"][0])