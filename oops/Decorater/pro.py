# create a nested function
# 1. outer function must take one mandatory.
# 2.outer function should return inner function.

def outer(x):# x = f1
    def inner():# f1 = inner
        print('hai')# access to @outer
    return inner
@outer
def f1():# calling to x = f1 and f1 = inner.
    print('hello')
f1()
