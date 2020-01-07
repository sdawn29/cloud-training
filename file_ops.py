# 1st way to write into a file
F1 = open('out1.txt', 'w')
x = 10
s = 'Python\n'
x = str(x) + '\n'
F1.write(x)
F1.write(s)
F1.flush() # transfers data frm buffer to file without closing the connection

# 2nd way to write to a file
L = [x, s]
F1.writelines(L)
F1.close()

F2 = open('out1.txt', 'r') # if file not available it will not create the file instead it will show an error
r1 = F2.read()
print('r1 =',r1)
F2.seek(0)
r2 = F2.read()
print('r2 =,', r2)
F2.seek(0)
r3 = F2.readline()
print('r3=',r3)
while True:
    line = F2.readline()
    if line == '':
        break
    else:
        print('line =', line)

F2.seek(0)
r4 = F2.readlines()
print('r4 =', r4)

r5 = []
for l in r4:
    l = l.strip()
    r5.append(l)
print('r5=', r5)

F2.seek(0)
for x in F2:
    print('Line =', x)

F2.seek(0)
r6 = list(F2)
F2.seek(0)
r7 = tuple(F2)

L1 = [ 'h1', 'h2']
L2 = ['ip1', 'ip2']
D1 = dict(zip(L1, L2))
print('D1 =', D1)

e = enumerate(L1)
print(list(e))

F2.seek(0)
D2 = dict(enumerate(F2))
print('D2 =', D2)
F2.close()

F3 = open('out1.txt', 'a')
F4 = open('out2.csv', 'a') # append mode uses the same file if present and appends contents to it
print(20, 'java', sep = '\n', file = F3, flush = True)
print(20, 'java', sep = ',', file = F4)
F3.close()
F4.close()

# 'w' -> Write only
# 'r' -> Read only
# 'a' -> Append only
# 'w+' -> Write and read
# 'r+' -> Read write
# 'a+' -> Append and read

# FOR BINARY FILES
# 'wb' -> Write only
# 'rb' -> Read only
# 'ab' -> Append only
# 'w+b' -> Write and read
# 'r+b' -> Read write
# 'a+b' -> Append and read
