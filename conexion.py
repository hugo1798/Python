from mysql.connector import pooling
from mysql.connector import Error
class Conexion:
    DATABASE = ''
    USERNAME = ''
    PASSWORD = ''
    DB_PORT = ''
    HOST = ''
    POOL_SIZE = 5
    POOL_NAME = ''
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD
                )
                print(f'Nombre del pool {cls.pool.pool_name}')
                print(f'Tamano del pool {cls.pool.pool_size}')
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al obtener el pool de conexiones: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        print('Liberando conexion...')
        conexion.close()
        print('Conexion liberada')

if __name__ == '__main__':
    # No es necesario mandar a llamar el pool ya que nuestro metodo de conexion manda a llamar el metodo obtener_pool
    # pool = Conexion.obtener_pool()
    # print(pool)
    conexion1 = Conexion.obtener_conexion()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
