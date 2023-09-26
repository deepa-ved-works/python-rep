"""Type casting is a method used for changing the variables/ values declared in a
certain data type into a different data type in order to match for the operation
required to be performed by the code snippet. In python, this feature can be accomplished by using the constructor
functions like int(), string(), float(), etc.
"""

a = 10.0
print(a)
print(type(a))
b = int(a)
print(b)
print(type(b))

#int()
#float()
#str()

a = int(input("Enter The Value of A : "))
b = int(input("Enter The Value of B : "))
c = a + b
print("Total : " + str(c))