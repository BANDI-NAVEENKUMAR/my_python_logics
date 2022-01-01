class grand_father:
    def b1(self):
        print("hi")
class father(grand_father):
    def b1(self):
        super().b1()
        print("hello")
class son(father):
    def b1(self):
        print("how are you both of you")

s = son()
s.b1()
f = father()
f.b1()