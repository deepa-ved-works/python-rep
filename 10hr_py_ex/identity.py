#Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.

"""
is
is not
"""
a = [1, 2]
b = [1, 2]
c = a
print(id(a))
print(id(c))
print(id(b))
print(a is c)
print(a is b)
print(a==b)
print(a is not c)
print(a is not b)
print(a!=b)

#Membership operators
#Membership operators are used to test if a sequence is presented in an object.
a=[10,25,45,88]
print(22 in a)
print(22 not in a)