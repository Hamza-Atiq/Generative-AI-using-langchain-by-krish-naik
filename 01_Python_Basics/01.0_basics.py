# Basic syntax rules in python
name : str = 'hamza'
Name : str = 'Atiq'

print(name)
print(Name)

#######################################

# Indentation

age : int = 28

if age >= 30:

    print(age)

print(age)

# Code exmaples of indentation

if True:

    print("Correct Indentation")

    if False:
        
        print("This one print")

    print("This will print")

print("Outside the if block")

################################

# Line continuation

total : int = 1 + 2 + 4 + 6 + 7 + 9 \
+ 3 + 5 + 8

print(total)

#################################

# Multiple statements on the single line

x : int = 5 ; y : int = 20 ; z = x + y

print(z)

###################################

# Type Inference

variable : int = 10

print(type(variable))

str_variable : str = "hamza"

print(type(str_variable))
