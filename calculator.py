while True:
    try:
        num1, op, num2 = input("Enter an expression (ex. 1 + 1): ").split()
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid input. Use the format: number operator number")
        continue

    if op == "+":
        print(f"Sum: {num1 + num2:g}")
    elif op == "-":
        print(f"Difference: {num1 - num2:g}")
    elif op == "*":
        print(f"Product: {num1 * num2:g}")
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            continue
        print(f"Quotient: {num1 / num2:g}")
    elif op == "**":
        print(f"Exponent: {num1 ** num2:g}")
    elif op == "//":
        if num2 == 0:
            print("Cannot divide by zero.")
            continue
        print(f"Floor Quotient: {num1 // num2:g}")
    elif op == "%":
        if num2 == 0:
            print("Cannot divide by zero.")
            continue
        print(f"Remainder: {num1 % num2:g}")
    else:
        print("Invalid operator. Use +, -, *, /, //, %, or **")
        continue
    break