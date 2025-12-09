import os
import json
import pandas as pd
import numpy as np 
import scipy
from random import choice, randint 
from collections import defaultdict

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
        return (avg_steps * 0.05) + (avg_steps)

    def get_workouts(self):
        """Getting workouts and providing the next one"""
        cadio_workouts = ['run', 'swim', 'boxing', 'HIIT', 'karate', 'hiking']
        strength_workouts = ['powerlifting', 'calisthetics', 'pushups', 'squats', 'deadlift']
        flexibility_workouts = ['yoga', 'stretch', 'swim']
        all_workouts = cadio_workouts + strength_workouts + flexibility_workouts
        workouts = []
        for workout in self.daily_logs:
            workouts.append(workout)
        if self.goal == "cardio" or self.goal == "flexibility":
            rand_choice_cardio = choice(cadio_workouts)
            return rand_choice_cardio
        elif self.goal == "strength" or self.goal == "muscle_gain": 
            rand_choice_strength = choice(strength_workouts)
            return rand_choice_strength
        elif self.goal == "flexibility":
            rand_choice_flex = choice(flexibility_workouts)
            return rand_choice_flex
        else:
            rand_choice_all = choice(all_workouts)
            return rand_choice_all
            
            
        
    def get_cals_burned(self):
        """Analyzing statisticall distance between calories burned between workouts"""
        groups = defaultdict(list)

        for log in self.daily_logs:
            workout_type = log['workout']
            calories = log['calories']
            groups[workout_type].append(calories)

        group_lists = list(groups.values())

        if len(group_lists) < 2:
            raise ValueError("Need at least 2 workout types for analysis.")
        f_stat, p_value = scipy.stats.f_oneway(*group_lists)
        return f_stat, p_value
        
    def reccomendations(self):
        """Generating workout reccomendation"""
        min_minutes = 15
        max_minutes = 60
        workout_time = randint(min_minutes, max_minutes)
        return f"{self.name} | {self.get_dates() + pd.Timedelta(days=1)}\n---------------------------\n1. walk {self.get_steps()} steps. \n2. Todays workout: {self.get_workouts()} \n3. Duration: {workout_time} minutes"

if __name__ == "__main__":
    plans = []
    for user in data:
        plans.append(WorkoutPlan(
            name=user["name"], 
            age=user["age"], 
            goal=user["goal"], 
            daily_logs=user["daily_logs"]
        ))
    for p in plans:
        print(p.reccomendations())
        print(p.get_cals_burned())