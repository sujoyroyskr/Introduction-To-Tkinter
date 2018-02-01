from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100) ## This creates a canvas for a user to draw frames, shapes, etc.
canvas.pack()

Line1 = canvas.create_line(0, 0, 150, 50) ## this creates a line with 0,0 - starting point on x and y axis and 150,50 - ending point on x and y axis
Line2 = canvas.create_line(0, 100, 150, 50, fill='red') ## fill here is to mention the color of the line drawn if not mentioned then by default it displays black.

## Drawing a rectangle
Rectangle1 = canvas.create_rectangle(50, 50, 100, 100, fill = 'yellow')

## In case to delete a line or anything else

## canvas.delete(Line2) -- This deletes Line2
## canvas.delete(ALL) -- This deletes everything created 

root.mainloop()
