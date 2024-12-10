from cryptography.fernet import Fernet

def conectarFernet():
    clave_fernet = "xKCclFQyQmODLcReVrSPJcdlpU9JhXN5VbD58cuhckg="
    f = Fernet(clave_fernet)
    return f

# contraseña_admin = "inacap123"
# contraseña_comercial = "inacap321"

# contraseña_admin_encriptada = f.encrypt(contraseña_admin.encode())
# contraseña_comercial_encriptada = f.encrypt(contraseña_comercial.encode())

# contraseña_admin_desencriptada = f.decrypt(contraseña_admin_encriptada)
# contraseña_comercial_desencriptada = f.decrypt(contraseña_comercial_encriptada)

# print(clave_fernet)
# print(contraseña_admin_encriptada)
# print(contraseña_comercial_encriptada)
# print(contraseña_admin_desencriptada)
# print(contraseña_comercial_desencriptada)


def crearContraseña(con: str):
    con_fernet = conectarFernet()
    con_encript = con_fernet.encrypt(con.encode())
    return con_encript