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
global NotPlaying
NotPlaying = True
selected = None
HaveRotated = False
run = True


FPS = 10
WIN = None


from FuncionesArturo import WIDTH, HEIGHT 

def RunGame(TheUser, CBoats, Matrix):
    global User
    User = TheUser
    global CantBoats
    CantBoats = CBoats
    global WIN
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    
    
    main()



    
    
Cursor = pygame.image.load(os.path.join("Images", "Cursor.png"))
global Barco2, Barco3, Barco4
Barco2 = pygame.image.load(os.path.join("Images", "Barco2.png"))
Barco3 = pygame.image.load(os.path.join("Images", "Barco3.png"))
Barco4 = pygame.image.load(os.path.join("Images", "Barco4.png"))

def Check_Rotated():
    global Barco2, Barco3, Barco4
    global barco2, barco3, barco4
    global WhichBoat
    global HaveRotated
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_e]:
        if WhichBoat == Barco4:
            HaveRotated = not HaveRotated
            Barco4 = pygame.transform.rotate(Barco4, 270)
        if WhichBoat == Barco3:
            HaveRotated = not HaveRotated
            Barco3 = pygame.transform.rotate(Barco3, 270)
        if WhichBoat == Barco2:
            HaveRotated = not HaveRotated
            Barco2 = pygame.transform.rotate(Barco2, 270)
        
        
    time.sleep(0.1)
    Check_Rotated()


 
    
#if keys_pressed[pygame.K_q]:
#print(cursor.x, cursor.y) #la idea es que esto modifique la matriz cuando se selecciona
#    board.draw_boat((cursor.x - 750)//70, (cursor.y%750)//70, WIN)
#if keys_pressed[pygame.K_e]:

def draw_boats(barco2, barco3, barco4, selected):
    global HaveRotated
    global Barco2, Barco3, Barco4
    global WhichBoat
    global board 
    global NotPlaying, CantBoats
    WIN.blit(Barco2, (barco2.x, barco2.y))
    WIN.blit(Barco3, (barco3.x, barco3.y))
    WIN.blit(Barco4, (barco4.x, barco4.y))
    if selected == barco2:
        WhichBoat = Barco2
    if selected == barco3:
        WhichBoat = Barco3
    if selected == barco4:
        WhichBoat = Barco4

    """ 
    if selected == barco2:
        print(selected.x + 210, selected.y)
    """
    
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
            
            
    #En esta parte falta hacer una serie de validaciones, en concreto se tiene que revisar que las fichas no se estan 
    #Colocando encima de otras 
    #Eso se hara posteriormente
    if keys_pressed[pygame.K_q]:
        #print(selected.x, selected.y)
        board.draw_boat((selected.x - 750)//70, (selected.y%750)//70, WIN)
        if selected == barco2:
            #print("yes")
            if HaveRotated:
                Var = selected.y
                while Var != selected.y + 70:
                    Var += 70
                    board.draw_boat((selected.x - 750)//70, (Var%750)//70, WIN)
                    #print(Var)
                CantBoats[2] -= 1
            else:
                Var = selected.x
                while Var != selected.x + 70:
                    Var += 70
                    board.draw_boat((Var - 750)//70, (selected.y%750)//70, WIN)
                    #print(Var)
                CantBoats[2] -= 1
        if selected == barco3:
            #print("yes")
            if HaveRotated:
                Var = selected.y
                while Var != selected.y + 140:
                    Var += 70
                    board.draw_boat((selected.x - 750)//70, (Var%750)//70, WIN)
                    #print(Var)
                CantBoats[1] -= 1
            else:
                Var = selected.x
                while Var != selected.x + 140:
                    Var += 70
                    board.draw_boat((Var - 750)//70, (selected.y%750)//70, WIN)
                    #print(Var)
                CantBoats[1] -= 1
        if selected == barco4:
            #print("yes")
            if HaveRotated:
                Var = selected.y
                while Var != selected.y + 210:
                    Var += 70
                    board.draw_boat((selected.x - 750)//70, (Var%750)//70, WIN)
                    #print(Var)
                CantBoats[0] -= 1
            else:
                Var = selected.x
                while Var != selected.x + 210:
                    Var += 70
                    board.draw_boat((Var - 750)//70, (selected.y%750)//70, WIN)
                    #print(Var)
                CantBoats[0] -= 1
                
        
    pygame.display.update()
    
    
    
    


def draw_window(cursor):
    # WIN.fill((17,114,169))
    global board
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
    global NotPlaying
    global CantBoats
    Thread(target = Check_Rotated, args = ()).start()
    cursor = pygame.Rect(750, 70, 70, 70)
    barco2 = pygame.Rect(750, -280, 140, 70)
    barco3 = pygame.Rect(750, -280, 210, 70)
    barco4 = pygame.Rect(750, -280, 280, 70)
    #selected = barco2
    

            
            
    global run
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        if NotPlaying and (CantBoats[0] != 0 or CantBoats[1] != 0 or CantBoats[2] != 0):
            if CantBoats[0] != 0:
                if selected is not barco4:
                    cursor = pygame.Rect(750, 70, 70, 70)
                    barco4 = pygame.Rect(750, 140, 280, 70)
                    HaveRotated = False
                selected = barco4
            elif CantBoats[1] != 0:
                if selected is not barco3:
                    cursor = pygame.Rect(750, 70, 70, 70)
                    barco3 = pygame.Rect(750, 140, 280, 70)
                    HaveRotated = False
                selected = barco3

            elif CantBoats[2] != 0:
                if selected is not barco2:
                    cursor = pygame.Rect(750, 70, 70, 70)
                    barco2 = pygame.Rect(750, 140, 280, 70)
                    HaveRotated = False
                selected = barco2

            else:
                NotPlaying = False
                
        if CantBoats[0] == 0:
            barco4 = pygame.Rect(750, -280, 280, 70)
        if CantBoats[1] == 0:
            barco3 = pygame.Rect(750, -280, 210, 70)
        if CantBoats[2] == 0:
            barco2 = pygame.Rect(750, -280, 280, 70)
            NotPlaying = False
        
        
        #print(CantBoats)
        
        # Ahora se quiere hacer un if para cuando is playing de la vara
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                FuncionesArturo.SafeBoards(User)
            if event.type == pygame.MOUSEBUTTONDOWN: #Cambiar esto por la idea en WASD con la casilla que selecciona
                pass
            
        
        draw_window(cursor)
        if NotPlaying:
            draw_boats(barco2, barco3, barco4, selected)

        
        
        

    
    
    pygame.quit()


