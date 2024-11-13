# Importar librerías
from os import system
import platform

# Funciones para ejecutar comandos en terminal. 
# Ejecuta el comando según sistema operativo usando librería platform
def pausa():
    os_string = platform.platform()
    if os_string[0] == 'm' or os_string[0] == 'l':
        system("read -p 'Presione una tecla para continuar...'")
    elif os_string[0] == 'w' or os_string[0] == 'W':
        system("pause")

def borrar():
    os_string = platform.platform()
    if os_string[0] == 'm' or os_string[0] == 'l':
        system("clear")
    elif os_string[0] == 'w' or os_string[0] == 'W':
        system("cls")