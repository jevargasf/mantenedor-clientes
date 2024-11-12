# Pruebas

rut = input("Ingrese RUT del cliente sin puntos ni guión:\n")
if rut.find(".") != -1:
    rut_string = rut.replace(".", "")
    rut_lista = rut_string.split("-")
    rut_sin_digito = rut_lista[0]
    digito_verificador = rut_lista[1]

suma = 0
for x, digito in enumerate(reversed(rut_sin_digito)):
    if 7-x == 1:
        suma += int(digito)*(8-x)
    elif 7-x == 0:
        suma += int(digito)*(10-x)
    elif 7-x >= 2:
        suma += int(digito)*(x+2)

modulo_once = 11-suma%11
if modulo_once < 10:
    digito_control = str(modulo_once)
elif modulo_once == 0:
    digito_control = '0'
elif modulo_once == 10:
    digito_control = 'K'

if digito_control == digito_verificador:
    print(True)
else:
    print("Error: El RUT ingresado no es válido.")

