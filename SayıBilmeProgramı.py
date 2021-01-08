#Sayı Tahmin Programı
import random
sayı = random.randint(0,100)
hak = int(input("Hakınnızı belirleyiniz : "))
sayac = 1
puan = 100
while hak>0:
    tahmin = int(input("Sayı :"))
    if tahmin == sayı:
        print(f"Tebrikler, {sayac}. tahminde bildiniz")
        print(f"{puan-(20)*(sayac-1)}")
        break
    elif tahmin>sayı:
        print("Aşağı")
    else :
        print("Yukarı")
    sayac+=1
    hak-=1
    if hak == 0 and puan == 0:
        print(f"Hakkınız bitti Üzgünüm tuttuğum sayı, {sayı},puanınız : {puan}")
