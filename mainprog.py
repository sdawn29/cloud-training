import addmodule

print(addmodule.msg)
print(addmodule.add(45, 10))
line = '-' * 40
print(line)

# 2nd way to add path using program to do this we use a std library named sys
import sys

print(sys.path)
# sys.path.append(r'C:\Users\lab365\Desktop\Python Training\lib')

import addmodule as a
print(a.msg)
print(a.add(10, 20))
print(line)


from addmodule import msg, add
print(msg)
print(add(10, 29))
print(line)

from addmodule import msg as m, add as a
print(m)
print(a(10, 20))
print(line)

from addmodule import *
print(msg)
print(add(10, 20))
print(line)

import project.net.addmodule
print(project.net.addmodule.msg)
print(line)

import project.net.addmodule as a
print(a.msg)
print(line)

from project.net.addmodule import msg, add
print(msg)
print(line)

