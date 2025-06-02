# Prompt user for two integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Prompt user for operation type
operation = input("Choose the operation (+, -, *, /): ")

#
match num1:
    case number if operation == "+":
        result  = number + num2

    case number if operation == "-":
        result = number - num2

    case number if operation == "*":
        result = number * num2

    case number if operation == "/": 
        if num2 == 0: result = "Cannot divide by zero"
        else: result = number / num2
    case _:
        result = "Please enter a valid operator"
print(result)
