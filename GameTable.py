"""
Segundo proyecto taller de Programacion
Rojas Rojas Mariana 
Acuña Duran Oscar
"""

import pygame #Se va a hacer uso de pygame para programar el juego
import os #Esta libreria se usa para obtener las imagenes del sistema operativo 
import tkinter as tk
import FuncionesArturo
import FuncionesMariana
from threading import Thread
import time

from FuncionesArturo import Board


global run 
global WIN
run = True


FPS = 10
WIN = None


from FuncionesArturo import WIDTH, HEIGHT 

def RunGame(User, CantBoats, Matrix):
    global WIN
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    
    
    main()



    
    
Cursor = pygame.image.load(os.path.join("Images", "Cursor.png"))


def draw_window(cursor):
    # WIN.fill((17,114,169))
    
    
    board = Board()
    pygame.display.set_caption("Battleship")
    
    
    
    board.draw(WIN)
    board.draw_enemy(WIN)
    

    WIN.blit(Cursor, (cursor.x, cursor.y))
    
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a]:
        if cursor.x != 750:
            cursor.x -= 70
    if keys_pressed[pygame.K_d]:
        if cursor.x != 1380:
            cursor.x += 70
    if keys_pressed[pygame.K_w]:
        if cursor.y != 0:
            cursor.y -= 70
    if keys_pressed[pygame.K_s]:
        if cursor.y != 630:
            cursor.y += 70
    if keys_pressed[pygame.K_q]:
        print(cursor.x, cursor.y)
        
    pygame.display.update()


    
def main():
    #Se define el cubo 
    cursor = pygame.Rect(750, 70, 70, 70)
    
    
    
    global run
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN: #Cambiar esto por la idea en WASD con la casilla que selecciona
                pass
            
        
        draw_window(cursor)
        
        

    
    
    pygame.quit()


