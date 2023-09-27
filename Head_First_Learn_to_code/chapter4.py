#Lists
scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54]
score = scores[3]
print('Solution #3 produced', score, 'bubbles.'  )

smoothies = ['coconut', 'strawberry', 'banana', 'pineapple', 'acai berry']
print(smoothies)
favorite = smoothies[2]
print(favorite)
smoothies[3] = 'tropical'
print(smoothies)
#length of smoothies
length = len(smoothies)
print(length)
#select last one
last = smoothies[length-1]
print(last)
last = smoothies[-1]
print(last)
second_last = smoothies[-2]
print(second_last)
third_last = smoothies[-3]
print(third_last)



eighties = ['', 'duran duran', 'B-52s', 'muse']
newwave = ['flock of seagulls', 'postal service']
remember = eighties[1]
eighties[1] = 'culture club'
band = newwave[0]
eighties[3] = band
eighties[0] = eighties[2]
eighties[2] = remember
print(eighties)



charactors = ['t', 'a', 'c', 'o']
output = ''
length = len(charactors)
i = 0
while(i < length):
    output = output + charactors[i]
    i = i + 1
length = length * -1
i = -2
while(i >= length):
    output = output + charactors[i]
    i = i - 1
print(output)



charactors = ['w', 'a', 's', 'i', 't', 'a', 'r']
output = ''
length = len(charactors)
i = 0
while(i < length):
    output = output + charactors[i]
    i = i + 1
length = length * -1
i = -2
while(i >= length):
    output = output + charactors[i]
    i = i - 1
print(output)



charactors = ['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c']
output = ''
length = len(charactors)
i = 0
while(i < length):
    output = output + charactors[i]
    i = i + 1
length = length * -1
i = -2
while(i >= length):
    output = output + charactors[i]
    i = i - 1
print(output)



#Bobble solution (While loop)
scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]
i = 0
length = len(scores)
while i < length:
    print('Bobble solution #' +str(i), 'score:', scores[i])
    i = i + 1



#For loop
scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]
i = 0
length = len(scores)
for i in range(length):
    print('Bobble solution #' +str(i), 'score:', scores[i])
    i = i + 1



#Smoothies has coconut
smoothies = ['coconut', 'strawberry', 'banana', 'tropical', 'acai berry']
has_coconut = [True, False, False, True, False]
i = 0
while i < len(has_coconut):
    if has_coconut[i]:
        print(smoothies[i], 'contains coconut')
    i = i + 1



smoothies = ['coconut', 'strawberry', 'banana', 'tropical', 'acai berry']
for smoothie in smoothies:
    output = 'We serve ' + smoothie
    print(output)



for i in range(5):
    print('Iterating through', i)


smoothies = ['coconut', 'strawberry', 'banana', 'tropical', 'acai berry']
length = len(smoothies)
for i in range(length):
    print('Smoothie #', i, smoothies[i])


print(list(range(5)))
print(list(range(5, 10)))
print(list(range(3, 10, 2)))
print(list(range(10, 0, -1)))
print(list(range(-10, 2)))



#Bubble solution
scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]
high_score = 0
length = len(scores)
for i in range(length):
    print('Bobble solution #' +str(i), 'score:', scores[i])
    if scores[i] > high_score:
        high_score = scores[i]
print('Bubble tests:', length)
print('Highest bubble score:', high_score)
best_solutions = []
for i in range(length):
    if high_score == scores[i]:
        best_solutions.append(i)
print('Solution with highest score:', best_solutions)


menu = ['Pizza', 'Pasta', 'Soup', 'Salad']
print(menu)
menu = []
menu.append('Burger')
menu.append('Sushi')
print(menu)
del menu[0]
print(menu)
menu.extend(['BBQ', 'Tacos'])
print(menu)
menu = menu + ['BBQ', 'Tacos']
print(menu)
menu.insert(1, 'Stir Fry')
print(menu)



#Bubble solution
scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]
costs = [.25, .27, .25, .25, .25, .25, .33, .31, .25, .29, .27, .22,
         .31, .25, .25, .33, .21, .25, .25, .25, .28, .25, .24, .22,
         .20, .25, .30, .25, .24, .25, .25, .25, .27, .25, .25, .29]
high_score = 0
length = len(scores)
for i in range(length):
    print('Bobble solution #' +str(i), 'score:', scores[i])
    if scores[i] > high_score:
        high_score = scores[i]
print('Bubble tests:', length)
print('Highest bubble score:', high_score)
best_solutions = []
for i in range(length):
    if high_score == scores[i]:
        best_solutions.append(i)
print('Solution with highest score:', best_solutions)
cost = 100.0
most_effective = 0
for i in range(length):
    if scores[i] == high_score and costs[i] < cost:
        most_effective = i
        cost = costs[i]
print('Solution', most_effective, 'is the most effictive with a cost of', costs[most_effective])



#Bubble solution
scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]
costs = [.25, .27, .25, .25, .25, .25, .33, .31, .25, .29, .27, .22,
         .31, .25, .25, .33, .21, .25, .25, .25, .28, .25, .24, .22,
         .20, .25, .30, .25, .24, .25, .25, .25, .27, .25, .25, .29]
high_score = 0
length = len(scores)
for i in range(length):
    print('Bobble solution #' +str(i), 'score:', scores[i])
    if scores[i] > high_score:
        high_score = scores[i]
print('Bubble tests:', length)
print('Highest bubble score:', high_score)
best_solutions = []
for i in range(length):
    if high_score == scores[i]:
        best_solutions.append(i)
print('Solution with highest score:', best_solutions)
cost = 100.0
most_effective = 0
for i in range(len(best_solutions)):
    index = best_solutions[i]
    if cost > costs[index]:
        most_effective = index
        cost = costs[index]
print('Solution', most_effective, 'is the most effective with a cost of', costs[most_effective])