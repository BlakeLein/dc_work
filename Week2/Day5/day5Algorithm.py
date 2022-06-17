

def productList(list):
    answerList = [] # Empty list to return as answer.
    for l in range(len(list)): # Outer loop tracks individual indices of the the list
        product = 1 # Set this counter variable to keep track of the multiplication answer.
        for x in range(len(list)): # Inner loop to compare indices to each other
            if l == x: # If indices are equal, keep moving.
                continue
            else:
                product *= list[x] # Update 'product' to the product of every other indexed value
        answerList.append(product) # Add the product to a new list.
    print(answerList)






example = [5, 1, 4, 2]
productList(example)

rightAnswer = [8, 40, 10, 20]

##### NOTES ######
# Whenever you need to return something from a for loop it needs to be outside the loop. Product is a base number of 1 (lowest
#   possible number to multiply by)
# Using range(len(list)) allows us to manipulate the indices.