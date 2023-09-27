# print (15/7*6)
"""
import keyword
print(keyword.kwlist)

name = input("Enter a string")
print(type(name))
print(name)

a = int(input("Enter the value of A : "))
b = int(input("Enter the value of B : "))
c = a + b
print (c)
print(type(a))

a = float(input("Enter the value of A : "))
b = float(input("Enter the value of B : "))
c = a + b
print (c)
print(type(a))

name1,name2,name3 = input("Enter 3 Names").split(',')
print("Name 1 : ",name1)
print("Name 2 : ",name2)
print("Name 3 : ",name3)
"""
a = "lion pride"
b = """ George Washington's Socks is the story of a group of 
kids who take a backyard camping trip and end up traveling 
through time to a critical point in the American Revolutionary War. 
As the story begins, ten-year-old Matt Carlton is looking forward to the first meeting of an adventure club 
he is starting with his friends."""
"""
print(type(a))
print (b)

para=[25, 22, 23]
print(para[0])
print(type(para))

para=["25", "22", "23"]
#print(','.join(para))
print('|'.join(para))
print(type(para))

para = []
print("Enter a para : ")

while True:
    line = input()
    if line:
        para.append(line)
    else:
        break
print(para)
book = '\n'.join(para)
print (book)

#type casting
a = 10.0
print(a)
print(type(a))
b = int(a)
print(b)
print(type(b))

a = int(input("Enter the value of A : "))
b = int(input("Enter the value of B : "))
c=a+b
print("Total : ", + c)
print("Total : " + str(c)

#string functions
s = "Tutor Joes"
print(s)
print(type(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count("t"))
print(s.endswith("es"))
print(s.find("o"))
print(s.find("o",5))
print(s.replace("o",'0'))
a = "JOES"
print("Is Upper : ",a.isupper())
print("Is Lower : ",a.islower())
print("Is Alpha Numeric : ",a.isalnum())
print("Is Alpha : ",a.isalpha())
s = "he\nis\ngood"
print(s)
print(s.splitlines())
print(s.splitlines(True))
a = "Tutor Joes Computer Education"
print(a.split(","))
print(a.split(" "))
s = "     Joes     "
print(len(s))
print(len(s.strip()))
print(len(s.lstrip()))
print(len(s.rstrip()))
s = "12-3-2020"
print(s.partition("-"))

#string manupilation
s = "sample"
print(s)
print(s[0:2])
print(s[:5])
print(s[1:])
print(s[-1])
print(s[-2:-1])
print(s[::-1])

#Arithmetic Operations
a = 123
b = 10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(2**3)

#Assignment Operators
a = 125
print(a)
a += 5 #a = a + 5
print(a)
a -= 10 #a = a - 10
print(a)
a *= 10 #a = a * 10
print(a)
a /= 10 #a = a / 10
print(a)
a %= 10 #a = a % 10
print(a)
a //= 10 #a = a // 10
print(a)

#Compaison Operators
a = 10
b = 20
print(a == b)
print(a != b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#Logical Operators
a = 10
print(a >= 10 and a<=10)
a = 25
print(a >= 10 and a<=10)
print(a >= 10 or a<=10)
print(not(a >= 10 and a<=10))

#Bitwise Operators
#   &   AND
#   |   OR
#   ^   XOR
#   ~   NOT
#   <<  Zero fill left shift
#   >>  Signed right shift

a = 25
b = 45
print(a&b)

a = 10
b = 11
print(a&b)

a = 25
b = 45
print(a|b)

a = 25
b = 45
print(a^b)

a = 25
b = 45
print(~a)

print(a<<2)
print(a>>2 )

#if statement
n = int(input("Enter Any Number"))
if n%2 == 0:
    print(n, "is an even number")
else:
    print(n, "is an odd number")

# If else statement
name = input("Enter your name")
age = int(input("Enter your age"))
if age>= 18:
    print(name, " age is ", age, "eligible for voteing")
else:
    print(name, "age is ", age, "and not eligible to vote")

# elif statement
#   1-5         0.5
#   5-10        1
#   10-30       5
#   >30         Membership Cancel

days = int(input("Enter a number of days"))
if days==0:
    print("Good,No fine")
elif days >=1 and days <=5:
    print("Fine amount : ", days * 0.5)
elif days>=5 and days<=10:
    print("Fine amount : ",days*1)
elif days>=10 and days<=30:
    print("Fine amount : ",days*5)
else:
    print("Membership Cancel")

# Nested if statement
# Total
# Average
# Result
# If pass grade
#   90-100  A
#   80-89   B
#   70-79   C

m1 = int(input("Enter Mark 1"))
m2 = int(input("Enter Mark 2"))
m3 = int(input("Enter Mark 3"))
total = m1 + m2 + m3
average = total/3.0
print("Total : ", total)
print("Average : ", average)
if m1>=35 and m2>= 35 and m3>= 35:
    print("Result : Pass")
    if average>=90 and average <=100:
        print("Grade : A")
    elif average >=80 and average <=89:
        print("Grade : B")
    elif average >=70 and average <=79:
        print("Grade : C")
    else:
        print("Grade : D")
else:
    print("Result : Fail")
    print("Grade : F")

# While Loop
i = 1
while i<=10:
    print(1)
    i+=1
print("---------------------")
print("Even Number: ")
n = 28
i = 2
while i<=28:
    print(i)
    i+=2

print("Odd Number: ")
n = 28
i = 0
while i<=28:
    print(i)
    i+=5

# Contiue Statement
i = 1
while i <= 20:
    if i%2==0:
        i=i+1
        continue
    print(i)
    i+=1

# Break Statement
i = 1
while i <= 20:
    if(i==7):
        break
    print(i)
    i+=1

# Break Statement
#   1-5     =>1,2,3,4,5
#   0-5     =>2,4  +2
#range(2,5)  =>

a = list(range(5))
print(a)

print(list(range(2,5))) #n-1
print(list(range(0,21,2)))
print(list(range(1,20,2)))

# For loop
for i in range(1,21):
    print(i)
print("--------------------------")
for i in range(1,21,2):
    print(i)
print("--------------------------")
for i in range(5):
    a = int(input("Enter a number"))
    b = int(input("Enter a number"))
    print(a+b)

# Nested for loop
for i in range(6):
    for j in range(i):
        print("*",end="")
    print("")
print("------------------------------------")
for i in range(5,0,-1):
    for j in range(i):
        print("*", end="")
    print("")
print("------------------------------------")
for i in range(65,70,1):
    for j in range(64,70,1):
        print(chr(j),end="")
    print("")

#While else and for else
i = 1
while i<=5:
    print(i)
    i+=1
else:
    print("Loop Completed")

for i in range(1,21):
    if i==5:
        break
    print(i)
else:
    print("For Loop Completed")

#List and its functons
a = [1, 2, 3, 4, 5]
print(a)
print(type(a))
a[0]=100
print(a)
print(a[0:3])
print(a[2:])
print(a[:3])

print("-------------------------")
a = [1,True,"Selvi",2.5,[1,2,3,4]]
print(a)
print(type(a))
print(type(a[0]))
print(a[0],"type is", type(a[0]))
print(a[1],"type is", type(a[1]))
print(a[2],"type is", type(a[2]))
print(a[3],"type is", type(a[3]))
print(a[4],"type is", type(a[4]))
print(a[4][1])
print("-------------------------")
a = [10, 25, 35, 45]
print(a)
a.clear()
print(a)
a = [10, 25, 35, 45]
b= a.copy()
print(b)
a = [10, 25, 35, 45, 25, 4, 25]
print(a.count(25))
print(a.index(25))
print(len(a))
print(max(a))
print(min(a))
print(a)
a.pop(0) # Removes element using index
print(a)
a = [10, 25, 35, 45, 25, 4, 25]
a.remove(25) # Removes values
print(a)
print("-------------------------")
names = ["Selvi"]
print(names)
names.append("Sri")
names.append("Shelly")
print(names)
name2=("Emmma","Lia")
names.extend(name2)
print(names)
names.insert(4,"Fleur")
print(names)
print(list(range(5)))
print(list("Tutor Joes"))
a = [10,50,100,85]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=["Orange","Apple","Zebra"]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=["Orange","Apple","Zebra"]
a.sort(key=len)
print(a)

# Tuples and it's functions
a = (1, 2.5, True,"Selvi")
print(a)
print(type(a))
print(a[1])
print(a[-1])
print(a[0:2])
b = list(a)
print(b)
b.append("Raja")
print(b)
print(type(b))
a=tuple(b)
print(a)
print(type(a))

for i in a:
    print(i)
if "Raja" in a:
    print("Raja is found")
else:
    print("Not found")
print(len(a))

a = (1,)
print(type(a))
del a
a = (1,2,7,4)
b = (5,6,7,8)
c = a + b
print(c)
print(c.count(7))
# Nested Tuples
a = (1,2,7,4)
b = (5,6,7,8)
c = (a,b)
print(c)
print(c[1])
print(c[0][1])

x = ("Joes",) * 10
print(x)
a = (1,2,7,4)
print(min(a))
print(max(a))

# Sets and its functions
names = {"Selvi", "Sri", "Shelly"}
print(names)
print(type(names))

# Access Values Using For Loop
for name in names:
    print(name)
# Adding new elements
names.add("Emma")
print(names)

# Update Another Set of Data
a = {"Poppy", "Branch", "Tiny Diamond"}
names.update(a)
print(names)
names.remove("Emma")
print(names)
names.discard("Branch")
print(names)
names.pop()
print(names)

names.clear()
print(names)

del names

names = {"Selvi", "Selvi", "Sri", "Shelly","Poppy", "Branch", "Tiny Diamond"}
print(names)

a = {1,2,3,4}
b = {"a","b","c","d"}
c = a.union(b)
print(c)
a.update(b)
print(a)

a = {1,2,3,4,5}
b = {5,6,7,8,9}
c = a.intersection(b)
print(c)
a.intersection_update(b)
print(a)

a = {5,6,7,8,9}
b = {5,6,7,8,9}
c = a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)

c = a.isdisjoint(b)
print(c)
c = a.issubset(b)
print(c)

c = a.issubset(b)
print(c)
c = a.issuperset(b)
print(c)

# Dictionary and its functions
user = {
    "Name" : "Selvi",
    "Age": 11,
    "Is married": "False"
}

print(user)
print(type(user))
print(user["Name"])
print(user.get("Age"))
print(user.keys())
print(user.values())
print(user.items())

for x in user:
    print(x, " ", user[x])

for x in user.values():
    print(x)

for x in user.keys():
    print(x)

for x,y in user.items():
    print(x,y)

if "gender" in user:
    print("Present")

# Changing Values
user.update({"gender":"Female"})
print(user)
user["age"]=35
user.pop("age")
print(user)
user.clear()
print(user)

users = {
    "user1" : {
    "Name" : "Selvi",
    "Age": 11,
    "Is married": "False"
    },
    "user2" : {
    "Name" : "Sri",
    "Age": 8,
    "Is married": "False"
    }
}
print(users)

# Identify Operators in Python
a = [1,2]
b = [1,2]
c = a
print(id(a))
print(id(b))
print(id(c))
print(a is c)
print(a==b)
print(a is not c)
print(a is not b)
print(a!=b)

#Membership Operators
a = [10,25,45,88]
print(22 in a)
print(22 not in a)

# User Define Function in Python
def welcome():
    print("Welcome to Tutor Joes.")
welcome()
welcome()
welcome()

#No Return Type Without Arguement Fuction In Python
def add():
    a = int(input("Enter the value of a"))
    b = int(input("Enter the value of b"))
    c = a + b
    print("Total ", c)

add()

# No return Type With Arguements Functions in Python
def sub(a,b):
    c = a - b
    print("Difference :", c)

sub(25, 6)

#Return Type Without Arguement Function In Python
def mul():
    a = int(input("Enter the value of a"))
    b = int(input("Enter the value of b"))
    c = a * b
    return c

x = mul()
print("Mul ", x)

# Return Types With Arguements Function In Python
def div(a,b):
    c = a / b
    return c

x = div(25, 2)
print("Division", x)

# Arbitary Arguement Function In Python (*)

def class_10(*students):
    print(students)
    for user in students:
        print(user)

class_10("Selvi", "Sri", "Shelly", "Emma")

# Keyword Arguement Function In Python
def message(name, age):
    print(name,"age is", age)

message(age = 11, name = "Selvi")

# Arbitrary Keyword Arguements Functions In Python
def bioData(**Data):
    print(Data)

bioData(name = "Selvi", age = 11, gender = "Female")

# Default Parameter Function In Python
def user(name, city = "Burbank"):
    print(name, " is from ", city)

user("Selvi", "Burbank")
user("Sri")

# Passing A List As An Arguemnet In Function
def total(marks):
    return sum(marks)

print("Total : ",total([55, 75, 95, 47]))

# Recursive Function Python
def factorial(x):
    if x==1:
        return 1
    else:
        return(x * factorial(x - 1))

print("Factorial : ", factorial(5))

# Lambda Function In Python
c = lambda a : a + 50
print(c(5))

c = lambda a,b:a*b
print(c(10,25))

# Date Time Package in Python
import datetime as dt

current_date = dt.date.today()
print("Current Date : ", current_date)

new = dt.date(2021, 10, 25)
print(new)
print("Year : ", new.year)
print("Month : ", new.month)
print("Day : ", new.day)
print("----------------------")
a = dt.time(10, 45, 5, 55505)
print(a)
print("Hour : ", a.hour)
print("Minute : ", a.minute)
print("Second : ", a.second)
print("Microsecond : ", a.microsecond)
print("----------------------")
current_time = dt.datetime.now()
print("Current Time : ", current_time)
new = dt.datetime(2021,5,31,17,2,10)
print(new)
print(new.date())
print(new.time())
print("----------------------")
current = dt.datetime.now()
new_year = dt.datetime(2022, 1, 1)
diffrence = new_year-current
print(diffrence)
print("----------------------")
current = dt.datetime.now()
print(current)
s = current.strftime("%A %B %D %Y")
print(s)

# Maths Function
import math
print(math.sqrt(4))
print(math.ceil(1.55555))
print(math.floor(1.55555))
print(math.factorial(5))
print(math.fabs(5))
print(math.pow(2, 3))
print(math.log2(2))
print(math.log10(2))
print(math.pi)
print(math.e)

# Try Block In Python
try:
    a = 10/0
except Exception as e:
    print(e)

# Try Except Else in Python
try:
    a = 10/25
except Exception as e:
    print(e)
else:
    print("A Value : ",a)

# Try Except Else Finally in Python
try:
    a = 10/25
except Exception as e:
    print(e)
else:
    print("A Value : ",a)
finally:
    print("Thank You")

# Types Of Exception In Python
print(dir(locals()["__builtins__"]))
print(len(dir(locals()["__builtins__"])))

try:
    print(a)
except NameError as e:
    print("A is not defined.")

try:
    print(10/0)
except ZeroDivisionError as e:
    print("Denominator can't be zero.")

try:
    a = int("Joes")
except ValueError as e:
    print("Please Enter Numbers Only")

try:
    a = [10,20,30,40]
    print(a[10])
except IndexError as e:
    print("Invalid Index")

try:
    f = open("text.txt")
except FileNotFoundError :
    print("File Not Found")
else:
    print(f.read())

# Handing Multiple Exceptions In Python
try:
    a = 10/20
    print(a)
    b = [10,20,30,40]
    print(b[10])
except ZeroDivisionError:
    print("Denominator cannot be zero.")
except IndexError:
    print("Invalid Index")

# Class and Objects
class car():
    pass

a = 10
print(type(a))
print(type(car))
swift = car()
print(isinstance(swift,car))
print(isinstance(a,int))
print(type(swift))

# Class Attributes In Python
class student():
    name = "Selvi"
    age = 11

# getattr method
print(getattr(student, "name"))
print(getattr(student, "age"))
print(getattr(student, "gender", "No Such Attribute Found"))

# Dot Notification
print(student.name)
print(student.age)

# setattr
setattr(student, "name", "Sri")
print(student.name)

setattr(student, "gender", "Female")
print(student.gender)

student.city = "Burbank"
print(student.city)

print(student.__dict__)
delattr(student,"city")
print(student.__dict__)
del student.gender
print(student.__dict__)

# Instance Attributes In Python
class user():
    course = "Java"

o = user()
print(user.__dict__)
print(user.course)
print(o.__dict__)
print(o.course)
o.course = "C++"
print(o.__dict__)
print(o.course)

o2 = user()
print(o2.course)

# Class Method
class student():
    name = "Selvi"
    age = 11

    def printall():
        print("name", student.name)
        print("age", student.age)

student.printall()
print(student.__dict__)

print(getattr(student,"printall"))
getattr(student,"printall")()

student.__dict__["printall"]()

# Instance Method In Python
class student():
    name = "Selvi"
    age = 11

    def printall(self,gender):
        print("name : ", student.name)
        print("age : ", student.age)
        print("gender : ", gender)

o = student()
o.printall()
student.printall(o)
o.printall("Female")
student.printall(o,"Female")

# Init Method
class user():
    def __init__(self,name):
        print("Call When No Instance Created")
        self.name = name
    def printall(self):
        print("Name : ", self.name)

o1 = user("Selvi")

o1.printall()
print(o1.__dict__)
o2 = user("Sri")
o2.printall()
print(o2.__dict__)
print(user.__dict__)

# Property Decorator In Python
class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        #self.msg = self.name + " is " + str(self.age) + " year old."
        
    @property
    def msg(self):
        return self.name + " is " + str(self.age) + " year old."

o = user("Selvi", 11)
print(o.name)
print(o.age)
print(o.msg)
o.age = 12
print(o.msg)

#Property Decorators Getter Setter In Python
class student():
    def __init__(self,total):
        self._total = total
    def average(self):
        return self._total/5.0
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, t):
        if t<0 or t>500:
            print("Invalid Total and can't change")
        self._total = t

o = student(450)
print("Total : ", o.total)
print("Average : ", o.average())
o.total = 250
print("Total : ", o.total)
print("Average : ", o.average())

# Property Method In Python
class student():
    def __init__(self,total):
        self._total = total

    def average(self):
        return self._total/5.0

    def getter(self):
        return self._total

    def setter(self, t):
        if t<0 or t>500:
            print("Invalid Total and can't change")
        self._total = t

    total = property(getter, setter)

o = student(450)
print("Total : ", o.total)
print("Average : ", o.average())
o.total = 350
print("Total : ", o.total)
print("Average : ", o.average())

# Class Method Decorator In Python
class student:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.count += 1

    def printDetail(self):
        print("Name : ", self.name, " Age : ", self.age)

    @classmethod
    def total(cls):
        return cls.count

o = student("Selvi", 11)
o.printDetail()
print("Total Admission : ", o.total())
a = student("Sri", 8)
a.printDetail()

print("Total Admission : ", student.total())

#Static Method In Python
class student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printDetail(self):
        print("Name : ", self.name, "Age : ", self.age)

    @staticmethod
    def welcome():
        print("Welcome to our Institution")

s1 = student("Selvi", 11)
s1.printDetail()
s1.welcome()

s2 = student("Sri", 8)
s2.printDetail()
s2.welcome()

# Abstaraction And Encapsulation In Python
class libraray:
    def __init__(self, books):
        self.books = books

    def list_books(self):
        print("Available Books")
        for book in self.books:
            print(book)

    def borrow_book(self, borrow_book):
        if borrow_book in self.books:
            print("Get Your Book Now.")
            self.books.remove(borrow_book)
        else:
            print("Book Not Available")

    def recieve_book(self, recieve_book):
        print("You Have Returned The Book")
        self.books.append(recieve_book)

books = ["C", "C++", "Java", "The Kingdom of Fantasy", "Case Solved"]
o = libraray(books)

msg = 
        1. Display Book
        2. Borrow Book
        3. Return Book

while True:
    print(msg)
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        o.list_books()
    elif ch == 2:
        book = input("Enter Book Name To Borrow : ")
        o.borrow_book(book)
    elif ch == 3:
        book = input("Enter Book Name To Return : ")
        o.recieve_book(book)
    else:
        print('Thank You, Come Again')
        quit()

# Single Inheritance
class Nokia:
    company = "Nokia India"
    website = "www.nokia-india.com"

    def contact_details(self):
        print("Adress : Cherry Road, Near Bus Street, Salem")

class Nokia1100(Nokia):
        def __init__(self):
            self.name = "Nokia 1100"
            self.year = 1998
        def product_details(self):
            print("Name : ", self.name)
            print("Year : ", self.year)
            print("Company : ", self.company)
            print("Website : ", self.website)

mobile = Nokia1100()
mobile.product_details()
mobile.contact_details()

# Multiple Inheritence
class Father:
    def fishing(self):
        print("Fishing in Rivers")
    def chess(self):
        print("Playing Chess From Father")

class Mother:
    def cooking(self):
        print("Cooking Food")
    def chess(self):
        print("Playing Chess From Mother")

class Son(Mother,Father):
    def ride(self):
        print("Riding Bicycle")

o = Son()
o.ride()
o.fishing()
o.cooking()
o.chess()

# Multileval Inheritance
class Grandfather:
    def ownHouse(self):
        print("Grandpa House")

class Father(Grandfather):
    def ownBike(self):
        print("Father's Bike")

class Son(Father):
    def ownBook(self):
        print("Son Have A Book")

o = Son()
o.ownHouse()
o.ownBike()
o.ownBook()
"""
# Function Overriding In Python
class Employee:
    def WorkingHrs(self):
        self.hrs = 50

    def printHrs(self):
        print("Total Working Hours : ", self.hrs)

class Trainee(Employee):
    def WorkingHrs(self):
        self.hrs = 60

    def resetHrs(self):
        super().WorkingHrs()

employee = Employee()
employee.WorkingHrs()
employee.printHrs()

trainee = Trainee()
trainee.WorkingHrs()
trainee.printHrs()