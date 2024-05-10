# Herramientas de flask a utilizar
from flask import Flask, render_template, request
# Gestor de base de datos a utilizar
import sqlite3

# aplicación de flask
app = Flask(__name__)

# Dirección de la base de datos, puede estar vacio el archivo.
DATABASE = 'database.db'

# Creamos una base de datos directamente
def create_table():
    # Conectar a base de datos
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS entries
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')
    conn.commit()
    conn.close()

create_table()

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Intenta hacer esto sino pasa al finally
    try:
        # Si envia el formulario por POST
        if request.method == 'POST':
            name = request.form['name']
            # Si el nombre existe insertar en la base de datos
            if name:
                cursor.execute('INSERT INTO entries (name) VALUES (?)', (name,))
                conn.commit()
    # Ejecuta esto igualmente
    finally:
        # Consigue los datos en forma de diccionario o array
        data = cursor.execute('SELECT * FROM entries').fetchall()
        conn.close()
    # abre el index.html y le pasa los datos para ser llamados
    return render_template('index.html', data=data)

# En caso de necesitar registro o inicios de sesión
# si el formulario es el mismo efectuar validación previa para no tener problemas
@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
