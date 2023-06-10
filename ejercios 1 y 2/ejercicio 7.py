#Introducir los lados de un triángulo y visualizar por pantalla si dicho triángulo es equilátero, isósceles o escaleno.
print ("Ingrese los lados de su triángulo, uno a la vez y presione la tecla enter: ")
a= float (input ())
b= float (input ())
c= float (input ())
if a > 0 and b >0 and c > 0:
    if a == b and a == c:
        print ("Según los datos ingresados, el triángulo es equilátero") 
    if a != b and a != c and b != c:
        print ("Según los datos ingresados, el triángulo es escaleno")
    if (a == b and a != c) or  (a == c and a != b) or (b == c and b != a):
        print ("Según los datos ingresados, el triángulo es isóceles")
 
else:
    print ("los datos ingresados no corresponden a un triángulo")