# -*- coding: utf-8 -*-
# ts=(2,)
# tp=(2)
# # print(type(tp))

# t=(2,"mit",3)
# print(t[0]) #prints 2.
# print(t[1:3]) #prints ('mit',3).
# print(len(t)) #prints 3.
# a=(3,"hi",5)+(9,10)
# print(a) #prints (3, 'hi', 5, 9, 10)
# #t[1]=4 #tuples are immutable. can't modify object.
# #prints TypeError: 'tuple' object does not support item assignment
# b=(3,5)+(9,10)
# print(max(b))
# print(sum(b))

# seq=(1,2,3,4,(8,9,10)) #len(seq) is equal to 5.
# print(seq[4][1]) #prints 9! i can do several indexing with tuples!

# for e in seq: #we can iterate through tuples.
#     print(e)
    
def qar(x,y):
    q=x//y
    r=x%y
    return (q,r) #returns a tuple

# both=qar(10, 3) #3,1
# (quot,rem)=qar(5, 4) #1,1
# print(both)
# both=(quot,rem) #it swaped its variables.
# print(both)

(quot,rem)=qar(6, 2) #it swaps its variables!
print('quotient is:',quot)
print('remainder is:',rem)