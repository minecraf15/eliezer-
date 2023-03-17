class Coche():
    def desplazamiento(self):
        print("me desplazo utilizando cuatro ruedas")


class moto():
    def desplazamiento(self):
        print("me desplazo utilizando dos ruedas ")
    

class Camion():
    def desplazamiento(self):
     print("me desplazo utilizando seis ruedas")



     
     
def desplazamientovihiculo(vihiculo):
    vihiculo.desplazamiento()

mivihiculo=moto()

desplazamientovihiculo(mivihiculo)


