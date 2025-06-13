FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# 
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

temperature = input("Enter the temperature to convert: ")
unit_of_measurement = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

float_temp = float(temperature)    

if unit_of_measurement == "c":
    print(f"{float_temp}C is {convert_to_fahrenheit(float_temp)}F")

elif unit_of_measurement == "f":
    print(f"{float_temp}F is {convert_to_celsius(float_temp)}C")
elif unit_of_measurement != "c" and unit_of_measurement != "f":
    print("Invalid unit of measurement! Please enter C or F.")
else:
    print("Invalid temperature")

