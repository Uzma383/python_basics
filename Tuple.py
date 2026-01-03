fruits = ('apple','banana','kiwi')
print(fruits)

print(type(fruits))

print(fruits[0])

print(fruits.index('banana'))

# Let's define courses, and allow duplicate
courses = ('ba', 'bcom', 'bsc', 'bsc', 'ba')
print(courses)
print(courses.count('bsc'))            
print(courses.index('bsc')) 

for item in courses:     
  print(item)

print(len(courses))

# check whether an element is in the tuple
fruits = ('apple','mango')

print('mango' in fruits)     
print('mangoes' in fruits)

#  Algebraic operations like max, min etc
print(max(2, 1, 3, 7))
print(min(2, 1, 3, 7))

# To convert list into a tuple
num = [1, 2, 3, 4]
new = tuple(num)

print(num)
print(new)

# Just like list, you can use -1 to get the last element, and -2 to get second last element
num = (1, 2, 3, 4, 5, 6, 7)
print(num[-1])
print(num[-2])