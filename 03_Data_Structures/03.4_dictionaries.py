from typing import Any

# Creating Dictionaries

empty_dict : dict = {}

print(type(empty_dict))

student : dict[str : Any] = {"name" : "hamza" , "age" : 32 , "grade" : 'A'}

print(student)
print(type(student))

# Accessing Dictionary elements

print(student['grade'])
print(student['age'])

# Accessing using get() method

print(student.get('grade'))
print(student.get('last_name'))
print(student.get('last_name',"Not Available"))


student["age"] = 28  # update value for the key

print(student)

student["address"] = "Pakistan" # added a new key and value

print(student)

del student['grade'] # delete key and value pair

print(student)

# Dictionary methods

keys = student.keys() # get all the keys

print(keys)

values = student.values() # get all values

print(values)

items = student.items() # get all key value pairs

print(items)

student_copy1 = student.copy() # shallow copy

print(student_copy1)
print(student)

student["name"] = "Atiq"

print(student_copy1)
print(student)

# Iterating Over Dictionaries

# Iterating over keys

for keys in student.keys():
    
    print(keys)
    
# Iterate over values

for value in student.values():
    
    print(value)
    
# Iterate over key value pairs

for key , value in student.items():
    
    print(f"{key} : {value}")
    
# Nested Disctionaries

students : dict[dict[str : Any]] = {
    
    "student1" : {"name" : "Ali" , "age" : 30 },
    "student2" : {"name" : "Abdullah" , "age" : 35}
    
}

print(students)

# Access nested dictionaries elements

print(students["student2"]["name"])
print(students["student2"]["age"])


# Iterating over nested dictionaries

for student_id , student_info in students.items():
    
    print(f"{student_id} : {student_info}")
    
    for key , value in student_info.items():
        
        print(f"{key} : {value}")
        
# Dictionary Comphrehension

squares = {x : x**2 for x in range(5)}

print(squares)

# USe a dictionary to count he frequency of elements in list

numbers : list[int] =[1 , 2 , 2 , 3 , 3 , 3 , 4 , 4 , 4 , 4]
frequency : dict ={}

for number in numbers:
    
    if number in frequency:
        
        frequency[number]+=1
        
    else:
        
        frequency[number]=1
        
print(frequency)

# Merge 2 dictionaries into one

dict1 : dict[str : int] = {"a" : 1 , "b" : 2}
dict2 : dict[str : int] = {"b" : 3 , "c" : 4}

merged_dict = {**dict1 , **dict2}

print(merged_dict)
