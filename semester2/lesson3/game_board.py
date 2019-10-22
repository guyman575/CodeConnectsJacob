import random
from game_helper import initialize_board 
from game_helper import add_bombs
from game_helper import add_nums

class GameBoard:

    # numRows: integer
    # numCols: integer
    # probability: integer
    # currentState: 2D array
    # solution: 2D array

    def __init__(self,numRows, numCols, probabilityOfBomb):
        self.numRows = numRows
        self.numCols = numCols
        self.probability = probabilityOfBomb
        self.currentState = initialize_board(self.numRows, self.numCols)
        soln = initialize_board(self.numRows, self.numCols)
        add_bombs(soln, self.probability)
        add_nums(soln)
        self.solution = soln

    

    def print_current_state(self):
        for row in self.currentState:
            for elt in row:
                print(elt, end=' ')
            print()

    # returns whether or not the move causes the user to lose
    # true: move succeeds
    # false: move fails
    def make_move(self, move_row, move_col):
        if self.solution[move_row][move_col] == "*":
            return False
        else:
            value = self.solution[move_row][move_col]
            self.currentState[move_row][move_col] = value
            return True
            
