PRECIO_DOLAR = 460

respuesta = input("Si desea convertir de pesos a dólar presione 1 \nSi desea convertir de dólar a pesos presione 2\n")

if (respuesta == "1"):
    pesosIngresados = float (input("Ingrese la cantidad de pesos a convertir: "))
    resultado= pesosIngresados/PRECIO_DOLAR

    print("Son, ", resultado ,"dólares")


elif (respuesta == "2"):
    dolaresIngresados = float(input("Ingrese la cantidad de dólares que desea convertir: "))
    
    resultado = dolaresIngresados*PRECIO_DOLAR

    print("Son ",dolaresIngresados*PRECIO_DOLAR," pesos")

else:
    print("Opción incorrecta")


