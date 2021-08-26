from tkinter import *
import sqlite3
root=Tk()
root.title("Giriş ekranı")
root.geometry("300x100")



def kayıtfunction():
    conn=sqlite3.connect("Adres.db")
    c=conn.cursor()
    a=entry.get()
    b=entry1.get()
    c.execute("CREATE TABLE IF NOT EXISTS kullanıcı (a TEXT,b TEXT)")
    c.execute("INSERT INTO kullanıcı VALUES(?,?)",(a,b))
    
    conn.commit()
    conn.close()

    entry.delete(0, END)
    entry1.delete(0, END)
    
    
    
label=Label(root,text="Kullanıcı Adı")
label1=Label(root,text="Şifre")
entry=Entry(root)
entry1=Entry(root,show="*")
button=Button(root,text="Kayıt",command=kayıtfunction)
error=Message(text="",width=160)
error.pack
error.config(padx=0)
label.place(x=10,y=1)
label1.place(x=10,y=20)
entry.pack()
entry1.pack()
button.pack()

root.mainloop()
