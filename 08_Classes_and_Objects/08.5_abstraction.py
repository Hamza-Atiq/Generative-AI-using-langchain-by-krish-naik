from abc import ABC , abstractmethod

# Abstract base class

class Vehicle(ABC):
    
    def drive(self):
        print('This vehicle is comportable for driving')
        
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def tyre(self):
        pass
    
class Car(Vehicle):
    
    def tyre(self):
        print('Car has 4 wheals') 
        
    def start_engine(self):
        print('Car Engine Started')
        
class Byke(Vehicle):
    
    def start_engine(self):
        print('Byke Engine Started')
        
    def tyre(self):
        print('Byke have 2 Wheals')
    
def operate_vehicle(vehicle):
    vehicle.start_engine()
    vehicle.drive()
    vehicle.tyre()
    
car = Car()
byke = Byke()

operate_vehicle(car)
operate_vehicle(byke)