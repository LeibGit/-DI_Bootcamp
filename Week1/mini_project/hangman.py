import random

wordlist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
bodypart_list = ['head', 'body', 'left arm', 'right arm', 'left leg', 'right leg']

word = random.choice(wordlist)

def play_hangman(hangman_word):
    display_word = ['_'] * len(hangman_word)
    list_of_guesses = []
    bp = []
    while True:
        bodypart = random.choice(bodypart_list)
        guess = input("Guess a letter: ")
        if guess in list_of_guesses:
            print("You already guessed this.")
        elif guess not in hangman_word:
            print(f"Not in word, you lost {bodypart}")
            bodypart_list.remove(bodypart)
            if not bodypart_list:
                print("You lost all body parts.")
                break
        elif guess in hangman_word:
            for index, char in enumerate(hangman_word):
                if guess == char:
                    list_of_guesses.append(guess)
                    display_word[index] = guess
        print(''.join(display_word))
        if ''.join(display_word) == hangman_word:
            print("You won")
            break
play_hangman(word)