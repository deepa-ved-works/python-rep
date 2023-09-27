# Bubble sort swap solution Ascending order
def bubble_sort(scores):
    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(scores)-1):
            if scores[i] > scores[i+1]:
                temp = scores[i]
                scores[i] = scores[i+1]
                scores[i+1] = temp
                swapped = True
scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]
bubble_sort(scores)
print(scores)
smoothies = ['coconut', 'strawberry', 'banana', 'pineapple', 'acai berry', 'mango']
bubble_sort(smoothies)
print(smoothies)


# Bubble sort swap solution Decending order
def bubble_sort(scores):
    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(scores)-1):
            if scores[i] < scores[i+1]:
                temp = scores[i]
                scores[i] = scores[i+1]
                scores[i+1] = temp
                swapped = True

scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]
bubble_sort(scores)
print(scores)

smoothies = ['coconut', 'strawberry', 'banana', 'pineapple', 'acai berry', 'mango']
bubble_sort(smoothies)
print(smoothies)



# Bubble sort swap solution
def bubble_sort(scores, numbers):
    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(scores)-1):
            if scores[i] < scores[i+1]:
                temp = scores[i]
                scores[i] = scores[i+1]
                scores[i+1] = temp
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
                swapped = True

scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]
number_of_scores = len(scores)
solution_numbers = list(range(number_of_scores))
bubble_sort(scores, solution_numbers)
print("Top Bubble Solution")
for i in range(0,5):
    print((i+1),')', 'Bubble solution #', solution_numbers[i], 'score:', scores[i])
    #print('Bubble solution #', solution_numbers[i], 'score:', scores[i])

characters = 'taco'
output = ''
length = len(characters)
i = 0
while(i < length):
    output = output + characters[i]
    i = i+1
length = length * -1
i = -2
while(i >= length):
    output = output + characters[i]
    i = i-1
print(output)



for i in range(0,4):
    for j in range(0,4):
        print(i + j)



for word in ['ox', 'cat', 'lion', 'tiger', 'bobcat']:
    for i in range(2, 7):
        letters = len(word)
        if(letters % i) == 0:
            print(i, word)



full = False
donations = []
full_load = 45
toys = ['robot', 'doll', 'ball', 'slinky']
while not full:
    for toy in toys:
        donations.append(toy)
        size = len(donations)
        if (size >= full_load):
            full = True
print('Full with', len(donations), 'toys')
print(donations)
