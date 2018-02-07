#########################           --------------------------------------------------            #########################
#########################           This One is to Show The Styling of GUI using ttk              #########################
#########################           --------------------------------------------------            #########################

from tkinter import *
import tkinter as tk
from tkinter import ttk

LARGE_FONT = ('Arial', 12)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        ## tk.Tk.iconbitmap(self, default="IconImg.ico")    ## This Function changes icon in the output window
        tk.Tk.wm_title(self, "Welcome to Intermediate Version Of Tkinter")  ## This Function changes title in the output window

        container = tk.Frame(self)
        container.pack(side = 'top', fill = 'both', expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

## ------ This for loop makes this function run for every page which you made ----------- ## 
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames [F] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text = "Welcome To Advance Tkinter", font = LARGE_FONT)
        label.pack(padx = 10, pady = 10)


        button = ttk.Button(self, text = 'Visit Page 1', command = lambda: controller.show_frame(PageOne))

        button.pack()

        button1 = ttk.Button(self, text = 'Visit Page 2', command = lambda: controller.show_frame(PageTwo))

        button1.pack()



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "Welcome To Page 1 of Tkinter", font = LARGE_FONT)
        label.pack(padx = 10, pady = 10)


        button1 = ttk.Button(self, text = 'visit Page 2', command = lambda: controller.show_frame(PageTwo))

        button1.pack()

        button2 = ttk.Button(self, text = 'Back to StartPage', command = lambda: controller.show_frame(StartPage))

        button2.pack()



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "Welcome To Page 2 of Tkinter", font = LARGE_FONT)
        label.pack(padx = 10, pady = 10)


        button1 = ttk.Button(self, text = 'visit Page 1', command = lambda: controller.show_frame(PageOne))

        button1.pack()

        button2 = ttk.Button(self, text = 'Back to StartPage', command = lambda: controller.show_frame(StartPage))

        button2.pack()


app = SeaofBTCapp()
app.mainloop()
        
    
