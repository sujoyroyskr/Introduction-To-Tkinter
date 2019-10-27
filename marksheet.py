#!/usr/bin/python


from tkinter import *
import tkinter
import tkinter.messagebox


def CalcCredit():

    NAME = studentName.get()
    ROLL_NO = 'CSE/'+studentRoll.get()+'/'+regNo.get()
    GRADE_1 = Grade_1.get()
    GRADE_2 = Grade_2.get()
    GRADE_3 = Grade_3.get()
    GRADE_4 = Grade_4.get()
    #print(GRADE_1,GRADE_2,GRADE_3,GRADE_4)

    if GRADE_1 == '' or GRADE_2 == '' or GRADE_3 == '' or GRADE_4 == '':
        tkinter.messagebox.showinfo( "Error!", "No grade can remain empty!")
    if NAME == '' and studentRoll.get() == '' and regNo.get() == '':
        tkinter.messagebox.showinfo( "Error!", "Enter Student details!")
    elif studentRoll.get() == '' and regNo.get() == '':
        tkinter.messagebox.showinfo( "Error!", "Enter Roll & Registration Number!")
    elif NAME == '' and regNo.get() == '':
        tkinter.messagebox.showinfo( "Error!", "Enter Name & Registration Number!")
    elif studentRoll.get() == '' and NAME == '':
        tkinter.messagebox.showinfo( "Error!", "Enter Name & Roll Number!")
    elif NAME == '':
        tkinter.messagebox.showinfo( "Error!", "Enter Name!")
    elif studentRoll.get() == '':
        tkinter.messagebox.showinfo( "Error!", "Enter Roll Number!")
    elif regNo.get() == '':
        tkinter.messagebox.showinfo( "Error!", "Enter Registration Number!")
    else:

        g1,g2,g3,g4 = 0,0,0,0

        if GRADE_1 == 'a' or GRADE_1 == 'A':
            g1=10
        elif GRADE_1 == 'b' or GRADE_1 == 'B':
            g1=9
        elif GRADE_1 == 'c' or GRADE_1 == 'C':
            g1=8
        elif GRADE_1 == 'd' or GRADE_1 == 'D':
            g1=7
        elif GRADE_1 == 'e' or GRADE_1 == 'E':
            g1=6
        elif GRADE_1 == 'f' or GRADE_1 == 'F':
            g1=5
        elif GRADE_1 == 'p' or GRADE_1 == 'P':
            g1=2

        if GRADE_2 == 'a' or GRADE_2 == 'A':
            g2=10
        elif GRADE_2 == 'b' or GRADE_2 == 'B':
            g2=9
        elif GRADE_2 == 'c' or GRADE_2 == 'C':
            g2=8
        elif GRADE_2 == 'd' or GRADE_2 == 'D':
            g2=7
        elif GRADE_2 == 'e' or GRADE_2 == 'E':
            g2=6
        elif GRADE_2 == 'f' or GRADE_2 == 'F':
            g2=5
        elif GRADE_2 == 'p' or GRADE_2 == 'P':
            g2=2

        if GRADE_3 == 'a' or GRADE_3 == 'A':
            g3=10
        elif GRADE_3 == 'b' or GRADE_3 == 'B':
            g3=9
        elif GRADE_3 == 'c' or GRADE_3 == 'C':
            g3=8
        elif GRADE_3 == 'd' or GRADE_3 == 'D':
            g3=7
        elif GRADE_3 == 'e' or GRADE_3 == 'E':
            g3=6
        elif GRADE_3 == 'f' or GRADE_3 == 'F':
            g3=5
        elif GRADE_3 == 'p' or GRADE_3 == 'P':
            g3=2

        if GRADE_4 == 'a' or GRADE_4 == 'A':
            g4=10
        elif GRADE_4 == 'b' or GRADE_4 == 'B':
            g4=9
        elif GRADE_4 == 'c' or GRADE_4 == 'C':
            g4=8
        elif GRADE_4 == 'd' or GRADE_4 == 'D':
            g4=7
        elif GRADE_4 == 'e' or GRADE_4 == 'E':
            g4=6
        elif GRADE_4 == 'f' or GRADE_4 == 'F':
            g4=5
        elif GRADE_4 == 'p' or GRADE_4 == 'P':
            g4=2


        cr1=g1*4
        cr2=g2*4
        cr3=g3*3
        cr4=g4*4

        SGPA = ((cr1+cr2+cr3+cr4)/150)*100

        Obt_1["text"]=cr1
        Obt_2["text"]=cr2
        Obt_3["text"]=cr3
        Obt_4["text"]=cr4
        TOTCRED["text"]=cr1+cr2+cr3+cr4
        SGPA1["text"]=SGPA


        


    #gd1 = StringVar()
top = Tk()
top.configure(background="yellow")
top.title("Marksheet")


Heading = Label(top, text=" MARKSHEET ", font=('algerian',30,'bold italic'), background="yellow", justify="center")
    #Heading.pack()
Heading.grid(row=0, column=2)

Name = Label(top, text="Student's Name: ", font=('Times New Roman',12,'bold italic'), background="yellow")
Name.grid(row=2, column=0)

studentName = Entry(top,font=('arial',12,'bold'), bd=5,insertwidth=4,bg="powder blue")
studentName.grid(row=2, column=1, columnspan=4)

Roll = Label(top, text="Roll No.: ", font=('Times New Roman',12,'bold italic'), background="yellow")
Roll.grid(row=3, column=0)

studentRoll = Entry(top,font=('arial',12,'bold'), bd=5,insertwidth=4,bg="powder blue", justify='right')
studentRoll.grid(row=3, column=1, columnspan=4)


Reg = Label(top, text="Registration No.: ", font=('Times New Roman',12,'bold italic'), background="yellow")
Reg.grid(row=4, column=0)

regNo = Entry(top,font=('arial',12,'bold'), bd=5,insertwidth=4,bg="powder blue", justify='right')
regNo.grid(row=4, column=1, columnspan=4)




    # TABLE



Sl = Label(top, text="Sl. No.", font=('Noto Serif',12,'bold italic'), background="red")
Sl.grid(row=10, ipadx=150)

Sub_cd = Label(top, text="Subject Code", font=('Noto Serif',12,'bold italic'), background="red")
Sub_cd.grid(row=10,column=1, ipadx=100)

Grade = Label(top, text="Grade", font=('Noto Serif',12,'bold italic'), background="red")
Grade.grid(row=10,column=2, ipadx=110)

Crd = Label(top, text="Subject Credit", font=('Noto Serif',12,'bold italic'), background="red")
Crd.grid(row=10,column=3, ipadx=25)

Obt = Label(top, text="Credit Obtained", font=('Noto Serif',12,'bold italic'), background="red")
Obt.grid(row=10,column=4, ipadx=50)



S_1 = Label(top, text="1", font=('Comic Sans',12,'italic'), background="yellow")
S_1.grid(row=12, ipadx=50)
S_1 = Label(top, text="2", font=('Comic Sans',12,'italic'), background="yellow")
S_1.grid(row=13, ipadx=50)
S_1 = Label(top, text="3", font=('Comic Sans',12,'italic'), background="yellow")
S_1.grid(row=14, ipadx=50)
S_1 = Label(top, text="4", font=('Comic Sans',12,'italic'), background="yellow")
S_1.grid(row=15, ipadx=50)


Code = Label(top, text="CS 201", font=('Comic Sans',12,'italic'), background="yellow")
Code.grid(row=12, column=1, ipadx=50)
Code = Label(top, text="CS 202", font=('Comic Sans',12,'italic'), background="yellow")
Code.grid(row=13, column=1, ipadx=50)
Code = Label(top, text="MA 201", font=('Comic Sans',12,'italic'), background="yellow")
Code.grid(row=14, column=1, ipadx=50)
Code = Label(top, text="EC 201", font=('Comic Sans',12,'italic'), background="yellow")
Code.grid(row=15, column=1, ipadx=50)


Grade_1 = Entry(top, font=('Comic Sans',12,'italic'), background="light yellow", justify='center')
Grade_1.grid(row=12, column=2)
gd1=Grade_1.get()
Grade_2 = Entry(top, font=('Comic Sans',12,'italic'), background="light yellow", justify='center')
Grade_2.grid(row=13, column=2)
gd2=Grade_2.get()
Grade_3 = Entry(top, font=('Comic Sans',12,'italic'), background="light yellow", justify='center')
Grade_3.grid(row=14, column=2)
gd3=Grade_3.get()
Grade_4 = Entry(top, font=('Comic Sans',12,'italic'), background="light yellow", justify='center')
Grade_4.grid(row=15, column=2)
gd4a=Grade_4.get()


Code = Label(top, text="4", font=('Comic Sans',12,'italic'), background="yellow")
Code.grid(row=12, column=3, ipadx=50)
Code = Label(top, text="4", font=('Comic Sans',12,'italic'), background="yellow")
Code.grid(row=13, column=3, ipadx=50)
Code = Label(top, text="3", font=('Comic Sans',12,'italic'), background="yellow")
Code.grid(row=14, column=3, ipadx=50)
Code = Label(top, text="4", font=('Comic Sans',12,'italic'), background="yellow")
Code.grid(row=15, column=3, ipadx=50)


Obt_1 = Label(top, text="-", font=('Comic Sans',12,'italic'), background="powder blue")
Obt_1.grid(row=12, column=4, ipadx=50)
Obt_2 = Label(top, text="-", font=('Comic Sans',12,'italic'), background="powder blue")
Obt_2.grid(row=13, column=4, ipadx=50)
Obt_3 = Label(top, text="-", font=('Comic Sans',12,'italic'), background="powder blue")
Obt_3.grid(row=14, column=4, ipadx=50)
Obt_4 = Label(top, text="-", font=('Comic Sans',12,'italic'), background="powder blue")
Obt_4.grid(row=15, column=4, ipadx=50)

TOT_CRED=Label(top, text="TOTAL CREDIT:", font=('Comic Sans',12,'bold'), background="yellow")
TOT_CRED.grid(row=17, column=0, ipadx=50)
TOTCRED= Label(top, text="-", font=('Comic Sans',12,'italic'), background="powder blue")
TOTCRED.grid(row=17, column=1, ipadx=50)

SG=Label(top, text="SGPA:", font=('Comic Sans',12,'bold'), background="yellow")
SG.grid(row=18, column=0, ipadx=50)
SGPA1= Label(top,text="-", font=('Comic Sans',12,'italic'), background="powder blue")
SGPA1.grid(row=18, column=1, ipadx=50)




SUBMIT = Button(top, padx=10, bd=5, font=('arial',12,'bold'), text='Calculate Result', fg='black', command=lambda: CalcCredit(), height=1, width=10)
SUBMIT.grid(row=50, column=2)



top.grid()
top.geometry("1280x720")
top.mainloop()