#Importa módulos para Interfaz Gráfica de usuario (tkinter)
import tkinter as tk
from tkinter import ttk
import time

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
    retardo : float=0.03
    for i in range(0,35):
        time.sleep(retardo)  #time.sleep,detiene la ejecucion de programa, se debe colocar para que las letras vayan imprimiendo una a una con el tiempo que llega por parámetro, sino saldrian todas juntas
        texto += char
        mylabel.config(text = texto) #coloca el valor de la variable texto dentro de label
        main_window.update_idletasks() #funcion para que la ventana se actualice
        main_window.update()            #funciones para que la ventana se actualice

#Ejecuta tres animaciones
crearAnimacion(10,10, 'G')
crearAnimacion(10,30, 'H')
crearAnimacion(10,50, 'S')


# Mantener las siguientes líneas siempre al final del script y en el mismo orden.
#Coloca la opcion "Salir"
opcionFinalizar()

#Bucle principal de la ventana
main_window.mainloop()

