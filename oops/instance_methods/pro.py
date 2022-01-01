class Mobile:
    def __init__(self,model,camera,price):
        self.model = model
        self.camera = camera
        self.price = price
    def make_call(self,number):
        print('make_calling,,,,,...{}'.format(number))

m1 = Mobile('vivo','64 mp','13000')
m2 = Mobile('honor', '64 mp','8500')
print(m1.__dict__)
print(m2.__dict__)
m1.make_call(6301012986)
m2.make_call(8297565729)


