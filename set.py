my_set = {1, 2, 3, 4}
print(my_set)

numbers = {1, 2, 2, 3, 3, 4}
print(numbers)

mixed_set = {1, "Python", 3.5, True}
print(mixed_set)

empty_set = set()
print(type(empty_set))

fruits = {"apple", "banana"}
fruits.add("orange")
print(fruits)

fruits.update(["mango", "grapes"])
print(fruits)

fruits.remove("banana")
print(fruits)

for item in fruits:
    print(item)

A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)

print(A & B)

print(A - B)

print("apple" in fruits)