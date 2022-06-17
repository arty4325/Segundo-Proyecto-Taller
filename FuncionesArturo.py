# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:19:30 2022

@author: RYZEN
"""

import pygame #Se va a hacer uso de pygame para programar el juego
import os #Esta libreria se usa para obtener las imagenes del sistema operativo 
import random 
import time
from threading import Thread
# Funciones arturo :)





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
    global THEBOARD, ENEMYBOARD, seconds
    
    def choose_enemys(boat, matriz, ret):
        ret = matriz
        if boat == 4:
            orientation = random.choice([0,1])
            #print(orientation)
            if orientation == 0: #horizontal
                row = random.choice([0,1,2,3,4,5,6,7,8,9])
                col = random.choice([0,1,2,3,4,5,6])
                flag = True
                for i in range(col,col+4):
                    if matriz[row][i] != 0: #importante notar el i 
                        flag = False
                        
                if flag == True:
                    for k in range(col, col + 4):
                        ret[row][k] = 1
                        
                if not flag:
                    #print("it happens")
                    return choose_enemys(boat, matriz, ret)
                
            if orientation == 1:
                row = random.choice([0,1,2,3,4,5,6])
                col = random.choice([0,1,2,3,4,5,6,7,8,9])
                flag = True
                
                for i in range(row, row + 4):
                    if matriz[i][col] != 0:
                        flag = False
                        
                if flag:
                    for i in range(row, row + 4):
                        ret[i][col] = 1
                if not flag:
                    #print("it happens")
                    return choose_enemys(boat, matriz, ret)
        if boat == 3:
            orientation = random.choice([0,1])
            #print(orientation)
            if orientation == 0: #horizontal
                row = random.choice([0,1,2,3,4,5,6,7,8,9])
                col = random.choice([0,1,2,3,4,5,6,7])
                flag = True
                for i in range(col,col+3):
                    if matriz[row][i] != 0: #importante notar el i 
                        flag = False
                        
                if flag == True:
                    for k in range(col, col + 3):
                        ret[row][k] = 1
                        
                if not flag:
                    #print("it happens")
                    return choose_enemys(boat, matriz, ret)
                
            if orientation == 1:
                row = random.choice([0,1,2,3,4,5,6,7])
                col = random.choice([0,1,2,3,4,5,6,7,8,9])
                flag = True
                
                for i in range(row, row + 3):
                    if matriz[i][col] != 0:
                        flag = False
                        
                if flag:
                    for i in range(row, row + 3):
                        ret[i][col] = 1
                if not flag:
                    #print("it happens")
                    return choose_enemys(boat, matriz, ret)
        if boat == 2:
            orientation = random.choice([0,1])
            #print(orientation)
            if orientation == 0: #horizontal
                row = random.choice([0,1,2,3,4,5,6,7,8,9])
                col = random.choice([0,1,2,3,4,5,6,7,8])
                flag = True
                for i in range(col,col+2):
                    if matriz[row][i] != 0: #importante notar el i 
                        flag = False
                        
                if flag == True:
                    for k in range(col, col + 2):
                        ret[row][k] = 1
                        
                if not flag:
                    #print("it happens")
                    return choose_enemys(boat, matriz, ret)
                
            if orientation == 1:
                row = random.choice([0,1,2,3,4,5,6,7,8])
                col = random.choice([0,1,2,3,4,5,6,7,8,9])
                flag = True
                
                for i in range(row, row + 2):
                    if matriz[i][col] != 0:
                        flag = False
                        
                if flag:
                    for i in range(row, row + 2):
                        ret[i][col] = 1
                if not flag:
                    #print("it happens")
                    return choose_enemys(boat, matriz, ret)
        return ret
    
    
    if Bool:
        seconds = 0
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
        
        while Boats[0] != 0:
            ENEMYBOARD = choose_enemys(4, ENEMYBOARD, [])
            Boats[0] -= 1
        while Boats[1] != 0:
            ENEMYBOARD = choose_enemys(3, ENEMYBOARD, [])
            Boats[1] -= 1
        while Boats[2] != 0:
            ENEMYBOARD = choose_enemys(2, ENEMYBOARD, [])
            Boats[2] -= 1
        
        SAVE = open(User + ".txt", "w+")
        for i in range(10):
            SAVE.write(str(THEBOARD[i]) + "\n")
        for i in range(10):
            SAVE.write(str(ENEMYBOARD[i]) + "\n")
        SAVE.close()
    
    
    

        
    if not Bool: 
        BOARDS = open(User + ".txt", "r")
        THEBOARD = []
        ENEMYBOARD = []
        for i in range(10):
            THEBOARD.append([])
            Var = BOARDS.readline()
            for k in Var[1:-2]:
                if k != "," and k != " ":
                    THEBOARD[i].append(int(k))
        for i in range(10):
            ENEMYBOARD.append([])
            Var = BOARDS.readline()
            for k in Var[1:-2]:
                if k != "," and k != " ":
                    ENEMYBOARD[i].append(int(k))
        alreadyplayedtime = BOARDS.readline()
        seconds = int(alreadyplayedtime)
        print(seconds)
        BOARDS.close()
    print(seconds)
    Thread(target = clock, args = ()).start()
    #print(THEBOARD, ENEMYBOARD)


def check_the_board():
    IWinFlag = False
    EnemyWinFlag = False
    CountMyBoats = 0
    for i in range(10):
        for k in range(10):
            if THEBOARD[i][k] == 1:
                CountMyBoats += 1
    CountEnemyBoats = 0
    for w in range(10):
        for r in range(10):
            if ENEMYBOARD[w][r] == 1:
                CountEnemyBoats += 1
    if CountMyBoats == 0:
        EnemyWinFlag = True
    if CountEnemyBoats == 0:
        IWinFlag = True
        
    return IWinFlag, EnemyWinFlag
        


def SafeBoards(User):
    global THEBOARD, ENEMYBOARD, seconds
    SAVE = open(User + ".txt", "w+")
    for i in range(10):
        SAVE.write(str(THEBOARD[i]) + "\n")
    for i in range(10):
        SAVE.write(str(ENEMYBOARD[i]) + "\n")
    SAVE.write(str(seconds))
    print(seconds)
    

    
                

    
    
class Board:
    def __init__(self):
        self.board = THEBOARD #Representacion interna del tablero (Probs esto se guarde en el .txt)
        self.enemy_board = ENEMYBOARD
        self.selected_piece = None #Se ha seleccionado o no se ha seleccionado 

    def draw_squares(self, win):
        #En el caso del battleship todos son azules 
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, RED, (750 + row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def draw_enemy_squares(self, win):
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, RED,  (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    
            
    def draw_boat(self, row, col, win):
        self.board[col][row] = 1
        #print(self.board, row, col)
        #self.draw_squares(win)
        #print(self.board)
        #piece = Piece(col, row, WHITE)
        #piece.draw(win)
   
    
    
    
    def draw(self, win): #Esto dibuja todo 
        self.draw_squares(win)

    def draw_enemy(self, win): #Esto dibuja todo 
        self.draw_enemy_squares(win)
        
    def draw_selected_notkilled_boat(self, row, col, win):
        flag = self.enemy_board[col][row] 
        if flag == 0:
            self.enemy_board[col][row] = 2 #Esto significa que se selecciono una casilla en la que no habia enemigo
        if flag == 1:
            self.enemy_board[col][row] = 3 #Esto significa que se selecciono una casilla en la que HABIA enemigo
        
        #self.enemy_board[col][row] = 2 
        #Esto se usa cuando uno dispara a una casilla en la cual no hay un bote
        #la idea en esto es que primero lea que es lo que hay y despues tome la desicion de lo que se esta haciendo
        #self.draw_enemy_squares(win)
        #piece = Piece(col, row, WHITE) #Cambiarle el color
        #piece.draw(win)
        
    def make_enemys(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                flag = self.board[col][row]
                if flag == 1:
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
            for col in range(COLS):
                flag = self.enemy_board[col][row]
                if flag == 2:
                    piece = Piece(col, row, BLACK)
                    piece.select_draw(win, (0, 0, 255))
                if flag == 3:
                    piece = Piece(col, row, BLACK)
                    piece.select_draw(win, (255, 0, 0))
                    
    
    def random_enemy(self, win):
        row = random.choice([0,1,2,3,4,5,6,7,8,9])
        col = random.choice([0,1,2,3,4,5,6,7,8,9])
        flag = self.board[col][row]
        if flag == 0:
            self.board[col][row] = 2 #Este 2 significa que en MI tablero el enemigo selecciono una casilla en donde NO habia barco
        if flag == 1:
            self.board[col][row] = 3 #Este 3 significa que MI tablero, el enemigo slecciono una casilla en donde HABIA un barco
            Board.random_enemy(self, win)
        if flag == 2 or flag == 3:
            Board.random_enemy(self, win)
                    
    #def create_board(self): #Se agregan piezas
    def return_what_i_selected(self, row, col):
        return self.enemy_board[col][row]


class Piece: #Esta clase tiene que ser modificada para despues trabajar con los barcos 
    PADDING = 10
    OUTLINE = 2
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False #Este se va a quitar
        self.direction = 1 #Cambiar esto por que no va con el juego 
        
        if self.color == RED: 
            self.direction = -1 
        else:
            self.direction = 1
        
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE//2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE//2
        
    def make_king(self):
        self.king = True #Este se quita 
    
    def draw(self, win):
        #Aqui se dibujarian los enemigos, hay que ver como hacer eso 
        radius = SQUARE_SIZE//2 - self.PADDING 
        pygame.draw.circle(win, self.color, (750 + self.x, self.y), radius)
        pygame.draw.circle(win, GREY, (750 + self.x, self.y), radius + self.OUTLINE) #Esto seria en el caso de los enemigos
        
    def enemy_selection(self, win, selcol):
        radius = SQUARE_SIZE//2 - self.PADDING
        #pygame.draw.circle(win, self.color, (750 + self.x, self.y), radius)
        pygame.draw.circle(win, selcol, (750 + self.x, self.y), radius + self.OUTLINE)
    
    def select_draw(self, win, selcol):
        radius = SQUARE_SIZE//2 - self.PADDING 
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        pygame.draw.circle(win, selcol, (self.x, self.y), radius + self.OUTLINE) #Esto seria en el caso de los enemigos
    
    def draw_enemy(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING 
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE) #Esto seria en el caso de los enemigos
    
    def __repr__(self):
         return str(self.color)


def build_podium(user):
    #Para este momento yo YA gane el juego
    #Quiero hacer dos listas, rnakingbytime y rankingbyname 
    global seconds
    UserTimeTime = []
    UserTimeName = []
    UserTimeTime.append(seconds)
    UserTimeName.append(user)
    
    RankingTime = open("RankingByTime.txt", "r")
    RankingTimeList = RankingTime.readlines()
    for i in range(len(RankingTimeList)):
        if i%2 == 1 and i != len(RankingTimeList) - 1:
            UserTimeTime.append(int(RankingTimeList[i][0:-1]))
        elif i%2 == 0:
            UserTimeName.append(RankingTimeList[i][0:-1])
        else:
            UserTimeTime.append(int(RankingTimeList[len(RankingTimeList) - 1]))
    
    def quick_sort(Lista):
        #Autor: Milton
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
        #Autor: Milton
        if i == n:
            return Menores, Iguales, Mayores
        if Lista[i] < Pivote:
            Menores.append(Lista[i])
        elif Lista[i] > Pivote:
            Mayores.append(Lista[i])
        elif Lista[i] == Pivote:
            Iguales.append(Lista[i])
        return partir(Lista, i + 1,n, Pivote, Menores, Iguales, Mayores)
    
    RankedTimeTime = quick_sort(UserTimeTime)
    RankedTimeNames = []
    
    for i in RankedTimeTime:
        IndexVal = UserTimeName[UserTimeTime.index(i)]
        RankedTimeNames.append(IndexVal)
        
    RankingTime.close()
    print(RankedTimeTime, RankedTimeNames)
    
    RankingTimeWrite = open('RankingByTime.txt', 'w+')
    
    for i in range(len(RankedTimeTime) - 1):
    
        RankingTimeWrite.write(RankedTimeNames[i] + "\n")
        RankingTimeWrite.write(str(RankedTimeTime[i]) + "\n")
    
    RankingTimeWrite.close()
    
    
    
    def insert_sort(Lista):
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
    
    RankingName = open("RankingByName.txt", "r")
    RankingNameList = RankingName.readlines()
    
    UserNameTime = []
    UserNameName = []
    UserNameTime.append(seconds)
    UserNameName.append(user)
    
    for i in range(len(RankingNameList)):
        if i % 2 == 1 and i != len(RankingNameList) - 1:
            UserNameTime.append(int(RankingNameList[i][0:-1]))
        elif i % 2 == 0:
            UserNameName.append(RankingNameList[i][0:-1])
        else:
            UserNameTime.append(int(RankingNameList[len(RankingNameList) - 1]))
    
    NonMutedUserNameName = UserNameName[:]
    
    RankedNameName = insert_sort(UserNameName)
    RankedNameTime = []
    
    for i in RankedNameName:
        IndexVal = UserNameTime[NonMutedUserNameName.index(i)]
        RankedNameTime.append(IndexVal)
    
    RankingName.close()
    
    RankingNameWrite = open("RankingByName.txt", "w+")
    for i in range(len(RankedNameName) - 1):
        RankingNameWrite.write(RankedNameName[i] + "\n")
        RankingNameWrite.write(str(RankedNameTime[i]) + "\n")
        
    RankingNameWrite.close()
        
    
    
    
        
    return RankedTimeTime, RankedTimeNames
    
    
            
    
    
    
    
    
    
    
    
    
    
    
    
     


        
        
        
        
        
        
        
        
        