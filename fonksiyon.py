#Homework_2
import math 
def dortgen_alan_hesapla_v1(kısakenar,uzunkenar):
    dalan = kısakenar*uzunkenar
    return dalan
def daire_alan_hesapla_v1(r):
    calan = (math.pi)*r**2
    return calan
print("-"*37)
kısakenar=int(input("Dikdörtgenin kısa kenarını giriniz: "))
uzunkenar=int(input("Dikdörtgenin uzun kenarını giriniz: "))
x = dortgen_alan_hesapla_v1(kısakenar,uzunkenar)
print(f"Dikdörtgenin Alanı: {x}")
print("-"*37)
r = int(input("Dairenin yarıçapını giriniz: "))
y = daire_alan_hesapla_v1(r)
print(f"Dairenin Alanı: {y}")
def dortgen_alan_hesapla_v2(kısakenar,uzunkenar):
    dalan2 = (kısakenar**2)*(uzunkenar**2)
    return dalan2
z = dortgen_alan_hesapla_v2(kısakenar,uzunkenar)
print("-"*37)
print(f"Dikdörtgenin 2.Alan Hesabı: {z}")
def daire_alan_hesapla_v2(r):
    calan2 = (math.pi)*(r**2)**2
    return calan2
d = daire_alan_hesapla_v2(r)
print(f"Dairenin 2.Alan Hesabı: {d}")
