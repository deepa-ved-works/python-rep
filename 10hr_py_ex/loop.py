# While Loop
"""
1.While Loop
2.For Loop
"""
i = 1
while i <= 10:
    print(i)
    i += 1
print("--------------------")
print("Even No : ")
n = 20
i = 2
while i <= 20:
    print(i)
    i += 2

# Continue Statement
i = 1
while i <= 20:
  if i % 2 == 0:
    i = i + 1
    continue;
  print(i)
  i += 1


# Break Statement
i = 1
while i <= 20:
  if i==7:
    break
  print(i)
  i += 1

  