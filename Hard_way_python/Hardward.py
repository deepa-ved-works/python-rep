'''
#hello.py
#Ask user for their name
#name = input("What's your name?")
# or
name = input("What's your name?").strip().title()

#Remove whitespaces from string
#name = name.strip()

# Capitialize user's name
#name = name.capitalize()
#name = name.title()
# or
#Remove whitespaces from string and Capitialize user's name
#name = name.strip().title()

#Split user's name into first and last
first, last = name.split(" ")
#print(f"Hello, {first} {last}")
print(f"Hello, {first}")
#say hello to user
#print("Hello,")
#print(name)
# or
#print("Hello," + name)
# or
#print("Hello,", end = "")
#print(name)
# or
#print("Hello,", name)
# or
print(f"Hello, {name}")
'''
'''
#calculator
x = 1
y = 2
z = x + y
print(z)

#x = input("What's x?")
#y = input("What's y? ")
#z = int(x) + int(y)
#print(z)
#or
#x = int(input("What's x?"))
#y = int(input("What's y? "))
#print(x + y)

#x = float(input("What's x?"))
#y = float(input("What's y? "))
#print(x + y)
#or
#z = round(x + y)
#print(f"{z:,}")

#x = float(input("What's x?")) #2
#y = float(input("What's y? "))#3
#z = x / y
#print(f"{z:,2f}")
'''
'''
#functions.py
#function
#def hello(to="world"):
#    print("hello,", to)
#hello()
#name = input("What's your name?")
#hello(name)

#def main():
#    name = input("What's your name?")
#    hello(name)
#def hello(to="World"):
#    print("hello,", to)
#main()

def main():
    x = int(input("What's x?"))
    print("x squared is", square(x))
def square(n):
    #return n * n
    #return n ** 2
    return pow(n, 2)
main()
'''
'''
#compare.py
x = int(input("What's x?"))
y = int(input("What's y?"))

if(x < y):
    print("x is less than y")
elif(x > y):
    print("x is greater than y")
elif(x == y):
    print("x is equal to y")
'''
'''
#grade.py
score = int(input("Score:"))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
'''
'''
#parity_odd_even.py
def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False # or
    #return True if n % 2 == 0 else False # or
    #return n % 2 == 0
main()
'''
'''
#house.py
name = input("What's your name? ")
if name == "Cho":
    print("Ravenclaw")
elif name == "Pansy":
    print("Slytherin")
elif name == "Cedric":
    print("Hufflepuff")
elif name == "Dean" or name == "Ginny" or name == "Seamus":
    print("Gryffindor")
else:
    print("Who")
'''

# match_case
name = input("What's your name? ")
match name:
    case "Cho":
        print("Ravenclaw")
    case "Pansy":
        print("Slytherin")
    case "Cedric":
        print("Hufflepuff")
    case "Seamus":
        print("Gryffindor")
