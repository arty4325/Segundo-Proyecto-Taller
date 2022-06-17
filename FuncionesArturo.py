"""
Modulo de Funciones varias
"""

import pygame #Se va a hacer uso de pygame para programar el juego
import os #Esta libreria se usa para obtener las imagenes del sistema operativo 
import random 
import time
from threading import Thread
import tkinter as tk






WIDTH, HEIGHT = 1450, 700 #Tamaño de la pantalla 
ROWS, COLS = 10, 10
SQUARE_SIZE = 700//COLS

RED = (65,105,225)
WHITE = (255, 255, 255)
BLACK = (0,206,209)
BLUE = (0, 0, 255) 
GREY = (128, 128, 128)

REALBLACK = (0, 0, 255)

global seconds 
seconds = None


def clock():
    global seconds 
    print(seconds)
    seconds = seconds + 1
    time.sleep(1)
    return clock()

def CreateBoards(Bool, User, Boats):
    """
            Instituto Tecnológico de Costa Rica
                Ingenieria en Computadores
    Nombre: CreateBoards(Bool, User, Boats)
    Lenguaje: Python 3.8.0
    Autor: Oscar Acuña Durán(2022049304), Mariana Saray Rojas Rojas (2020076936)
    Version: 1.0
    Fecha de última modificación: Junio 16/ 2022
    Entradas: Bool recibe un valor de True o False, User es un string y representa el nombre de usuario y Boats es una lista
    Restricciones: Boats tiene que tener una cantidad de barcos que quepa en el tablero
    Salidas: Crea o carga las matrices que se usan durante el juego
    """
    global THEBOARD, ENEMYBOARD, seconds
    
    def choose_enemys(boat, matriz, ret):
        """
            Instituto Tecnológico de Costa Rica
                Ingenieria en Computadores
        Nombre: choose_enemys(boat, matriz, ret)
        Lenguaje: Python 3.8.0
        Autor: Oscar Acuña Durán(2022049304), Mariana Saray Rojas Rojas (2020076936)
        Version: 1.0
        Fecha de última modificación: Junio 16/ 2022
        Entradas: boat es un numero entero entre 2 y 4, matriz es una matiz de 10x10 y ret es la variable en la que se almacena el resultado en cola
        Restricciones: boat pertenece a [2, 4] y es entero, matriz y ret son listas, matriz es de 10x10
        Salidas: acomoda los barcos enemigos en una matriz que se usa durante el juego
        """
        ret = matriz
        if boat == 4: #Se esta tomando en consideracion el barco grande
            orientation = random.choice([0,1]) #Se elige la orientacion del barco, 1 es vertical y 0 es horizontal 
            if orientation == 0: #horizontal
                row = random.choice([0,1,2,3,4,5,6,7,8,9]) #Se puede escoger cualquier fila como pivote
                col = random.choice([0,1,2,3,4,5,6]) #Como el barco ocupa cuatro casillas el pivote esta entre 0 y 6
                flag = True #Se crea una bandera que se utilizara para revisar que no hay barcos en las casillas que se piensa usar
                for i in range(col,col+4): # Toma cuatro casillas a la derecha del pivote
                    if matriz[row][i] != 0: #Revisa si en alguna de esas casillas hay algo 
                        flag = False #Si hay algo la bandera lo indica
                        
                if flag == True: #Si no hay nada en las casillas que se piensan usar, se procede a colocar el barco
                    for k in range(col, col + 4): #Se hace un loop en las columnas
                        ret[row][k] = 1 #Se cambia el valor en la matriz, 1 = hay barco
                        
                if not flag: #Si habia algo en las casillas que se pensaban usar, se tiene que volver a llamar la funcioin
                    return choose_enemys(boat, matriz, ret) #Se intenta de nuevo colocar el barco
                
            if orientation == 1: #Si la orientacion es vertical
                row = random.choice([0,1,2,3,4,5,6]) #El pivote de la fila esta entre 0 y 6
                col = random.choice([0,1,2,3,4,5,6,7,8,9]) #El pivote en la columna esta entre 0 y 10
                flag = True #Se revisa que en las casillas en las que se piensa poner el barco no haya nada
                
                for i in range(row, row + 4): #Revisando las columnas
                    if matriz[i][col] != 0:
                        flag = False
                        
                if flag: #Si no hay nada en las casillas que se piensan usar, se coloca el barco
                    for i in range(row, row + 4):
                        ret[i][col] = 1 #Se cambia el valor en la matriz
                if not flag: #Si habia algo en las casilla que se piensan usar, se tiene que volver a llamar la funcion
                    return choose_enemys(boat, matriz, ret)
        if boat == 3: # Se considera el barco mediano 
            orientation = random.choice([0,1]) #Se revisa si se colocara horizontal o vertical
            if orientation == 0: #horizontal
                row = random.choice([0,1,2,3,4,5,6,7,8,9]) #pivote en las filas no tiene restriccion 
                col = random.choice([0,1,2,3,4,5,6,7]) #Pivote en las columas tiene que estar entre 0 y 6
                flag = True #Se revisa qeu no haya nada en las casillas que se piensan usar 
                for i in range(col,col+3):
                    if matriz[row][i] != 0: 
                        flag = False #Si se encuentra algo la bandera se vuelve falsa
                        
                if flag == True: #Si no hay nada en las casillas que se piensan usar, se coloca el barco
                    for k in range(col, col + 3):
                        ret[row][k] = 1 #El valor en la matriz se cambia
                        
                if not flag: #si habia algo en las casillas que se pensaban usar se vuelve a intentar
                    return choose_enemys(boat, matriz, ret)
                
            if orientation == 1: #Analogamente cuando el barco se coloca de manera vertical 
                row = random.choice([0,1,2,3,4,5,6,7]) #El pivote en las filas esta entre 0 y 7
                col = random.choice([0,1,2,3,4,5,6,7,8,9]) # El pivote en las columnas esta entre 0 y 9
                flag = True #Se crea una bandera para revisar que no hay nada en las casillas que se piensan usar 
                
                for i in range(row, row + 3):
                    if matriz[i][col] != 0:
                        flag = False #Si se encuentra algo se declara la bandera como false
                        
                if flag: #Si no se encontro nada se coloca el barco en la matriz
                    for i in range(row, row + 3):
                        ret[i][col] = 1
                if not flag: #Si habia algun numero distinto a cero en esas casillas se vuelve a intentar colocar el barco
                    return choose_enemys(boat, matriz, ret)
                
        if boat == 2: #Se esta tomando en consideracion el barco pequeño 
            orientation = random.choice([0,1]) #Orientacion vertical o horizontal 
            if orientation == 0: #horizontal
                row = random.choice([0,1,2,3,4,5,6,7,8,9]) #Pivote en filas entre 0 y 9
                col = random.choice([0,1,2,3,4,5,6,7,8]) #Pivote en columnas entre 0 y 8
                flag = True #Bandera para revisar que las casillas que se piensan usar estan disponibles
                for i in range(col,col+2): 
                    if matriz[row][i] != 0: #importante notar el i 
                        flag = False #Si se encuentra algo en esas casillas se declara la bandera como falsa
                        
                if flag == True: #Si no se encuentra nada entonces se colocan los barcos en la matriz
                    for k in range(col, col + 2):
                        ret[row][k] = 1 #Se modifica la matriz
                        
                if not flag: #Si habia algo se vuelve a intentar la colocacion
                    return choose_enemys(boat, matriz, ret)
                
            if orientation == 1: #Si la orientacion es vertical 
                row = random.choice([0,1,2,3,4,5,6,7,8]) #Pivote en fila entre 0 y 8
                col = random.choice([0,1,2,3,4,5,6,7,8,9]) #Pivote en columna entre 0 y 9
                flag = True #Bandera para revisar casillas que se piensan usar 
                
                for i in range(row, row + 2):
                    if matriz[i][col] != 0:
                        flag = False #Si hay algo en las casillas que se piensan usar, se cambia la bandera a Falso
                        
                if flag: #Si las casillas estan disponibles se coloca en barco en la matiz 
                    for i in range(row, row + 2):
                        ret[i][col] = 1 #Se modifica la matriz 
                if not flag:
                    return choose_enemys(boat, matriz, ret)
        return ret
    
    
    if Bool: #Bool es verdadero en el caso de que se este creando una nueva partida
        seconds = 0
        #Se crean las matrices del jugador y del enemigo 
        THEBOARD = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        ENEMYBOARD = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
        
        while Boats[0] != 0: #Se revisa cuantos barcos grandes se tienen que colocar, y se colocan en el tablero enemigo
            ENEMYBOARD = choose_enemys(4, ENEMYBOARD, [])
            Boats[0] -= 1
        while Boats[1] != 0: #Se revisa cuantos barcos medianos hay que colocar, y se colocan en el tablero enemigo 
            ENEMYBOARD = choose_enemys(3, ENEMYBOARD, [])
            Boats[1] -= 1
        while Boats[2] != 0: #Se revisa cuantos barcos pequeños hay qeu colocar, y se colocan en el tablero enemigo
            ENEMYBOARD = choose_enemys(2, ENEMYBOARD, [])
            Boats[2] -= 1
        
        SAVE = open(User + ".txt", "w+") #Se garda esto en un archivo txt
        for i in range(10):
            SAVE.write(str(THEBOARD[i]) + "\n")
        for i in range(10):
            SAVE.write(str(ENEMYBOARD[i]) + "\n")
        SAVE.close()
    
    
    

        
    if not Bool: #Si se esta cargando una partida que ya se estaba jugando con antelacion
        BOARDS = open(User + ".txt", "r") #Se abre el documento que tiene las matrices
        THEBOARD = [] #Se asigna la variable para la matriz del jugador
        ENEMYBOARD = [] #Se asigna la variable para la matriz del enemigo 
        for i in range(10): #Se leen las primeras diez lineas de la matriz para colocarlas en la matriz del jugador
            THEBOARD.append([])
            Var = BOARDS.readline()
            for k in Var[1:-2]:
                if k != "," and k != " ":
                    THEBOARD[i].append(int(k))
        for i in range(10): #Se leen las otras diez lineas de la matriz para colocarlas en la matriz del enemigo 
            ENEMYBOARD.append([])
            Var = BOARDS.readline()
            for k in Var[1:-2]:
                if k != "," and k != " ":
                    ENEMYBOARD[i].append(int(k))
        alreadyplayedtime = BOARDS.readline()
        seconds = int(alreadyplayedtime) #Se cargan los segundos que ya se habian jugado 
        BOARDS.close()
    Thread(target = clock, args = ()).start()
    
    

        
    

def check_the_board(): #Se crea una funcion para revisar si yo o el enemigo ya ganaron el juego 
    IWinFlag = False
    EnemyWinFlag = False
    CountMyBoats = 0
    for i in range(10): #Si no hay ningun 1 en mi matriz, gano el enemigo 
        for k in range(10):
            if THEBOARD[i][k] == 1:
                CountMyBoats += 1
    CountEnemyBoats = 0
    for w in range(10): #Si no hay ningun 2 en mi matriz, gane yo 
        for r in range(10):
            if ENEMYBOARD[w][r] == 1:
                CountEnemyBoats += 1
    if CountMyBoats == 0:
        EnemyWinFlag = True
    if CountEnemyBoats == 0:
        IWinFlag = True
    return IWinFlag, EnemyWinFlag #Se devuelve una tupla con el resultado 
        


def SafeBoards(User): #Se crea una funcion para guardar las matrices cuando se cierra el juego 
    global THEBOARD, ENEMYBOARD, seconds
    SAVE = open(User + ".txt", "w+")
    for i in range(10):
        SAVE.write(str(THEBOARD[i]) + "\n")
    for i in range(10):
        SAVE.write(str(ENEMYBOARD[i]) + "\n")
    SAVE.write(str(seconds)) #Se guarda el tiempo que se ha jugado por el momento 
    

    
                

    
    
class Board: #Se crea una clase que esta encargada de controlar el tablero 
    def __init__(self):
        self.board = THEBOARD #Representacion interna del tablero con la matriz que ya se habia hecho 
        self.enemy_board = ENEMYBOARD
        self.selected_piece = None #Se revisa si esa pieza ya se selecciono o no 

    def draw_squares(self, win):
        #En esta funcion se dibujan los cuadros del tablero, en el caso del battleship todos son azules
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, RED, (750 + row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def draw_enemy_squares(self, win): #Se dibuja el tablero del enemigo 
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, RED,  (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    
            
    def draw_boat(self, row, col, win):
        self.board[col][row] = 1
    
    
    
    def draw(self, win): #Llama a draw_squares(win)
        self.draw_squares(win)

    def draw_enemy(self, win): #Llama a draw_enemy(win)
        self.draw_enemy_squares(win) 
        
    def draw_selected_notkilled_boat(self, row, col, win):
        flag = self.enemy_board[col][row] 
        if flag == 0:
            self.enemy_board[col][row] = 2 #Esto significa que se selecciono una casilla en la que no habia enemigo
        if flag == 1:
            self.enemy_board[col][row] = 3 #Esto significa que se selecciono una casilla en la que HABIA enemigo

        
    def make_enemys(self, win):
        for row in range(ROWS):
            for col in range(COLS): #Se recorre la matriz
                flag = self.board[col][row]
                if flag == 1: #Se dibujan circulos de distintos colores dependiendo de lo que se encuentre 
                    piece = Piece(col, row, WHITE) 
                    piece.draw(win)
                elif flag == 2:
                    piece = Piece(col, row, REALBLACK)
                    piece.enemy_selection(win, (0, 255, 0))
                elif flag == 3:
                    piece = Piece(col, row, REALBLACK)
                    piece.enemy_selection(win, (255, 0, 0))
    
    def draw_on_enemyboard(self, win):
        for row in range(ROWS):
            for col in range(COLS): #Se recorre la matriz
                flag = self.enemy_board[col][row]
                if flag == 2: #Se dibujan circulos de distintos colores dependiendo de lo que se encuentre
                    piece = Piece(col, row, BLACK)
                    piece.select_draw(win, (0, 0, 255))
                if flag == 3:
                    piece = Piece(col, row, BLACK)
                    piece.select_draw(win, (255, 0, 0))
                    
    
    def random_enemy(self, win):
        row = random.choice([0,1,2,3,4,5,6,7,8,9]) #El enemigo escoge una fila arbitraria 
        col = random.choice([0,1,2,3,4,5,6,7,8,9]) #El enemigo escoge una columna arbitraria
        flag = self.board[col][row] #Se revisa que es lo que hay en lo que escogio el enemigo 
        if flag == 0:
            self.board[col][row] = 2 #Este 2 significa que en MI tablero el enemigo selecciono una casilla en donde NO habia barco
        if flag == 1:
            self.board[col][row] = 3 #Este 3 significa que MI tablero, el enemigo slecciono una casilla en donde HABIA un barco
            Board.random_enemy(self, win)
        if flag == 2 or flag == 3:
            Board.random_enemy(self, win) #Si esto pasa significa que el enemigo selecciono una casilla ya seleccionada
            #Es entonces que se tiene que volver a intetntar la seleccion 
                    
    def return_what_i_selected(self, row, col):
        return self.enemy_board[col][row] #Devuelve cuale es la fila y la columna que el jugador eligio 


class Piece:  #Esta clase se encarga de dibujar el tablero y los circulos en la pantalla
    PADDING = 10
    OUTLINE = 2
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color        

        
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    def calc_pos(self): #Esto se usa para calcular la posicion 
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE//2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE//2
    
    def draw(self, win):
        #Aqui se dibujarian los enemigos
        radius = SQUARE_SIZE//2 - self.PADDING 
        pygame.draw.circle(win, GREY, (750 + self.x, self.y), radius + self.OUTLINE) #Esto seria en el caso de los enemigos
        
    def enemy_selection(self, win, selcol): 
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, selcol, (750 + self.x, self.y), radius + self.OUTLINE)
    
    def select_draw(self, win, selcol):
        radius = SQUARE_SIZE//2 - self.PADDING 
        pygame.draw.circle(win, selcol, (self.x, self.y), radius + self.OUTLINE) #Esto seria en el caso de los enemigos
    
    def draw_enemy(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING 
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE) #Esto seria en el caso de los enemigos
    
    def __repr__(self):
         return str(self.color)


def build_podium(user): #Esta funcion se encarga de organizar el salon de la fama en tiempos de juego y en nombre de usuario 
    """
        Instituto Tecnológico de Costa Rica
            Ingenieria en Computadores
            Nombre: CreateBoards(Bool, User, Boats)
    Lenguaje: Python 3.8.0
    Autor: Oscar Acuña Durán(2022049304), Mariana Saray Rojas Rojas (2020076936)
    Version: 1.0
    Fecha de última modificación: Junio 16/ 2022
    Entradas: la entrada consiste en el nombre de usuario 
    Restricciones: Tiene que ser un string
    Salidas: Construye el podium
    """
    global seconds
    UserTimeTime = [] #Lista la organizacion del tiempo cuando se organiza con el tiempo 
    UserTimeName = []  #Lista para la organizacion de los nombres cuando se organiza con el tiempo 
    UserTimeTime.append(seconds) #Se agregan los segundos de esta partida 
    UserTimeName.append(user) #Se agrega el nombre de usuario de esta partida 
    
    RankingTime = open("RankingByTime.txt", "r") #Se abre el .txt que contiene la organizacion por tiempo 
    RankingTimeList = RankingTime.readlines() 
    for i in range(len(RankingTimeList)): #Se crean dos listas, una con el tiempo y la otra con los nombres 
        if i%2 == 1 and i != len(RankingTimeList) - 1:
            UserTimeTime.append(int(RankingTimeList[i][0:-1]))
        elif i%2 == 0:
            UserTimeName.append(RankingTimeList[i][0:-1])
        else:
            UserTimeTime.append(int(RankingTimeList[len(RankingTimeList) - 1]))
    
    def quick_sort(Lista):
        """
            Instituto Tecnológico de Costa Rica
                Ingenieria en Computadores
                Nombre: CreateBoards(Bool, User, Boats)
        Lenguaje: Python 3.8.0
        Autor: Ing. Milton Villegas Lemus
        Version: 1.0
        Fecha de última modificación: Desconocido 
        Entradas: la entrada consiste en una lista
        Restricciones: La lista tiene que contener elementos ordenables
        Salidas: Da una lista con los valores ordenados
        """
        Menores = []
        Iguales = []
        Mayores = []
        if len(Lista) <= 1:
            return Lista
        Pivote = Lista[-1]
        partir(Lista, 0, len(Lista), Pivote, Menores, Iguales, Mayores)
        Ret = quick_sort(Menores)
        Ret.extend(Iguales) #Extiendelo con esta otra lista
        Ret.extend(quick_sort(Mayores))
        return Ret

    def partir(Lista, i, n, Pivote, Menores, Iguales, Mayores):
        if i == n:
            return Menores, Iguales, Mayores
        if Lista[i] < Pivote:
            Menores.append(Lista[i])
        elif Lista[i] > Pivote:
            Mayores.append(Lista[i])
        elif Lista[i] == Pivote:
            Iguales.append(Lista[i])
        return partir(Lista, i + 1,n, Pivote, Menores, Iguales, Mayores)
    
    RankedTimeTime = quick_sort(UserTimeTime) #Se usa el quick_sort para organizar los tiempos
    RankedTimeNames = [] #Se crea una lista con la cual se van a organizar los nombres
    
    for i in RankedTimeTime: #Se usa el indice para colocar los nombres en el mismo orden en el que va el tiempo 
        IndexVal = UserTimeName[UserTimeTime.index(i)]
        RankedTimeNames.append(IndexVal)
        
    RankingTime.close() #Se cierra el archivo .txt que se estaba utilizando 
    
    RankingTimeWrite = open('RankingByTime.txt', 'w+') #Se vuelve a abrir el mimso archivo pero ahora con la opcion de escritura
    
    for i in range(len(RankedTimeTime) - 1): #Se colocan los datos en el archivo en el orden en el que se encuentran en las listas
    
        RankingTimeWrite.write(RankedTimeNames[i] + "\n")
        RankingTimeWrite.write(str(RankedTimeTime[i]) + "\n")
    
    RankingTimeWrite.close() #se vuelve a cerrar el archivo 
    
    
    
    def insert_sort(Lista):
        """
            Instituto Tecnológico de Costa Rica
                Ingenieria en Computadores
                Nombre: CreateBoards(Bool, User, Boats)
        Lenguaje: Python 3.8.0
        Autor: Ing. Milton Villegas Lemus
        Version: 1.0
        Fecha de última modificación: Desconocido 
        Entradas: la entrada consiste en una lista
        Restricciones: La lista tiene que contener elementos ordenables
        Salidas: Da una lista con los valores ordenados
        """
        return insert_sort_aux(Lista, 1, len(Lista))

    def insert_sort_aux(Lista, i, n):
        if i == n:
            return Lista
        Aux = Lista[i]
        j = incluye_orden(Lista, i, Aux)
        Lista[j] = Aux
        return insert_sort_aux(Lista, i + 1, n)
    
    def incluye_orden(Lista, j, Aux):
        if j <= 0 or Lista[j -1] <= Aux:
            return j
        Lista[j] = Lista[j - 1]
        return incluye_orden(Lista, j - 1, Aux)
    
    RankingName = open("RankingByName.txt", "r") #Se abre el archivo .txt en donde se guardan los datos ordenados por nombre
    RankingNameList = RankingName.readlines() 
    
    UserNameTime = [] #Se crea una varialbe para la organizacion por tiempo cuando se ordena por nombres
    UserNameName = [] #Se cra una variable para la organizacion por nombre cuando se ordena por nombre 
    UserNameTime.append(seconds) #Se agregan los valores en segundos de la partida actual 
    UserNameName.append(user) #Se agregan el nombre de la partida actual 
    
    for i in range(len(RankingNameList)): #Se agregan todos los valores queestan en el archivo .txt a dos lisstas 
        if i % 2 == 1 and i != len(RankingNameList) - 1:
            UserNameTime.append(int(RankingNameList[i][0:-1]))
        elif i % 2 == 0:
            UserNameName.append(RankingNameList[i][0:-1])
        else:
            UserNameTime.append(int(RankingNameList[len(RankingNameList) - 1]))
    
    NonMutedUserNameName = UserNameName[:] #Como las listas son objetos mutables se crea otra lista que no muta al mismo tiempo
    
    RankedNameName = insert_sort(UserNameName) #Se utiliza el insert sort para ordenar en nombre de lista los nombres
    RankedNameTime = [] 
    
    for i in RankedNameName: #Se usan los indices para odernar el tiempo en el mismo orden en el que estan los nombres
        IndexVal = UserNameTime[NonMutedUserNameName.index(i)]
        RankedNameTime.append(IndexVal)
     
    RankingName.close() #Se cierra el archivo .txt
    
    RankingNameWrite = open("RankingByName.txt", "w+") #Se vuelve a abrir el archivo .txt en modo escritura 
    for i in range(len(RankedNameName) - 1):
        RankingNameWrite.write(RankedNameName[i] + "\n")
        RankingNameWrite.write(str(RankedNameTime[i]) + "\n") #Se escribe la informacion ordenada en el archivo 
        
    RankingNameWrite.close() #Se cierra el archivo .txt
        
    
    
    
        
    return RankedTimeTime, RankedTimeNames
    
    
            
    
    
    
    
    
    
    
    
    
    
    
    
     


        
        
        
        
        
        
        
        
        