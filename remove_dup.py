# -*- coding: utf-8 -*-
def remove_dup(L1,L2):
    L1copy=L1[:]
    for char in L1copy:
        if char in L2:
            L1.remove(char)
    return L1
L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]
remove_dup(L1, L2)
print(L1)

