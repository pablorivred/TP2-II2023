import pygame
def iniciar_juego():
    pygame.init()
    pantalla = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("Pac-Man")




    # Agregar las instancias a una lista de fantasmas



    boton_pausa = pygame.Rect(200, 100, 80, 40)
    color_boton_pausa = (0, 255, 0)
    pygame.draw.rect(pantalla, color_boton_pausa, boton_pausa)
    pygame.draw.polygon(pantalla, (0, 0, 0), [(740, 20), (740, 40), (760, 30)])