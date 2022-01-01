class A:
    def __init__(self):
        self.x = 15
        self.y = 17
class B(A):
    def m1(self):
        print(self)

a=A()
b=B()
print(a.x)
print(a.y)
print(b.x)
print(b.y)


