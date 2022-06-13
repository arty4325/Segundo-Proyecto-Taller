# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:19:30 2022

@author: RYZEN
"""

import pygame #Se va a hacer uso de pygame para programar el juego
import os #Esta libreria se usa para obtener las imagenes del sistema operativo 
import random 
# Funciones arturo :)

WIDTH, HEIGHT = 1450, 850 #Tamaño de la pantalla 
ROWS, COLS = 10, 10
SQUARE_SIZE = 700//COLS

RED = (65,105,225)
WHITE = (255, 255, 255)
BLACK = (0,206,209)
BLUE = (0, 0, 255) 
GREY = (128, 128, 128)


def CreateBoards(Bool, User, Boats):
    global THEBOARD, ENEMYBOARD
    
    def choose_enemys(boat, matriz, ret):
        ret = matriz
        if boat == 4:
            orientation = random.choice([0,1])
            print(orientation)
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
                    print("it happens")
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
                    print("it happens")
                    return choose_enemys(boat, matriz, ret)
        if boat == 3:
            orientation = random.choice([0,1])
            print(orientation)
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
                    print("it happens")
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
                    print("it happens")
                    return choose_enemys(boat, matriz, ret)
        if boat == 2:
            orientation = random.choice([0,1])
            print(orientation)
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
                    print("it happens")
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
                    print("it happens")
                    return choose_enemys(boat, matriz, ret)
        return ret
    
    
    if Bool:
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
        BOARDS.close()
    print(THEBOARD, ENEMYBOARD)




def SafeBoards(User):
    global THEBOARD, ENEMYBOARD
    SAVE = open(User + ".txt", "w+")
    for i in range(10):
        SAVE.write(str(THEBOARD[i]) + "\n")
    for i in range(10):
        SAVE.write(str(ENEMYBOARD[i]) + "\n")
    
                
        
        
    
class Board:
    def __init__(self):
        self.board = THEBOARD #Representacion interna del tablero (Probs esto se guarde en el .txt)
        self.enemy_board = []
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
        print(self.board, row, col)
        self.draw_squares(win)
        #print(self.board)
        piece = Piece(col, row, WHITE)
        piece.draw(win)
   
    
    
    
    def draw(self, win): #Esto dibuja todo 
        self.draw_squares(win)

    def draw_enemy(self, win): #Esto dibuja todo 
        self.draw_enemy_squares(win)
        
        
        
    def make_enemys(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                flag = self.board[col][row]
                if flag == 1:
                    piece = Piece(col, row, WHITE)
                    piece.draw(win)
        
    
   
                    
    #def create_board(self): #Se agregan piezas


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
    
    def draw_enemy(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING 
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE) #Esto seria en el caso de los enemigos
    
    def __repr__(self):
         return str(self.color)

     


        
        
        
        
        
        
        
        
        