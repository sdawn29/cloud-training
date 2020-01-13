s = 'abc123xyz456ABC'
r1 = s.split('123')
print(r1)

import re

r2 = re.split('\d{3}', s)
print(r2)

r3 = s.find('123')

if r3 != -1:
    print('Substring found')

r4 = re.search('\d{2}', s)
if r4 is not None:
    print('Digit Found')

F = open(r'C:\Users\lab365\Desktop\Python Training\log\serverlog.txt')
data = F.read()
ips = re.findall('\d{3}\.\d{3}\.\d{3}\.\d{3}', data)
print('ips=', ips)
