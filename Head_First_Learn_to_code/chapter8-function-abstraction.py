marbles = [10, 13, 39, 14, 41, 9, 3]
print('the total is', sum(marbles))

def compute_sum(list):
    sum = 0
    for number in list:
        sum = sum + number
    return sum
print('The total is', compute_sum(marbles))

def recursive_compute_sum(list):
    if len(list) == 0:
        return 0
    else:
        first = list[0]
        rest = list[1:]
        sum = first + recursive_compute_sum(rest)
        return sum
sum = recursive_compute_sum(marbles)
print('The total is', sum)

# Palindrome (if it comes revers order also same word ada ada)
def is_palindrome(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]:
            return is_palindrome(word[1:-1])
        else:
            return False
words = ['tacocat', 'radar', 'yak', 'rader', 'kayjak']
for word in words:
    print(word, is_palindrome(word))


my_dictionary = {}
my_dictionary['jenny'] = '867-5309'
my_dictionary['paul'] = '555-1201'
my_dictionary['david'] = '321-6617'
my_dictionary['jamie'] = '771-0091'
my_dictionary['paul'] = '443-0000'
phone_number = my_dictionary['jenny']
print(" jenny's number is", phone_number)

my_dictionary['age'] = 27
my_dictionary[42] = 'answer'

my_dictionary['scores'] = [92, 87, 99]
del my_dictionary['david']

if 'jenny' in my_dictionary:
    print("Found her", my_dictionary['jenny'])
else:
    print('I need to get her number')

for key in my_dictionary:
    print(key, ':', my_dictionary[key])

harry = {'firstname': 'Harry',
         'lastname': 'Potter',
         'house': 'Gryffindor',
         'friends': ['Ron', 'Hermione'],
         'born': 1980}
print(my_dictionary)



movies = []  #list
movie = {} #dictionary
movie['name'] = 'Forbidden Planet'
movie['year'] = 1957
movie['rating'] = '*****'
movie['year'] = 1956
movies.append(movie)
movie2 = {'name': 'I was a Teenage Werewolf',
          'year': 1957, 'rating': '****'}
movie2['rating'] = '***'
movies.append(movie2)
movies.append({'name': 'Viking Women and the Sea Serpent',
              'year':1957,
              'rating': '**'})
movies.append({'name': 'Vertigo',
               'year': 1958,
               'rating': '*****'})
print('Head First Movie Recommendations')
print('--------------------------------')
for movie in movies:
    if len(movie['rating']) >= 4:
        print(movie['name'], '(' + movie['rating'] + ')', movie['year'])



names = ['Kim', 'John', 'Josh']
emails = ['kim@oreilly.com', 'john@abc.com', 'josh@wickedlysmart.com']
users = {'Kim': 'kim@oreilly.com',
         'John': 'john@abc.com',
         'Josh': 'josh@wickedlysmart.com'}
users['Avary'] = 'avary@gmail.com'
del users['John']
if 'Josh' in users:
    print("Josh's email address is:", users['Josh'])

email = {'Kim': 'kim@oreilly.com',
         'John': 'john@abc.com',
         'Josh': 'josh@wickedlysmart.com'}
genders = {'Kim': 'f',
         'John': 'm',
         'Josh': 'm'}
attributes = { 'email': 'kim@oreilly.com',
               'gender': 'f',
               'age': 27,
               'friends': ['John', 'Josh']
               }
users = {}
users['Kim'] = attributes
users['John'] = {'email':'john@abc.com', 'gender': 'm', 'age': 24, 'friends': ['Kim','Josh'] }
users['Josh'] = {'email':'josh@wickedlysmart.com', 'gender': 'm', 'age': 32, 'friends': ['Kim'] }



movies = {}
movie = {}

movie['name'] = 'Forbidden Planet'
movie['year'] = 1957
movie['rating'] = '*****'
movie['year'] = 1956

movies['Forbidden Planet'] = movie

movie2 = {'name': 'I Was a Teenage Werewolf',
               'year': 1957, 'rating': '****'}
movie2['rating'] = '***'
movies[movie2['name']] = movie2

movies['Viking Women and the Sea Serpent'] = {'name': 'Viking Women and the Sea Serpent',
                                              'year': 1957,
                                              'rating': '**'}

movies['Vertigo'] =  {'name': 'Vertigo',
                      'year': 1958,
                      'rating': '*****'}

print('Head First Movie Recommendations')
print('--------------------------------')
for name in movies:
    movie = movies[name]
    if len(movie['rating']) >= 4:
        print(movie['name'], '(' + movie['rating'] + ')',  movie['year'])

print('Head First Movie Staff Pick')
print('---------------------------')
movie = movies['I Was a Teenage Werewolf']
print(movie['name'], '(' + movie['rating'] + ')',  movie['year'])



users = {}
users['Kim'] = {'email': 'kim@oreilly.com', 'gender': 'f', 'age': 27, 'friends': ['John', 'Josh']}
users['John'] = {'email': 'john@abc.com', 'gender': 'm', 'age': 24, 'friends': ['Kim', 'Josh']}
users['Josh'] = {'email': 'josh@wickedlysmart.com', 'gender': 'm', 'age': 32, 'friends': ['Kim']}
def average_age(username):
    global users
    user = users[username]
    friends = user['friends']
    sum = 0
    for name in friends:
        friend = users[name]
        sum = sum + friend['age']
    average = sum/len(friends)
    print(username + "'s friends have an average age of", average)
average_age('Kim')
average_age('John')
average_age('Josh')



users = {}
users['Kim'] = {'email': 'kim@oreilly.com', 'gender': 'f', 'age': 27, 'friends': ['John', 'Josh']}
users['John'] = {'email': 'john@abc.com', 'gender': 'm', 'age': 24, 'friends': ['Kim', 'Josh']}
users['Josh'] = {'email': 'josh@wickedlysmart.com', 'gender': 'm', 'age': 32, 'friends': ['Kim']}
max = 1000
for name in users:
    user = users[name]
    friends = user['friends']
    if len(friends) < max:
        most_anti_social = name
        max = len(friends)
    print('The most_anti_social user is', most_anti_social)
