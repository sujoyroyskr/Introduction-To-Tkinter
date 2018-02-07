from tkinter import *
from tkinter import ttk

## ---------------------- Place Geometry Manager -------------------- ##
root = Tk()

root.geometry('640x480+200+200') ## ('pixcels * pixcels + x-cordinate + y-cordinate')

ttk.Label(root, text = "Hey", background = 'green').place(x = 100, y = 50)
ttk.Label(root, text = "Welcome", background = 'red').place(relx = 0.5, rely = 0.5, anchor = 'center')
ttk.Label(root, text = "Tkinter", background = 'grey').place(relx = 0.5, x = 100, rely = 0.5, y = 50)
ttk.Label(root, text = "Python 3.6", background = 'orange').place(relx = 1.0, x = -5, y = 5, anchor = 'ne')


root.mainloop()
