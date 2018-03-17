#!/usr/bin/env python3

dog_names = ["Codie", "Sparky", "Jackson", "Fido"]
dog_weights = [40, 9, 12, 65]

for i in range(len(dog_names)):
     if dog_weights[i] > 20:
         print(dog_names[i], 'says WOOF WOOF')
     else:
         print(dog_names[i], 'says woof woof')

