# -*- coding: utf-8 -*-
def calc(op, x, y):
 return op(x,y)
def div(a,b):
 if b != 0:
  return a/b
 print("Denom was 0.") #Bu kodda print satırı, bir else bloğu gibi davranarak, if bloğunun koşulu sağlanmadığında çalışacak bir alternatif yol sunar. Ancak, return anahtar kelimesinin kullanımı nedeniyle tam olarak bir else bloğu olarak adlandırılamaz.
res = calc(div,2,0)

