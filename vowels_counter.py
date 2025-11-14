vowels = 'aeiou'

def count_vowels(word):
    counter = 0
    for i in word.lower():
        if i in vowels:
            counter += 1
    return counter

while True:
    word = input('Enter a word/sentece/phrase or q to quit: ')
    if word.lower() == 'q':
        break
    vowels_counter = count_vowels(word)
    print(f'Vowels: {vowels_counter}')