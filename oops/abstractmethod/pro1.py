from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def m1(self):
        print('absractmethod')
    def m2(self): # this is not abstractmethod but this optional
        print('not abstractmethod')
    @abstractmethod
    def m3(self):
        print('abstractmethod1')

class B(A):
    def m1(self):
        print('abstractmethod')

    #def m2(self):
        #print('hello')
    def m3(self):
        print('abstractmethod1')

b = B()
b.m1()
#b.m2()
b.m3()
