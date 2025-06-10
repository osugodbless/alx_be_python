def perform_operation(num1, num2, operation):
    if operation == "add":
        result = num1 + num2
    elif operation == "substract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2
    else:
        result = "You entered an invalid operation. Please try again!"
    return result
