from tkinter import *

root = Tk()

one = Label(root, text="Label 1", bg="black", fg="white") ## Label creates a Label, in this case its created in root which is it's GUI Structure.
one.pack()

two = Label(root, text="Label 2", bg="red", fg="white")
two.pack(fill=X)

three = Label(root, text="Label 3", bg="violet", fg="white")
three.pack(side=LEFT, fill=Y)

root.mainloop()
