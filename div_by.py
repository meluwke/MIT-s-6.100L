# -*- coding: utf-8 -*-
def div_by (n,d):
   """ n and d are ints > 0
Returns True if d divides n evenly and False otherwise 
   """
   if n%d==0:
       print(True)
   else:
       print(False)

print(div_by(195, 3)) #we'll talk about in next lectures
div_by(10, 3)