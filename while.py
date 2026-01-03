# 1. Simple while loop
i = 1
while i <= 5:
    print(i)
    i = i + 1


# 2. while loop with even numbers
num = 2
while num <= 10:
    print("Even:", num)
    num += 2


# 3. while loop with if condition
count = 1
while count <= 5:
    if count == 3:
        print("Reached 3")
    print(count)
    count += 1


# 4. while loop with break
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1


# 5. while loop with continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)


# 6. while loop with user input
number = int(input("Enter a number: "))

while number != 0:
    print("You entered:", number)
    number = int(input("Enter 0 to stop: "))


# 7. Real-life example: login attempts
attempts = 0

while attempts < 3:
    password = input("Enter password: ")
    if password == "admin":
        print("Login successful")
        break
    else:
        print("Wrong password")
    attempts += 1
