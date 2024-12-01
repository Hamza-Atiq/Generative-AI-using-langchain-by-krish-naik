# Person class with public variables

class Person:
    
    def __init__(self , name : str , age : int):
        
        self.name = name
        self.age = age
        
def get_name(person):
    return person.name , person.age

person1 = Person('Hamza' , 27)
print(get_name(person1))

print(dir(person1))

##############################

# Person class with private variables

class Person:
    
    def __init__(self , name : str , age : int , gender : 'str'):
        
        self.__name = name
        self.__age = age
        self.gender = gender
        
def get_name(person):
    return person.name , person.age , person.gender

person2 = Person('Amna' , 27 , 'Female')
print(get_name(person2))

print(dir(person2))

# it gives error because we cannot access the private variables out of the class

########################

# Person class with protected variables

class Person:
    
    def __init__(self , name : str , age : int , gender : str):
        
        self._name = name
        self._age = age
        self.gender = gender 
        
class Employee(Person):
    
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

person3 = Employee('Hamza' , 27 , 'Male')
print(person3._name)
print(person3._age)
print(person3.gender)

print(dir(person3))

##########################

# Encapsulation with getter and setter

class Person:
    
    def __init__(self , name : str , age : int ):
        
        self.__name = name
        self.__age = age
        
    # Getter method for name
    def get_name(self):
        return self.__name
    
    # Getter method for age
    def get_age(self):
        return self.__age
    
    # Setter method for name
    def set_name(self , name):
        self.__name = name
        
    # Setter method for age
    def set_age(self , age):
        if age > 0:
            self.__age = age
        else:
            print('Age cannot be negative')
            
person = Person('Abdullah' , 2)
               
## Access and modify private variables using getter and setter

print(person.get_name())
print(person.get_age())

person.set_name('Muraij')
print(person.get_name())

person.set_age(35)
print(person.get_age())

person.set_age(-5)        