# Base class

class Animal:
    
    def speak(self):
        return 'sound of the animal'
    
# Derived class 1

class Dog(Animal):
    
    def speak(self):
        return 'woof !'
    
class Cat(Animal):
    
    def speak(self):
        return 'Meow !'
    
# function that demonstrate polmorphisim
def animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())
animal_speak(dog)
animal_speak(cat)

########################

# Polymorphism with functions and methods

# base class

class Shape:
    
    def area(self):
        return 'The are of the figure'
    
# Derived class 1
    
class Rectange(Shape):
    
    def __init__(self , weidth , height):
        self.weidth = weidth
        self.height = height
        self.name = 'Rectangle'
        
    def area(self):
        return self.weidth * self.height
    
# Derived class 2
    
class Circle(Shape):
    
    def __init__(self , radius):
        self.radius = radius
        self.name = 'Circle'
        
    def area(self):
        return 3.14 * self.radius ** 2
    
# Function that demonstrate polmorphism

def print_area(shape):
    
    print(f'The area of the {shape.name} is {shape.area()}')
    
rec = Rectange(4 , 6)
circle = Circle(5)

print_area(rec)
print_area(circle)
    
#########################
        
# Polmorphism with abstract base classes

from abc import ABC , abstractmethod

# Define an abstract class

class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass
    
# Derived class 1

class Car(Vehicle):
    
    def start_engine(self):
        return 'Car Engine started'

# Derived class 2

class Motorcycle(Vehicle):
    
    def start_engine(self):
        return 'Motorcycle engine started'
    
# function that demonstrates polymorphism

def start_vehicle(vehicle):
    
    print(vehicle.start_engine())
    
car = Car()
motorcycle = Motorcycle()

start_vehicle(car)
start_vehicle(motorcycle)

