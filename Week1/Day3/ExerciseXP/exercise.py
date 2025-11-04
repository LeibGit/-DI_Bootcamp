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