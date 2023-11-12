import pygame
import random
import math
from pygame import mixer


#Se inicializa pygame.
pygame.init()
#Se crea la pantalla.
pantalla = pygame.display.set_mode((800, 600))

juego_terminado = False
# Titulo y icono.
pygame.display.set_caption("Invacion espacial.")
icono = pygame.image.load("ovni.png")
fondo = pygame.image.load('fondo.jpg')
pygame.display.set_icon(icono)

# agregar musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Jugador.
img_jugador = pygame.image.load("cohete.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio  = 0
jugador_y_cambio  = 0

# Funcion del jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio  = []
enemigo_y_cambio  = []
cantidad_enemigos = 10

#Generar enemigos

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.1)
    enemigo_y_cambio.append(0.03)
# Funcion del enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

# bala

img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 0
bala_x_cambio = 0
bala_y_cambio = 5
bala_visible = False
"""
class Balas:
    img_bala = []
    bala_x = []
    bala_y = []
    bala_x_cambio = []
    bala_y_cambio = []
    bala_visible = []

    def disparar(self,img_bala,  x , y):
        global bala_visible
        bala_visible = True
        pantalla.blit(img_bala, (x + 16, y + 10))

nueva_bala = Balas()
for i in range(10):
    nueva_bala[i]
"""

# Funcion del bala

def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16,  y + 10))

# Detectar colidiones

def detectar_coliciones(x1, y1, x2, y2):
    distancia = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if distancia < 27:
        return True
    else:
        return False

# puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

# texto final de juego
fuente_final = pygame.font.Font('freesansbold.ttf', 40)


def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60, 200))


# funcion mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


#Funcionamiento del programa.

while not juego_terminado:
    # Pantalla

    pantalla.blit(fondo, (0,0))
    for evento in pygame.event.get():
        # Cerrar el juego
        if evento.type == pygame.QUIT:
            juego_terminado = True


        # Movimiento del jugador
        if  evento.type == pygame.KEYDOWN:
            # Movimiento horizontal.
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1

            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1

            #Movimiento vertical.

            if evento.key == pygame.K_UP:
                jugador_y_cambio = -0.5
            if evento.key == pygame.K_DOWN:
                jugador_y_cambio = 0.5

            # Disparar bala

            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)


        # Tecla levantada
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
            elif evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                jugador_y_cambio = 0
       

    #Ubicacion del jugador.
    jugador_x += jugador_x_cambio
    jugador_y += jugador_y_cambio
    # Mantener nave dentro de bordes
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736.
    if jugador_y >= 536:
        jugador_y = 536
    elif jugador_y <= 500:
        jugador_y = 500

    # Ubicacion del enemigo.
    for e in range(cantidad_enemigos):

        # fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break




        enemigo_x[e] += enemigo_x_cambio[e]
        enemigo_y[e] += enemigo_y_cambio[e]

        # Mantener enemigo dentro de bordes
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.1
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.1


        #colision

        colision = detectar_coliciones(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('golpe.mp3')
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)
        enemigo(enemigo_x[e], enemigo_y[e] , e)
        # Movimiento bala

        if bala_y <= -64:
            bala_y = jugador_y
            bala_visible = False
        if bala_visible:
            disparar_bala(bala_x, bala_y)
            bala_y -= bala_y_cambio

    jugador(jugador_x, jugador_y)
    mostrar_puntaje(texto_x, texto_y)

    pygame.display.update()