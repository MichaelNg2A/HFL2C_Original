#!/usr/bin/env python3

import random

choices = ['rock', 'paper', 'scissors']

computer_choice = random.choice(choices)

user_choice = input('rock, paper or scissors? ')

print('You choose', user_choice, 'and the computer choose', computer_choice)
