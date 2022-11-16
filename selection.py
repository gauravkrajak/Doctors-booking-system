import tkinter
from tkinter import *
global root
import json


class selection:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Page")
        self.root.geometry("2000x800")
        self.root.config(background="#ffffff")

        #======welcome
        self.welcome= Label(
            self.root,
            text="Choose Your Preference",
            font=("forte",50,"bold"),
            background = "sky blue",
            foreground = "orange",
            width="400"

        )
        self.welcome.pack()

        # bg image

        self.bg = PhotoImage(file="10.png")

        bck = Label(
            self.root,
            image=self.bg,

        )

        bck.pack()

        # ====registerframe===

        frame1 = Frame(self.root, bg="white")
        frame1.place(x=150, y=200, width=300, height=400)

        title = Label(
            frame1,
            text="Dental Treatment",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="green"

        )

        title.pack(pady=(0, 5))

        self.img1 = PhotoImage(file="7.png")

        labelimage = Label(
            frame1,
            image=self.img1,
            background="#ffffff",
        )

        labelimage.pack(padx=(40, 10))

        Button(
            self.root,
            text="Book Appointment",
            padx=10,
            pady=10,
            width=12,
            bg="green",
            fg="black",
            font=("times new roman", 15, "bold"),
            command=self.dental,
            # command=self.loginn

        ).place(x=225, y=520)

        frame2 = Frame(self.root, bg="white")
        frame2.place(x=650, y=200, width=300, height=400)

        title = Label(
            frame2,
            text="Ortho Treatment",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="green"

        )

        title.pack(pady=(10, 5))

        self.img2 = PhotoImage(file="8.png")

        labelimage = Label(
            frame2,
            image=self.img2,
            background="#ffffff",
        )

        labelimage.pack(padx=(40, 10))

        Button(
            self.root,
            text="Book Appointment",
            padx=10,
            pady=10,
            width=12,
            bg="green",
            fg="black",
            font=("times new roman", 15, "bold"),
            command=self.ortho,
            # command=self.loginn

         ).place(x=710, y=520)

        frame3 = Frame(self.root, bg="white")
        frame3.place(x=1100, y=200, width=300, height=400)

        title = Label(
            frame3,
            text="Multi Specilist",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="green"

        )

        title.pack(pady=(10, 5))

        self.img3 = PhotoImage(file="9.png")

        labelimage = Label(
            frame3,
            image=self.img3,
            background="#ffffff",
        )

        labelimage.pack(padx=(40, 10))

        Button(
            self.root,
            text="Book Appointment",
            padx=10,
            pady=10,
            width=12,
            bg="green",
            fg="black",
            font=("times new roman", 15, "bold"),
            command=self.multis,
            # command=self.loginn

        ).place(x=1170, y=520)



        # ====username

    # def loginn(self):

    def clear(self):
        self.chk.delete(0, END)
        self.var_email.delete(0, END)
        self.var_fname.delete(0, END)
        self.txt_password.delete(0, END)


    def dental(self):
        self.root.destroy()
        import dentaldr

    def ortho(self):
        self.root.destroy()
        import orthodr

    def multis(self):
        self.root.destroy()
        import multidr


root = tkinter.Tk()
obj = selection(root)
root.mainloop()