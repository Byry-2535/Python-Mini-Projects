import random as r

collection = {}
pulls = 100
characters = ["Arlecchino", "Furina", "Hu Tao", "Yoimiya", "Diluc"]
items = {
        "Sword":19.58,
        "Bow":19.58,
        "Shield":19.58,
        "Pistol":19.58,
        "Spellbook":19.58,
        "Qiqi":.1
    }

def choose():
    print("\nChoose your preferred Character:")

    for i, character in enumerate(characters):
        print(f"\t{i+1}. {character}")
    else:
        while True:
            try:
                desired = int(input("Choose: "))
                if desired <= 0:
                    print("Invalid Input!")
                else:
                    items[characters[desired-1]] = 2
                    break
            except Exception:
                print("Invalid Input!")

def prizes():
    print("\nPrizes:")

    for key, value in items.items():
        print(f"\t{key} - {value}%")

def draw(pull):
    if pull <= 0:
        print("\nYou've used all of your Pulls! Try Again.")
    elif pull >= 10:
        print("1x or 10x Draw", end=", ")
        while True:
            try:
                desired = int(input("Select(1 or 10): "))
                if desired == 1:
                    pull -= 1
                    break
                elif desired == 10:
                    pull -= 10
                    break
                else:
                    print("Invalid Input!")
            except Exception:
                print("Invalid Input!")
        gacha(pull, desired)
    elif pull < 10:
        print("1x Draw", end=", ")
        while True:
            try:
                desired = int(input("Select(1 only): "))
                if desired == 1:
                    pull -= 1
                    break
                else:
                    print("Invalid Input!")
            except Exception:
                print("Invalid Input!")
        gacha(pull, desired)

def gacha(pull, x):
    new_items = list(items)
    rates = items.values()

    if x == 1:
        results = r.choices(new_items, weights=rates, k=1)
    elif x == 10:
        results = r.choices(new_items, weights=rates, k=10)

    print(f"You got:", end=" ")

    for index, value in enumerate(results):
        if index == len(results)-1:
            print(value)
        else:
            print(value, end=", ")

    print(f"Balance: {pull}")

    for result in results:
        if result not in collection:
            collection[result] = 1
        elif result in collection:
            if result == new_items[-1]:
                print("Super Lucky! Pull + 10"); pull += 10
                print(f"Balance: {pull}")
            elif result == new_items[-2]:
                print("Diba sabi sayo eh maswerte ka. Pull + 100")
                pull += 100; print(f"Balance: {pull}")

            collection[result] += 1
    draw(pull)

def main():
    while True:
        name = input("Enter your Username: ")

        if name.strip() == "" or name.isdigit():
            print("Invalid Username!")
        else:
            break

    choose()
    prizes()
    draw(pulls)

if __name__ == '__main__':
    main()