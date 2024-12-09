from clases.gestion.cliente import Cliente
from clases.gestion.sucursal import Sucursal

class ClienteSucursal():
    __id = 0
    cliente = Cliente()
    sucursal = Sucursal()
    __est_asi = 0

    def __init__(self):
        pass

    def getId(self):
        return self.__id
    
    def setId(self, id: int):
        self.__id = id

    def getEstadoAsignacion(self):
        return self.__est_asi
    
    def setEstadoAsignacion(self, nuevo_estado: int):
        self.__est_asi = nuevo_estado