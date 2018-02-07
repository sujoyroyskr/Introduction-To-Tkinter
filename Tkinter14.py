from tkinter import *
import tkinter as tk

LARGE_FONT = ('Arial', 12)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side = 'top', fill = 'both', expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        
        frame = StartPage(container, self)

        self.frames [StartPage] = frame

        frame.grid(row = 0, column = 0, sticky = 'nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

## ------- This Meathod Is Independent Of the Above Class ------- ##

## def Button():            ## Use this When not using lambda
   ## print("Welcome To Advance Tkinter")



def Button(btprint): ## Use This While using Lambda to Print
    print(btprint)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Welcome To Advance Tkinter", font = LARGE_FONT)
        label.pack(padx = 10, pady = 10)

        ## button1 = tk.Button(self, text = 'Click Me', command=Button)    ## Use this when not using lambda

        button1 = tk.Button(self, text = 'Click Me', command = lambda: Button("Welcome To Tkinter Using Labmda"))
        
        button1.pack()


app = SeaofBTCapp()
app.mainloop()
        
    
