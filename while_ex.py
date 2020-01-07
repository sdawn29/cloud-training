a = 0
while a < 10:
    print('a =', a)
    a += 1 # a = a + 1

S = 'python'
b = 0
while b < len(S):
    print('b =', S[b])
    b += 1

L = ['FN', 'LN', 'ADR', 'a1', 'FN', 'ADR', 'a2']
i = 0
while i < len(L):
    if L[i] == 'ADR':
        i = i + 1
        print(L[i])
        i = i + 1
    else:
        i = i + 1

j = 0
while j < len(L):
    if L[j].startswith('a'):
        print('FOUND')
        break
    else:
        j = j + 1
else:
    print('Not Found')

k = 0
while k < len(L):
    if not L[k].startswith('a'):
        k = k + 1
        continue
    print(L[k])
    k = k + 1
    print('Last statement of while')

cart = []
while True:
    i = input('Enter Item:')
    cart.append(i)
    ch  = input('quit(y/n)? :')
    if ch == 'y':
        print('cart =', cart)
        break

