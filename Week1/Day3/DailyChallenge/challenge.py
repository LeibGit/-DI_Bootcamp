# Challenge 1
dictionary = {}

word = str(input("Enter a word: "))

for index, char in enumerate(word):
    if char in dictionary.keys():
        dictionary[char].append(index)
    else:
        dictionary[char] = [index]
print(dictionary)

# challenge 2
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = 300
basket = []

for item, cost in items_purchase.items():
    items_purchase[item] = items_purchase[item].replace("$", "").replace(",", "")
    print(items_purchase[item])
    if int(items_purchase[item]) <= wallet:
        basket.append(item)
        wallet -= int(items_purchase[item])
    else:
        continue
print(basket)