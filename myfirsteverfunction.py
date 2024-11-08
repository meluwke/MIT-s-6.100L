# -*- coding: utf-8 -*-

def odd (x):
   """    Parameters- i : positive int.
    Returns - :true if its odd otherwise false
   """
   if x %2 != 0:
     return True
   else:
    return False

for i in range(1,11):
    if odd(i):
        print(i,"even")
    else:
        print(i,"odd")
# önemli ps: Ancak, fonksiyon gövdesindeki tüm satırların dört boşluk girintili olması gerekirdi,
# çünkü Python girintileri dört boşluk (veya bir TAB) ile hizalı olarak tanımlar.

# odd(4)=False
# print(odd(4)) 