# IF STATEMENT
# Used to evaluate a condition

# 1. Simple IF
age = 20

if age >= 18:
    print("You are eligible to vote")


# 2. IF with false condition
num = 5

if num > 10:
    print("Number is greater than 10")


# 3. IF – ELSE
marks = 35

if marks >= 40:
    print("Pass")
else:
    print("Fail")


# 4. IF – ELIF – ELSE
score = 85

if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 60:
    print("Grade C")
else:
    print("Grade D")


# 5. IF with logical operators
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")


# 6. IF with OR operator
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")


# 7. Nested IF
num = 10

if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Negative number")


# 8. IF with comparison operators
a = 10
b = 20

if a < b:
    print("a is less than b")


# 9. IF with membership operator
fruits = ["apple", "banana", "mango"]

if "apple" in fruits:
    print("Apple is available")


# 10. IF with user input (try changing input)
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")



###  NESTED IF ELSE ###

num = 8

if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Negative Number or Zero")
