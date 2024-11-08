# -*- coding: utf-8 -*-
def ss(L):
    """ L is a list whose elements are lists with int elements
    Returns the sum of all int elements. """
    s=0
    for i in L: #i represents sublists here.
      s+=sum(i)
    return s
# tot=0
# for i in L:
#     for e in i:
#         tot+=e
#         return tot
print(ss([[5,8,9,1],[2,3,1]]))