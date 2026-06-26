def calculator():
    print("--- Simple Calculator ---")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
        return

    print("\nSelect an operation:")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")

    operation = input("Enter your choice (+, -, *, /): ").strip()

    if operation == "+":
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")
    elif operation == "/":
        if num2 == 0:
            print("\nError: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nError: Invalid operation selected.")

calculator()
