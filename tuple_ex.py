#tuple -> class
T1 = tuple([10, 20, 30])
T2 = (10, 12.5, 'python', ['a', 'b'], (10, 20))
print(T2)
print(T2[1])
print(T2[-4:4:2])

i = T2.index('python')
c = T2.count(12.5)
print(i, c)

#converting tuple to list
T = (10, 20)
L = list(T)
print('L =', L)

#converting list to tuple

L = [30, 40]
T = tuple(L)
print('T =', T)
