class Persona():

    __rut = ""
    __nombre = ""
    __ap_paterno = ""
    __ap_materno = ""
    __edad = 0

    def __init__(self):
        pass

    def getRut(self):
        return self.__rut
    
    def setRut(self, rut: str):
        self.__rut = rut

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nom: str):
        self.__nombre = nom

    def getApPaterno(self):
        return self.__ap_paterno
    
    def setApPaterno(self, ap_pat: str):
        self.__ap_paterno = ap_pat

    def getApMaterno(self):
        return self.__ap_materno
    
    def setApMaterno(self, ap_mat: str):
        self.__ap_materno = ap_mat

    def getEdad(self):
        return self.__edad
    
    def setEdad(self, edad: int):
        self.__edad = edad