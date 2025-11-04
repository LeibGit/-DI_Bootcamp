# Exercise #1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict = dict(zip(keys, values))
print(new_dict)

# Exercise #2
def total_cost():
    family_members = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
    total_cost = 0
    for key, value in family_members.items():
        if value < 3:
            print(f"{key}'s ticket is free")
        elif value >= 3 and value <= 12:
            print(f"{key}'s ticket is $10") 
            total_cost += 10
        else: 
            print(f"{key}'s ticket is $15")
            total_cost += 15
    print(f'${total_cost}')
total_cost()

# Exercise #3
brand = {
    "name": "zara", 
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": [
        "men", 
        "women", 
        "children", 
        "home" 
    ],
    "international_competitors": [
        "Gap",
        "H&M", 
        "Benetton",
    ],
    "number_stores": 7000, 
    "major_color": {
        "France": "blue", 
        "Spain": "red", 
        "US": "Pink" "green"
    }
}

brand["number_stores"] = 2
print(f"We service: {", ".join(brand['type_of_clothes'])}")
brand["country_creation"] = 'Spain'

if brand["international_competitors"]:
    brand["international_competitors"].append('Desigual')

print(brand)

del brand["creation_date"]
print(brand)

print(brand["international_competitors"][0])

print(brand['major_color']['US'])

print(len(brand.keys()))
print(brand.keys())

more_on_zara = {
    "creation_date": "11/4/2025", 
    "number_stores": "10"
}

final_dict = {**brand, **more_on_zara}
print(final_dict)

# Exercise 4
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
character_dict = {}
revised_dict = {}
sorted_dict = {}
for index, user in enumerate(users):
    character_dict[user] = index
print(character_dict) 

for index, user in enumerate(users):
    revised_dict[index] = user
print(revised_dict) 

sorted_users = sorted(users)

for index, user in enumerate(sorted_users):
    sorted_dict[user] = index
print(sorted_dict)