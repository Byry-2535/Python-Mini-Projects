def loop(user, iterations):
    for i in range(iterations+1):
        print(f"X{i}: {user:04d}")
        user *= user
        digits = count_digits(user)

        if digits >= 6:
            user = find_middle4(user)
        else:
            user = 0

def count_digits(user):
    count = 0

    while user:
        count += 1
        user //= 10

    return count

def find_middle4(user):
    user //= 100
    return user % 10000

def main():
    while True:
        user = input("Enter a 4 digit number (ex. 1234): ")
        iterations = input("How many iterations?: ")

        if user.isdigit() and iterations.isdigit():
            user = int(user)
            iterations = int(iterations)
            if 999 < user <= 9999:
                break
            else:
                print("Please Input a 4 digit number.")
        else:
            print("Invalid Input.")

    loop(user, iterations)

if __name__ == "__main__":
    main()