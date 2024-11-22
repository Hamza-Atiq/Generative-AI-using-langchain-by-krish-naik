# square function

def square(x):
    
    return x*x

numbers : list[int] = [1 , 2 , 3 , 4 , 5 , 6 , 9]
print(list(map(square , numbers )))

###########

# Lambda function with map

numbers1 : list[int] = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8]
print(list(map(lambda x : x * x , numbers1)))

#####################

# Map multiple iterables

numbers2 : list[int] = [1 , 2 , 3]
numbers3 : list[int] = [4 , 5 , 6]

added_numbers = list(map(lambda x , y : x + y , numbers2 , numbers3))
print(added_numbers)

##################

# Map to convert a list of strings to integers

str_numbers : list[str] = ['1' , '2' , '3' , '4' , '5']
int_numbers = list(map(int , str_numbers))

print(int_numbers)  
print(type(int_numbers))

##################

words : list[str] = ['apple' , 'banana' , 'mango' , 'guava' , 'cherry' ]

upper_case = list(map(str.upper , words ))

print(upper_case)

####################

def get_name(person):
    
    return person['name']

people=[
    {'name':'arslan','age':32},
    {'name':'dawood','age':33}
]
print(list(map(get_name,people)))

