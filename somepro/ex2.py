class Duck:
    def __init__(self):
        print('quack..quack..')

class Dog:
    def __init__(self):
        print('bow..bow..')

class Cat:
    def __init__(self):
        print('moew..moew..')

class Goat:
    def __init__(self):
        print('myaah..myaah..')

i=[Duck(),Dog(),Cat(),Goat()]
for obj in i:
    print(obj)