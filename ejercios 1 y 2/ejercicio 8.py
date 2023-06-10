#Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago:
#Contado (1): se aplica un descuento del 10% al importe
#Tarjeta (2): se aplica un interés de 10%
#Débito (3): se aplica un descuento del 5%
#Mostrar el importe, el descuento o interés y el importe total.

monto= float(input("Ingrese el monto que desea abonar:  "))
opcionesdepago= (input ("Ingrese la forma de pago: contado, débito o tarjeta de credito: "))

contado= monto * 90/100
tarjeta_de_credito= monto *110/100
debito= monto *95/100

if opcionesdepago=="contado":
    print ("Su pago de contado tiene un 10% de descuento y será de: $ ",contado)
elif opcionesdepago=="tarjeta":
    print ("Su pago con tarjeta de crédito tiene un 10% de interés, el importe a abonar es de: $ ",tarjeta_de_credito)
elif opcionesdepago=="debito":
    print ("Su pago con tarjeta de débito tiene un descuento del 5%, el importe a abinar será de: ",debito)