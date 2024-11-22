from typing import Any

# creating a tuple

empty_tuple : tuple = ()
print(empty_tuple)
print(type(empty_tuple))

################

numbers : tuple[list[int]] = tuple([1 , 2 , 3 , 4 , 5 , 6])
print(numbers)

print(numbers[2])
print(numbers[-1])
print(numbers[::-1])

mixed_tuple : tuple[Any] = (1 , "Hello World" , 3.14 , True)

# Tuple Operations

concatenation_tuple = numbers + mixed_tuple
print(concatenation_tuple)

# Tuple Methods

print(numbers.count(1))
print(numbers.index(3))

# Packing and Unpacking tuple
# packing

packed_tuple = 1 , "Hello" , 3.14
print(packed_tuple)

# unpacking a tuple

a , b , c = packed_tuple

print(a)
print(b)
print(c)

# Unpacking with *

numbers : tuple[int] = (1 , 2 , 3 , 4 , 5 , 6)
first , *middle , last = numbers

print(first)
print(middle)
print(last)

nested_tuple : tuple[tuple[Any]]= ((1, 2, 3), ("a", "b", "c"), (True, False))

# access the elements inside a tuple
print(nested_tuple[0])
print(nested_tuple[1][2])

# iterating over nested tuples
for sub_tuple in nested_tuple:
    
    for item in sub_tuple:
        
        print(item , end=" ")
        
    print()
    
    