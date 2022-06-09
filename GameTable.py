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
global HaveRotated
global selected
selected = None
HaveRotated = False
run = True


FPS = 10
WIN = None


from FuncionesArturo import WIDTH, HEIGHT 

def RunGame(TheUser, CantBoats, Matrix):
    global User
    User = TheUser
    global WIN
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    
    
    main()



    
    
Cursor = pygame.image.load(os.path.join("Images", "Cursor.png"))
global Barco2, Barco3, Barco4
Barco2 = pygame.image.load(os.path.join("Images", "Barco2.png"))
Barco3 = pygame.image.load(os.path.join("Images", "Barco3.png"))
Barco4 = pygame.image.load(os.path.join("Images", "Barco4.png"))

def Check_Rotated():
    global HaveRotated 
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_e]:
        Rotate_Boat()
        HaveRotated = not HaveRotated
    time.sleep(0.1)
    Check_Rotated()

def Rotate_Boat():
    global barco2, barco3, barco4
    global Barco2, Barco3, Barco4
    global HaveRotated 
    global WhichBoat
    global selected
    
    if HaveRotated:
        if WhichBoat == Barco4:
            Barco4 = pygame.transform.rotate(Barco4, 270)
    else:
        WhichBoat = pygame.transform.rotate(WhichBoat, 90)
    
    

def draw_boats(barco2, barco3, barco4, selected):
    global HaveRotated
    global Barco2, Barco3, Barco4
    global WhichBoat
    WIN.blit(Barco2, (barco2.x, barco2.y))
    WIN.blit(Barco3, (barco3.x, barco3.y))
    WIN.blit(Barco4, (barco4.x, barco4.y))
    if selected == barco2:
        WhichBoat = Barco2
    if selected == barco3:
        WhichBoat = Barco3
    if selected == barco4:
        WhichBoat = Barco4

        
    if selected == barco2:
        print(selected.x + 210, selected.y)
    
    #print(selected.x, selected.y)
    
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a]:
        if selected.x != 750:
            selected.x -= 70
    if keys_pressed[pygame.K_d]:
        if selected.x != 1380:
            selected.x += 70
    if keys_pressed[pygame.K_w]:
        if selected.y != 0:
            selected.y -= 70
    if keys_pressed[pygame.K_s]:
        if selected.y != 630:
            selected.y += 70
    #if keys_pressed[pygame.K_e]:
        
    pygame.display.update()
    
    
    
    


def draw_window(cursor):
    # WIN.fill((17,114,169))
   
    board = Board()
    pygame.display.set_caption("Battleship")

    board.draw(WIN)
    board.draw_enemy(WIN)
    board.make_enemys(WIN)

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
    #if keys_pressed[pygame.K_q]:
        #print(cursor.x, cursor.y) #la idea es que esto modifique la matriz cuando se selecciona
    #    board.draw_boat((cursor.x - 750)//70, (cursor.y%750)//70, WIN)
    #if keys_pressed[pygame.K_e]:
        
        
    pygame.display.update()


    
def main():
    #Se define el cubo 
    global HaveRotated
    global selected
    global barco2, barco3, barco4
    Thread(target = Check_Rotated, args = ()).start()
    cursor = pygame.Rect(750, -70, 70, 70)
    barco2 = pygame.Rect(750, -70, 140, 70)
    barco3 = pygame.Rect(750, -70, 210, 70)
    barco4 = pygame.Rect(750, -70, 280, 70)
    selected = barco4
    
    
    global run
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                FuncionesArturo.SafeBoards(User)
            if event.type == pygame.MOUSEBUTTONDOWN: #Cambiar esto por la idea en WASD con la casilla que selecciona
                pass
            
        
        draw_window(cursor)
        draw_boats(barco2, barco3, barco4, selected)
        print(HaveRotated)
        
        
        

    
    
    pygame.quit()


