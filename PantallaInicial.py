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
    """
            Instituto Tecnológico de Costa Rica
                Ingenieria en Computadores
    Nombre: CreateBoards(Bool, User, Boats)
    Lenguaje: Python 3.8.0
    Autor: Oscar Acuña Durán(2022049304), Mariana Saray Rojas Rojas (2020076936)
    Version: 1.0
    Fecha de última modificación: Junio 16/ 2022
    Entradas: window e inicio
    Restricciones: ambos parametros con el Tk y el canvas de tkinter respectivamente
    Salidas: crea una ventana en tkinter
    """
    global temp
    Inicio.configure(background = '#3885BD') #Se le pone un fondo de pantalla al tkinter
    Background = ImageTk.PhotoImage(file = "Images/BegginningLogo.png")
    Inicio.create_image(50, 0, image = Background, anchor = "nw") 
    
    def InicSecion(): #Botonde inicio de secion 
        Inicio.delete("all") 
        labelDest(temp)
        NewAccountWindow(window, Inicio) #Esto llama a otra funcion en tkinter 
    
    def SavedGame(): #Funcion qeu permite cargar partida guardada 
        Inicio.delete("all") 
        labelDest(temp)
        OldAccountWindow(window, Inicio) #Esto llama a otra funcion en tkinter
    
    
    def About(): #Abre la pantalla about 
        Inicio.delete("all")
        labelDest(temp)
        
        
    def SalonFama(): #Funcion que permite ir al salon de la fama 
        Inicio.delete("all")
        labelDest(temp)
        RankingWindow(window, Inicio) #Esto llama a otra funcion en tkinter
        
        
    def Exit(): #Funcion de salir 
        labelDest(temp)
        window.destroy() #Esto cierra la ventana de tkinter 
        
        
    InicButton = tk.Button(Inicio, command = InicSecion, text = "Login") #Se crea el boton de inicio de secion 
    InicButton.place(x = 335, y = 200, anchor = "nw")  
    temp.append(InicButton)

    
    SavedGameButton = tk.Button(Inicio, command = SavedGame, text = "Jugar juego guardado") #Se crea el boton de cargar partida
    SavedGameButton.place(x = 295, y = 300, anchor = "nw")
    temp.append(SavedGameButton)

    
    AboutButton = tk.Button(Inicio, command = About, text = "About") #Se crea el boton de la pantalla about 
    AboutButton.place(x = 335, y = 400, anchor = "nw")
    temp.append(AboutButton)

     
    FameButton = tk.Button(Inicio, command = SalonFama, text = "Ranking") #Se crea el boton del podium 
    FameButton.place(x = 335, y = 500, anchor = "nw") 
    temp.append(FameButton)


    ExitButton = tk.Button(Inicio, command = Exit, text = "Exit") #Se crea el boton para salir de la partida 
    ExitButton.place(x = 335, y = 600, anchor = "nw") 
    temp.append(ExitButton)


    window.mainloop()
    

def RankingWindow(window, Inicio): #Funcion del raking 
    global TimeDisplaying
    TimeRanking = open("RankingByTime.txt", "r") #Se lee el archivo txt que orena por ranking
    TimeRankingList = TimeRanking.readlines()
    TimeRanking.close()
    
    TimeDisplaying = True
    
    Names = []
    Times = []
    temp = []
     
    for i in range(len(TimeRankingList)): #Se crean dos listas, una con los nombres y otra con loss tiempos 
        if i % 2 == 0: 
            Names.append(TimeRankingList[i][0:-1])
        elif i % 2 == 1:
            Times.append(TimeRankingList[i][0:-1])

    #Se colocan los labels de los rankings
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
    
    
    
    
    def change_label(): #Se crea un boton para cuando se quiere cambiar de ranking 
        global TimeDisplaying
        global temp 
        labelDest(temp)
        temp = []
        if TimeDisplaying == True: #Si a lo que se quiere ir es a el orden por nombres 
            TimeRanking = open("RankingByName.txt", "r") #Se lee el archivo txt que ordena por nombres 
            TimeRankingList = TimeRanking.readlines()
            TimeRanking.close()
            
            Names = []
            Times = []
            
    
            for i in range(len(TimeRankingList)): #Se crean dos listas, una que tiene los nombres y otra que tiene los labels
                if i % 2 == 0:
                    Names.append(TimeRankingList[i][0:-1])
                elif i % 2 == 1:
                    Times.append(TimeRankingList[i][0:-1])
                    
            #Se colocan los labels 
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
    
        
        elif TimeDisplaying == False: # en el caso que se quiera ir a la orgnanizacion por tiempos 
            TimeRanking = open("RankingByTime.txt", "r") #Se abre el archivo .txt que lee el tiempo 
            TimeRankingList = TimeRanking.readlines()
            TimeRanking.close()
            
            Names = []
            Times = []
            
    
            for i in range(len(TimeRankingList)): #Se crean dos listas, una con los nombres y otra con los tiempos 
                if i % 2 == 0:
                    Names.append(TimeRankingList[i][0:-1])
                elif i % 2 == 1:
                    Times.append(TimeRankingList[i][0:-1])
            #Se colocan los labels 
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
                
        TimeDisplaying = not TimeDisplaying #Se invierte la variable depsue sdel cambio 
    
    
    
    Change_button = tk.Button(Inicio, command = change_label, text = "Cambiar de Ranking") #Se coloca el boton en la pantalla 
    Change_button.place(x = 200, y = 100, anchor = "nw")
            
    
    
    
    
    
        
    
                
    


def NewAccountWindow(window, Inicio): #Esta variable permite crear una nueva cuenta 
    
    Background = ImageTk.PhotoImage(file = "Images/BegginningLogo.png") #Se pone un fondo 
    Inicio.create_image(50, 0, image = Background, anchor = "nw")
    
    UserEntry = tk.Entry(Inicio, width = 10, font = ("Helvetica", 50)) #Se coloca el entry para oclocar elnombre de usuario 
    UserEntry.place(x = 170, y = 300, anchor = "nw")
    
    BigBoats = tk.Entry(Inicio, width = 4, font = ("Helvetica", 30)) #se colcoa el entry para escoger los barcos grandes
    BigBoats.place(x = 75, y = 450, anchor = "nw")
    
    MediumBoats = tk.Entry(Inicio, width = 4, font = ("Helvetica", 30)) #se coloca el entry para escoger los barcos medianos
    MediumBoats.place(x = 275, y = 450, anchor = "nw")
    
    SmallBoats = tk.Entry(Inicio, width = 4, font = ("Helvetica", 30)) #Se coloca el entry para colocar los barcos pequeñso
    SmallBoats.place(x = 500, y = 450, anchor = "nw")
    
    def UserLoad(): #Se crea el boton que carga todos los entrys 
        nonlocal UserEntry, BigBoats, MediumBoats, SmallBoats
        User = UserEntry.get()
        BBoats = BigBoats.get()
        MBoats = MediumBoats.get()
        SBoats = SmallBoats.get()
        
        
        window.destroy()
        FuncionesArturo.CreateBoards(True, User, [int(BBoats), int(MBoats), int(SBoats)])
        GameTable.RunGame(User, [int(BBoats), int(MBoats), int(SBoats)], [], True)  #Se convierte todo a numeros 
        #Enteros y se llama a la ventana de pygame 
        
        
    UserButton = tk.Button(Inicio, command = UserLoad, text = "Nombre de usuario") #Boton para colocar el nombre de usuario 
    UserButton.place(x = 170, y = 390, anchor = "nw") # Se coloca el boton del nombre de usuario 
    
    
    window.mainloop()

def OldAccountWindow(window, Inicio):#Ventana de tkinter que permite cargar un usuario antiguo 
    
    Background = ImageTk.PhotoImage(file = "Images/BegginningLogo.png") #Se carga el fondo de pantalla
    Inicio.create_image(50, 0, image = Background, anchor = "nw") 
    
    UserEntry = tk.Entry(Inicio, width = 10, font = ("Helvetica", 50)) #Se crea el entry en donde se coloca el nombre de usuario 
    UserEntry.place(x = 170, y = 300, anchor = "nw")

    
    def UserLoad(): #SE crea la funcion para el boton para cargar el nombre de usuario 
        nonlocal UserEntry
        User = UserEntry.get()
        window.destroy()
        FuncionesArturo.CreateBoards(False, User,[])
        GameTable.RunGame(User, [0,0,0], [], False) #Se llama al juego 
        
        
        
        
        
    UserButton = tk.Button(Inicio, command = UserLoad, text = "Nombre de usuario") #boton para el nombre de usuario 
    UserButton.place(x = 170, y = 390, anchor = "nw") #Boton para el nombre de usuario
    
    
    window.mainloop()
    




PantallaInicial(window, Inicio)