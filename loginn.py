import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox

email= ''
class login:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Page")
        self.root.geometry("700x555")
        self.root.config(background="#ffffff")

        labeltext = Label(
            self.root,
            text="Book Your Appointment With Doctor",
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

        login = Label(
            frame1,
            text="LOGIN HERE",
            font=("times new roman", 17, "bold"),
            bg="white",
            fg="green"

        )

        login.pack(pady=(10, 20))

        email = Label(
            frame1,
            text="Email",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="grey",

        )

        email.pack()

        self.var_idd = StringVar()
        self.txt_email=Entry(
        frame1,
        font=("times new roman",15),
        bg="lightgray",
        textvariable=self.var_idd
        )
        # txt_name.place(x=150,y=100,width=150)

        self.txt_email.pack(pady=(0, 20))

        password = Label(
            frame1,
            text="Password",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="grey",

        )
        password.pack()

        #user name block
        self.var_pass = StringVar()
        self.txt_password=Entry(
        frame1,
        show='*',
        font=("times new roman",15),
        bg="lightgray",
        textvariable=self.var_pass
        )

        self.txt_password.pack(pady=(0,20))


        Button(
            self.root,
            text="Sign In",
            padx=6,
            pady=6,
            width=8,
            bg="green",
            fg="black",
            font=("times new roman", 14, "bold"),
            command=self.welcomee
        ).place(x=290, y=400)

        Button(
            self.root,
            text="Sign Up",
            padx=5,
            pady=5,
            width=7,
            bg="light green",
            fg="black",
            font=("times new roman", 10, "bold"),
            command=self.registerr
        ).place(x=420, y=460)

    def welcomee(self):


        con = pymysql.connect(host="localhost", user="root", password="", database="student")
        print(con)
        cur = con.cursor()
        cur.execute(f'select password from employee where email = "{self.var_idd.get()}"')
        password = cur.fetchall()
        print(password)

        if ((self.var_pass.get(),),) == password:
            messagebox.showinfo('Login', 'logged in successfully.')
            self.root.destroy()
            cur.execute(f'select phone from employee where email = "{self.var_idd.get()}"')
            phone = cur.fetchall()
            print(phone)
            if str(phone) == "(('',),)":

                import booking2
            else:
                import booking



        else:
            messagebox.showerror('Error', 'Please enter correct Email or Password', parent=self.root)
            #  else:

    #     messagebox.showerror('Login','Please agree to the terms and conditions',parent=self.root)

    def registerr(self):
        self.root.destroy()
        import reg

    def login(self):
        print(self.txt_email.get(), self.txt_password.get())


root = tkinter.Tk()
obj = login(root)
root.mainloop()
