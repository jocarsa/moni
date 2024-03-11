import tkinter as tk
from imports.variables import *

def bloques(ventana):
    herramientas = tk.Frame(ventana)
    herramientas.grid(row=0,column=0)

    tk.Label(herramientas,text="Herramientas").pack()

    principal = tk.Frame(ventana)
    principal.grid(row=0,column=1)

    tk.Label(principal,text="Principal").pack()

    propiedades = tk.Frame(ventana)
    propiedades.grid(row=0,column=2)

    tk.Label(propiedades,text="Propiedades").pack()

    ventana.rowconfigure(0,weight=100)
    ventana.columnconfigure(0,weight=10)
    ventana.columnconfigure(1,weight=80)
    ventana.columnconfigure(2,weight=10)
    print(prueba)
