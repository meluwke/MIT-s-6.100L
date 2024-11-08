# -*- coding: utf-8 -*-


secret=13
guess=int(input("guess the number i choose between 1 to 20.\n"))
if (secret==guess):
    print("you've found it!\n")
elif (guess<secret):
    print("your guess is less than my number.\n")
else: #there is no need for if guess>secret because there is no other option.
    print("your guess is greater than my number.\n")