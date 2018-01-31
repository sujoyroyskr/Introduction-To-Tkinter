from tkinter import *


def printThis():  ### A fuction Created For further use
    print("No Functionality Added For Now........Work in Progress")
    
root = Tk()

## Creating Main Menu and its Drop Down Through Tkinter

menu = Menu(root)  ## Menu Bar to be made in root which is the main window
root.config(menu = menu)

subMenu = Menu(menu) ## Creating Submenu inside menu
menu.add_cascade(label="File", menu=subMenu) ## File is the 1st option in the Menu Bar
subMenu.add_command(label="Create New File....", command=printThis) ## SubMenu Created for the File
subMenu.add_command(label="Open File", command=printThis)
subMenu.add_command(label="Class Browser", command=printThis)
subMenu.add_command(label="Path Browser", command=printThis)
subMenu.add_command(label="Recent Opened Files", command=printThis)
subMenu.add_separator() ## Seperator is used to divide the Submenu into sections
subMenu.add_command(label="Save", command=printThis)
subMenu.add_command(label="Save As", command=printThis)
subMenu.add_command(label="Save Copy As", command=printThis)
subMenu.add_separator()
subMenu.add_command(label="Print Window", command=printThis)
subMenu.add_separator()
subMenu.add_command(label="Close", command=printThis)
subMenu.add_command(label="Exit", command=printThis)


subMenu2 = Menu(menu)
menu.add_cascade(label="Edit", menu=subMenu2)
subMenu2.add_command(label="Undo", command=printThis)
subMenu2.add_command(label="Redo", command=printThis)
subMenu2.add_separator()
subMenu2.add_command(label="Cut", command=printThis)
subMenu2.add_command(label="Copy", command=printThis)
subMenu2.add_command(label="Paste", command=printThis)
subMenu2.add_separator()


## Creating Toolbar Menu

toolbar = Frame(root, bg="black") ## Creating Toolbar in root

## Creating Button inside toolbar
insertButton = Button(toolbar, text="Insert New Cell", command=printThis)
insertButton.pack(side=LEFT, padx=2, pady=2)

insertButton2 = Button(toolbar, text="Print New Cell", command=printThis)
insertButton2.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

## Creating Status Bar

status = Label(root, text="Work in Progress.........", bd=1, relief= SUNKEN, anchor=W) ##bd is borden and SUNKEN is to import/merge in screen
status.pack(side=BOTTOM, fill=X)

root.mainloop()
