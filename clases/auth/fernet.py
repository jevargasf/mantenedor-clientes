from cryptography.fernet import Fernet

def conectarFernet():
    clave_fernet = "xKCclFQyQmODLcReVrSPJcdlpU9JhXN5VbD58cuhckg="
    f = Fernet(clave_fernet)
    return f

def crearContraseña(con: str):
    con_fernet = conectarFernet()
    con_encript = con_fernet.encrypt(con.encode())
    return con_encript