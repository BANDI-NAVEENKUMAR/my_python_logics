class Student:
    c = 20
    def __init__(self):
        self.x = 10
    def m1(self):
        self.x = 50
    @classmethod
    def m2(cls):
        cls.c = 100

s = Student()
s.m1()
print(s.x) # x.=10 access to x.=50
Student.m2()
print(s.c) # c=20 access to cls.c=100

