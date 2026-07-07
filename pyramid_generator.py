def pyramid(l):
    if l % 2 == 0:
        l += 1

    if l > 101:
        print("\nToo much, defaulting to 101")
        l = 101

    asterisks = 0
    while asterisks <= l:
        print(f"{"*" * (asterisks + 1) : ^{l}}")
        asterisks += 2

pyramid(10)