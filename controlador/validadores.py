import controlador.consola as consola

def validaSting(inst: str, min: int, max: int):
    while True:
        try:
            op = input(inst)
            if min < len(op) < max:
                return op
            else:
                print("Error: Fuera de rango.")
                consola.pausa()
        except:
            print("Error: Fuera de tipo.")
            consola.pausa()

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