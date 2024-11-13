from clases.gestion.cliente import Cliente
from clases.gestion.sucursal import Sucursal
from clases.gestion.cliente_sucursal import ClienteSucursal
from bbdd.DAO import DAO
from os import system
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

    def pause(self):
        system("read -p 'Presione una tecla para continuar...'")

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
        op = validadores.validaInt("¿Qué desea hacer?\n1. Asignar cliente\n2. Ver asignaciones\n3. Modificar asignación\n4. Eliminar asignación\n5. Volver\n", 1, 5, "Error: Ingrese una de las opciones válidas.", "Error: Ingrese una opción válida.")

        if op == 1:
            self.asignarCliente()
        elif op == 2:
            self.verAsignaciones()
        elif op == 3:
            self.modificarAsignacion()
        elif op == 4:
            self.eliminarAsignacion()
        elif op == 5:
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
        rut = validadores.validaString("Ingrese RUT del cliente con puntos y guión. Ej: 11.111.111-1:\n", 11, 12, "Error: Por favor, ingrese RUT con puntos y guión.\n", "Error: Por favor, ingrese RUT con puntos y guión.")
        while True:
            try:
                rut = input("Ingrese RUT del cliente con puntos y guión. Ej: 11.111.111-1:\n")
                if validaRut.valida(rut) == True:
                    break
                else:
                    print("El RUT ingresado no es válido. Por favor, intente nuevamente.\n")
            except:
                print("Error: Por favor, ingrese un rut válido.\n")

        if self.d.comprobarRutCliente(rut) is not None:
            print("Error: El RUT ingresado ya está registrado. Por favor, intente nuevamente.\n")
            consola.pausa()
            self.menuClientes()

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

# Aquí estoy
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
        pass

    def eliminarCliente(self):
        pass

# Administración de sucursales
    def registrarSucursal(self):
        while True:
            try:
                nom_suc = input("Ingrese nombre de la sucursal:\n")
                if 0 > len(nom_suc):
                    print("Error: Nombre de sucursal no puede quedar vacío. Por favor, ingrese un nombre.\n")
                    self.pause()
                elif len(nom_suc) > 100:
                    print("Error: El nombre de la sucursal no puede superar los 100 caracteres.")
                    self.pause()
                else:
                    break
            except:
                print("Error: Por favor, ingrese un nombre válido.")
                self.pause()

        while True:
            try:
                dir_suc = input("Ingrese la dirección de la sucursal:\n")
                if len(dir_suc) < 0:
                    print("Error: Dirección de la sucursal no puede quedar vacía. Por favor, ingrese una dirección.\n")
                    self.pause()
                elif len(dir_suc) > 200:
                    print("Error: La dirección de la sucursal no puede superar los 200 caracteres.\n")
                    self.pause()
                else:
                    break
            except:
                print("Error: Por favor, ingrese una dirección válida.\n")
                self.pause()

        while True:
            try:
                ano_con = int(input("Ingrese el año de constitución de la sucursal:\n"))
                mes_con = int(input("Ingrese el mes de constitución de la sucursal en formato numérico. Ejemplo: Enero es el mes 1:\n"))
                dia_con = int(input("Ingrese el día de constitución de la sucursal en formato numérico:\n"))
                ano_actual = date.today()
                if ano_con > int(ano_actual.strftime("%Y")):
                    print("Error: El año no puede ser mayor a la fecha actual. Por favor, ingrese un año válido.")
                    self.pause()
                elif ano_con < 1992:
                    print("Error: El año de constitución de la sucursal no puede ser menor al año de constitución de la empresa.")
                    self.pause()
                elif date(ano_con, mes_con, dia_con):
                    print("Fecha válida.")
                    break
                else:
                    print("Error: Ingrese una fecha válida.")
            except:
                print("Error: Por favor, ingrese una fecha válida. Ejemplo: 2024-2-20.")
                self.pause()

        fec_con = date(ano_con, mes_con, dia_con)
        self.sucursal.setNombre(nom_suc)
        self.sucursal.setDireccion(dir_suc)
        self.sucursal.setFechaConstitucion(fec_con)
        self.d.agregarSucursal(self.sucursal)

    def verSucursales(self):
        response = self.d.listarSucursales()

        for x, sucursal in enumerate(response):
            print(f"---- Sucursal N° {x+1} ----\n")
            print(f"Nombre: {sucursal[0]}")
            print(f"Dirección: {sucursal[1]}")
            print(f"Fecha constitución: {sucursal[2]}\n")



    def buscarSucursal(self):
        pass

    def modificarSucursal(self):
        pass

    def eliminarSucursal(self):
        pass

# Administración de asignaciones
    def asignarCliente(self):
        while True:
            try:
                id_cli = int(input("Ingrese id del cliente que desea asignar:\n"))
                if id_cli > 0:
                    break
                else:
                    print("Error: Por favor, ingrese un id válido.")
            except:
                print("Error: Por favor, ingrese un id en formato numérico.")

        while True:
            try:
                id_suc = int(input("Ingrese id de la sucursal que desea asignar al cliente:\n"))
                if id_suc > 0:
                    break
                else:
                    print("Error: Por favor, ingrese un id válido.")
            except:
                print("Error: Por favor, ingrese un id en formato numérico.")

        self.cliente_sucursal.cliente.setId(id_cli)
        self.cliente_sucursal.sucursal.setid(id_suc)
        self.d.asignarCliente(self.cliente_sucursal)

    def verAsignaciones(self):
        response = self.d.listarAsignaciones()
        for x, asignaciones in enumerate(response):
            print(f"---- Asignación {x+1} ----\n")
            print(f"Cliente: {asignaciones[0]}")
            print(f"Sucursal: {asignaciones[1]}")

    def modificarAsignacion(self):
        pass

    def eliminarAsignacion(self):
        pass


