# -*- coding: utf-8 -*-
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
factorial_a=1
factorial_b=1
factorial_c=1
d=1
while d<=a:
    factorial_a=d*factorial_a
    d+=1
d=1
while d<=b:
    factorial_b=d*factorial_b
    d+=1
d=1
while d<=c:
    factorial_c=d*factorial_c
    d+=1
print(factorial_a,factorial_b,factorial_c)
    
    
    
