# Importar la biblioteca Pygame
import pygame
from pygame.locals import *
import sys

# Iniciación de Pygame
pygame.init()

# Tamaño de la ventana
W, H = 500, 400

# FPS
FPS = 60
RELOJ = pygame.time.Clock()

# Crear pantalla
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption('Extinction: Claw & Ashes')

# Icono del juego
icono = pygame.image.load("pygame_carnivores/imagenes/skull.png")
pygame.display.set_icon(icono)

# Fondo
fondo = pygame.image.load("pygame_carnivores/imagenes/fondo.jpeg").convert()

# Música de fondo

pygame.mixer_music.load("pygame_carnivores/sonidos/Echoes of the Ancients (1).mp3") # Especificamos la ruta de audio
pygame.mixer.music.play(-1) # Reproduce el audio del juego, el "-1" sirve para reproducir el audio en bucle
# pygame.mixer.music.set_volume(0.5) especificamos el volumen al que queremos reproducir el audio 

# Personaje
quieto = pygame.image.load("pygame_carnivores/sprites/quieto.png")

camina_derecha = [
    pygame.image.load("pygame_carnivores/sprites/caminando_1.png"),
    pygame.image.load("pygame_carnivores/sprites/caminando_2.png"),
    pygame.image.load("pygame_carnivores/sprites/caminando_3.png"),
    pygame.image.load("pygame_carnivores/sprites/caminando_4.png"),
    pygame.image.load("pygame_carnivores/sprites/caminando_5.png"),
    pygame.image.load("pygame_carnivores/sprites/caminando_6.png")
]

camina_izquierda = [
    pygame.image.load("pygame_carnivores/sprites/caminando_1_izq.png"),
    pygame.image.load("pygame_carnivores/sprites/caminando_2_izq.png"),
    pygame.image.load("pygame_carnivores/sprites/caminando_3_izq.png"),
    pygame.image.load("pygame_carnivores/sprites/caminando_4_izq.png"),
    pygame.image.load("pygame_carnivores/sprites/caminando_5_izq.png"),
    pygame.image.load("pygame_carnivores/sprites/caminando_6_izq.png")
]

# Sonido

sonido_arriba = pygame.image.load("pygame_carnivores/sonidos/sonido_activo.png")
sonido_abajo = pygame.image.load("pygame_carnivores/sonidos/sonido_bajando.png")
sonido_mute = pygame.image.load("pygame_carnivores/sonidos/mute.png")
sonido_max = pygame.image.load("pygame_carnivores/sonidos/sonido_maximo.png")

# Posición y velocidad del personaje
px = 50
py = 200
ancho = 40
velocidad = 5

# Dirección
izquierda = False
derecha = False

# Contador de animación
frame_actual = 0
sprite_actual = 0
frames_por_sprite = 10  # Más alto = animación más lenta

# Fondo desplazable
x = 0

# Función para dibujar todo
def recargarPantalla():
    global frame_actual, sprite_actual, x

    # Fondo en movimiento
    #x_relativa = x % fondo.get_rect().width
    #PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    #if x_relativa < W:
    #    PANTALLA.blit(fodndo, (x_relativa, 0))
    #x -= 1
  
    # Redibujar el fondo completo
    PANTALLA.blit(fondo, (0, 0))

    # Animación del personaje
    if izquierda:
        PANTALLA.blit(camina_izquierda[sprite_actual], (px, py))
        frame_actual += 1
        if frame_actual >= frames_por_sprite:
            frame_actual = 0
            sprite_actual = (sprite_actual + 1) % len(camina_izquierda)
    elif derecha:
        PANTALLA.blit(camina_derecha[sprite_actual], (px, py))
        frame_actual += 1
        if frame_actual >= frames_por_sprite:
            frame_actual = 0
            sprite_actual = (sprite_actual + 1) % len(camina_derecha)
    else:
        PANTALLA.blit(quieto, (px, py))
        frame_actual = 0
        sprite_actual = 0

# Bucle principal
while True:
    RELOJ.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Teclas presionadas
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False
    elif keys[pygame.K_d] and px < W - ancho:
        px += velocidad
        izquierda = False
        derecha = True
    else:
        izquierda = False
        derecha = False

    if keys[pygame.K_w] and py > 0:
        py -= velocidad
    if keys[pygame.K_s] and py < H - ancho:
        py += velocidad

    recargarPantalla()

        # Control del audio

    # Set = Establecer valores
    # Get = Obtener valores

    #  Bajar volumen

    if keys[pygame.K_9] and pygame.mixer_music.get_volume() > 0.0:
        pygame.mixer_music.set_volume(pygame.mixer_music.get_volume() - 0.01) # haciendo uso de get y set decrementamos el valor del volumen
        PANTALLA.blit(sonido_abajo,(400,25)) #  al tener 0.01 especificamos tener 100 niveles de volumen
    elif keys[pygame.K_9] and pygame.mixer_music.get_volume() == 0.0:
        PANTALLA.blit(sonido_mute, (400, 25))

    # Sube volumen

    if keys[pygame.K_0] and pygame.mixer_music.get_volume() < 1.0:
        pygame.mixer_music.set_volume(pygame.mixer_music.get_volume() + 0.01)
        PANTALLA.blit(sonido_arriba,(400,25))
    elif keys[pygame.K_0] and pygame.mixer_music.get_volume() == 1.0:
        PANTALLA.blit(sonido_max, (400, 25))

    # Desactivar sonido

    elif keys[pygame.K_m]:
        pygame.mixer_music.set_volume(0.0)
        PANTALLA.blit(sonido_mute, (400,25))

    # Reactivar sonido

    elif keys[pygame.K_COMMA]:
        pygame.mixer_music.set_volume(1.0)
        PANTALLA.blit(sonido_max, (400,25))

    pygame.display.update()