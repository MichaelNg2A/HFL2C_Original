#!/usr/bin/env python3
############################################################
# rock.py                                                  #
############################################################
#                                                          #
# Name:       rock.py                                      #
# Version:    1.0                                          #
# Updated February 22nd, 2018                              #
# Author:     MichaelNg.GitHub@KWMeads.com                 #
#                                                          #
# This is a Python Program to play Rock, Paper Scissors    #
# with the computer.  Based on the exercises in Head First #
# Learn to Code - Chapter #3.  Good Luck!                  #
#                                                          #
############################################################

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

# Display what everyone's choices were.

print('You choose', user_choice, 'and the computer choose', computer_choice)

#  Define the "winner" if there's a tie.

if computer_choice == user_choice:
    winner = 'Tie'

# elif tree to walk through all the other scenarios where the Computer wins.

elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'

elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'

elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'

# If the computer is not the winner, the User must be the winner.

else:
    winner = 'User'

# Use this wording on the winner line if there's a tie.

if winner == 'Tie':
    print('We both choose', computer_choice + ', play again.')

# If there's only one winner, use the original wording to announce it.

else:
    print(winner, 'won, I choose', computer_choice + '.')
