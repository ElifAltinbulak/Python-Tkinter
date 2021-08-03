#day34
from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("LİST")
window.geometry("400x300")

f=Frame(window)
f.grid()

l=Listbox(f)
l.insert(1,"Reading")
l.insert(2,"Writing")
l.insert(3,"Listening")
l.insert(4,"Speaking")
l.grid(padx=110,pady=10)
window.mainloop()
