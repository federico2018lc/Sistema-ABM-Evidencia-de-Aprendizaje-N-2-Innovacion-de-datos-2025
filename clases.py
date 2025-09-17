import sqlite3 
#creamos la clase Contactos, con métodos que interactuan(DML) con la base de datos "agenda2025.db"
class Contactos:
    #creamos el objeto contacto con el metodo __init__ 
    def __init__(self, DNI, nombre, apellido, telefono, mail):
        self.DNI = DNI
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.mail = mail

    def __str__(self):
        return f"{self.DNI}, {self.nombre},{self.apellido}, {self.telefono}, {self.mail}"

#Conexión con MySQL (método)
    def conectar_db(self):
        self.conector = sqlite3.connect("agenda2025.db") # Crea o usa base de datos
        self.cursor = self.conector.cursor()

#Cerrar conexion (método)
    def cerrar_conexion(self):
        if self.cursor:
            self.cursor.close()
        if self.conector:
            self.conector.close()
#Agregar contacto (método)
    def agregar_contacto(self):
        self.conectar_db()
        sql = "INSERT INTO contactos (DNI, nombre, apellido, telefono, mail) VALUES (?,?,?,?,?)"
        valores = (self.DNI, self.nombre, self.apellido, self.telefono, self.mail)
        self.cursor.execute(sql, valores)
        self.conector.commit()
        print("Contacto agregado con éxito.")
        self.cerrar_conexion()
#para agregar: 
#Crear objeto persona:  persona1 = Contactos("1", "fede", "Lopez", "3512345678", "fede@example.com")
#Guardar en la base: persona1.agregar_contacto()

#Método para mostrar los contactos guardados en la tabla Contactos
#utilizacmos un método estático, ya que no necesitamos un objeto en particular para ver toda la lista. 
    @staticmethod
    def mostrar_contactos():
        conector = sqlite3.connect("agenda2025.db") # Crea o usa base de datos
        cursor = conector.cursor()
        cursor.execute("SELECT * FROM contactos")
        resultado = cursor.fetchall()
        cursor.close()
        conector.close()
        return resultado
#Para usar este méstodo: Contactos.mostrar_contactos()

    @staticmethod
    def seleccionar_contacto(DNI):
        conector = sqlite3.connect("agenda2025.db") # Crea o usa base de datos
        cursor = conector.cursor()
        cursor.execute("SELECT * FROM contactos WHERE DNI = ?", (DNI,))
        resultado = cursor.fetchone()
        cursor.close()
        conector.close()
        return resultado
#Para usar este méstodo: Contactos.seleccionar_contactos()  

# Método de modificación   
    def modificar_contacto(self):
        self.conectar_db()
        sql = """
        UPDATE contactos
        SET nombre = ?, apellido = ?, telefono = ?, mail = ?
        WHERE DNI = ? 
        """
        valores = (self.nombre, self.apellido, self.telefono, self.mail, self.DNI)
        self.cursor.execute(sql, valores)
        self.conector.commit()
        print("Contacto mofidicado con éxito.")
        self.cerrar_conexion()       
#para usar método:
#persona = Contactos("1", "Fede", "Lopez", "3512345678", "ag@example.com")
#persona.modificar_contacto()

#Método para guardar los datos previos a una modificación.
    @staticmethod
    def guardar_datos_previos(DNI):
        conector = sqlite3.connect("agenda2025.db") # usa base de datos
        cursor = conector.cursor()
        sql = "INSERT INTO datos_previos (DNI, nombre, apellido, telefono, mail) VALUES (?,?,?,?,?)"
        resultado = Contactos.seleccionar_contacto(DNI)
        cursor.execute(sql,resultado)
        conector.commit()
        cursor.close()
        conector.close()

#Método eliminar contactos, (elimina y a la vez guarda ese contacto eliminado en la tabla eliminados como si fuese un backup)
    @staticmethod
    def eliminar_contactos(DNI):
        conector = sqlite3.connect("agenda2025.db") # Crea o usa base de datos
        cursor = conector.cursor()
        sql = "INSERT INTO eliminados (DNI, nombre, apellido, telefono, mail) VALUES (?,?,?,?,?)"
        resultado = Contactos.seleccionar_contacto(DNI)
        cursor.execute(sql,resultado)
        sql = "DELETE FROM contactos WHERE DNI = ?"
        cursor.execute(sql, (DNI,))
        conector.commit()
        print(f"Contacto con DNI {DNI} eliminado.")
        cursor.close()
        conector.close()
#Para usar este método: 
# Elegir el DNI que se quiere borrar y 
#Contactos.eliminar_contactos(2)  agregar el DNI 
#Contactos.mostrar_contactos() Ver como quedo la lista

            
