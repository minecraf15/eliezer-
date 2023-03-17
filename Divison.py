print("ingresa un numero de las tablas de multiplicar:  ")
a=True
while a == True:
    try:
        num = int (input("ingres dos numeros "))
        num2= int (input("ingresa un numero2"))
        resultado = num/num2
        if resultado>0:
            a=False
            print(resultado)
    
    
    except Exception:
        print("no ingreso bien el numeor ")




        
