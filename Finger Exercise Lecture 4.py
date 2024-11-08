# -*- coding: utf-8 -*-
N=int(216)
for roots in range(N+1):
    if roots**3==N:
        print("it's a perfect cube.")
        break #this keyword discards all of the code that left to execute.
else:
 print("error!") 