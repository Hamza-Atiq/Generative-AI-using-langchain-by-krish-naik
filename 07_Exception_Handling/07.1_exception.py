# Exception try , except block with customized statement

try:
    
    a = b
    
except:
    
    print("The variable has not been assigned")
    
##################

# try , except block with built in exception

try:
    
    a = b
    
except NameError as ex:
    
    print(ex)
    
#################

# try , except block with built in and customized exception

try:
    
    result = 1 / 0
    
except ZeroDivisionError as ex:
    
    print(ex)
    print("Please enter the denominator greater than 0")
    
#################

# try , except block with built in exception

try:
    
    result = 1 / 2
    
    a=b
    
except ZeroDivisionError as ex:
    
    print(ex)
    print("Please enter the denominator greater than 0")
    
except Exception as ex1:  # used for all type of exceptions
    
    print(ex1)
    print('Main exception got caught here')
    
####################

try:
    
    num = int(input("Enter a number : "))
    result = 10 / num
    
except ValueError:
    
    print("This is not a valid number")
    
except ZeroDivisionError:
    
    print("enter denominator greater than 0")
    
except Exception as ex:
    
    print(ex)
    
#####################

# try , except , else block
try:
    
    num = int(input("Enter a number : "))
    result = 10 / num
    
except ValueError:
    
    print("That's not a valid number!")
    
except ZeroDivisionError:
    
    print("You can't divide by zero!")
    
except Exception as ex:
    
    print(ex)
    
else:
    
    print(f"the result is {result}")
    
#######################

# try , except , else and finally
try:
    
    num = int(input("Enter a number : "))
    result = 10 / num
     
except ValueError:
     
    print("That's not a valid number!")
     
except ZeroDivisionError:
     
    print("You can't divide by zero!")
     
except Exception as ex:
    
    print(ex)
    
else:
    
    print(f"The result is {result}")
    
finally:
    
    print("Execution complete.")
    
########################

# File handling and Exception HAndling

try:
    
    file = open(r'07_Exception_Handling\example.txt' , 'r')
    content = file.read()
    a = b
    print(content)

except FileNotFoundError:
    
    print("The file does not exists")
    
except Exception as ex:
    
    print(ex)

finally:
    
    if 'file' in locals() or not file.closed():
        file.close()
        print('file close')
        
