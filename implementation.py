# -*- coding: utf-8 -*-
x = 4
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001
while abs(guess**2 - x) >= epsilon:
    guess += increment
    num_guesses += 1
print(f'num_guesses = {num_guesses}')
print(f'{guess} is close to square root of {x}')

33,30