edad_como_cadena = input("Dime tu edad: ")
edad = int(edad_como_cadena)

if edad >= 0 and edad <= 2:
    print("Bebé")
elif edad >= 3 and edad <= 11:
    print("Niño")
elif edad >= 12 and edad <= 17:
    print("Adolescente")
elif edad >= 18 and edad <= 64:
    print("Adulto")
elif edad >= 65:
    print("Anciano")
else:
    print("Edad inválida")


