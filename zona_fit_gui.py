import tkinter as tk
from tkinter import ttk

from clienteDAO import ClienteDAO


class App(tk.Tk):
    COLOR_VENTANA = '#454545'

    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.mostrar_tabla()

    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(background=App.COLOR_VENTANA)
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')
        self.estilos.configure(self, background='#042B0C',
                               foreground='#D5C7BC',
                               fieldbackground='#618B4A')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)',
                             font=('Arial', 20),
                             background=App.COLOR_VENTANA,
                             foreground='#D5C7BC')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_tabla(self):
        self.frame_tabla = ttk.Frame(self)
        # Definicion de estilos de la tabla
        self.estilos.configure('Treeview', background='#618B4A',
                               foreground='#454545',
                               filedbackground='#618B4A',
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
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL,
                                  command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

    def mostrar_formulario(self):
        pass

if __name__ == '__main__':
    app = App()
    app.mainloop()
