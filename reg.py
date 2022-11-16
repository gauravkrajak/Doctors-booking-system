import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql


class register:
    def __init__(self,root):
    
        self.root=root
        self.root.title("Registration Page")
        self.root.geometry("700x540")
        self.root.config(background="#ffffff")

        #bg image

        self.bg=PhotoImage(file="6.png")

        bck=Label(
            self.root,
            image=self.bg,

        )

        bck.pack()

        #====registerframe===

        frame1=Frame(self.root,bg="white")
        frame1.place(x=200,y=100,width=300,height=400)

        title= Label(
            frame1,
            text="REGISTER HERE",
            font=("times new roman",15,"bold"),
            bg="white",
            fg="green"

        )


        title.pack(pady=(10,20))


        #====username

        
        name= Label(
            frame1,
            text="User Name",
            font=("times new roman",12,"bold"),
            bg="white",
            fg="grey",
            
            

        )

        name.place(x=50,y=500)
        name.pack()

        #user name block
        self.var_fname=StringVar()
        self.txt_name=Entry(
        frame1,
        font=("times new roman",15),
        bg="lightgray",
        textvariable=self.var_fname
        )
        self.txt_name.place(x=150,y=100,width=150)

        self.txt_name.pack(pady=(0,20))


        #====email

        email= Label(
            frame1,
            text="Email",
            font=("times new roman",12,"bold"),
            bg="white",
            fg="grey",
            

        )
        email.pack()

        #user name block
        self.var_email=StringVar()
        self.txt_email=Entry(
        frame1,
        font=("times new roman",15),
        bg="lightgray",
        textvariable=self.var_email
        )

        self.txt_email.pack(pady=(0,20))


        #===password

        password= Label(
            frame1,
            text="Password",
            font=("times new roman",12,"bold"),
            bg="white",
            fg="grey",
            

        )
        password.pack()

        #user name block
        self.var_passwd = StringVar()
        self.txt_password=Entry(
        frame1,
        font=("times new roman",15),
        bg="lightgray",
        textvariable=self.var_passwd
        )

        self.txt_password.pack(pady=(0,20))

        #check t & c
        self.var_chk=IntVar()
        chk=Checkbutton(
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
            font=("times new roman",15,"bold"),
            command=self.register_data,
           # command=self.loginn

            ).place(x=260, y=420)

   # def loginn(self):

    def clear(self):
        self.chk.delete(0, END)
        self.var_email.delete(0, END)
        self.var_fname.delete(0, END)
        self.txt_password.delete(0, END)

    def register_data(self):

        # self.clear(self)
        print(self.var_chk.get())
        if self.var_fname.get() == "":
            messagebox.showerror('Username', 'Username required')
        elif self.var_chk.get() == 1:

            con = pymysql.connect(host="localhost", user="root", password="", database="student")
            print(con)
            cur = con.cursor()
            cur.execute("insert into employee(name,email,password) values(%s,%s,%s)",
                        (
                            self.var_fname.get(),
                            self.var_email.get(),
                            self.var_passwd.get()
                        ))

            con.commit()
            con.close()
            self.root.destroy()
            import loginn
        else:
            messagebox.showerror('Register', 'Please agree terms and conditions.', parent=self.root)


root = tkinter.Tk()
obj=register(root)
root.mainloop()

