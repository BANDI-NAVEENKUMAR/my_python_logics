class A:
    def a1(self):
        print("classA")
class B:
    def b1(self):
        print("classB")
class C:
    def c1(self):
        print("classC")
class D(A,B,C):
    def d1(self):
        print("classD")

d = D()
d.a1()
d.b1()
d.c1()
d.d1()