import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in self.word]
        self.list_of_guesses = []
        # self.num_unguessed_letters = len([letter for letter not in ])







guesses = 5

def guess_input():
    while True:
        user_guess = input("Your guess: ").lower()
        if user_guess.isalpha() and len(user_guess) == 1:
            return user_guess
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")



def check_guess(word, guess, guesses):
    if guess in word:
        print(f"Good guess! '{guess} is in the word.'")
    else:
        print(f"Wrong guess! '{guess}' is not in the word.")
        guesses -= 1



word_list = ["apple", "banana", "kiwi", "passionfruit", "lychee"]
word = random.choice(word_list)
guess1 = guess_input()
print(guess1)
check_guess(word, guess1, guesses)