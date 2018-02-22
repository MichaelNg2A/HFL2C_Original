#!/usr/bin/env python3

import random

# Define the "winner" variable with an empty string.

winner = ''

# Define the options that the computer can choose from.

choices = ['rock', 'paper', 'scissors']

# Use the random.choice module to randomly choose one of the options above.

computer_choice = random.choice(choices)

# Subroutine to prompt the user for an option and verify that it's valid.

user_choice = ''
while (user_choice != 'rock' and
    user_choice != 'paper' and
    user_choice != 'scissors'):
        user_choice = input('rock, paper or scissors? ')

print('You choose', user_choice, 'and the computer choose', computer_choice)

if computer_choice == user_choice:
    winner = 'Tie'

elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'

elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'

elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'

else:
    winner = 'User'

if winner == 'Tie':
    print('We both choose', computer_choice + ', play again.')

else:
    print(winner, 'won, I choose', computer_choice + '.')
