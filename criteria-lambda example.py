# -*- coding: utf-8 -*-
def even(x):
   return x%2==0
def five(x):
    return x==5
def apply(criteria,n):
    """
    * criteria is a func that takes in a number and returns a bool
    * n is an int
    Returns *how many ints* from 0 to n (inclusive) match
    the criteria (i.e. return True when run with criteria)
    """
    count=0
    for numbers in range(n+1):
        if criteria(numbers):#⭐you should write criteria so when you change the function that goes with apply, end value would able to change too.
         count+=1
    return count
howmany= apply(five, 10)
#print(howmany)
print('apply with five func.:',apply(five, 4))
print('apply with anon func.:',apply(lambda x: x==5, 100))

print(even(8))
print((lambda x: x%2==0)(8)) #lambda functions are one-time use. it cant be reused because it has no name!
 