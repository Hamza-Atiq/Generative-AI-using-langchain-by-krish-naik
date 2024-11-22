from typing import Any

# syntax

def function_name(parameters):
    """Docstring"""
    # Function body
    expression = 0 * parameters
    return expression

function_name(0)

############################

def even_or_odd(num : int):
    
    """This function finds even or odd"""
    
    if num % 2 == 0:
        
        print("the number is even")
        
    else:
        
        print("the number is odd")
        
# Call this function
even_or_odd(24)
even_or_odd(23)

# function with multiple parameters

def add(a : int , b : int) -> int:
    
    return a + b

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

result = add(a, b)

print(f"The result is: {result}")

##################################

# Default parameters

def greet(name : str = "Guest"):
    
    print(f"Hello {name} Welcome To the paradise")

greet("Muraij")
greet()

#####################################

# Positional arguments

def print_numbers(*args : Any) -> Any:
    
    for number in args:
        
        print(number)
        
print_numbers(1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , "Fasiah")

############################

# Keywords Arguments

def print_details(**kwargs : dict[str : Any]) -> dict:
    
    for key , value in kwargs.items():
        
        print(f"{key} : {value}")
        
print_details(name = "Kashan" , age = "30" , country = "Pakistan")

# combine positional arguments and keyword arguments

def print_details(*args : Any , **kwargs : dict[str : Any]):
    
    for val in args:
        
        print(f"Positional arument : {val}")
    
    for key , value in kwargs.items():
        
        print(f"{key} : {value}")
        
print_details(1 , 2 , 3 , 4 , "kifayat" , name = "jhanzaib" , age = 32 , country = "pak")

##################################

# Example 1

# Temperature Conversion

def temperature_conversion(temp : float , unit : str):
    
    """This function converts temperature between Celsius and Fahrenheit"""
    
    if unit.lower() == 'c':
        return temp * 9/5 + 32  # Celsius To Fahrenheit
    
    elif unit.lower() == 'f':
        return (temp-32) * 5/9 # Fahrenheit to celsius
    
    else:
        print('Invalid character')
        
print(temperature_conversion(25 , 'c'))
print(temperature_conversion(77 , 'f'))
temperature_conversion(67 , 'i')

###################################

# Example 2

# Password checker

def password_checker(password : str):
    
    """This function checks if the password is strong or not"""
    
    errors = []
    
    # Check password length
    
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    
    # Check for a digit
    
    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one digit.")
    
    # Check for a lowercase letter
    
    if not any(char.islower() for char in password):
        errors.append("Password must contain at least one lowercase letter.")
    
    # Check for an uppercase letter
    
    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter.")
    
    # Check for a special character
    
    if not any(char in '!@#$%^<>&*()_+' for char in password):
        errors.append("Password must contain at least one special character (!@#$%^<>&*()_+).")
    
    # Print result
    
    if errors:
        print("Weak password ! Issues:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Strong password !")
        
# Calling the function
password_checker("WeakPwd")
password_checker("Str0ngPwd")
password_checker("Str0ngPwd@")

###############################

# Example 3

# Total cost of items in a shopping cart

def total_cost(cart : dict[str : Any]):
    
    """ Calculate the Total Cost Of Items In a Shopping Cart"""
    
    total_cost : int = 0
    
    for item in cart:
        
        total_cost += item['price'] * item['quantity']
        
    return total_cost

# Example cart data

cart=[
    {'name':'Apple','price':0.5,'quantity':4},
    {'name':'Banana','price':0.3,'quantity':6},
    {'name':'Orange','price':0.7,'quantity':3},
    {'name':'pineapple','price':0.9,'quantity':6},
    {'name':'mango','price':0.7,'quantity':10}

]

# calling the function
total_cost = total_cost(cart)
print(f"total_cost : {total_cost}" )

###############################

# Example 4

# string a palindrome

def is_palindrome(string : str):
    
    """Check IF a String Is Palindrome"""
    
    string = string.lower().replace(" " , "")
    
    return string == string[::-1]

print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Hello"))

######################################

# Example 5

# caculate factorial

def factorial(num : int):
    
    """Calculate the factorials of a number using recursion"""
    
    if num == 0:
        
        return 1
    
    else:
        
        return num * factorial(num -1)
    
print(factorial(6))

##############################################

# Example 6

# count frequency of words in file

def count_word_frequency(file_path):
    
    """A Function To Read A File and count the frequency of each word"""
    
    word_count = {}
    
    with open(file_path , 'r') as file:
        
        for line in file:
            
            words = line.split()
            
            for word in words:
                
                word = word.lower().strip('.,_!?;:"\'')
                word_count[word] = word_count.get(word , 0) + 1
                
    return word_count , len(word_count)

file_path = r"04_Functions\README.roboflow.txt"
word_frequency = count_word_frequency(file_path)
print(word_frequency)

##################################

# Example 7

# Validate email address

import re

def is_valid_email(email):
    """Checks if an email is valid."""
    if not isinstance(email, str) or not email.strip():
        return False
    
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Test cases
print(is_valid_email("Test@Example.com"))    
print(is_valid_email("user@domain.org"))     
print(is_valid_email("invalid-email"))       
print(is_valid_email(""))                    
print(is_valid_email(None))                  
