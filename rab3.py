#!/usr/bin/env python3


# Prints out board.
def print_board(board):
    for row in board:
        print("".join(row))

# Gets all possible locations.
def get_poss_locs(board, word):
    poss_locs = []
    length = len(word)
    # Horizontal possible locations.
    for i in range(10):
        for j in range(10 - length + 1):
            good = True
            for k in range(len(word)):
                if board[i][j + k] not in ["-", word[k]]:
                    good = False
                    break
            if good:
                # 0 is axis indicator.
                yield (i, j, 0)
    # Vertical possible locations.
    for i in range(10 - length + 1):
        for j in range(10):
            good = True
            for k in range(len(word)):
                if board[i + k][j] not in ["-", word[k]]:
                    good = False
                    break
            if good:
                # 1 is axis indicator.
                yield (i, j, 1)

# Reverts move.
def revert(board, word, loc):
    i, j, axis = loc
    # Axis 0 is horizontal.
    if axis == 0:
        for k in range(len(word)):
            board[i][j + k] = "-"
    # Axis 1 is vertical.
    else:
        for k in range(len(word)):
            board[i + k][j] = "-"

# Writes the word on board at specified location.
def move(board, word, loc):
    i, j, axis = loc
    if axis == 0:
        for k in range(len(word)):
            board[i][j + k] = word[k]
    else:
        for k in range(len(word)):
            board[i + k][j] = word[k]

# Attempts to solve the board.
def solve(board, words):
    global solved
    if len(words) == 0:
        if not solved:
            print_board(board)
        solved = True
        return
    word = words.pop()
    pos_locs = [loc for loc in get_poss_locs(board, word)]
    for loc in pos_locs:
        move(board, word, loc)
        solve(board, words)
        revert(board, word, loc)
    words.append(word)


if __name__ == "__main__":
    board = []
    for _ in range(10):
        board.append(list(input()))
    words = str(input()).split(";")
    solved = False
    solve(board, words)
