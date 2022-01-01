from abc import abstractmethod,ABC

class A(ABC):
    @abstractmethod
    def s1(self):
        print('life is beautiful')

class B(A):
    @abstractmethod
    def s2(self):
        print('life is wonderful')

class C(B):
    def s1(self):
        print('hello')
    def s2(self):
        print('tell me')

c = C()
c.s1()
c.s2()
