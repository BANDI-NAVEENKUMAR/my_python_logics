# ambiguity:-

class A:
    def m1(self):
        print("A")
class B:
    def m1(self):
        print("B")
class C:
    def m1(self):
        print("C")
class D(B,C):
    pass

d = D()
d.m1()
