import sqlite3
conexion=sqlite3.connect("VIp ")
curso=conexion.cursor()
curso.execute(" Create Table productos(nombre_articulo varchar(50),precio integer, seccion varchar(20))")


conexion.close()