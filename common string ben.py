# -*- coding: utf-8 -*-
def commonstring(string1,string2):
    common=[]
    onlystring1=[]
    onlystring2=[]
    for char in string1:
        if char in string2:
            if char not in common:
                common.append(char)
        else:
            onlystring1.append(char)
    for char in string2:
        if char not in string1 and char not in common:
            onlystring2.append(char)
    return (common, onlystring1,onlystring2)

string1=input("str1: ")
string2=input("str2: ")
common,onlystring1,onlystring2 = commonstring(string1, string2)
print(f' common letters are {common}')
print(f' string1s letters are {onlystring1}')
print(onlystring2)
        
            
        
  
  