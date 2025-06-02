# Prompt user for two integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Prompt user for operation type
operation = input("Choose the operation (+, -, *, /): ")

# Perform calculation based on operation
match operation:
    case operator if operation == "+":
        result  = num1 + num2

    case operator if operation == "-":
        result = num1 - num2

    case operator if operation == "*":
        result = num1 * num2

    case operator if operation == "/": 
        if num2 == 0: result = "Cannot divide by zero"
        else: result = num1 / num2
    
    case _:
        result = "Please enter a valid operator"
print("The result is", result)
