import random
# import numpy as np
from words import words_list

# list of words, pull from randomly and select a word
# also create list of characters from word_to_guess for printing
# progress in guessing the word
word_to_guess = random.choice(words_list)
correct_letters = list(word_to_guess)

# number of guesses limited by hangman parts
# head, 2 arms, 2 legs, body, eyes, frown
guess_limit = 8

def get_indices(correct_letters, player_guess):
    index_results = []
    offset = -1
    while True:
        try:
            offset = correct_letters.index(player_guess, offset+1)
        except ValueError:
            print(index_results)
            return index_results
        index_results.append(offset)
    # index_results = np.where(correct_letters == player_guess)[0]
    
    


# print underscores and fill in correctly guessed letters
def print_word_progress(word_to_guess, correct_letters, player_guess):
    # check if the guess is in the word
    # if it is, need to know the index of the correct letters, then print
    # underscores at the indices which are still blank, then print correct
    # letters filled in at their indices too
    # then return to guessing
    if player_guess in word_to_guess:
        get_indices(correct_letters, player_guess)
    else:
        print("Wrong!")



def playHangman(word_to_guess):
    while True:
        underscores_num = len(word_to_guess)
        print('_ ' * underscores_num)

        # get player input for guess
        print('Guess a letter: ')
        player_guess = input().lower()
        # check for value of guess, must be a letter
        if player_guess.isalpha() == False:
                print('You must guess a letter, please try again: ')
        
        # check if guess is in the word and give player feedback
        print_word_progress(word_to_guess, correct_letters, player_guess)


# game ends when hangman is complete or they finish the word correctly

# prompt to play again or terminate

playHangman(word_to_guess)