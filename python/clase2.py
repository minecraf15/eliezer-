class Animal():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

   
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")

class Vaca(Animal):
    def hacer_sonido(self):
        print("Muu")



perro = Perro("Fido", 3)
gato = Gato("Pelusa", 2)
vaca = Vaca("Lola", 5)

perro.hacer_sonido()  # "Guau"
gato.hacer_sonido()  # "Miau"
vaca.hacer_sonido()  # "Muu"