# -*- coding: utf-8 -*-

def char_counts(s):
    """ s is a string of lowercase chars
Return a tuple where the first element is the
number of vowels(sesliler) in s and the second element
is the number of consonants(sessizler) in s
    """
    vowels='aeuıiöüo'
    (num_vow,num_cons)=(0,0)
    for i in s:
        #if i==vowels--Bu satır, i değişkeninin tam olarak 'aeuıiöüo' adlı dizeye eşit olup olmadığını kontrol eder.
        if i in vowels:
            num_vow+=1
        elif i not in vowels:
            num_cons+=1
        if i==' ':
            num_cons-=1
    return(num_vow,num_cons)
print(char_counts('selamlar'))
print(char_counts('hi there'))        
    