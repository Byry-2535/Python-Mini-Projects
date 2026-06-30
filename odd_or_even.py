while True:
    number = input("Enter a Number: ")

    if number.isdigit():
        number = int(number)
        print("Odd" if number % 2 == 1 else "Even")
    elif number.lower() == "q":
        break
    else:
        continue