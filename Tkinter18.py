#########################           --------------------------------------------------            #########################
#########################           Adding Graph to Tkinter Window using a matplotlib             #########################
#########################                         and Running it Live                             #########################
#########################           --------------------------------------------------            #########################

import matplotlib
matplotlib.use("TkAgg") ## This can be considered as the back-end of the matplot-lib
from matplotlib.backends.backend_tkapp import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style


from tkinter import *
import tkinter as tk
from tkinter import ttk


LARGE_FONT = ('Arial', 12)
style.use("ggplot")

f = Figure(figsize=(5,4), dpi=100)
a = f.add_subplot(111)

def animate(i):
    pullData = open('TestData.txt','r').read() ## To check the graph live keep changing the txt document and the changes would be visible
    dataArray = pullData.split('\n')
    xar=[]
    yar=[]
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    a.clear()
    a.plot(xar,yar)

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
        for F in (StartPage, PageOne, PageTwo, PageThree):
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

        button2 = ttk.Button(self, text = 'Visit Graph Page', command = lambda: controller.show_frame(PageThree))

        button2.pack()



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


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "Welcome To The Graph Page", font = LARGE_FONT)
        label.pack(padx = 10, pady = 10)


        button1 = ttk.Button(self, text = 'Home Page', command = lambda: controller.show_frame(StartPage))

        button1.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111) ## 111 means 1 by 1 (222 - means 2 by 2)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5]) ## in first [] cordinates of x axis are mentioned but in second[] cordinates of y axis are mentioned

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = SeaofBTCapp()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()



