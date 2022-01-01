# Nested Funtion:- Nested function can be called from outer function only.

def f1():
    print('hai')
    def f2():
        print('bye')
    f2()

    def f3():
        print('sure')
    f3()




f1()