car_brands = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
car_brand_list = []

for i in car_brands.split():
    car_brand_list.append(i)
print(car_brand_list)

count = 0
for i in car_brand_list:
    count += 1
print(f"there are {count} car brands.")

car_brand_list.sort(reverse=True)
print(car_brand_list)

for brand in car_brands.split():
    count = 0
    if 'o' in brand:
        count += 1
    print(count)

for brand in car_brands.split():
    count = 0
    if 'i' in brand:
        count += 1
    print(count)
