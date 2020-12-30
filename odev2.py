#Odev2.py
print("!Etkinlik Önerme!")
ad=input("Adınızı Giriniz: ")
soyad=input("Soyadınızı Giriniz: ")
while True:
    print(f"******Hoş Geldin,",ad,soyad,"******")
    derece=int(float(input("Havanın derecesini giriniz: ")))
    if -10<=derece<0:
        print("-Kayak zamanı!!-")
        break
    elif 0<=derece<=10:
        print("-Evde film izlemek süper bir fikir!-")
        break
    elif 10<derece<=20:
        print("-Arkadaşların ile dışarda buluşabilirsiniz!-")
        break
    elif 20<derece<=30:
        print("-Havuza ya da denize girmek için harika bir gün!-")
        break
    elif 30<derece<=40:
        print("-Dışarıya çıkmak tehlikeli olabilir şapka ve suyunu unutma!-")
        break
    else:
        print("-Bu iklim koşuluna uygun bir sıcaklık değil lütfen tekrar deneyin!!!-")
        
