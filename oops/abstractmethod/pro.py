from abc import ABC,abstractmethod

class Bird(ABC): # Bird is abstractclass and ABC is inheritance
    def fly(self):
        print('flying')
    @abstractmethod # this is abtractmedthod
    def eat(self):
        print('eating biryani')

class Aeroplane(Bird): # Aeroplane is abstractclass
    def eat(self): # manditory
        print('Aeroplane cannot eat')

a = Aeroplane()
a.fly()
a.eat()
