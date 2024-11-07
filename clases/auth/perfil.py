class Perfil():
    id = 0
    nombre = ""
    
    def __init__(self):
        pass
    
    def getId(self):
        return self.id
    
    def setId(self, id: int):
        self.id = id
        
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nom: str):
        self.nombre = nom