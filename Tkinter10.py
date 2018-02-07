from tkinter import *
from tkinter import ttk  ## ttk is used as a constructor to create a button for your GUI application and also it gives a style to button
                         ## If its button constructor is created without using ttk, it would provide with a older style of button.

def callback():
    print("..........Work in Progress..........")

root = Tk()


## ------ This creates a Normal Label Showing up Some Text --------- ##
label = Label(root, text="Welcome to Tkinter Tutorial")
label.pack()

## -------- This will Create a Button ---------- ##
button = ttk.Button(root, text="Click To Expand", command=callback)

button.state(['disabled']) ## This Function disables the button Function
button.instate(['disabled']) ## This command checks wheather state is in disabled meathod or not
button.state(['!disabled']) ## This Command again enables the button to function

## ------- TO configure Image to button basically image would be used as button ------------- ##
picture = PhotoImage(file = 'D:\\Users\\850034273\\Desktop\\Tkinter\\image.png')
## button.config(image = picture) ## This is to configue image as button

## -------- PhotoImage Object will be used to used to Resize the Image which is used as a Button ------------##
small_picture = picture.subsample(5, 5)  ## This fuction is used to resize the picture to be used as Button.....
button.config(image = small_picture)




button.pack()

root.mainloop()
