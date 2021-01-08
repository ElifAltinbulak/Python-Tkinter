#Hesap Makinesi
while True:
    num1=int(float(input("1-")))
    num2=int(float(input("2-")))
    secım = int(input("""1-Toplama
2-Çıkarma
3-Çarpma
4-Bölme
5-Mod
6-Üs alma
7-Tam sayı
8-Çıkış
****Yapacağınız işlemi seçiniz: """))
    if secım ==1:
        sonuc = num1+num2
        print(f"Sonuç: {sonuc}")
    elif secım ==2:
        sonuc = num1-num2
        print(f"Sonuç: {sonuc}")
    elif secım ==3:
        sonuc= num1*num2
        print(sonuc)
    elif secım == 4:
        sonuc=num1/num2
        print(f"Sonuç: {sonuc}")
    elif secım == 5:
        sonuc = num1%num2
        print(f"Sonuç: {sonuc}")
    elif secım==6:
        sonuc = num1**num2
        print(f"Sonuç: {sonuc}")
    elif secım==7:
        sonuc = num1//num2
        print(f"Sonuç: {sonuc}")
    elif secım == 8:
        print("Lütfen Bekleyin...")
        break
