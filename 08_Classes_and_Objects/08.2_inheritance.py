# Single inheritance

# PARENT CLASS

class Car:
    
    def __init__(self , windows , doors , enginetype , name , model):
        
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype
        self.name = name
        self.model = model
        
    def drive(self):
        
        print(f'The person wil drive the {self.name} car')
        
    def car_data(self):
        
        print(f'The car name : {self.name} , car model : {self.model} , car engine type : {self.enginetype}')
        
car1 = Car(6 , 4 , 'petrol' , 'bmw' , 2012 ) 
car1.drive()
car1.car_data()

class Tesla(Car):
    
    def __init__(self, windows, doors, enginetype, name, model , is_selfdriving):
        super().__init__(windows, doors, enginetype, name, model)
        
        self.is_selfdriving = is_selfdriving
        
    def selfdriving(self):
        
        print(f'Tesla supports self driving : {self.is_selfdriving}')
        
tesla1 = Tesla(6 , 4 , 'electric' , 'telsa' , 2024 , True)
tesla1.selfdriving()
tesla1.car_data()
tesla1.drive()

# Multiple Inheritance

# base class 1

class Animal:
    
    def __init__(self , name):
        
        self.name = name
        
    def speak(self):
        
        print('subclass must implement this method')
        
# base class 2

class Pet:
    
    def __init__(self , owner):
        
        self.owner = owner
        
# derived class

class Cat(Animal , Pet):
    
    def __init__(self , name , owner):
        Animal.__init__(self, name)
        Pet.__init__(self , owner)
        
    def speak(self):
        
        return f'{self.name} say meoo'
        
# Create an object

cat1 = Cat('cato' , 'Ali')
print(cat1.speak())
