#Realice un programa que lea 4 números y diga cuántos son pares y cuantos impares y devuelva la sumatoria de los pares.

números= []
impares= 0
pares= 0
suma= 0
for i in range(4):
    números.append(int(input("ingrese un número: ")))
    if (números [i]%2 == 0):
     pares= pares + 1
     suma= suma + números [i]
    else:
       impares = impares + 1
       print ("Los números pares son: ", pares)
       print ("Los números impares ingresasdos son: ", impares)
       
       
              
 