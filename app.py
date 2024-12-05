import random
from words import words_list

# list of words, pull from randomly and select a word
# also create list of characters from word_to_guess for printing
# progress in guessing the word
word_to_guess = random.choice(words_list)
correct_letters = list(word_to_guess)

# number of guesses limited by hangman parts
# head, 2 arms, 2 legs, body, eyes, frown
guess_limit = 8

# visually show how many letters in word with underscores
# fill in as they guess correct letters and reprint
def print_word_progress(word_to_guess, correct_letters):
    underscores_num = len(word_to_guess)
    print('_ ' * underscores_num)

def playHangman(word_to_guess, correct_letters):
    while True:
        print_word_progress(word_to_guess, correct_letters)
        print('Guess a letter: ')
        player_guess = input().lower()
        # check for value of guess, must be a letter
        if player_guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('You must guess a letter, please try again: ')

# user gets feedback for each guess (correct or wrong)

# game ends when hangman is complete or they finish the word correctly

# prompt to play again or terminate

playHangman(word_to_guess, correct_letters)