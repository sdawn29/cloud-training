"""This file is about the list
to merge it, remove duplicates  and perform
search operation. If not found give the next no and index"""
l1 = [1, 3, 5, 16, 8]
l2 = [6, 5, 9, 4, 13, 12]
l3=l1+l2
s=set(l3)
l4=list(s)
l4.sort()
print(l4)
while True:
    in_val=input('Enter Device ID:')
    in_val=int(in_val)
    if in_val in l4:
        print('Device ID found,ID=',in_val,'Its Index:',l4.index(in_val))
    elif in_val>max(l4):
        print('Not found')
    else:
        for i in l4:
            if i>in_val:
                print('val=',i,'ind=',l4.index(i))
                break
    ch=input('Do you want to quit(y/n)?')
    if ch=='y':
        break

