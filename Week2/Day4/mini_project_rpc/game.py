import random

class Game():

    def get_user_item(self):
        user_select = input("Enter (rock/paper/scissors): ").strip().lower()
        return user_select
    
    def get_computer_item(self):
        list_of_moves = ["rock", "paper", "scissors"]
        choice = random.choice(list_of_moves)
        return choice
    
    def get_game_result(self, user_item, computer_item):
        # loss instances
        if user_item == "paper" and computer_item == "scissors":
            return "loss"
        elif user_item == "scissors" and computer_item =="rock":
            return "loss"
        elif user_item == "rock" and computer_item == "paper":
            return "loss"
        
        # Win instances
        elif computer_item == "paper" and user_item == "scissors":
            return "win"
        elif computer_item == "scissors" and user_item =="rock":
            return "win"
        elif computer_item == "rock" and user_item == "paper":
            return "win"
        
        # Tie instances
        elif computer_item == "paper" and user_item == "paper":
            return "tie"
        elif computer_item == "scissors" and user_item =="scissors":
            return "tie"
        elif computer_item == "rock" and user_item == "rock":
            return "tie"
        else:
            return "An unkown error occured."
    
    def play(self):
        user_choice =  self.get_user_item()
        computer_choice = self.get_computer_item()
        game_res = self.get_game_result(user_item=user_choice, computer_item=computer_choice)
        print(f"{game_res}")
        return game_res