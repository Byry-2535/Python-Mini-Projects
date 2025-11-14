import random

def roll():
    value = random.randint(1, 6)
    return value

while True:
    players = input('Enter the number of players (2 - 4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('Player must be between 2 and 4. Try Again')
            continue
    else:
        print('Invalid!')
        continue
    
players_list = [0 for _ in range(players)]
target_score = 10
while max(players_list) < target_score:
    for i in range(players):
        print(f'\nPlayer {i+1}\'s turn')
        print(f'Total Score: {players_list[i]}\n')
        current_score = 0
        while True:
            choice = input('Roll? (y/n): ').lower()
            if choice == 'y':
                value = roll()
                print(f'You rolled a {value}')
                if value == 1:
                    current_score = 0
                    print('return 0;')
                    break
                else:
                    current_score += value
            elif choice == 'n':
                break
            else:
                print('Invalid!')
                continue
            print(f'Current Score: {current_score}')
        players_list[i] += current_score
        print(f'Total Score: {players_list[i]}')

target_score = max(players_list)        
winner = players_list.index(target_score)
print(f'\nPlayer {winner+1} Wins.\nScore: {target_score}')