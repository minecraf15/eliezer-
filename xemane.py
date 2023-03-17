class Persona:
    PE=" "
    nombre = ""
    edad = ""
    def  __init__(self):
        self.nombre = input('Ingrese su nombre: ')
        self.edad = int(input('Ingrese su edad: '))
        print(f'te llamas {self.nombre} tienes {self.edad} años')
class Estudiante(Persona): #se comienza con la herencia
    def prom_final(C1, C2, C3):
        CF = (C1 + C2 + C3) / 3
        return CF
class Docente(Persona):
    def salario_fin(Hora, salarioo):
        SF = (Hora * salarioo)
        return SF
print("Bienvenido al programa, si es un alumno y desea saber su calificacion, presione 1")
print("Bienvenido al programa, si es un docente y desea saber su salario total, presione 2")
Res = int(input("¿Que desea hacer? "))


if Res == 1:
    PE=Estudiante()
    C1=int(input("ingresa tu primera calificacion: "))
    C2=int(input("ingresa tu segunda calificacion: "))
    C3=int(input("ingresa tu tercera calificacion: "))
    R=Estudiante.prom_final(C1,C2,C3)
    print("tu promedio final es", +R)
    if R>70:
        print ("¡Bien hecho!")
    elif R<70:
        print ("Ups... hay que estudiar más")

elif Res == 2:
    PE=Docente()
    HOG = int(input("¿Cuanto ganas por hora?: "))
    Hora = int(input("¿Cuantas horas trabajas a la semana?: "))
    resultado = Docente.salario_fin(HOG, Hora)
    print("tu salario final es de ", +resultado, "pesos")

print ("Muchas gracias por usar este programa :)")
