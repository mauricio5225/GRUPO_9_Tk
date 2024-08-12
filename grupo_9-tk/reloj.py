import tkinter as tk
import time

ventana = tk.Tk()
ventana.title('Reloj simple')
ancho_ventana = 400
alto_ventana = 100
ancho_pantalla, alto_pantalla = ventana.winfo_screenmmwidth(), ventana.winfo_screenheight()
posicion_x = ancho_pantalla - ancho_ventana
posicion_y = alto_pantalla - alto_ventana

ventana.geometry(f"{ancho_ventana}x{alto_ventana}-{posicion_x}-{posicion_y}")

reloj = tk.Label(ventana, font = ('Arial', 60), bg = 'blue', fg = 'white') 

def hora():
    tiempo_actual = time.strftime('%H:%M:%S')
    reloj.config(text = tiempo_actual)
    ventana.after(1000, hora)
    reloj.pack(anchor = 'center')

hora()

ventana.mainloop()