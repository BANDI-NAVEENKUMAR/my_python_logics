class Matli:
    def m1(self):
        print("all of members")
class Vaddepalli(Matli):
    def m2(self):
        print("vaddepalli pepole")
class Yallampalli(Matli):
    def m3(self):
        print("yallampalli pepole")
class Peddur(Matli): # only access to parent class(Matli). not access to Vaddepalli, Yallampalli.
    def m4(self):
        print("peddur people")

m = Matli()
m.m1()
v = Vaddepalli()
v.m1()
v.m2()
y = Yallampalli()
y.m1()
y.m3()
p = Peddur()
p.m1()
p.m4()