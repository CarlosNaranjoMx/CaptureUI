############ Requirements files ################################################
from tkinter import *

import file02

tk = file02.tk
entry_name = file02.entry_name

# Vincular el evento <Return> de la entry con la función accion
file02.entry_name.bind("<Return>", lambda event: file02.capture_tk())
file02.entry_name.bind("<Alt-q>", lambda event: file02.capture_tk())
Button(file02.tk,text="capture",command=file02.capture_tk).grid(row=1, column=2)