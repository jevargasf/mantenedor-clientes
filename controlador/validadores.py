import controlador.consola as consola
import maskpass

def validaString(inst: str, min: int, max: int, err: str, exc: str):
    while True:
        try:
            op = input(inst)
            if min <= len(op) <= max:
                break
            else:
                print(err)
                consola.pausa()
        except:
            print(exc)
            consola.pausa()
    return op

def validaInt(inst: str, min: int, max: int, err: str, exc: str):
    while True:
        try:
            op = int(input(inst))
            if min <= op <= max:
                return op
            else:
                print(err)
                consola.pausa()
        except:
            print(exc)
            consola.pausa()

def validaContraseña(inst: str, min: int, max: int, err: str, exc: str):
    while True:
        try:
            op = maskpass.askpass(inst)
            if min <= len(op) <= max:
                break
            else:
                print(err)
                consola.pausa()
        except:
            print(exc)
            consola.pausa()
    return op