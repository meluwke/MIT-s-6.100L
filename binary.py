# -*- coding: utf-8 -*-
## Only positive numbers
num = 1507
result = ''
if num == 0:
   result = '0'
while num > 0:
  result = str(num%2) + result #yan yana ekliyor toplama işlemi yok.
  num = num//2
print(result)
