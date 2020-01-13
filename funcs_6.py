# keyword only arguments
def add(a, b=10, *c, d, e):  # d and e are keyword only arguments because all other values are captured by c
    r = a + b + sum(c) + d + e
    return r


res = add(10, 20, 30, 40, 50, e=60, d=70)
print('res =', res)


def telnet(*cmds, h=None, p=None):
    return 'Hello'


res2 = telnet()
res3 = telnet('dir')
print(res2, res3)
res4 = telnet('dir, p=1, h=2')
print(res4)

# telnet(*, h, p) for this function declaration h and p are both keyword only arguments
