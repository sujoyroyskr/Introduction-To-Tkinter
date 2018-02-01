from tkinter import *
## Display Message on a Dialouge Box 

import tkinter.messagebox ## tHIS IMPORTS the message dialouge box

root = Tk()

tkinter.messagebox.showinfo("Welcome To Tkinter (This is Title)", "Welcome To the introduction of Tkinter") ## This shows a dialouge box with a title name and a message
 
answer = tkinter.messagebox.askquestion("Entry Level 1", "Are you interested in Learning Tkinter?")  ## This asks a Yes or No question and prints output on console
if answer == 'Yes':
    print('You are at the right Place....')

if answer == 'No':
    print('Better Try Someother GUI')    

root.mainloop()
