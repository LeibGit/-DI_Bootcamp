import string

alphabet = string.ascii_lowercase
text = input("Enter a message: ")

def encode_word():
    letters = []
    for letter in text:
        new_letter = ord(letter) + 3
        letters.append(chr(new_letter))
    print("".join(letters))
encode_word()

text2 = input("Enter a message: ")
def decode_word():
    letters = []
    for letter in text2:
        new_letter = ord(letter) - 3
        letters.append(chr(new_letter))
    print("".join(letters))
decode_word()