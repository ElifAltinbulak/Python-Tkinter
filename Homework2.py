#Homework2
first_name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))
birth = int(input("Date of birth(just year): "))
person = [first_name,last_name,age,birth]
for i in person:
    print(i)
if age>=18:
    print("You can go out to the street")
elif 0<=age<18:
    print("You can't go out because it's too dangerous")
else:
    print("You entered an invalid age")
