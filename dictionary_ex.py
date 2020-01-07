#dictionary -> class
D = { 'course' : 'python', 'dur':10, 'loc':'Blr'}
print(D)
print(D['course'])

# Dictionary are unordered

#add or update
D['course'] = ['c++', 'java']
print(D)
E = D.copy()

#remove from a dictionary
r1 = D.pop('course')
print('pop =', r1, D)
del D['dur']
print('After del =', D)
r2 = D.popitem()
print('Pop item =', r2, D)

#other methods
K = E.keys()
V = E.values()
I = E.items()
print(K, V, I, sep = '\n')
