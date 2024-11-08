# -*- coding: utf-8 -*-
where = input("Go left or right? ")
counter=0
while where == "right" or counter<2:
    counter+=1
where = input("Go left or right? ")
print("You got out!")
if counter>3:
    print(":(")
    


