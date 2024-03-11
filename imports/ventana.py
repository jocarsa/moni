from PIL import Image, ImageTk
import tkinter as tk
from ttkbootstrap import Style
from imports.mimenu import *

def estilizarVentana(bienvenida,ventana):

    style = Style(theme="solar")
    
    anchura = ventana.winfo_screenwidth()
    altura = ventana.winfo_screenheight()

    anchura_bienvenida = 400
    altura_bienvenida = 400
    x_bienvenida = int(anchura/2)-int(anchura_bienvenida/2)
    y_bienvenida = int(altura/2)-int(altura_bienvenida/2)
    anchura_ventana = 1024
    altura_ventana = 768
    x_ventana = int(anchura/2)-int(anchura_ventana/2)
    y_ventana = int(altura/2)-int(altura_ventana/2)

    bienvenida.geometry(f"{anchura_bienvenida}x{altura_bienvenida}+{x_bienvenida}+{y_bienvenida}")
    ventana.geometry(f"{anchura_ventana}x{altura_ventana}+{x_ventana}+{y_ventana}")

    bienvenida.title("Bienvenida")
    ventana.title("Moni v0.1")

    bienvenida.iconbitmap("res/icono.ico")
    ventana.iconbitmap("res/icono.ico")

    bienvenida.attributes("-topmost", True)
    bienvenida.resizable(False, False)

    imagen_bienvenida = Image.open("res/bienvenida.png")
    foto_bienvenida = ImageTk.PhotoImage(imagen_bienvenida)
    tk.Label(bienvenida,image=foto_bienvenida).pack()

    menu(ventana)

    herramientas = tk.Frame(ventana)
    herramientas.grid(row=0,column=0)

    tk.Label(herramientas,text="Herramientas").pack()

    principal = tk.Frame(ventana)
    principal.grid(row=0,column=1)

    tk.Label(principal,text="Principal").pack()

    propiedades = tk.Frame(ventana)
    propiedades.grid(row=0,column=2)

    tk.Label(propiedades,text="Propiedades").pack()

    ventana.mainloop()
    bienvenida.mainloop()
