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



def is_palindrome(word):
    i = 0
    j = len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i = i + 1
        j = j - 1
    return True
words = ['tacocat', 'radar', 'yak', 'rader', 'kayjak', 'aka']
for word in words:
    print(word, is_palindrome(word))
