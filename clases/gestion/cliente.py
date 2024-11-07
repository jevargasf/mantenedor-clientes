from clases.gestion.persona import Persona

class Cliente(Persona):
    __id = 0
    __telefono = ""
    __forma_pago = ""

    def __init__(self):
        pass
    
    def getId(self):
        return self.__id
    
    def setId(self, id: int):
        self.__id = id

    def getTelefono(self):
        return self.__telefono
    
    def setTelefono(self, tel: str):
        self.__telefono = tel

    def getFormaPago(self):
        return self.__forma_pago
    
    def setFormaPago(self, for_pag: str):
        self.__forma_pago = for_pag