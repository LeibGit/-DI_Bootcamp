from anagram_checker import AnagramChecker

def main():
    while True:
        print("1.Enter a word to get anagrams and check if it is in the list.")
        print("2.Exit.")
        user_input = int(input("Enter number here: "))

        if user_input == 2:
            break
        elif user_input == 1:
            get_word = input("Enter a word: ")
            measure = get_word.split()
            if len(measure) >= 2:
                print("only one word allowed. ")
                break 
            elif get_word.strip().isalpha() == False:
                print("input invalid, only alphabetic letters allowed")
                break
            else:
                new_instance = AnagramChecker()
                print("input valid, here is a list of anagrams")
                print(new_instance.get_anagrams(word=get_word.strip()))
main()