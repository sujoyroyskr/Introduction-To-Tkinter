from tkinter import *   ## This is to import everything from Tkinter

root = Tk()  ## This is mainly to give a proper Structure to your application 

topFrame = Frame(root) ## Top frame is top half of the Screen which is assigned to root(GUI structure), Frame creates an empty screen to work on.
topFrame.pack()
bottomFrame = Frame(root) ## Bottom Frame is the bottom half of the screen.
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1 TF", fg="red")  ## Creating Button on top frame, giving the text color using fg(fore-ground).
button2 = Button(topFrame, text="Button 2 TF", fg="blue")
button3 = Button(bottomFrame, text="Button 3 BF", fg="green")
button4 = Button(bottomFrame, text="Button 4 BF", fg="yellow")

button1.pack(side=LEFT)  ## To run the things you made it's important to pack your things and inside the pack side=LEFT means that the button is going to be on the left side of the screen followed by the others irrespective of the frame.
button2.pack(side=LEFT)
button3.pack(side=RIGHT)
button4.pack(side=RIGHT)


root.mainloop()

## In Laymann terms, finally to wrap the things up you need to run your created GUI Structure in an infinte loop.
