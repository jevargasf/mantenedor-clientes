from cryptography.fernet import Fernet

clave_fernet = Fernet.generate_key()

contraseña_admin = "inacap123"
contraseña_comercial = "inacap321"
f = Fernet(clave_fernet)
contraseña_admin_encriptada = f.encrypt(contraseña_admin.encode())
contraseña_comercial_encriptada = f.encrypt(contraseña_comercial.encode())

contraseña_admin_desencriptada = f.decrypt(contraseña_admin_encriptada)
contraseña_comercial_desencriptada = f.decrypt(contraseña_comercial_encriptada)

print(clave_fernet)
print(contraseña_admin_encriptada)
print(contraseña_comercial_encriptada)
print(contraseña_admin_desencriptada)
print(contraseña_comercial_desencriptada)