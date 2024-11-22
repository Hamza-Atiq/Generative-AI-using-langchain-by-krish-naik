from typing import Any

def even_number_checker(number):
    
    if number % 2 == 0:
        return True
    
num : list[int] = [1 , 2 , 4 , 5 , 6 , 7 , 9 , 8]
print(list(filter(even_number_checker , num)))

####################

# filter with lambda function

num1 : list[int] = [1 , 2 , 3 , 6 , 13 , 4 , 5 , 6 , 7 , 7 , 78]

print(list(filter(lambda x : x > 5 , num1))) 

###################

# Filter with a lambda function and multiple conditions

num2 : list[int] = [1 , 2 , 3 , 6 , 13 , 4 , 5 , 6 , 7 , 7 , 78]

print(list(filter(lambda x : x > 5 and x % 2 == 0 , num2))) 

#######################

# Filter() to check if the age is greate than 25 in dictionaries
people : list[dict[str : Any]] = [
    
    {'name' : 'Kamran' , 'age' : 32},
    {'name' : 'Junaid' , 'age' : 33},
    {'name' : 'John' , 'age' : 25}
    
]

def age_greater_than_25(person):
    
    return person['age'] > 25

print(list(filter(age_greater_than_25 , people)))