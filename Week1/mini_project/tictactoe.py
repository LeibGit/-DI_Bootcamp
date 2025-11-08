grid = [
    [' ',' ', ' '], 
    [' ', ' ', ' '], 
    [' ', ' ', ' '],
]

def display_board():
    print("-"*13)
    for row in grid:
        print('  |  '.join(row))
        print("-"*13)
display_board()

def player_move(player):
    while True:
        get_move = input("Enter which position you want to move in this format 'row column': ")
        row, column = map(int, get_move.split())
        if row <= 3 and row >= 0 and column <= 3 and column >= 0:
            grid[row][column] = player
            display_board()
        else:
            False
            print("Enter an input between 1 and 3 for the row and column.")
player_move('x')