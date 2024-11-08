# -*- coding: utf-8 -*-
def firstName(fullName):
    firstSpace = fullName.index(" ")
    givenName = fullName[:firstSpace]
    return givenName

fullName = input("Enter a person's full name: ")
print("First name:", firstName(fullName))

