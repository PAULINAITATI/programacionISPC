#Realice un programa que lea dos números y diga cuál es el mayor.
a= int(input("Ingrese un número: "))
b= int (input ("Ingrese otro número: "))
if a==b:
    print ("Los números ingresado son iguales")

elif a > b:
    print(f"El número mayor es: {a}")
else:
    print(f"El número mayor es: {b}")