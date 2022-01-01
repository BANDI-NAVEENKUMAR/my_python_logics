# returning a function from another function.

def f1(x):
    return x**2
res = f1(11)
print(res)


def f1():
    def f2():
        print('hai')
    return f2
i = f1()
i()
