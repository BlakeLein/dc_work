# OOP Lab

# Ex 1:

class Student:
    def __init__(self, name):
        self.name = name
        print(f"Hello {self.name}")

    def greeting(self):
        print(f"Good afternoon {self.name}! Are you ready for class today?")

# #Ex. 2:
# blake = Student("Blake")
# jason = Student("Jason")
# stacy = Student("Stacy")
# andrea = Student("Andrea")
# west = Student("West")


class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color


    def carDetails(self):
        print("Here are the details of the car.")

honda = Car("Honda", "CRV", "Black")
# print(honda.carDetails())
# print(honda.color)

class Hybrid(Car):
    def __init__(self, make, model, color, battery):
        self.make = make
        self.model = model
        self.color = color
        self.battery = battery

    def carType(self):
        print("I am a hybrid car.")


# class ElectricCar(Car):
#     def carType(self):
#         print("I am an electric car.")

rav4 = Hybrid("Toyota", "Rav4", "Gray", "Lithium")
print(rav4.make)
print(rav4.model)
print(rav4.color)
print(rav4.battery)

# tesla = ElectricCar()

# print(honda.carDetails())
# print(rav4.carType())
# print(tesla.carType())