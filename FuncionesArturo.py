# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:19:30 2022

@author: RYZEN
"""

import pygame #Se va a hacer uso de pygame para programar el juego
import os #Esta libreria se usa para obtener las imagenes del sistema operativo 

# Funciones arturo :)

WIDTH, HEIGHT = 1450, 850 #Tamaño de la pantalla 
ROWS, COLS = 10, 10
SQUARE_SIZE = 700//COLS

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255) 
GREY = (128, 128, 128)
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

class Board:
    def __init__(self):
        self.board = THEBOARD #Representacion interna del tablero (Probs esto se guarde en el .txt)
        self.enemy_board = []
        self.selected_piece = None #Se ha seleccionado o no se ha seleccionado 
        self.red_left = self.white_left = 12 # Se han seleccionado piezas ? 
        self.red_kings = self.white_kings = 0 
        self.create_board()
        self.create_enemy_board()
    
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
    
    
    def create_board(self): #Se tienen que crear piezas, depsues esto se va a cambiar para que sea el usuario el que las crea
        for row in range(ROWS):
            #self.board.append([]) #Se quiere tener una lista interna para cada row
            """
            for col in range(COLS):

                if col % 2 == ((row + 1)%2): #Si la columna en la que estamos es igual a la otra vara mas uno pero diferente puede dibujar la vara
                    #CAMBIAR esto no es asi
                    #A como esta puesto ahora es para hacer las piezas intercaladas en esto
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0) #No se tiene pieza en esta momento, se puede ver bien qeu es lo que se tiene en cada fila o columna
                else:
                    self.board[row].append(0)

                self.board[row].append(0)
            """
                    
    def create_enemy_board(self): #Se tienen que crear piezas, depsues esto se va a cambiar para que sea el usuario el que las crea
        for row in range(ROWS):
            #self.enemy_board.append([]) #Se quiere tener una lista interna para cada row
            """
            for col in range(COLS):
                
                if col % 2 == ((row + 1)%2): #Si la columna en la que estamos es igual a la otra vara mas uno pero diferente puede dibujar la vara
                    #CAMBIAR esto no es asi
                    #A como esta puesto ahora es para hacer las piezas intercaladas en esto
                    
                    if row < 3:
                        self.enemy_board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.enemy_board[row].append(Piece(row, col, RED))
                    else:
                        self.enemy_board[row].append(0) #No se tiene pieza en esta momento, se puede ver bien qeu es lo que se tiene en cada fila o columna
                    
                else:
                
                self.enemy_board[row].append(0)
            """
            
    def draw_boat(self, row, col):
        self.board[row][col] = 1
        print(self.board, row, col)
        
   
        
    
    
    def draw(self, win): #Esto dibuja todo 
        self.draw_squares(win)
        #print(self.board)
        """
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
        """

    def draw_enemy(self, win): #Esto dibuja todo 
        self.draw_enemy_squares(win)
        """
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.enemy_board[row][col]
                if piece != 0:
                    piece.draw_enemy(win)
        """
   
                    
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

     


        
        
        
        
        
        
        
        
        