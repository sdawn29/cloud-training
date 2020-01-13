x = 10


def f1():
    x = 20  # enclosed scope local to this function and its inner function would be able to access

    def f2():
        # nonlocal x  # nonlocal keyword checks the immediate variable for the value
        global x  # global keyword is used to access the global variable
        x = 30  # Local Scope
        print('F2 =', x)

    f2()
    print('F1 =', x)


f1()
print('Global =', x)

print(dir(__builtins__))
