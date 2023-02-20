from tkinter import *
import tkinter
from tkinter import ttk
from methode import *

root=Tk()
root.title("generate Password")
root.geometry("600x500")

def genere():
    lent=int(spin_box.get())
    password.delete(0,END)
    password.insert(0,generate_password(lent))


 
fenetre=Frame(root ,bg="#b02750",width=600,height=500)
fenetre.pack()



titre = Label(fenetre,text="Password Generator",font=("Arial",20),bg="#b02750",fg="white")
titre.pack()

lent=Label(fenetre,text="Length",font=("Arial",15),bg="#b02750",fg="white")
lent.pack()

current_value = tkinter.StringVar(value=8)
spin_box = ttk.Spinbox(
    fenetre,
    from_= 2,
    to=30,
    textvariable=current_value,
    wrap=True)

spin_box.pack()
fenetre2=Frame(fenetre ,bg="green")
fenetre2.pack(padx=100 ,pady=60)

password=Entry(fenetre2,font=("Arial",15),bg="green",fg="white")
password.pack()

generer=Button(fenetre,text="Generate",font=("Arial",15),bg="green",fg="white",command=lambda:genere())
generer.pack()






root.mainloop()