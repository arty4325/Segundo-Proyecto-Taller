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

global run 
global WIN
run = True


FPS = 60
WIN = None


def RunGame(User, CantBoats, Matrix):
    global WIN
    WIN = pygame.display.set_mode((1450, 700))
    main()


def draw_window():
    WIN.fill((17,114,169))
    pygame.display.update()
    


def main():
    global run
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    
    
    pygame.quit()


