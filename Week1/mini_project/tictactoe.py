def play_game():
    grid = [
        [' ',' ', ' '], 
        [' ', ' ', ' '], 
        [' ', ' ', ' '],
    ]
    player_one = 'x'
    player_two = 'o'
    current_player = player_one

    def display_board():
        print("-"*13)
        for row in grid:
            print('  |  '.join(row))
            print("-"*13)


    def player_move(grid, player):
        nonlocal current_player
        while True:
            get_move = input("Enter which position you want to move in this format 'row column': ")
            row, column = map(int, get_move.split())
            if row <= 3 and row >= 0 and column <= 3 and column >= 0:
                if grid[row-1][column-1] == ' ':
                    grid[row-1][column-1] = player
                    current_player = player_two if current_player == player_one else player_one
                    break
                else:
                    print("This cell is taken.")
            else:
                print("Enter an input between 1 and 3 for the row and column.")
    
    def check_winner(grid, player):
        for row in grid:
            if row == [player, player, player]:
                print(f"{player} wins!")
                return True
            for c in range(3):
                if grid[0][c] == player and grid[1][c] == player and grid[2][c] == player:
                    print(f"{player} wins.")
                    return True
            if grid[0][0] == grid[1][1] == grid[2][2] == player or grid[0][2] == grid[1][1] == grid[2][0] == player:
                print(f"{player} wins!")
                return True
            return False
            
    while True:
        display_board()
        player_move(grid, current_player)
        if check_winner(grid, player_one) or check_winner(grid, player_two):
            break
play_game()