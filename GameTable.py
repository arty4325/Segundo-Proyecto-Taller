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

import pyfirmata
import keyboard
import time

pygame.mixer.init()
# if you want to use this module.
pygame.mixer.music.load('morse-code-alphabet.ogg')
pygame.mixer.music.play()

ProtoBoard = pyfirmata.Arduino('COM4')   #Se establece cual es el pin en el cual esta funcionando el arduino 

it = pyfirmata.util.Iterator(ProtoBoard) #Se itera en la lectura del arduino 
it.start()

#Se le da una variable al funcionamiento de cada pin 
w_pin=ProtoBoard.get_pin('d:10:i') 
a_pin=ProtoBoard.get_pin('d:8:i')
s_pin=ProtoBoard.get_pin('d:11:i')
d_pin=ProtoBoard.get_pin('d:9:i')
e_pin=ProtoBoard.get_pin('d:13:i')
q_pin=ProtoBoard.get_pin('d:12:i')

def TurnOnLight(pin, board): #Se crea una funcion que prende la luz led por un segundo dada la indicacion de un pin en el arduino
    board.digital[pin].write(1)
    time.sleep(1)
    board.digital[pin].write(0)


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


def RunGame(TheUser, CBoats, Matrix, Bool): #Esta funcion se encarga de correr el Pygame tras haber puesto los inputs en tkinter
    global ImPlaying 
    if Bool == False:
        ImPlaying = True
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
    """
            Instituto Tecnológico de Costa Rica
                Ingenieria en Computadores
    Nombre: Check_Rotated()
    Lenguaje: Python 3.8.0
    Autor: Oscar Acuña Durán(2022049304), Mariana Saray Rojas Rojas (2020076936)
    Version: 1.0
    Fecha de última modificación: Junio 16/ 2022
    Entradas: No tiene entradas
    Restricciones: No tiene restricciones 
    Salidas: Indica en una variable global si el bote ha rotado o no 
    """
    global Barco2, Barco3, Barco4
    global barco2, barco3, barco4
    global WhichBoat
    global HaveRotated
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_e]: #La tecla e es la que se utiliza para rotar el bote
        if WhichBoat == Barco4: 
            HaveRotated = not HaveRotated
            Barco4 = pygame.transform.rotate(Barco4, 270) #Se rota un bote de tamaño 4
        if WhichBoat == Barco3:
            HaveRotated = not HaveRotated
            Barco3 = pygame.transform.rotate(Barco3, 270) #Se rota un bote de tamaño 3
        if WhichBoat == Barco2:
            HaveRotated = not HaveRotated
            Barco2 = pygame.transform.rotate(Barco2, 270) #Se rota un bote de tamaño 2
         
        
    time.sleep(0.1)
    Check_Rotated()

def draw_boats(barco2, barco3, barco4, selected): 
    """
            Instituto Tecnológico de Costa Rica
                Ingenieria en Computadores
    Nombre: CreateBoards(Bool, User, Boats)
    Lenguaje: Python 3.8.0
    Autor: Oscar Acuña Durán(2022049304), Mariana Saray Rojas Rojas (2020076936)
    Version: 1.0
    Fecha de última modificación: Junio 16/ 2022
    Entradas: barco2, barco3, barco4, son variables que permiten obtejer las coordenadas de los barcos en el eje x y y
    selected es el barco que se selecciono 
    Restricciones: Estas tienen que ser variables propias de pygame que permitan el movimiento de los barcos 
    Salidas: Dibuja los barcos en el tablero 
    """
    global HaveRotated
    global Barco2, Barco3, Barco4
    global WhichBoat
    global board 
    global NotPlaying, CantBoats
    global ImPlaying
    
    WIN.blit(Barco2, (barco2.x, barco2.y)) #Se coloca el barco 2 en la pantalla
    WIN.blit(Barco3, (barco3.x, barco3.y)) #Se coloca el barco 3 en la pantalla
    WIN.blit(Barco4, (barco4.x, barco4.y)) #Se coloca el barco 4 en la pantalla 
    
    if selected == barco2: #Se establece en la variable WhichBoat cual es el barco que se coloco 
        WhichBoat = Barco2
    if selected == barco3:
        WhichBoat = Barco3
    if selected == barco4:
        WhichBoat = Barco4
        
    keys_pressed = pygame.key.get_pressed() #Esto se utiliza para poder leer varias teclas al mismo tiempo en pygame
    if keys_pressed[pygame.K_a]: #Si se estripa a se mueve a la izquierda 
        if selected.x != 750:
            selected.x -= 70
    if keys_pressed[pygame.K_d]: #si s estripa d se mueve a la derecha 
        if selected.x != 1380:
            selected.x += 70 
    if keys_pressed[pygame.K_w]: #Si se estripa w se mueve hacia arriba
        if selected.y != 0:
            selected.y -= 70
    if keys_pressed[pygame.K_s]: #Si se estripa s se mueve hacia abajo 
        if selected.y != 630:
            selected.y += 70
            

    
    if keys_pressed[pygame.K_q]: #La tecla q se utiliza para poder dibujar el barco

        board.draw_boat((selected.x - 750)//70, (selected.y%750)//70, WIN)  #Se dibuja en el punto de pivote 
        if selected == barco2: #Dependiendo del barco que se selecciono y si ha rotado o no, se dibuja en la pantalla
            if HaveRotated:
                Var = selected.y
                while Var != selected.y + 70:
                    Var += 70
                    board.draw_boat((selected.x - 750)//70, (Var%750)//70, WIN)
                CantBoats[2] -= 1
            else:
                Var = selected.x
                while Var != selected.x + 70:
                    Var += 70
                    board.draw_boat((Var - 750)//70, (selected.y%750)//70, WIN)
                CantBoats[2] -= 1
        if selected == barco3:
            if HaveRotated:
                Var = selected.y
                while Var != selected.y + 140:
                    Var += 70
                    board.draw_boat((selected.x - 750)//70, (Var%750)//70, WIN)
                CantBoats[1] -= 1
            else:
                Var = selected.x
                while Var != selected.x + 140:
                    Var += 70
                    board.draw_boat((Var - 750)//70, (selected.y%750)//70, WIN)
                CantBoats[1] -= 1
        if selected == barco4:
            if HaveRotated:
                Var = selected.y
                while Var != selected.y + 210:
                    Var += 70
                    board.draw_boat((selected.x - 750)//70, (Var%750)//70, WIN)
                CantBoats[0] -= 1
            else:
                Var = selected.x
                while Var != selected.x + 210:
                    Var += 70
                    board.draw_boat((Var - 750)//70, (selected.y%750)//70, WIN)
                CantBoats[0] -= 1
        if CantBoats[0] == 0 and CantBoats[1] == 0 and CantBoats[2] == 0: #Cuando ya no quedan barcos, comienza el juego 
             ImPlaying = True
        
    pygame.display.update()
    
    
    
    


def draw_window():
    global board
    board = Board()
    pygame.display.set_caption("Battleship")

    board.draw(WIN) #En esta funcion se ejecuta la clase que esta encargada de dibujar el tablero y a los enemios
    board.draw_enemy(WIN)
    board.make_enemys(WIN)
    board.draw_on_enemyboard(WIN)
    pygame.display.update()


def Play_Game(cursor):
    """
            Instituto Tecnológico de Costa Rica
                Ingenieria en Computadores
    Nombre: Play_Game(cursor)
    Lenguaje: Python 3.8.0
    Autor: Oscar Acuña Durán(2022049304), Mariana Saray Rojas Rojas (2020076936)
    Version: 1.0
    Fecha de última modificación: Junio 16/ 2022
    Entradas: cursor, es el "mouse" que se utiliza en el juego 
    Restricciones: cursor tiene que ser la varibable de pygame que permite mover la imagen
    Salidas: Mueve el cursor del juego y selecciona casillas en la pantalla
    """
    global ImPlaying #Esta variable dicta si yo estoy jugando o si esta jugando mi enemigo
    global run
    global User
    WIN.blit(Cursor, (cursor.x, cursor.y)) #Se coloca el cursor en la pantalla
    
    
    keys_pressed = pygame.key.get_pressed() #Se comienza a detectar si se estripan teclas del tecaldo 
    if ImPlaying: #Esto se ejecuta si es mi turno de jugar 
        if keys_pressed[pygame.K_a]: #Movimiento hacia la izquierda
            if cursor.x != 750: #Restriccion de este movimiento
                cursor.x -= 70 
        if keys_pressed[pygame.K_d]: #Movimiento hacia la derecha
            if cursor.x != 1380: #Restriccion de este movimiento 
                cursor.x += 70
        if keys_pressed[pygame.K_w]: #Movimiento hacia arriba 
            if cursor.y != 0: #Restriccion de este movimiento 
                cursor.y -= 70
        if keys_pressed[pygame.K_s]: #Movimiento hacia abajo  
            if cursor.y != 630: #Restriccion de este movimiento
                cursor.y += 70
        if keys_pressed[pygame.K_q]: #Esto quiere decir qeu se selecciono una casilla en el tablero 
            val = board.return_what_i_selected((cursor.x - 750)//70, (cursor.y%750)//70) #valor que hay en lsa coordenadas de esa casilla 
            #En el tablero enemgio 
            if val == 0:  #Esto quiere decir que en la casilla que se seelecciono, no habia nada 
                Thread(target = TurnOnLight, args = (2, ProtoBoard, )).start() #Se enciende la primera luz led del control
            if val == 1: #Esto quiere decir que habia un bote en la casilla que se selecciono 
                Thread(target = TurnOnLight, args = (3, ProtoBoard, )).start() #Se enciende la segunda luz del control
            if val == 0 or val == 1: #Se indica en la matiz que es lo que paso, si habia un bote se pone un 3 en la 
                #matriz, y si no habia uno, se coloca un 2
                board.draw_selected_notkilled_boat((cursor.x - 750)//70, (cursor.y%750)//70, WIN) #indicacion y escritura en la matriz 
            HaveIWon, HaveEnemyWon = FuncionesArturo.check_the_board() #Revisa si el jugador ya gano o si el enemigo gano 
            if HaveIWon: #Si el jugador gano 
                Top10 = FuncionesArturo.build_podium(User)[1][0:9] #Se revisa si esta en el ranking 
                if User in Top10: #Si esta en el ranking 
                    Thread(target = TurnOnLight, args = (5, ProtoBoard, )).start() #Se enciende la ultima luz led del control
                Thread(target = TurnOnLight, args = (4, ProtoBoard, )).start() #Se enciende la tercera luz del control led
            
            if HaveIWon or HaveEnemyWon: #Cuando el jugador o el enemigo ganaron
                run = False #Se cierra el juego 
                
            if val == 0: #Si la casilla que selecciona el jugador no tiene bote entonces se le cede el turno al enemigo 
                ImPlaying = False
    if ImPlaying == False: #Juega el enemigo 
        board.random_enemy(WIN) #Escoje una casilla arbitraria del tablero del jugador
        
        HaveIWon, HaveEnemyWon = FuncionesArturo.check_the_board() #Revisa la condicion de la partida 
        
        if HaveIWon or HaveEnemyWon: #Si alguien ya gano, solamente cierra el jeugo 
            run = False 
        
        ImPlaying = True #Le cede el turno a el otro jugador 
        
    pygame.display.update() #Se tiene que actualizar la pantalla de pygame 



def main():
    global ImPlaying
    global HaveRotated
    global selected
    global barco2, barco3, barco4
    global NotPlaying
    global CantBoats
    global run
    Thread(target = Check_Rotated, args = ()).start()
    cursor = pygame.Rect(750, 70, 70, 70)   #Posicion inicial del cursor 
    barco2 = pygame.Rect(750, -280, 140, 70)#Posicion inicial del barco2
    barco3 = pygame.Rect(750, -280, 210, 70)#Posicion Iniicial del barco3
    barco4 = pygame.Rect(750, -280, 280, 70)#Posicion Inicial del barco4      
    global run
    clock = pygame.time.Clock()
    while run:
        time.sleep(0.1)
        
        d = d_pin.read() #Se leen los pines del arduino 
        s = s_pin.read()
        a = a_pin.read()
        w = w_pin.read()
        e = e_pin.read()
        q = q_pin.read()
        
        
        if w == True: #Dependiendo del pin que se lea, se presiona una tecla en el teclado 
            keyboard.press("w")
        elif w == False:
            keyboard.release("w")
        
        if a == True:
            keyboard.press("a")
        elif a == False:
            keyboard.release("a")
        
        if s == True:
            keyboard.press("s")
        elif s == False:
            keyboard.release("s")
        
        if d == True:
            keyboard.press("d")
        elif d == False:
            keyboard.release("d")
            
        if q == True:
            keyboard.press("q")
        elif q == False:
            keyboard.release("q")
            
        if e == True:
            keyboard.press("e")
        elif e == False:
            keyboard.release("e")
        
        clock.tick(FPS) #Se corre el jeugo en la cantidad de frames per second predeterminada 
        
        if NotPlaying and (CantBoats[0] != 0 or CantBoats[1] != 0 or CantBoats[2] != 0): #Si aun quedan barcos 
            if CantBoats[0] != 0: #Si no quedan barcos de tipo 4
                if selected is not barco4: #Si el que esta seleccionado no es el barco 4
                    cursor = pygame.Rect(750, 70, 70, 70)
                    barco4 = pygame.Rect(750, 140, 280, 70) #Este se coloca en la posicion inicial 
                    HaveRotated = False 
                selected = barco4
            elif CantBoats[1] != 0: # Si no quedan barcos de tipo 3
                if selected is not barco3:
                    cursor = pygame.Rect(750, 70, 70, 70)
                    barco3 = pygame.Rect(750, 140, 280, 70) #Este se coloca en la posicion inicial 
                    HaveRotated = False
                selected = barco3

            elif CantBoats[2] != 0: #Si el qeu se selecciono no es de tipo 2
                 if selected is not barco2:
                    cursor = pygame.Rect(750, 70, 70, 70)
                    barco2 = pygame.Rect(750, 140, 280, 70) #Este se coloca en la posicion inciial 
                    HaveRotated = False
                 selected = barco2

            else:
                NotPlaying = False #Si no quedan barcos del todo, se tiene que comenzar el juego 
                
                
        if CantBoats[0] == 0:
            barco4 = pygame.Rect(750, -280, 280, 70)
        if CantBoats[1] == 0:
            barco3 = pygame.Rect(750, -280, 210, 70)
        if CantBoats[2] == 0:
            barco2 = pygame.Rect(750, -280, 280, 70)
            NotPlaying = False

        for event in pygame.event.get(): #Se detectan los eventos que han pasado en el jeugo 
            if event.type == pygame.QUIT: #Si se cierra la ventana de tkinter
                run = False #Se cierra el juego 
                FuncionesArturo.SafeBoards(User) #Se guarda el estado de la matriz en el archivo txt
            if event.type == pygame.MOUSEBUTTONDOWN: 
                pass
            
        
        draw_window() 
        if NotPlaying: #si aun no se esta jugando se ejecuta la funcion draw_boats
            draw_boats(barco2, barco3, barco4, selected)
        if not NotPlaying: #Si ya se esta jugando se ejecuta la funcion play_game
            Play_Game(cursor)

        
        
        

    
    
    pygame.quit()


