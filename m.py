class Sq:
    def __init__(self, s):
        self.so = s

    def A(self):
        return (self.so ** 2)
    
    def perim(self):
        print(4 * self.so)

class Trian(Sq):
    def __init__(self, s):
        super().__init__(s)

    def A(self):
        print((2 * (self.so ** 2)) / 2)
    
    def perim(self):
        print(3 * self.so)

class Py(Trian, Sq):
    def __init__(self, h, k_1 ,l ):
        self.h_2 = h
        self.k_1 = k_1
        self. l  = l
    def A(self):
        print(Sq(self.l).A() + (4 * (Trian(self.k_1).A())))
    
    def s_A(self):
        print(4 * (Trian(self.l).A()))
    
    def vo(self):
        return (self.s_s * self.s_t * self.h) / 3
pi = float(input("enter sq: "))
li = float(input("enter trian: "))
ki = float(input("enter py: "))
squar = Sq(pi)
trian = Trian(li)
pyram = Py(ki, pi, li)
print( squar.A(),  squar.perim())
print( trian.A(),trian.perim())
print(pyram.A(),  pyram.vo(),pyram.s_A())