from anagram_checker import AnagramChecker


def main():
    test_instance = AnagramChecker()
    while True:
        print("1. Check validity of a word.")
        print("2. Check if word is an anagram.")
        print("3. Get all anagrams.")
        print("4. To exit.")
        user_input = int(input("Pick one of the following options: "))

        if user_input == 1:
            word = input("Enter a word: ")
            print(test_instance.is_valid(word=word))
        elif user_input == 2:
            word1 = input("Enter a word: ")
            word2 = input("Enter another word: ")
            print(test_instance.is_anagram(word1=word1, word2=word2))
        elif user_input == 3:
            word = input("Enter a word: ")
            print(test_instance.get_anagrams(word_to_check=word))
        elif user_input == 4:
            break
        else:
            print("Please enter a valid input")

main()