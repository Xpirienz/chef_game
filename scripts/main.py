import pygame
from sys import exit
#Julisss
#######################################################--SCREEN--#################################################################
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
height, width = screen.get_size()
##############################################---MENU AND TUTO FILES---############################################################
#Font and colors
font = pygame.font.Font('fonts\Concrete.ttf',90)
black = (23, 32, 42)
white = (255, 255, 255)

#Sound effects
menu_sound = pygame.mixer.Sound("effects/menusound.wav")

#Backgrounds menu

surface_load_background = pygame.image.load('graphics/art_menu/background.png').convert_alpha()
surface_background = pygame.transform.scale(surface_load_background,(height, width))
rect_background = surface_background.get_rect(bottomright = (height, width))

surface_load_backgroundt = pygame.image.load('graphics/art_menu/background_tuto.png').convert_alpha()
surface_backgroundt = pygame.transform.scale(surface_load_backgroundt,(height,width))
rect_backgroundt = surface_backgroundt.get_rect(bottomright =(height, width))

#Game backgrounds
surface_load_background_game = pygame.image.load('graphics/art_game background/background_game.png').convert_alpha()
surface_backgroundg = pygame.transform.scale(surface_load_background_game,(height,width))
rect_backgroundg = surface_backgroundg.get_rect(center = (height//2,width//4))

surface_load_kidchen = pygame.image.load('graphics/art_game background/table work background.png').convert_alpha()
surface_kidchen = pygame.transform.scale(surface_load_kidchen,(height,width))
rect_kidchen = surface_kidchen.get_rect(bottomright = (height,width))

#Game objects

#Toppings
surface_load_cheese = pygame.image.load('graphics/art_kidchen elements/cheese.png').convert_alpha()
surface_cheese = pygame.transform.scale(surface_load_cheese,(90,90))
rect_cheese = surface_cheese.get_rect(center = (height//4,width//1.350))

surface_load_chips = pygame.image.load('graphics/art_kidchen elements/chips.png').convert_alpha()
surface_chips = pygame.transform.scale(surface_load_chips,(150,150))
rect_chips = surface_chips.get_rect(midbottom = (height//4.4,width//1.470))

surface_load_lettuce = pygame.image.load('graphics/art_kidchen elements/lettuce.png').convert_alpha()
surface_lettuce = pygame.transform.scale(surface_load_lettuce,(90,90))
rect_lettuce = surface_lettuce.get_rect(center = (height//3.050,width//1.345))

surface_load_tomat = pygame.image.load('graphics/art_kidchen elements/tomato.png').convert_alpha()
surface_tomat = pygame.transform.scale(surface_load_tomat,(90,90))
rect_tomat = surface_tomat.get_rect(center = (height//3.090,width//1.193))

surface_load_onion = pygame.image.load('graphics/art_kidchen elements/onion.png').convert_alpha()
surface_onion = pygame.transform.scale(surface_load_onion,(90,90))
rect_onion = surface_onion.get_rect(center = (height//3.090,width//1.076))

#Carnes
surface_load_meat1 = pygame.image.load('graphics/art_kidchen elements/meat_1.png').convert_alpha()
surface_meat1 = pygame.transform.scale(surface_load_meat1,(94,94))
rect_meat1 = surface_meat1.get_rect(center = (height//6,width//1.355))

surface_load_meat2 = pygame.image.load('graphics/art_kidchen elements/meat_2.png').convert_alpha()
surface_meat2 = pygame.transform.scale(surface_load_meat2,(100,100))
rect_meat2 = surface_meat2.get_rect(center = (height//6,width//1.195))

surface_load_sausage = pygame.image.load('graphics/art_kidchen elements/sausage.png').convert_alpha()
surface_sausage = pygame.transform.scale(surface_load_sausage,(80,80))
rect_sausage = surface_sausage.get_rect(center = (height//6,width//1.08))

surface_load_jamoneta = pygame.image.load('graphics/art_kidchen elements/jamoneta.png').convert_alpha()
surface_jamoneta = pygame.transform.scale(surface_load_jamoneta,(100,100))
rect_jamoneta = surface_jamoneta.get_rect(center = (height//4.05,width//1.2))

#Harinas
surface_load_pan1 = pygame.image.load('graphics/art_kidchen elements/pan_1.png').convert_alpha()
surface_pan1 = pygame.transform.scale(surface_load_pan1,(100,100))
rect_pan1 = surface_pan1.get_rect(center = (height//11,width//1.36))

surface_load_pan2 = pygame.image.load('graphics/art_kidchen elements/pan_2.png').convert_alpha()
surface_pan2 = pygame.transform.scale(surface_load_pan2,(94,94))
rect_pan2 = surface_pan2.get_rect(center = (height//11,width//1.2040))

surface_load_pan3 = pygame.image.load('graphics/art_kidchen elements/pan_3.png').convert_alpha()
surface_pan3 = pygame.transform.scale(surface_load_pan3,(100,100))
rect_pan3 = surface_pan3.get_rect(center = (height//11,width//1.075))

surface_load_tortilla = pygame.image.load('graphics/art_kidchen elements/tortilla.png').convert_alpha()
surface_tortilla = pygame.transform.scale(surface_load_tortilla,(100,100))
rect_tortilla = surface_tortilla.get_rect(center = (height//4.05,width//1.092))

#Salsas
surface_load_salsa1 = pygame.image.load('graphics/art_kidchen elements/salsa_1.png').convert_alpha()
surface_salsa1 = pygame.transform.scale(surface_load_salsa1,(50,100))
rect_salsa1 = surface_salsa1.get_rect(midbottom = (height//2,width//1.370))

surface_load_salsa2 = pygame.image.load('graphics/art_kidchen elements/salsa_2.png').convert_alpha()
surface_salsa2 = pygame.transform.scale(surface_load_salsa2,(50,100))
rect_salsa2 = surface_salsa2.get_rect(midbottom = (height//2.190,width//1.370))

surface_load_salsa3 = pygame.image.load('graphics/art_kidchen elements/salsa_3.png').convert_alpha()
surface_salsa3 = pygame.transform.scale(surface_load_salsa3,(50,100))
rect_salsa3 = surface_salsa3.get_rect(midbottom = (height//1.85,width//1.370))

#Bebidas
surface_load_soda = pygame.image.load('graphics/art_kidchen elements/soda.png').convert_alpha()
surface_soda = pygame.transform.scale(surface_load_soda,(100,100))
rect_soda = surface_soda.get_rect(midbottom = (height//12,width//1.470))

surface_load_water = pygame.image.load('graphics/art_kidchen elements/wather.png').convert_alpha()
surface_water = pygame.transform.scale(surface_load_water,(100,100))
rect_water = surface_water.get_rect(midbottom = (height//8,width//1.470))

surface_load_boxjuice = pygame.image.load('graphics/art_kidchen elements/boxjuice.png').convert_alpha()
surface_boxjuice = pygame.transform.scale(surface_load_boxjuice,(100,100))
rect_boxjuice = surface_boxjuice.get_rect(midbottom = (height//6,width//1.470))


#Title text
surface_load_title = pygame.image.load('graphics/art_menu/title.png').convert_alpha()
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


surface_fly = pygame.image.load('graphics/Fly1.png')
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
    global arrastre

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

        #Blitss
        screen.blit(surface_backgroundg,rect_backgroundg)
        screen.blit(surface_kidchen,rect_kidchen)
        screen.blit(surface_pan1,rect_pan1)
        screen.blit(surface_pan2,rect_pan2)
        screen.blit(surface_pan3,rect_pan3)
        screen.blit(surface_meat1,rect_meat1)
        screen.blit(surface_meat2,rect_meat2)
        screen.blit(surface_sausage,rect_sausage)
        screen.blit(surface_cheese,rect_cheese)
        screen.blit(surface_jamoneta,rect_jamoneta)
        screen.blit(surface_tortilla,rect_tortilla)
        screen.blit(surface_lettuce,rect_lettuce)
        screen.blit(surface_tomat,rect_tomat)
        screen.blit(surface_onion,rect_onion)
        screen.blit(surface_chips,rect_chips)
        screen.blit(surface_soda,rect_soda)
        screen.blit(surface_water,rect_water)
        screen.blit(surface_boxjuice,rect_boxjuice)
        screen.blit(surface_salsa1,rect_salsa1)
        screen.blit(surface_salsa2,rect_salsa2)
        screen.blit(surface_salsa3,rect_salsa3)
        
        screen.blit(surface_fly,fly_rect)


        pygame.display.update()
        clock.tick(60)
#--------------------------------------------------------------------------------------------------------------------------------#

master_menu()