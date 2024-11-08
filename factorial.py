# -*- coding: utf-8 -*-
x=int(input())
a=1
factorial=1 #factorial variable keeps track of product
while a<=x:
    factorial*=a
    a+=1
print(f'{x} factorial is {factorial}')