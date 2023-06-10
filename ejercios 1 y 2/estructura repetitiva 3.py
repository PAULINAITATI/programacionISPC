#Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, cuántos mayores de edad y cuántos
#menores de edad.
edad = []
sexo = []
varones = 0
mujeres = 0
mayores = 0
menores = 0

for i in range(4):
    edad.append(int(input("ingrese edad: ")))
    sexo.append(input("ingrese sexo: f o m:  "))
    if (edad[i] < 18):
        menores = menores + 1
    else:
        mayores = mayores + 1
    if (sexo[i] == "f"):
        mujeres = mujeres + 1
    else:
        varones = varones + 1

print(f"hay {mujeres} mujeres, {varones} varones \n {mayores} son mayores y {menores} son menores ")