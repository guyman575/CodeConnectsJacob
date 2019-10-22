import random
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

def add_nums(solution):
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