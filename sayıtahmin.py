#Sayı Tahmin
 hak=0
while hak<5:#hakları burda bildir
    num=int(input("Bir sayı giriniz: "))
    sn=rnd.randint(0,100)
    if num==sn:
        print("Bildiniz")
        break
    elif num>sn:
        print("aşağı")
    elif num<sn:
        print("yukarı")
    hak+=1   
print(f"Hakkınız bitti sayınız:{sn}")

    
