list1 = [1, 3, 5, 16, 8]
list2 = [6, 5, 9, 4, 13, 12]

list3 = list(set(list1 + list2))
print(list3)
s = input('Enter a device id')
s = int(s)

try:
    indexv = list3.index(s)
    print('Value is ', list3[indexv])
    print('Index is ', indexv)
except ValueError:
    for i in range(len(list3)):
        if s > list3[len(list3) - 1]:
            print('Not found')
            break
        if list3[i] > s:
            print('Value is ', list3[i])
            print('Index is ', list3.index(list3[i]))
            break


