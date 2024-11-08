# -*- coding: utf-8 -*-
secret=9
if secret in range(1,11):
    print(f'{secret} is in range!')
else:
    print("secret is not in range of 1-10.")

# another way   
# secret = 7
# found_flag = False
# for i in range(1, 11):
#     if i == secret:
#         found_flag = True
#         print("found")
# if found_flag == False:
#     print("not found")
