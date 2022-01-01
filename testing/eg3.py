class A(object):
    x=1
class B(A):
    pass
class C(A):
    pass

B.x = 2
A.x = 4
print(C.x)

