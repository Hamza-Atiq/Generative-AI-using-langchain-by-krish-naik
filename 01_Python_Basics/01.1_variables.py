# Declaring and assigning variables

age : int = 32
height : float = 6.1
name : str = 'Hamza'
is_student : bool = True

print(age)
print(height)
print(name)
print(is_student)

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

###################################

# Dynamic Typing

var : int = 10 

print(var , type(var))

var : str = "Hello"
print(var , type(var))

var : float = 3.14

print(var , type(var))

#######################################

# input 

age : int = int(input("What is the Your age : "))

#########################################

### Simple calculator

num1 : int = float(input("Enter first number : "))
num2 : float = float(input("Enter second number : "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
