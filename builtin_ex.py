# map
L = [100, 200, 300, 400]


def sub(i):
    return i - 10


lambda i: i - 10

r1 = map(sub, L)
print(list(r1))


# filter
def filt(j):
    return j > 100


r2 = filter(filt, L)
print(list(r2))

# reduce
import functools as fc


def red(p, q):
    return p + q


r3 = fc.reduce(red, L)
M = ['W', 'E', 'L']
r4 = fc.reduce(red, M)
print(r3, r4)

# lambda functions these are the functions that dont have names and we have to write lambda functions in a single
# line we can comprehend any where

r5 = map(lambda i: i - 10, L)
r6 = filter(lambda j: j > 100, L)
r7 = fc.reduce(lambda p, q: p + q, L)

print(list(r5), list(r6), r7, sep='\n')

f= lambda a, b: a + b
rs = f(10, 20)
print('rs =', rs)

L = [(lambda i: i * i)(a) for a in range(10)]
print('L =', L)

keys = ['A', 'B']
values = [10, 20]
D = {k: (lambda i:i+i)(v) for k,v in zip(keys, values)}
print('D =', D)

