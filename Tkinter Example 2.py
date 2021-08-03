import tkinter as tk
import random as rnd
def dice():
    label["text"]=rnd.randint(1,6)
fırst = tk.Tk()
fırst.title("Rolling a die!")
fırst.columnconfigure(0,minsize=200)
fırst.rowconfigure(0,minsize=50)

button=tk.Button(text="Roll a die",command=dice)
label=tk.Label()

button.grid(row=0,column=0,ipadx=135,ipady=50)
label.grid(row=1,column=0,ipadx=135,ipady=50)

fırst.mainloop()
