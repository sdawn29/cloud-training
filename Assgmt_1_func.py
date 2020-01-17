"""
this is the functional implementation of the assignment 1

>>> L = [10, 20, 30]
>>> dev_id_search(20, L)
'Dev Id found,Dev Id=20Index=1'
>>> dev_id_search(20)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: dev_id_search() missing 1 required positional argument: 'dev_list'

"""


def dev_id_search(dev_id, dev_list):
    if dev_id in dev_list:
        return 'Dev Id found,Dev Id=' + str(dev_id) + 'Index=' + str(dev_list.index(dev_id))
    elif dev_id > max(dev_list):
        return 'Not found'
    else:
        for i in dev_list:
            if i > dev_id:
                return 'val=' + str(i) + 'ind=' + str(dev_list.index(i))


def main():
    l1 = [1, 3, 5, 16, 8]
    l2 = [6, 5, 9, 4, 13, 12]
    l3 = l1 + l2
    s = set(l3)
    l4 = list(s)
    while True:
        i = input('Enter id to search:')
        i = eval(i)
        r = dev_id_search(i, l4)
        print('Search Result=', r)
        ch = input('Quit(y/n)?')
        if ch == 'y':
            break


# if we write main() then it will work but if we want to use this function in other file then import will execute
# everything even main too so we dont want main to be executed in other file
if __name__ == '__main__':
    main()
    import doctest
    doctest.testmod()
