import pygame
from sys import exit

pygame.init()
#Screen
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
height, width = screen.get_size()

#Font and colors
font = pygame.font.Font('fonts\Pixeltype.ttf',90)

black = (23, 32, 42)
white = (253, 254, 254)


#Background
surface_load_background = pygame.image.load('graphics/background.jpg')
surface_background = pygame.transform.scale(surface_load_background,(height, width))
rect_background = surface_background.get_rect(midbottom = (height//2, width))

#Title text
surface_load_title = pygame.image.load('graphics/title.png')
surface_title = pygame.transform.scale(surface_load_title,(height//1.5,width//1.5))
rect_title = surface_title.get_rect(center = (height//2,width//3))

#Play
surface_play = font.render('Play', False, white)
rect_play = surface_play.get_rect(center = (height//2,width//1.4))

#Exit
surface_exit = font.render('Exit', False, white)
rect_exit = surface_exit.get_rect(center = (height//2, width//1.2))


while True:
    #Loop events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rect_exit.collidepoint(event.pos):
                    pygame.quit()
                    exit()
                if rect_play.collidepoint(event.pos):
                    print('JUGANDO')
        
    #Background
    screen.blit(surface_background, rect_background)

    #Title
    screen.blit(surface_title, rect_title)

    #Text
    screen.blit(surface_play, rect_play)
    screen.blit(surface_exit, rect_exit)

    #Button mouse motion animation
    mouse_pos = pygame.mouse.get_pos()
    if rect_play.collidepoint(mouse_pos):pygame.draw.line(screen,white, (rect_play.left, rect_play.bottom),(rect_play.right, rect_play.bottom), 4)
    if rect_exit.collidepoint(mouse_pos):pygame.draw.line(screen,white, (rect_exit.left, rect_exit.bottom - 10),(rect_exit.right, rect_exit.bottom -10), 4)


    pygame.display.update()
    clock.tick(60)
