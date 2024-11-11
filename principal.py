from controlador.funciones import Funciones

class Principal():
    __menu = Funciones()

    def __init__(self):        
        pass

    def ejecutarPrograma(self):
        self.__menu.menuInicio()


# Iniciar programa
inicio = Principal()
inicio.ejecutarPrograma()