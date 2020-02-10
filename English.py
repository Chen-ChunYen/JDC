# Jack's Dictionary System.
# Created by Chun-Yen, Chen (Jack).
# 2020/02/10
# Copyright Chun-Yen, Chen. All right reserved.

import functions as fun

print("Welcome to JDS!")
print("This is a dictionary which created by Chun-Yen.")
print('----------')
print('Notice:')
print('----------')
print("V0.0.0  2020/02/10")
print('----------')
print('What can I help you today?')

request = input('Search: s, Add: a, Modify: m, Quit: q\n')
while request != 'q':
    if request == 's':
        print("What do you want to search?")
        search = input()
        #searching function
        fun.searching(search)
        
    elif request == 'a':
        print("What do you want to add?")
        add = input()
        #adding function
        fun.adding(add)
        
    elif request == 'm':
        print("What do you want to modify?")
        modify = input()
        #modifying function
        fun.modifying(modify)
        
    else:
        print("Wrong input!")

    print("==========")
    request = input('Search: s, Add: a, Modify: m, Quit: q\n')

print("Thank you! Press 'Enter' to leave...", end = '')
input()
