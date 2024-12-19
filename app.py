from flask import Flask, render_template, redirect, url_for

from cliente import Cliente
from clienteDAO import ClienteDAO
from cliente_form import ClienteForm

app = Flask(__name__)

titulo_tab = 'Zona FIT, tu gimnasio'
titulo_app = 'Zona FIT'

app.config['SECRET_KEY'] = 'llave_secreta'

@app.route('/')
def inicio():
    app.logger.debug('Path de inicio')
    # Recuperando clientes de la base de datos
    clientes_db = ClienteDAO.listar_clientes()
    cliente = Cliente()
    cliente_forma = ClienteForm(obj=cliente)
    return render_template('index.html',
                           titulo1=titulo_tab,
                           titulo2=titulo_app,
                           clientes=clientes_db,
                           forma=cliente_forma)

@app.route('/guardar', methods=['POST'])
def guardar():
    cliente = Cliente()
    cliente_forma = ClienteForm(obj=cliente)
    if cliente_forma.validate_on_submit():
        # usamos este etodo para llenar el objeto cliente con los valores del formulario
        cliente_forma.populate_obj(cliente)
        if not cliente.id:
            ClienteDAO.insertar_cliente(cliente)
        else:
            ClienteDAO.actualizar_cliente(cliente)
    return redirect(url_for('inicio'))

@app.route('/editar/<int:id>')
def editar(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    cliente_forma = ClienteForm(obj=cliente)
    clientes_db = ClienteDAO.listar_clientes()
    return redirect(url_for('index.html', titulo2=titulo_app, clientes=clientes_db, forma=cliente_forma))

@app.route('/eliminar/<int:id>')
def eliminar(id):
    cliente = Cliente(id=id)
    ClienteDAO.eliminar_cliente(cliente)
    return redirect(url_for('inicio'))

@app.route('/Limpiar')
def Limpiar():
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)
