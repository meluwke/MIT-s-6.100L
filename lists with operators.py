# -*- coding: utf-8 -*-
# L = [2, 'a', 4, [1,2]] #len(L)=4
#L[0] evaluates to 2
#L[4] gives an error because there is not 4th element.
L1=[1,2]+[3,4] #evaluates to L1=[1,2,3,4]
# print(L1)
L1[2]=6 #list are mutable so we change the values of it.
print(L1)

total=0
for i in L1:
    #loop variable i takes values of list IN ORDER!(1 then 2 then 6 then 4)
    print(i)
    total+=i
print(total)
