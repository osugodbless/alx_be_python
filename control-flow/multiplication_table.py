# Prompt user to enter a number
number = int(input("Enter a number to see its multiplication table: "))

# Print a multiplication table based on users input
for i in range(1, 11):
    product = number * i
    print(f"{number} X {i} = {product}")
