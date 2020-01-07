# core Datatypes
# Numbers
# Strings
'''
LIST
TUPLES
'''

"""
Dictionary
Set
"""

#Numbers
a = 10 #int
b = 12.5 #float
c = 0x12 #hex
d = 0b1010 #bin
e = 0o12 #oct

print('Hello')
print('a')
print('Result = ',a,b,c,d,e, sep = '|', end='.')#file= , flush=
print('Test')

f = int(20)
print(f)

print(a)
print(id(a)) #prints the reference id of a
print(type(a)) #prints the what kind of object it is holding
print(type(a).__name__) #prints the only type of the variable a

a = 100
print(id(a))

b=a #reference copy
a = 200
b = 300

#Sys.getRefcount
