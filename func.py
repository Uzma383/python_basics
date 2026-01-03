# 1. Simple function (no arguments)
def greet():
    print("Hello, welcome to Python!")

greet()


# 2. Function with one argument
def greet_user(name):
    print("Hello", name)

greet_user("Uzma")
print(type(greet_user))


# 3. Function with multiple arguments
def add(a, b):
    print("Addition:", a + b)

add(10, 20)


# 4. Function that returns a value
def square(num):
    return num * num

result = square(5)
print("Square:", result)


# 5. Function with default argument
def country(name, nation="India"):
    print(name, "is from", nation)

country("Uzma")
country("John", "USA")


# 6. Function with keyword arguments
def student(name, age):
    print("Name:", name, "Age:", age)

student(age=21, name="Uzma")


# 7. Function returning multiple values
def calculate(a, b):
    return a + b, a - b, a * b

result = calculate(10, 5)
print("Sum, Difference, Product:", result)


# 8. Function calling another function
def welcome():
    print("Welcome!")

def start():
    welcome()

start()


def hi(name):    
    message = "Hi "+name  
    return message  

name = input("Enter the name:")    
print(hi(name))