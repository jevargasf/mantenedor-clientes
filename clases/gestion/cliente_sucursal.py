from clases.gestion.cliente import Cliente
from clases.gestion.sucursal import Sucursal

class ClienteSucursal():
    __id = 0
    cliente = Cliente()
    sucursal = Sucursal()

    def __init__(self):
        pass

    def getId(self):
        return self.__id
    
    def setId(self, id: int):
        self.__id = id