class Usuario():
    id = 0
    nombre_usuario = ""
    contrasena = ""
    id_perfil = 0
    nombre_perfil = ""
    
    def __init__(self):
        pass
    
    def getId(self):
        return self.id
    
    def setId(self, id: int):
        self.id = id
        
    def getNombreUsuario(self):
        return self.nombre_usuario
    
    def setNombreUsuario(self, nom_usu: str):
        self.nombre_perfil = nom_usu
        
    def getContrasena(self):
        return self.contrasena
    
    def setContrasena(self, con: str):
        self.contrasena = con
    
    def getIdPerfil(self):
        return self.id_perfil
    
    def setIdPerfil(self, id_perfil: int):
        self.id_perfil = id_perfil
        
    def getNombrePerfil(self):
        return self.nombre_perfil
    
    def setNombrePerfil(self, nom_per: str):
        self.nombre_perfil = nom_per