import pygame
from sys import exit

#######################################################--SCREEN--#################################################################
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
height, width = screen.get_size()
##############################################---MENU AND TUTO FILES---############################################################
#Font and colors
font = pygame.font.Font('fonts\Concrete.ttf',90)
black = (23, 32, 42)
white = (253, 254, 254)

#Sound effects
menu_sound = pygame.mixer.Sound("effects\menusound.wav")

#Backgrounds

surface_load_background = pygame.image.load('graphics/background.png')
surface_background = pygame.transform.scale(surface_load_background,(height, width))
rect_background = surface_background.get_rect(bottomright = (height, width))

surface_load_backgroundt = pygame.image.load('graphics/background_tuto.png')
surface_backgroundt = pygame.transform.scale(surface_load_backgroundt,(height,width))
rect_backgroundt = surface_backgroundt.get_rect(bottomright =(height, width))


#Title text
surface_load_title = pygame.image.load('graphics/title.png')
surface_title = pygame.transform.smoothscale(surface_load_title,(height//1.5,width//1.5))
rect_title = surface_title.get_rect(center = (height//2,width//3))

#Play
surface_play = font.render('Play', True, white)
rect_play = surface_play.get_rect(center = (height//2,width//1.4))

#Exit
surface_exit = font.render('Exit', True, white)
rect_exit = surface_exit.get_rect(center = (height//2, width//1.2))

#Continue
surface_continue = font.render('continue', True, white)
rect_continue = surface_continue.get_rect(center = (height//1.2, width//1.2))


surface_fly = pygame.image.load('graphics\Fly1.png')
fly_rect = surface_fly.get_rect(center =(height//2,width//2))


#Flag switches 
sound_played_play = False
sound_played_exit = False
sound_played_continue = False
arrastre = False
##################################################################################################################################

#-------------------------------------------------------------MENU---------------------------------------------------------------#
def master_menu():
    #Import global variables
    global sound_played_exit,sound_played_play

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
                        tutorial_screen()

        #Background
        screen.blit(surface_background, rect_background)

        #Title
        screen.blit(surface_title, rect_title)

        #Text
        screen.blit(surface_play, rect_play)
        screen.blit(surface_exit, rect_exit)

        #Button mouse motion animation with sound effect
        mouse_pos = pygame.mouse.get_pos()

        if rect_play.collidepoint(mouse_pos):
            pygame.draw.line(screen,white, (rect_play.left, rect_play.bottom +10 ),(rect_play.right, rect_play.bottom +10), 7)
            if not sound_played_play:  
                menu_sound.play()
                sound_played_play = True
        else:
            sound_played_play = False
        
        if rect_exit.collidepoint(mouse_pos):
            pygame.draw.line(screen,white, (rect_exit.left, rect_exit.bottom - 5),(rect_exit.right, rect_exit.bottom -5), 7)
            if not sound_played_exit:  
                menu_sound.play()
                sound_played_exit = True
        else:
            sound_played_exit = False
            
        pygame.display.update()
        clock.tick(60)
#--------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------TUTO---------------------------------------------------------------#
def tutorial_screen():
    #Loop events
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rect_continue.collidepoint(event.pos):
                        game_running()
            
        #Background(menu info options)
        screen.blit(surface_backgroundt,rect_background)
        
        #Continue
        screen.blit(surface_continue, rect_continue)

        #Button mouse motion animation with sound effects
        mouse_pos = pygame.mouse.get_pos()

        if rect_continue.collidepoint(mouse_pos):
            pygame.draw.line(screen,white, (rect_continue.left, rect_continue.bottom - 5),(rect_continue.right, rect_continue.bottom -5), 7)
            if not sound_played_exit:  
                menu_sound.play()
                sound_played_exit = True
        else:
            sound_played_exit = False

        pygame.display.update()
        clock.tick(60)
#--------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------GAME---------------------------------------------------------------#
def game_running():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if fly_rect.collidepoint(event.pos):
                    arrastre = True
                    offset_x = event.pos[0] - fly_rect.x
                    offset_y = event.pos[1] - fly_rect.y
            if event.type == pygame.MOUSEBUTTONUP:
                arrastre = False
            if event.type == pygame.MOUSEMOTION and arrastre:
                 fly_rect.x = event.pos[0] - offset_x
                 fly_rect.y = event.pos[1] - offset_y
                 
        screen.fill('White')
        screen.blit(surface_fly,fly_rect)


        pygame.display.update()
        clock.tick(60)
#--------------------------------------------------------------------------------------------------------------------------------#

master_menu()