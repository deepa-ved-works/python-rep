#Try Block in Python
#Try block
#The try block lets you test a block of code for errors.

#Else
#You can use the else keyword to define a block of code to be executed if no errors were raised.

#Finally
#The finally block, if specified, will be executed regardless if the try block raises an error or not.

#Except
#The except block lets you handle the error. The finally block lets you execute code, regardless of the result of the try- and except blocks.

#Exception Handling
#When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

#Many Exceptions
#You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error.

"""
# try block in Python
try:
    a = 10 / 0
except Exception as e:
    print(e)

# Try Else
try:
    a = 10 / 25
except Exception as e:
    print(e)
else:
    print("A Value : ",a)

# Try else finally
try:
    a = 10 / 0
except Exception as e:
    print(e)
else:
    print("A Value : ",a)
finally:
    print("Thank You")


# Type of Exceptions in Python
print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))

# Nameerror Exception


try:
    print(a)
except NameError as e:
    print("A is not Defined")

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("denominator cant be zero")

try:
    a = int("Joes")
except ValueError as e:
    print("Please Enter Numbers only")

try:
    a = [10, 20, 30, 40]
    print(a[10])
except IndexError as e:
    print("Invalid Index")

try:
    f = open("tesot.txt")
except FileNotFoundError:
    print("File Not Found")
else:
    print(f.read())
"""

try:
    a = 10 / 20
    print(a)
    b = [10, 20, 30, 40]
    print(b[0])
    a = open('ramu.txt')
except ZeroDivisionError:
    print("denominator cant be zero")
except IndexError:
    print("Invalid Index")
except Exception as e:
    print(e)