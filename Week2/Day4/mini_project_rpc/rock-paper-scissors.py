from game import Game

def get_user_menu():
    print("1. Play new game.")
    print("2. Show scores.")
    print("3. Quit.")
    user_input = int(input("Enter an option: ").strip())
    if user_input in range(1, 4):
        return user_input
    else:   
        return "Enter a valid option."

def print_results(results: dict):
    print("Thanks for playing.")
    return f"Wins: {results['win']}, Losses: {results['loss']}, Ties: {results['ties']}"

def main():
    res = {'loss': 0, 'win': 0, 'tie': 0}
    while True:
        value = get_user_menu()
        if value == 1:
            new_game = Game()
            value = new_game.play()
            if value == 'win':
                res['win'] += 1
            elif value == 'loss':
                res['loss'] += 1
            elif value == 'tie':
                res['tie'] += 1  
        elif value == 2:
            print(res)
        else:
            print(res)
            break
if __name__=="__main__":
    main()