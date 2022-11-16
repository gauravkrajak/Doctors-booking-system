import tkinter
from tkinter import *

class welcme:
    def __init__(self,root):

        self.root=root
        self.root.title("welcome Page")
        self.root.geometry("700x470")
        self.root.config(background="#ffffff")


        #======welcome
        self.welcome= Label(
            self.root,
            text="welcome",
            font=("forte",50,"bold"),
            background = "sky blue",
            foreground = "orange",
            width="400"

        )
        self.welcome.pack()

        #bg image

        self.bg=PhotoImage(file="4.png")

        bck=Label(
            self.root,
            image=self.bg,

        )
 

        bck.pack(padx=(0,300))
       #frame===

        frame1=Frame(self.root,bg="white")
        frame1.place(x=400,y=100,width=300,height=260)

        self.img1 = PhotoImage(file="logo.png")

        labelimage = Label(
            frame1,
            image = self.img1,
            background = "#ffffff",
        )
        #labelimage.place(x=500,y=50),
        labelimage.pack(pady=(50,0))


        Button(
            self.root,
            text="START",
            padx=10,
            pady=10,
            width=12,
            bg="green",
            fg="black",
            font=("castellar",15,"bold"),
            command=self.welcomee
            ).place(x=450, y=400)

    def welcomee(self):
        self.root.destroy()
        import login

root=tkinter.Tk()
obj=welcme(root)
root.mainloop()