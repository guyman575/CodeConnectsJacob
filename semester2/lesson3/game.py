from game_board import GameBoard

n = int(input("how many rows?"))
m = int(input("how many columns?"))
p = int(input("Pick a number between 1 and 100 for probability of a bomb?"))
my_game = GameBoard(n,m,p)
while True:
    my_game.print_current_state()
    move = my_game.make_move(int(input("What Row?")), int(input("What Column?")))
    if move == False:
        break