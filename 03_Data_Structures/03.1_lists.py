from typing import Any

lst : list = []
print(type(lst))

mixed_list : list[Any] = ['hamza' , 'atiq' , 1 , 3 , True , 27]

print(mixed_list)

print(mixed_list[0])
print(mixed_list[2])
print(mixed_list[4])
print(mixed_list[-1])

mixed_list[2] = 'boy'

print(mixed_list)

mixed_list[3:] = 'studying'

print(mixed_list) 

mixed_list.append('AI')

print(mixed_list)

mixed_list.insert(2 , 'rawalpindi')

print(mixed_list)

mixed_list.remove('i')

print(mixed_list)

mixed_list.pop()

print(mixed_list)

print(mixed_list.index('t'))

print(mixed_list.count('g'))

mixed_list.sort()

print(mixed_list)

mixed_list.reverse()

print(mixed_list)

print(mixed_list[::-1])

##############################

for i in mixed_list:
    
    print(i)
    
##############################
    
for index , i in enumerate(mixed_list):
    
    print(index , i)
    
new_lst : list = []

###############################

for x in range(10):
    
    new_lst.append(x**3)
    
print(new_lst)

##########################

lst_compre = [x**2 for x in range(10)]

print(lst_compre)

##########################

square_even = [x**2 for x in range(20) if x % 2 == 0]

print(square_even)

## Nested List Comphrension

lst1 : list[int] = [1,2,3,4]
lst2 : list[str] = ['a','b','c','d']

pair=[[i,j] for i in lst1 for j in lst2]

print(pair)

## List Comprehension with function calls
words : list[str] = ["hello" , "world" , "python" , "list" , "comprehension"]
lengths = [len(word) for word in words]
print(lengths)    

#################################

# Example 1

to_do_list : list[str] = ["Buy Groceries" , "Clean the house" , "Pay bills"]

## Adding to task
to_do_list.append("Schedule meeting")
to_do_list.append("Go For a Run")

## Removing a completed task
to_do_list.remove("Clean the house")

## checking if a task is in the list
if "Pay bills" in to_do_list:
    
    print("Don't forgrt to pay the utility bills")

print("To Do List remaining")

for task in to_do_list:
    
    if task != "Pay bills":
        
        print(f"-{task}")
        
##########################################

# Example 2

# Organizing student grades
grades : list[int] = [85 , 92 , 78 , 90 , 88]

# Adding a new grade
grades.append(95)

# Calculating the average grade
average_grade = sum(grades) / len(grades)
print(f"Average Grade: {average_grade:.2f}")

# Finding the highest and lowest grades
highest_grade = max(grades)
lowest_grade = min(grades)

print(f"Highest Grade: {highest_grade}")
print(f"Lowest Grade: {lowest_grade}")

###############################################

# Example 3

# Managing an inventory
inventory : list[str] = ["apples" , "bananas" , "oranges" , "grapes" , 'watermelon']

# Adding a new item
inventory.append("strawberries")

# Removing an item that is out of stock
inventory.remove("bananas")

# Checking if an item is in stock
item = "oranges"
if item in inventory:
    
    print(f"{item} are in stock.")
    
else:
    
    print(f"{item} are out of stock.")

# Printing the inventory
print("Inventory List:")

for item in inventory:
    
    print(f"- {item}")

#################################################

# Example # 4

# Collecting user feedback
feedback : list[str] = ["Great service!" , "Very satisfied" , "Could be better" , "Excellent experience"]

# Adding new feedback
feedback.append("Not happy with the service")

# Counting specific feedback
positive_feedback_count = sum(1 for comment in feedback if "great" in comment.lower() or "excellent" in comment.lower() or 'very satisfied' in comment.lower())
print(f"Positive Feedback Count: {positive_feedback_count}")

# Printing all feedback
print("User Feedback:")
for comment in feedback:
    print(f"- {comment}")
    
    