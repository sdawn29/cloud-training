# -*- coding: utf-8 -*
D = {'ROM': 'ROM information',
     'HDD': 'HDD information',
     'FDD': 'FDD information',
     'RAM': 'RAM information',
     'CPU': 'CPU Information'}
flag = 99
search = input('Enter term to search: ')
keysList = sorted(list(D.keys()))
item = D.get(search)

if item is None:
    for i in keysList:
        if i.startswith(search):
            flag = 1
            print(D.get(i))
else:
    print(D.get(search))
    flag = 1

if flag != 1:
    print('Device Not Found')
