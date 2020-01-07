a = 'PERSON'
print(a)

b = "PERSON'S"

c = '''PERSONS'S HEIGHT XYZ"'''

d = """Person"""
print(b, c, d, sep='\n')

s1 = 'Hello'
s2 = 'py'
s3 = s1 + s2
s4 = s1 * 10
print(s3, s4)
line = '-' * 40
print(line)

e = 'Person\'s'
print(e)

f = r'c:\newfolder\test.py'  # r denotes raw string and ignores all escape sequences
print(f)

g = 'WEL COME'
print(g)
print(len(g))  # len() -> find the length of any collections
print(g[1])  # get character from any index
print(g[
      1:6])  # get the substring from index 1 upto index 6 the end index is excluded this can be used in any collections if the collection  is indexed
print(g[1:])  # substring till the end
print(g[:6])  # substring from the beining to the end
print(g[:])  # all the characters of the string will be printed

h = g[:]
print(id(h), id(g))

# step
print(g[1:6:1])
print(g[1:6:2])  # final attribute os for stepping in this case the elements will be stepped by 2

# reverse
print(g[::-1])
print(g[6:1:-2])  # index is reered while using a negative step the output will also come reverse

# negative index
print(g[-7:-2])

# last four characters 
print(g[len(g) - 4:])  # using only positive index
print(g[-4:])  # using negative index

# str -> class
i = 10
j = str(i)  # '10'
k = str('Python')
print(i, j, k, sep='\n')

r1 = g.startswith('wel')  # returns a boolean value
print('r1 =', r1)
r2 = g.endswith('me')
print('r2 =', r2)

r3 = g.isupper()
r4 = g.upper()
print(r3, r4, sep='\n')

r5 = g.islower()
r6 = g.lower()
print(r5, r6, sep='\n')

l = 'abc'
r7 = l.isalpha()

m = '123'
r8 = m.isdigit()

n = 'abc123'
r9 = n.isalnum()
print(r7, r8, r9, sep='\n')

r10 = n[-3:].isdigit()
print(r10)

r11 = g.count('E')  # count the number of occurences of e in the given string
print('r11 =', r11)

r12 = g.index('E')  # if not found it will throw index error
r13 = g.find('E')  # if not found it will return -1
print(r12, r13)

r14 = g.index('E', 3)  # start looking for the character from the 3rd index
r15 = g.index('E', 3, 8)  # find the character between the index 3 to 8
print(r14, r15)

r16 = g.rindex('E')  # returns the index of the position of the character starting from the reverse
print('r16 =', r16)

p = '   wel   come   '
r17 = p.strip()  # removes all trailing spaces
r18 = p.lstrip()  # removes trailing spaces from the left side of the string
r19 = p.rstrip()  # removes trailing spaces from the right side of the string
print(r17, r18, r19, sep='\n')

q = '[wel[come][]'
r20 = q.strip(']w[e')  # checks each charater from the ends with the group of the given characters and the removes the character untill it reaches the character from which it cant remove an more character
r21 = q.lstrip('w[')
r22 = q.rstrip('][e')
print(r20, r21, r22)

r23 = g.replace('E', 'e')
print('r23 =', r23)

r24 = g.split()  # whereever there is a space the string will split and become elemets of a list
r25 = g.split('E')  # splits where there is a 'E'

x = 10
y = 20
z = x + y
r26 = 'add of x and y is z'
r27 = 'add of {} and {} is {}'.format(x, y, z)  # formating stings while showing the output, 1 to 1 ,aping in this case
r28 = 'add of {1} and {0} is {2}'.format(x, y,
                                         z)  # inside the braces we can mention the indes number of the format() parameters
# python v3.5 and up
r29 = f'add of {x} and {y} is {z}'

r30 = '-'.join(g)  # seperate each character with the -
