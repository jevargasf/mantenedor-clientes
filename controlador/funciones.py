from clases.gestion.cliente import Cliente
from clases.gestion.sucursal import Sucursal
from clases.gestion.cliente_sucursal import ClienteSucursal
from clases.auth.usuario import Usuario
from bbdd.DAO import DAO
from datetime import date
import controlador.validaRut as validaRut
import controlador.validadores as validadores
import controlador.consola as consola
import controlador.api as api
from beautifultable import BeautifulTable
from clases.auth import fernet

class Funciones():
    cliente = Cliente()
    sucursal = Sucursal()
    cliente_sucursal = ClienteSucursal()
    usuario = Usuario()
    d = DAO()

    def __init__(self):
        pass

# Navegación
    def menuInicio(self):
        op = validadores.validaInt("Ingrese una opción:\n1. Iniciar Sesión\n2. Salir\n", 1, 2, "Error: Ingrese un valor numérico.", "Error de rango: Ingrese una de las opciones válidas.")

        if op == 1:
            self.iniciarSesion()
        elif op == 2:
            self.salir()
        
    def menuAdmin(self):
        print(f"Bienvenido. Perfil: {self.usuario.perfil.getNomPerfil()}\n")
        op = validadores.validaInt("¿Qué desea hacer?\n1. Administrar clientes\n2. Administrar sucursales\n3. Recuperar JSON\n4. Administrar usuarios\n5. Cerrar sesión\n", 1, 5, "Error: Ingrese una de las opciones válidas.", "Error: Ingrese un valor numérico.")

        if op == 1:
            self.menuClientes()
        elif op == 2:
            self.menuSucursales()
        elif op == 3:
            self.recuperarJson()
        elif op == 4:
            self.menuUsuarios()
        elif op == 5:
            self.cerrarSesion()

    def menuComercial(self):
        print(f"Bienvenido. Perfil: {self.usuario.perfil.getNomPerfil()}\n")
        op = validadores.validaInt("¿Qué desea hacer?\n1. Administrar asignaciones\n2. Cerrar sesión\n", 1, 2, "Error: Ingrese una de las opciones válidas.", "Error: Ingrese un valor numérico.")

        if op == 1:
            self.menuAsignaciones()
        elif op == 2:
            self.cerrarSesion()

    def menuClientes(self):
        op = validadores.validaInt("¿Qué desea hacer?\n1. Registrar cliente\n2. Ver clientes\n3. Buscar cliente\n4. Modificar cliente\n5. Eliminar cliente\n6. Volver\n", 1, 6, "Error: Ingrese una de las opciones válidas.", "Error: Ingrese una opción válida.")

        if op == 1:
            self.registrarCliente()
        elif op == 2:
            self.verClientes()
        elif op == 3:
            self.buscarCliente()
        elif op == 4:
            self.modificarCliente()
        elif op == 5:
            self.eliminarCliente()
        elif op == 6:
            self.menuAdmin()

    def menuSucursales(self):
        op = validadores.validaInt("¿Qué desea hacer?\n1. Registrar sucursal\n2. Ver sucursales\n3. Buscar sucursal\n4. Modificar sucursal\n5. Eliminar sucursal\n6. Volver\n", 1, 6, "Error: Ingrese una de las opciones válidas.", "Error: Ingrese una opción válida.")

        if op == 1:
            self.registrarSucursal()
        elif op == 2:
            self.verSucursales()
        elif op == 3:
            self.buscarSucursal()
        elif op == 4:
            self.modificarSucursal()
        elif op == 5:
            self.eliminarSucursal()
        elif op == 6:
            self.menuAdmin()
    
    def menuAsignaciones(self):
        op = validadores.validaInt("¿Qué desea hacer?\n1. Asignar cliente\n2. Ver asignaciones\n3. Modificar asignación\n4. Volver\n", 1, 4, "Error: Ingrese una de las opciones válidas.", "Error: Ingrese una opción válida.")

        if op == 1:
            self.asignarCliente()
        elif op == 2:
            self.verAsignaciones()
        elif op == 3:
            self.modificarAsignacion()
        elif op == 4:
            self.menuComercial()

    def menuUsuarios(self):
        op = validadores.validaInt("¿Qué desea hacer?\n1. Registrar usuario\n2. Ver usuarios\n3. Buscar usuario\n4. Modificar usuario\n5. Eliminar usuario\n6. Volver\n", 1, 6, "Error: Ingrese una de las opciones válidas.", "Error: Ingrese una opción válida.")

        if op == 1:
            self.registrarUsuario()
        elif op == 2:
            self.verUsuarios()
        elif op == 3:
            self.buscarUsuario()
        elif op == 4:
            self.modificarUsuario()
        elif op == 5:
            self.eliminarUsuario()
        elif op == 6:
            self.menuAdmin()
    
    def salir(self):
        pass



# Autenticación
    def iniciarSesion(self):
        # pedir nombre usuario (RUT)
        try:
            rut = input("Ingrese su RUT con puntos y guión. Ej: 11.111.111-1:\n")
            if validaRut.valida(rut) == True:
                if rut.find(".") != -1:
                    rut_sin_puntos = rut.replace(".", "")
                    rut_sin_guion = rut_sin_puntos.replace("-", "")
            else:
                print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")
                consola.pausa()
                return self.menuInicio()
        except:
                print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")
                consola.pausa()

        # pedir contraseña (enmascarar)
        contraseña = validadores.validaContraseña("Ingrese contraseña:\n", 1, 10, "Error: La contraseña debe tener entre 1 y 10 caracteres.", "Error: Por favor, ingrese una contraseña válida.")

        self.usuario.setNombreUsuario(rut_sin_guion)
        self.usuario.setContraseña(contraseña)
        respuesta = self.d.login(self.usuario)
        if respuesta is None:
            print("Error: RUT y/o la contraseña incorrectos. Intente nuevamente.\n")
            consola.pausa()
            return self.menuInicio()
        elif respuesta is not None:
            self.usuario.perfil.setNomPerfil(respuesta[3])
            if respuesta[2] == 1:
                return self.menuAdmin()
            elif respuesta[2] == 2:
                return self.menuComercial()
        else:
            print("Error: Ocurrió un error inesperado. Por favor, intente nuevamente.")
            consola.pausa()
            return self.menuInicio()

        
    def cerrarSesion(self):
        print("Cerrando sesión...\n")
        consola.pausa()
        self.menuInicio()

# Administración de usuarios
    def registrarUsuario(self):
        # ingrese rut
        try:
            rut = input("Ingrese RUT del nuevo usuario con puntos y guión. Ej: 11.111.111-1:\n")
            if validaRut.valida(rut) == True:
                if rut.find(".") != -1:
                    rut_sin_puntos = rut.replace(".", "")
                    rut_sin_guion = rut_sin_puntos.replace("-", "")
            else:
                print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")
                consola.pausa()
                return self.menuClientes()
        except:
            print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")
            consola.pausa()

        comprobar_usuario = self.d.comprobarUsuario(rut_sin_guion)
        # comprobar si ya está registrado
        if comprobar_usuario is not None:
            # comprobar si está habilitado
            if comprobar_usuario[1] == 1:
                print("Error: El RUT ingresado ya está registrado en el sistema. Por favor, intente con otro RUT.")
                consola.pausa()
                return self.menuUsuarios()
            elif comprobar_usuario[1] == 0:
                # ¿Desea reestablecer el usuario?
                pass
            else:
                print("Error: Ocurrió un error inesperado. Por favor, intente nuevamente.")
                consola.pausa()
                return self.menuUsuarios()
        elif comprobar_usuario is None:
            # continuar registrando el usuario
            # ingrese contraseña
            con = validadores.validaContraseña("Ingrese contraseña. Debe tener mínimo 8 caracteres alfanuméricos:\n", 8, 50, "Error: La contraseña debe tener entre 8 y 50 caracteres.\n", "Error: Ingrese una contraseña válida.\n")
            con_encriptada = fernet.crearContraseña(con)

            # elegir perfil 1. administrador, 2. comercial
            op = validadores.validaInt("Ingrese el tipo de perfil para este usuario:\n1. Administrador\n2. Comercial\n", 1, 2, "Error de rango: Ingrese una de las opciones válidas.", "Error: Ingrese un valor numérico.")
            self.usuario.setNombreUsuario(rut_sin_guion)
            self.usuario.setContraseña(con_encriptada)
            self.usuario.perfil.setId(op)
            # set estado = 1
            self.usuario.setEstado(1)
            # llamar consulta DAO
            self.d.agregarUsuario(self.usuario)
            consola.pausa()
            return self.menuUsuarios()
        
    def verUsuarios(self):
        pass

    def buscarUsuario(self):
        pass

    def modificarUsuario(self):
        pass

    def eliminarUsuario(self):
        pass

# Administración de clientes
    def registrarCliente(self):
        try:
            rut = input("Ingrese RUT del cliente con puntos y guión. Ej: 11.111.111-1:\n")
            if validaRut.valida(rut) == True:
                if rut.find(".") != -1:
                    rut_sin_puntos = rut.replace(".", "")
                    rut_sin_guion = rut_sin_puntos.replace("-", "")
            else:
                print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")
                consola.pausa()
                return self.menuClientes()
        except:
            print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")
            consola.pausa()

        comprobar_cliente = self.d.comprobarRutCliente(rut_sin_guion)

        if comprobar_cliente is None:
            nombre = validadores.validaString("Ingrese nombre del cliente:\n", 1, 50, "Error: El nombre debe tener entre 1 y 50 caracteres.", "Error: Por favor, ingrese un nombre válido.")
            ap_pat = validadores.validaString("Ingrese apellido paterno del cliente:\n", 1, 50, "Error: El apellido paterno debe tener entre 1 y 50 caracteres.", "Error: Por favor, ingrese un apellido paterno válido.")
            ap_mat = validadores.validaString("Ingrese apellido materno del cliente:\n", 1, 50, "Error: El apellido materno debe tener entre 1 y 50 caracteres.", "Error: Por favor, ingrese un apellido paterno válido.")
            edad = validadores.validaInt("Ingrese la edad del cliente:\n", 1, 110, "Error de rango: Ingrese una edad válida. Debe ser mayor que 0 y menor que 110.", "Error de tipo: Ingrese la edad como un número.")
            telefono = validadores.validaString("Ingrese número de teléfono del cliente. Ejemplo: 987654321\n", 9, 9, "Error: Por favor, ingrese un número de teléfono de 9 dígitos.", "Error: Por favor, ingrese un número de teléfono válido.")
            forma_pago = validadores.validaString("Ingrese forma de pago del cliente:\n1. Efectivo\n2. Débito\n3. Crédito\n", 1, 3, "Error de rango: Por favor, ingrese una de las opciones del menú.", "Error de tipo: Ingrese una opción numérica.")

            if forma_pago == "1":
                forma_pago = "Efectivo"
                
            elif forma_pago == "2":
                forma_pago = "Débito"
                
            elif forma_pago == "3":
                forma_pago = "Crédito"
                
            self.cliente.setRut(rut_sin_guion)
            self.cliente.setNombre(nombre)
            self.cliente.setApPaterno(ap_pat)
            self.cliente.setApMaterno(ap_mat)
            self.cliente.setTelefono(telefono)
            self.cliente.setEdad(edad)
            self.cliente.setFormaPago(forma_pago)
            self.cliente.setEstado(1)
            
            self.d.agregarCliente(self.cliente)
            
            consola.pausa()
            self.menuClientes()
        # si cliente ya existe: dos casos
        elif comprobar_cliente[0] == rut_sin_guion and comprobar_cliente[1] == 1:
            print("Error: El RUT ingresado ya está registrado. Por favor, intente nuevamente.\n")
            consola.pausa()
            self.menuClientes()
        # elif el rut se encuentra, pero el estado = 0, ¿desea volver a habilitarlo en la base de datos?
        elif comprobar_cliente[0] == rut_sin_guion and comprobar_cliente[1] == 0:
            op = validadores.validaInt("El RUT del cliente fue eliminado de la base de datos anteriormente. ¿Desea reestablecer el registro del cliente?\n1. Sí\n2. No\n", 1, 2, "Error: Fuera de rango. Ingrese una de las opciones disponibles.\n", "Error: Fuera de tipo. Ingrese un valor numérico.\n")
            if op == 1:
                self.cliente.setRut(rut_sin_guion)
                self.cliente.setEstado(1)
                self.d.modificarEstadoCliente(self.cliente)
                print("El registro del cliente fue reestablecido exitosamente.\n")
                consola.pausa()
                self.menuClientes()
            elif op == 2:
                print("La operación fue cancelada.\n")
                consola.pausa()
                self.menuClientes()

    def verClientes(self):
        respuesta = self.d.listarClientes()
    
        if respuesta is None or len(respuesta) == 0:
            print("No existen clientes registrados en la base de datos.\n")
        else:
            table = BeautifulTable() 
            for x, cliente in enumerate(respuesta):
                table.rows.append([x+1, cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], cliente[5], cliente[6]])
            
            table.columns.header = ["N°", "RUT", "Nombre", "Apellido Paterno", "Apellido Materno", "Edad", "Teléfono", "Forma de Pago"]
            print(table)

        consola.pausa()
        self.menuClientes()

    def buscarCliente(self):
        try:
            rut = input("Ingrese su RUT con puntos y guión. Ej: 11.111.111-1:\n")
            if validaRut.valida(rut) == True:
                if rut.find(".") != -1:
                    rut_sin_puntos = rut.replace(".", "")
                if rut.find("-") != -1:
                    rut_sin_guion = rut_sin_puntos.replace("-", "")
                respuesta = self.d.consultarCliente(rut_sin_guion)
            if respuesta is None:
                print("El cliente no está registrado en la base de datos. Intente nuevamente.\n")
            else:
                print(f"---- Datos cliente ----\n")
                print(f"RUT:{respuesta[0]}")
                print(f"Nombre: {respuesta[1]}")
                print(f"Apellido paterno: {respuesta[2]}")
                print(f"Apellido materno: {respuesta[3]}")
                print(f"Edad: {respuesta[4]}")
                print(f"Teléfono: +56{respuesta[5]}")
                print(f"Forma de pago: {respuesta[6]}\n")
        except:
                print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")

        consola.pausa()
        self.menuClientes()

    def modificarCliente(self):
        # input de rut y comprobar cliente
        try:
            rut = input("Ingrese RUT del cliente que desea modificar con puntos y guión. Ej: 11.111.111-1:\n")
            if validaRut.valida(rut) == True:
                if rut.find(".") != -1:
                    rut_sin_puntos = rut.replace(".", "")
                if rut.find("-") != -1:
                    rut_sin_guion = rut_sin_puntos.replace("-", "")
            else:
                print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")
                consola.pausa()
                return self.menuClientes()
        except:
            print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")
            consola.pausa()

        comprobar_cliente = self.d.comprobarRutCliente(rut_sin_guion)
        if comprobar_cliente is None:
            print("Error: El RUT del cliente no existe. Por favor, intente nuevamente.\n")
            consola.pausa()
            return self.menuClientes()
        elif comprobar_cliente[1] == 0:
            print("Error: El RUT del cliente fue eliminado de la base de datos. Por favor, intente nuevamente.\n")
            consola.pausa()
            return self.menuClientes()
        respuesta = self.d.consultarCliente(rut_sin_guion)

        print(f"---- Datos cliente ----\n")
        print(f"1. RUT:{respuesta[0]}")
        print(f"2. Nombre: {respuesta[1]}")
        print(f"3. Apellido paterno: {respuesta[2]}")
        print(f"4. Apellido materno: {respuesta[3]}")
        print(f"5. Edad: {respuesta[4]}")
        print(f"6. Teléfono: +56{respuesta[5]}")
        print(f"7. Forma de pago: {respuesta[6]}\n")
        op = validadores.validaInt("Ingrese la opción del campo que desea modificar:\n", 1, 7, "Error: Ingrese un valor de la lista.", "Error: Ingrese un valor numérico.")
        # ingrese campo que desea editar (lista del 1 al 6?), con valor existente
        # pedir datos cliente
        if op == 1:
            # validar nuevo rut
            try:
                nuevo_rut = input("Ingrese nuevo RUT del cliente con puntos y guión. Ej: 11.111.111-1:\n")
                if validaRut.valida(nuevo_rut) == True:
                    if nuevo_rut.find(".") != -1:
                        nuevo_rut_sin_puntos = nuevo_rut.replace(".", "")
                    if nuevo_rut.find("-") != -1:
                        nuevo_rut_sin_guion = nuevo_rut_sin_puntos.replace("-", "")
                    if self.d.comprobarRutCliente(nuevo_rut_sin_guion) is not None:
                        print("Error: El RUT ingresado ya está registrado en la base de datos. Intente nuevamente.\n")
                        consola.pausa()
                        return self.menuClientes()
                    else:
                        self.cliente.setRut(nuevo_rut_sin_guion)
                else:
                    print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")
                    consola.pausa()
                    return self.menuClientes()
            except:
                print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")
        elif op == 2:
            # validar nuevo valor
            nuevo_nom = validadores.validaString("Ingrese nuevo nombre del cliente:\n", 1, 50, "Error: El nombre debe tener entre 1 y 50 caracteres.", "Error: Por favor, ingrese un nombre válido.")
            self.cliente.setNombre(nuevo_nom)
        elif op == 3:
            nuevo_ap_pat = validadores.validaString("Ingrese nuevo apellido paterno del cliente:\n", 1, 50, "Error: El apellido paterno debe tener entre 1 y 50 caracteres.", "Error: Por favor, ingrese un apellido paterno válido.")
            self.cliente.setApPaterno(nuevo_ap_pat)
        elif op == 4:
            nuevo_ap_mat = validadores.validaString("Ingrese nuevo apellido materno del cliente:\n", 1, 50, "Error: El apellido materno debe tener entre 1 y 50 caracteres.", "Error: Por favor, ingrese un apellido paterno válido.")
            self.cliente.setApMaterno(nuevo_ap_mat)
        elif op == 5:
            nueva_edad = validadores.validaInt("Ingrese la nueva edad del cliente:\n", 1, 110, "Error de rango: Ingrese una edad válida. Debe ser mayor que 0 y menor que 110.", "Error de tipo: Ingrese la edad como un número.")
            self.cliente.setEdad(nueva_edad)
        elif op == 6:
            nuevo_telefono = validadores.validaString("Ingrese nuevo número de teléfono del cliente. Ejemplo: 987654321\n", 9, 9, "Error: Por favor, ingrese un número de teléfono de 9 dígitos.", "Error: Por favor, ingrese un número de teléfono válido.")
            self.cliente.setTelefono(nuevo_telefono)
        elif op == 7:
            nueva_forma_pago = validadores.validaString("Ingrese nueva forma de pago del cliente:\n1. Efectivo\n2. Débito\n3. Crédito\n", 1, 3, "Error de rango: Por favor, ingrese una de las opciones del menú.", "Error de tipo: Ingrese una opción numérica.")
            if nueva_forma_pago == "1":
                nueva_forma_pago = "Efectivo"
                
            elif nueva_forma_pago == "2":
                nueva_forma_pago = "Débito"
                
            elif nueva_forma_pago == "3":
                nueva_forma_pago = "Crédito"
            self.cliente.setFormaPago(nueva_forma_pago)

        # identificar id de registro en tabla clientes
        respuesta_id = self.d.consultarIdCliente(rut_sin_guion)
        id_cli = respuesta_id[0]
        self.cliente.setId(id_cli)
        # realizar modificación en la tabla
        self.d.editarCliente(op, self.cliente)
        
        consola.pausa()
        self.menuClientes()

    def eliminarCliente(self): 
        try:
            rut = input("Ingrese RUT del cliente que desea eliminar con puntos y guión. Ej: 11.111.111-1:\n")
            if validaRut.valida(rut) == True:
                if rut.find(".") != -1:
                    rut_sin_puntos = rut.replace(".", "")
                if rut.find("-") != -1:
                    rut_sin_guion = rut_sin_puntos.replace("-", "")
            else:
                print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")
                consola.pausa()
                return self.menuClientes()
        except:
            print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")

        comprobar_cliente = self.d.comprobarRutCliente(rut_sin_guion)
        if comprobar_cliente is None:
            print("Error: El RUT del cliente no existe. Por favor, intente nuevamente.")
            consola.pausa()
            return self.menuClientes()
        elif comprobar_cliente[1] == 0:
            print("Error: El RUT del cliente fue eliminado de la base de datos.\n")
            consola.pausa()
            return self.menuClientes()
        # mostrar datos cliente
        respuesta = self.d.consultarCliente(rut_sin_guion)
        print(f"---- Datos cliente ----\n")
        print(f"1. RUT:{respuesta[0]}")
        print(f"2. Nombre: {respuesta[1]}")
        print(f"3. Apellido paterno: {respuesta[2]}")
        print(f"4. Apellido materno: {respuesta[3]}")
        print(f"5. Edad: {respuesta[4]}")
        print(f"6. Teléfono: +56{respuesta[5]}")
        print(f"7. Forma de pago: {respuesta[6]}\n")
        

        # if comprobar que cliente está asignado a una sucursal, preguntar si está seguro
        consultar_id_cli = self.d.consultarIdCliente(rut_sin_guion)
        id_cli = consultar_id_cli[0]
        
        comprobar_asignacion = self.d.comprobarAsignacion(id_cli)
        if comprobar_asignacion is None or len(comprobar_asignacion) == 0:            
            op = validadores.validaInt("¿Está seguro de que desea eliminar este cliente? Esta operación no se puede deshacer. 1. Sí\n2. No\n", 1, 2, "Error: Fuera de rango. Ingrese una de las opciones disponibles.\n", "Error: Fuera de tipo. Ingrese un valor numérico.\n")
            if op == 1:
                # cambiar estado asignación también
                self.cliente.setEstado(0)
                self.cliente.setRut(rut_sin_guion)
                self.d.modificarEstadoCliente(self.cliente)
                print("La eliminación fue exitosa.\n")
            elif op == 2:
                print("La eliminación fue cancelada.\n")
        else:
            op = validadores.validaInt("El cliente está asignado a una sucursal. ¿Está seguro de que desea eliminar este cliente? Esta operación no se puede deshacer.\n1. Sí\n2. No\n", 1, 2, "Error: Fuera de rango. Ingrese una de las opciones disponibles.\n", "Error: Fuera de tipo. Ingrese un valor numérico.\n")
            if op == 1:
                self.cliente.setEstado(0)
                self.cliente.setRut(rut_sin_guion)
                self.d.modificarEstadoCliente(self.cliente)
                self.d.deshabilitarAsginacion(id_cli)
                print("La eliminación fue exitosa.\n")
            elif op == 2:
                print("La eliminación fue cancelada.\n")

        consola.pausa()
        self.menuClientes()

# Administración de sucursales
    def registrarSucursal(self):
        nom_suc = validadores.validaString("Ingrese nombre de la sucursal:\n", 1, 100, "Error: Nombre de sucursal debe tener entre 1 y 100 caracteres. Por favor, ingrese nuevamente.\n", "Error: El nombre de la sucursal no puede superar los 100 caracteres.\n")
        comprobar_sucursal = self.d.comprobarNombreSucursal(nom_suc)
        # nombre sucursal existe y estado = 1
        if comprobar_sucursal is not None:
            if comprobar_sucursal[0] == nom_suc and comprobar_sucursal[1] == 1:
                print("Error: El nombre de la sucursal ya existe. Por favor, intente nuevamente.")
                consola.pausa()
                return self.menuSucursales()
            # elif el nombre de la sucursal ya existe, pero estado = 0, ¿desea volver a habilitarla?
            elif comprobar_sucursal[0] == nom_suc and comprobar_sucursal[1] == 0:
                op = validadores.validaInt("La sucursal fue eliminada de la base de datos anteriormente. ¿Desea reestablecer el registro de la sucursal? 1. Sí\n2. No\n", 1, 2, "Error: Fuera de rango. Ingrese una de las opciones disponibles.\n", "Error: Fuera de tipo. Ingrese un valor numérico.\n")
                if op == 1:
                    # cambiar estado
                    self.sucursal.setEstado(1)
                    self.sucursal.setNombre(nom_suc)
                    self.d.modificarEstadoSucursal(self.sucursal)
                    print("El registro de sucursal fue reestablecido exitosamente.\n")
                    consola.pausa()
                    return self.menuSucursales()
                elif op == 2:
                    print("La operación fue cancelada exitosamente.\n")
                    consola.pausa()
                    return self.menuSucursales()
        else:
            dir_suc = validadores.validaString("Ingrese la dirección de la sucursal:\n", 1, 200, "Error: Dirección de la sucursal debe tener entre 1 y 200 caracteres. Por favor, ingrese nuevamente.\n", "Error: Por favor, ingrese una dirección válida.\n")
            
            while True:
                try:
                    ano_con = int(input("Ingrese el año de constitución de la sucursal:\n"))
                    mes_con = int(input("Ingrese el mes de constitución de la sucursal en formato numérico. Ejemplo: Enero es el mes 1:\n"))
                    dia_con = int(input("Ingrese el día de constitución de la sucursal en formato numérico:\n"))
                    ano_actual = date.today()
                    if ano_con > int(ano_actual.strftime("%Y")):
                        print("Error: El año no puede ser mayor a la fecha actual. Por favor, ingrese un año válido.")
                        consola.pausa()
                    elif ano_con < 1992:
                        print("Error: El año de constitución de la sucursal no puede ser menor al año de constitución de la empresa.")
                        consola.pausa()
                    elif date(ano_con, mes_con, dia_con):
                        print("Fecha válida.")
                        break
                    else:
                        print("Error: Ingrese una fecha válida.")
                except:
                    print("Error: Por favor, ingrese una fecha válida. Ejemplo: 2024-2-20.")
                    consola.pausa()

            fec_con = date(ano_con, mes_con, dia_con)
            self.sucursal.setNombre(nom_suc)
            self.sucursal.setDireccion(dir_suc)
            self.sucursal.setFechaConstitucion(fec_con)
            self.sucursal.setEstado(1)
            self.d.agregarSucursal(self.sucursal)

            self.menuSucursales()

    def verSucursales(self):
        response = self.d.listarSucursales()

        if response is None or len(response) == 0:
            print("No existen sucursales registradas en la base de datos.\n")
        else:
            table = BeautifulTable()
            table.columns.header = ["N°", "Nombre Sucursal", "Dirección", "Fecha de Constitución"]
            for x, sucursal in enumerate(response):
                table.rows.append([x+1, sucursal[0], sucursal[1], str(sucursal[2])])
            print(table)

        consola.pausa()
        self.menuSucursales()

    def buscarSucursal(self):
        nom_suc = validadores.validaString("Ingrese nombre de la sucursal:\n", 1, 100, "Error: Nombre de sucursal debe tener entre 1 y 100. Por favor, ingrese nuevamente.\n", "Error: El nombre de la sucursal no puede superar los 100 caracteres.")
        respuesta = self.d.consultarSucursal(nom_suc)

        if respuesta is None:
            print("La sucursal no existe. Intente nuevamente.\n")
        else:
            print(f"---- Datos sucursal ----\n")
            print(f"Nombre sucursal:{respuesta[0]}")
            print(f"Dirección: {respuesta[1]}")
            print(f"Fecha de constitución: {respuesta[2]}")
        
        consola.pausa()
        self.menuSucursales()

    def modificarSucursal(self):
        nom_suc = validadores.validaString("Ingrese nombre de la sucursal que desea modificar:\n", 1, 100, "Error: Nombre de sucursal debe tener entre 1 y 100. Por favor, ingrese nuevamente.\n", "Error: El nombre de la sucursal no puede superar los 100 caracteres.\n")
        # comprobar sucursal
        comprobar_sucursal = self.d.comprobarNombreSucursal(nom_suc)
        if comprobar_sucursal is not None:
            if comprobar_sucursal[0] == nom_suc and comprobar_sucursal[1] == 0:
                print("Error: La sucursal fue eliminada de la base de datos. Por favor, intente nuevamente.")
                consola.pausa()
                return self.menuSucursales()
            # elif el nombre de la sucursal ya existe, pero estado = 0, ¿desea volver a habilitarla?
            elif comprobar_sucursal[0] == nom_suc and comprobar_sucursal[1] == 1:
                respuesta = self.d.consultarSucursal(nom_suc)
                print(f"---- Datos sucursal ----\n")
                print(f"1. Nombre: {respuesta[0]}")
                print(f"2. Dirección: {respuesta[1]}")
                print(f"3. Fecha constitución: {respuesta[2]}\n")
            else:
                print("Error: El nombre de la sucursal no existe. Por favor, intente nuevamente.\n")
                consola.pausa()
                return self.menuSucursales()
        else:
            print("Error: El nombre de la sucursal no existe. Por favor, intente nuevamente.\n")
            consola.pausa()
            return self.menuSucursales()

        op = validadores.validaInt("Ingrese la opción del campo que desea modificar:\n", 1, 3, "Error: Ingrese un valor de la lista.", "Error: Ingrese un valor numérico.")
        if op == 1:
            nuevo_nom = validadores.validaString("Ingrese nuevo nombre de la sucursal:\n", 1, 100, "Error: Nombre de sucursal debe tener entre 1 y 100 caracteres. Por favor, ingrese nuevamente.\n", "Error: El nombre de la sucursal no puede superar los 100 caracteres.\n")
            self.sucursal.setNombre(nuevo_nom)
        elif op == 2:
            nueva_dir = validadores.validaString("Ingrese nueva dirección de la sucursal:\n", 1, 200, "Error: Dirección de la sucursal debe tener entre 1 y 200 caracteres. Por favor, ingrese nuevamente.\n", "Error: Por favor, ingrese una dirección válida.\n")
            self.sucursal.setDireccion(nueva_dir)
        elif op == 3:
            while True:
                try:
                    nuevo_ano = int(input("Ingrese el nuevo año de constitución de la sucursal:\n"))
                    nuevo_mes = int(input("Ingrese el nuevo mes de constitución de la sucursal en formato numérico. Ejemplo: Enero es el mes 1:\n"))
                    nuevo_dia = int(input("Ingrese el nuevo día de constitución de la sucursal en formato numérico:\n"))
                    ano_actual = date.today()
                    if nuevo_ano > int(ano_actual.strftime("%Y")):
                        print("Error: El año no puede ser mayor a la fecha actual. Por favor, ingrese un año válido.")
                        consola.pausa()
                    elif nuevo_ano < 1992:
                        print("Error: El año de constitución de la sucursal no puede ser menor al año de constitución de la empresa.")
                        consola.pausa()
                    elif date(nuevo_ano, nuevo_mes, nuevo_dia):
                        print("Fecha válida.")
                        break
                    else:
                        print("Error: Ingrese una fecha válida.")
                except:
                    print("Error: Por favor, ingrese una fecha válida. Ejemplo: 2024-2-20.")
                    consola.pausa()
            nueva_fec = date(nuevo_ano, nuevo_mes, nuevo_dia)
            self.sucursal.setFechaConstitucion(nueva_fec)
        
        respuesta_id_suc = self.d.consultarIdSucursal(nom_suc)
        id_suc = respuesta_id_suc[0]
        self.sucursal.setId(id_suc)

        self.d.editarSucursal(op, self.sucursal)
        self.menuSucursales()

    def eliminarSucursal(self):
        nom_suc = validadores.validaString("Ingrese nombre de la sucursal que desea eliminar:\n", 1, 100, "Error: Nombre de sucursal debe tener entre 1 y 100. Por favor, ingrese nuevamente.\n", "Error: El nombre de la sucursal no puede superar los 100 caracteres.\n")
        # comprobar sucursal
        comprobar_sucursal = self.d.comprobarNombreSucursal(nom_suc)
        if comprobar_sucursal is not None:
            if comprobar_sucursal[0] == nom_suc and comprobar_sucursal[1] == 0:
                print("Error: La sucursal ya fue eliminada de la base de datos. Por favor, con otra sucursal.")
                consola.pausa()
                return self.menuSucursales()
            # elif el nombre de la sucursal existe, pero estado = 1, ¿desea eliminarla?
            elif comprobar_sucursal[0] == nom_suc and comprobar_sucursal[1] == 1:
                respuesta = self.d.consultarSucursal(nom_suc)
                print(f"---- Datos sucursal ----\n")
                print(f"1. Nombre: {respuesta[0]}")
                print(f"2. Dirección: {respuesta[1]}")
                print(f"3. Fecha constitución: {respuesta[2]}\n")

                op = validadores.validaInt("¿Está seguro de que desea eliminar esta sucursal? Esta operación no se puede deshacer.\n1. Sí\n2. No\n", 1, 2, "Error: Fuera de rango. Ingrese una de las opciones disponibles.\n", "Error: Fuera de tipo. Ingrese un valor numérico.\n")
                if op == 1:
                    self.sucursal.setEstado(0)
                    self.sucursal.setNombre(nom_suc)
                    # conseguir id sucursal (antes de eliminarla)
                    id_suc = self.d.consultarIdSucursal(nom_suc)
                    self.d.modificarEstadoSucursal(self.sucursal)
                    # conseguir el id de todas las asignaciones que coinciden con esta sucursal
                    # cambiar esas asignaciones a estado = 0
                    self.d.deshabilitarAsginacionPorSucursal(id_suc)
                    print("Sucursal eliminada exitosamente.\n")
                elif op == 2:
                    print("La eliminación fue cancelada.\n")
                consola.pausa()
                return self.menuSucursales()
            else:
                print("Error: El nombre de la sucursal no existe. Por favor, intente nuevamente.\n")
                consola.pausa()
                return self.menuSucursales()
        else:
            print("Error: El nombre de la sucursal no existe. Por favor, intente nuevamente.\n")
            consola.pausa()
            return self.menuSucursales()


# Administración de asignaciones
    def asignarCliente(self):
        # ¿hay clientes para asignar? ¿hay sucursales para asignar? 
        respuesta_clientes = self.d.listarClientes()
        respuesta_sucursales = self.d.listarSucursales()
        if (respuesta_clientes is None or len(respuesta_clientes) == 0) or (respuesta_sucursales is None or len(respuesta_sucursales) == 0):
            print("No hay registros suficientes en la base de datos para realizar asignaciones\n")
            consola.pausa()
            return self.menuAsignaciones()
        else:
        # pedir rut, ¿el rut ingresado es correcto?
            try:
                rut = input("Ingrese RUT del cliente con puntos y guión. Ej: 11.111.111-1:\n")
                # el rut es válido
                if validaRut.valida(rut) == True:
                    if rut.find(".") != -1:
                        rut_sin_puntos = rut.replace(".", "")
                        rut_sin_guion = rut_sin_puntos.replace("-", "")
                # el rut no es válido, salir
                else:
                    print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")
                    consola.pausa()
                    return self.menuAsignaciones()
            # el rut no es válido, interrumpir
            except:
                print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")
                consola.pausa()
        # ¿el cliente coincide con un rut de la bbdd? (¿el cliente existe?)
        comprobar_cliente = self.d.comprobarRutCliente(rut_sin_guion)
        # dio como respuesta un rut registrado en la base de datos
        if comprobar_cliente is not None:
            # el rut existe, pero fue eliminado
            if comprobar_cliente[0] == rut_sin_guion and comprobar_cliente[1] == 0:
                print("Error: El cliente ya fue eliminado de la base de datos. Por favor, intente nuevamente.\n")
                consola.pausa()
                return self.menuAsignaciones()
            # el rut existe y está habilitado
            elif comprobar_cliente[0] == rut_sin_guion and comprobar_cliente[1] == 1:
                # Comprobar si cliente ya está asignado a sucursal
                pedir_id = self.d.consultarIdCliente(rut_sin_guion)
                id_cli = pedir_id[0]
                comprobar_asignacion = self.d.comprobarAsignacion(id_cli)
                # Sí existe una asignación para ese cliente
                if comprobar_asignacion is not None:
                    # la asignación está habilitada
                    if comprobar_asignacion[0] == 1:
                        print("Error: El cliente ya tiene una sucursal asignada. Por favor, intente nuevamente con otro cliente.\n")
                        consola.pausa()
                        return self.menuAsignaciones()
                    # Ya existe una asignación, pero estado sucursal = deshabilitado
                    elif comprobar_asignacion[0] == 0 and comprobar_asignacion[4] == 0:
                        op = validadores.validaInt(f"El cliente poseía una asignación anteriormente, pero su sucursal fue eliminada. ¿Desea asignar nueva sucursal al cliente?\n1. Sí\n2. No\n", 1, 2, "Error: Fuera de rango. Ingrese una de las opciones disponibles.\n", "Error: Fuera de tipo. Ingrese un valor numérico.\n")
                        if op == 1:
                            print("Se le solicitarán los datos para una nueva asignación")
                            consola.pausa()
                        elif op == 2:
                            print("Operación cancelada.")
                            consola.pausa()
                            return self.menuAsignaciones()
                    # Ya existe una asignación, pero fue eliminada y la sucursal sigue habilitada
                    elif comprobar_asignacion[0] == 0 and comprobar_asignacion[4] == 1:
                        op = validadores.validaInt(f"El cliente poseía una asginación anteriormente en {comprobar_asignacion[4]}. ¿Desea reestablecerla?\n1. Sí\n2. No\n", 1, 2, "Error: Fuera de rango. Ingrese una de las opciones disponibles.\n", "Error: Fuera de tipo. Ingrese un valor numérico.\n")
                        if op == 1:
                            id_cli = comprobar_asignacion[1]
                            self.d.reestablecerAsginacion(id_cli)
                            consola.pausa()
                            return self.menuAsignaciones()
                        elif op == 2:
                            print("Operación cancelada.")
                            consola.pausa()
                            return self.menuAsignaciones()
                # la respuesta de consultar asignación es None (no hay asignaciones para ese rut)
                else:
                    print("Se le solicitarán los datos para una crear asignación")
                    consola.pausa()
        # el rut ingresado es válido, pero no coincide con ningún registro de la bbdd
        else:
            print("Error: El RUT ingresado no está registrado en la base de datos. Por favor, intente nuevamente.\n")
            consola.pausa()
            return self.menuAsignaciones()

        # ¿el nombre de sucursal ingresado es válido?
        nom_suc = validadores.validaString("Ingrese nombre de la sucursal que desea asignar:\n", 1, 100, "Error: Nombre de sucursal debe tener entre 1 y 100. Por favor, ingrese nuevamente.\n", "Error: El nombre de la sucursal no puede superar los 100 caracteres.")
        # ¿la sucursal ingresada existe?
        comprobar_sucursal = self.d.comprobarNombreSucursal(nom_suc)
        if comprobar_sucursal is None:
            print("Error: El nombre de la sucursal no existe. Por favor, intente nuevamente.")
            consola.pausa()
            return self.menuAsignaciones()
        elif comprobar_sucursal is not None:
            # el nuevo nombre de sucursal es una sucursal que ya existía, pero fue eliminada
            if comprobar_sucursal[1] == 0:
                print("Error: Esta sucursal ya fue eliminada de la base de datos. Por favor, intente nuevamente.\n")
                consola.pausa()
                return self.menuAsignaciones()
            else:
                # Buscar id cliente por rut
                respuesta_cli = self.d.consultarIdCliente(rut_sin_guion)
                id_cli = respuesta_cli[0]
                # Buscar id sucursal por nombre
                respuesta_suc = self.d.consultarIdSucursal(nom_suc)
                id_suc = respuesta_suc[0]

                # Crear asignación 
                self.cliente_sucursal.cliente.setId(id_cli)
                self.cliente_sucursal.sucursal.setId(id_suc)
                self.cliente_sucursal.setEstadoAsignacion(1)
                self.d.asignarCliente(self.cliente_sucursal)
                return self.menuAsignaciones()
        else:
            print("Error: Ocurrió un error inesperado. Por favor, intente nuevamente.\n")
            consola.pausa()
            return self.menuAsignaciones()

    def verAsignaciones(self):
        response = self.d.listarAsignaciones()

        if response is None or len(response) == 0:
            print("No hay clientes asginados a sucursales actualmente.\n")
        else:
            table = BeautifulTable()
            table.columns.header = ["N°", "Nombre Cliente", "Sucursal"]
            for x, asignaciones in enumerate(response):
                table.rows.append([x+1, asignaciones[0], asignaciones[1]])
            print(table)
            
        consola.pausa()
        self.menuAsignaciones()

    def modificarAsignacion(self):
        # ¿existen asignaciones para modificar?
        response = self.d.listarAsignaciones()
        if response is None or len(response) == 0:
            print("No hay asginaciones registradas en la base de datos.\n")
            consola.pausa()
            return self.menuAsignaciones()
        else:
        # sí hay asignaciones para modificar
        # pedir rut, ¿el rut ingresado es correcto?
            try:
                rut = input("Ingrese RUT del cliente que desea modificar con puntos y guión. Ej: 11.111.111-1:\n")
                # el rut es válido
                if validaRut.valida(rut) == True:
                    if rut.find(".") != -1:
                        rut_sin_puntos = rut.replace(".", "")
                        rut_sin_guion = rut_sin_puntos.replace("-", "")
                # el rut no es válido, salir
                else:
                    print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")
                    consola.pausa()
                    return self.menuAsignaciones()
            # el rut no es válido, interrumpir
            except:
                print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")
                consola.pausa()

            # ¿el cliente ingresado existe?
            comprobar_cliente = self.d.comprobarRutCliente(rut_sin_guion)
            if comprobar_cliente is not None:
                # el rut existe, pero fue eliminado
                if comprobar_cliente[0] == rut_sin_guion and comprobar_cliente[1] == 0:
                    print("Error: El cliente ya fue eliminado de la base de datos. Por favor, intente nuevamente.\n")
                    consola.pausa()
                    return self.menuAsignaciones()
                # el rut existe y está habilitado
                elif comprobar_cliente[0] == rut_sin_guion and comprobar_cliente[1] == 1:
                    # Comprobar si cliente tiene asignación
                    pedir_id = self.d.consultarIdCliente(rut_sin_guion)
                    id_cli = pedir_id[0]
                    comprobar_asignacion = self.d.comprobarAsignacion(id_cli)
                    # Sí existe una asignación para ese cliente
                    if comprobar_asignacion is not None:
                        # la asignación está habilitada
                        if comprobar_asignacion[0] == 1:
                            # Modificar asignación
                            datos_asignacion = self.d.consultarAsginacion(id_cli)
                            # mostrar asginación actual
                            print("---- Asignación actual ----\n")
                            print(f"Cliente: {datos_asignacion[0]}")
                            print(f"Sucursal: {datos_asignacion[1]}\n")

                            # pedir nombre sucursal a la que se quiere cambiar
                            # ¿el nombre de sucursal ingresado es válido?
                            nom_suc = validadores.validaString("Ingrese nombre de la nueva sucursal a la que desea asignar al cliente:\n", 1, 100, "Error: Nombre de sucursal debe tener entre 1 y 100 caracteres. Por favor, ingrese nuevamente.\n", "Error: El nombre de la sucursal no puede superar los 100 caracteres.\n")
                            # ¿la sucursal ingresada existe?
                            id_nueva_suc = self.d.consultarIdSucursal(nom_suc)
                            if id_nueva_suc is not None:

                                id_asig = self.d.consultarIdAsignacion(id_cli)

                                self.cliente_sucursal.setId(id_asig)
                                self.cliente_sucursal.cliente.setId(id_cli)
                                self.cliente_sucursal.sucursal.setId(id_nueva_suc)
                                self.d.editarAsignacion(self.cliente_sucursal)

                                return self.menuAsignaciones()
                            # ingresó nombre no existente de sucursal
                            else:
                                print("La sucursal ingresada no existe. Por favor, intente nuevamente.\n")
                                consola.pausa()
                                return self.menuAsignaciones()
                        # Ya existe una asignación, pero estado sucursal = deshabilitado
                        # esto no debería pasar porque toda sucursal deshabilitada también deshabilita su asignación
                        elif comprobar_asignacion[0] == 0 and comprobar_asignacion[5] == 0:
                            print("Error: El cliente poseía una asignación anteriormente, pero su sucursal fue eliminada. Intente creando una nueva asignación.")
                            consola.pausa()
                            return self.menuAsignaciones()
                        # Ya existe una asignación, pero fue eliminada y la sucursal sigue habilitada
                        elif comprobar_asignacion[0] == 0 and comprobar_asignacion[5] == 1:
                            op = validadores.validaInt(f"El cliente poseía una asginación anteriormente en {comprobar_asignacion[4]}. ¿Desea reestablecerla?\n1. Sí\n2. No\n", 1, 2, "Error: Fuera de rango. Ingrese una de las opciones disponibles.\n", "Error: Fuera de tipo. Ingrese un valor numérico.\n")
                            if op == 1:
                                id_cli = comprobar_asignacion[1]
                                self.d.reestablecerAsginacion(id_cli)
                                consola.pausa()
                                return self.menuAsignaciones()
                            elif op == 2:
                                print("Operación cancelada.")
                                consola.pausa()
                                return self.menuAsignaciones()
                    # la respuesta de consultar asignación es None (no hay asignaciones para ese rut)
                    else:
                        print("Error: El cliente no está asginado a una sucursal.")
                        consola.pausa()
                        return self.menuAsignaciones()
            # el rut ingresado es válido, pero no coincide con ningún registro de la bbdd
            else:
                print("Error: El RUT ingresado no está registrado en la base de datos. Por favor, intente nuevamente.\n")
                consola.pausa()
                return self.menuAsignaciones()

# JSON
    def recuperarJson(self):
        
        respuesta = api.consultar()
        for x, registro in enumerate(respuesta):
            print(f'---- Oferta N° {x+1}: {registro["titulo"]} ----\n')
            print("Detalles:\n")
            print(f' - Tipo: {registro["detalles"]["tipo"]}\n')
            print(f' - Empresa: {registro["detalles"]["empresa"]}\n')
            print(f' - Ubicación: {registro["detalles"]["ubicacion"]}\n')
            print(f' - Requisitos:')
            for requisito in registro["detalles"]["requisitos"]:
                print(f"  * {requisito}")
            print(f'\n - Descripción: {registro["detalles"]["descripcion"]}\n')
            print(f' - Formación adicional:')
            for formacion in registro["detalles"]["formacion_adicional"]:
                print(f"  * {formacion}")
            print("\n")


        consola.pausa()
        self.menuAdmin()