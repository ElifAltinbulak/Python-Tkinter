#ATM
while True :
    kullanıcı_adı=input("Kullanıcı Adınızı Giriniz : ")
    pw = input("Şifrenizi Giriniz : ")
    if kullanıcı_adı=="Elif" and pw=="ab123":
        hesap = 10000
        while True :
            print("""Yapmak istediğiniz işlemleri giriniz :
                  1-Para Çekmek
                  2-Para Yatırmak
                  3-Havale Yaptırmak
                  4-Çıkış""")
            secım = int(input("İşleminizi Seçiniz : "))
            if secım == 1:
                x = int(input("Çekeceğiniz fiyat : "))
                hesap-=x
                print(f"Kalan Tutar : {hesap}")
            elif secım == 2:
                y = int(input("Yatırmak istediğiniz fiyat : "))
                hesap+=y
                print(f"Kalan Tutar : {hesap}")
            elif secım == 3:
                z = int(input("Havale edeceğiniz tutar : "))
                name = input("Havale edeceğiniz kişi adı : ")
                hesap-=z
                print(f"Hesaptaki ücret : {hesap} Havale ücreti : {z} Havale edilen kişi : {name}")
            elif secım == 4:
                print("İşlem yapılıyor...")
                print("Bizi Tercih Ettiğiniz İçin Teşekkürler:)")
                break
            else :
                print("Yanlış Seçim. Tekrar Deneyiniz")
    else :
        print("Yanlış Girdiniz Tekrar Deneyiniz")
