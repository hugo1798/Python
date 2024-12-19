from conexion import Conexion
from cliente import Cliente

class ClienteDAO:

    # Sentencias SQL
    SELECCIONAR = 'SELECT * FROM cliente'
    SELECCIONAR_ID = 'SELECT * FROM cliente WHERE id=%s'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def listar_clientes(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase cliente - tabla cliente,
            # debido a que con fetchall estamos recuperando tuplas con la informacion de la tabla
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al listar los clientes: {e}')
        finally:
            if conexion is not None:
                Conexion.liberar_conexion(conexion)

    @classmethod
    def seleccionar_por_id(cls, id):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (id,)
            cursor.execute(cls.SELECCIONAR_ID, valores)
            registro = cursor.fetchone()
            cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
            return cliente
        except Exception as e:
            print(f'Excepcion al seleccionar cliente por id {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar_cliente(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar el cliente: {e}')
        finally:
            Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar_cliente(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar el cliente: {e}')
        finally:
            Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar_cliente(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id, )
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar el cliente: {e}')
        finally:
            Conexion.liberar_conexion(conexion)

if __name__ == '__main__':
    # Insertando un nuevo cliente
    # cliente1 = Cliente(nombre='Juan Carlos', apellido='Gama', membresia=102)
    # clientes_insertados = ClienteDAO.insertar_cliente(cliente1)
    # print(f'Clientes insertados: {clientes_insertados}')
    # Actualizando un cliente
    # cliente_up = Cliente(3, 'Maria Eugenia', 'Velazco', 99)
    # clientes_actualizados = ClienteDAO.actualizar_cliente(cliente_up)
    # print(f'Clientes actualizados: {clientes_actualizados}')
    # Eliminando un cliente
    # cliente_del = Cliente(id=3)
    # clientes_eliminados = ClienteDAO.eliminar_cliente(cliente_del)
    # print(f'Clientes eliminados: {clientes_eliminados}')
    # Listando los clientes
    clientes = ClienteDAO.listar_clientes()
    for cliente in clientes:
        print(cliente)
