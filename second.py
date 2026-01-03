fruits = ['apple','banana','kiwi']
print(fruits)

print(type(fruits))

print(fruits[0])
print(fruits[1])
print(fruits[0:2])

fruits.append('Mango')
print(fruits)

fruits.sort()
print(fruits)

# Similary, sort works on the list with only numbers as well
nums = [12, 4, 2, 11, 1, 100]
print(nums)
nums.sort()
print(nums)

#checking length
countries = ['Russia', 'India', 'US', 'Japan', 'Germany', 'Italy', 'Zambia']
print(len(countries))
# Returns the one with highest alphabet, when list is made of strings
print(max(countries))   
print(min(countries))

# Let's define a simple for loop

for item in countries:            
  print(item)


for item in countries:
      print(f'{item} --- {item.upper()} --- {len(item)}')   