import pygame
from sys import exit

#######################################################--SCREEN--#################################################################
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
height, width = screen.get_size()
##############################################---MENU AND TUTO FILES---############################################################
#Font and colors
font = pygame.font.Font('fonts/Concrete.ttf',90)
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

#Game objets

ingredientes_data = [

    # Carnes, panes y verduras
    {"name": "cheese", "path": 'graphics/art_kidchen elements/cheese.png', "size": (90, 90), "pos": (height//4, width//1.350), "align": "center"},
    {"name": "lettuce", "path": 'graphics/art_kidchen elements/lettuce.png', "size": (90, 90), "pos": (height//3.050, width//1.345), "align": "center"},
    {"name": "tomato", "path": 'graphics/art_kidchen elements/tomato.png', "size": (90, 90), "pos": (height//3.090, width//1.193), "align": "center"},
    {"name": "onion", "path": 'graphics/art_kidchen elements/onion.png', "size": (90, 90), "pos": (height//3.090, width//1.076), "align": "center"},
    {"name": "meat1", "path": 'graphics/art_kidchen elements/meat_1.png', "size": (94, 94), "pos": (height//6, width//1.355), "align": "center"},
    {"name": "meat2", "path": 'graphics/art_kidchen elements/meat_2.png', "size": (100, 100), "pos": (height//6, width//1.195), "align": "center"},
    {"name": "sausage", "path": 'graphics/art_kidchen elements/sausage.png', "size": (80, 80), "pos": (height//6, width//1.08), "align": "center"},
    {"name": "jamoneta", "path": 'graphics/art_kidchen elements/jamoneta.png', "size": (100, 100), "pos": (height//4.05, width//1.2), "align": "center"},
    {"name": "pan1", "path": 'graphics/art_kidchen elements/pan_1.png', "size": (100, 100), "pos": (height//11, width//1.36), "align": "center"},
    {"name": "pan2", "path": 'graphics/art_kidchen elements/pan_2.png', "size": (94, 94), "pos": (height//11, width//1.204), "align": "center"},
    {"name": "pan3", "path": 'graphics/art_kidchen elements/pan_3.png', "size": (100, 100), "pos": (height//11, width//1.075), "align": "center"},
    {"name": "tortilla", "path": 'graphics/art_kidchen elements/tortilla.png', "size": (100, 100), "pos": (height//4.05, width//1.092), "align": "center"},
    
    # Salsas
    {"name": "salsa1", "path": 'graphics/art_kidchen elements/salsa_1.png', "size": (50, 100), "pos": (height//2, width//1.370), "align": "midbottom"},
    {"name": "salsa2", "path": 'graphics/art_kidchen elements/salsa_2.png', "size": (50, 100), "pos": (height//2.190, width//1.370), "align": "midbottom"},
    {"name": "salsa3", "path": 'graphics/art_kidchen elements/salsa_3.png', "size": (50, 100), "pos": (height//1.85, width//1.370), "align": "midbottom"},
    
    # Bebidas y papitas
    {"name": "soda", "path": 'graphics/art_kidchen elements/soda.png', "size": (100, 100), "pos": (height//12, width//1.470), "align": "midbottom"},
    {"name": "water", "path": 'graphics/art_kidchen elements/wather.png', "size": (100, 100), "pos": (height//8, width//1.470), "align": "midbottom"},
    {"name": "boxjuice", "path": 'graphics/art_kidchen elements/boxjuice.png', "size": (100, 100), "pos": (height//6, width//1.470), "align": "midbottom"},
    {"name": "chips", "path": 'graphics/art_kidchen elements/chips.png', "size": (150, 150), "pos": (height//4.4, width//1.470), "align": "midbottom"}
]

ingredientes = []
for ing in ingredientes_data:
    image = pygame.image.load(ing["path"]).convert_alpha()
    image = pygame.transform.scale(image, ing["size"])
    rect = image.get_rect()
    
    if ing["align"] == "center":
        rect.center = ing["pos"]
    elif ing["align"] == "midbottom":
        rect.midbottom = ing["pos"]
    
    ingredientes.append({"name": ing["name"], "image": image, "rect": rect})

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


#Zona de armado

zona_armado = pygame.Rect(width*0.7426 , height*0.418, height * 0.26, width*0.187)


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








        #Blitss en pantalla
        screen.blit(surface_backgroundg,rect_backgroundg)
        screen.blit(surface_kidchen,rect_kidchen)
        for ing in ingredientes:
            screen.blit(ing["image"], ing["rect"])
        screen.blit(surface_fly,fly_rect)
        pygame.draw.rect(screen, 'Red', zona_armado, 3)




        pygame.display.update()
        clock.tick(60)
#--------------------------------------------------------------------------------------------------------------------------------#

master_menu()