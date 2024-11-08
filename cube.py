# -*- coding: utf-8 -*-
cube=int(input())
for guess in range(abs(cube)+1):
    if cube<0:
           guess= -guess
    if guess**3==cube:
        print(f'cube root of {cube} is {guess}.')
        break
else:
    print(f'there is no integer that is the cube root of {cube}.')

