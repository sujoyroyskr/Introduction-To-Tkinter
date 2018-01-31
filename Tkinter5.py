from tkinter import *

root = Tk()

##Event Mouse Clicked

def leftClick(event):
    print("Mouse Left Click")

def scrollClick(event):
    print("Mouse Scroller Clicked")

def rightClick(event):
    print("Mouse Right Cick")

frame = Frame(root, width=500, height=450)  ## Frame creates an empty page 
frame.bind("<Button-1>", leftClick) 
frame.bind("<Button-2>", scrollClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

root.mainloop()
