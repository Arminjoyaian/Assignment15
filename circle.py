import math

class Circle:
    def __init__(self, c):
        self.cir = c

    def A(self):
        print((self.cir ** 2) * math.pi)

    def Perim(self):
        print((self.cir * 2) * math.pi )
    
class Sh(Circle):
    def __init__(self, s):
        super().__init__(s)
        
    def A(self):
        print((self.cir ** 2) * math.pi * 4)

cir = Circle(3)
print(cir.A())
sh = Sh(3)