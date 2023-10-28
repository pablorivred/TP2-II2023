
import pygame
import sys
def mostrar_menu():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Menú")

    fondo = pygame.image.load("shovelmenu.jpg")

    jugar_btn = pygame.image.load("Sin título.png")

    reloj = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:

                if jugar_btn.get_rect(topleft=(100, 300)).collidepoint(evento.pos):
                    return

        pantalla.blit(fondo, (0, 0))
        pantalla.blit(jugar_btn, (100, 300))

        pygame.display.update()
        reloj.tick(30)


mostrar_menu()
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

    def mover(self, direccion):
        if direccion == "arriba":
            self.posicion_x -= self.velocidad
        elif direccion == "abajo":
            self.posicion_x += self.velocidad
        elif direccion == "izquierda":
            self.posicion_y -= self.velocidad
        elif direccion == "derecha":
            self.posicion_y += self.velocidad

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def cambiar_velocidad(self, nueva_velocidad):
        self.velocidad = nueva_velocidad

    def mover(self, direccion, tablero):
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
        self.numero_de_juego = 1
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



    def iniciar_juego(self):
        pygame.init()
        pantalla = pygame.display.set_mode((1000, 800))
        pygame.display.set_caption("Pac-Man")
        pacman = Pacman(13, 17)

        reloj = pygame.time.Clock()

        imagen_comida = pygame.image.load("comida.png")

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()


            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                pacman.mover("arriba", juego.tablero)
            if keys[pygame.K_DOWN]:
                pacman.mover("abajo", juego.tablero)
            if keys[pygame.K_LEFT]:
                pacman.mover("izquierda", juego.tablero)
            if keys[pygame.K_RIGHT]:
                pacman.mover("derecha", juego.tablero)

            pacman.comer(juego.tablero, juego)
            if not pacman.agresivo:
                if juego.tablero[pacman.posicion_x][pacman.posicion_y] == 2:
                    pacman.comer_capsula(juego.tablero)
                    pacman.agresivo = True
                    pacman.tiempo_agresivo = pygame.time.get_ticks()  # Registra el tiempo actual
                    # Verifica si Pac-Man está en modo agresivo y controla el tiempo de duración
            if pacman.agresivo:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual - pacman.tiempo_agresivo >= pacman.duracion_agresivo:
                    pacman.agresivo = False  # Pac-Man vuelve a ser vulnerable
                    # Dibuja el tablero y otros elementos gráficos aquí...

            pantalla.fill((0, 0, 0))
            # Dibuja el tablero y otros elementos gráficos
            pantalla.fill((0, 0, 0))  # Limpia la pantalla con color negro

            for fila in range(len(self.tablero)):
                for columna in range(len(self.tablero[0])):
                    if self.tablero[fila][columna] == 0:
                        pygame.draw.rect(pantalla, (0, 0, 255), (columna * 20, fila * 20, 20, 20))  # Pared (rectángulo azul)
                    elif self.tablero[fila][columna] == 1:
                        pygame.draw.ellipse(pantalla, (255, 255, 0), (columna * 20 + 5, fila * 20 + 5, 10, 10))  # Punto (elipse amarilla)
                    elif self.tablero[fila][columna] == 2:
                        pygame.draw.ellipse(pantalla, (255, 0, 0),(columna * 20 + 5, fila * 20 + 5, 10, 10))  # Cápsula (elipse roja)
                    elif self.tablero[fila][columna] == 3:
                        pantalla.blit(imagen_comida, (columna * 20, fila * 20))  # Comida (imagen)
            pacman.dibujar(pantalla)  # Dibuja a PacMan en la pantalla

            pygame.display.update()
            reloj.tick(10)

if __name__ == "__main__":
    juego = Juego()
    juego.iniciar_juego()

