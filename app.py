import random
from words import words_list

# list of words, pull from randomly and select a word
word_to_guess = random.choice(words_list)


# number of guesses limited by hangman parts
# head, 2 arms, 2 legs, body
guess_limit = 6

# visually show how many letters in word with underscores
# fill in as they guess correct letters and reprint
def print_word_progress():
    underscores_num = len(word_to_guess)
    print('_ ' * underscores_num)
    correct_letters = word_to_guess.split()
    print(correct_letters)    

def playHangman():
    while True:

# user gets feedback for each guess (correct or wrong)

# game ends when hangman is complete or they finish the word correctly

# prompt to play again or terminate