# -*- coding: utf-8 -*-

def first_to_last_diff(s, c):
    """ s is a string, c is single character string
        Returns the difference between the index where c first
        occurs and the index where c last occurs. If c does not 
        occur in s, returns -1. 
    """
    if c not in s:
        return -1
    
    for a in range(len(s)):
        if s[a]==c:
            break #burda break veriliyor ki a'nın direkt index değeri kaydedilsin.
    for j in range(len(s)-1,-1,-1): #range(start,stop,step)
        if s[j]==c:
            break
    sonuc=j-a
    return sonuc
    
print(first_to_last_diff('aa', 'a'))

# 2. Write code that satisfies the following specs:
# For example
# print(first_to_last_diff('aaaa', 'a'))  # prints 3
# print(first_to_last_diff('abcabcabc', 'b'))  # prints 6
# print(first_to_last_diff('aacc', 'b'))  # prints -1

