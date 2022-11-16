import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
import smtplib as s


class register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Page")
        self.root.geometry("2000x8000")
        self.root.config(background="#ffffff")

        # bg image

        self.bg = PhotoImage(file="10.png")

        bck = Label(
            self.root,
            image=self.bg,

        )

        bck.pack()

        # ====registerframe===

        frame1 = Frame(self.root, bg="white")
        frame1.place(x=420, y=100, width=700, height=500)

        title = Label(
            frame1,
            text="You Are Just One Step Away To Book Your Appointment With Dr. Shivam",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="green"

        )

        title.pack(pady=(10, 20))

        # ====username

        name = Label(
            frame1,
            text="Enter Your Mobile Number",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="grey",

        )

        name.place(x=50, y=500)
        name.pack()

        # user name block
        self.var_fname = StringVar()
        self.txt_name = Entry(
            frame1,
            font=("times new roman", 20),
            bg="lightgray",
            textvariable=self.var_fname
        )
        self.txt_name.place(x=150, y=300, width=150)

        self.txt_name.pack(pady=(0, 20))

        # ====email

        email = Label(
            frame1,
            text="Email",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="grey",

        )
        email.pack()

        # email name block
        self.var_email = StringVar()
        self.txt_email = Entry(
            frame1,
            font=("times new roman", 20),
            bg="lightgray",
            textvariable=self.var_email,
            #state='disabled'
        )

        self.txt_email.pack(pady=(0, 20))


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

        self.img1 = PhotoImage(file="14.png")

        labelimage = Label(
            frame1,
            image=self.img1,
            background="#ffffff",
        )

        labelimage.pack(pady=(10, 0))

        Button(
            self.root,
            text="REGISTER",
            padx=10,
            pady=10,
            width=12,
            bg="green",
            fg="black",
            font=("times new roman", 15, "bold"),
            command=self.confirm,
            # command=self.loginn

        ).place(x=670, y=500)

    # def loginn(self):

    def clear(self):
        self.chk.delete(0, END)
        self.var_email.delete(0, END)
        self.var_fname.delete(0, END)


    def confirm(self):


        print(self.var_fname.get())

        if self.var_email.get() == "":
            messagebox.showerror('Email', 'Username or Email required')

        elif self.var_chk.get() == 1:

            con = pymysql.connect(host="localhost", user="root", password="", database="student")
            print(con)
            cur = con.cursor()
            cur.execute(f'update employee SET phone="{self.var_fname.get()}" where email = "{self.var_email.get()}" ')

            con.commit()
            con.close()
            e = self.var_email.get()
            print(e)

            ob = s.SMTP("smtp.gmail.com", 587)
            ob.starttls()
            ob.login("teamstudentwelfare@gmail.com", "khajuria123")
            subject = "Appointment Booked"
            body = "Congratulations you have successfully booked an appointment with Dr. Shivam .\n #Time :- 5 PM(Tomorrow) .\n You have to reach on time and mask is compulsory for entry .\n Thank you"
            message = "Subject:{}\n\n{}".format(subject, body)
            print(message)
            listofAddress = e
            ob.sendmail("teamstudentfare@gmailcom", listofAddress, message)
            print("send succesfulyy")
            ob.quit()

            self.root.destroy()
            import cnfrm


root = tkinter.Tk()
obj = register(root)
root.mainloop()

