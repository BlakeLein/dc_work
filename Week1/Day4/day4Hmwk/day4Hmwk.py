#Ex 1: Get factorial

# import math
# def getFactorial():
#     num = int(input("Give me a numebr and I will tell you the factorial: "))
#     print(f"The factorial of {num} is:")
#     print(math.factorial(num))

# getFactorial()

# def getFactorial(num):
#     fact = 1
#     for i in range(1, num+1):
#         fact = fact*i
    
#     print(fact)

# getFactorial(5)

#Ex 2: Palindrome

# def isPalindrome(value):
#     if value == value[::-1]:
#         print("This is a palindrome!")
#     else:
#         print("This is not a palindrome!")

# isPalindrome("tacocat")

# #Ex. 3: Prime or not
# num = int(input("Give me a number and I'll tell you if it's a prime number. "))

# def isPrime(num):
#     factors =[] # Adding it to a list ensures that it doesn't print every time a number meets this condition. If any number makes it to the list, it's not prime.
#     for i in range(2, num):
#         if num % i == 0:
#             factors.append(i) 
#         if len(factors) == 0:
#             print(f"{num} is a prime number.")
#         else:
#             print("This is a prime number.")

# isPrime(4)