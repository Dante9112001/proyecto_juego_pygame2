import pygame
#traer un archivo con codigo hacia otro archivo
from sys import exit

import random

import time



time.time()
pygame.init()# inicializar las funciones de la libreria pygame 



clock = pygame.time.Clock()


#screen = pygame.display.set_mode((1360,768))
screen = pygame.display.set_mode((1360, 400))

#VARIABLES QUE VAN A CAMBIAR SU VALOR
if True:   
    speed = 1.5
    
    main_font = pygame.font.Font(None, 30)
    
    speeddown = pygame.Surface((64, 40))
    speeddown.fill('green')
    speed_down_rect = speeddown.get_rect(topleft = (1216,40))

    speedup =pygame.Surface((64, 40))
    speedup.fill('green')
    speed_up_rect = speedup.get_rect(topleft = (1290,40))

    objective = pygame.Surface((40 ,40))
    objective.fill('red')
    objectiverect = objective.get_rect(midleft = (0, 0))

    sky_surf = pygame.Surface((1366,768))
    sky_surf.fill('white')
    skyrect = sky_surf.get_rect(topleft = (0,0))

    numery = random.randrange(1,100)
    numerx= random.randrange(1,100)
#FUNCION PARA PODER SALIR DEL JUEGO
def salida():
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

while True:
    clock.tick(speed)
#LAS CAPAS DE TEXTO(COLOCADAS AQUI PARA QUE SE ACTUALISEN CONSTANTEMENTE)
    textsurf = main_font.render(f"la velocidad es: {speed}", True, 'black' )
    textrect = textsurf.get_rect(topleft = (1165, 0)) 


    
#SCREEN BLITS
    if True:    
        screen.blit(sky_surf, skyrect)
        screen.blit(objective, objectiverect)
        screen.blit(textsurf, textrect )
        screen.blit(speedup, speed_up_rect)
        screen.blit(speeddown, speed_down_rect)

 
    if timer == 0:
        timer = time.sleep(1)
        numery = random.randrange(1,768)
        numerx = random.randrange(1,1366)    
        objectiverect.top = numery
        objectiverect.left = numerx
    
    salida()
  
    pygame.display.update() 
#compañero proyecto
#8292029181
#clickcode 