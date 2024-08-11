"""Página de inicio interactiva:
Componentes: Menú desplegable, Reloj simple.
Descripción: Una página de inicio con un menú desplegable para
navegar entre diferentes secciones de la página y un reloj
simple que muestra la hora actual en la esquina superior derecha."""


import tkinter as tk
from tkinter import Menu
import time
from PIL import Image, ImageTk

# Función para actualizar el reloj
def actualizar_reloj():
    hora_actual = time.strftime('%H:%M:%S')
    etiqueta_reloj.config(text=hora_actual)
    etiqueta_reloj.after(1000, actualizar_reloj)
    
# Otras funciones
def mostrar_seccion1():
    etiqueta_principal.config(text="Ingresaste a la sección 1")

def mostrar_seccion2():
    etiqueta_principal.config(text="Ingresaste a la sección 2")
    
def mostrar_seccion3():
    etiqueta_principal.config(text="Ingresaste a la sección 3")

def salir():
    root.quit()
    
# ventana principal
root = tk.Tk()
root.title("Página de Inicio Interactiva del Grupo 9")
root.geometry("900x600")
root.configure(bg="yellow")  # Color verde claro para la ventana principal
root.minsize(800,450)
root.iconbitmap("d:/TKINDER-INFO2024/grupo9/grupo_9-tk/favicon.ico")
root.resizable(False,True)

imagen_fondo = Image.open("D:/TKINDER-INFO2024/grupo9/grupo_9-tk/imagen_info.png")
imagen_fondo = imagen_fondo.resize((500, 300), Image.Resampling.LANCZOS)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

label_fondo = tk.Label(root, image=imagen_fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)


# armado del menú desplegable
menu_bar = Menu(root, bg="red", fg="brown")#no funciona color
root.config(menu=menu_bar)

menu_navegacion = Menu(menu_bar, tearoff=0, bg="lightblue", fg="black",
                       activebackground="white", activeforeground="black")
menu_bar.add_cascade(label="Navegar", menu=menu_navegacion, background="orange")  # Fondo celeste para "Navegar"
menu_navegacion.add_command(label="Sección 1", command=mostrar_seccion1)
menu_navegacion.add_command(label="Sección 2", command=mostrar_seccion2)
menu_navegacion.add_command(label="Sección 3", command=mostrar_seccion3)
menu_navegacion.add_separator()
menu_navegacion.add_command(label="Salir", command=salir)   

# Etiqueta principal
etiqueta_principal = tk.Label(root, text="INFORMATORIO 2024 - COMISION 4",
                              font=('Arial', 25), fg="black", bg="lightgrey")
etiqueta_principal.pack(pady=30)
etiqueta_principal = tk.Label(root, text="Bienvenido a la Página de Inicio del Grupo 9",
                              font=('Arial', 25), fg="black", bg="lightgrey")
etiqueta_principal.pack(pady=10)

# Crear Listbox y agregarlo a la esquina inferior derecha
listbox = tk.Listbox(root, height=9, width=20)
listbox.place(relx=1.0, rely=1.0, anchor='se', x=-20, y=-10)

# Crear título "Grupo 9" y posicionarlo un poco más a la izquierda y abajo
titulo = tk.Label(root, text="Grupo 9", font=('arial', 14))
titulo.place(relx=1.0, rely=1.0, anchor='se', x=-60, y=-180)

# Lista de nombres de los integrantes
integrantes = ["Noemi Ciscka", "Burgos Mauricio", "Esteban Ayala", "Yamila"]

# Agregar los nombres de los integrantes a la lista
for integrante in integrantes:
    listbox.insert(tk.END, integrante)
    
root.mainloop()    
