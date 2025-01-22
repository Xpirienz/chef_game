import pygame
from sys import exit

pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((800, 400))

# Título
pygame.display.set_caption('UN food')

clock = pygame.time.Clock()  # Limitar FPS

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VINOTINTO = (128, 0, 32)
CAFE = (214, 150, 97)

# Fuentes
test_font = pygame.font.Font(None, 70)
botton_font = pygame.font.Font(None, 40)
instructions_font = pygame.font.Font(None, 30)

# Fondo e imágenes
fondo = pygame.image.load('Desktop/Proyecto ch/imagns/fondo.webp').convert()

fondo = pygame.transform.scale(fondo, (800, 400))

cursor_img = pygame.image.load('Desktop/Proyecto ch/imagns/mano.png').convert_alpha()
cursor_img = pygame.transform.scale(cursor_img, (30, 30))

# Textos y botones
text_1 = test_font.render('UNfood', True, NEGRO)
boton_iniciar = pygame.Rect(350, 120, 130, 50)
boton_instrucciones = pygame.Rect(310, 180, 240, 50)
boton_salir = pygame.Rect(350, 240, 130, 50)

current_screen = "menu"

def mostrar_mensaje(mensaje):
    print(mensaje)

def mostrar_instrucciones():
    """Dibuja la pantalla de instrucciones."""
    screen.fill(BLANCO)
    title = test_font.render("Instrucciones", True, NEGRO)
    screen.blit(title, (280, 20))

    instrucciones = [
        "El jugador contará con tres vidas al iniciar cada nivel.",
        "El jugador comienza con una cantidad ilimitada de ingredientes para armar comidas.",
        "Se despliega una fila de clientes con pedidos específicos que deben ser atendidos.",
        "Se debe despachar el pedido antes que el cronómetro del cliente llegue a 0 y se pierda la venta.",
        "Entregar un pedido incorrecto penaliza al jugador y pierde una vida.",
        "Si el jugador pierde todas sus vidas, la partida termina.",
        "El jugador debe alcanzar un umbral de dinero al final de cada nivel para superarlo.",
        "Si la comida no es correcta, puede desecharla y hacer otra.",
    ]

    y_offset = 80
    for linea in instrucciones:
        texto = instructions_font.render(linea, True, NEGRO)
        screen.blit(texto, (50, y_offset))
        y_offset += 40

    boton_volver = pygame.Rect(650, 330, 120, 40)
    pygame.draw.rect(screen, CAFE, boton_volver)
    text_volver = botton_font.render("VOLVER", True, VINOTINTO)
    screen.blit(text_volver, (665, 340))
    return boton_volver


# Bucle principal
while True:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "menu":
                if boton_iniciar.collidepoint(event.pos):
                    print("¡Iniciar Juego!")
                elif boton_instrucciones.collidepoint(event.pos):
                    current_screen = "instrucciones"
                elif boton_salir.collidepoint(event.pos):
                    print("Salir")
                    pygame.quit()
                    exit()
            elif current_screen == "instrucciones":
                boton_volver = mostrar_instrucciones()
                if boton_volver.collidepoint(event.pos):
                    current_screen = "menu"

    # Dibujar el fondo y los botones
    if current_screen == "menu":

        screen.blit(fondo, (0, 0))
        screen.blit(text_1, (320, 70))

        pygame.draw.rect(screen, CAFE, boton_iniciar)
        pygame.draw.rect(screen, CAFE, boton_instrucciones)
        pygame.draw.rect(screen, CAFE, boton_salir)

        # Añadir texto a los botones
        text_b1 = botton_font.render('INICIO', True, VINOTINTO)
        text_b2 = botton_font.render('INSTRUCCIONES', True, VINOTINTO)
        text_b3 = botton_font.render('SALIR', True, VINOTINTO)

        screen.blit(text_b1, (370, 130))
        screen.blit(text_b2, (310, 190))
        screen.blit(text_b3, (370, 250))

    elif current_screen == "instrucciones":
        boton_volver = mostrar_instrucciones()


    # Posición del cursor 
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(cursor_img, (mouse_pos[0] - 15, mouse_pos[1] - 15))

    # Actualizar pantalla
    pygame.display.update()
    clock.tick(60)