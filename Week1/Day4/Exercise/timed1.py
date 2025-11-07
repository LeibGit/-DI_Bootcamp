prompt = input("Enter a word and a char: ")

word, char = prompt.split(" ")
count = 0
if char in word:
    print(word.count(char))
else:
    print("character not in word.")