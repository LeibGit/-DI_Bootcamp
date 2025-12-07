import os
import json
import pandas as pd
import numpy as np 
from random import choice, randint 

with open("users.json", 'r') as file:
    data = json.load(file)

class WorkoutPlan():
    def __init__(self, name, age, goal, daily_logs):
        self.name = name
        self.age = age
        self.goal = goal
        self.daily_logs = daily_logs

    def get_dates(self):
        """Getting the most recent date the user worked out"""
        dates = []
        for log in self.daily_logs:
            dates.append(log['date'])
        cleaned_dates = []
        for d in dates:
            cleaned_dates.append(pd.to_datetime(d))
        latest_date = np.max(cleaned_dates)
        return latest_date

    def get_steps(self):
        """Getting average steps of the user"""
        total_steps = 0
        workout_type = []
        for log in self.daily_logs:
            total_steps += log['steps']
        avg_steps = total_steps / len(self.daily_logs)
        return avg_steps

    def get_workouts(self):
        """Getting workouts and providing the next one"""
        cadio_workouts = ['run', 'swim', 'boxing', 'HIIT', 'karate', 'hiking']
        strength_workouts = ['powerlifting', 'calisthetics', 'pushups', 'squats', 'deadlift']
        workouts = []
        for workout in self.daily_logs:
            workouts.append(workout)
        if self.goal == "cardio":
            rand_choice_cardio = choice(cadio_workouts)
            return rand_choice_cardio
        else:
            rand_choice_strength = choice(strength_workouts)
            return rand_choice_strength
        
    def reccomendations(self):
        """Generating workout reccomendation"""
        min_minutes = 15
        max_minutes = 60
        workout_time = randint(min_minutes, max_minutes)
        return f"{self.name} | {self.get_dates() + pd.Timedelta(days=1)}\n---------------------------\n1. walk {self.get_steps()} steps. \n2. Todays workout: {self.get_workouts()} \n3. Duration: {workout_time} minutes"

if __name__ == "__main__":
    for user in data:
        new_inst = WorkoutPlan(
            name=user["name"], 
            age=user["age"], 
            goal=user["goal"], 
            daily_logs=user["daily_logs"]
        )
    print(new_inst.reccomendations())