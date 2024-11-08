# -*- coding: utf-8 -*-

sleep_time=int(input("how many hours do you sleep in a day?\n"))
food_time=int(input("how many hours do you eat in a day?\n"))
freetime=abs(24-(sleep_time+food_time))
if (sleep_time+food_time)>24:
    print("that's impossible! dont lie.\n")
elif (sleep_time+food_time)>=24:
    print("no free time! sorry.\n")
else:
    print("you have",freetime,"hours as freetime. have fun!")
    

