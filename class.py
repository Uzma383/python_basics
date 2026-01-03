# 1. Simple class and object
class Student:
    pass

s1 = Student()
print(s1)


# 2. Class with variables (attributes)
class Student:
    name = "Uzma"
    age = 21

s1 = Student()
print(s1.name)
print(s1.age)


# 3. Class with function (method)
class Student:
    def display(self):
        print("This is a student")

s1 = Student()
s1.display()


# 4. Class with constructor (__init__)
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Uzma", 21)
s2 = Student("Ali", 22)

s1.show()
s2.show()


# 5. Real-life example: Car
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(self.brand, self.model, "is starting")

c1 = Car("Toyota", "Innova")
c2 = Car("Honda", "City")

c1.start()
c2.start()


# 6. Modify object properties
c1.model = "Fortuner"
print(c1.model)





# 1. Instance variables
class Student:
    def __init__(self, name, age):
        self.name = name    # instance variable
        self.age = age      # instance variable

s1 = Student("Uzma", 21)
s2 = Student("Ali", 22)

print(s1.name, s1.age)   # Uzma 21
print(s2.name, s2.age)   # Ali 22


# 2. Class variable (shared by all objects)
class Student:
    school = "CTOschool"  # class variable

    def __init__(self, name):
        self.name = name    # instance variable

s1 = Student("Uzma")
s2 = Student("Ali")

print(s1.name, s1.school)  # Uzma CTOschool
print(s2.name, s2.school)  # Ali CTOschool

# Change class variable
Student.school = "NewSchool"
print(s1.school)  # NewSchool
print(s2.school)  # NewSchool


# 3. Private variable
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   # private variable

    def show_salary(self):
        print("Salary of", self.name, "is", self.__salary)

e1 = Employee("Uzma", 50000)
e1.show_salary()




# 4. Adding multiple instance variables
class Car:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    def display(self):
        print(self.brand, self.model, self.color, self.year)

c1 = Car("Toyota", "Innova", "White", 2020)
c2 = Car("Honda", "City", "Black", 2021)

c1.display()
c2.display()


# 5. Modify instance variables
c1.color = "Red"
c1.year = 2022
c1.display()  # Toyota Innova Red 2022


# 6. Multiple methods (functions) in class
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited", amount, "New balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn", amount, "New balance:", self.balance)
        else:
            print("Insufficient balance")

a1 = BankAccount("Uzma", 1000)
a1.deposit(500)
a1.withdraw(300)
a1.withdraw(1500)



# The above code is correct, but we'd like to pass name and age when we create object. 
# So this is how we'll modify the code

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def details(self):
        print("Employee Name: ",  self.name)
        print("Employee Age: ", self.age)
 

emp1 = Employee("John", 26)         
emp2 = Employee("Jane", 24)         

emp1.details()
emp2.details()


# Class definition
class Student:
    name = "Uzma"
    age = 21

# Creating an object
s1 = Student()

# Accessing object properties
print(s1.name)  # Uzma
print(s1.age)   # 21
