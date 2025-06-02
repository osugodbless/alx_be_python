# Prompt user for current weather condition
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Recommend clothing based on user input
if weather == "sunny":
    recommendation = "Wear a t-shirt and sunglasses."
elif weather == "rainy":
    recommendation = "Don't forget your umbrella and a raincoat."
elif weather == "cold":
    recommendation = "Make sure to wear a warm coat and a scarf."
else:
    recommendation = "Sorry, I don't have recommendation for this weather."

# Print the recommendation based on user input
print(recommendation)
