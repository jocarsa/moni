import tkinter as tk

bienvenida = tk.Tk()
ventana = tk.Tk()

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

bienvenida.attributes("-topmost", True)
bienvenida.resizable(False, False)

ventana.mainloop()
bienvenida.mainloop()
