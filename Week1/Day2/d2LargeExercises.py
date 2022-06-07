import random

# #Ex 1
# #Step 1
# secretNumber = 5
# print("I am thinking of a number between 1 and 10.")

# while True:
#     guess = int(input("What is your guess? "))

#     if guess == secretNumber:
#         print("You got it!")
#         break
#     elif guess != secretNumber:
#         print("Nope, try again.")


# #Step 2
# secretNumber = 5
# print("I am thinking of a number between 1 and 10.")

# while True:
#     guess = int(input("What is your guess? "))

#     if guess == secretNumber:
#         print("You got it!")
#         break
#     elif guess < secretNumber:
#         print("Too low! Try again.")
#     elif guess > secretNumber:
#         print("Too high! Try again.")

#Step 3
# secretNumber = random.randint(1, 10)
# print("I am thinking of a number between 1 and 10.")

# while True:
#     guess = int(input("What is your guess? "))

#     if guess == secretNumber:
#         print("You got it!")
#         break
#     elif guess < secretNumber:
#         print("Too low! Try again.")
#     elif guess > secretNumber:
#         print("Too high! Try again.")

#Step 4
# while True:
#     secretNumber = random.randint(1, 10)
#     guessesLeft = 10
#     print("I am thinking of a number between 1 and 10.")

#     while True:
#         if guessesLeft == 0:
#             print("You're out of guesses. Better luck next time!")
#             break

#         print(f"You have {guessesLeft} guesses left.")    
#         guess = int(input("What is your guess? "))

#         if guess == secretNumber:
#             print("You got it!")
#             break
#         elif guess < secretNumber:
#             print("Too low! Try again.")
#             guessesLeft -= 1
#         elif guess > secretNumber:
#             print("Too high! Try again.")
#             guessesLeft -= 1
    
#     playAgain = input("Would you like to play again? (y/n) ")
#     if playAgain != 'y':
#         break