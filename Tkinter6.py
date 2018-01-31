from tkinter import *

## Start Using classes

class TkinterButton:  ##Class Created 

    def __init__(self, master):  ## Root is now Master and further it's called by the frame
        frame = Frame(master)
        frame.pack()

## Creating Buttons inside the frame

        self.printButton = Button(frame, text="Message Printed", command=self.printMessage) ## self.printMessage is another function for printing out the Message 
        self.printButton.pack()

        self.quitButton = Button(frame, text="Quit Task", command=frame.quit) ## frame.quit makes you exit from the window
        self.quitButton.pack()

    def printMessage(self):
        print("This Is GUI with Tkinter")

root = Tk()
class_call = TkinterButton(root) ## An object to call the class
root.mainloop()
