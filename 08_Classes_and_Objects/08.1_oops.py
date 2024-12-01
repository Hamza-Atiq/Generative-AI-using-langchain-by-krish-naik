# basic class 

class Car:
    
    pass

audi = Car()
bmw = Car()

print(type(bmw))
print(audi)

###########

# Instance Variable and methods

class Dog:
    
    # constructor
    
    def __init__(self , name , age):
        self.name = name            # self.name is instance variable
        self.age = age
        
        
# create object
dog1 = Dog('buddy' , 3)
print(dog1.name)
print(dog1.age)

##################

# Class with instance methods

class Dog:
    
    # constructor
    
    def __init__(self , name , age):
        self.name = name            # self.name is instance variable
        self.age = age
        
    def bark(self):
        print(f'{self.name} says woof')
        
dog2 = Dog('buddy' , 4)
dog2.bark()

print(dir(dog2))

#######################

# Modeling a bank account

class BankAccount:
    
    def __init__(self , owner , balance = 0):
        
        self.owner = owner
        self.balance = balance
        
    def deposit(self , amount ):
        
        self.balance += amount
        print(f'{amount} is deposited . new balance is {self.balance}')
        
    def withdraw(self , amount):
        
        if amount > self.balance:
            
            print('Insufficent balance')
            
        else:
            
            self.balance -= amount
            print(f'{amount} is withdrawn. new balance is {self.balance}')
            
    def get_balance(self):
        
        return self.balance
    
# create an account

account1 = BankAccount('hamza' , 1000)
print(account1.balance)
account1.deposit(2000)
account1.withdraw(5000)
account1.withdraw(500)
print(account1.get_balance())
        
