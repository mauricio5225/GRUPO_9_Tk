import tkinter as tk
import time

def hora(ventana):
    ventana.title('Reloj simple')
    ventana.geometry('400x200')
    reloj = tk.Label(ventana, font =
    ('Arial', 60), bg = 'blue', fg = 'white')

    tiempo_actual = time.strftime('%H:%M:%S')
    reloj.config(text = tiempo_actual)
    ventana.after(1000, hora)
    reloj.pack(anchor = 'center')
    ventana.mainloop()

if __name__ == "__main__":
    ventana = tk.Tk()
    calc = hora(ventana)
    ventana.mainloop()
    
