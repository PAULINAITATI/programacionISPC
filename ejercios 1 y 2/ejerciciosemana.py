#Realice un programa que pida un número del 1 al 7 y diga el nombre del mes correspondiente.
numero = int(input("Ingrese un número del uno al siete: "))

if numero == 1:
    print ("Lunes")
elif numero == 2:
    print ("Martes")
elif numero == 3:
    print ("Miércoles")
elif numero == 4:
    print ("Jueves")
elif numero == 5:
    print ("Viernes")
elif numero == 6:
    print ("Sábado")
elif numero == 7:
    print ("Domingo")
else:
    print("Los datos ingresados son incorrectos")