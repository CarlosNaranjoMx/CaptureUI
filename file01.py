############ Requirements files ################################################
from tkinter import Tk,Toplevel,Label,Entry

########################## Vars ################################################
tk = Tk()
tk.title("Capture")

ventana = Toplevel(tk)
ventana.geometry("300x200+400+200")
ventana.config(highlightbackground="red", highlightcolor="red", highlightthickness=5)
ventana.attributes("-alpha", 0.1) # Ajustar el nivel de transparencia
ventana.wm_transient(tk)

label = Label(tk,text="Category:").grid(row=0,column=0)
entry = Entry(tk)
entry.grid(row=0,column=1)

label_name = Label(tk,text="Name:").grid(row=1,column=0)
entry_name = Entry(tk)
entry_name.grid(row=1,column=1)

def mover_ventana2(event):
    # Obtener la posición y el tamaño de la ventana principal
    x1 = tk.winfo_x()
    y1 = tk.winfo_y()
    w1 = tk.winfo_width()
    h1 = tk.winfo_height()
    # Calcular la posición de la ventana secundaria para que quede a la derecha de la principal
    x2 = x1 + w1
    y2 = y1
    # Cambiar la posición de la ventana secundaria
    ventana.geometry(f"+{x2}+{y2}")

def accion():
    # Obtener el texto de la entry
    texto = entry_name.get()
    # Imprimir el texto en la consola
    # print(texto)

# Vincular el evento <Return> de la entry con la función accion
entry_name.bind("<Return>", lambda event: accion())

# Vincular el evento <Configure> de la ventana principal con la función mover_ventana2
tk.bind("<Configure>", mover_ventana2)

