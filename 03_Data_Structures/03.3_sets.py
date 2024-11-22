from typing import Any

# create a set

my_set : set[int] = {1 , 2 , 3 , 4 , 5}
print(my_set)
print(type(my_set))

my_set : set[int] = set([1 , 2 , 3 , 6 , 5 , 4 , 5 , 6])
print(my_set)

# Basics Sets Operation
# Adiing Elements

my_set.add(7)
print(my_set)

# Remove the elements from a set
my_set.remove(3)
print(my_set)

# if element not present in the set discord not gives error remove gives error
my_set.discard(11)
print(my_set)

# pop method pop first element
removed_element = my_set.pop()
print(removed_element)
print(my_set)

## clear all the elements
my_set.clear()
print(my_set)

# Set Memebership test
my_set : set[int] = {1 , 2 , 3 , 4 , 5}

print(3 in my_set)
print(10 in my_set)

# MAthematical Operation
set1 : set[int] = {1 , 2 , 3 , 4 , 5 , 6}
set2 : set[int] = {4 , 5 , 6 , 7 , 8 , 9}

# Union
union_set = set1.union(set2)
print(union_set)

# Intersection
intersection_set = set1.intersection(set2)
print(intersection_set)

# Difference 
print(set1.difference(set2))

print(set2.difference(set1))

# Symmetric Difference
print(set1.symmetric_difference(set2))


set1.intersection_update(set2)
print(set1)
print(set2)

set2.intersection_update(set1)
print(set1)
print(set2)

# Sets Methods
set1 : set[int] = {1 , 2 ,  3 , 4 , 5}
set2 : set[int] = {3 , 4 , 5}

# is subset
print(set1.issubset(set2))

print(set1.issuperset(set2))

# Counting Unique words in text

text : str = "In this tutorial we are discussing about sets"
words = text.split()
print(words)

# convert list of words to set to get unique words

unique_words=set(words)

print(unique_words)
print(len(unique_words))