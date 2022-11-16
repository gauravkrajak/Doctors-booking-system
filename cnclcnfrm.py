import tkinter
from tkinter import *


class login:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Page")
        self.root.geometry("700x555")
        self.root.config(background="#ffffff")

        labeltext = Label(
            self.root,
            text="Your Appointment Is Successfully Cancelled",
            font=("Comic sans MS", 15, "bold"),
            # background = "#ffffff",
            background="sky blue",
            foreground="red",
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
        frame1.place(x=150, y=150, width=400, height=250)

        email = Label(
            frame1,
            text="You Will Recieve Your Confirmation Via Email",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",

        )

        email.pack()

        self.img1 = PhotoImage(file="16.png")

        labelimage = Label(
            frame1,
            image=self.img1,
            background="#ffffff",
        )

        labelimage.pack(padx=(30, 10))


    def welcomee(self):
        self.root.destroy()
        import welcome

    def registerr(self):
        self.root.destroy()
        import reg

    def login(self):
        print(self.txt_email.get(), self.txt_password.get())


root = tkinter.Tk()
obj = login(root)
root.mainloop()

