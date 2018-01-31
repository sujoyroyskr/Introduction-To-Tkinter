from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1 TF", fg="red")
button2 = Button(topFrame, text="Button 2 TF", fg="blue")
button3 = Button(bottomFrame, text="Button 3 BF", fg="green")
button4 = Button(bottomFrame, text="Button 4 BF", fg="yellow")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=RIGHT)
button4.pack(side=RIGHT)


root.mainloop()
