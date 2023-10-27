import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import random

dorado="#F8C230"


def ventana_principal():
    def ventana_jugar():
        ventana_jugar = tk.Toplevel()
        ventana_jugar.minsize(1046, 785)
        ventana_jugar.title("Jugar")
        ventana_jugar.resizable(False, False)
        ventana_jugar.configure(bg=dorado)

        





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