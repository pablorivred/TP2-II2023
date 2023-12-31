import pygame
import sys
import time
import random
from tkinter import simpledialog
import tkinter
import pygame.mixer
from PIL import Image, ImageTk


pygame.mixer.init()
pygame.mixer.music.load("Y2meta.app - Take On Me (8 Bit Remix Cover Version) [Tribute to A-ha] - 8 Bit Universe (128 kbps) (2).mp3")
pygame.mixer.music.play(-1)
efecto_comer = pygame.mixer.Sound("Y2meta.app - SONIDO DE PAC MAN (128 kbps) (1).mp3")

def mostrar_menu():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 500))
    pygame.display.set_caption("Menú")

    fondo = pygame.image.load("menu.png")

    jugar_btn = pygame.image.load("jugar2.png")
    records_btn = pygame.image.load("Records (2).png")
    acerca_btn = pygame.image.load("acerca.png")


    reloj = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:#verifica si se hizo clic en algun boton

                if jugar_btn.get_rect(topleft=(20, 100)).collidepoint(evento.pos):
                    return
                if records_btn.get_rect(topleft=(20, 200)).collidepoint(evento.pos):
                    mostrar_puntajes()
                if acerca_btn.get_rect(topleft=(20, 300)).collidepoint(evento.pos):
                    mostrar_informacion(pantalla)

        pantalla.blit(fondo, (0, 0))#muestra el fondo en la pantalla
        pantalla.blit(jugar_btn, (20, 100))
        pantalla.blit(records_btn, (20, 200))
        pantalla.blit(acerca_btn,(20, 300))

        pygame.display.update()
        reloj.tick(30)

def mostrar_informacion(pantalla):
    pantalla.fill((0, 0, 0))  # Limpia la pantalla
    fuente = pygame.font.Font(None, 30)
    imagen = pygame.image.load("WhatsApp Image 2023-11-03 at 10.08.44 PM.jpg")
    imagen2=pygame.image.load("WhatsApp Image 2023-11-10 at 5.20.12 PM.jpg")
    texto = "Este proyecto ha sido realizado por el estudiante Pablo Esteban Rivera Redondo"
    texto2="carnet: 2023395989"
    texto22="y Deiver Jesus Quesada Navarro"
    texto222="carnet:2023153933"
    texto3="estudiantes del Instituto Tecnologico de Costa Rica"
    texto4 = "introduccion a la programacion grupo #1"
    texto5 = "ingenieria en computadores"
    texto6 = "Profesor:Jeff Schmidt Peralta"
    texto7 = "año 2023 Costa Rica"
    texto_superficie = fuente.render(texto, True, (255, 255, 255)) # renderiza el texto
    texto_superficie2 = fuente.render(texto2, True, (255, 255, 255))
    texto_superficie22 = fuente.render(texto22, True, (255, 255, 255))
    texto_superficie222 = fuente.render(texto222, True, (255, 255, 255))
    texto_superficie3 = fuente.render(texto3, True, (255, 255, 255))
    texto_superficie4 = fuente.render(texto4, True, (255, 255, 255))
    texto_superficie5 = fuente.render(texto5, True, (255, 255, 255))
    texto_superficie6 = fuente.render(texto6, True, (255, 255, 255))
    texto_superficie7 = fuente.render(texto7, True, (255, 255, 255))
    texto_rect7 = texto_superficie7.get_rect()#posiciona el texto en la pantalla
    texto_rect6 = texto_superficie6.get_rect()
    texto_rect5 = texto_superficie5.get_rect()
    texto_rect4 = texto_superficie4.get_rect()
    texto_rect3 = texto_superficie3.get_rect()
    texto_rect2 = texto_superficie2.get_rect()
    texto_rect22 = texto_superficie22.get_rect()
    texto_rect222 = texto_superficie222.get_rect()
    texto_rect2.topleft = (0, 25)
    texto_rect22.topleft = (0, 50)
    texto_rect222.topleft = (0, 75)
    texto_rect3.topleft = (0, 100)
    texto_rect4.topleft = (0, 125)
    texto_rect5.topleft = (0, 150)
    texto_rect6.topleft = (0, 175)
    texto_rect7.topleft = (0, 200)
    texto_rect = texto_superficie.get_rect()
    fondo = pygame.image.load("menu.png")
    pantalla.blit(fondo,(0,0))
    pantalla.blit(imagen, (300, 100))
    pantalla.blit(imagen2,(550,100))
    pantalla.blit(texto_superficie, texto_rect)
    pantalla.blit(texto_superficie2, texto_rect2)
    pantalla.blit(texto_superficie22, texto_rect22)
    pantalla.blit(texto_superficie222, texto_rect222)
    pantalla.blit(texto_superficie3, texto_rect3)
    pantalla.blit(texto_superficie4, texto_rect4)
    pantalla.blit(texto_superficie5, texto_rect5)
    pantalla.blit(texto_superficie6, texto_rect6)
    pantalla.blit(texto_superficie7, texto_rect7)
    pygame.display.update()
    en_ejecucion = True
    while en_ejecucion:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_ejecucion = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                en_ejecucion = False
def mostrar_puntajes():
    # Abre el archivo en modo de lectura
    with open("puntajes.txt", "r") as archivo:

        puntajes = archivo.read()

    # Muestra los puntajes en una ventana de diálogo
    tkinter.messagebox.showinfo("los mas mejores", puntajes)
mostrar_menu()

class Fantasmas:
    def __init__(self, id, x, y, color):
        self.id = id
        self.color = color
        self.estado = False
        self.posicion_x = x
        self.posicion_y = y
        self.velocidad = 1
        self.direccion = "derecha"
        self.fantasmaRojo = pygame.image.load("fantasmas/fantasmaRojo.png")
        self.fantasmaCeleste = pygame.image.load("fantasmas/fantasmaAzul.png")
        self.fantasmaRosa = pygame.image.load("fantasmas/fantasmaRosa.png")
        self.fantasmaNaranja = pygame.image.load("fantasmas/fantasmaNaranja.png")
        self.fantasmaVerde = pygame.image.load("fantasmas/nuevo.png")
        self.fantasmaAzul = pygame.image.load("fantasmas/fantasmaAzul.png")
        self.estadoVulnerable = pygame.image.load("fantasmas/Vulnerable.png")

    def mostrar_fantasma(self):
        print("Color de Fantasma:", self.color)
        print("Estado de Fantasma:", self.estado)
        print("Posición X de Fantasma:", self.posicion_x)
        print("Posición Y de Fantasma:", self.posicion_y)
        print("Velocidad de Fantasma:", self.velocidad)
        print("Dirección de Fantasma:", self.direccion)
        print("Imagen Rojo de Fantasma:", self.fantasmaRojo)
        print("Imagen Celeste de Fantasma:", self.fantasmaCeleste)
        print("Imagen Rosa de Fantasma:", self.fantasmaRosa)
        print("Imagen Naranja de Fantasma:", self.fantasmaNaranja)
        print("Imagen Verde de Fantasma:", self.fantasmaVerde)
        print("Imagen Azul de Fantasma:", self.fantasmaAzul)
        print("Imagen Vulnerable de Fantasma:", self.estadoVulnerable)

    def mover(self, tablero):
        nueva_posicion_x = self.posicion_x # Guarda las posiciones actuales del fantasma
        nueva_posicion_y = self.posicion_y

        if self.direccion == "arriba":# Actualiza las posiciones según la dirección del fantasma
            nueva_posicion_x -= self.velocidad
        elif self.direccion == "abajo":
            nueva_posicion_x += self.velocidad
        elif self.direccion == "izquierda":
            nueva_posicion_y -= self.velocidad
        elif self.direccion == "derecha":
            nueva_posicion_y += self.velocidad
        # Verifica si las nuevas posiciones están dentro de los límites del tablero y no hay paredes (valor 0)
        if (
            nueva_posicion_x >= 0
            and nueva_posicion_x < len(tablero)
            and nueva_posicion_y >= 0
            and nueva_posicion_y < len(tablero[0])
            and tablero[nueva_posicion_x][nueva_posicion_y] != 0
        ):
            self.posicion_x = nueva_posicion_x
            self.posicion_y = nueva_posicion_y
        else:
            # Si toca una pared, elige una nueva dirección aleatoria
            direcciones_posibles = ["arriba", "abajo", "izquierda", "derecha"]
            direcciones_posibles.remove(self.direccion)  # Elimina la dirección actual
            self.direccion = random.choice(direcciones_posibles)

    def cambiar_a_vulnerable(self):
        self.imagen = self.estadoVulnerable#cambia la imagen del fantasma a la de vulnerable
        self.estado=True
        self.velocidad=1
    def cambiar_a_normal(self):
        self.estado=False
        self.velocidad=1

    def dibujar(self, pantalla):
        if self.color == "Rojo":# Verifica el color del fantasma
            if self.estado == True:# Verifica si el estado del fantasma es vulnerable
                pantalla.blit(self.imagen, (self.posicion_y * 20, self.posicion_x * 20))# Si es vulnerable, dibuja la imagen vulnerable en la posición del fantasma
            else:
                pantalla.blit(self.fantasmaRojo, (self.posicion_y * 20, self.posicion_x * 20))# Si no es vulnerable, dibuja la imagen normal del fantasma en la posición del fantasma
        elif self.color == "Rosa":
            if self.estado == True:
                pantalla.blit(self.imagen, (self.posicion_y * 20, self.posicion_x * 20))
            else:
                pantalla.blit(self.fantasmaRosa, (self.posicion_y * 20, self.posicion_x * 20))
        elif self.color == "Celeste":
            if self.estado == True:
                pantalla.blit(self.imagen, (self.posicion_y * 20, self.posicion_x * 20))
            else:
                pantalla.blit(self.fantasmaCeleste, (self.posicion_y * 20, self.posicion_x * 20))
        elif self.color == "Naranja":
            if self.estado == True:
                pantalla.blit(self.imagen, (self.posicion_y * 20, self.posicion_x * 20))
            else:
                pantalla.blit(self.fantasmaNaranja, (self.posicion_y * 20, self.posicion_x * 20))
        elif self.color == "Verde":
            if self.estado == True:
                pantalla.blit(self.imagen, (self.posicion_y * 20, self.posicion_x * 20))
            else:
                pantalla.blit(self.fantasmaVerde, (self.posicion_y * 20, self.posicion_x * 20))

class Pacman:
    def __init__(self, x, y):
        self.estado = "vivo"
        self.posicion_x = x
        self.posicion_y = y
        self.velocidad = 1
        self.agresivo = False
        self.tiempo_agresivo = 0
        self.duracion_agresivo = 10000
        self.imagen_abierto = pygame.image.load("pacman_abierto.png")
        self.imagen_cerrado = pygame.image.load("pacman_cerrado.png")
        self.boca_abierta = True

    def mostrar_pacman(self):
        print("Estado de Pacman:", self.estado)
        print("Posición X:", self.posicion_x)
        print("Posición Y:", self.posicion_y)
        print("Velocidad:", self.velocidad)
        print("Agresivo:", self.agresivo)
        print("Tiempo Agresivo:", self.tiempo_agresivo)
        print("Duración Agresivo:", self.duracion_agresivo)
        print("Boca Abierta:", self.boca_abierta)
        print("Imagen Abierto:", self.imagen_abierto)
        print("Imagen Cerrado:", self.imagen_cerrado)



    def cambiar_estado(self, nuevo_estado):# Método para cambiar el estado de Pac-Man
        self.estado = nuevo_estado

    def cambiar_velocidad(self, nueva_velocidad): # Método para cambiar la velocidad de Pac-Man
        self.velocidad = nueva_velocidad

    def mover(self, direccion, tablero):# Método para mover a Pac-Man en una dirección dada
        # Calcula las nuevas coordenadas después de moverse
        nueva_posicion_x = self.posicion_x
        nueva_posicion_y = self.posicion_y

        if direccion == "arriba":
            nueva_posicion_x -= self.velocidad
        elif direccion == "abajo":
            nueva_posicion_x += self.velocidad
        elif direccion == "izquierda":
            nueva_posicion_y -= self.velocidad
        elif direccion == "derecha":
            nueva_posicion_y += self.velocidad

        # Verifica si la nueva posición es una pared (valor 0 en el tablero)
        if tablero[nueva_posicion_x][nueva_posicion_y] != 0:
            self.posicion_x = nueva_posicion_x
            self.posicion_y = nueva_posicion_y

    def comer(self, tablero, juego):
        # Verifica si Pac-Man está en una posición con alimento (valor 1 en el tablero)
        if tablero[self.posicion_x][self.posicion_y] == 1:
            # Borra el alimento de la matriz y suma 5 puntos al puntaje del juego
            tablero[self.posicion_x][self.posicion_y] = 4  # Marca como comida comida
            juego.score += 5  # Suma puntos al juego

    def comer_capsula(self, tablero):
        if tablero[self.posicion_x][self.posicion_y] == 2:
            tablero[self.posicion_x][self.posicion_y] = 5
    def comer_alimento(self, tablero):
        if tablero[self.posicion_x][self.posicion_y] == 3:
            tablero[self.posicion_x][self.posicion_y] = 6
            juego.score += 20

    def eliminar_fantasma(self, fantasmas):
        for fantasma in fantasmas:
            if self.posicion_x == fantasma.posicion_x and self.posicion_y == fantasma.posicion_y:
                fantasmas.remove(fantasma)  # Elimina el fantasma
                juego.score += 100

    def dibujar(self, pantalla):
        if self.boca_abierta:
            imagen_pacman = self.imagen_abierto
        else:
            imagen_pacman = self.imagen_cerrado

        pantalla.blit(imagen_pacman, (self.posicion_y * 20, self.posicion_x * 20))

        # Cambia el estado de la boca para el siguiente ciclo
        self.boca_abierta = not self.boca_abierta

class Juego:
    def __init__(self):
        self.fuente = pygame.font.Font(None, 36)
        self.tablero = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 4, 4, 4, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.nivel = 1
        self.score = 0
        self.game_over = False




    def detectar_colision(self, pac_man, fantasmas, pacman):
        if pacman.agresivo == False: # Verifica si Pac-Man no está en modo agresivo
            for fantasma in fantasmas:# Itera sobre la lista de fantasmas
                if pac_man.posicion_x == fantasma.posicion_x and pac_man.posicion_y == fantasma.posicion_y:# Verifica si la posición de Pac-Man coincide con la posición de un fantasma
                    puntaje_jugador = f"Tu puntaje fue: {self.score}"# Muestra un cuadro de diálogo con el puntaje del jugador y solicita su nombre
                    nombre_jugador = simpledialog.askstring("Misión Fracasada",
                                                            puntaje_jugador + "\nIntroduce tu nombre:")

                    self.game_over = True# Establece el estado de juego como "game over"
                    self.guardar_puntaje(nombre_jugador, self.score)# Guarda el puntaje del jugador junto con su nombre

                    print("Nombre del jugador:", nombre_jugador)#para verificar el guardado lo imprime en la consola
                    mostrar_menu()#muestra el menu

    def guardar_puntaje(self, nombre_jugador, score):
        # Lee los puntajes actuales del archivo
        puntajes = []
        with open("puntajes.txt", "r") as archivo:
            for linea in archivo:
                nombre, puntaje = linea.strip().split(": ")
                puntajes.append({"nombre": nombre, "puntaje": int(puntaje)})

        # Agrega el nuevo puntaje a la lista de puntajes
        puntajes.append({"nombre": nombre_jugador, "puntaje": score})

        # Ordena la lista de puntajes de mayor a menor
        puntajes_ordenados = sorted(puntajes, key=lambda x: x["puntaje"], reverse=True)

        # Abre el archivo en modo de escritura y guarda los puntajes ordenados
        with open("puntajes.txt", "w") as archivo:
            for jugador in puntajes_ordenados:
                archivo.write(f"{jugador['nombre']}: {jugador['puntaje']}\n")

    # Lógica para mostrar los puntajes más altos aquí

    def iniciar_juego(self):
        pygame.init()
        pantalla = pygame.display.set_mode((1000, 770))
        pygame.display.set_caption("Pac-Man")
        pacman = Pacman(13, 17)

        reloj = pygame.time.Clock()

        imagen_comida = pygame.image.load("comida.png")

        def actualizar_nivel(nivel, tablero, score):
            if score >=1500 and nivel == 1: # Verifica si el puntaje es mayor o igual a 2500 y el nivel actual es 1
                self.nivel = 2 # Establece el nivel del juego como 2

                for fila in range(len(tablero)):  # actualiza el tablero con los valores originales de las capsulas y alimentos
                    for columna in range(len(tablero[fila])):
                        if tablero[fila][columna] == 4:
                            tablero[fila][columna] = 1
                        if tablero[fila][columna] == 5:
                            tablero[fila][columna] = 2
                        if tablero[fila][columna] == 6:
                            tablero[fila][columna] = 3
            if self.nivel == 2 and len(fantasmas)==0: # Verifica si el nivel es 2 y no hay fantasmas en la lista
                fantasmaVerde = Fantasmas(3, 31, 26,"Verde")  # Crea instancias de fantasmas para el segundo nivel y los agrega a la lista de fantasmas
                fantasmas.append(fantasmaVerde)
                fantasmas.append(fantasmaRojo)
                fantasmas.append(fantasmaRosa)
                fantasmas.append(fantasmaCeleste)
                fantasmas.append(fantasmaNaranja)


        # Crear instancias de Fantasmas con diferentes colores
        fantasmaRojo = Fantasmas(0, 1, 1, "Rojo")        # Esquina superior izquierda
        fantasmaRosa = Fantasmas(1, 1, 26, "Rosa")       # Esquina superior derecha
        fantasmaCeleste = Fantasmas(2, 31, 1, "Celeste")  # Esquina inferior izquierda
        fantasmaNaranja = Fantasmas(3, 31, 26, "Naranja") # Esquina inferior derecha




        fantasmas = [fantasmaRojo, fantasmaRosa, fantasmaCeleste, fantasmaNaranja]


        pausado = False
        pausa_btn = pygame.image.load("pausa2.png")
        pausa_rect = pausa_btn.get_rect()
        pausa_rect.topleft = (750, 150)
        pantalla.blit(pausa_btn, pausa_rect)



        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    pausado = not pausado  # Cambia el estado de pausado
                    print(self.tablero)
                    pacman.mostrar_pacman()
                    fantasmaCeleste.mostrar_fantasma()
                    fantasmaNaranja.mostrar_fantasma()
                    fantasmaRosa.mostrar_fantasma()
                    fantasmaRojo.mostrar_fantasma()


            if not pausado:#verifica si no esta pausado
                if self.nivel==1:
                    actualizar_nivel(juego.nivel, juego.tablero, juego.score) # Actualiza el nivel si es el nivel 1
                elif self.nivel==2:
                    pass
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:# Captura las teclas presionadas para mover al pacman
                    pacman.mover("arriba", juego.tablero)
                    efecto_comer.play()
                if keys[pygame.K_DOWN]:
                    pacman.mover("abajo", juego.tablero)
                    efecto_comer.play()
                if keys[pygame.K_LEFT]:
                    pacman.mover("izquierda", juego.tablero)
                    efecto_comer.play()
                if keys[pygame.K_RIGHT]:
                    pacman.mover("derecha", juego.tablero)
                    efecto_comer.play()
                if juego.nivel == 2 and juego.score >= 2500:# Verifica si es el nivel 2 y se alcanzó el puntaje requerido
                    puntaje_jugador = f"Tu puntaje fue: {self.score}"
                    nombre_jugador = simpledialog.askstring("ganaste\n tu puntaje fue:",puntaje_jugador + "\nIntroduce tu nombre:")
                    self.guardar_puntaje(nombre_jugador, self.score)
                    mostrar_menu()
                juego.detectar_colision(pacman, fantasmas, pacman)#verifica las colisiones
                pacman.comer(juego.tablero, juego)#llamada de la funcion para comer
                pacman.comer_alimento(juego.tablero)
                if not pacman.agresivo:#verifica si el pacman esta agresivo
                    if juego.tablero[pacman.posicion_x][pacman.posicion_y] == 2:#verifica si pacamn comio una capsula
                        pacman.comer_capsula(juego.tablero)
                        pacman.agresivo = True#vuelve a pacman agresivo
                        pacman.tiempo_agresivo = pygame.time.get_ticks()  # Registra el tiempo actual
                        # Verifica si Pac-Man está en modo agresivo y controla el tiempo de duración
                if pacman.agresivo:
                    tiempo_actual = pygame.time.get_ticks()
                    if tiempo_actual - pacman.tiempo_agresivo >= pacman.duracion_agresivo:
                        pacman.agresivo = False  # Pac-Man vuelve a ser vulnerable
                        for fantasma in fantasmas:
                            fantasma.cambiar_a_normal()


                if pacman.agresivo:
                    pacman.eliminar_fantasma(fantasmas)#elimina a los fantasmas si pacman esta agresivo
                if pacman.agresivo:
                    for fantasma in fantasmas:
                        fantasma.cambiar_a_vulnerable()#cambia la imagen de los fantasmas



                pantalla.fill((0, 0, 0))
                # Dibuja el tablero y otros elementos gráficos
                pantalla.fill((0, 0, 0))  # Limpia la pantalla con color negro

                puntaje_texto = self.fuente.render(f"Puntaje: {self.score}", True, (255, 255, 255))# Crear una superficie de texto para el puntaje con la fuente definida previamente

                nivel_texto= self.fuente.render(f"nivel:{int(self.nivel)}", True, (255,255,255))
                pantalla.blit(puntaje_texto, (750, 50))# Mostrar el puntaje en la pantalla
                pantalla.blit(nivel_texto, (750, 100))# Mostrar el nivel en la pantalla

                pantalla.blit(pausa_btn, pausa_rect)# Mostrar el botón de pausa en la pantalla

                for fila in range(len(self.tablero)):
                    for columna in range(len(self.tablero[0])):
                        if self.tablero[fila][columna] == 0:# Verificar el valor en la posición actual del tablero
                            pygame.draw.rect(pantalla, (0, 0, 255),
                                             (columna * 20, fila * 20, 20, 20))  # Pared (rectángulo azul)
                        elif self.tablero[fila][columna] == 1:# Verificar el valor en la posición actual del tablero
                            pygame.draw.ellipse(pantalla, (255, 255, 0),
                                                (columna * 20 + 5, fila * 20 + 5, 10, 10))  # Punto (elipse amarilla)
                        elif self.tablero[fila][columna] == 2:# Verificar el valor en la posición actual del tablero
                            pygame.draw.ellipse(pantalla, (255, 0, 0),
                                                (columna * 20 + 5, fila * 20 + 5, 10, 10))  # Cápsula (elipse roja)
                        elif self.tablero[fila][columna] == 3:# Verificar el valor en la posición actual del tablero
                            pantalla.blit(imagen_comida, (columna * 20, fila * 20))  # Comida (imagen)
                pacman.dibujar(pantalla)  # Dibuja a PacMan en la pantalla

                for fantasma in fantasmas:#dibuja a los fantasmas en el juego
                    fantasma.mover(juego.tablero)
                    fantasma.dibujar(pantalla)

                pygame.display.update()#actualiza la pantalla
                reloj.tick(5)




if __name__ == "__main__":
    juego = Juego()
    juego.iniciar_juego()


