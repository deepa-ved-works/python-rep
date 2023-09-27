'''
#ex1.py
print("Hellow World")
#print("Hello again")
#print("I like typing this.")
#print("This is fun.")
#print("Yay! Printing.")
#print("I'd much rather you 'not'.")
#print('I"said" do not touch this.')
#print("I like typing this.")
print("----------------------")
print("Another line.")
'''
'''
#ex2.py
# A comment, this is so you can read your program later.
# Anything after the # is ignored by python,
print("I could have code like this.") # and the comment after is ignored
# You can also use a comment to "disable" or comment out code:
# print("This won't run.")
print("This will run.")
'''
'''
#ex3.py
print("I will now count my chickens:")
print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)
print("Now I will count the eggs: ")
print(3 + 2 + 1 -5 + 4 % 2 - 1 / 4 + 6)
print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)
print("what is 3 + 2?", 3 + 2)
print("what is 5 - 7?", 5 - 7)
print("Oh, that's why it's False.")
print("How about some more.")
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
'''
'''
#ex4.py
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
'''
'''
#ex5.py
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")
# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
'''
'''
#ex6.py
#define a variable
types_of_people = 10
x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
print(x)
print(y)
print(f"I said: {x}")
print(f"I also said: '{y}'")
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))
w = "This is the left side of..."
e = "a string with a right side."
print(w + e)
'''
'''
#ex7.py
print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # what'd that do?
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# watch end = ' ' at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
'''
'''
#ex8.py
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
 ))
'''
'''
#ex9.py
# Here's some new strange stuff, remember type it exactly.
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print("Here are the days: ", days)
print("Here are the months: ", months)
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
 """)
'''
'''
#ex10.py
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print("This is a tubby cat {}".format(tabby_cat))
'''
'''
#ex11.py
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()
print(f"So, you're {age} year's old, {height} feet tall and {weight} kg heavy.")
'''
'''
#ex12.py
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
'''
'''
#ex13.py
from sys import argv
# read the WYSS section for how to run this
script, first, second, third, fourth = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your third variable is:", fourth)
user_input = input("Add some text: ")
print(f"Your input is: {user_input}.")
'''
'''
#ex14.py
from sys import argv
script, user_name, age = argv
prompt = '>>> '
print(f"Hi {user_name}, I'm the {script} script.")
print(f"You are {age} year's old.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)
print(f"Where do you live {user_name}?")
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
'''
'''
#ex15.py read file
from sys import argv
script, filename = argv
txt = open(filename)
print(f"Here's your file {filename}:")
print(txt.read())
print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())
'''
'''
#ex16.py   write file
from sys import argv
script, filename = argv
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")
print("Opening the file...")
target = open(filename, 'w')
print("Truncating the file. Goodbye!")
target.truncate()
print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("I'm going to write these to the file.")
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")    or
target.write(f"{line1}\n{line2}\n{line3}\n")
print("And finally, we close it.")
target.close()
txt = open(filename)
print(txt.read())
txt.close()
'''
'''
#ex17.py   copy and paste from one file to another file
from sys import argv
from os.path import exists
script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")
# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()  #or
#in_file = open(from_file).read()
print(f"The input file is {len(indata)} bytes long")
#print(f"The input file is {len(in_file)} bytes long")
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()
out_file = open(to_file, 'w')
out_file.write(indata)
#out_file.write(in_file)
print("Alright, all done.")
out_file.close()
in_file.close()              ,
'''
'''
#ex18.py
# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")
# this one takes no arguments
def print_none():
    print("I got nothin'.")
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
'''
'''
#ex19.py
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
'''
'''
#ex19a.py
def add_two_numbers(number1, number2):
    print(f"{number1} + {number2} equals {number1 + number2}.")
add_two_numbers(1,9)
add_two_numbers(2,3)
add_two_numbers(1 + 2, 3 + 7)
add_two_numbers(5 - 2, 2 - 1)
add_two_numbers(2 + 3, 7 - 2 )
number1 = 3
number2 = 8
add_two_numbers(number1, number2)
add_two_numbers(number1 + number2, number2 - number1)
add_two_numbers(number1 + 5, number2 + 2)
add_two_numbers(number1 - 1, number2 - 3)
add_two_numbers(number1 + number1 + number2, 31 + 2)
'''
'''
#ex20.py
from sys import argv
script, input_file = argv
def print_all(f):
    print(f.read())
def rewind(f):
    f.seek(0)
def print_a_line(line_count, f):
    print(line_count, f.readline())
current_file = open(input_file)
print("First let's print the whole file:\n")
print_all(current_file)
print("Now let's rewind, kind of like a tape.")
rewind(current_file)
print("Let's print four lines:")
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
'''
'''
#ex21.py
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b
def power(a, b):
    print(f"{a} to the power of {b}")
    return a ** b
print("Let's do some math with just functions!")
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")
#power function
result = power(2,3)
print(f"Power Result: {result}")
#formula
#age = (10 + 3)
output = multiply(age, add(10, 3))
print(f"Output {output}")
#24 + 34 / 100 - 1023
#what1 = add(24, divide(34, subtract(100, 1023)))
#rint("That becomes: ", what1, "Can you do it by hand?")
'''
'''
#ex23.py
import sys
script, input_encoding, error = sys.argv
def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes, "<===>", cooked_string)
languages = open("languages.txt", encoding="utf-8")
main(languages, input_encoding, error)
'''
'''
#ex24.py
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
print("--------------")
print(poem)
print("--------------")
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
start_point = 10000
beans, jars, crates = secret_formula(start_point)
# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")
start_point = start_point / 10
print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
'''
'''
#ex25.py
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
'''
'''
#ex26.py
from sys import argv
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
script, filename = argv
txt = open(filename)
print("Here's your file {filename}:")
print(txt.read())
print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())
print('Let\'s practice everything.')
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
print("--------------")
print(poem)
print("--------------")
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
start_point = 10000
beans, jars, crates = secret_formula(start_point)
# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")
start_point = start_point / 10
print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
people = 20
cats = 30
dogs = 15
if people < cats:
    print("Too many cats! The world is doomed!")
if people > cats:
    print("Not many cats! The world is saved!")
if people < dogs:
    print("The world is drooled on!")
if people > dogs:
    print("The world is dry!")
dogs += 5
if people >= dogs:
    print("People are greater than or equal to dogs.")
if people <= dogs:
    print("People are less than or equal to dogs.")
if people == dogs:
    print("People are dogs.")
'''
'''
#ex29
people = 20
cats = 10
dogs = 15
if people < cats:
    print("Too many cats! The world is doomed!")
if people > cats:
    print("Not many cats! The world is saved!")
if people < dogs:
    print("The world is drooled on!")
if people > dogs:
    print("The world is dry!")
dogs += 5
if people >= dogs:
    print("People are greater than or equal to dogs.")
if people <= dogs:
    print("People are less than or equal to dogs.")
if people == dogs:
    print("People are dogs.")
if not(people == cats):
    print("Cats are not humans.")
'''
'''
#ex30.py
people = 30
cars = 40
trucks = 15
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
'''
'''
#ex31.py
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2 or door #3?""")
door = input("> ")
if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    bear = input("> ")
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    insanity = input("> ")
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
elif door == "3":
    print("Good Choice, Now pick a price")
    print("1. Gold coins")
    print("2. Treasure chest")
    prize = input("> ")
    if prize == "1":
        print("You get 100011 Gold coins, Great Job")
    elif prize == "2":
        print("You get a Treasure chest filled with Dimonds, Great Job")
    else:
        print("It's a trap, You die")
else:
   print("You stumble around and fall on a knife and die. Good job!")
'''
'''
#ex32.py
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")
# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")
# also we can go through mixed lists too
for i in change:
    print(f"I got {i}")
# we can also build lists, first start with an empty one
element = list(range(0,6))
for j in element:
    print(f"My Own Element was: {j}")

elements = []
# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)
# now we can print them out too
for i in elements:
    print(f"Element was: {i}")
'''
'''
#ex33.py
numbers = []
numbers1 = []
def iterate(iteration):
    i = 0
    while i < iteration:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
        
def iterate1(iteration1, inc):
    for i in range(0, iteration1, inc):
        print(f"At the top i is {i}")
        numbers1.append(i)
        print("Numbers now: ", numbers1)
        print(f"At the bottom i is {i}")

iterate(6)
print("The 1numbers: ")
for num in numbers:
    print(num)
iterate1(10,2)
print("The numbers1: ")
for num in numbers1:
    print(num)
'''
'''
#ex35.py
from sys import exit
def gold_room():
    print("This room is full of gold. How much do you take?")
    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    while True:
        choice = input("> ")
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    choice = input("> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    choice = input("> ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
start()
'''
'''
#ex38.py
ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that.")
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
                "Corn", "Banana", "Girl", "Boy"]
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")
print("There we go: ", stuff)
print("Let's do some things with stuff.")
print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar!
'''
'''
#ex39.py
# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
 }

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])
# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])
# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])
# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')
if not state:
    print("Sorry, no Texas.")
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
'''
#ex40.py
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
    def something_else(self):
        print("Do something else")

happy_bday = Song(["Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"])
bulls_on_parade = Song(["They rally around tha family",
    "With pockets full of shells"])
happy_bday_lyrics = ["Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"]
happy_bday1 = Song(happy_bday_lyrics)
another_song = Song(["This is another song......"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
happy_bday1.sing_me_a_song()
another_song.sing_me_a_song()
another_song.something_else()