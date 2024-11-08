# -*- coding: utf-8 -*-
def remove_elem(L, e):
    """
    L is a list
    Returns a new list with elements in the same order as L
    but without any elements equal to e.
    """
    newL=[]
    for i in L:
        if i!=e:
         newL.append(i)
    return newL 
L=["a","b","c","d","e","f","a","b","d"]
print(remove_elem(L,"a"))