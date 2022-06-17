"""
En este modulo se va a crear la pantalla Inicial en tkinter 
Esta pantalla Inicial le permite al jugador elegir la cantidad de naves
Le permite al jugador ingresar su nombre de usuario 
Le permite al jugador ver la pantalla de Ranking 
Y le permite al jugador iniciar una partida que ya estuviera guardada
"""

import tkinter as tk
from PIL import Image, ImageTk
import GameTable
import FuncionesArturo

global IsLoaded

global temp
temp = []


window = tk.Tk()
window.title("Battleship")
window.minsize(700, 700)
window.resizable(False, False)

Inicio = tk.Canvas(window, width = 700, height = 700)
Inicio.place(x = 0, y = 0)

def labelDest(List):
    if List == []:
        return [] # Condicion de finalizacion 
    else:
        (List[0]).destroy() # Se destruyen los elementos 
        labelDest(List[1:]) # Se hace un slicing
    

def PantallaInicial(window, Inicio):
    global temp
    Inicio.configure(background = '#3885BD')
    # Se pone el logo del juego
    Background = ImageTk.PhotoImage(file = "Images/BegginningLogo.png")
    Inicio.create_image(50, 0, image = Background, anchor = "nw")
    
    # Se quiere crear una serie de botones
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
        OldAccountWindow(window, Inicio)
    
    
    def About():
        print("PantallaAbout")
        Inicio.delete("all")
        labelDest(temp)
        
        
    def SalonFama():
        print("Se inicia el salon de la fama")
        Inicio.delete("all")
        labelDest(temp)
        #Programar el salon de la fama
        RankingWindow(window, Inicio)
        
        
        
        
        
       
        
    def Exit():
        labelDest(temp)
        window.destroy()
        #Inicio.delete("all")
        
        
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
    

def RankingWindow(window, Inicio):
    global TimeDisplaying
    TimeRanking = open("RankingByTime.txt", "r")
    TimeRankingList = TimeRanking.readlines()
    TimeRanking.close()
    
    TimeDisplaying = True
    
    Names = []
    Times = []
    temp = []
    
    for i in range(len(TimeRankingList)):
        if i % 2 == 0:
            Names.append(TimeRankingList[i][0:-1])
        elif i % 2 == 1:
            Times.append(TimeRankingList[i][0:-1])
          
    print(Names, Times)
        
    if len(Names) >= 1:
        FirstPlace = tk.Label(Inicio, text = Names[0] + Times[0], font = ("Arial", 20), background = "#4A1798")
        FirstPlace.place(x = 350, y = 100, anchor = "nw")
        temp.append(FirstPlace)
    if len(Names) >= 2:
        SecondPlace = tk.Label(Inicio, text = Names[1] + Times[1], font = ("Arial", 20), background = "#4A1798")
        SecondPlace.place(x = 350, y = 150, anchor = "nw")
        temp.append(SecondPlace)
    if len(Names) >= 3:
        ThirdPlace = tk.Label(Inicio, text = Names[2] + Times[2], font = ("Arial", 20), background = "#4A1798")
        ThirdPlace.place(x = 350, y = 200, anchor = "nw")
        temp.append(ThirdPlace)
    if len(Names) >= 4:
        FourthPlace = tk.Label(Inicio, text = Names[3] + Times[3], font = ("Arial", 20), background = "#4A1798")
        FourthPlace.place(x = 350, y = 250, anchor = "nw")
        temp.append(FourthPlace)
    if len(Names) >= 5:
        FifthPlace = tk.Label(Inicio, text = Names[4] + Times[4], font = ("Arial", 20), background = "#4A1798")
        FifthPlace.place(x = 350, y = 300, anchor = "nw")
        temp.append(FifthPlace)
    if len(Names) >= 6:
        SeventhPlace = tk.Label(Inicio, text = Names[5] + Times[5], font = ("Arial", 20), background = "#4A1798")
        SeventhPlace.place(x = 350, y = 350, anchor = "nw")
        temp.append(SeventhPlace)
    if len(Names) >= 7:
        EightPlace = tk.Label(Inicio, text = Names[6] + Times[6], font = ("Arial", 20), background = "#4A1798")
        EightPlace.place(x = 350, y = 400, anchor = "nw")
        temp.append(EightPlace)
    if len(Names) >= 8:
        NinthPlace = tk.Label(Inicio, text = Names[7] + Times[7], font = ("Arial", 20), background = "#4A1798")
        NinthPlace.place(x = 350, y = 450, anchor = "nw")
        temp.append(NinthPlace)
    if len(Names) >= 9:
        TenthPlace = tk.Label(Inicio, text = Names[8] + Times[8], font = ("Arial", 20), background = "#4A1798")
        TenthPlace.place(x = 350, y = 500, anchor = "nw")
        temp.append(TenthPlace)
    if len(Names) >= 10:
        ElevenPlace = tk.Label(Inicio, text = Names[9] + Times[9], font = ("Arial", 20), background = "#4A1798")
        ElevenPlace.place(x = 350, y = 550, anchor = "nw")
        temp.append(ElevenPlace)
    
    
    
    
    def change_label():
        global TimeDisplaying
        global temp 
        labelDest(temp)
        temp = []
        if TimeDisplaying == True:
            TimeRanking = open("RankingByName.txt", "r")
            TimeRankingList = TimeRanking.readlines()
            TimeRanking.close()
            
            Names = []
            Times = []
            
    
            for i in range(len(TimeRankingList)):
                if i % 2 == 0:
                    Names.append(TimeRankingList[i][0:-1])
                elif i % 2 == 1:
                    Times.append(TimeRankingList[i][0:-1])
        
            if len(Names) >= 1:
                FirstPlace = tk.Label(Inicio, text = Names[0] + Times[0], font = ("Arial", 20), background = "#4A1798")
                FirstPlace.place(x = 350, y = 100, anchor = "nw")
                temp.append(FirstPlace)
            if len(Names) >= 2:
                SecondPlace = tk.Label(Inicio, text = Names[1] + Times[1], font = ("Arial", 20), background = "#4A1798")
                SecondPlace.place(x = 350, y = 150, anchor = "nw")
                temp.append(SecondPlace)
            if len(Names) >= 3:
                ThirdPlace = tk.Label(Inicio, text = Names[2] + Times[2], font = ("Arial", 20), background = "#4A1798")
                ThirdPlace.place(x = 350, y = 200, anchor = "nw")
                temp.append(ThirdPlace)
            if len(Names) >= 4:
                FourthPlace = tk.Label(Inicio, text = Names[3] + Times[3], font = ("Arial", 20), background = "#4A1798")
                FourthPlace.place(x = 350, y = 250, anchor = "nw")
                temp.append(FourthPlace)
            if len(Names) >= 5:
                FifthPlace = tk.Label(Inicio, text = Names[4] + Times[4], font = ("Arial", 20), background = "#4A1798")
                FifthPlace.place(x = 350, y = 300, anchor = "nw")
                temp.append(FifthPlace)
            if len(Names) >= 6:
                SeventhPlace = tk.Label(Inicio, text = Names[5] + Times[5], font = ("Arial", 20), background = "#4A1798")
                SeventhPlace.place(x = 350, y = 350, anchor = "nw")
                temp.append(SeventhPlace)
            if len(Names) >= 7:
                EightPlace = tk.Label(Inicio, text = Names[6] + Times[6], font = ("Arial", 20), background = "#4A1798")
                EightPlace.place(x = 350, y = 400, anchor = "nw")
                temp.append(EightPlace)
            if len(Names) >= 8:
                NinthPlace = tk.Label(Inicio, text = Names[7] + Times[7], font = ("Arial", 20), background = "#4A1798")
                NinthPlace.place(x = 350, y = 450, anchor = "nw")
                temp.append(NinthPlace)
            if len(Names) >= 9:
                TenthPlace = tk.Label(Inicio, text = Names[8] + Times[8], font = ("Arial", 20), background = "#4A1798")
                TenthPlace.place(x = 350, y = 500, anchor = "nw")
                temp.append(TenthPlace)
            if len(Names) >= 10:
                ElevenPlace = tk.Label(Inicio, text = Names[9] + Times[9], font = ("Arial", 20), background = "#4A1798")
                ElevenPlace.place(x = 350, y = 550, anchor = "nw")
                temp.append(ElevenPlace)
    
    
        elif TimeDisplaying == False:
            TimeRanking = open("RankingByTime.txt", "r")
            TimeRankingList = TimeRanking.readlines()
            TimeRanking.close()
            
            Names = []
            Times = []
            
    
            for i in range(len(TimeRankingList)):
                if i % 2 == 0:
                    Names.append(TimeRankingList[i][0:-1])
                elif i % 2 == 1:
                    Times.append(TimeRankingList[i][0:-1])
        
            if len(Names) >= 1:
                FirstPlace = tk.Label(Inicio, text = Names[0] + Times[0], font = ("Arial", 20), background = "#4A1798")
                FirstPlace.place(x = 350, y = 100, anchor = "nw")
                temp.append(FirstPlace)
            if len(Names) >= 2:
                SecondPlace = tk.Label(Inicio, text = Names[1] + Times[1], font = ("Arial", 20), background = "#4A1798")
                SecondPlace.place(x = 350, y = 150, anchor = "nw")
                temp.append(SecondPlace)
            if len(Names) >= 3:
                ThirdPlace = tk.Label(Inicio, text = Names[2] + Times[2], font = ("Arial", 20), background = "#4A1798")
                ThirdPlace.place(x = 350, y = 200, anchor = "nw")
                temp.append(ThirdPlace)
            if len(Names) >= 4:
                FourthPlace = tk.Label(Inicio, text = Names[3] + Times[3], font = ("Arial", 20), background = "#4A1798")
                FourthPlace.place(x = 350, y = 250, anchor = "nw")
                temp.append(FourthPlace)
            if len(Names) >= 5:
                FifthPlace = tk.Label(Inicio, text = Names[4] + Times[4], font = ("Arial", 20), background = "#4A1798")
                FifthPlace.place(x = 350, y = 300, anchor = "nw")
                temp.append(FifthPlace)
            if len(Names) >= 6:
                SeventhPlace = tk.Label(Inicio, text = Names[5] + Times[5], font = ("Arial", 20), background = "#4A1798")
                SeventhPlace.place(x = 350, y = 350, anchor = "nw")
                temp.append(SeventhPlace)
            if len(Names) >= 7:
                EightPlace = tk.Label(Inicio, text = Names[6] + Times[6], font = ("Arial", 20), background = "#4A1798")
                EightPlace.place(x = 350, y = 400, anchor = "nw")
                temp.append(EightPlace)
            if len(Names) >= 8:
                NinthPlace = tk.Label(Inicio, text = Names[7] + Times[7], font = ("Arial", 20), background = "#4A1798")
                NinthPlace.place(x = 350, y = 450, anchor = "nw")
                temp.append(NinthPlace)
            if len(Names) >= 9:
                TenthPlace = tk.Label(Inicio, text = Names[8] + Times[8], font = ("Arial", 20), background = "#4A1798")
                TenthPlace.place(x = 350, y = 500, anchor = "nw")
                temp.append(TenthPlace)
            if len(Names) >= 10:
                ElevenPlace = tk.Label(Inicio, text = Names[9] + Times[9], font = ("Arial", 20), background = "#4A1798")
                ElevenPlace.place(x = 350, y = 550, anchor = "nw")
                temp.append(ElevenPlace)
                
        TimeDisplaying = not TimeDisplaying
    
    
    
    Change_button = tk.Button(Inicio, command = change_label, text = "Cambiar de Ranking")
    Change_button.place(x = 200, y = 100, anchor = "nw")
            
    
    
    
    
    
        
    
                
    


def NewAccountWindow(window, Inicio):
    
    Background = ImageTk.PhotoImage(file = "Images/BegginningLogo.png")
    Inicio.create_image(50, 0, image = Background, anchor = "nw")
    
    UserEntry = tk.Entry(Inicio, width = 10, font = ("Helvetica", 50))
    UserEntry.place(x = 170, y = 300, anchor = "nw")
    
    BigBoats = tk.Entry(Inicio, width = 4, font = ("Helvetica", 30))
    BigBoats.place(x = 75, y = 450, anchor = "nw")
    
    MediumBoats = tk.Entry(Inicio, width = 4, font = ("Helvetica", 30))
    MediumBoats.place(x = 275, y = 450, anchor = "nw")
    
    SmallBoats = tk.Entry(Inicio, width = 4, font = ("Helvetica", 30))
    SmallBoats.place(x = 500, y = 450, anchor = "nw")
    
    def UserLoad():
        nonlocal UserEntry, BigBoats, MediumBoats, SmallBoats
        User = UserEntry.get()
        BBoats = BigBoats.get()
        MBoats = MediumBoats.get()
        SBoats = SmallBoats.get()
        
        
        window.destroy()
        FuncionesArturo.CreateBoards(True, User, [int(BBoats), int(MBoats), int(SBoats)])
        GameTable.RunGame(User, [int(BBoats), int(MBoats), int(SBoats)], [], True) 
        # grandes , medianos , pequeños 
        
        
        
        
        
    UserButton = tk.Button(Inicio, command = UserLoad, text = "Nombre de usuario")
    UserButton.place(x = 170, y = 390, anchor = "nw")
    
    
    window.mainloop()

def OldAccountWindow(window, Inicio):
    
    Background = ImageTk.PhotoImage(file = "Images/BegginningLogo.png")
    Inicio.create_image(50, 0, image = Background, anchor = "nw")
    
    UserEntry = tk.Entry(Inicio, width = 10, font = ("Helvetica", 50))
    UserEntry.place(x = 170, y = 300, anchor = "nw")
    # Se podria programar que revise si ese nombre de usuario existe
    
    def UserLoad():
        nonlocal UserEntry
        User = UserEntry.get()
        window.destroy()
        FuncionesArturo.CreateBoards(False, User,[])
        GameTable.RunGame(User, [0,0,0], [], False)
        
        
        
        
        
    UserButton = tk.Button(Inicio, command = UserLoad, text = "Nombre de usuario")
    UserButton.place(x = 170, y = 390, anchor = "nw")
    
    
    window.mainloop()
    




PantallaInicial(window, Inicio)