# -*- coding: utf-8 -*-
def mob(n, f1, f2):
    """ n is an int
        f1 and f2 are functions that take in an int and return a float
    Applies f1 and f2 on all numbers between 0 and n (inclusive). 
    Returns the maximum value of all these results.
    """
    L=[] #we created a empty list so we can add our values in it.
    for num in range(n+1): #created a loop becuz it wants 0 to n.
       c=max(f1(num), f2(num)) #basically we evaluated values of two func and define the max of it as "c"
       L.append(c) #added the c value to our list L with "L.append(c)"
    return max(L) 
       
   
        
# print(mob(2, lambda x:x-1, lambda x:x+1))  # prints 3
print(mob(10, lambda x:x*2, lambda x:x/2))  # prints 20
