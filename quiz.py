print('Simple Quiz Game\n')

while True:
    choice = input('1. Play\n2. Exit\n>> ')
    if choice.isdigit():
        choice = int(choice)
    else:
        print('Invalid Input!')
        continue
    if choice == 2:
        quit()
    elif choice != 1:
        print('Invalid!')
    else:
        break
questions = {'CPU Stands for?':'central processing unit', 'GPU stands for?':'graphics processing unit', 'RAM stand for?':'random access memory'}
score = 0

for k, v in enumerate(questions):
    print(f'Question No. {k+1}:\n{v}')
    answer = input('>> ').lower()
    if answer == questions[v]:
        score += 1
        
print(f'\nYour Score: {score}/{len(questions)}\n')