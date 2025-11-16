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
import requests

class Character():
    def __init__(self, char=None, strength=0, dexterity=0, constitution=0, intelligence=0, wisdom=0, charisma=0):
        self.char = char
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def define_players(self):
        num_of_players = int(input("Enter how many players are playing in ingterger format: "))
        player_dict = {}
        for player in range(1, num_of_players + 1):
            get_player_name = input("What is your name: ")
            get_player_age = input("What is your age: ")
            player_dict[get_player_name] = get_player_age
        with open('player.json', 'w') as file:
            json.dump(player_dict, file, indent=4)
        return f"All players saved successfully in json."


if __name__=="__main__":
    test = Character()
    print(test.define_players())