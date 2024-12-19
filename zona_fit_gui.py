import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

from cliente import Cliente
from clienteDAO import ClienteDAO


class App(tk.Tk):
    COLOR_VENTANA = '#454545'

    def __init__(self):
        super().__init__()
        self.id_cliente = None
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.cargar_tabla()
        self.mostrar_botones()

    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(background=App.COLOR_VENTANA)
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')
        self.estilos.configure(self, background='#454545',
                               foreground='#D5C7BC',
                               fieldbackground='#785964')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)',
                             font=('Arial', 20),
                             background=App.COLOR_VENTANA,
                             foreground='#D5C7BC')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def cargar_tabla(self):
        self.frame_tabla = ttk.Frame(self)
        # Definicion de estilos de la tabla
        self.estilos.configure('Treeview', background='#785964',
                               foreground='#D5C7BC',
                               filedbackground='#785964',
                               rowheight=20)
        # Definicion de las columnas de la tabla
        columnas = ('ID', 'Nombre', 'Apellido', 'Membresia')
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show="headings")
        self.tabla.grid(row=0, column=0)
        self.frame_tabla.grid(row=1, column=1, padx=20)
        # Agregando cabeceros a la tabla
        self.tabla.heading('ID', text='ID', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresia', anchor=tk.W)
        # Definiendo las cloumnas
        self.tabla.column('ID', anchor=tk.CENTER, width=50)
        self.tabla.column('Nombre', anchor=tk.W, width=100)
        self.tabla.column('Apellido', anchor=tk.W, width=100)
        self.tabla.column('Membresia', anchor=tk.W, width=100)
        # Cargando la informacion en las columnas
        clientes = ClienteDAO.listar_clientes()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END,
                              values=(cliente.id, cliente.nombre, cliente.apellido, cliente.membresia))
        # Agregando el scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL,
                                  command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)
        # Recuperando el id cliente a traves del click de la tabla
        self.tabla.bind('<<TreeviewSelect>>', self.cargar_cliente)

        self.tabla.grid(row=0, column=0)

        self.frame_tabla.grid(row=1, column=1, padx=20)

    def mostrar_formulario(self):
        self.frame_formulario = ttk.Frame()

        nombre_label = ttk.Label(self.frame_formulario, text='Nombre: ')
        nombre_label.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
        self.nombre_entry = ttk.Entry(self.frame_formulario)
        self.nombre_entry.grid(row=0, column=1)

        apellido_label = ttk.Label(self.frame_formulario, text='Apellido: ')
        apellido_label.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)
        self.apellido_entry = ttk.Entry(self.frame_formulario)
        self.apellido_entry.grid(row=1, column=1)

        membresia_label = ttk.Label(self.frame_formulario, text='Membresia: ')
        membresia_label.grid(row=2, column=0, sticky=tk.W, pady=30, padx=5)
        self.membresia_entry = ttk.Entry(self.frame_formulario)
        self.membresia_entry.grid(row=2, column=1)

        self.frame_formulario.grid(row=1, column=0)

    def mostrar_botones(self):
        self.frame_botones = ttk.Frame()

        agregar = ttk.Button(self.frame_botones, text='Guardar', command=self.validar_cliente)
        agregar.grid(row=0, column=0, padx=30)

        eliminar = ttk.Button(self.frame_botones, text='Eliminar', command=self.eliminar_cliente)
        eliminar.grid(row=0, column=1, padx=30)

        limpiar = ttk.Button(self.frame_botones, text='Limpiar', command=self.limpiar_datos)
        limpiar.grid(row=0, column=2, padx=30)

        self.estilos.configure('TButton', background='#2B0405')
        self.estilos.map('TButton', background=[('active', '#454545')])

        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)

    def validar_cliente(self):
        # Validando los campos
        if(self.nombre_entry.get() and self.apellido_entry.get() and self.membresia_entry.get()):
            if self.validar_membresia():
                self.guardar_cliente()
            else:
                showerror(title='Error', message='El valor de la membresia tiene que ser numerico')
                self.membresia_entry.delete(0, tk.END)
                self.membresia_entry.focus_set()
        else:
            showerror(title='Error', message='Todos los campos del formulario deben de tener informacion')
            self.nombre_entry.focus_set()

    def validar_membresia(self):
        try:
            int(self.membresia_entry.get())
            return True
        except:
            return False

    def guardar_cliente(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        membresia = self.membresia_entry.get()
        # Validamos el id_cliente para saber si existe
        if self.id_cliente is None:
            cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
            ClienteDAO.insertar_cliente(cliente)
            showinfo(title='Adicion exitosa', message='Cliente insertado')
        else:
            cliente = Cliente(self.id_cliente, nombre, apellido, membresia)
            ClienteDAO.actualizar_cliente(cliente)
            showinfo(title='Actualizacion exitosa', message='Cliente actualizado exitosamente')
        self.recargar_datos()

    def eliminar_cliente(self):
        if self.id_cliente is None:
            showerror(title='Error', message='Debe seleccionarse un cliente para eliminarlo')
        else:
            cliente = Cliente(id=self.id_cliente)
            ClienteDAO.eliminar_cliente(cliente)
            showinfo(title='Eliminacion exitosa', message='Cliente eliminado correctamente')
            self.recargar_datos()

    def limpiar_datos(self):
        self.limpiar_formulario()
        self.id_cliente = None

    def recargar_datos(self):
        self.cargar_tabla()
        self.limpiar_datos()

    def limpiar_formulario(self):
        self.nombre_entry.delete(0, tk.END)
        self.apellido_entry.delete(0, tk.END)
        self.membresia_entry.delete(0, tk.END)

    def cargar_cliente(self, event):
        elemento_seleccionado = self.tabla.selection()[0]
        elemento = self.tabla.item(elemento_seleccionado)
        # Recuperando la tupla de valores del cliente seleccionado
        cliente_t = elemento['values']
        self.id_cliente = cliente_t[0]
        nombre = cliente_t[1]
        apellido = cliente_t[2]
        membresia = cliente_t[3]
        # Limpiando formulario antes de cargar la informacion
        self.limpiar_formulario()

        self.nombre_entry.insert(0, nombre)
        self.apellido_entry.insert(0, apellido)
        self.membresia_entry.insert(0, membresia)

if __name__ == '__main__':
    app = App()
    app.mainloop()
