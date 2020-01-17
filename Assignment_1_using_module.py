import Assgmt_1_func as af
while True:
    i = input('Enter ID: ')
    i = eval(i)
    L = [20, 10, 30]
    L.sort()
    r = af.dev_id_search(i, L)
    print('result=', r)
    ch = input('Quit(y/n)?: ')
    if ch == 'y':
        break
