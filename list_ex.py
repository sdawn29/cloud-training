#list -> class
l1 = list([10, 20, 30]) # a list of 3 elements
l2 = [10, 12.5, 'python', ['a','b']] #shortcut of creating a list

print(l2)
print(l2[1])
print(l2[2][1])

print(l2[-1:1:-1])

#add element ot the list
l2.append(200)
print('append=',l2)
l2.insert(2,300)
print('Insert=',l2)

l3 = [10,20]
l4 = ['a', 'b']
l5 = l3 + l4
l6 = l3 * 10
print(l5, l6, sep = '\n')

l3.extend(l4)
print('extends =', l3)

#remove elements from list
r1 = l5.pop()
print('r1=', r1, l5)
r2 = l5.pop(2)
print('r2 =', r2, l5)
r3 = l5.remove(20) #in this case we are passing the value, it will remove the first occurance of the value
print('remove=', r3, l5)
del l5[0]
print('After del=', l5)

#update elements to the list
print('l3=',l3)
l3[1] = 'Java'
print('after update=',l3)

#some other methods
l6 =[10, 30, 20]
l6.sort() #ascending order
print('sort ascend =', l6)
l7 = ['z','a','b']
l7.sort(reverse = True) #descending order
print('sort desc =', l7)
l8 = [10, 'a', 20, 'b']
l8.reverse() # print the reverse of the list
print('reverse=',l8)
l8.clear()
print('l8=',l8)

#copy
l = [10, ['a', 'b']]
m = l # Reference copy
n =l.copy() #shallow copy

#copy module -> copy(), deepcopy()
import copy
p = copy.deepcopy(l)
print(id(l[0]), id(p[0]))
print(id(l[1]), id(p[1]))

