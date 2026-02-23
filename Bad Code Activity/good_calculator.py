def add(a, b):
    """Returns the sum of two numbers"""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers"""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers"""
    return a * b


def divide(a, b):
    """Returns the quotient of two numbers"""
    if b == 0:
        print("Cannot divide by zero")
    else:
        return a / b


def get_numbers():
    """Prompts the user for two numbers and returns them"""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input, please enter numeric values")
        return get_numbers()


def main():
    """Main loop"""
    operations = {
        "1": add,
        "2": subtract,
        "3": multiply,
        "4": divide
    }

    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "5":
            print("Goodbye")
            break

        if choice in operations:
            a, b = get_numbers()
            try:
                result = operations[choice](a, b)
                print(f"Result: {result}")
            except ValueError as e:
                print(e)
        else:
            print("Invalid selection")


if __name__ == "__main__":
    main()

