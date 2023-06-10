numeros = []
mayores = 0
menores = 0
max = 0
min = 0

for i in range(10):
    numeros.append(int(input("ingrese un numero : ")))
    if (numeros[i] > max):
        max = numeros[i]
        
    elif (numeros[i] < min):
        min = numeros[i]
    elif (min == 0):
        min = numeros[i]

    if (numeros[i] > 100):
        mayores = mayores + 1
    else:
        menores = menores + 1

print("Los números mayores son :", mayores, " los números menores son :", menores)