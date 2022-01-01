def outer():
    def inner(a):
        print(a-5)
    return inner
naveen = outer()
naveen(10)