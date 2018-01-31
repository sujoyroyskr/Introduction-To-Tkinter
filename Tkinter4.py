from tkinter import *

root = Tk()

##Binding Functions to User Interface

def printName():  ##Function Created
    print("Welcome to TKinter")

button1 = Button(root, text="Click to know What's Inside", command=printName) ##Check the Output in Console, command is used to bind that function with the layout
button1.pack()

## Another Way to Doing the same thing
## def printName(event):
##    print("Welcome to TKinter")

##button1 = Button(root, text="Click to know What's Inside")
##button1.bind("<Button-1>", printName)
##button1.pack()




root.mainloop()
