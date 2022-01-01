# outer-> calculator:- should be return inner function.

def calculator():
    def add(a,b):
        print(a + b)
    return add
r = calculator() # calling to add.
r(10,20) # taKen the add() of values.
