# IF Statement in Python

n = int(input("Enter The Number : "))
if n % 2 == 0:
    print(n, " is Even Number")

# IF Else Statement in Python

name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
if age >= 18:
    print(name, " age is ", age, " Eligible for Vote.")
else:
    print(name, " age is ", age, " Not Eligible for Vote.")


# elif Statement in Python
"""
0       No Fine
1-5     0.5
5-10    1
10-30   5
>30     Membership Cancel
"""
days = int(input("Enter The Days : "))
if days == 0:
    print("Good No Fine")
elif days >= 1 and days <= 5:
    print("Fine Amount : ", days * 0.5)
elif days > 5 and days <= 10:
    print("Fine Amount : ", days * 1)
elif days > 10 and days <= 30:
    print("Fine Amount : ", days * 5)
else:
    print("Membership Cancel")

# Nested If Statement in Python
"""
3 Marks as Input
Total
Average
Result
If Pass Grade
    90-100 A
    80-89 B
    70-79 C
    Else D
"""
m1 = int(input("Enter Mark-1  : "))
m2 = int(input("Enter Mark-2  : "))
m3 = int(input("Enter Mark-3  : "))
total = m1 + m2 + m3
average = total / 3.0
print("Total  : ", total)
print("Average  : ", average)
if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Result  : Pass")
    if average >= 90 and average <= 100:
        print("Grade : A")
    elif average >= 80 and average <= 89:
        print("Grade : B")
    elif average >= 70 and average <= 79:
        print("Grade : C")
    else:
        print("Grade : D")
else:
    print("Result  : Fail")
    print("Grade   : No Grade")