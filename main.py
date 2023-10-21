import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import random

dorado="#F8C230"


class Juego:
    def __init__(self, ventana_jugar):
        self.root = ventana_jugar
        self.root.title("Juego con Tkinter")
        self.numero_juego = 1
        self.nivel = 1
        self.score = 0
        self.tablero = [[1] * 36 for _ in range(40)]  # Matriz inicial con valores de alimento (1)
        self.canvas = tk.Canvas(self.root, width=1000, height=720)
        self.canvas.pack(fill=tk.BOTH, expand=True)  # Ajusta el lienzo para llenar la ventana
        self.actualizar_tablero()

    def iniciar_juego(self):
        self.numero_juego += 1
        self.nivel = 1
        self.score = 0
        self.configurar_tablero()
        self.actualizar_tablero()

    def configurar_tablero(self):
        # Puedes personalizar esta función para definir la disposición de las paredes
        for i in range(40):
            for j in range(36):

                # Aquí puedes establecer la lógica para colocar paredes de manera aleatoria:
                if random.random() < 0.3:  # Probabilidad del 10% de que haya una pared
                    self.tablero[i][j] = 0
                elif random.random() < 0.01:
                    self.tablero[i][j] = 2

    def actualizar_tablero(self):
        self.canvas.delete("all")  # Borra cualquier elemento en el lienzo

        # Tamaño de celda
        celda_ancho = 20
        celda_alto = 20

        for fila in range(40):
            for columna in range(36):
                elemento = self.tablero[fila][columna]

                x1 = columna * celda_ancho
                y1 = fila * celda_alto
                x2 = x1 + celda_ancho
                y2 = y1 + celda_alto

                if elemento == 0:  # Pared
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
                elif elemento == 1:  # Alimento
                    x1 += 5  # Modifica estos valores para ajustar el tamaño del alimento
                    y1 += 5
                    x2 -= 5
                    y2 -= 5
                    self.canvas.create_oval(x1, y1, x2, y2, fill="yellow")
                elif elemento == 2:  # capsula
                    x1 += 3  # Modifica estos valores para ajustar el tamaño del alimento
                    y1 += 3
                    x2 -= 3
                    y2 -= 3
                    self.canvas.create_oval(x1, y1, x2, y2, fill="red")
def ventana_principal():
    def ventana_jugar():
        ventana_jugar = tk.Toplevel()
        ventana_jugar.minsize(1046, 785)
        ventana_jugar.title("Jugar")
        ventana_jugar.resizable(False, False)
        ventana_jugar.configure(bg=dorado)

        juego_actual = Juego(ventana_jugar)





    ventanaPrincipal = tk.Tk()
    ventanaPrincipal.minsize(1192, 670)
    ventanaPrincipal.title("shovel man")
    ventanaPrincipal.resizable(False, False)

    Inicio = tk.Canvas(ventanaPrincipal, width=1192, height=670)
    Inicio.place(x=0, y=0)
    Image_inicio = ImageTk.PhotoImage(file="shovelmenu.jpg")
    Inicio.create_image(0, 0, image=Image_inicio, anchor="nw")

    custom_font = font.Font(family="MegaMan 2 Regular", size=15)

    titulo = font.Font(family="MegaMan 2 Regular", size=20)


    label = tk.Label(ventanaPrincipal, text="shovel man", font=titulo, bg=dorado )
    label.place(x=200, y=100)

    Boton_jugar = tk.Button(ventanaPrincipal, text="jugar", font=custom_font,  bg=dorado, command=ventana_jugar
                            )
    Boton_jugar.place(x=30, y=250)

    Boton_marcadores = tk.Button(ventanaPrincipal, text="salon de leyendas", font=custom_font,bg=dorado
                                 )
    Boton_marcadores.place(x=30, y=350)

    Boton_acerca = tk.Button(ventanaPrincipal, text="acerca", font=custom_font, bg=dorado)
    Boton_acerca.place(x=30, y=450)
    ventanaPrincipal.mainloop()

ventana_principal()