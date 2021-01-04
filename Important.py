#İmportant
print(1,2,3,4,sep="-",end="--")
print(1,2,3,4,5,end="..")
#if we should use sep and end together. it will one after another everytime.
#Dict
Mary={
    "name":"Mary",
    "surname":"Kamoncik",
    "age":20,
    "job":"Civil Engineering"}
a=Mary["name"]#This is very important!
print(a)
b=Mary["surname"]
print(b)
print("**Holla**")
print(f"""Name:{Mary['name']}
Surname:{Mary['surname']}
Age:{Mary['age']}
Job:{Mary['job']}""")
