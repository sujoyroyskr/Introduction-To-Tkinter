from tkinter import *
from matplotlib import pyplot as plt
import math
import numpy as np

def sine_w(c=1):
    x=np.arange(-1*math.pi*2,math.pi*2,0.05)
    y=np.sin(c*x)
    plt.plot(x,y)
    plt.title("sine wave")
    plt.xlabel("angle")
    plt.ylabel("sine")
    plt.show()
    
def cos_w(c=1):
    x=np.arange(-1*math.pi*2,math.pi*2,0.05)
    y=np.cos(c*x)
    plt.plot(x,y)
    plt.title("cos wave")
    plt.xlabel("angle")
    plt.ylabel("cos")
    plt.show()
    
def tan_w(c=1):
    x=np.arange(-1*math.pi*2,math.pi*2,0.05)
    y=np.tan(c*x)
    plt.plot(x,y)
    plt.title("tan wave")
    plt.xlabel("angle")
    plt.ylabel("tan")
    plt.show()

def cot_w(c=1):
    x=np.arange(0,math.pi*2,0.05)
    y=np.tan(c*x)
    plt.plot(x,1/y)
    plt.title("cot wave")
    plt.xlabel("angle")
    plt.ylabel("cot")
    plt.show()

def sec_w(c=1):
    x=np.arange(0,math.pi*2,0.05)
    y=np.cos(c*x)
    plt.plot(x,1/y)
    plt.title("sec wave")
    plt.xlabel("angle")
    plt.ylabel("sec")
    plt.show()

def cosec_w(c=1):
    x=np.arange(0,math.pi*2,0.05)
    y=np.sin(c*x)
    plt.plot(x,1/y)
    plt.title("cosec wave")
    plt.xlabel("angle")
    plt.ylabel("cosec")
    plt.show()




tk=Tk()
tk.title("Tkinter5")

frame=Frame(tk)
frame.pack()

bframe=Frame(tk)
bframe.pack(side=BOTTOM)

cframe=Frame(bframe)
cframe.pack(side=BOTTOM)

but1=Button(tk,text="sine",padx="5px",pady="5px",width=6,font={"Georgia",10,"italic"},background="cyan",activebackground="grey",command=sine_w)
but1.pack(side=LEFT)

but2=Button(tk,text="cos",padx="5px",pady="5px",width=6,font={"Georgia",10,"italic"},background="lightpink",activebackground="grey",command=cos_w)
but2.pack(side=RIGHT)

but3=Button(bframe,text="tan",padx="5px",pady="5px",width=6,font={"Georgia",10,"italic"},background="orange",activebackground="grey",command=tan_w)
but3.pack(side=LEFT)

but4=Button(bframe,text="cot",padx="5px",pady="5px",width=6,font={"Georgia",10,"italic"},background="red",activebackground="grey",command=cot_w)
but4.pack(side=RIGHT)

but5=Button(cframe,text="cosec",padx="5px",pady="5px",width=6,font={"Georgia",10,"italic"},background="lawn green",activebackground="grey",command=cosec_w)
but5.pack(side=LEFT)

but5=Button(cframe,text="sec",padx="5px",pady="5px",width=6,font={"Georgia",10,"italic"},background="sienna1",activebackground="grey",command=sec_w)
but5.pack(side=LEFT)



tk.mainloop()