#for elementary school student learn multiplication
import random as rnd
num1=rnd.randint(0,10)
num2=rnd.randint(0,10)
result=int(input(f"How much is {num1} times {num2}:"))
if num1*num2==result:
    print("Very good!")
else:
    print("No,please try again")
