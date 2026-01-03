num1 = 3
num2 = 3.0 
print(type(num1))
print(type(num2))


text = "Welcome"
print(text[2:5])
print(text[:2])
print(text[2:])


a = '2'
b = '3'
print(a, type(a))
print(b, type(b))
print('Addition = ', a+b)   

print()                     

a = int(a)
b = int(b)
print(a, type(a))       
print(b, type(b))       
print('Addition = ', a+b)

#Try passing some integer as input and check its datatype.
num = input('enter some integer  -  ')   
print(num)
print(type(num))

# Carry addition of two user-inputted numbers
num1 = input('Enter first number:  ')
num2 = input('Enter second number:  ')
print(num1 + num2)    
print(int(num1) + int(num2)) 


# multiple if else => use elif
 
height = 176
if height < 140:
    print('too short')
elif height < 180:
    print('height is ok')
else:
    print('too tall')



# You can pass boolean value (True or False) to the condition in if. In that case, you don't need any logical operator like == or !=


is_subscribed = False
if is_subscribed:             
    print('You  subscribed!')  
else:
    print('Please subscribe')