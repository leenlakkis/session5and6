#Class Slides:
a=6
print(a+2.0)
a/=2
print(a)
b = a
print(b+2)
c= a>b
print(c and a)
print(a+b+c)

name = input("What is your name?")
age = input("How old are you?")
age= int(age)
birth_year = 2023 - age

print(f"OMG {name}, you are {age} years old so you were born in {birth_year}!")
print("OMG", name + ", you are", age, "years old so you were born in", birth_year)

age = int(input("What is your age?"))
age= input("How old are you?")
age= int(age)

print(f"Your name is {age}")
