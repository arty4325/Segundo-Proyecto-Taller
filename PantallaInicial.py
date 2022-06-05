"""
En este modulo se va a crear la pantalla Inicial en tkinter 
Esta pantalla Inicial le permite al jugador elegir la cantidad de naves
Le permite al jugador ingresar su nombre de usuario 
Le permite al jugador ver la pantalla de Ranking 
Y le permite al jugador iniciar una partida que ya estuviera guardada
"""

import tkinter as tk
from PIL import Image, ImageTk


window = tk.Tk()
window.title("Battleship")
window.minsize(700, 700)
window.resizable(False, False)

Inicio = tk.Canvas(window, width = 700, height = 700)
Inicio.place(x = 0, y = 0)

def PantallaInicial(window, Inicio):
    Inicio.configure(background = '#3885BD')
    #Se pone el logo del juego
    Background = ImageTk.PhotoImage(file = "Images/BegginningLogo.png")
    Inicio.create_image(50, 0, image = Background, anchor = "nw")
    
    
    
    
    
    
    window.mainloop()

PantallaInicial(window, Inicio)