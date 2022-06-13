# OOP Notes - 6/12/2022

- Object oriented programming is good for simulating real-life situations.
- Classes hold the information, and we access that information by creating an instance of that class and assigning it to a variable.
- A method is a function inside a class.
- Encapsulation is the practice of bundling data, methods, and attributes into a single unit. Because it is in this unit, everything inside can access everything else inside.

### The Constructor Method

- The first method for each class is the constructor method. This takes the parameters passed to the class when the instance was created and initializes them.
- Whatever parameters the constructor method takes is what arguments you need to pass it when you declare an instance of the class.
- You can of course set defaults for these as you would a normal function.

### Other Methods

- Every Method in a class must have at least the parameter 'self'. 'self' ALWAYS come first!
- Methods inside of a class should have one, specific purpose. Do not over fill methods.
- Any parameters you wish to pass to methods can instead be added to the **init**() method. If you want them to be changeable inside that method, you can add them as parameters to the **init**() method. You do not have to do this.

### Inheritance

- Used to make spcialized versions of classes.
- To make an inheritance, make a new class and include the parent class in the parentheses.

```
class newClass(parentClass):
    Begin code
```

- A class that inherits is called a sub-class.
- The parent class is then know as the super-class.
- You can add to a sub class all you want.
- You can alter a sub class all you want. Simply make the same thing and redefine it.
- You can create a new **init**() method for your subclass, but what if you still want access to the **init**() method for the super class? Sometimes we do not want to totally override. Below you can see how we have access to a new **init**() method, but

```
 class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, hunger=5, cuddle_level=1): #Subclass attribute
        super().__init__(name, fullness, 100, hunger, 1) # Superclass attribute
        self.cuddle_level = cuddle_level # New att for sub class we need to initialize
```

- When should we add new attributes to the super class vs. an individual subclass?
  - If you want to change EVERYTHING, change the superclass. If you want to change one or a few things, change the subclasses.

### Polymorphism

- Passing methods from a parent class to a subclass.
- As long as classes or superclasses define a particular method, the instance can respond to that message.
- For instance, if all of our classes have a **str**() method, we can print every instance of that class in one print statement and it will display the info for each independent class.
- You don't have to know what kind of thing it is. You only have to pass it a message that it can respond to.

### **str**() Method:

- This built-in or 'magic method' in Python is designed to represent the class objects as a string.
- The string method should be defined in a way that is easy to read and outputs all the members of the class.
- Also used as a debugging tool when the members of a class need to be checked.
- It is up to the developer to format what is printed, but when you called a print statemtent: print(myClass), it will display what you put in the **str** method.

### Method Resolution

- When you perform a function call, such as benji.get_love(), Python checks if that object knows how to get_love(). If the class benji belongs to didn't define that method, Python checks the superclass. If that class didn't define it, Python checks the superclass of the superclass.
- It does this until it finds the method or runs out of superclasses to check.

### Classes helping classes

- It is a good idea to consider storing information in another class when your attributes start to have attributes.
- You can create a separate module and do some importing to keep everything nice and organized.
