from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from ttkbootstrap import Style
from tkinter import ttk

principal = None

slider = None

def rangoCambia(event):
    global slider
    print("Ha cambiado")
    print(slider.get())

def imagenBrillo():
    global slider
    print("edito el brillo")
    ventana_brillo = tk.Toplevel()
    ventana_brillo.geometry("800x400")
    ventana_brillo.title("Brillo")
    slider = ttk.Scale(ventana_brillo)
    slider.pack(padx=50, pady=50)
    slider.bind("<Motion>", rangoCambia)
    
def abrirArchivo():
    global principal
    print("Abro un archivo")
    imagen = filedialog.askopenfilename(title="Selecciona un archivo")
    if imagen:
        foto = Image.open(imagen)
        mifoto = ImageTk.PhotoImage(foto)
        etiqueta = tk.Label(principal, image=mifoto)
        etiqueta.image = mifoto
        etiqueta.pack()

def bloques(ventana):
    global principal
    herramientas = tk.Frame(ventana)
    herramientas.grid(row=0, column=0)

    tk.Label(herramientas, text="Herramientas").pack()

    principal = tk.Frame(ventana)
    principal.grid(row=0, column=1)

    tk.Label(principal, text="Principal").pack()

    propiedades = tk.Frame(ventana)
    propiedades.grid(row=0, column=2)

    tk.Label(propiedades, text="Propiedades").pack()

    ventana.rowconfigure(0, weight=100)
    ventana.columnconfigure(0, weight=10)
    ventana.columnconfigure(1, weight=80)
    ventana.columnconfigure(2, weight=10)

def menu(ventana):
    menu = tk.Menu(ventana)
    ventana.config(menu=menu)
    archivo = tk.Menu(menu)
    menu.add_cascade(label="Archivo", menu=archivo)

    archivo.add_command(label="Abrir archivo", command=abrirArchivo)
    editar = tk.Menu(menu)
    menu.add_cascade(label="Editar", menu=editar)
    colores = tk.Menu(menu)
    menu.add_cascade(label="Colores", menu=colores)
    colores.add_command(label="Brillo", command=imagenBrillo)
    ayuda = tk.Menu(menu)
    menu.add_cascade(label="Ayuda", menu=ayuda)

def estilizarVentana(ventana):
    style = Style(theme="solar")

    anchura = ventana.winfo_screenwidth()
    altura = ventana.winfo_screenheight()

    anchura_bienvenida = 400
    altura_bienvenida = 400
    x_bienvenida = int(anchura / 2) - int(anchura_bienvenida / 2)
    y_bienvenida = int(altura / 2) - int(altura_bienvenida / 2)
    anchura_ventana = 1024
    altura_ventana = 768
    x_ventana = int(anchura / 2) - int(anchura_ventana / 2)
    y_ventana = int(altura / 2) - int(altura_ventana / 2)

    #bienvenida.geometry(f"{anchura_bienvenida}x{altura_bienvenida}+{x_bienvenida}+{y_bienvenida}")
    ventana.geometry(f"{anchura_ventana}x{altura_ventana}+{x_ventana}+{y_ventana}")

    #bienvenida.title("Bienvenida")
    ventana.title("Moni v0.1")

    #bienvenida.iconbitmap("../res/icono.ico")
    ventana.iconbitmap("../res/icono.ico")

    #bienvenida.attributes("-topmost", True)
    #bienvenida.resizable(False, False)

    imagen_bienvenida = Image.open("../res/bienvenida.png")
    foto_bienvenida = ImageTk.PhotoImage(imagen_bienvenida)
    #tk.Label(bienvenida, image=foto_bienvenida).pack()

    bloques(ventana)
    menu(ventana)

    #bienvenida.mainloop()
    ventana.mainloop()

# Create the main window
#bienvenida = tk.Tk()
ventana = tk.Tk()

# Apply styling and configure windows
estilizarVentana(ventana)
