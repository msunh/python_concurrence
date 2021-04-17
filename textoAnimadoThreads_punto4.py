#Importa módulos para Interfaz Gráfica de usuario (tkinter)
import tkinter as tk
from tkinter import ttk
import time
import threading

#Crea la ventana principal
main_window = tk.Tk()
main_window.title("Ejemplo")
main_window.configure(width=350, height=200)

#Función que crea y posiciona el botón "Salir"
def opcionFinalizar():
    boton = ttk.Button(main_window, text="Salir", command=main_window.destroy)
    boton.place(x=100, y=170)


#Función que crea una etiqueta (label) de texto en la posición (x,y) de la pantalla.
def createLabel(a,b):
    label = ttk.Label(text="")
    label.place(x=a,y=b)
    return label


#Función que crea una etiqueta (llamando a createLabel()) y luego anima texto dentro de la misma.
def crearAnimacion(a, b, char):
    mylabel = createLabel(a,b)
    texto=""
    retardo : float=0.10
    for i in range(0,35):
        time.sleep(retardo)  
        texto += char
        mylabel.config(text = texto) 
        main_window.update_idletasks() 
        main_window.update()            
        

hilo_1 = threading.Thread(target=crearAnimacion(10,10, 'G'))
print ("creo hilo 1")
hilo_2 = threading.Thread(target=crearAnimacion(10,30, 'H'))
print ("creo hilo 2")
hilo_3 = threading.Thread(target=crearAnimacion(10,50, 'S'))
print ("creo hilo 3")


hilo_1.start()
print ("arranco hilo 1")
hilo_2.start()
print ("arranco hilo 2")
hilo_3.start()
print ("arranco hilo 3")
time.sleep(1)

hilo_1.join()
hilo_2.join()
hilo_3.join()

# Mantener las siguientes líneas siempre al final del script y en el mismo orden.
#Coloca la opcion "Salir"
opcionFinalizar()
print("termina la ejecucion")

#Bucle principal de la ventana
main_window.mainloop()

