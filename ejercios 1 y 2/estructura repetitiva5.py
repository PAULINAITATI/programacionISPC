#Leer 15 números negativos y convertirlos a positivos e imprimir dichos números# 
numeros = []
maximo = 15

while maximo > 0:
    num = int(input("ingrese un numero negativo: "))
    if (num < 0):
        numeros.append(num * -1)
        maximo = maximo - 1
    else:
        print("no es un numero negativo")

print(f"lista de numeros: {numeros} ")