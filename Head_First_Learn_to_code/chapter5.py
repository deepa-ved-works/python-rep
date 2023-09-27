dog_name = "Codie"
dog_weight = 40
if dog_weight > 20:
    print(dog_name, 'says WOOF WOOF')
else:
    print(dog_name, 'says woof woof')
dog_name = "Sparky"
dog_weight = 9
if dog_weight > 20:
    print(dog_name, 'says WOOF WOOF')
else:
    print(dog_name, 'says woof woof')
dog_name = "Jackson"
dog_weight = 12
if dog_weight > 20:
    print(dog_name, 'says WOOF WOOF')
else:
    print(dog_name, 'says woof woof')
dog_name = "Fido"
dog_weight = 65
if dog_weight > 20:
    print(dog_name, 'says WOOF WOOF')
else:
    print(dog_name, 'says woof woof')



def bark(name, weight):
    if weight > 20:
        print(name, 'says WOOF WOOF')
    else:
        print(name, 'says woof woof')
print("\nI'm a Function")
print('Get those dogs ready')
bark('Codie', 42)
bark('Sparky', 9)
bark('Jackson', 12)
bark('Fido', 66)
bark('Speedy', 20)
bark('Barnaby', -1)
bark('Scottie', 0)
bark('Rover', 21)
print("Okey, we're all done")



def how_should_I_get_there(miles):
    if miles >= 120.0:
        print('Take a plane')
    elif miles >= 2.0:
        print('Take a car')
    else:
        print('Walk')
how_should_I_get_there(800.3)
how_should_I_get_there(2.0)
how_should_I_get_there(.5)



#Return value
def get_bark(weight):
    if weight > 20:
        return 'WOOF WOOF'
    else:
        return 'woof woof'
codies_bark = get_bark(40)
print("Codie's bark is", codies_bark)
print(get_bark(20))



def make_greeting(name):
    return 'Hi ' + name + '!'
print(make_greeting("Speedy"))




def compute(x, y):
    total = x + y
    if(total > 10):
        total = 10
    return total
print(compute(2, 3))
print(compute(11, 3))



def allow_access(person):
    if person == 'Dr Evil':
        answer = True
    else:
        answer = False
    return answer
print(allow_access("Codie"))
print(allow_access('Dr Evil'))




hair = input("What color hair [brown]? ")
if hair == '':
    hair = 'brown'
print('You chose', hair)
hair_length = input("What hair length [short]? ")
if hair_length == '':
    hair_length = 'short'
print('You chose', hair_length)
eyes = input("What eye color [blue]? ")
if eyes == '':
    eyes = 'blue'
print('You chose', eyes)
gender = input("What gender [female]? ")
if gender == '':
    gender = 'female'
print('You chose', gender)
has_glasses = input("Has glasses [no]? ")
if has_glasses == '':
    has_glasses = 'no'
print('You chose', has_glasses)
has_beard = input("Has beard [no]? ")
if has_beard == '':
    has_beard = 'no'
print('You chose', has_beard)




def get_attribute(query, default):
    question = query + ' [' + default + ']? '
    answer = input(question)
    if (answer == ''):
        answer = default
    print('You chose', answer)
hair = get_attribute('What hair color', 'brown')
hair_length = get_attribute('What hair length', 'short')
eyes = get_attribute('What eye color', 'blue')
gender = get_attribute('What gender', 'female')
has_glasses = get_attribute('Has glasses', 'no')
has_beard = get_attribute('Has beard', 'no')




def drink_me(param):
    msg = 'Drinking ' + param + ' glass'
    print(msg)
    param = 'empty'
glass = 'full'
drink_me(glass)
print('The glass is', glass)




greeting = 'Greetings'
def greet(name, message):
    global greeting
    greeting = 'Hi'
    print(greeting, name + '.', message)
greet('June', 'See you soon!')
print(greeting)



def greet(name, message='You rule!'):
    print('Hi', name + '.', message)
greet('John')
greet('Jennifer', 'How are you today?')



def greet(name, emoticon, message='You rule!'):
    print('Hi', name + '.', message, emoticon)
greet(message='Where have you been?', name='Jill', emoticon='Thumbs up')
greet('Betty', message='Yo!', emoticon=':)')



def make_sundae(ice_cream='vanilla', sauce='chocolate', nuts=True,
                banana=True, brownies=False, whipped_cream=True):
    recipe = ice_cream + ' ice cream and ' + sauce + ' sauce '
    if nuts:
        recipe = recipe + 'with nuts and '
    if banana:
        recipe = recipe + 'a banana and '
    if brownies:
        recipe = recipe + 'a brownie and '
    if not whipped_cream:
        recipe = recipe + 'no '
    recipe = recipe + 'whipped cream on top.'
    return recipe
sundae = make_sundae()
print('One sundae coming up with', sundae)
sundae = make_sundae('chocolate')
print('One sundae coming up with', sundae)
sundae = make_sundae(sauce='caramel', whipped_cream=False, banana=False)
print('One sundae coming up with', sundae)
sundae = make_sundae(whipped_cream=False, banana=True,
                        brownies=True, ice_cream='peanut butter')
print('One sundae coming up with', sundae)



balance = 10500
camera_on = True
def steal(balance, amount):
    global camera_on
    camera_on = False
    if(amount < balance):
        balance = balance - amount
    return amount
    camera_on = True
proceeds = steal(balance, 1250)
print('Criminal: you stole', proceeds)