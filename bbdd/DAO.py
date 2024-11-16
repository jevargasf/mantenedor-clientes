from clases.gestion.cliente import Cliente
from clases.gestion.sucursal import Sucursal
from clases.gestion.cliente_sucursal import ClienteSucursal
from os import system
import pymysql
import controlador.consola as consola


class DAO():
    def __init__(self):
        pass
    
    def pause(self):
        system("read -p 'Presione una tecla para continuar...'")

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
        
# CRUD Clientes
    def agregarCliente(self, cli: Cliente):
        try:
            sql = "insert into clientes(rut_cli, nom_cli, ap_pat, ap_mat, eda_cli, tel_cli, pag_cli) values(%s, %s, %s, %s, %s, %s, %s)"
            valores = (cli.getRut(), cli.getNombre(), cli.getApPaterno(), cli.getApMaterno(), cli.getEdad(), cli.getTelefono(), cli.getFormaPago())
            self.__conectar()
            self.cursor.execute(sql, valores)
            self.connection.commit()
            self.__desconectar()
            print("Cliente registrado exitosamente.\n")
            consola.pausa()
        except:
            print("Error en DAO: Error al agregar nuevo registro de cliente.\n")
            consola.pausa()


    def listarClientes(self):
        try:
            sql = "select rut_cli, nom_cli, ap_pat, ap_mat, eda_cli, tel_cli, pag_cli from clientes"
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
            sql = "select rut_cli from clientes where rut_cli=%s"
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
            sql = "select rut_cli, nom_cli, ap_pat, ap_mat, eda_cli, tel_cli, pag_cli from clientes where rut_cli=%s"
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
            sql = "select id_cli from clientes where rut_cli=%s"
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
            consola.pausa()
        except:
            print("Error en DAO: Error al modificar cliente.")
            consola.pausa()

    def deshabilitarCliente(self):
        pass

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
            sql = "select nom_suc, dir_suc, fec_con from sucursales"
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
            sql = "select nom_suc from sucursales where nom_suc=%s"
            self.__conectar()
            self.cursor.execute(sql, nombre)
            response = self.cursor.fetchone()
            self.__desconectar()
            return response
        except:
            print("Error en DAO: Error al comprobar nombre sucursal.")
            consola.pausa()

    def consultarSucursal(self, nombre):
        try:
            sql = "select nom_suc, dir_suc, fec_con from sucursales where nom_suc=%s"
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
            sql = "select id_suc from sucursales where nom_suc=%s"
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

    def deshabilitarSucursal(self):
        pass

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
            sql = "select id_nub from nub where id_cli=%s"
            self.__conectar()
            self.cursor.execute(sql, id_cli)
            response = self.cursor.fetchone()
            self.__desconectar()
            return response
        except:
            print("Error en DAO: Error al consultar asignación.\n")
            consola.pausa()
            
    def listarAsignaciones(self):
        try:
            sql = "select clientes.nom_cli, sucursales.nom_suc from nub inner join clientes on nub.id_cli = clientes.id_cli inner join sucursales on nub.id_suc = sucursales.id_suc"
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
            sql = "select clientes.nom_cli, sucursales.nom_suc from nub inner join clientes on nub.id_cli = clientes.id_cli inner join sucursales on nub.id_suc = sucursales.id_suc where nub.id_cli = %s"
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
            sql = "update nub set id_cli = %s, id_suc = %s where id_nub = %s"
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
            
    def borrarAsignacion(self):
        pass