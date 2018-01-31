from tkinter import *

root = Tk()

label1 = Label(root, text="Name")
label2 = Label(root, text="Password")

entry1 = Entry(root)  ## Asking to enter some sort of information
entry2 = Entry(root)

label1.grid(row=0, sticky=E)  ##By Default it will go to column 0, not necessary to mention atleast for the first time
label2.grid(row=1, sticky=E)  ## Grid is similar to pack, used for packing up the window

## Sticky refers to the alignment if E it means east similarly N,W,S for north west and south

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

checkButton1 = Checkbutton(root, text="Keep me Logged in")  ## It is used to create a CheckButton
checkButton1.grid(columnspan=3)  ## columnspan is used to merge column lets say if it's 2 then column 1 and 2 will be merged

root.mainloop()
