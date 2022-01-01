# Hierarichical inheritance:- one class can be inherited by multiple class.

class A:
    def m1(self):
        print("parent class")
class B(A):
    x = 10
class C(B):
    y = 20
class D(C):
    z = 40
class E(C):
    m = 50

d = D()
d.m1()
print(D.x)
print(D.y)
print(D.z)
e = E()
print(E.m)