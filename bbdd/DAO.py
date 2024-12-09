from clases.gestion.cliente import Cliente
from clases.gestion.sucursal import Sucursal
from clases.gestion.cliente_sucursal import ClienteSucursal
from clases.auth.usuario import Usuario
import pymysql
import controlador.consola as consola
from cryptography.fernet import Fernet

class DAO():
    def __init__(self):
        pass

    def __conectar(self):
        try:
            self.connection = pymysql.connect(
                host = "localhost",
                user = "root",
                password = "",
                db = "bd_gestion"
            )
            self.cursor = self.connection.cursor()
            
            #print("Conexión a la base de datos establecida correctamente.")
            #self.pause()
        except:
            print("Error en DAO: Error en la conexión a la base de datos.")
            consola.pausa()
                    
    def __desconectar(self):
        self.connection.close()

# Login
    def login(self, usu: Usuario):
        try:
            self.__conectar()
            sql = "select usuarios.nom_usu, usuarios.con_usu, usuarios.id_per, perfiles.nom_per, usuarios.est_usu from usuarios inner join perfiles on usuarios.id_per = perfiles.id_per where usuarios.nom_usu = %s"
            print(usu.getNombreUsuario())
            self.cursor.execute(sql, usu.getNombreUsuario())
            response = self.cursor.fetchone()
            self.__desconectar()

            if response is None:
                return None
            else:
                #key = Fernet.generate_key()
                clave_fernet = "xKCclFQyQmODLcReVrSPJcdlpU9JhXN5VbD58cuhckg="
                f = Fernet(clave_fernet)
                con_ingresada = usu.getContraseña()
                
                con_encriptada = response[1]
                
                con_desencriptada = f.decrypt(con_encriptada).decode()

                if con_ingresada == con_desencriptada:
                    return response
                else:
                    return None        
        except:
            print("Error en DAO: Error al comprobar credenciales.\n")
            consola.pausa()

# CRUD Clientes
    def agregarCliente(self, cli: Cliente):
        try:
            sql = "insert into clientes(rut_cli, nom_cli, ap_pat, ap_mat, eda_cli, tel_cli, pag_cli, est_cli) values(%s, %s, %s, %s, %s, %s, %s, %s)"
            valores = (cli.getRut(), cli.getNombre(), cli.getApPaterno(), cli.getApMaterno(), cli.getEdad(), cli.getTelefono(), cli.getFormaPago(), cli.getEstado())
            print(valores)
            self.__conectar()
            self.cursor.execute(sql, valores)
            self.connection.commit()
            self.__desconectar()
            print("Cliente registrado exitosamente.\n")

        except:
            print("Error en DAO: Error al agregar nuevo registro de cliente.\n")
            consola.pausa()

    def listarClientes(self):
        try:
            sql = "select rut_cli, nom_cli, ap_pat, ap_mat, eda_cli, tel_cli, pag_cli from clientes where est_cli = 1"
            self.__conectar()
            self.cursor.execute(sql)
            response = self.cursor.fetchall()
            self.__desconectar()
            return response
        except:
            print("Error en DAO: Error al consultar registro de clientes.")
            consola.pausa()

    def comprobarRutCliente(self, rut):
        try:
            sql = "select rut_cli, est_cli from clientes where rut_cli=%s"
            self.__conectar()
            self.cursor.execute(sql, rut)
            response = self.cursor.fetchone()
            self.__desconectar()
            return response
        except:
            print("Error en DAO: Error al comprobar RUT cliente.")
            consola.pausa()

    def consultarCliente(self, rut):
        try:
            sql = "select rut_cli, nom_cli, ap_pat, ap_mat, eda_cli, tel_cli, pag_cli from clientes where rut_cli=%s and est_cli = 1"
            self.__conectar()
            self.cursor.execute(sql, rut)
            response = self.cursor.fetchone()
            self.__desconectar()
            return response
        except:
            print("Error en DAO: Error al consultar RUT cliente.")
            consola.pausa()

    def consultarIdCliente(self, rut):
        try:
            sql = "select id_cli from clientes where rut_cli=%s and est_cli = 1"
            self.__conectar()
            self.cursor.execute(sql, rut)
            response = self.cursor.fetchone()
            self.__desconectar()
            return response
        except:
            print("Error en DAO: Error al consultar id de cliente.")

    def editarCliente(self, op, cli: Cliente):
        try:
            self.__conectar()
            if op == 1:
                values = (cli.getRut(), cli.getId())
                sql = "update clientes set rut_cli=%s where id_cli=%s"
            elif op == 2:
                values = (cli.getNombre(), cli.getId())
                sql = "update clientes set nom_cli=%s where id_cli=%s"
            elif op == 3:
                values = (cli.getApPaterno(), cli.getId())
                sql = "update clientes set ap_pat=%s where id_cli=%s"
            elif op == 4:
                values = (cli.getApMaterno(), cli.getId())
                sql = "update clientes set ap_mat=%s where id_cli=%s"
            elif op == 5:
                values = (cli.getEdad(), cli.getId())
                sql = "update clientes set eda_cli=%s where id_cli=%s"
            elif op == 6:
                values = (cli.getTelefono(), cli.getId())
                sql = "update clientes set tel_cli=%s where id_cli=%s"
            elif op == 7:
                values = (cli.getFormaPago(), cli.getId())
                sql = "update clientes set pag_cli=%s where id_cli=%s"

            self.cursor.execute(sql, values)
            self.connection.commit()
            self.__desconectar()
            print("Cliente modificado exitosamente.")
        except:
            print("Error en DAO: Error al modificar cliente.")
            consola.pausa()

    def modificarEstadoCliente(self, cli: Cliente):
        try:
            sql = "update clientes set est_cli=%s where rut_cli=%s"
            values = (cli.getEstado(), cli.getRut())
            self.__conectar()
            self.cursor.execute(sql, values)
            self.connection.commit()
            self.__desconectar()
        except:
            print("Error en DAO: Error al modificar el estado del cliente.\n")
            consola.pausa()

# CRUD Sucursales
    def agregarSucursal(self, suc: Sucursal):
        try:
            sql = "insert into sucursales(nom_suc, dir_suc, fec_con) values(%s,%s,%s)"
            valores = (suc.getNombre(), suc.getDireccion(), suc.getFechaConstitucion())
            self.__conectar()
            self.cursor.execute(sql, valores)
            self.connection.commit()
            self.__desconectar()
            print("Sucursal agregada exitosamente.\n")
            consola.pausa()
        except:
            print("Error en DAO: Error al agregar nuevo registro de sucursal.\n")
            consola.pausa()

    def listarSucursales(self):
        try:
            sql = "select nom_suc, dir_suc, fec_con from sucursales where est_suc = 1"
            self.__conectar()
            self.cursor.execute(sql)
            response = self.cursor.fetchall()
            self.__desconectar()
            return response
        except:
            print("Error en DAO: Error al consultar registro de sucursales.\n")
            consola.pausa()

    def comprobarNombreSucursal(self, nombre):
        try:
            sql = "select nom_suc, est_suc from sucursales where nom_suc=%s"
            self.__conectar()
            self.cursor.execute(sql, nombre)
            response = self.cursor.fetchone()
            print(response)
            self.__desconectar()
            return response
        except:
            print("Error en DAO: Error al comprobar nombre sucursal.")
            consola.pausa()

    def consultarSucursal(self, nombre):
        try:
            sql = "select nom_suc, dir_suc, fec_con from sucursales where nom_suc=%s and est_suc = 1"
            self.__conectar()
            self.cursor.execute(sql, nombre)
            response = self.cursor.fetchone()
            self.__desconectar()
            return response
        except:
            print("Error en DAO: Error al consultar sucursal.")
            consola.pausa()

    def consultarIdSucursal(self, nombre):
        try:
            sql = "select id_suc from sucursales where nom_suc=%s and est_suc = 1"
            self.__conectar()
            self.cursor.execute(sql, nombre)
            response = self.cursor.fetchone()
            self.__desconectar()
            return response
        except:
            print("Error en DAO: Error al consultar id de sucursal.")

    def editarSucursal(self, op, suc: Sucursal):
        try:
            self.__conectar()
            if op == 1:
                values = (suc.getNombre(), suc.getId())
                sql = "update sucursales set nom_suc = %s where id_suc = %s"
            elif op == 2:
                values = (suc.getDireccion(), suc.getId())
                sql = "update sucursales set dir_suc = %s where id_suc = %s"
            elif op == 3:
                values = (suc.getFechaConstitucion(), suc.getId())
                sql = "update sucursales set fec_con = %s where id_suc = %s"
            self.cursor.execute(sql, values)
            self.connection.commit()
            self.__desconectar()
            print("Sucursal modificada exitosamente.")
            consola.pausa()
        except:
            print("Error en DAO: Error al modificar sucursal.")
            consola.pausa()

    def modificarEstadoSucursal(self, suc: Sucursal):
        try:
            sql = "update sucursales set est_suc = %s where nom_suc = %s"
            values = (suc.getEstado(), suc.getNombre())
            self.__conectar()
            self.cursor.execute(sql, values)
            self.connection.commit()
            self.__desconectar()
        except:
            print("Error en DAO: Error al eliminar sucursal.")
            consola.pausa()

# CRUD Asignaciones
    def asignarCliente(self, asig: ClienteSucursal):
        try:
            sql = "insert into nub(id_cli, id_suc) values(%s,%s)"
            valores = (asig.cliente.getId(), asig.sucursal.getId())
            self.__conectar()
            self.cursor.execute(sql, valores)
            self.connection.commit()
            self.__desconectar()
            print("Cliente asignado exitosamente.\n")
            consola.pausa()
        except:
            print("Error en DAO: Error al asignar cliente a sucursal.\n")
            consola.pausa()

    def comprobarAsignacion(self, id_cli):
        try:
            sql = "select nub.est_asi, nub.id_cli, nub.id_suc, sucursales.nom_suc, sucursales.est_suc from nub inner join sucursales on nub.id_suc = sucursales.id_suc where nub.id_cli=%s"
            self.__conectar()
            self.cursor.execute(sql, id_cli)
            response = self.cursor.fetchone()
            self.__desconectar()
            return response
        except:
            print("Error en DAO: Error al consultar asignación.\n")
            consola.pausa()

    def consultarIdAsignacion(self, id_cli):
        try:
            sql = "select id_nub from nub where id_cli=%s"
            self.__conectar()
            self.cursor.execute(sql, id_cli)
            response = self.cursor.fetchone()
            self.__desconectar()
            return response
        except:
            print("Error en DAO: Error al consultar id de asignación.\n")
            consola.pausa()
    
    def listarAsignaciones(self):
        try:
            sql = "select concat(clientes.nom_cli,' ',clientes.ap_pat), sucursales.nom_suc from nub inner join clientes on nub.id_cli = clientes.id_cli inner join sucursales on nub.id_suc = sucursales.id_suc where est_cli = 1 and est_suc = 1 and nub.est_asi = 1"
            self.__conectar()
            self.cursor.execute(sql)
            response = self.cursor.fetchall()
            self.__desconectar()
            return response
        except:
            print("Error en DAO: Error al consultar registro de asignaciones.\n")
            consola.pausa()

    def consultarAsginacion(self, id_cli):
        try:
            sql = "select concat(clientes.nom_cli,' ',clientes.ap_pat), sucursales.nom_suc from nub inner join clientes on nub.id_cli = clientes.id_cli inner join sucursales on nub.id_suc = sucursales.id_suc where nub.id_cli = %s and clientes.est_cli = 1 and sucursales.est_suc = 1 and nub.est_asi = 1"
            self.__conectar()
            self.cursor.execute(sql, id_cli)
            response = self.cursor.fetchone()
            self.__desconectar
            return response
        except:
            print("Error en DAO: Error al consultar asignación de cliente a sucursal.\n")
            consola.pausa()

    def editarAsignacion(self, asig: ClienteSucursal):
        try:
            sql = "update nub set id_cli = %s, id_suc = %s where id_nub = %s and est_asi = 1"
            values = (asig.cliente.getId(), asig.sucursal.getId(), asig.getId())
            self.__conectar()
            self.cursor.execute(sql, values)
            self.connection.commit()
            self.__desconectar()
            print("Asginación de cliente modificada exitosamente.\n")
            consola.pausa()
        except:
            print("Error en DAO: Error al modificar la asignación de cliente a sucursal.")
            consola.pausa()

    # la idea es que exista solo 1 asignación vigente en la tabla (que coincidan id_cli y estado = 1)
    def deshabilitarAsginacion(self, id_cli):
        try:
            sql = "update nub set est_asi = 0 where id_cli = %s and est_asi = 1"
            self.__conectar()
            self.cursor.execute(sql, id_cli)
            self.connection.commit()
            self.__desconectar()
            print("Asignación eliminada exitosamente.")
        except:
            print("Error en DAO: Error al eliminar la asignación de cliente a sucursal.")

    def reestablecerAsginacion(self, id_cli):
        try:
            sql = "update nub set est_asi = 1 where id_cli = %s and est_asi = 0"
            self.__conectar()
            self.cursor.execute(sql, id_cli)
            self.connection.commit()
            self.__desconectar()
            print("Asignación reestrablecida exitosamente.")
        except:
            print("Error en DAO: Error al eliminar la asignación de cliente a sucursal.")

# CRUD usuarios
    # acá las funciones de (al menos) agregar usuario