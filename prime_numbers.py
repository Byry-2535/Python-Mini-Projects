try:
    number = int(input("Enter a Number: "))
    if number <= 0:
        print("Number must be more than zero.")
    elif number == 1:
        print(f"{number} is not Prime.")
    else:
        for i in range(2, number):
            if number % i == 0:
                print(f"{number} is not Prime.")
                break
        else:
            print(f"{number} is Prime.")
except ValueError:
    print("Please enter a valid integer.")