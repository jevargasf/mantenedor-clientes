from clases.gestion.cliente import Cliente
from clases.gestion.sucursal import Sucursal
from clases.gestion.cliente_sucursal import ClienteSucursal
from os import system
import pymysql


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
            self.pause()
                    
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
            self.pause()
        except:
            print("Error en DAO: Error al agregar nuevo registro de cliente.\n")
            self.pause()


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
            self.pause()

    def comprobarRutCliente(self, rut):
        try:
            sql = "select rut_cli from clientes where rut_cli=%s"
            self.__conectar()
            self.cursor.execute(sql, rut)
            response = self.cursor.fetchone()
            self.__desconectar()
            return response
        except:
            print("Error en DAO: Error al consultar RUT cliente.")
            self.pause()

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
            self.pause()
        except:
            print("Error en DAO: Error al agregar nuevo registro de sucursal.\n")
            self.pause()

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
            self.pause()

    def comprobarSucursal(self):
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
        except:
            print("Error en DAO: Error al asignar cliente a sucursal.\n")
            self.pause()

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
            self.pause()
