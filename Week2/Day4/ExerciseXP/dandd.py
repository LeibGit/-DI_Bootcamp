"""
1. Ask User how many players are playing
2. For each user prompt them to create there character getting name and age of character
3. Output all characters into a json file with all different character attributes
4. Each character will have six attributes (Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma)
5. Scores for attributes are determended randomly. You role 6-sided dice and record the sum of the largest three dice
6. This is done 6 times, once for each attribute
7. Character class should be in charge of creating characters
8. Game class should be in charge of how many time a character gets instantiated and exporting the data in json
"""
import random
import json

def define_attributes():
    count = 0
    dice_values = []
    while count < 4: 
        dice_values.append(random.choice([1, 2, 3, 4, 5, 6]))
        count += 1
    min_val = min(dice_values)
    dice_values.remove(min_val)
    sum_val = sum(dice_values)
    return sum_val
class Game():
    def __init__(self):
        pass
class Character():
    def __init__(self, char=None):
        self.strength = define_attributes()
        self.dexterity = define_attributes()
        self.constitution = define_attributes()
        self.intelligence = define_attributes()
        self.wisdom = define_attributes()
        self.charisma = define_attributes()

    def define_players(self):
        num_of_players = int(input("Enter how many players are playing in ingterger format: "))
        player_dict = {}
        for player in range(1, num_of_players + 1):
            get_player_name = input("What is your name: ")
            get_player_age = int(input("What is your age: "))
            player_dict[int(player)] = {
                "name": get_player_name, 
                "age": get_player_age, 
                "strength": self.strength, 
                "dexterity": self.dexterity, 
                "constitution": self.constitution, 
                "intelligence": self.intelligence, 
                "wisdom": self.wisdom, 
                "charisma": self.charisma
            }
        with open('player.json', 'w') as file:
            json.dump(player_dict, file, indent=4)
        return f"All players saved successfully in json."
    
if __name__=="__main__":
    test = Character()
    print(test.define_players())