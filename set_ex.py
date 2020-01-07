# Unordered Collection
# No Index
# No Key
# Mutable
# It can hold only immutable objects
# stores the unique values

S = {10, 10, 20, 'python'}
print(S)

#adding values to a set
S.add(30)
S.add(30)
print('add=', S)

#removing from set
r1 = S.remove(10)
print('remove=', S, r1)
r2 = S.pop()
print('pop =',r2, S)

# set operations
S1 = { 10, 20, 30, 40 }
S2 = { 30, 40, 50, 60 }
S3 = S1.union(S2)
print('union=', S3)
S4 = S1.intersection(S2)
print('intersection=',S4)
S5 = S1.difference(S2)
S6 = S1-S2
print(S5, S6, sep = '\n')
