class A:
    def m1(self):
        print(10)
class B(A):
    def m2(self):
        print(20)
class C(B):
    def m3(self):
        print(40)
class D(C):
    def m4(self):

        print(50)

d = D()
d.m1()
d.m2()
d.m3()
d.m4()


f = [10,20,30]
g = [item * 2 for item in f]
print(g)