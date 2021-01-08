#Egzersiz
#Girilen sayı asal sayı mı değil midir?
num = int(input("Enter the integer number: "))
for i in range(2,num+1):
    if num%i==0:
        print("Asal Sayı değildir")
        break
    else:
        print("Asal sayıdr")
        break
i = 2
while i<=num:
    if num%i==0:
        print("Asal Sayı değildir")
        break
    else:
        print("Asal sayıdır")
        break
