import random

while True:
    number = input('Enter a Number: ')
    if number.isdigit():
        number = int(number)
        break
    else:
        print('Invalid!')
        continue
random_number = random.randint(0, number)
attemps = 0

print('Guess')
while True:
    guess = input('>> ')
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Invalid! Guess again')
        continue
    if guess == random_number:
        print('Correct!')
        attemps += 1
        break
    elif guess > random_number:
        print('Lower')
    else:
        print('Higher')
    attemps += 1
print(f'You guessed it in {attemps} attemps.\n')