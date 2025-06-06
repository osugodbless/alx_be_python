# Initialize number to 1
number = 1
# Prompt user to enter a number
user_input_number = int(input("Enter the size of the pattern: "))

# Outer loop to iterate through each row
while number <= user_input_number:
    # Inner loop to print asterisks side by side
    for i in range(user_input_number):
        print("*", end="")
    number = number + 1
    print()
