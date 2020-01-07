a = 0
if a == 10:
    print('a eq 10')
if a > 10:
    print('a gt 10')
if a < 10:
    print('a lt 10')

a = 0
if a == 10:
    print('a eq 10')
elif a > 10:
    print('a gt 10')
elif a < 10:
    print('a lt 10')

a = 0
if a == 10:
    print('a eq 10')
elif a > 10:
    print('a gt 10')
else:
    print('a lt 10')

S = 'python'
if 'th' in S:
    print('Substring found')
if not S.startswith('java'):
    print('Not java')
if S != 'c++':
    print('Not c++')
if S[1:3] == 'yt':
    print('yt found')

L1 = [10, 20]
L2 = L1
L3 = L1.copy()
if 20 in L1:
    print('20 found')
if L1 is L2: # is compares the id of the the list or the references
    print('Both reffers the same object')
if id(L1) == id(L2): # same as the previous staement checks the reference of the objects
    print('Both refers same object')
if L1 == L3: # checks the content also
    print('contents are the same in the both lists')

D = {'A':10, 'B':20}
if 'B' in D:
    print('Key-B is found')
if 'B' in D.keys():
    print('Key B found')
if 20 in D.values():
    print('20 found')
if ('A', 10) in D.items(): # [('A',10), ('B', 20)]
    print('Items found')

# to keep any block empty the keyword pass is used
if a > 10:
    pass