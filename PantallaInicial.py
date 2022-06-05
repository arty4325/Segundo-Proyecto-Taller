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

def labelDest(List):
    if List == []:
        return [] #Condicion de finalizacion 
    else:
        (List[0]).destroy() #Se destruyen los elementos 
        labelDest(List[1:]) #Se hace un slicing
    

def PantallaInicial(window, Inicio):
    Inicio.configure(background = '#3885BD')
    #Se pone el logo del juego
    Background = ImageTk.PhotoImage(file = "Images/BegginningLogo.png")
    Inicio.create_image(50, 0, image = Background, anchor = "nw")
    
    temp = []
    
    #Se quiere crear una serie de botones
    # 1) Boton de Inicio de Sesion (Username and Cant - Naves)
    # 2) Boton de jugar partida guardada 
    # 3) Boton de about
    # 4) Boton de salon de la fama
    # 5) Boton de exit
    # Estos botones van a redirigir a otras funciones y haran otras cosas
    # Los botones llevan a nuevas pantallas que llaman al juego en instancias distintas
    
    def InicSecion():
        print("Inicia Sesion")
        Inicio.delete("all")
        labelDest(temp)
        NewAccountWindow(window, Inicio)
    
    def SavedGame():
        print("Juega partida guardada")
        Inicio.delete("all")
        labelDest(temp)
    
    def About():
        print("PantallaAbout")
        Inicio.delete("all")
        labelDest(temp)
        
    def SalonFama():
        print("Se inicia el salon de la fama")
        Inicio.delete("all")
        labelDest(temp)
        
    def Exit():
        labelDest(temp)
        window.destroy()
        Inicio.delete("all")
        
        
    InicButton = tk.Button(Inicio, command = InicSecion, text = "Login")
    InicButton.place(x = 335, y = 200, anchor = "nw")
    temp.append(InicButton)
    
    SavedGameButton = tk.Button(Inicio, command = SavedGame, text = "Jugar juego guardado")
    SavedGameButton.place(x = 295, y = 300, anchor = "nw")
    temp.append(SavedGameButton)
    
    AboutButton = tk.Button(Inicio, command = About, text = "About")
    AboutButton.place(x = 335, y = 400, anchor = "nw")
    temp.append(AboutButton)
    
    FameButton = tk.Button(Inicio, command = SalonFama, text = "Ranking")
    FameButton.place(x = 335, y = 500, anchor = "nw")
    temp.append(FameButton)

    ExitButton = tk.Button(Inicio, command = Exit, text = "Exit")
    ExitButton.place(x = 335, y = 600, anchor = "nw")
    temp.append(ExitButton)

    window.mainloop()

def NewAccountWindow(window, Inicio):
    Background = ImageTk.PhotoImage(file = "Images/BegginningLogo.png")
    Inicio.create_image(50, 0, image = Background, anchor = "nw")
    
    UserEntry = tk.Entry(Inicio, width = 10, font = ("Helvetica", 50))
    UserEntry.place(x = 170, y = 300, anchor = "nw")
    
    def UserLoad():
        nonlocal UserEntry
        User = UserEntry.get()
        print(User)
        
    UserButton = tk.Button(Inicio, command = UserLoad, text = "Nombre de usuario")
    UserButton.place(x = 170, y = 390, anchor = "nw")
    
    window.mainloop()
    




PantallaInicial(window, Inicio)