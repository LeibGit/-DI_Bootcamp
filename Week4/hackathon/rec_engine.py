import os
import json
import pandas as pd
import numpy as np 


with open("users.json", 'r') as file:
    data = json.load(file)

class WorkoutPlan():
    def __init__(self, name, age, goal, daily_logs):
        self.name = name
        self.age = age
        self.goal = goal
        self.daily_logs = daily_logs

    def reccomendations(self):
        for log in self.daily_logs:
            print(log)

if __name__ == "__main__":
    for user in data:
        new_inst = WorkoutPlan(
            name=user["name"], 
            age=user["age"], 
            goal=user["goal"], 
            daily_logs=user["daily_logs"]
        )
    new_inst.reccomendations()