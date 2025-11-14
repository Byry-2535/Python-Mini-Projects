def create():
    username = input('Username: ')
    password = input('Password: ')
    with open('accounts.txt', 'a') as a:
        a.write(f'{username}|{password} \n')
        
def view():
    with open('accounts.txt', 'r') as r:
        for line in r.readlines():
            data = line.strip()
            user, passw = data.split('|')
            print(f'Username: {user} | Password: {passw}')
            
while True:
    print('1. Create 2. View 3. Quit')
    option = input('>> ')
    if option == '1':
        create()
    elif option == '2':
        view()
    elif option == '3':
        quit()
    else:
        print('Invalid Input!')
        continue