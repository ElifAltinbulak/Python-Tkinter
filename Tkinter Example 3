import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename
def fopen():
    filepath=askopenfilename(
        filetypes=[("Text Files", "*.txt"),("All Files","*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text=input_file.read()
        txt_edit.insert(tk.END, text)
    fırst.title(f"Text Editor - {filepath}")
def fsave():
    filepath=asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"),("All Files", "*.*")], )
    if not filepath:
        return
    with open(filepath,"w") as output_file:
        text=txt_edit.get(1.0, tk.END)
        output_file.write(text)
    fırst.title(f"Text Editor - {filepath}")
fırst=tk.Tk()
fırst.title(f"Text Editör")
fırst.rowconfigure(0,minsize=480,weight=1)
fırst.columnconfigure(1,minsize=480,weight=1)
txt_edit=tk.Text(fırst)
frame=tk.Frame(fırst, relief=tk.RAISED,bd=2)
b_open=tk.Button(frame,text="Open",command=fopen)
b_save=tk.Button(frame,text="Save As...",command=fsave)

frame.grid(row=0,column=0,sticky="ns")
txt_edit.grid(row=0,column=1,sticky="nsew")
b_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
b_save.grid(row=1,column=0,sticky="ew",padx=5)
fırst.mainloop()
