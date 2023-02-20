from tkinter import *

root=Tk()
root.title("generate Password")
root.geometry("600x500")
root.config(bg="#b02750")

titre = Label(root,text="Password Generator",font=("Arial",20),bg="#b02750",fg="white")
titre.pack()

lent=Label(root,text="Length",font=("Arial",15),bg="#b02750",fg="white")
lent.pack()


root.mainloop()