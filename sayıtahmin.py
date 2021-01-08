#Sayı Tahmin
import random as rnd
for i in range(0,3):
    while True:
        num = int(input("Please enter the integer number: "))
        sn = rnd.randint(0,10)
        if num<sn:
            print("Büyük bir sayı giriniz")
        elif num>sn:
            print("Küçük bir sayı giriniz")
        elif num==sn:
            print("Buldunuzzzz")
            break
        else:
            print("Geçersiz bir sayı girdiniz")

    
