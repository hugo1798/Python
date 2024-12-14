import sys
from clienteDAO import ClienteDAO
from cliente import Cliente

print('Zona Fit App'.center(50, '-'))

opcion = None

while opcion != 5:
    print('''
    Selecciona una opcion:
    1. Listar clientes
    2. Agregar un cliente nuevo
    3. Modificar un cliente existente
    4. Eliminar un cliente
    5. Salir
    ''')
    opcion = int(input('Escribe tu opcion: '))

    if opcion == 1:
        clientes = ClienteDAO.listar_clientes()
        print('\n Listado de clientes'.center(50))
        for cliente in clientes:
            print(cliente)
        print()
    elif opcion == 2:
        print('\n Insertando un nuevo cliente')
        nombre_var = input('Escribe el nombre del cliente: ')
        apellido_var = input('Escribe el apellido del cliente: ')
        membresia_var = input('Escribe el numero de la membresia del cliente: ')
        cliente_ins = Cliente(nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
        clientes_insertados = ClienteDAO.insertar_cliente(cliente_ins)
        print('Cliente insertado')
        print()
    elif opcion == 3:
        print('\n Actualizando un cliente')
        id_var = int(input('Escribe el id del cliente a actualizar: '))
        nombre_var = input('Escribe el nombre del cliente: ')
        apellido_var = input('Escribe el apellido del cliente: ')
        membresia_var = input('Escribe el numero de la membresia del cliente: ')
        cliente_up = Cliente(id=id_var, nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
        clientes_actualizados = ClienteDAO.actualizar_cliente(cliente_up)
        print('Cliente actualizado')
        print()
    elif opcion == 4:
        print('\n Eliminando un cliente')
        id_var = int(input('Escribe el id del cliente a eliminar: '))
        cliente_del = Cliente(id=id_var)
        clientes_eliminados = ClienteDAO.eliminar_cliente(cliente_del)
        print('Cliente eliminado')
        print()
print('Saliendo de la aplicacion...')
sys.exit()