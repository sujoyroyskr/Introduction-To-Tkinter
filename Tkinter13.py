from tkinter import *
from tkinter import ttk

root = Tk()

## ------- Event Binding -----------##

## ------- This Function Mainly Creates an entry event --------- ##
entry = ttk.Entry(root)
entry.pack()

entry.bind('<<Copy>>', lambda e: print('copy')) ## This function is for Copy Event.
entry.bind('<<Paste>>', lambda e: print('Paste')) ## This function is for Paste Event.

## ----------- Here, is a new Function that triggers odd Numbers ---------- ##
entry.event_add('<<OddNumber>>', '1','3', '5','7', '9')
entry.bind('<<OddNumber>>', lambda e: print('This is Odd Number'))

## --------- This Event prints the event OddNumber which was called Above ---------- ##
## print(entry.event_info('<<OddNumber>>'))

## ---------- This event auto-generates both the events mentioned below --------------##
## entry.event_generate('<<OddNumber>>')
## entry.event_generate('<<Paste>>')

## ------ This event deletes the OddNumber Event ----------------- ##
## entry.event_delete('<<OddNumber>>')


root.mainloop()
