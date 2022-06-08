#Tic Tac Toe Board?

size = 3

# for y in range(size):
#     for x in range(size):
#         print(x, y)


board = [] #Start with an empty List

for y in range(size):
    # Each element in the board will also be a List
    board.append([])
    for x in range(size):
        # Fill the inner pieces with our coordinates.
        board[y].append(f"[{y}][{x}]")

    for row in board:
        for column in row:
            print(f"{column}", end='')
        print("\n")


# Validate Subsequence:


#Three Number Sum:
