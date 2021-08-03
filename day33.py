from tkinter import *
from tkinter import messagebox
fırst=Tk()
fırst.title("www.yazılım.com")
fırst.geometry("400x300")
uygulama=Frame(fırst)
uygulama.grid()
l=Label(uygulama,text="Adınızı Giriniz")
l.grid(padx=110,pady=10)
e=Entry(uygulama,bd=2)
e.grid(padx=110,pady=3)
fırst.mainloop()
