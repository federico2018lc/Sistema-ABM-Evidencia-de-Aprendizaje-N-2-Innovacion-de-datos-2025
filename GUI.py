import clases
import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
root = tk.Tk()
root.title("ABM Contactos")
root.geometry("300x250")  # un poco más alto para que quepan los botones
# === TÍTULO PRINCIPAL ===
titulo = tk.Label(root, text="Sistema ABM de Contactos",
                  font=("Segoe UI", 14, "bold"),  # fuente estilo VS Code
                  bg="#1E90FF",  # celeste (puedes probar también "#007ACC" que es el azul de VS Code)
                  fg="white",    # letras blancas
                  padx=10, pady=10)
titulo.pack(fill="x")  # que ocupe todo el ancho
# Funciones de ejemplo
def agregar():
    # Crear ventana secundaria
    ventana_agregar = tk.Toplevel(root)
    ventana_agregar.title("Agregar Contacto")
    ventana_agregar.geometry("350x250")

    # Etiquetas y campos de entrada
    tk.Label(ventana_agregar, text="DNI:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_dni = tk.Entry(ventana_agregar)
    entry_dni.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(ventana_agregar, text="Nombre:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_nombre = tk.Entry(ventana_agregar)
    entry_nombre.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana_agregar, text="Apellido:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_apellido = tk.Entry(ventana_agregar)
    entry_apellido.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(ventana_agregar, text="Teléfono:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entry_telefono = tk.Entry(ventana_agregar)
    entry_telefono.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(ventana_agregar, text="Mail:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    entry_mail = tk.Entry(ventana_agregar)
    entry_mail.grid(row=4, column=1, padx=10, pady=5)

    # Función interna para guardar el contacto
    def guardar():
        dni = entry_dni.get()
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        telefono = entry_telefono.get()
        mail = entry_mail.get()

        # Validar que no estén vacíos
        if not (dni and nombre and apellido and telefono and mail):
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return
        contacto = clases.Contactos(dni, nombre, apellido, telefono, mail)
        contacto.agregar_contacto()  # Guarda en la base
        messagebox.showinfo("Éxito", "Contacto agregado correctamente")
        ventana_agregar.destroy()  # Cierra la ventana secundaria

    # Botón Guardar
    tk.Button(ventana_agregar, text="Guardar", command=guardar).grid(row=5, column=0, columnspan=2, pady=10)

def mostrar():
    # Crear ventana secundaria
    ventana_mostrar = tk.Toplevel(root)
    ventana_mostrar.title("Lista de Contactos")
    ventana_mostrar.geometry("700x500")

    # Obtener contactos de la clase
    contactos = clases.Contactos.mostrar_contactos()

    # Mostrar en un Text
    text_area = tk.Text(ventana_mostrar, width=90, height=30)
    text_area.pack(padx=10, pady=10)

    if contactos:
        text_area.insert(tk.END, f"{'DNI':<12}{'Nombre':<15}{'Apellido':<15}{'Teléfono':<15}{'Mail'}\n")
        text_area.insert(tk.END, "-"*70 + "\n")
        for c in contactos:
            text_area.insert(tk.END, f"{c[0]:<12}{c[1]:<15}{c[2]:<15}{c[3]:<15}{c[4]}\n")
    else:
        text_area.insert(tk.END, "No hay contactos registrados")
        
def modificar():
    # Crear ventana secundaria
    ventana_modificar = tk.Toplevel(root)
    ventana_modificar.title("Modificar contacto")
    ventana_modificar.geometry("500x300")

    # Etiquetas y campo para buscar por DNI
    tk.Label(ventana_modificar, text="DNI:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_dni = tk.Entry(ventana_modificar, width=30)
    entry_dni.grid(row=0, column=1, padx=10, pady=5)

    # Campos de edición (vacíos al inicio)
    tk.Label(ventana_modificar, text="Nombre:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_nombre = tk.Entry(ventana_modificar, width=30)
    entry_nombre.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana_modificar, text="Apellido:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_apellido = tk.Entry(ventana_modificar, width=30)
    entry_apellido.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(ventana_modificar, text="Teléfono:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entry_telefono = tk.Entry(ventana_modificar, width=30)
    entry_telefono.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(ventana_modificar, text="Mail:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    entry_mail = tk.Entry(ventana_modificar, width=30)
    entry_mail.grid(row=4, column=1, padx=10, pady=5)

    # Función para buscar el contacto por DNI y rellenar los campos
    def buscar_contacto():
        dni = entry_dni.get()
        resultado = clases.Contactos.seleccionar_contacto(dni)

        if resultado:
            #acá funcion que guarde el contacto en previo 
            clases.Contactos.guardar_datos_previos(dni)
            # Rellenar los campos con los datos actuales
            entry_nombre.delete(0, tk.END)
            entry_apellido.delete(0, tk.END)
            entry_telefono.delete(0, tk.END)
            entry_mail.delete(0, tk.END)

            entry_nombre.insert(0, resultado[1])
            entry_apellido.insert(0, resultado[2])
            entry_telefono.insert(0, resultado[3])
            entry_mail.insert(0, resultado[4])
        else:
            messagebox.showwarning("Error", "No se encontró el contacto")

    # Función para guardar los cambios
    def guardar_cambios():
        dni = entry_dni.get()
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        telefono = entry_telefono.get()
        mail = entry_mail.get()

        if not (dni and nombre and apellido and telefono and mail):
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        contacto = clases.Contactos(dni, nombre, apellido, telefono, mail)
        contacto.modificar_contacto()
        messagebox.showinfo("Éxito", "Contacto modificado correctamente")
        ventana_modificar.destroy()

    # Botones
    tk.Button(ventana_modificar, text="Buscar", command=buscar_contacto).grid(row=5, column=0, pady=10)
    tk.Button(ventana_modificar, text="Guardar cambios", command=guardar_cambios).grid(row=5, column=1, pady=10)
    
def eliminar():
    # Crear ventana secundaria
    ventana_agregar = tk.Toplevel(root)
    ventana_agregar.title("Eliminar contacto")
    ventana_agregar.geometry("350x250")

    # Etiquetas y campos de entrada
    tk.Label(ventana_agregar, text="DNI:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_dni = tk.Entry(ventana_agregar)
    entry_dni.grid(row=0, column=1, padx=10, pady=5)
    def eliminar():
        dni = entry_dni.get()
        try:
            clases.Contactos.eliminar_contactos(dni)
            messagebox.showinfo("Éxito", "Contacto eliminado correctamente")
        except:
            messagebox.showinfo("Error", "DNI no encontrado.\nConsulte lista de contactos en Mostrar ")
        ventana_agregar.destroy()  # Cierra la ventana secundaria  
    # Botón eliminar
    tk.Button(ventana_agregar, text="Eliminar", command=eliminar).grid(row=5, column=0, columnspan=2, pady=10)

def salir():
    root.destroy()  # cierra la ventana

# Crear botones
btn_agregar = tk.Button(root, text="Agregar", width=20, command=agregar)
btn_agregar.pack(pady=5)

btn_mostrar = tk.Button(root, text="Mostrar", width=20, command=mostrar)
btn_mostrar.pack(pady=5)

btn_modificar = tk.Button(root, text="Modificar", width=20, command=modificar)
btn_modificar.pack(pady=5)

btn_eliminar = tk.Button(root, text="Eliminar", width=20, command=eliminar)
btn_eliminar.pack(pady=5)

btn_salir = tk.Button(root, text="Salir", width=20, command=salir)
btn_salir.pack(pady=5)

# Ejecutar ventana
root.mainloop()
