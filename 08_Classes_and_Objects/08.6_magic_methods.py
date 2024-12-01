'''
__init__': Initializes a new instance of a class.
__str__: Returns a string representation of an object.
__repr__: Returns an official string representation of an object.
__len__: Returns the length of an object.
__getitem__: Gets an item from a container.
__setitem__: Sets an item in a container.
'''

#########################

class Person:
    pass

person=Person()
print(dir(person))

#######################

# Basic Methods

class Person:
    
    def __init__(self , name : str , age : int):
        
        self.name = name
        self.age = age
        
person=Person("Kamran" , 34)
print(person)

#######################

class Person:
    
    def __init__(self , name : str , age : int):
        
        self.name=name
        self.age=age
    
    def __str__(self):
        return f"{self.name} , {self.age} years old"
    
    def __repr__(self):
        return f"Person(name = {self.name} , age= {self.age})"
    
person=Person("Manan" , 36)
print(person)
print(repr(person))