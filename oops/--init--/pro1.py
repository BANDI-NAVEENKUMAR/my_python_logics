class sample:
    def __init__(self):
        self.x = 10
        self.y = 20
    def increase(self):
        self.x = self.x + 20
        self.y = self.y + 40
    def decrease(self):
        self.x = self.x - 10
        self.y = self.y - 20
s1 = sample() # goto __init__(self)
s2 = sample() # goto __init__(self)
s1.increase() #s1 access to increase(self)
s2.decrease() #s2 access to decrease(self)
print(s1.__dict__)
print(s2.__dict__)
