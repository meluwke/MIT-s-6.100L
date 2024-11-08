# -*- coding: utf-8 -*-
def count_words(sen):
    """ sen is a string representing a sentence
    Returns how many words are in s (i.e. a word is a
    a sequence of characters between spaces. """
    L1 = sen.split()
    return len(L1)
print(count_words("Hello it's me"))
print(count_words("naber nasılsın iyi misin"))
print(count_words("ben")) 