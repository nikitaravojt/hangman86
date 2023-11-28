import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in self.word]
        self.list_of_guesses = []
        # self.num_unguessed_letters = len([letter for letter not in ])


    def check_guess(self, guess):
        if guess in self.word:
            print(f"Good guess! '{guess} is in the word.'")
            for idx, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[idx] = guess
            # reduce num_letters by 1?
        else:
            print(f"Wrong guess! '{guess}' is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} guesses remaining.")


    def ask_for_input(self):
        while True:
            user_guess = input("Your guess: ").lower()
            if not user_guess.isalpha() or len(user_guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif user_guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.check_guess(user_guess)
                self.list_of_guesses.append(user_guess)



word_list = ["apple", "banana", "kiwi", "passionfruit", "lychee"]
game1 = Hangman(word_list=word_list)
print('f')
# game1.ask_for_input()