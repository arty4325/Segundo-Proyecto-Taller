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

from FuncionesArturo import Board


global run 
global WIN
run = True


FPS = 60
WIN = None


from FuncionesArturo import WIDTH, HEIGHT 


def RunGame(User, CantBoats, Matrix):
    global WIN
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    main()


def draw_window():
    # WIN.fill((17,114,169))
    
    board = Board()


    
    pygame.display.set_caption("Battleship")
    

    board.draw(WIN)
    board.draw_enemy(WIN)

    
    
    pygame.display.update()
    
    
def main():
    global run
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN: #Cambiar esto por la idea en WASD con la casilla que selecciona
                pass 

            
        draw_window()

    
    
    pygame.quit()


