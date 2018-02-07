from tkinter import *
from tkinter import ttk
from tkinter import messagebox


## ------------------------------- Making Of a FeedBack Form ------------------- ##
class Feedback:

    def __init__(self, master):

        master.title("Welcome To Tkinter")
        master.resizable(False, False)
        master.configure(background = 'eld8b9')

        self.style = ttk.Style()
        self.style.configure('TFrame', background = 'eld8b9')
        self.style.configure('TButton', background = 'eld8b9')
        self.style.configure('TLabel', background = 'eld8b9', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))
        
        
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.logo_image = PhotoImage(file = "D:\\Users\\850034273\\Desktop\\Tkinter\\image.png")
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspam = 2)
        ttk.Label(self.frame_header, text = "Welcome To Introduction Of Tkinter", style = 'Header.Tlabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300,
                  text = "Welcome To Tkinter, for more codes and Documentation, "
                         " Check out main repository in Github.").grid(row = 0, column = 2)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(slef.frame_header, text = 'Name: ').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(slef.frame_header, text = 'Email: ').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(slef.frame_header, text = 'Comments: ').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

        ttk.entry_name = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        ttk.entry_email = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        ttk.text_comments = Text(self.frame_content, width = 50, height = 10, font = ('Arial', 10))

        self.entry_name.grid(row = 1, column = 0, padx = 5)
        self.entry_email.grid(row = 1, column = 1, padx = 5)
        self.text_comments.grid(row = 3, column = 0, columnspan = 5, padx = 5)

        ttk.Button(self.frame_content, text = 'Submit', command = self.submit).grid(row = 4, column = 0, padx = 5)
        ttk.Button(self.frame_content, text = 'Clear', command = self.clear).grid(row = 4, column = 0, padx = 5)


    def submit(slef):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Comments: {}'.format(self.entry_name.get()))

        



root = Tk()

root.mainloop()
