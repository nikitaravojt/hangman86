import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for _ in self.word]
        self.list_of_guesses = []
        self.letters_to_guess = len(set(self.word))


    def check_guess(self, guess):
        """Checks if the guessed letter "guess" (str) is in the word.
        If True, the corresponding underscore(s) in word_guessed are replaced
        with the letter. Otheriwse, the total number of allowed guesses is 
        reduced by 1 (i.e., num_lives reduced by 1)."""

        if guess in self.word:
            print(f"Good guess! '{guess} is in the word.'")
            for idx, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[idx] = guess
            self.letters_to_guess -= 1
            print(self.word_guessed)
        else:
            print(f"Wrong guess! '{guess}' is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} guesses remaining.")


    def ask_for_input(self):
        """Continually asks user for input until a valid input is given.
        Input must be a single alphabetical character (letter) and it must
        not have been guessed yet. If this criteria is fulfilled, the
        check_guess() method is called. """

        while True:
            user_guess = input("Your guess: ").lower()
            if not user_guess.isalpha() or len(user_guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif user_guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.check_guess(user_guess)
                self.list_of_guesses.append(user_guess)
                break


def play_game(word_list):
    """Function to initialise a game object and begin the game. Requires
    word_list list as input."""
    num_lives = 5
    game = Hangman(word_list=word_list, num_lives=num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.letters_to_guess != 0:
            game.ask_for_input()
        else:
            print(f"Congratulations! You guessed the word, it was: {game.word}")
            break


play_game(["apple", "banana", "kiwi", "passionfruit", "lychee"])
