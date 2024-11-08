# -*- coding: utf-8 -*-
def square(L):
    return [c**2 for c in L]
M=[2,5,1]
print(square(M))

#solution 1 - using index
def square_list(L):
    index = 0
    for elem in L:
        L[index] = elem**2
        index += 1

#solution 2 - looping through index
def square_list1(L):
    for i in range(len(L)):
        L[i] = L[i]**2 #An assignment statement. L[i] is not a name, but points to a particular spot in the list data structure.

#solution 3 - enumerate⭐
 # ⭐enumerate fonksiyonu, bir iterable (örneğin bir liste) üzerinde döngü
 # yaparken hem elemanları hem de indekslerini verir. Bu yöntem, hem indeks
 # hem de elemana erişim sağladığı için oldukça kullanışlıdır.
def square_list2(L):
   for i, elem in enumerate(L): #i,elem index ve element yerini tutuyorlar!!
       L[i] = elem**2
