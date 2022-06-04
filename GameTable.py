"""
Segundo proyecto taller de Programacion
Rojas Rojas Mariana 
Acuña Duran Oscar
"""

import pygame #Se va a hacer uso de pygame para programar el juego
import os #Esta libreria se usa para obtener las imagenes del sistema operativo 



WIN = pygame.display.set_mode((1600, 800))
FPS = 60

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    
    pygame.quit()

if __name__ == "__main__":
    main()
