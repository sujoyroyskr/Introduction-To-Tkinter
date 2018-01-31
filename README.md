# Introduction-To-Tkinter
An introduction to Tkinter, which can be used to make GUI Applications in python.

Tkinter is Python's de-facto standard GUI (Graphical User Interface) package. It is a thin object-oriented layer on top of Tcl/Tk.

The Tkinter module (“Tk interface”) is the standard Python interface to the Tk GUI toolkit. Both Tk and Tkinter are available on most Unix platforms, as well as on Windows systems. (Tk itself is not part of Python; it is maintained at ActiveState.)


# Installing In Mac

Firstly install Pythyon on your System..........

Run the installer and follow along. You'll end up with a fresh install of ActivePython in /Library/Frameworks, along with links to the versioned Python binaries placed in /usr/local/bin (e.g. 'python3.4' if you downloaded ActivePython 3.4.x). From a Terminal window you should then be able to run a Python shell:

% /usr/local/bin/python3.4

Now, in the Python Command Prompt....

>>> import tkinter
>>> tkinter._test()

This should pop up a small window; the first line at the top of the window should say "This is Tcl/Tk version 8.5"; make sure it is not 8.4!

>>> tkinter.Tcl().eval('info patchlevel')


# Installing On Windows

In, windows after installing python, in the Pycharm/Idle (or Which-ever you are using)
Just import everything from tkinter

>>> from tkinter import *
