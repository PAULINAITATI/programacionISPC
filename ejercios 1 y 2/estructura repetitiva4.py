#Leer 10 números y mostrar solamente los números positivos, y su sumatoria.


numeros = []
suma = 0
positivos = ""

for i in range(10):
    numeros.append(int(input("ingrese numero: ")))
    if (numeros[i] >= 0):
        suma = suma + numeros[i]
        positivos += f"{numeros[i]},"
print(f"Num + :{positivos} sum: {suma}")

