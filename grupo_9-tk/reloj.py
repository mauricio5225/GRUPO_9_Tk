#reloj
import tkinter as tk
import time

def mostrar_reloj(etiqueta_reloj):
    def actualizar_reloj():
        hora_actual = time.strftime('%H:%M:%S')
        etiqueta_reloj.config(text=hora_actual)
        etiqueta_reloj.after(1000, actualizar_reloj)

    actualizar_reloj()




    
#hora()
#ventana.mainloop()