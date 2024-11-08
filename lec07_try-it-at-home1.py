# -*- coding: utf-8 -*-

def consonants(word): #consonants=ünsüzler
    """ word is a string of lowercase letters
        Returns a string containing only the consonants 
        of word in the order they appear
    """
    unluler="aeuoıiüö"
    sonuc=""
    for harf in range (len(word)):
        if word[harf] not in unluler:
            sonuc=sonuc+word[harf] #sonuc+=word[harf]
    return sonuc

# other way (more pythonic i guess)
# for harf in word:
#     if harf not in unluler:
#         sonuc+=harf
# return sonuc          
        
print(consonants("abcedsd"))
print(consonants("aaa"))
print(consonants("abc"))

# 1. Write code that satisfies the following specs:
# For example
# print(keep_consonants("abcd"))  # prints bcd
# print(keep_consonants("aaa"))  # prints an empty string
# print(keep_consonants("babas"))  # prints bbs