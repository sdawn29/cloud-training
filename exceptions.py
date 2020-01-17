a = 10
b = 0

try:
    r = a/b
    print('r =', r)
except:
    print('SOME ERROR')

try:
    r2 = a/b
    print('r2 =', r2)

except ZeroDivisionError:
    print('In ZDE')

except NameError as n:
    print('NE =', n)

except (KeyError, IndexError):
    print('KE or IE')

L = []
try:
    print(l[1])

except Exception as e:
    print('e =', e)
    print('type =', type(e))

c =10
d =10

try:
    r = c/d

except:
    print('In Except')

else:
    r = c/c
    print('In else')

try:
    r = c/d
except:
    print('In except')
    # print('xyz')

finally:
    print('In finally')

e = 0
f = 0

try:
    if f == 0:
        raise ZeroDivisionError

    print('stmt-100')
    r = e/f

except ZeroDivisionError:
    print('from raise')

result = 'Test Case Failed'
try:
    assert 'success' in result, 'Some test failed' 
    print('Test case success')

except AssertionError as ae:
    print('ae =', ae)


class MyError(Exception):
    def __init__(self, m):
        self.msg = m

try:
    if 'success' not in result:
        raise MYerror('Test Failed')
    else:
        print('Execution Success')
except MyError as me:
    print('me =', me)
