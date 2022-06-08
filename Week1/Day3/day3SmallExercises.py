numbers = [1, 2, 3, 4, 5, 6, 7]

#Ex 1: Sum the numbers
sum = sum(numbers)
print(sum)

#Ex 2: Largest Number
max = max(numbers)
print(max)

#Ex 3: Smallest Number
min = min(numbers)
print(min)

#Ex 4: Even Numbers
for n in numbers:
    if n % 2 == 0:
        print(n)

#Ex 5: Positive numbers
for n in numbers:
    if n > 0:
        print(n)

#Ex. 6: Positive numbers 2
newList = []
for n in numbers:
    if n > 0:
        newList.append(n)
print(newList)

#Ex 7: Factor
factor = 6

factorList = [n*6 for n in numbers]
print(factorList)

#Ex. 8: Reverse a string
string = "Reaganomics" [::-1]
print(string)