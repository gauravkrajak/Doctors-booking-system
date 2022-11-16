import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox

class loginnn:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Page")
        self.root.geometry("700x555")
        self.root.config(background="#ffffff")

        labeltext = Label(
            self.root,
            text="Welcome Back",
            font=("Comic sans MS", 24, "bold"),
            # background = "#ffffff",
            background="sky blue",
            foreground="saddle brown",
            width="400",
        )
        labeltext.pack()

        # bg image

        self.bg = PhotoImage(file="5.png")

        bck = Label(
            root,
            image=self.bg,

        )
        bck.pack()

        frame1 = Frame(root, bg="white")
        frame1.place(x=200, y=150, width=300, height=350)

        self.img1 = PhotoImage(file="14.png")

        labelimage = Label(
            frame1,
            image=self.img1,
            background="#ffffff",
        )

        labelimage.pack(pady=(10, 0))

        Button(
            self.root,
            text="New appointment",
            padx=40,
            pady=6,
            width=8,
            bg="green",
            fg="black",
            font=("times new roman", 14, "bold"),
            command=self.neww
        ).place(x=270, y=300)

        Button(
            self.root,
            text="Cancel Appointment",
            padx=40,
            pady=6,
            width=8,
            bg="red",
            fg="black",
            font=("times new roman", 14, "bold"),
            command=self.registerr
        ).place(x=270, y=400)

    #def welcomee(self):

    def registerr(self):
        self.root.destroy()
        import cancel




    def neww(self):
        self.root.destroy()
        import selection



root = tkinter.Tk()
obj = loginnn(root)
root.mainloop()
