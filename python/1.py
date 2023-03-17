class Perro ():
    def __init__(self,n,r,c) -> None:
        self.nombre=n
        self.raza=r
        self.tamaño=None
        self.edad=None
        self.color=c


    def jugar(self):
        print("{} esta jugando su pelota".format(self.nombre))

    def dumierdo(self):
        print("{} el esta se esta tomando una fiesta ".format(self.nombre))

    def molesto(self):
        print("{} es te esta ladrando, porque anda furioso ".format(self.nombre))
    

    def llama(self,nombre):
        self.nombre=nombre
        

    def cumpleaños(self,):
        self.edad = 4
        print(" su edad de {} es de  {} años".format(self.nombre,self.edad))


class persona(Perro):
    def __init__(self, n, r, c,a) -> None:
        super().__init__(n, r, c)

    def altura(self):
        print(" su nombre se llama {} ".format(self.nombre),"su raza es {}".format(self.raza),"su color de pie es {}".format(self.color),"y su tamaño es {} ".format(self.tamaño))



        
        
mi_perro = Perro("bobo","pitbull","negro")
print(mi_perro.nombre)
mi_perro.jugar()
mi_perro.cumpleaños()


persona1=persona("tonto","maya","moreno","grande ")
persona1.altura()
