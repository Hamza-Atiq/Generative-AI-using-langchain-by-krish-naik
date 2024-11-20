# if else statement

age : int = 16

if age >= 18:
    
    print("You are eligible for voting")
    
else:
    
    print("You are a minor")
    
###################################

# if elif else

age : int = 17

if age < 13 :
    
    print('You are a child')
    
elif age < 18 :
    
    print('You are teenager')
    
else:
    
    print('You are adult')
    
########################################

# nested conditioal statements

num : int = int(input('Enter the Number : '))

if num > 0:
    
    if num % 2 == 0:
        
        print(f'{num} is even')
        
    else:
        
        print(f'{num} is odd')
        
else:
    
    print('Number is negative or zero')
    
##########################################

# Example 1

# Leap Year

year : int = int(input('Enter the Year : '))

if year % 4 == 0:
    
    if year % 100 == 0:
        
        if year % 400 == 0:
            
            print(f'{year} is a leap year')
            
        else:
            
            print(f'{year} is not a leap year')
            
    else:
        
        print(f'{year} is a leap year')
        
else:
    
    print(f'{year} is not a leap year') 
    
######################################

# Example 2

# Simple Calculator

num_1 : float = float(input("Enter the first number : "))
num_2 : float = float(input("Enter the second number : ")) 
operator : str = input("Enter the opertaion which you want to perform (+ , - , * , / , // , ** , %) : ")

if operator == '+':
    
    print(f"sum = {num_1 + num_2}")
    
elif operator == '-':
    
    print(f'subrtraction = {num_1 - num_2}')
    
elif operator == '*':
    
    print(f'Multiplication = {num_1 * num_2}')
    
elif operator == '/':
    
    if num_2 == 0:
        
        print('num_2 is zero so its is not divisible ')
        
    else:
    
        print(f'divison = {num_1 / num_2}')
    
elif operator == '//':
    
    print(f'floor division = {num_1 // num_2}')
    
elif operator == '%':
    
    print(f'reminder = {num_1 % num_2}')
    
elif operator == '**':
    
    print(f'power = {num_1 ** num_2}')
    
else:
    
    print('incorrect operator')
    
##############################################

# Example 3

# Ticket price based on age and wheather the person is student

age : int = int(input('Enter your age : '))
is_student : str = input('Are you student (Yes / no) : ').lower()

if age < 5 :
    
    price = 'Free'

elif age <= 12 :
    
    price = '$10'
    
elif age <= 18:
    
    if is_student == 'yes':
        
        price = '$12'
        
    else:
        
        price = '$15'
        
elif age <= 64 :
    
    if is_student == 'yes':
        
        price = '$20'
        
    else:
        
        price = '$25'
        
else:
    
    price = '$5'
    
print(f'Ticket price : {price}')

###########################################

# Example 4 

# Employee Bonus calculation

years_of_service : int = int(input('Enter year of expirence : '))
performance_rating : float = float(input('Enter performance rating (1.0 - 5.0) : '))

if performance_rating >= 4.5:
    
    if years_of_service > 10:
        
        bonus_percentage = 20
        
    elif years_of_service > 5:
        
        bonus_percentage = 15
        
    else:
        
        bonus_percentage = 10
        
elif performance_rating >= 3.5:
    
    if years_of_service > 10 :
        
        bonus_percentage = 12
        
    elif years_of_service > 5 :
        
        bonus_percentage = 8
        
    else:
        
        bonus_percentage = 4
        
else:
    
    bonus_percentage = 0
    
salary : float = float(input('Enter current salary : '))
bonus_amount : float = salary * bonus_percentage / 100

print(f'Bonus amount : ${bonus_amount:.2f}') 

############################################

# Example 5

# user login system

# Predefined username and password

stored_username : str = "admin"
stored_password : str = "password123"

# Take user input
username : str = input("Enter username : ")
password : str = input("Enter password : ")

# Check login credentials
if username == stored_username:
    
    if password == stored_password:
        
        print("Login successful ! ")
        
    else:
        
        print("Incorrect password.")
        
else:
    
    print("Username not found.")
      