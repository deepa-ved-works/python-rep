'''
#Variable declaration and data type
a = 10.0
print(a)
print(type(a))
b = int(a)
print(b)
print(type(b))
a = 10.0
print(a)
print(type(a))
b = int(a)
print(b)
print(type(b))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# input function
a = int(input("Enter the value of A : "))
b = int(input("Enter the value of B : "))
c = a + b
print(c)

a = float(input("Enter the value of A : "))
b = float(input("Enter the value of B : "))
c = a+b
print(c)

a = int(input("Enter the value of A : "))
b = int(input("Enter the value of B : "))
c = a + b
print("Total : ", c)
print("Total : ", str(c))

#multiple input
# Enter three Names : shelly sri selvi
n1, n2, n3 = input("Enter three Names : ").split()
print("Name1 : ", n1)
print("Name2 : ", n2)
print("Name3 : ", n3)
#Enter three Names : Selvi,Sri,Shelly
n1, n2, n3 = input("Enter three Names : ").split(',')
print("Name1 : ", n1)
print("Name2 : ", n2)
print("Name3 : ", n3)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#String & multiline
a = """ Madhava Gopal from Salem, Tamilnadu, India, has written a book on Tamil Vedham 
which he claims to have existed 4 million years ago. 
He also claims that this knowledge was lost when Lemuria submerged into the sea. 
Madhava Gopal wants to share what he has learned with everyone"""
print(a)

para = []
print(type(para))
print(para)

para = [25, 33, 22]
print(para[0])
print(para[2])
print(para)

para = ["25", "33", "22"]
print(para)
print(",".join(para))
print("|".join(para))

para = []
print("Enter the para : ")
while True:
    line = input()
    if line:
        para.append(line)
    else:
        break
print(para)
output = '\n'.join(para)
print(output)

s = "ThamizhSelvi MithunaSri ShellyPearl"
print(s)
print(type(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count('e'))
print(s.endswith("rl"))
print(s.endswith("ri"))
print(s.find("a"))
print(s.find("a",5))
print(s.replace("a", "0"))
print(s.isupper())
print(s.islower())
print(s.isalpha())
print(s.isalnum())

a = "He\nis\ngood"
print(a)
print(a.splitlines())
print(a.splitlines(True))

a = "How was the day today."
print(a.split(" "))
a = "How,was,the,day,today."
print(a.split(","))

s = "      SelviSriShellyp         "
print(len(s))
print(len(s.strip()))
print(len(s.lstrip()))
print(len(s.rstrip()))

s = '13-03-2020'
print(s.partition('-'))

s = "Sample"
print(s)
print(s[0:2])
print(s[:5])
print(s[1:])
print(s[-1])
print(s[:-1])
print(s[-2:-1])
print(s[::-1])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#operators
#Arithmetic operators(+, -, *, /, %, //, **)
a = 123
b = 30
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(3**3)
#Assignment operators(+=, -+, *=, /=, %=, //=)
a = 123
print(a)
a += 30
print(a)
a -= 27
print(a)
a *= 30
print(a)
a /= 30
print(a)
a %= 30
print(a)
a //= 30
print(a)
# Comparision or Relational operators(==, !=, >, <, >=, <=)
a = 10
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
#Logical operators(and, or, not)
a = 24
print(a >= 9 and b <= 21)
print(a >= 9 or b <=21)
print(not(a >= 9 and b <= 21))
#Bitwise operator(&(AND), |(OR), ^(XOR), ~(NOT), <<, >>
a = 10
b = 11
print(a & b)
a = 25
b = 45
print(a | b)
print(a ^ b)
print(~a)
print(~b)
print(a << 2)
print(a >> 2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#If statement
#check given number is even
n = int(input("Enter the Number : "))
if(n%2 == 0):
    print(n," is even number")

#If else statement
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(name, "age is", age, "Eligible for vote.")
else:
    print(name, "age is", age, "Not eligible for vote.")

#elif statement:
#Return books 1 to 5 days delay 0.50 fine
#Return books 5 t0 10 days delay 1.00 fine
#Return books 10 to 30 days delay 5.00 fine
#Return books >30 days delay membership cancel
days = int(input("Enter the Days : "))
if(days == 0):
    print("Good, no fine")
elif(days >= 1 and days <= 5):
    print("Fine Amount : ", days * 0.50)
elif(days >= 5 and days <= 10):
    print("Fine Amount : ", days * 1.00)
elif(days >= 10 and days <= 30):
    print("Fine Amount : ", days * 5.00)
else:
    print("Membership Cancel")
'''
