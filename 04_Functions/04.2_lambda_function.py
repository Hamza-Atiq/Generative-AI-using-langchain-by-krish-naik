# syntax 

# lambda arguments : expression

# addition using lambda

addition = lambda a , b : a + b

print(addition(3,7))

addition1 = lambda x , y , z : x + y + z

print(addition1(13 , 14 , 19))

# Even number checker

even = lambda num : num % 2 == 0

print(even(45))
print(even(44))

# map()- applies a function to all items in a list

numbers_lst : list[int] = [1 , 2 , 4 , 6 , 3 , 7 , 9]

print(list(map(lambda x : x ** 2 , numbers_lst)))