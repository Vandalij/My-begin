n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
operation = input("Enter your operation (+, -, *, /): ")

# if operation == "+":
#     result = n1 + n2
#     print(f"Result: {result}")
# elif operation == "-":
#     result = n1 - n2
#     print(f"Result: {result}")
# elif operation == "*":
#     result = n1 * n2
#     print(f"Result: {result}")
# elif operation == "/":
#     if n2 != 0:
#         result = n1 / n2
#         print(f"Result: {result}")
#     else:
#         print("Error: division by zero!")
# else:
#     print("Unknown operation! Please enter one of the following: +, -, *, /")

####
def calculaotor(n1, n2, operation):
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

result = calculaotor(n1, n2, operation)
print(f"Result: {result}")