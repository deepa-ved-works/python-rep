import ch1text
def compute_redability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    print(text)

compute_redability(ch1text.text)



#Split
lyrics = 'I heard you on the wireless back in fifty two'
words = lyrics.split()
print(words)
for char in lyrics:
    print(char)


def compute_redability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0
    words = text.split()
    total_words = len(words)
    print(words)
    print(total_words, 'words')
compute_redability(ch1text.text)



def count_sentenses(text):
    count = 0
    for char in text:
        if char == '.' or char == ';' or char == '?' or char == '!':
            count = count + 1
    return count
def compute_redability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0
    words = text.split()
    total_words = len(words)
    total_sentences = count_sentenses(text)
    print(total_words, 'words')
    print(total_sentences, 'sentences')
compute_redability(ch1text.text)



smoothies = ['coconut', 'strawberry', 'banana', 'pineapple', 'acai berry']
if('coconut' in smoothies):
    print('Yes, they have coconut!')
else:
    print('Oh well, no coconut today.')
lyrics = 'I heard you on the wireless back in fifty two'
if('wireless' in lyrics):
    print('Yes, they have wireless')
else:
    print('Oh well, no coconut today.')



def count_sentenses(text):
    count = 0
    terminals = '.;?!'
    for char in text:
        if char in terminals:
            count = count + 1
    return count
def compute_redability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0
    words = text.split()
    total_words = len(words)
    total_sentences = count_sentenses(text)
    print(total_words, 'words')
    print(total_sentences, 'sentences')
compute_redability(ch1text.text)



def count_syllables(words):
    count = 0
    for word in words:
        word_count = count_syllables_in_word(word)
        count = count + word_count
        return count
def count_syllables_in_word(word):
    count = 0
    if len(word) <= 3:
        return 1
    vowels = "aeiouAEIOU"
    prev_char_was_vowel = False
    for char in word:
        if char in vowels:
            if not prev_char_was_vowel:
                count = count + 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False
    return count
def compute_redability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0
    words = text.split()
    total_words = len(words)
    total_sentences = count_sentenses(text)
    total_syllables = count_syllables(words)
    print(total_words, 'words')
    print(total_sentences, 'sentences')
    print(total_syllables, 'syllables')
#compute_redability(ch1text.text)



lyrics = 'I heard you on the wireless back in fifty two'
my_substring = lyrics[2:7]
print(my_substring)
my_substring = lyrics[:6]
print(my_substring)
my_substring = lyrics[28:]
print(my_substring)
my_substring = lyrics[28:-1]
print(my_substring)
my_substring = lyrics[-17:]
print(my_substring)



smoothies = ['coconut', 'strawberry', 'banana', 'pineapple', 'acai berry']
print(smoothies[2:4])
print(smoothies[:2])
print(smoothies[3:-1])
str = 'a man a plan panama'
print(str[:])
print(str[:2])
print(str[2:])
print(str[1:7])
print(str[3:-1])
print(str[-2:-1])
print(str[0:-1])
print(str[0:4])


def count_syllables(words):
    count = 0
    for word in words:
        word_count = count_syllables_in_word(word)
        count = count + word_count
        return count
def count_syllables_in_word(word):
    count = 0
    endings = '.,;?!:'
    last_char = word[-1]
    if last_char in endings:
        processed_word = word[0:-1]
    else:
        processed_word = word
    if len(processed_word) <= 3:
        return 1
    if processed_word[-1] in 'eE':
        processed_word = processed_word[0:-1]
    vowels = "aeiouAEIOU"
    prev_char_was_vowel = False
    for char in processed_word:
        if char in vowels:
            if not prev_char_was_vowel:
                count = count + 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False
    if processed_word[-1] in 'yY':
        count = count + 1
    return count
def count_sentenses(text):
    count = 0
    terminals = '.;?!'
    for char in text:
        if char in terminals:
            count = count + 1
    return count
def output_results(score):
    if score >= 90:
        print('Reading level of 5th Grade')
    elif score >= 80:
        print('Reading level of 6th Grade')
    elif score >= 70:
        print('Reading level of 7th Grade')
    elif score >= 60:
        print('Reading level of 8-9th Grade')
    elif score >= 50:
        print('Reading level of 10-12th Grade')
    elif score >= 30:
        print('Reading level of College Student')
    else:
        print('Reading level of College Graduate')
def compute_redability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0
    words = text.split()
    total_words = len(words)
    total_sentences = count_sentenses(text)
    total_syllables = count_syllables(words)
    score = (206.835 - 1.015 * (total_words / total_sentences)
             -84.6 * (total_syllables / total_words))
    output_results(score)
compute_redability(ch1text.text)