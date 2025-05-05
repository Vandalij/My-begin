def calculator(n1, n2, operation):
    match operation:
        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case "*":
            return n1 * n2
        case "/":
            if n2 != 0:
                return n1 / n2
            else:
                return "Error: division by zero!"
        case _:
            return "Unknown operation! Please enter one of the following: +, -, *, /"

while True:
    try:
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        operation = input("Enter your operation (+, -, *, /): ")
        result = calculator(n1, n2, operation)
        print(f"Result: {result}")
    except ValueError:
        print("Please enter valid integers!")

    cont = input("Do you want to continue? (y/n): ").lower()
    if cont != "y":
        print("Calculator finished.")
        break

