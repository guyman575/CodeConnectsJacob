import random
# take in m, n, p
# n: length
# m: width
# p: probability of bomb

# * * . . .
# . . . . .
# . * . . .

# * * 1 0 0
# 3 3 2 0 0
# 1 * 1 0 0

def print_board(gameboard):
    for row in gameboard:
        for elt in row:
            print(elt, end=' ')
        print()

# return 2D array of all '.' for the given size
def initialize_board(rows, columns):
    gameboard =[]
    for i in range(0, rows):
        game_row = []
        for j in range(0, columns):
            game_row.append(".")
        # ['.','.','.']
        gameboard.append(game_row)
    return gameboard

# random.randint
# HINT if random.randint <= p
def add_bombs(gameboard, p):
    for row in gameboard:
        for j in range(len(row)):
            if random.randint(0,100) <= p:
                row[j] = "*"

def add_nums(gameboard):
    solution = gameboard.copy()
    for i in range(len(solution)):
        for j in range(len(solution[0])):
            if solution[i][j] == ".":
                total = 0
                if i != len(solution)-1 and solution[i + 1][j] == "*":
                    total += 1
                if i != 0 and solution[i - 1][j] == "*":
                    total += 1
                if i != len(solution)-1 and j != len(solution[0]) - 1 and solution[i + 1][j + 1] == "*":
                    total += 1
                if i != len(solution)-1 and j != 0 and solution[i + 1][j - 1] == "*":
                    total += 1
                if i != 0 and j != 0 and solution[i - 1][j - 1] == "*":
                    total += 1
                if i != 0 and j != len(solution[0])-1 and solution[i - 1][j + 1] == "*":
                    total += 1
                if j != len(solution[0])-1 and solution[i][j + 1] == "*":
                    total += 1
                if j != 0 and solution[i][j - 1] == "*":
                    total += 1
                solution[i][j] = str(total)
    return solution
                

n = int(input("What is the length of the board?"))
m = int(input("What is the width of the board?"))
p = int(input("Pick a number between 1 and 100 for probability of a bomb?"))
print(p)
gameboard = initialize_board(n,m)
print_board(gameboard)


add_bombs(gameboard, p)
print_board(gameboard)

solution = add_nums(gameboard)
print_board(solution)

