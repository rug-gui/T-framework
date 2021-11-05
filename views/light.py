from tkinter import *
import os
root=Tk()
root.title('tk')
#root.iconbitmap(os.path.curdir+"/assets/icon/favicon.ico")
if os.path.isfile(os.path.curdir+'/assets/favicon/light.ico'):
    root.iconbitmap(os.path.curdir+"/assets/favicon/light.ico")