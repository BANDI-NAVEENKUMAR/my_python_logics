class A:
    def m1(self):
        print('hello')
    @classmethod
    def m2(cls):
        print('naveen')


a = A()
a.m1()
A.m2()

