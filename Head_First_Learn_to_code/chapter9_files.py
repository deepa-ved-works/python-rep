#Read file
my_file = open('lib.txt', 'r')
my_text = my_file.read()
print(my_text)
my_file.close()



'''
for i in range(0, 1000):
    filename = str(i) + '.txt'
    file = open(filename, 'r')
    text = file.read()
    if 'needle' in text:
        print('Found needle in file' + str(i) + '.txt')
        break
    file.close()
print('Scan complete')
'''


#Read fist 2 lines
my_file = open('lib.txt', 'r')
line1 = my_file.readline()
print(line1)
line2 = my_file.readline()
print(line2)



#New line
print('Ger ready for new lines:\n\n\n\n\n\n')


#use while loop read last line
my_file = open('lib.txt', 'r')
while True:
    line = my_file.readline()
    if line != '':
        print(line)
    else:
        break
my_file.close()



#use for loop read last line
my_file = open('lib.txt', 'r')
for line in my_file:
    print(line)
my_file.close()




def make_crazy_lib(filename):
    file = open(filename, 'r')
    text = ''
    for line in file:
        text = text + process_line(line) + '\n'
    file.close()
    return text
placeholders = ['NOUN', 'ADJECTIVE', 'VERB_ING', 'VERB']
def process_line(line):
    global placeholders
    processed_line = ''
    words = line.split()
    for word in words:
        stripped = word.strip('.,;?!')
        if stripped in placeholders:
            answer = input('Enter a ' + stripped + ":")
            processed_line = processed_line + answer
            if word[-1] in '.,;?!':
                processed_line = processed_line + word[-1] + ' '
            else:
                processed_line = processed_line + word + ' '
        else:
            processed_line = processed_line + word + ' '
    return processed_line + '\n'

def main():
    lib = make_crazy_lib('lib.txt')
    print(lib)
if __name__ == '__main__':
    main()



