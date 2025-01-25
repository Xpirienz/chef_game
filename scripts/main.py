import pygame
from random import randint

pygame.init()

pantalla = pygame.display.set_mode((800,600))
pygame.display.set_caption('colisión')

rectangulo = pygame.Rect(0,0,25,25)

obstaculos = []
for _ in range(16):
    obstaculo = pygame.Rect(randint(0,700),randint(0,500),25,25)
    obstaculos.append(obstaculo)




pygame.mouse.set_visible(False)


run = True

while run:
    pantalla.fill((64,64,64))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    col = 'GREEN'

   
    if rectangulo.collidelist(obstaculos) >= 0:
        col = 'RED'

    pos = pygame.mouse.get_pos()
    rectangulo.center = pos
    pygame.draw.rect(pantalla,col,rectangulo)
    for obstaculo in obstaculos:
        pygame.draw.rect(pantalla,'BLUE', obstaculo)

    pygame.display.flip()
