from datetime import date

class Sucursal():
    __id = 0
    __nombre = ""
    __direccion = ""
    __fecha_constitucion = ""

    def __init__(self):
        pass

    def getId(self):
        return self.__id
    
    def setid(self, id: int):
        self.__id = id

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nom: str):
        self.__nombre = nom

    def getDireccion(self):
        return self.__direccion
    
    def setDireccion(self, dir: str):
        self.__direccion = dir

    def getFechaConstitucion(self):
        return self.__fecha_constitucion
    
    def setFechaConstitucion(self, fec_const: date):
        self.__fecha_constitucion = fec_const