import pygame
import sys
import random 
pygame.init()


clock = pygame.time.Clock()

screen = pygame.display.set_mode((400, 400))
skysurf = pygame.Surface((400,400))
skyrect = skysurf.get_rect(topleft = (0,0))
skysurf.fill('blue')

groundsurf = pygame.Surface((400, 100))
groundrect = groundsurf.get_rect(topleft = (0, 300))
groundsurf.fill('green')

woodsurf = pygame.Surface((30, 50))
woodrect = woodsurf.get_rect(topleft = (70, 250))
woodsurf.fill('brown')

leavessurf = pygame.Surface((90, 40))
leavesrect = leavessurf.get_rect(topleft = (40, 225))
leavessurf.fill('green')

sunsurf = pygame.Surface((60, 60))
sunrect = sunsurf.get_rect(topleft = (320, 50))
sunsurf.fill('yellow')

playersurf = pygame.Surface((30, 50))
playerrect = playersurf.get_rect(topleft = (0,100))
playersurf.fill('red')

punterosurf = pygame.Surface((20,20))
punterorect = punterosurf.get_rect(midtop = (0,0))
punterosurf.fill('purple')

    
def gravedad_jugador(playerspeedY):
    playerspeedY = 4
    if playerrect.colliderect(groundrect):
        playerspeedY = 0
    playerrect.y += playerspeedY


        
    
def playermovement(button_press):
    button_press = pygame.key.get_pressed()
    if button_press[pygame.K_d]:
        playerrect.x += 2
    elif button_press[pygame.K_a]:
        playerrect.x -= 2
    elif button_press[pygame.K_w] and playerrect.colliderect(groundrect):
        playerrect.y -= 50 

    
def salida ():
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
while True:
    gravedad_jugador(0)
    playermovement(0)
    screen.blit(skysurf, skyrect)    
    screen.blit(groundsurf, groundrect)
    screen.blit(woodsurf, woodrect)
    screen.blit(leavessurf, leavesrect)
    screen.blit(sunsurf, sunrect)
    screen.blit(playersurf, playerrect)
    screen.blit(punterosurf,pygame.mouse.get_pos())
    salida()
    
    if punterorect.collidepoint():
        if pygame.mouse.get_pressed:
            print('collision')
    
    clock.tick(30)
    pygame.display.update()