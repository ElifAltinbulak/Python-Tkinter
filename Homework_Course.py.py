#Homework2
print("*******************************")
for i in range(0,3):
    name=input("Name: ")
    surname=input("Surname: ")
    if name==("Elif".strip()) and (surname=="Altınbulak".strip()):
        print(f"****Welcome,{name} {surname}****")
        while True:
            chose=int(input("Firstly,How many lessons you have(min=3),(max=5) : "))
            if chose==3:
                exam1 = int(input("Midterm :"))
                exam2 = int(input("Final :"))
                exam3 = int(input("Project :"))
                avarge=(exam1*0.3)+(exam2*0.5)+(exam3*0.2)
                grade = {"Midterm":(exam1),"Final":(exam2),"Project":(exam3)}
                if 90<=avarge<=100:
                    print("AA")
                elif 70<=avarge<=90:
                    print("BB")
                elif 50<=avarge<=70:
                    print("CC")
                elif 30<=avarge<=50:
                    print("DD")
                elif 0<=avarge<=30:
                    print("FF")
                else:
                    print("You entered an invalid grade")
                print(grade)
                break
            elif chose==4:
                exam4 = int(input("Midterm1 :"))
                exam5 = int(input("Midterm2 :"))
                exam6 = int(input("Final :"))
                exam7 = int(input("Project :"))
                avarge1=((exam4*0.15)+(exam5*0.15)/2)+(exam6*0.5)+(exam7*0.2)
                grade1={"Midterm1":(exam4),"Midterm2":(exam5),"Final":(exam6),"Project":(exam7)}
                if 90<=avarge1<=100:
                    print("AA")
                elif 70<=avarge1<=90:
                    print("BB")
                elif 50<=avarge1<=70:
                    print("CC")
                elif 30<=avarge1<=50:
                    print("DD")
                elif 0<=avarge1<=30:
                    print("FF")
                else:
                    print("You entered an invalid grade")
                print(grade1)
                break
            elif chose==5:
                exam8 = int(input("Midterm1 :"))
                exam9 = int(input("Midterm2 :"))
                exam10 = int(input("Midterm3 :"))
                exam11 = int(input("Final :"))
                exam12 = int(input("Project :"))
                avarge2=((exam8*0.1)+(exam9*0.1)+(exam10*0.1)/3)+(exam11*0.5)+(exam12*0.2)
                grade2={"Midterm1":(exam8),"Midterm2":(exam9),"Midterm3":(exam10),"Final":(exam11),"Project":(exam12)}
                if 90<=avarge2<=100:
                    print("AA")
                elif 70<=avarge2<=90:
                    print("BB")
                elif 50<=avarge2<=70:
                    print("CC")
                elif 30<=avarge2<=50:
                    print("DD")
                elif 0<=avarge2<=30:
                    print("FF , you failed in class ")
                else:
                    print("You entered an invalid grade")
                print(grade2)
                break
            else:
                print("Please enter 3 or 5 lessons")
        break    
    elif i==2:
        print("Please Try Agin Later..")



    

