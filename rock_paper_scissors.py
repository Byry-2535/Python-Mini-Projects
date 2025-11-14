import random

options = ['rock', 'paper', 'scissors']
player_wins = 0
computer_wins = 0
draw = 0

while True:
    player = input('Rock/Paper/Scissors/Q to Quit\n>> ').lower()
    if player == 'q':
        break
    if player not in options:
        print('Invalid Input!')
        continue
    computer = random.choice(options)
    print(f'Computer chose: {computer}')
    if player == computer:
        print('DRAW!')
        draw += 1
    elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
        print('You WON!')
        player_wins += 1
    else:
        print('You LOST!')
        computer_wins += 1
        
print(f'\nPlayer wins: {player_wins}\nComputer wins: {computer_wins}\nDraws: {draw}\n')