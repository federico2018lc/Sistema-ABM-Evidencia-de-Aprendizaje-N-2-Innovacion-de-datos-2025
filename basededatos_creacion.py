
#Creación de base de datos "agenda2025.db" con sqlite3 - DDL - Data Definition Language
#Solo debe ejecutarse una vez, sino habra problemas con las primary key.

import sqlite3   #el framework sqlite3 ya viene con python, así que solo se importa.
#Crea en la carpeta un archivo "agenda2025.db" el cual se puede abrir con SQLiteStudio para realizar consultas.

#creamos una base de datos con sqlite3 (DDL-Data Definition Language)
conexion = sqlite3.connect("agenda2025.db") # Crea o usa base de datos
#Este comando crea una base de datos en la carpeta donde se encuentra el archivo.py
#con SQLiteStudio se puede acceder a la base de datos 
cursor=conexion.cursor() #establece conexión

#Creamos tabla contactos con sus atributos (DDL)
cursor.execute("""create table  if not exists contactos
                (dni integer primary key,  
                nombre varchar(50) not null, 
                apellido varchar(50) not null,
                telefono varchar(50) not null,
                mail varchar(50) not null)""") 
#como no vamosa a realizar operaciones numericas con telefono, elegimos el tipo varchat.
#primary key: dni ya que es un documento único para cada persona.

#Creamos tabla eliminados con sus atributos borrados de la bd. En caso de emergencia.
# no se accede desde la aplicacion de ventana, si no a traves de consultas sql. SELECT * FROM eliminados, 
cursor.execute("""create table  if not exists eliminados
                (id integer primary key,  
                dni varchar(50) not null,    
                nombre varchar(50) not null, 
                apellido varchar(50) not null,
                telefono varchar(50) not null,
                mail varchar(50) not null)""") 
conexion.commit() #guardamos cambios

cursor.execute("""create table  if not exists datos_previos
                (id integer primary key autoincrement,  
                dni integer not null,    
                nombre varchar(50) not null, 
                apellido varchar(50) not null,
                telefono varchar(50) not null,
                mail varchar(50) not null,
                foreign key (dni) references contactos(dni))""") 

varios_contactos=[("22443856","Mariela", "Yacci", "35124243","mariela@mail.com"), ("43601086", "Dante", "Coledas", "35412585", "dante@mail.com"),
                    ("35994586", "Federico", "Lopez", "35412575", "fede@mail.com"),("31600022", "Emanuel", "Toledo", "35434575", "ema@mail.com"),
                    ("30844042", "Marcela ", "Knecht ", "354123444", "marce@mail.com"),("45807137", "Tomas ", "Barrera ", "354123454", "tomas@mail.com"),
                    ("1", "Juan ", "Bar ", "354333454", "juan@mail.com"),("2", "Ulises", "Bueno ", "323123454", "uli@mail.com"),
                    ("3", "Mona", "Jimenez ", "223323454", "mona@mail.com"),]   
#creamos contactos con dni 1, 2 y 3 para facilitar su uso en las pruebas.

# ejecuatamos un INSERT - DML (Data Manipulation Language)
#para cargar varios_contactos (lista de tuplas)
cursor.executemany("insert into contactos ( dni, nombre, apellido, telefono, mail) values (?,?,?,?,?)", varios_contactos)
#método executemany para agregar varios contactos a la vez. 

conexion.commit() #guardamos cambios
conexion.close() #cerramos conexión

