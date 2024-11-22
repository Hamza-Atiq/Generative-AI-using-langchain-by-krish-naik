from typing import Any

import array

arr = array.array('i' , [1 , 2 , 3 , 4])
print(arr)

################

# random 

import random

print(random.randint(1,10))
print(random.choice(['apple' , 'banana' , 'cherry']))

###########

# File And Directory Access

import os

print(os.getcwd())

# os.mkdir('test_dir')

####################

# High level operations on files and collection of files

import shutil

shutil.copyfile(r'05_Modules_and_Packages\source.txt',r'05_Modules_and_Packages\destination.txt')

####################

# Data Serialization

import json

data : dict[str : Any] = {'name' : 'Khurram' , 'age' : 25}

json_str = json.dumps(data)

print(json_str)
print(type(json_str))

parsed_data=json.loads(json_str)

print(parsed_data)
print(type(parsed_data))

#############

# csv file

import csv

with open(r'05_Modules_and_Packages\example.csv' , mode = 'w' , newline= "") as file:
    
    writer = csv.writer(file)
    writer.writerow(['name' , 'age' , 'education' , 'location'])
    writer.writerow(['Hamza' , 28 , 'AI' , 'RWP'])
    writer.writerow(['Atiq' , 48 , 'Electrical diploma' , 'RYD'])
    writer.writerow(['Saif' , 18 , 'Fsc' , 'LHR'])
    writer.writerow(['Amin' , 38 , 'AI' , 'KHI'])
    
with open(r'05_Modules_and_Packages\example.csv' , mode = 'r') as file1:
    
    reader = csv.reader(file1)
    
    for row in reader:
        
        print(row)
    

    
    