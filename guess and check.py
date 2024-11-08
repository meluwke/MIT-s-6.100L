# -*- coding: utf-8 -*-
guess=0
negative=False
x=int(input("enter integer: "))
if x<0:
    negative=True
while guess**2 <x:
    guess+=1
if guess**2==x:
    print(f' square root of {x} is {guess}')
else:
 print(x,"is not a perfect square")
 if negative== True: #Ancak daha Pythonik bir yol, sadece if negative: yazmaktır, çünkü negative zaten True veya False değerini tutar. Buna göre, if negative: yazmak yeterli olacaktır.
     print("did you mean", -x,"?")
    
    
    