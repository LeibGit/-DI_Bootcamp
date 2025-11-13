# Exercise 1
from datetime import date, timedelta
import holidays
import re
import random 
import string

def today():    
    us_holidays = holidays.US(years=range(2025, 2026))
    todays_date = date.today()
    next_holiday = us_holidays.get_closest_holiday(todays_date)

    return f"The next closest holiday is {next_holiday[1]} on the date: {next_holiday[0]}"

# Exercise 2
def jupiter_age(age):
    person_age = timedelta(seconds=age)
    num_days = person_age.days
    earth_years = f"You are {round(num_days / 365, 2)} years old on earth"
    mercury = f"You are {0.2408467 * round(num_days / 365, 2)} on mercury"
    venus = f"You are {0.61519726 * round(num_days / 365, 2)} on venus"
    mars = f"You are {1.8808158 * round(num_days / 365, 2)} on mars"
    jupiter = f"You are {11.862615 * round(num_days / 365, 2)} on jupiter"
    saturn = f"You are {29.447498 * round(num_days / 365, 2)} on saturn"
    uranus = f"You are {84.016846 * round(num_days / 365, 2)} on uranus"
    neptune = f"You are {84.016846 * round(num_days / 365, 2)} on neptune"
    return (
    f"Earth: {earth_years}\n"
    f"Mercury: {mercury}\n"
    f"Venus: {venus}\n"
    f"Mars: {mars}\n"
    f"Jupiter: {jupiter}\n"
    f"Saturn: {saturn}\n"
    f"Uranus: {uranus}\n"
    f"Neptune: {neptune}"
)

# Exercise 3
txt = 'k5k3q2g5z6x9bn'
numbers = re.findall('\d+', txt)

# Exercise 4
full_name = input("Enter your full name: ")

pattern = r"^[A-Z][a-z]+ [a-z]+$"

if re.match(pattern, full_name):
    print(f"{full_name} is valid")
else:
    print(f"{full_name} is not valid.")

# Exercise 5
def generate_password():
    random_chars = string.digits + string.ascii_lowercase
    new_password = []
    string_conversion = ""
    flag = True
    while flag:
        defined_range = int(input("Enter a number between 6 and 30: "))
        if defined_range > 30 or defined_range < 6:
            loop_active = False
        else:
            for i in range(0, defined_range):
                ran = random.choices(random_chars)
                new_password += ran
            for i in new_password:
                string_conversion += i
            flag = False
    return string_conversion
        

if __name__=="__main__":
    print(today())
    print(jupiter_age(1000000000))
    print(numbers)
    print(generate_password())