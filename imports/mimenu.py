import tkinter as tk

def menu(ventana):
    menu = tk.Menu(ventana)
    ventana.config(menu=menu)
    archivo = tk.Menu(menu)
    menu.add_cascade(label="Archivo",menu=archivo)

    menu.add_cascade(label="Editar",menu=archivo)

    menu.add_cascade(label="Colores",menu=archivo)

    menu.add_cascade(label="Ayuda",menu=archivo)
