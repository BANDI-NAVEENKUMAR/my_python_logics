class A:
    def m1(self):
        print("parent class")
class B:
    def m1(self):
        print('child class')
class C(A):
    def m1(self):
        print("hello")
class D(B,C,A):
    pass


c = C()
c.m1()