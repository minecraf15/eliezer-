

#las tablas de multiplicar con for
print("ingresa un numero de las tablas de multiplicar:  ")
a=True
while a== True:
 try:
    num=int(input(" tamine se pode poder cosas negativas "))
    if num>0 or num<1:
      a=False
 except Exception:
    print("pusiste algo mal")
    print("vuelve intentarlo ")
 except ZeroDivisionError:
   a=0
for e in range(1,11):
  resultado=e*num
  print(num,"x",e," = ",resultado)
  




 
