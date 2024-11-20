# arithematic operations

a : int = 100
b : int = 15

add_result = a + b            #addiiton
sub_result = a - b            #substraction 
mult_result = a * b           #multiplication
div_result = a / b            #division
floor_div_result = a // b     # floor division
modulus_result = a % b        #modulus operation
exponent_result = a ** b      # Exponentiation

print(add_result)
print(sub_result)
print(mult_result)
print(div_result)
print(floor_div_result)
print(modulus_result)
print(exponent_result)

####################################

# comparison operators

a : int = 19
b : int = 19

print(a == b)

str1 : str = "Hamza"
str2 : str = 'hamza'

print(str1 == str2)

# greater than or equal to

number1 : int = 45
number2 : int = 45

print(number1 >= number2)
print(number1 <= number2)

###################################

# Logical operators

x : bool = True
y : bool = True

print(x and y)

z : bool = True
e : bool = False

print(z and e)

q : bool = False
i : bool = True

print(q or i)

r : bool = False
t : bool = False

print(r or t)

#############################

# Simple calculator

num1 : float = float(input("Enter first number : "))
num2 : float = float(input("Enter second number : "))

# Performing arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
exponentiation = num1 ** num2

# Displaying results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)