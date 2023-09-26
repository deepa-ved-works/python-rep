# For Loop in Python
for i in range(0, 21, 2):
    print(i)

for i in range(5):
    a=int(input("Enter a No : "))
    b=int(input("Enter a No : "))
    print(a+b)


# Nested For Loop
"""
*
**
***
****
*****

*****
****
***
**
*

ABCDE
ABCDE
ABCDE
ABCDE
ABCDE

A-Z => 65-90
a-z=> 97-122

"""

for i in range(6):
    for j in range(i):
        print("*",end="")
    print("")
print("----------------")

for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("")
print("----------------")

for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="")
    print("")


# While Else & For Else

i=1
while i<=5:
    #if(i==4):
        #break
    print(i)
    i+=1
else:
    print("Loop Completed")

for i in range(1,21):
    #if i==5:
        #break
    print(i)
else:
    print("For Loop Completed")