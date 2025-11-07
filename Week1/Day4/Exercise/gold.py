"""
current_year = 2025
current_month = 11

def get_age(year, month, day):    
    age = current_year - year
    if current_month < month:
        age -= 1
    return age
get_age(year=2020, month=5, day=7)


def can_retire(gender, dob):
    year, month, day = map(int, dob.split("/"))
    age = get_age(year=year, month=month, day=day)

    if gender.lower() == 'f' and age >= 62:
        return 'Can retire'
    elif gender.lower() == 'm' and age >= 67:
        return 'Can retire'
    else:
        return 'cannot retire'


gender_prompt = input("Enter gender (m/f): ")
dob_prompt = input("Enter date of birth in yyyy/mm/dd format: ")

result =  can_retire(gender_prompt, dob_prompt)
print(result)
"""
# Exercise 2
def sum_function(X: int):
    str_x = str(X)
    str_x_2 = str(X) + str(X)
    str_x_3 = str(X) + str(X) + str(X)
    str_x_4 = str(X) + str(X) + str(X) + str(X)
    lst_of_str_x = [str_x, str_x_2, str_x_3, str_x_4]
    total_sum = 0
    for x in lst_of_str_x:
        new_x = int(x)
        total_sum += new_x
    print(total_sum)
sum_function(3)