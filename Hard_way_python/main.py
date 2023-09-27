"""
# print statement
print("Hello World")
print("I will count my chickens: ")
print("Hens",25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)
print("Now I will count the eggs: ")
print(3+2+1-5+4%2-1/4+6)
print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5- 7)

cars=100
print("There are", cars, "cars available")
my_name = 'Deepa'
my_height = 74
my_weight = 65
print(f"Let's talk about {my_name}")
total = my_height + my_weight
print(f"if I add {my_height}, {my_weight} I get {total}.")

types_of_people = 10
x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
print(x)
print(y)
print(f"I said: {x}")
print(f"I also said: '{y}'")


print("Mary had a little lamb, little lamb, little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Marry went.")
print("." * 26)
endl1 = "C"
endl2 = "h"
endl3 = "e"
endl4 = "e"
endl5 = "s"
endl6 = "e"
endl7 = "B"
endl8 = "u"
endl9 = "r"
endl10 = "g"
endl11 = "e"
endl12 = "r"
print(endl1 + endl2 + endl3 + endl4 + endl5 + endl6, end=' ')
print(endl7 + endl8 + endl9 + endl10 + endl11 + endl12)


formatter = "{} {} {} {} {} {} "
print(formatter.format(1, 2, 3, 4, 5, 6))
print(formatter.format("one", "two", "three", "four", "five", "six"))
print(formatter.format(True, False, True, False, True, False))
print(formatter.format("Deepa Ponnusamy",
                       "Selvi Eswaran",
                       "Sri Eswaran",
                       "Shelly Eswaran",
                       "Eswaran Palanisamy",
                       "Komarapalayam"))

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print("Here are the days: ", days)
print("Here are the months: ", months)

tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\a \\ cat."
fat_cat =
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print("How old are you?", end=' ')
age = input()
print("Haw tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()
print(f"So you're {age} years old, {height} inch tall and {weight} kg heavy.")

from sys import argv
script, first, second, third = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
#(venv) linuxdeepa.my.lan@linuxdeepa:~/PycharmProjects/Hard_way_python> python3.6 main.py first 2nd 3rd
#The script is called: main.py
#Your first variable is: first
#Your second variable is: 2nd
#Your third variable is: 3rd
"""
