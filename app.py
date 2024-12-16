from flask import Flask, render_template

from clienteDAO import ClienteDAO

app = Flask(__name__)

titulo_tab = 'Zona FIT, tu gimnasio'
titulo_app = 'Zona FIT'

@app.route('/')
def inicio():
    app.logger.debug('Path de inicio')
    # Recuperando clientes de la base de datos
    clientes_db = ClienteDAO.listar_clientes()
    print(clientes_db)
    return render_template('index.html',
                           titulo1=titulo_tab,
                           titulo2=titulo_app,
                           clientes=clientes_db)



if __name__ == '__main__':
    app.run(debug=True)
