import tkinter
from tkinter import *
from tkinter import messagebox

global root
import json


class selection:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Page")
        self.root.geometry("2000x800")
        self.root.config(background="#ffffff")

        # ======welcome
        self.welcome = Label(
            self.root,
            text="Available Multi Specilist Doctors",
            font=("forte", 50, "bold"),
            background="sky blue",
            foreground="orange",
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
            text="Dr. Saneha",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="green"

        )

        title.pack(pady=(0, 5))

        self.img1 = PhotoImage(file="12.png")

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
            command=self.sneha,
            # command=self.loginn

        ).place(x=225, y=520)

        frame2 = Frame(self.root, bg="white")
        frame2.place(x=650, y=200, width=300, height=400)

        title = Label(
            frame2,
            text="Dr. Yash",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="green"

        )

        title.pack(pady=(0, 5))

        self.img2 = PhotoImage(file="13.png")

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
            command=self.yash,
            # command=self.loginn

        ).place(x=710, y=520)

        frame3 = Frame(self.root, bg="white")
        frame3.place(x=1100, y=200, width=300, height=400)

        title = Label(
            frame3,
            text="Dr. Arman",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="green"

        )

        title.pack(pady=(10, 5))

        self.img3 = PhotoImage(file="11.png")

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
            command=self.arman,
            # command=self.loginn

        ).place(x=1170, y=520)

        # ====username
        ''' 

        name = Label(
            frame1,
            text="User Name",
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="grey",

        )

        name.place(x=50, y=500)
        name.pack()

        # user name block
        self.var_fname = StringVar()
        self.txt_name = Entry(
            frame1,
            font=("times new roman", 15),
            bg="lightgray",
            textvariable=self.var_fname
        )
        self.txt_name.place(x=150, y=100, width=150)

        self.txt_name.pack(pady=(0, 20))

        # ====email

        email = Label(
            frame1,
            text="Email",
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="grey",

        )
        email.pack()

        # user name block
        self.var_email = StringVar()
        self.txt_email = Entry(
            frame1,
            font=("times new roman", 15),
            bg="lightgray",
            textvariable=self.var_email
        )

        self.txt_email.pack(pady=(0, 20))

        # ===password

        password = Label(
            frame1,
            text="Password",
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="grey",

        )
        password.pack()

        # user name block

        self.txt_password = Entry(
            frame1,
            font=("times new roman", 15),
            bg="lightgray",
        )

        self.txt_password.pack(pady=(0, 20))

        # check t & c
        self.var_chk = IntVar()
        chk = Checkbutton(
            frame1,
            text="I Agree The Terms & Conditions",
            bg="white",
            variable=self.var_chk,
            onvalue=1,
            offvalue=0,

        )
        chk.pack()

        Button(
            self.root,
            text="REGISTER",
            padx=10,
            pady=10,
            width=12,
            bg="green",
            fg="black",
            font=("times new roman", 15, "bold"),
            command=self.register_data,
            # command=self.loginn

        ).place(x=260, y=420)

        '''

    # def loginn(self):

    def clear(self):
        self.chk.delete(0, END)
        self.var_email.delete(0, END)
        self.var_fname.delete(0, END)
        self.txt_password.delete(0, END)

    def register_data(self):
        print(self.var_fname.get())
        print(self.var_email.get())
        print(self.txt_password.get())
        if self.var_chk.get() == 0:
            messagebox.showerror("error", "Please Agree our terms & condition", parent=self.root)
        # self.clear(self)
        self.root.destroy()
        import login

    def sneha(self):
        self.root.destroy()
        import drSaneha
    def yash(self):
        self.root.destroy()
        import drYash
    def arman(self):
        self.root.destroy()
        import DrArman



root = tkinter.Tk()
obj = selection(root)
root.mainloop()