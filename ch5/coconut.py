#!/usr/bin/env python3

smoothies = ['coconut',
             'strawberry',
             'banana',
             'tropical',
             'acai berry']

has_coconut = [True,
               False,
               False,
               True,
               False]

i = 0
length = len(smoothies)
for i in range(length):
    if has_coconut[i]:
        print(smoothies[i],'contains coconut')
