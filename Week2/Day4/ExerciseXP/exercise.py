import random


def main():
    while True:
        print("This program is for creating a random sentence given words.")
        input_length = int(input("How many words should your sentence be? "))
        if input_length < 2 or input_length > 20:
            print("Enter an interger between 2 and 20.")
        else:
            get_random_sentence(input_length)
            break
    return get_random_sentence(input_length)

def get_words_from_file(file_path):
    with open(file_path, "r") as word_file:
        list_of_words = []
        for word in word_file.read().split():
            list_of_words.append(word)
        return list_of_words
    
def get_random_sentence(sentence_length):
    sentence = ""
    count = 0
    while count < sentence_length:
        new_word = random.choice(get_words_from_file(r"C:\Users\leibn\Downloads\random_words.txt"))
        sentence = sentence + " " + new_word
        count += 1
    return sentence.lower()

if __name__=="__main__":
    print(main())
