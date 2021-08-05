import tkinter as tk
import xlsxwriter
window=tk.Tk()
window.geometry("200x200")
window.title("ögrenci")
def kayıt():
    planWorkbook=xlsxwriter.Workbook("kayıt.xlsx")
    planSheet=planWorkbook.add_worksheet("ogrenci")
    satır=[ogrenciadsoyad.get(),ogrencino.get(),okuladı.get()]
    planSheet.write("A1","Öğrenci Adı Soyadı")
    planSheet.write("B1","Öğrenci No")
    planSheet.write("C1","Okul Adı")

    planSheet.write("A2",satır[0])
    planSheet.write("B2",satır[1])
    planSheet.write("C2",satır[2])
    planWorkbook.close()

label1=tk.Label(window,text="Öğrenci Adı Soyadı")
ogrenciadsoyad=tk.Entry(window)
label2=tk.Label(window,text="Öğrenci No")
ogrencino=tk.Entry(window)
label3=tk.Label(window,text="Okul Adı")
okuladı=tk.Entry(window)

buton=tk.Button(window,text="Kaydet",command=kayıt)
label1.pack()
ogrenciadsoyad.pack()
label2.pack()
ogrencino.pack()
label3.pack()
okuladı.pack()
buton.pack()
