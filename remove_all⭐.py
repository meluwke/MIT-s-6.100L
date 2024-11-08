# -*- coding: utf-8 -*-
def remove_all(L, e):
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None
    """
    # with copying
    
    # copyL=L[:]
    # L.clear()
    # for char in copyL:
    #     if not char==e:
    #         L.append(char)
    
    #slightly wrong version (mit lecture 11)
        
    for char in L:
      if char==e:
          L.remove(e)
         
    #even better version⭐
    
    # while e in L:
    #    L.remove(e) 
            
            
    return L
L1=[1,2,2,2]
remove_all(L1, 2)
print(L1) # prints [1]



L = [1,2,3,2,1,5]
remove_all(L, 1)
print(L)