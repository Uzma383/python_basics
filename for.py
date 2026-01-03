# 1. Simple for loop
for i in range(5):
    print(i)


# 2. for loop with custom range
for i in range(1, 6):
    print("Number:", i)


# 3. for loop through a list
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# 4. for loop through a string
for ch in "Python":
    print(ch)


# 5. for loop with if condition
for num in range(1, 11):
    if num % 2 == 0:
        print("Even:", num)


# 6. for loop with break
for i in range(1, 10):
    if i == 5:
        break
    print(i)


# 7. break with list search
numbers = [10, 20, 30, 40, 50]

for n in numbers:
    if n == 30:
        print("Found 30")
        break
    print("Checking:", n)


# 8. Nested for loop with break
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print("i =", i, "j =", j)


# 9. Real-life example: password check
passwords = ["abc", "123", "pass", "admin"]

for pwd in passwords:
    if pwd == "admin":
        print("Correct password found")
        break
    print("Trying:", pwd)
