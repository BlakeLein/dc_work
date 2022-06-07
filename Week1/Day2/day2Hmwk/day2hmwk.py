#Coin Flip:
from random import randint

def coinFlip():
    print("You flipped a coin!")
    odds = randint(1, 2)
    if odds == 1:
        print("It's Heads!")
    elif odds == 2:
        print("It's Tails!")

coinFlip()

#Even Odd:
def evenOrOdd():
    print("If you tell me a number, I'll tell you if it's even or odd.")
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("That's an even number!")
    else:
        print("That's an odd number!")

# On a loop:
while True:
    evenOrOdd()

    again = input("Would you like to play again? (y/n) ")
    if again == 'n':
        break

#Dice Roller
from random import randint

def rollDice(sides):
    roll = randint(1, sides)
    print("Rolling...")
    print(roll)

while True:
    print("Let's roll a dice!")
    sides = int(input("How many sides should it have? (2, 20) "))
    
    if sides > 20 or sides < 2:
        print("Please pick a number between 2 and 20.")
        
    else:
        rollDice(sides)
        again = input("Would you like to roll again? (y/n) ")
        if again == 'n':
            break

  
