class A:
    x = 10

    def __init__(self):
        self.y = 20

    def change(self):
        A.x = A.x + 5
        self.y = self.y + 5


a1 = A()
a2 = A()
a1.change()
a2.change()
print(A.x)
print(a1.y)
print(a2.y)