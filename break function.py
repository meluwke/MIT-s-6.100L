# -*- coding: utf-8 -*-
sum=0
for i in range(2,16,3):#2 5 8 11 14
    sum+=i
    if sum==15:
        break #this statement did let us to skip i to take values 11 and 14
print(sum*"hi ")


