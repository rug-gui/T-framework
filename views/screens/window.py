from tkinter import *
import sys
import darkdetect
# setting path
sys.path.append('../T')
import main

if main.vmode[0][1]=='Light':
    from views import light as wndw
elif main.vmode[0][1]=='Dark':
    from views import dark as wndw
    
app = wndw.root
#-------Your GUI Screen Here ------
import ttkthemes
from tkinter import ttk
app.tk.call("source", "assets/theme/Forest/forest-light.tcl")
# Then set the theme you want with the set_theme procedure
#app.tk.call("set_theme", "light")

style = ttk.Style(app)
style.theme_use("forest-light")

#app.config(bg='pink')
'''from PIL import Image,ImageTk
bg=Image.open('assets/bg/0.png')
bgn=ImageTk.PhotoImage(image=bg)
bg_lbl=Label(app,text='bg',image=bgn)
bg_lbl.place(x = 0, y = 0)'''
import customtkinter  # <- import the CustomTkinter module

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = Label(master=app,text='Testing123')
button.place(relx=0.5, rely=0.5, anchor=CENTER)

ttk.Button(app,text='Hello World').pack()

"""
from accesories import bg
bg.set('angular','#56743','#89876',watermark=0)"""
def darkmodeon():
    app.destroy()
    from views import dark
    Label(dark.window,text='Hello World').pack()
    dark.root.mainloop()
if darkdetect.isDark():
    from accesories import setmode
    setmode.SetMode('Dark')
    app.after(3000,lambda:darkmodeon())
app.mainloop()
