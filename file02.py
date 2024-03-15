############ Requirements imports ################################################
import config as conf
from mss import mss
import json
import cv2
import numpy as np
from os import mkdir
from os.path import join,exists
import json
from tkinter import END

################# Local imports ################################################
import file01

########################## Vars ################################################
tk = file01.tk
entry_name = file01.entry_name
########################## Code ################################################
def capture_tk():
    width = file01.ventana.winfo_width()
    height = file01.ventana.winfo_height()
    x = file01.ventana.winfo_x()
    y = file01.ventana.winfo_y()
    capture_str = file01.entry.get()
    # bounding_box = {'top': 100, 'left': 0, 'width': 1920, 'height': 1080}
    bounding_box = {'top': y+35, 'left': x+10, 'width': width, 'height': height}
    sct = mss()
    sct_img = sct.grab(bounding_box)

    vars = dict()
    entry_name_str = file01.entry_name.get()
    with open("vars.json","r") as file:
        texto = file.read()
        vars = json.loads(texto)

    if capture_str in vars: vars[capture_str] += 1
    else: vars[capture_str] = 0
    with open("vars.json","w") as file:
        file.write(json.dumps(vars))

    # if not exists(join(conf.IMG,capture_str)): mkdir(join(conf.IMG,capture_str))
    # cv2.imwrite(join(conf.IMG,'%s'%capture_str,"%d_%s.png"%(vars[capture_str],entry_name_str)),np.array(sct_img))
    cv2.imwrite(join(conf.IMG,"%s_%d_%s.png"%(capture_str,vars[capture_str],entry_name_str)),np.array(sct_img))

    # file01.entry.delete(0,END)
    file01.entry_name.delete(0,END)