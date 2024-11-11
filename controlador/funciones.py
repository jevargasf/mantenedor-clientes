from clases.gestion.cliente import Cliente
from clases.gestion.sucursal import Sucursal
from clases.gestion.cliente_sucursal import ClienteSucursal
from bbdd.DAO import DAO
from os import system
from datetime import date


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
        while True:
            try:
                op = int(input("Ingrese una opción:\n1. Iniciar Sesión\n2. Salir\n"))
                if op == 1 or op == 2:
                    break
                else:
                    print("Error de rango: Ingrese una de las opciones válidas.")
                    self.pause()
            except:
                print("Error de tipo: Ingrese un valor numérico.")
                self.pause()

        if op == 1:
            self.menuPrincipal()
        elif op == 2:
            self.salir()
        
    def menuPrincipal(self):
        while True:
            try:
                op = int(input("¿Qué desea hacer?\n1. Administrar clientes\n2. Administrar sucursales\n3. Administrar asignaciones\n4. Estadísticas\n5. Cerrar sesión\n"))
                if 1 <= op <= 5:
                    break
                else:
                    print("Error: Ingrese una de las opciones válidas.")
            except:
                print("Error: Ingrese un valor numérico.")
                self.pause()

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
        while True:
            try:
                op = int(input("¿Qué desea hacer?\n1. Registrar cliente\n2. Ver clientes\n3. Buscar cliente\n4. Modificar cliente\n5. Eliminar cliente\n6. Volver\n"))
                if 1 <= op <= 6:
                    break
                else:
                    print("Error: Ingrese una de las opciones válidas.")
            except:
                print("Error: Ingrese una opción válida.")
                self.pause()

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
        while True:
            try:
                op = int(input("¿Qué desea hacer?\n1. Registrar sucursal\n2. Ver sucursales\n3. Buscar sucursal\n4. Modificar sucursal\n5. Eliminar sucursal\n6. Volver\n"))
                if 1 <= op <= 6:
                    break
                else:
                    print("Error: Ingrese una de las opciones válidas.")
            except:
                print("Error: Ingrese una opción válida.")
                self.pause()

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
        while True:
            try:
                op = int(input("¿Qué desea hacer?\n1. Asignar cliente\n2. Ver asignaciones\n3. Modificar asignación\n4. Eliminar asignación\n5. Volver\n"))
                if 1 <= op <= 5:
                    break
                else:
                    print("Error: Ingrese una de las opciones válidas.")
            except:
                print("Error: Ingrese una opción válida.")
                self.pause()

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
        while True:
            try:
                op = int(input("¿Qué desea hacer?\n1. Opción 1\n2. Opción 2\n3. Opción 3\n4. Volver\n"))
            except:
                print("Error: Ingrese una opción válida.")
                self.pause()

    def salir():
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
                rut = input("Ingrese RUT del cliente sin puntos ni guión:\n")
                if len(rut) > 9:
                    print("Error: Por favor, ingrese el RUT en el formato solicitado.")
                elif len(rut) < 8:
                    print("Error: Por favor, ingrese un RUT válido.")
                elif len(rut) == 0:
                    print("Error: El campo RUT no puede quedar vacío.")
                else:
                    break
            except:
                print("Error: Por favor, ingrese un rut válido.")

        if self.d.comprobarRutCliente(rut) is not None:
            print("Error: El RUT ingresado ya está registrado. Por favor, intente nuevamente.")
            self.pause()
            self.menuClientes()
        else:
            self.pause()
            print("El RUT del cliente es válido.")


        while True:
            try:
                nombre = input("Ingrese nombre del cliente:\n")
                if len(nombre) < 1:
                    print("Error: El campo nombre no puede quedar vacío.")
                elif len(nombre) > 50:
                    print("Error: El nombre no debe superar los 50 caracteres.")
                else:
                    break
            except:
                print("Error: Por favor, ingrese un nombre válido.")

        while True:
            try:
                ap_pat = input("Ingrese apellido paterno del cliente:\n")
                if len(ap_pat) < 1:
                    print("Error: El campo apellido paterno no puede quedar vacío.")
                elif len(ap_pat) > 50:
                    print("Error: El apellido paterno no debe superar los 50 caracteres.")
                else:
                    break
            except:  
                print("Error: Por favor, ingrese un apellido paterno válido.")

        while True:
            try:
                ap_mat = input("Ingrese apellido materno del cliente:\n")
                if len(ap_mat) < 1:
                    print("Error: El campo apellido materno no puede quedar vacío.")
                elif len(ap_mat) > 50:
                    print("Error: El apellido materno no debe superar los 50 caracteres.")
                else:
                    break
            except:  
                print("Error: Por favor, ingrese un apellido materno válido.")

        while True:
            try:
                edad = int(input("Ingrese la edad del cliente:\n"))
                if 0 < edad < 110:
                    break
                else:
                    print("Error de rango: Ingrese una edad válida. Debe ser mayor que 0 y menor que 110.")
            except:
                print("Error de tipo: Ingrese la edad como un número.")
        
        while True:
            try:
                telefono = input("Ingrese número de teléfono del cliente. Ejemplo: 987654321\n")
                if len(telefono) == 9:
                    break
                else:
                    print("Error: Por favor, ingrese un número de teléfono de 9 dígitos.")
            except:
                print("Error: Por favor, ingrese un número de teléfono válido.")

        while True:
            try:
                forma_pago = int(input("Ingrese forma de pago del cliente:\n1. Efectivo\n2. Débito\n3. Crédito\n"))
                if forma_pago == 1 or forma_pago == 2 or forma_pago == 3:
                    break
                else:
                    print("Error de rango: Por favor, ingrese una de las opciones del menú.")
            except:
                print("Error de tipo: Ingrese una opción numérica.")

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
        
        self.pause()
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

        self.pause()
        self.menuClientes()

    def buscarCliente(self):
        rut = input("Ingrese rut del cliente sin puntos ni guión Ej: 112223334: ")
        # Validar rut
        respuesta = self.d.consultarCliente(rut)
        self.pause()
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