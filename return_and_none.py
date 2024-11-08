# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:40:43 2024

@author: melik
"""

def add(x,y):
    return x+y
def mult(x,y):
    print(x*y)
      
add(1,2) #didnt give an output
print(add(2,3)) #becuz return has been added, it gives an output.
    
mult(3,4) #becuz print is given in func def., it gave an output
print(mult(4,5)) #becuz code added extra 'print' the none has been printed
#when you dont add return, python automatically adds a None.⭐