from controlador.funciones import Menu

class Principal():
    __menu = Menu()

    def __init__(self):        
        pass

    def ejecutarPrograma(self):
        self.__menu.menuInicio()


# Iniciar programa
inicio = Principal()
inicio.ejecutarPrograma()