import tkinter as tk

bienvenida = tk.Tk()
ventana = tk.Tk()

anchura = ventana.winfo_screenwidth()
altura = ventana.winfo_screenheight()

bienvenida.geometry(f"400x400+{int(anchura/2)-200}+{int(altura/2)-200}")
ventana.geometry(f"1024x768+{int(anchura/2)-512}+{int(altura/2)-384}")

ventana.mainloop()
bienvenida.mainloop()
