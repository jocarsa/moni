import tkinter as tk

def abrirArchivo():
    print("Abro un archivo")

def menu(ventana):
    menu = tk.Menu(ventana)
    ventana.config(menu=menu)
    archivo = tk.Menu(menu)
    menu.add_cascade(label="Archivo",menu=archivo)
    
    archivo.add_command(label="Abrir archivo",command=abrirArchivo)
    
    menu.add_cascade(label="Editar",menu=archivo)

    menu.add_cascade(label="Colores",menu=archivo)

    menu.add_cascade(label="Ayuda",menu=archivo)
