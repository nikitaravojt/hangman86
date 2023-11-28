import random


def guess():
    while True:
        user_guess = input("Your guess: ").lower()
        if user_guess.isalpha() and len(user_guess) == 1:
            return user_guess
        else:
            print("Please enter a single letter!")


word_list = ["apple", "banana", "kiwi", "passionfruit", "lychee"]
word = random.choice(word_list)
guess1 = guess()
print(guess1)