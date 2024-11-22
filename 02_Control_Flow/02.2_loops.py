# For Loop

for i in range(1,6) :
    
    print(i)
    
for i in range(1,10,2) :
    
    print(i)
    
for i in range(10,1,-2) :
    
    print(i)
    
name : str = "Hamza atiq"

for i in name :
    
    print(i)
    
#########################################

# While loop

count : int = 0

while count<5:
    
    print(count)
    count=count+1
    
# Loop control statements

for i in range(10):
    
    if i==5:
        
        break
    
    print(i)
    
for i in range(10):
    
    if i % 2 == 0:
        
        continue
    
    print(i)
    
for i in range(5):
    
    if i == 3:
        
        pass
    
    print(i)
    
###################################

# Nested loops

for i in range(5):
    
    for j in range(2):
        
        print(f"i:{i} and j:{j}")
        
# sum of first 10 natural numbers using while loop

n : int = 10   
sum : int = 0
count : int = 1

while count <= n:
    
    sum = sum+count
    count += 1

print("Sum of first 10 natural number : " , sum)

# sum of first 10 natural numbers using for loop

n : int = 10   
sum : int = 0

for i in range(11):
    
    sum += i

print(sum)

# Prime numbers between 1 and 100

for num in range(1,101):
    
    if num > 1:
        
        for i in range(2,num):
            
            if num % i == 0:
                
                break
            
        else: 
            
            print(num)