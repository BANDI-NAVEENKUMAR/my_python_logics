# Mutliple inheritance:- When a class is child from more then one parent class it is called multiple inheritance.
# The child class inherits all the features of the parent class.

class A:
    x = 10
class B:
    y = 20
class C(A,B):
    pass

c = C()
print(c.x)
print(c.y)