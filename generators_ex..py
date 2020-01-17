T1 = (10, 20, 30)
T2 = (i for i in range(10))
line = '-' * 40

print('T1 =', T1)
print('T2 =', T2)
print('list(T2) =', list(T2))
print(line)

L = [1, 2, 3, 4]
def squares(M):
    res = []
    for j in M:
        r = j * j
        res.append(r)
    return res


r1 = squares(L)
for a in r1:
    print('a =', a)
print(line)


def gen_squares(N):
    for k in N:
        yield k*k
    
    for l in N:
        yield l*l


r2 = gen_squares(L)
for b in r2:
    print('b =', b)

print('r1 =', r1)
print('r2 =', list(r2))