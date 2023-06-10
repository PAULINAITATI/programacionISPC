#3. Realice un programa que lea tres números, muestre cuál es el mayor y determine si es par o impar.


a= int(input("Ingrese un número:" ))
b= int(input("Ingrese un número:" ))
c= int(input("Ingrese un número:" ))

numero=0
if b < a > b:
    numero= a
    print ("El número mayor es: ", a)

elif a < b > c:
    numero= b
    print ("El número mayor es: ", b)
elif a < c > b:
     numero= c
     print ("El número mayor es: ", c)

if numero % 2 == 0:
    print(numero, "es par.")
else:
    print(numero, "es impar.")

