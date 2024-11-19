class Perfil():
    __id = 0
    __nomPerfil = ""
    __estado = 0

    def __init__(self):
        pass

    def getId(self):
        return self.__id

    def setId(self, id: int):
        self.__id = id

    def getNomPerfil(self):
        return self.__nomPerfil
    
    def setNomPerfil(self, nom_perfil: str):
        self.__nomPerfil = nom_perfil

    def getEstado(self):
        return self.__estado
    
    def setEstado(self, est: int):
        self.__estado = est