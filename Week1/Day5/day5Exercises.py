# // Write a function that takes in a string of lowercase letters
# // and returns the index of the string's first non-repeating character.
# // If the input string does not have any non-repeating characters,
# // your function should return -1.
string = "abcdcaf"

def nonRepeating(string):
    print(string)
    # stringList = list(string)

    for i in string:
        for j in string:
            if i != j:
                print(i)
            
            
          

            
                



nonRepeating(string)