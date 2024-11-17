from clases.gestion.cliente import Cliente
from clases.gestion.sucursal import Sucursal
from clases.gestion.cliente_sucursal import ClienteSucursal
from bbdd.DAO import DAO
from datetime import date
import controlador.validaRut as validaRut
import controlador.validadores as validadores
import controlador.consola as consola

class Funciones():
    cliente = Cliente()
    sucursal = Sucursal()
    cliente_sucursal = ClienteSucursal()
    d = DAO()

    def __init__(self):
        pass

# Navegación
    def menuInicio(self):
        op = validadores.validaInt("Ingrese una opción:\n1. Iniciar Sesión\n2. Salir\n", 1, 2, "Error: Ingrese un valor numérico.", "Error de rango: Ingrese una de las opciones válidas.")

        if op == 1:
            self.menuPrincipal()
        elif op == 2:
            self.salir()
        
    def menuPrincipal(self):
        op = validadores.validaInt("¿Qué desea hacer?\n1. Administrar clientes\n2. Administrar sucursales\n3. Administrar asignaciones\n4. Estadísticas\n5. Cerrar sesión\n", 1, 5, "Error: Ingrese una de las opciones válidas.", "Error: Ingrese un valor numérico.")

        if op == 1:
            self.menuClientes()
        elif op == 2:
            self.menuSucursales()
        elif op == 3:
            self.menuAsignaciones()
        elif op == 4:
            self.menuEstadísticas()
        elif op == 5:
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
            self.menuPrincipal()

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
            self.menuPrincipal()
    
    def menuAsignaciones(self):
        op = validadores.validaInt("¿Qué desea hacer?\n1. Asignar cliente\n2. Ver asignaciones\n3. Modificar asignación\n4. Volver\n", 1, 4, "Error: Ingrese una de las opciones válidas.", "Error: Ingrese una opción válida.")

        if op == 1:
            self.asignarCliente()
        elif op == 2:
            self.verAsignaciones()
        elif op == 3:
            self.modificarAsignacion()
        elif op == 4:
            self.menuPrincipal()

    def menuEstadísticas(self):
        op = validadores.validaInt("¿Qué desea hacer?\n1. Opción 1\n2. Opción 2\n3. Opción 3\n4. Volver\n", 1, 4, "Error: Ingrese una de las opciones válidas.", "Error: Ingrese una opción válida.")

    def salir(self):
        pass



# Autenticación
    def iniciarSesion(self):
        pass
    
    def cerrarSesion(self):
        self.menuInicio()

# Administración de clientes
    def registrarCliente(self):
        while True:
            try:
                rut = input("Ingrese RUT del cliente con puntos y guión. Ej: 11.111.111-1:\n")
                if validaRut.valida(rut) == True:
                    break
                else:
                    print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")
            except:
                print("Error: Por favor, ingrese un rut válido.\n")
        
        if rut.find(".") != -1:
            rut_sin_puntos = rut.replace(".", "")
            rut_sin_guion = rut_sin_puntos.replace("-", "")
       
        comprobar_cliente = self.d.comprobarRutCliente(rut_sin_guion)

        # si cliente ya existe: dos casos
        if comprobar_cliente[0] == rut_sin_guion and comprobar_cliente[1] == 1:
            print("Error: El RUT ingresado ya está registrado. Por favor, intente nuevamente.\n")
            consola.pausa()
            self.menuClientes()
        # elif el rut se encuentra, pero el estado = 0, ¿desea volver a habilitarlo en la base de datos?
        elif comprobar_cliente[0] == rut_sin_guion and comprobar_cliente[1] == 0:
            op = validadores.validaInt("El RUT del cliente fue eliminado de la base de datos anteriormente. ¿Desea reestablecer el registro del cliente?\n1. Sí\n2. No\n", 1, 2, "Error: Fuera de rango. Ingrese una de las opciones disponibles.\n", "Error: Fuera de tipo. Ingrese un valor numérico.\n")
            if op == 1:
                self.cliente.setRut(rut_sin_guion)
                self.cliente.setEstado(1)
                print(self.cliente.getRut(), self.cliente.getEstado())
                self.d.modificarEstadoCliente(self.cliente)
                print("El registro del cliente fue reestablecido exitosamente.\n")
                consola.pausa()
                self.menuClientes()
            elif op == 2:
                print("La operación fue cancelada.\n")
                consola.pausa()
                self.menuClientes()
        else:
            nombre = validadores.validaString("Ingrese nombre del cliente:\n", 1, 50, "Error: El nombre debe tener entre 1 y 50 caracteres.", "Error: Por favor, ingrese un nombre válido.")
            ap_pat = validadores.validaString("Ingrese apellido paterno del cliente:\n", 1, 50, "Error: El apellido paterno debe tener entre 1 y 50 caracteres.", "Error: Por favor, ingrese un apellido paterno válido.")
            ap_mat = validadores.validaString("Ingrese apellido materno del cliente:\n", 1, 50, "Error: El apellido materno debe tener entre 1 y 50 caracteres.", "Error: Por favor, ingrese un apellido paterno válido.")
            edad = validadores.validaInt("Ingrese la edad del cliente:\n", 1, 110, "Error de rango: Ingrese una edad válida. Debe ser mayor que 0 y menor que 110.", "Error de tipo: Ingrese la edad como un número.")
            telefono = validadores.validaString("Ingrese número de teléfono del cliente. Ejemplo: 987654321\n", 9, 9, "Error: Por favor, ingrese un número de teléfono de 9 dígitos.", "Error: Por favor, ingrese un número de teléfono válido.")
            forma_pago = validadores.validaString("Ingrese forma de pago del cliente:\n1. Efectivo\n2. Débito\n3. Crédito\n", 1, 3, "Error de rango: Por favor, ingrese una de las opciones del menú.", "Error de tipo: Ingrese una opción numérica.")

            if forma_pago == 1:
                forma_pago = "Efectivo"
            elif forma_pago == 2:
                forma_pago = "Débito"
            elif forma_pago == 3:
                forma_pago = "Crédito"
        
            self.cliente.setRut(rut)
            self.cliente.setNombre(nombre)
            self.cliente.setApPaterno(ap_pat)
            self.cliente.setApMaterno(ap_mat)
            self.cliente.setTelefono(telefono)
            self.cliente.setEdad(edad)
            self.cliente.setFormaPago(forma_pago)
            self.d.agregarCliente(self.cliente)
            
            consola.pausa()
            self.menuClientes()

    def verClientes(self):
        respuesta = self.d.listarClientes()
    
        if respuesta is None or len(respuesta) == 0:
            print("No existen clientes registrados en la base de datos.\n")
        else:    
            for x, cliente in enumerate(respuesta):
                print(f"---- Cliente N° {x+1} ----\n")
                print(f"RUT:{cliente[0]}")
                print(f"Nombre: {cliente[1]}")
                print(f"Apellido paterno: {cliente[2]}")
                print(f"Apellido materno: {cliente[3]}")
                print(f"Edad: {cliente[4]}")
                print(f"Teléfono: +56{cliente[5]}")
                print(f"Forma de pago: {cliente[6]}\n")

        consola.pausa()
        self.menuClientes()

    def buscarCliente(self):
        rut = validadores.validaString("Ingrese RUT del cliente con puntos y guión. Ej: 11.111.111-1:\n", 11, 12, "Error: Por favor, ingrese RUT con puntos y guión.\n", "Error: Por favor, ingrese RUT con puntos y guión.")
        if validaRut.valida(rut) == True:
            if rut.find(".") != -1:
                rut_sin_puntos = rut.replace(".", "")
            if rut.find("-") != -1:
                rut_sin_guion = rut_sin_puntos.replace("-", "")
            respuesta = self.d.consultarCliente(rut_sin_guion)
        else:
            consola.pausa()
            print("Error: El RUT del cliente no es válido. Intente nuevamente.\n")
            self.menuClientes()

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

        consola.pausa()
        self.menuClientes()

    def modificarCliente(self):
        # input de rut y comprobar cliente
        # falta: que no se rompa el programa cuando se ingresa un rut que ya fue registrado en la bbdd pero fue deshabilitado
        rut = validadores.validaString("Ingrese RUT del cliente que desea modificar con puntos y guión. Ej: 11.111.111-1:\n", 11, 12, "Error: Por favor, ingrese RUT con puntos y guión.\n", "Error: Por favor, ingrese RUT con puntos y guión.")
        if validaRut.valida(rut) == True:
            if rut.find(".") != -1:
                rut_sin_puntos = rut.replace(".", "")
            if rut.find("-") != -1:
                rut_sin_guion = rut_sin_puntos.replace("-", "")
            comprobar_cliente = self.d.comprobarRutCliente(rut_sin_guion)
            if comprobar_cliente is None:
                print("Error: El RUT del cliente no existe. Por favor, intente nuevamente.")
                self.menuClientes()
            respuesta = self.d.consultarCliente(rut_sin_guion)
        else:
            consola.pausa()
            print("Error: El RUT del cliente no es válido. Intente nuevamente.\n")
            self.menuClientes()

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
            nuevo_rut = validadores.validaString("Ingrese nuevo RUT del cliente con puntos y guión. Ej: 11.111.111-1:\n", 11, 12, "Error: Por favor, ingrese RUT con puntos y guión.\n", "Error: Por favor, ingrese RUT con puntos y guión.")
            if validaRut.valida(nuevo_rut) == True:
                # comprueba que no está registrado en la bbdd
                nuevo_rut_sin_puntos = rut.replace(".", "")
                nuevo_rut_sin_guion = nuevo_rut_sin_puntos.replace("-","")
                if self.d.comprobarRutCliente(nuevo_rut_sin_guion) is not None:
                    print("Error: El RUT ingresado ya está registrado en la base de datos. Intente nuevamente.\n")
                    consola.pausa()
                    self.menuClientes()
                else:
                    self.cliente.setRut(nuevo_rut_sin_guion)
            else:
                print("Error: El RUT del cliente no es válido. Intente nuevamente.\n")
                consola.pausa()
                self.menuClientes()
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
            self.cliente.setFormaPago(nueva_forma_pago)
        
        # identificar id de registro en tabla clientes
        respuesta_id = self.d.consultarIdCliente(rut_sin_guion)
        id_cli = respuesta_id[0]
        self.cliente.setId(id_cli)
        # realizar modificación en la tabla
        self.d.editarCliente(op, self.cliente)
        
        # cancelar la operación en todo momento?

    def eliminarCliente(self):
        rut = validadores.validaString("Ingrese RUT del cliente que desea eliminar con puntos y guión. Ej: 11.111.111-1:\n", 11, 12, "Error: Por favor, ingrese RUT con puntos y guión.\n", "Error: Por favor, ingrese RUT con puntos y guión.")
        if validaRut.valida(rut) == True:
            if rut.find(".") != -1:
                rut_sin_puntos = rut.replace(".", "")
            if rut.find("-") != -1:
                rut_sin_guion = rut_sin_puntos.replace("-", "")
            comprobar_cliente = self.d.comprobarRutCliente(rut_sin_guion)
            if comprobar_cliente is None:
                print("Error: El RUT del cliente no existe. Por favor, intente nuevamente.")
                self.menuClientes()
        else:
            print("Error: El RUT del cliente no es válido. Intente nuevamente.\n")
            consola.pausa()
            self.menuClientes()
    
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
        if comprobar_sucursal[0] == nom_suc and comprobar_sucursal[1] == 1:
            print("Error: El nombre de la sucursal ya existe. Por favor, intente nuevamente.")
            consola.pausa()
            self.menuSucursales()
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
                self.menuSucursales()
            elif op == 2:
                print("La operación fue cancelada exitosamente.\n")
                consola.pausa()
                self.menuSucursales()
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
            self.d.agregarSucursal(self.sucursal)

            self.menuSucursales()

    def verSucursales(self):
        response = self.d.listarSucursales()

        if response is None:
            print("No existen sucursales registradas en la base de datos.\n")
        else:
            for x, sucursal in enumerate(response):
                print(f"---- Sucursal N° {x+1} ----\n")
                print(f"Nombre: {sucursal[0]}")
                print(f"Dirección: {sucursal[1]}")
                print(f"Fecha constitución: {sucursal[2]}\n")

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
        if comprobar_sucursal is None:
            print("Error: El nombre de la sucursal no existe. Por favor, intente nuevamente.\n")
            consola.pausa()
            self.menuSucursales()

        respuesta = self.d.consultarSucursal(nom_suc)
        print(f"---- Datos sucursal ----\n")
        print(f"1. Nombre: {respuesta[0]}")
        print(f"2. Dirección: {respuesta[1]}")
        print(f"3. Fecha constitución: {respuesta[2]}\n")

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
        if comprobar_sucursal is None:
            print("Error: El nombre de la sucursal no existe. Por favor, intente nuevamente.\n")
            consola.pausa()
            self.menuSucursales()

        respuesta = self.d.consultarSucursal(nom_suc)
        print(f"---- Datos sucursal ----\n")
        print(f"1. Nombre: {respuesta[0]}")
        print(f"2. Dirección: {respuesta[1]}")
        print(f"3. Fecha constitución: {respuesta[2]}\n")

        op = validadores.validaInt("¿Está seguro de que desea eliminar esta sucursal? Esta operación no se puede deshacer. 1. Sí\n2. No\n", 1, 2, "Error: Fuera de rango. Ingrese una de las opciones disponibles.\n", "Error: Fuera de tipo. Ingrese un valor numérico.\n")
        if op == 1:
            self.sucursal.setEstado(0)
            self.sucursal.setNombre(nom_suc)
            self.d.modificarEstadoSucursal(self.sucursal)
            print("Sucursal eliminada exitosamente.\n")
        elif op == 2:
            print("La eliminación fue cancelada.\n")
        consola.pausa()
        self.menuSucursales()

# Administración de asignaciones
    def asignarCliente(self):
        rut = validadores.validaString("Ingrese RUT del cliente con puntos y guión. Ej: 11.111.111-1:\n", 11, 12, "Error: Por favor, ingrese RUT con puntos y guión.\n", "Error: Por favor, ingrese RUT con puntos y guión.")
        while True:
            try:
                if validaRut.valida(rut) == True:
                    break
                else:
                    print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")
            except:
                print("Error: Por favor, ingrese un rut válido.\n")

        rut_sin_puntos = rut.replace(".", "")
        rut_sin_guion = rut_sin_puntos.replace("-","")
        if self.d.comprobarRutCliente(rut_sin_guion) is None:
            print("Error: El RUT ingresado no existe. Por favor, intente nuevamente.\n")
            consola.pausa()
            self.menuAsignaciones()

        # Comprobar si cliente ya está asignado a sucursal
        if self.d.comprobarAsignacion(id_cli) is not None:
            print("Error: El cliente ya tiene una sucursal asignada. Por favor, intente nuevamente con otro cliente.\n")
            consola.pausa()
            self.menuAsignaciones()

        nom_suc = validadores.validaString("Ingrese nombre de la sucursal:\n", 1, 100, "Error: Nombre de sucursal debe tener entre 1 y 100. Por favor, ingrese nuevamente.\n", "Error: El nombre de la sucursal no puede superar los 100 caracteres.")
        if self.d.comprobarNombreSucursal(nom_suc) is None:
            print("Error: El nombre de la sucursal no existe. Por favor, intente nuevamente.")
            consola.pausa()
            self.menuAsignaciones()

        # Buscar id cliente por rut
        respuesta_cli = self.d.consultarIdCliente(rut_sin_guion)
        id_cli = respuesta_cli[0]
        # Buscar id sucursal por nombre
        respuesta_suc = self.d.consultarIdSucursal(nom_suc)
        id_suc = respuesta_suc[0]

        # Crear asignación 
        self.cliente_sucursal.cliente.setId(id_cli)
        self.cliente_sucursal.sucursal.setid(id_suc)
        self.d.asignarCliente(self.cliente_sucursal)
        
        self.menuAsignaciones()

    def verAsignaciones(self):
        response = self.d.listarAsignaciones()

        if response is None or len(response) == 0:
            print("No hay clientes asginados a sucursales actualmente.\n")
        else:
            for x, asignaciones in enumerate(response):
                print(f"---- Asignación {x+1} ----\n")
                print(f"Cliente: {asignaciones[0]}")
                print(f"Sucursal: {asignaciones[1]}\n")

        consola.pausa()
        self.menuAsignaciones()

    def modificarAsignacion(self):
        # elegir cliente al que se quiere cambiar asignación
        rut = validadores.validaString("Ingrese RUT del cliente que desea modificar con puntos y guión. Ej: 11.111.111-1:\n", 11, 12, "Error: Por favor, ingrese RUT con puntos y guión.\n", "Error: Por favor, ingrese RUT con puntos y guión.")
        if validaRut.valida(rut) == True:
            if rut.find(".") != -1:
                rut_sin_puntos = rut.replace(".", "")
            if rut.find("-") != -1:
                rut_sin_guion = rut_sin_puntos.replace("-", "")
            comprobar_cliente = self.d.comprobarRutCliente(rut_sin_guion)
            if comprobar_cliente is None:
                print("Error: El RUT del cliente no existe. Por favor, intente nuevamente.")
                self.menuClientes()
            id_cli = self.d.consultarIdCliente(rut_sin_guion)
        else:
            consola.pausa()
            print("Error: El RUT del cliente no es válido. Intente nuevamente.\n")
            self.menuClientes()
        
        respuesta = self.d.consultarAsginacion(id_cli)
        
        # mostrar asginación actual
        print("---- Asignación actual ----\n")
        print(f"Cliente: {respuesta[0]}")
        print(f"Sucursal: {respuesta[1]}\n")

        # pedir nombre sucursal a la que se quiere cambiar
        nom_suc = validadores.validaString("Ingrese nombre de la nueva sucursal a la que desea asignar al cliente:\n", 1, 100, "Error: Nombre de sucursal debe tener entre 1 y 100 caracteres. Por favor, ingrese nuevamente.\n", "Error: El nombre de la sucursal no puede superar los 100 caracteres.\n")
        id_nueva_suc = self.d.consultarIdSucursal(nom_suc)
        id_asig = self.d.comprobarAsignacion(id_cli)

        self.cliente_sucursal.setId(id_asig)
        self.cliente_sucursal.cliente.setId(id_cli)
        self.cliente_sucursal.sucursal.setId(id_nueva_suc)
        self.d.editarAsignacion(self.cliente_sucursal)

        self.menuAsignaciones()


