import tkinter as tk
import random
import time

# Dibujo del ahorcado
dibujo = ['''
   +---+
   |   |
       |
       |
       |
       |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
FINISH HIM
=========''']

# Funciones

def palabra_aleatoria(lista):
    return random.choice(lista)

def ingresoLetra():
    letra = entry_letra.get().upper()
    if len(letra) == 1 and letra.isalpha():
        entry_letra.delete(0, tk.END)
        return letra
    else:
        lbl_mensaje.config(text="Ingrese una letra válida")
        return None

def letraPorLetra(palabra):
    return list(palabra)

def eliminarLetras(letra, lista):
    while letra in lista:
        lista.remove(letra)
    return lista

def letrasUsadas(letra, cadena):
    if len(cadena) == 0:
        cadena += letra
    else:
        cadena += (", " + letra)
    lbl_letras_usadas.config(text=f'Letras usadas: {cadena}')
    return cadena

def letraPorGuiones(letra, palabra, lista):
    if not lista:
        lista = ["_ " for _ in palabra]
    
    for idx, char in enumerate(palabra):
        if char == letra:
            lista[idx] = letra + " "
    
    lbl_palabra.config(text="".join(lista))
    return lista

def iniciar_partida():
    global intento, correctas, letras_acertadas, letras_usadas_str, letras_palabra, palabra_actual

    intento = 0
    correctas = 0
    letras_acertadas = []
    letras_usadas_str = ""
    lbl_mensaje.config(text="")
    
    palabra_actual = palabra_aleatoria(lista_palabras).upper()
    letras_palabra = letraPorLetra(palabra_actual)
    
    lbl_palabra.config(text=len(palabra_actual) * "_ ")
    lbl_dibujo.config(text=dibujo[intento])
    lbl_letras_usadas.config(text="Letras usadas: ")
    
def verificar_letra():
    global intento, correctas, letras_acertadas, letras_usadas_str, letras_palabra

    letra = ingresoLetra()
    if not letra:
        return
    
    if letra in letras_palabra:
        letras_acertadas = letraPorGuiones(letra, palabra_actual, letras_acertadas)
        correctas += letras_palabra.count(letra)
        letras_palabra = eliminarLetras(letra, letras_palabra)
        
        if correctas == len(palabra_actual):
            lbl_mensaje.config(text="¡Ganaste! Adivinaste la palabra.")
            return
        
    elif letra in letras_usadas_str:
        lbl_mensaje.config(text="Ya probaste con esta letra.")
    else:
        intento += 1
        lbl_dibujo.config(text=dibujo[intento])
        
        if intento == len(dibujo) - 1:
            lbl_mensaje.config(text=f"Perdiste. La palabra era: {palabra_actual}")
            return
    
    letras_usadas_str = letrasUsadas(letra, letras_usadas_str)

def jugar_de_nuevo():
    if len(lista_palabras) > 0:
        iniciar_partida()
    else:
        lbl_mensaje.config(text="No hay más palabras disponibles.")

# Interfaz gráfica

root = tk.Tk()
root.title("Ahorcado - Grupo 7")
root.config(bg ="green3")

"""# Frame principal
frame = tk.Frame(root)
frame.pack(pady=20)
frame.config(bg="grey")"""
# Frame principal
frame = tk.Frame(root, width=900, height=500, bg="lightgreen")  # Ajusta el tamaño del Frame
frame.pack(pady=130)
#frame.pack_propagate(True)  # Evita que el Frame cambie de tamaño automáticamente según el contenido

# Dibujo del ahorcado
lbl_dibujo = tk.Label(frame, text=dibujo[0], font=("Courier", 15),  bg ="orange")
lbl_dibujo.grid(row=0, column=0, columnspan=2)

# Palabra con guiones
lbl_palabra = tk.Label(frame, text="", font=("Courier", 20,"bold"),fg="green")
lbl_palabra.grid(row=1, column=0, columnspan=2, pady=10)

# Letras usadas
lbl_letras_usadas = tk.Label(frame, text="Letras usadas: ", font=("Courier", 15), fg="blue", bg="yellow",relief="sunken")
lbl_letras_usadas.grid(row=2, column=0, columnspan=2)

# Entrada de letra
lbl_letra = tk.Label(frame, text="Ingresa una letra: ", font=("Courier", 15), fg="blue", bg="lightblue", relief="raised")
lbl_letra.grid(row=3, column=0, pady=10)
entry_letra = tk.Entry(frame, font=("Courier", 15,"bold"),bg="yellow", fg="black")
entry_letra.grid(row=3, column=1)

# Botones
btn_verificar = tk.Button(frame, text="Verificar Letra", command=verificar_letra,
                          bg="lightblue", font=("Courier", 15), fg="red",  relief="raised")
btn_verificar.grid(row=4, column=0, pady=20)


btn_nueva_partida = tk.Button(frame, text="Nueva Partida", command=jugar_de_nuevo, font=("Courier", 15), bg="lightblue", fg="red")
btn_nueva_partida.grid(row=4, column=1)

# Mensajes
lbl_mensaje = tk.Label(frame, text="", font=("Courier", 15))
lbl_mensaje.grid(row=5, column=0, columnspan=2)

lista_palabras = ["heladera", "manzana", "informatorio", "programacion", "tortuga", "ventilador", "python", "mochila", "cocina","celular", "berenjena", "zanahoria", "servilleta", "yerba"]
iniciar_partida()

root.mainloop()
