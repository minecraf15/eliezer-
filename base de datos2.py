import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('example.db')

# Crear una tabla
conn.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

# Insertar datos en la tabla
conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Juan', 'juan@example.com'))

# Consultar datos de la tabla
cursor = conn.execute("SELECT id, name, email FROM users")
for row in cursor:
    print(row)

# Cerrar la conexión
conn.close()
