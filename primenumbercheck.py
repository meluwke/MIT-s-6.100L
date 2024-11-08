# -*- coding: utf-8 -*-
num=int(input("choose a number: "))
prime=True
for divider in range (2,num): #her sayı kendisine bölünebileceğinden num+1 tüm inputları asal olmayan bir sayı olarak verir.
    if num % divider==0:
        prime=False
        break
if prime==True:
    print(f'{num} is a prime number.')
else:
    print(f'{num} is not a prime number.')