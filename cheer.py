
letters="aeoöiıüuAEOUÜİÖI"
word=input("give me a cheer word: ")
times=int(input("which level do you want? (1-10): "))
for a in word: #for each a in 'word'
    if a in letters:
        print(f'give me an {a}: {a}') #print("give me an",a,": ",a)
    else:
        print (f'give me a {a}: {a}')
print("what is that spell?")
print ((f'{word} !!!\n')*times)
    # you can also use for last print:
    # for i in range(times):
    #   print (word,'!!!')