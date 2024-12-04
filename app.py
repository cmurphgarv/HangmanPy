import random
from words import words_list

# list of words, pull from randomly and select a word
word_to_guess = random.choice(words_list)
print(word_to_guess)

# number of guesses limited by hangman parts
guess_limit = 6

# visually show how many letters in word
underscores_num = len(word_to_guess)
print('_ ' * underscores_num)

# user gets feedback for each guess (correct or wrong)

# game ends when hangman is complete or they finish the word correctly

# prompt to play again or terminate