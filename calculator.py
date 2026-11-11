def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    if second == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return first / second


def main():
    operations = {
        "1": ("Add", add),
        "2": ("Subtract", subtract),
        "3": ("Multiply", multiply),
        "4": ("Divide", divide),
    }

    while True:
        print("\nCalculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        if choice not in operations:
            print("Invalid option. Please choose a number from 1 to 5.")
            continue

        try:
            first = float(input("Enter the first number: "))
            second = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        operation_name, operation = operations[choice]
        try:
            result = operation(first, second)
        except ZeroDivisionError as error:
            print(error)
            continue

        print(f"{operation_name} result: {result}")


if __name__ == "__main__":
    main()

def modulus(first, second):
    return first % second