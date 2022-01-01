from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def m1(self):
        print('stammer')
class B(A):
    def m1(self):
        super().m1() # this is access to parent method in child class
        print('sutter')

b = B()
b.m1()