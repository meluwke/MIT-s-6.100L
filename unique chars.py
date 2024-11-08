# -*- coding: utf-8 -*-
# Assume you are given a string of lowercase letters in variable s. 
# Count how many unique letters there are in s. For example, if 
# s = "abca" Then your code prints 3. 

s="abcdefffffffffffbddeeeff"
char=""
for a in s:
   if a not in char:
     char= a+char #becuz now im creating a new variable i need to write 'char' to left
print (len(char))  
   
    #In Python, the left side of an assignment must be a variable, and it must directly refer to a location in memory that can hold a value.
    #a + char is an expression that adds (concatenates) two strings, but it is not a valid left-hand operand for assignment. The left-hand side of the = operator must be a variable that you can assign a value to, and a + char is not a valid place to store a value—it's a temporary result, not a variable.
