from clases.auth.perfil import Perfil

class Usuario():
    __id = 0
    __nomUsuario = ""
    __contraseña = ""
    perfil = Perfil()
    __estado = 0

    def __init__(self):
        pass

    def getId(self):
        return self.__id

    def setId(self, id: int):
        self.__id = id

    def getNombreUsuario(self):
        return self.__nomUsuario
    
    def setNombreUsuario(self, nom: str):
        self.__nomUsuario = nom

    def getContraseña(self):
        return self.__contraseña
    
    def setContraseña(self, con: str):
        self.__contraseña = con

    def getEstado(self):
        return self.__estado
    
    def setEstado(self, est: int):
        self.__estado = est